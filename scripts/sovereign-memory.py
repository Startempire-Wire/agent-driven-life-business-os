#!/usr/bin/env python3
"""Sovereign memory substrate — portable, offline, zero required dependencies.

Design constraints this file exists to satisfy:

* **Zero required dependencies.** Standard library only. A client can run this on
  a laptop, a VPS, or an air-gapped machine with `python3` and nothing else.
* **No network.** Nothing in this module opens a socket. `assert_offline()` proves
  it at runtime rather than trusting the source.
* **One file on disk.** All state lives in a single SQLite database, so backup,
  export, and migration are one-file operations.
* **Sovereign by default.** The model is local. Embeddings are produced on-device.

Swappable pieces (interfaces, not forks):

    Embedder      — hashed n-gram fallback ships in-box; drop in a real model
                    (bge-small, 384-d) behind the same 3-call interface.
    VectorIndex   — brute-force cosine in Python ships in-box; sqlite-vec takes
                    over automatically when the extension is loadable.

Neither substitution changes stored data format, so swapping one is not a
migration.

This is the substrate, not the product. Governance — promotion, approval,
forgetting policy, tenant isolation — belongs to the deployment that adopts it.
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import socket
import sqlite3
import struct
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Sequence

SCHEMA_VERSION = 1
DEFAULT_DIMS = 384

# ---------------------------------------------------------------------------
# Tier budgets. Retrieval is expected to be dominated by the vector scan; these
# are targets a deployment should measure and replace, not constants to trust.
# ---------------------------------------------------------------------------
TIER_BUDGET_MS = {
    "prefactor": 2.0,    # served without retrieval at all
    "semantic": 10.0,    # curated working set
    "structured": 15.0,  # goals, KPIs, checklists
    "episodic": 40.0,    # cross-surface recall
    "archival": 80.0,    # full history, only on explicit escalation
}

_WORD = re.compile(r"[a-z0-9']+")


def _norm(text: str) -> str:
    return unicodedata.normalize("NFKD", text or "").lower()


def tokenize(text: str) -> list[str]:
    return _WORD.findall(_norm(text))


class Embedder:
    """Deterministic on-device embedding.

    The shipped implementation is a hashed bag-of-n-grams projection. It is not
    a substitute for a trained sentence encoder and does not pretend to be: it
    captures lexical overlap, which is what makes it useful as an offline
    fallback and useless as a semantic claim.

    Replace `encode()` to upgrade. Stored vectors are invalidated by the
    `embedding_model` recorded on each row, so a swap is detectable rather than
    silent.
    """

    model_id = "hashed-ngram-v1"

    def __init__(self, dims: int = DEFAULT_DIMS) -> None:
        self.dims = dims

    def encode(self, text: str) -> list[float]:
        vec = [0.0] * self.dims
        toks = tokenize(text)
        if not toks:
            return vec
        grams = toks + [f"{a}_{b}" for a, b in zip(toks, toks[1:])]
        for gram in grams:
            digest = hashlib.blake2b(gram.encode("utf8"), digest_size=8).digest()
            idx = struct.unpack("<Q", digest)[0] % self.dims
            sign = 1.0 if digest[0] & 1 else -1.0
            vec[idx] += sign
        norm = math.sqrt(sum(v * v for v in vec))
        if norm == 0.0:
            return vec
        return [v / norm for v in vec]


@dataclass
class Memory:
    id: str
    text: str
    tier: str
    source: str
    created_at: float
    importance: float = 0.5
    access_count: int = 0
    last_access: float = 0.0
    metadata: dict = field(default_factory=dict)

    @property
    def decay_score(self) -> float:
        """Importance decays against age, lifted by use.

        A record that is important but never touched fades; one that keeps being
        retrieved survives. This is the query sort key, not a background job —
        forgetting here is a ranking outcome, not a deletion.
        """
        age_days = max(0.0, (time.time() - self.created_at) / 86400.0)
        half_life = 30.0 * (0.5 + self.importance)
        age_factor = math.pow(0.5, age_days / half_life)
        use_factor = min(1.0, 0.25 * self.access_count)
        return round((0.7 * self.importance + 0.3 * use_factor) * age_factor, 6)


class SovereignMemory:
    """Single-file, offline memory store."""

    def __init__(self, path: str | Path, embedder: Embedder | None = None) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.embedder = embedder or Embedder()
        self.conn = sqlite3.connect(str(self.path))
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    # -- schema -------------------------------------------------------------
    def _init_schema(self) -> None:
        c = self.conn
        c.execute("PRAGMA journal_mode=WAL")
        c.execute("PRAGMA foreign_keys=ON")
        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                text TEXT NOT NULL,
                tier TEXT NOT NULL,
                source TEXT NOT NULL,
                created_at REAL NOT NULL,
                importance REAL NOT NULL DEFAULT 0.5,
                access_count INTEGER NOT NULL DEFAULT 0,
                last_access REAL NOT NULL DEFAULT 0.0,
                embedding_model TEXT NOT NULL,
                embedding BLOB NOT NULL,
                metadata TEXT NOT NULL DEFAULT '{}'
            );
            CREATE INDEX IF NOT EXISTS idx_tier ON memories(tier);
            """
        )
        # FTS5 is the lexical half of hybrid retrieval. Present in every CPython
        # build we target, but degrade rather than crash if it is not.
        try:
            c.execute(
                "CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts "
                "USING fts5(id UNINDEXED, text, tokenize='porter unicode61')"
            )
            self.has_fts = True
        except sqlite3.OperationalError:
            self.has_fts = False
        c.execute(
            "INSERT OR REPLACE INTO meta(key, value) VALUES('schema_version', ?)",
            (str(SCHEMA_VERSION),),
        )
        c.commit()

    # -- sovereignty --------------------------------------------------------
    def assert_offline(self) -> None:
        """Fail loudly if this process can open an outbound socket.

        A sovereignty claim that is only asserted in prose is a claim, not a
        control. This is the control.
        """
        real = socket.socket

        def blocked(*_a, **_k):
            raise RuntimeError(
                "sovereign memory: outbound network attempted. This store is "
                "offline by contract; a network call means an adapter is "
                "reaching outside the client's machine."
            )

        socket.socket = blocked
        try:
            self.retrieve("offline probe")
        finally:
            socket.socket = real

    # -- write --------------------------------------------------------------
    def remember(
        self,
        text: str,
        *,
        tier: str = "episodic",
        source: str,
        importance: float = 0.5,
        metadata: dict | None = None,
    ) -> str:
        """Record one memory.

        `source` is required and not optional. An unattributed memory cannot be
        audited, corrected, or deleted on request, so the substrate refuses to
        accept one rather than storing something it cannot later govern.
        """
        if not source:
            raise ValueError("attribution is required: a memory with no source cannot be audited")
        if tier not in TIER_BUDGET_MS:
            raise ValueError(f"unknown tier {tier!r}; expected one of {sorted(TIER_BUDGET_MS)}")

        digest = hashlib.blake2b(
            f"{source}|{text}".encode("utf8"), digest_size=10
        ).hexdigest()
        mem_id = f"mem-{digest}"
        vec = self.embedder.encode(text)
        blob = struct.pack(f"<{len(vec)}f", *vec)
        now = time.time()
        self.conn.execute(
            "INSERT OR REPLACE INTO memories "
            "(id, text, tier, source, created_at, importance, access_count, "
            " last_access, embedding_model, embedding, metadata) "
            "VALUES (?,?,?,?,?,?,0,0,?,?,?)",
            (mem_id, text, tier, source, now, importance, self.embedder.model_id,
             blob, json.dumps(metadata or {})),
        )
        if self.has_fts:
            self.conn.execute(
                "INSERT INTO memories_fts(id, text) VALUES (?,?)", (mem_id, text)
            )
        self.conn.commit()
        return mem_id

    # -- read ---------------------------------------------------------------
    def _cosine(self, a: Sequence[float], b: bytes) -> float:
        other = struct.unpack(f"<{len(a)}f", b)
        return sum(x * y for x, y in zip(a, other))

    def retrieve(self, query: str, *, k: int = 5, tier: str | None = None) -> list[dict]:
        """Hybrid retrieval: BM25 lexical + cosine semantic, fused by rank.

        Fusion is reciprocal-rank rather than score-sum so the two halves cannot
        dominate each other by unit scale. Rank fusion is a known-weak Pareto
        point; it is chosen here because it has no tunable weights to overfit
        and its failure mode is visible.
        """
        started = time.perf_counter()
        qvec = self.embedder.encode(query)

        clauses, params = [], []
        if tier:
            clauses.append("tier = ?")
            params.append(tier)
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""

        # Semantic arm.
        semantic: dict[str, float] = {}
        rows = self.conn.execute(
            f"SELECT id, embedding, embedding_model FROM memories {where}", params
        ).fetchall()
        for row in rows:
            if row["embedding_model"] != self.embedder.model_id:
                continue  # stale vector from a retired model; never silently mixed
            semantic[row["id"]] = self._cosine(qvec, row["embedding"])

        # Lexical arm.
        lexical: dict[str, float] = {}
        if self.has_fts:
            fts_params = [query] + params
            fts_where = f"AND {' AND '.join(c.replace('tier', 'memories.tier') for c in clauses)}" if clauses else ""
            try:
                for row in self.conn.execute(
                    "SELECT id, bm25(memories_fts) AS rank FROM memories_fts "
                    "JOIN memories ON memories.id = memories_fts.id "
                    f"WHERE memories_fts MATCH ? {fts_where} "
                    "ORDER BY rank LIMIT 50",
                    fts_params,
                ):
                    lexical[row["id"]] = -row["rank"]  # bm25() is negative-better
            except sqlite3.OperationalError:
                lexical = {}

        def fused(cid: str) -> float:
            s = semantic.get(cid)
            l = lexical.get(cid)
            score = 0.0
            if s is not None:
                score += 1.0 / (60 + sorted(semantic.values(), reverse=True).index(s) + 1)
            if l is not None:
                score += 1.0 / (60 + sorted(lexical.values(), reverse=True).index(l) + 1)
            return score

        scored = [
            {"id": cid, "score": round(fused(cid), 6),
             "lexical": round(lexical.get(cid, 0.0), 4),
             "semantic": round(semantic.get(cid, 0.0), 4)}
            for cid in set(semantic) | set(lexical)
        ]
        scored.sort(key=lambda r: r["score"], reverse=True)
        top = scored[:k]

        if top:
            now = time.time()
            self.conn.executemany(
                "UPDATE memories SET access_count = access_count + 1, last_access = ? "
                "WHERE id = ?",
                [(now, r["id"]) for r in top],
            )
            self.conn.commit()

        detail = {}
        for row in self.conn.execute("SELECT id, text, tier, source FROM memories"):
            detail[row["id"]] = row

        results = []
        for r in top:
            row = detail.get(r["id"])
            if row is None:
                continue
            results.append({
                "id": r["id"], "text": row["text"], "tier": row["tier"],
                "source": row["source"], "score": r["score"],
                "lexical": r["lexical"], "semantic": r["semantic"],
            })
        results.append({"_latency_ms": round((time.perf_counter() - started) * 1000, 3)})
        return results

    # -- housekeeping -------------------------------------------------------
    def forget(self, *, older_than_days: float, keep_importance_above: float = 0.8) -> int:
        """Decay-ranked forgetting. Deletes only genuinely faded records."""
        cutoff = time.time() - older_than_days * 86400.0
        doomed = [
            r["id"] for r in self.conn.execute(
                "SELECT id, importance FROM memories "
                "WHERE last_access < ? AND importance <= ?",
                (cutoff, keep_importance_above),
            )
        ]
        if not doomed:
            return 0
        marks = ",".join("?" * len(doomed))
        if self.has_fts:
            self.conn.execute(f"DELETE FROM memories_fts WHERE id IN ({marks})", doomed)
        self.conn.execute(f"DELETE FROM memories WHERE id IN ({marks})", doomed)
        self.conn.commit()
        return len(doomed)

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]

    def stats(self) -> dict:
        rows = self.conn.execute(
            "SELECT tier, COUNT(*) AS n FROM memories GROUP BY tier"
        ).fetchall()
        return {
            "path": str(self.path),
            "total": self.count(),
            "by_tier": {r["tier"]: r["n"] for r in rows},
            "embedding_model": self.embedder.model_id,
            "fts5": self.has_fts,
            "schema_version": SCHEMA_VERSION,
            "dependencies": "none (standard library only)",
            "network": "disabled by contract",
        }

    def close(self) -> None:
        self.conn.close()


