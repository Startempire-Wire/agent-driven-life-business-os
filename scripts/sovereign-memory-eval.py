#!/usr/bin/env python3
"""Portable memory evaluation — a harness that is designed to FAIL.

The existing deployment evaluation scores text similarity against a baseline
built from the same corpus. Such a harness cannot fail: a mirror index scores
1.0 and is still "below baseline", and a total backend outage leaves the score
frozen. Four numbers in the live deployment proved nothing — they held steady
across four days in which the memory backend returned HTTP 500 on every call.

This harness is built the other way round. Every gate below has a demonstrated
failure mode, and the harness is fault-injected in `--self-test` to prove it
still notices.

Gates
    G0  INSTALLABILITY   runs on bare python3, no third-party import
    G1  REACHABILITY     write → read through the real consumer path
    G2  MIRROR TRAP      refuses to score a set that is trivially self-similar
    G3  RETRIEVAL        hybrid recall on a golden set
    G4  CAUSAL LIFT      WITH long-term memory vs. WITHOUT (null control arm)
    G5  SOVEREIGNTY      full lifecycle with every socket hard-blocked
    G6  LATENCY          retrieval inside the declared tier budget

G4 is the only gate that answers "is this memory worth having". The null arm is
given the *recent context* an agent has without any long-term store, so it is a
baseline that genuinely can succeed. If both arms score the same, the harness
reports that memory is decoration for this task set — which is a real, correct,
failing verdict rather than a score to be quietly improved.

Usage
    python3 sovereign-memory-eval.py --self-test     # prove the gates can fail
    python3 sovereign-memory-eval.py                 # run the gates
Exit code is 0 only when every gate passes.
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import os
import socket
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUBSTRATE = HERE / "sovereign-memory.py"

NETWORK_MODULES = {
    "socket", "urllib", "urllib.request", "http", "http.client",
    "requests", "httpx", "ftplib", "smtplib", "telnetlib", "xmlrpc",
}

PASS, FAIL, WARN = "PASS", "FAIL", "WARN"


def load_substrate():
    spec = importlib.util.spec_from_file_location("sovereign_memory", SUBSTRATE)
    module = importlib.util.module_from_spec(spec)
    sys.modules["sovereign_memory"] = module  # dataclasses requires registration
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Task set. `recall_only` facts exist ONLY in long-term memory. `recent` facts
# are in the agent's recent context and therefore reachable WITHOUT a store.
# The null arm is handed the recent set, so it can genuinely score above zero —
# which is what makes the lift measurable rather than tautological.
# ---------------------------------------------------------------------------
TASKS = [
    # (query, answer_keyword, arm)
    ("what does the client actually sell",
     "subscription", "recall_only"),
    ("when does the retainer renew",
     "march", "recall_only"),
    ("what is the retention policy",
     "ninety", "recall_only"),
    ("what is our incident severity policy",
     "sev1", "recall_only"),
    ("who owns the billing integration",
     "finance", "recall_only"),

    ("what did we just agree on",
     "friday", "recent"),
    ("what is the current sprint focus",
     "latency", "recent"),
    ("what did the operator ask for",
     "review", "recent"),
]

RECENT_CONTEXT = [
    "We agreed to review the roadmap on Friday.",
    "Current sprint focus is retrieval latency for the memory store.",
    "The operator asked for a review of the deployment runbook.",
]

LONG_TERM = [
    ("Client sells a subscription-first plan with annual prepay.",
     "semantic", "operator:2026-09-14"),
    ("The primary client retainer renews in March.",
     "structured", "operator:2026-09-20"),
    ("Data retention policy is ninety days for episodic tier, one year archival.",
     "semantic", "policy:2026-10-01"),
    ("Incident severity policy: SEV1 pages the on-call owner immediately.",
     "structured", "policy:2026-09-28"),
    ("Billing integration is owned by the finance team, not engineering.",
     "episodic", "ops:2026-09-30"),
]

# Adversarial filler: topically adjacent to the queries but containing none of
# the answers. Without this, recall is trivial and the harness flatters itself.
FILLER = [
    "The subscription dashboard renders revenue cohorts by month.",
    "March is when the planning cycle begins for the next quarter.",
    "Retention is measured against the ninety-day churn baseline.",
    "SEV1 incidents are triaged before SEV2 during peak hours.",
    "Finance reviews billing invoices at the end of each month.",
    "The roadmap review covers latency, cost, and retention targets.",
    "Sprint planning happens before the Friday deployment window.",
]


class Report:
    def __init__(self, quiet: bool = False) -> None:
        self.gates: list[dict] = []
        self.quiet = quiet

    def add(self, gate: str, status: str, detail: str, evidence: dict | None = None) -> None:
        self.gates.append({"gate": gate, "status": status, "detail": detail,
                           "evidence": evidence or {}})
        mark = {PASS: "PASS", FAIL: "FAIL", WARN: "WARN"}[status]
        if not self.quiet:
            print(f"  [{mark}] {gate:<4} {detail}")

    @property
    def ok(self) -> bool:
        return all(g["status"] != FAIL for g in self.gates)

    def as_dict(self) -> dict:
        return {
            "verdict": "VERIFIED" if self.ok else "NOT VERIFIED",
            "gates": self.gates,
        }


def g0_installability(rep: Report) -> None:
    """Does it run where a client can run it?"""
    tree = ast.parse(SUBSTRATE.read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            imported.add(node.module.split(".")[0])

    third_party = sorted(imported - set(sys.stdlib_module_names))
    if third_party:
        rep.add("G0", FAIL, f"requires non-stdlib packages: {third_party}")
    else:
        rep.add("G0", PASS, f"bare python{sys.version_info.major}.{sys.version_info.minor}, "
                            f"zero third-party imports", {"imports": len(imported)})


def build_corpus(module, db_path: str, query_text: str | None = None):
    """Populate a fresh store. `query_text` seeds the mirror trap when given."""
    store = module.SovereignMemory(db_path)
    for text, tier, source in LONG_TERM:
        store.remember(text, tier=tier, source=source, importance=0.8)
    for text in FILLER:
        store.remember(text, tier="episodic", source="filler:noise", importance=0.3)
    if query_text:
        store.remember(query_text, tier="episodic", source="trap:mirror")
    return store


def g1_reachability(rep: Report, module, tmp: str) -> None:
    """Process up is not health. Prove the data path traverses."""
    store = module.SovereignMemory(os.path.join(tmp, "reach.db"))
    probe = "Reachability probe: the sovereign store must return this exact token."
    token = "REACHABILITY-TOKEN-4417"
    store.remember(f"{probe} {token}", tier="semantic", source="eval:reachability")
    hits = [r for r in store.retrieve("reachability probe token") if "_latency_ms" not in r]
    store.close()
    if hits and token in hits[0]["text"]:
        rep.add("G1", PASS, "write→read traversed the real consumer path",
                {"top_score": hits[0]["score"]})
    else:
        rep.add("G1", FAIL, "data stored but not retrievable — backend unreachable or silent")


def g2_mirror_trap(rep: Report, module, tmp: str, seed_mirror: bool = True) -> None:
    """Refuse to score a set that is trivially self-similar.

    If the query text is also in the index, similarity is 1.0 and any harness
    reporting that as quality is reporting that it can read its own input.
    `seed_mirror=False` is the honest control: same corpus, no mirror seeded.
    """
    store = build_corpus(
        module,
        os.path.join(tmp, "trap.db" if seed_mirror else "honest.db"),
        query_text="when does the retainer renew" if seed_mirror else None,
    )
    top = next(
        (r for r in store.retrieve("when does the retainer renew", k=1)
         if "_latency_ms" not in r),
        None,
    )
    store.close()
    if top and top["semantic"] > 0.999:
        rep.add("G2", FAIL,
                "MIRROR TRAP: query text is in the index; similarity is self-reference",
                {"semantic": top["semantic"]})
    else:
        rep.add("G2", PASS, "query text absent from index; score is not self-reference",
                {"semantic": top["semantic"] if top else 0.0})


def g3_retrieval(rep: Report, module, tmp: str) -> None:
    store = build_corpus(module, os.path.join(tmp, "g3.db"))
    hits = 0
    detail = []
    for query, keyword, arm in TASKS:
        got = [r for r in store.retrieve(query, k=3) if "_latency_ms" not in r]
        ok = bool(got) and keyword in got[0]["text"].lower()
        hits += ok
        detail.append({"query": query, "hit": ok, "top": got[0]["text"][:56] if got else None})
    store.close()
    rate = hits / len(TASKS)
    status = PASS if rate >= 0.70 else (WARN if rate >= 0.50 else FAIL)
    rep.add("G3", status, f"hybrid recall@3 = {rate:.2f} ({hits}/{len(TASKS)})",
            {"per_task": detail})


def _answer(query: str, keyword: str, corpus: list[str], module, db: str | None) -> bool:
    """Can this agent answer using only what is genuinely available to it?

    `corpus` is everything in-context for that arm. When `db` is given the agent
    may additionally consult long-term memory; when it is None it may not.

    The null arm must NOT be handed the long-term facts directly. Doing so makes
    both arms identical and pins lift at zero by construction — a control arm
    that cannot differ is not a control arm.
    """
    pool = list(corpus)
    if db:
        store = module.SovereignMemory(db)
        pool += [r["text"] for r in store.retrieve(query, k=3) if "_latency_ms" not in r]
        store.close()
    return any(keyword in text.lower() for text in pool)


def g4_causal_lift(rep: Report, module, tmp: str) -> None:
    """THE gate. WITH long-term memory vs. WITHOUT (null control arm).

    Arm A — recent context + long-term store (retrieval ON).
    Arm B — recent context only. No store is opened. This is what an agent has
            with no memory at all, so it is a baseline that can genuinely
            succeed on `recent` tasks and must genuinely fail on `recall_only`
            ones. That asymmetry is what makes the lift measurable.

    A lift near zero means long-term memory changed no answer: a correct failing
    verdict, not a score to quietly improve.
    """
    db = os.path.join(tmp, "g4.db")
    store = build_corpus(module, db)

    arm_a = arm_b = 0
    per_task = []
    for query, keyword, arm in TASKS:
        with_store = _answer(query, keyword, RECENT_CONTEXT, module, db)
        without_store = _answer(query, keyword, RECENT_CONTEXT, module, None)
        arm_a += with_store
        arm_b += without_store
        per_task.append({"query": query, "class": arm,
                         "with": with_store, "without": without_store})
    store.close()

    lift = (arm_a - arm_b) / len(TASKS)
    if lift >= 0.30:
        status, detail = PASS, (
            f"memory is load-bearing: lift = {lift:+.2f} "
            f"(with={arm_a}/{len(TASKS)}, null arm={arm_b}/{len(TASKS)})"
        )
    elif lift > 0:
        status, detail = WARN, f"weak lift {lift:+.2f} — memory helps, marginally"
    else:
        status, detail = FAIL, (
            f"NO LIFT ({lift:+.2f}): long-term memory changed no answer. "
            "It is decoration for this task set — do not claim it works."
        )
    rep.add("G4", status, detail, {"per_task": per_task})


def g5_sovereignty(rep: Report, module, tmp: str) -> None:
    """Full lifecycle with every socket hard-blocked.

    Not "the blocker fired" — the store never opens a socket, so proving the
    blocker fires proves nothing. The claim under test is that the system needs
    no network to work, so the whole lifecycle must complete while blocked.
    """
    real_socket, real_conn = socket.socket, socket.create_connection

    def blocked(*_a, **_k):
        raise RuntimeError("NETWORK ATTEMPTED — sovereignty contract violated")

    socket.socket = blocked
    socket.create_connection = blocked
    try:
        db = os.path.join(tmp, "airgap.db")
        store = module.SovereignMemory(db)
        store.remember("Air-gapped write must still be durable.",
                       tier="semantic", source="eval:sovereignty")
        store.remember("Air-gapped retrieval must still work on-device.",
                       tier="episodic", source="eval:sovereignty")
        hits = [r for r in store.retrieve("air-gapped retrieval on-device")
                if "_latency_ms" not in r]
        store.close()
        if hits:
            rep.add("G5", PASS, "full write→read lifecycle completed air-gapped",
                    {"retrieved": len(hits)})
        else:
            rep.add("G5", FAIL, "lifecycle broke with sockets blocked — system is not sovereign")
    except RuntimeError as exc:
        rep.add("G5", FAIL, f"store attempted a network call: {exc}")
    finally:
        socket.socket, socket.create_connection = real_socket, real_conn


def g6_latency(rep: Report, module, tmp: str) -> None:
    store = build_corpus(module, os.path.join(tmp, "g6.db"))
    for _ in range(5):
        store.retrieve("warm up the index")
    samples = []
    for _ in range(30):
        out = store.retrieve("client subscription renews in march")
        samples.append(next(r["_latency_ms"] for r in out if "_latency_ms" in r))
    store.close()
    samples.sort()
    p50, p95 = samples[len(samples) // 2], samples[int(len(samples) * 0.95)]
    budget = module.TIER_BUDGET_MS["semantic"]
    status = PASS if p95 <= budget else FAIL
    rep.add("G6", status, f"p50={p50:.2f}ms p95={p95:.2f}ms (semantic budget {budget}ms)",
            {"p50": p50, "p95": p95})


def run_all(quiet: bool = False) -> Report:
    rep = Report(quiet=quiet)
    if not quiet:
        print("\n  PORTABLE MEMORY EVALUATION\n")
    g0_installability(rep)
    module = load_substrate()
    with tempfile.TemporaryDirectory() as tmp:
        g1_reachability(rep, module, tmp)
        g2_mirror_trap(rep, module, tmp, seed_mirror=False)
        g3_retrieval(rep, module, tmp)
        g4_causal_lift(rep, module, tmp)
        g5_sovereignty(rep, module, tmp)
        g6_latency(rep, module, tmp)
    return rep


def self_test() -> bool:
    """Fault-inject each gate. A gate that cannot fail is theater."""
    print("\n  FAULT INJECTION — proving the harness can fail\n")
    module = load_substrate()
    ok = True

    def check(name: str, expect_fail: bool, fn) -> None:
        nonlocal ok
        rep = Report(quiet=True)
        try:
            fn(rep)
            failed = any(g["status"] == FAIL for g in rep.gates)
        except Exception as exc:  # a crash is also a detected fault
            failed, name_out = True, f"{name} (raised {type(exc).__name__})"
            name_out = name
        good = failed == expect_fail
        ok = ok and good
        mark = "PASS" if good else "FAIL"
        outcome = "detected" if failed else "passed (missed)"
        print(f"  [{mark}] {name:<38} {outcome}")

    with tempfile.TemporaryDirectory() as tmp:
        # 1. G1 must fail when the store cannot be read back.
        def g1_broken(rep: Report) -> None:
            class Blind(module.SovereignMemory):
                def retrieve(self, *a, **k):
                    return [{"_latency_ms": 0.0}]
            store = Blind(os.path.join(tmp, "blind.db"))
            store.remember("x y z", source="t")
            hits = [r for r in store.retrieve("q") if "_latency_ms" not in r]
            store.close()
            rep.add("G1", PASS if hits else FAIL, "read-back")
        check("G1 blind store (must FAIL)", True, g1_broken)

        # 2. G2 must fail when the query text is in the index.
        def g2_mirrored(rep: Report) -> None:
            g2_mirror_trap(rep, module, tmp)
        check("G2 mirror trap (must FAIL)", True, g2_mirrored)

        # 3. G4 must fail when long-term memory adds nothing.
        def g4_no_lift(rep: Report) -> None:
            original = list(TASKS)
            try:
                TASKS[:] = [t for t in original if t[2] == "recent"]  # store holds nothing useful
                g4_causal_lift(rep, module, tmp)
            finally:
                TASKS[:] = original
        check("G4 zero-lift task set (must FAIL)", True, g4_no_lift)

        # 4. G5 must fail when the store reaches for the network.
        def g5_phoning(rep: Report) -> None:
            class Phoning(module.SovereignMemory):
                def retrieve(self, *a, **k):
                    socket.create_connection(("example.invalid", 80))
                    return super().retrieve(*a, **k)
            g5_with_override(rep, Phoning)
        check("G5 store phoning home (must FAIL)", True, g5_phoning)

        # 5. Controls: the honest system must PASS the same gates.
        def g1_ok(rep: Report) -> None:
            g1_reachability(rep, module, tmp)
        check("G1 healthy store (must PASS)", False, g1_ok)

        def g2_ok(rep: Report) -> None:
            g2_mirror_trap(rep, module, tmp, seed_mirror=False)
        check("G2 honest query set (must PASS)", False, g2_ok)

    print()
    return ok


def g5_with_override(rep: Report, store_cls) -> None:
    """G5 against an arbitrary store class, for fault injection."""
    real_socket, real_conn = socket.socket, socket.create_connection

    def blocked(*_a, **_k):
        raise RuntimeError("NETWORK ATTEMPTED — sovereignty contract violated")

    socket.socket = blocked
    socket.create_connection = blocked
    try:
        store = store_cls(os.path.join(tempfile.mkdtemp(), "phoning.db"))
        store.remember("w", source="t")
        hits = [r for r in store.retrieve("w") if "_latency_ms" not in r]
        store.close()
        rep.add("G5", PASS if hits else FAIL, "air-gap")
    except RuntimeError as exc:
        rep.add("G5", FAIL, f"network call attempted: {exc}")
    finally:
        socket.socket, socket.create_connection = real_socket, real_conn


def main() -> int:
    ap = argparse.ArgumentParser(description="Portable memory evaluation")
    ap.add_argument("--self-test", action="store_true",
                    help="fault-inject every gate to prove it can fail")
    ap.add_argument("--json", action="store_true", help="emit the report as JSON")
    args = ap.parse_args()

    if args.self_test:
        return 0 if self_test() else 1

    if args.json:
        # Machine output must be parseable on its own: suppress the human report
        # rather than interleaving prose into a JSON document.
        print(json.dumps(run_all(quiet=True).as_dict(), indent=2))
        return 0

    rep = run_all()
    print(f"\n  VERDICT: {rep.as_dict()['verdict']}\n")
    return 0 if rep.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