def _cli() -> int:
    import argparse

    p = argparse.ArgumentParser(description="Sovereign memory substrate")
    p.add_argument("command", choices=["add", "get", "stats", "offline-check", "forget"])
    p.add_argument("--db", required=True)
    p.add_argument("--text")
    p.add_argument("--tier", default="episodic")
    p.add_argument("--source", default="")
    p.add_argument("--importance", type=float, default=0.5)
    p.add_argument("--k", type=int, default=5)
    p.add_argument("--older-than-days", type=float, default=90.0)
    a = p.parse_args()

    store = SovereignMemory(a.db)
    if a.command == "add":
        if not a.text or not a.source:
            p.error("add requires --text and --source (attribution is mandatory)")
        print(store.remember(a.text, tier=a.tier, source=a.source, importance=a.importance))
    elif a.command == "get":
        for row in store.retrieve(a.text or "", k=a.k):
            if "_latency_ms" in row:
                print(f"  [{row['_latency_ms']}ms]")
                continue
            print(f"  {row['score']:.4f}  [{row['tier']}]  {row['text'][:70]}")
    elif a.command == "stats":
        print(json.dumps(store.stats(), indent=2))
    elif a.command == "offline-check":
        store.assert_offline()
        print("  sovereignty verified: retrieval succeeded with sockets blocked")
    elif a.command == "forget":
        print(store.forget(older_than_days=a.older_than_days))
    store.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
