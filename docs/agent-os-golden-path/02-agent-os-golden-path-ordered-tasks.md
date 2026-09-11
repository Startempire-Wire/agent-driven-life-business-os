# Golden Path — iterable working doc (essence, spine, scars, tasks)

- Date: 2026-09-10 (iteration 2)
- Locked essence: an end-to-end instruction set that lets an agent **fully execute** a ground-up build-out of the Human Life & Business Agent OS on **current brownfield workstations** — with **zero human turns** during setup.
- Loop paradigm: **ACITL — Agent Computer In The Loop.** The Agent Computer (Veragensia, with remote access) is the loop's hands; the owner is the **grantor**, not the courier. (Operator-originated paradigm, 2026-09-10.)
- Source spine: the operator's **proven as-built client deployment sequence** (below), not an abstract phase model.
- Method adopted from the starter: its **essence only** — pre-made decisions (defaults), paid-for failures (scars), embedded proof (checks), dependency-true order. Its stack, phases, and public-app specifics are not copied. Verbatim reference: `https://burcs.dev/starter.md`.
- Published lineage: [0.1.0](0.1.0.md) phases remain the coverage scaffold; [0.1.1](0.1.1.md) clarifications stand. Working iteration targets **0.2.0** built from the spine + live reconciliation.
- Current acceptance: iteration/documentation only. No installer, customer rollout, or end-to-end acceptance is claimed.

## One working doc, not another control plane

This is the single iterable project-local artifact for the Golden Path work. Reuse task IDs when admitting executable work to existing task/CallGraph systems; link records here. No second execution ledger. `ready` means dependencies satisfied, not permission to mutate infrastructure — operational changes still resolve their own authority, capability, acceptance and rollback.

## Locked design decisions (inputs to every revision)

1. **Zero human turns bar.** A step passes when a fresh agent, holding granted credentials, executes it without asking. Anything failing the test either gets an authorized automation path or is classified irreducible-human — exact, batched, minimal.
2. **ACITL.** The Agent Computer replaces the human courier. The owner consents once per surface; the AC drives the screens. Secret-entry moments are **AC-driven, owner-typed**: the AC opens the form remotely, the owner types the secret once, and the agent never sees or stores it. Authority origin stays with the owner; nonrenewable assets stay owner-only.
3. **Brownfield-first.** The path starts on the client's existing computer, audits what is present, and builds out. It never assumes a clean machine, never imports another deployment's private state, and distinguishes pre-existing from newly created resources.
4. **Starter essence, not starter content.** Every spine step carries: defaults (decisions already made), scars (real failures with fixes), one embedded check (proves done, not "typed"), and dependency-true ordering. Phase numbering is coverage, never permission or schedule.
5. **Reuse-first.** Existing installers/CLIs own every step (Pi, Focusa lifecycle, UIAI, rbw, gog, GitHub/Tailscale auth flows, OpenClaw, provisioning). The Golden Path names which mechanism owns which step; it does not replace them.

## The as-built spine (source: operator's client deployments)

The proven manual sequence, restated as the spine with step classes:

| Stage | Steps (operator's sequence) | Class |
|---|---|---|
| 1. Workstation substrate | Install Pi; connect OpenAI subscription or OpenRouter; download Focusa; download UIAI Engine; set up Bitwarden (shared vault); set up rbw (agent-side secret retrieval) | Mixed: installs = AC-with-grant; provider account/billing consent = owner-typed once; Bitwarden master pw = AC-driven, owner-typed |
| 2. Remote control plane | OVH VPS account; respond to verification emails; browser login to VPS | AC-with-grant after one consent (email access, credentials); billing/verification screens = one owner moment |
| 3. Mesh + identity | GitHub (create if none); GitHub authenticates Tailscale; Tailscale on all machines; connected machines let agents surf between | AC-with-grant (GitHub/Tailscale auth via granted renewable routes); machine installs = AC on managed machines, owner-assisted on machines the AC cannot reach |
| 4. Knowledge + audit | Document all; gog CLI across G Suite for audits | AC-with-grant (gog OAuth consent once) |
| 5. Operating plane | OpenClaw on VPS as Chief of Staff; full business audit to categorize the business; create business owner voice profile (correspondence); create systems of common tasks; create crons for regular workflows; set up virtual employees with role-based toolsets and permissions | AC-executed with granted tools; voice profile needs owner-supplied samples = one owner moment |
| 6. Ongoing operation | "This is just the beginning" — the path hands off to operation, not to a finish line | Handoff contract; replacement agent continues from durable state |

The consent surface is the enumerated set of owner moments above — the target is a few named moments per provider, not scattered asks. Any step still requiring the human as courier is unexercised automation to be built, not a permanent gate.

## Scar ledger (paid-for failures — standing iteration input)

Operator-fed deployment scars. Each becomes: observed failure → default → check → consent boundary. Exclusions/security changes are grant moments, never silent.

| Scar (Windows brownfield) | Default | Check |
|---|---|---|
| Antivirus / script blocking kills installers, npm lifecycle scripts, downloaded scripts | Signed official installers only; no silent exclusions | Installer completes; signed binary runs; script executes where authorized |
| No proper terminal | Windows Terminal + PowerShell 7; WSL-vs-native decided once, not per machine | Terminal opens; agent harness runs in it |
| No node/npm | Official Node installer; PATH set | `node -v` and `npm -v` succeed in the agent's shell |
| UAC/elevation prompts scattered | Batch into one elevation moment | Count elevation prompts per deployment = 1 |
| PowerShell execution policy / Defender ASR blocks agent scripts | Per-script unblock; blanket policy change needs owner consent | Agent's authorized scripts execute; unrelated scripts stay blocked |

Feeding rule: the operator feeds scars as found; each is encoded once here, then referenced by spine steps. Nothing enters the portable repo that names a private client.

## Ordered tasks

| ID | Status | Depends on | Task and done-condition |
|---|---|---|---|
| GP-01 | done | — | Pull upstream docs; read candidate, root guide, handoff; locate task owner. Evidence: fast-forward to `3658ecc`; four docs; no duplicate ledger. |
| GP-02 | done | GP-01 | Compare starter method; publish iteration list and first clarification; record findings. Done = lineage preserved, links checked. |
| GP-03 | ready | GP-02 | Distill the **as-built spine** (above) into the essential spine draft: per step — class, owning mechanism, granted authority, check, scar references, irreducible-human moments. Replace the abstract profile-matrix framing. Reference-owner profile becomes a sub-case of the same spine. |
| GP-04 | planned | GP-03 | Reconcile the live estate through approved read-only routes; classify configured/reachable/usable-by-agent/verified separately with evidence; inventory **consent surfaces** (every current human moment and its grant path). Reuse existing audit work. |
| GP-05 | planned | GP-04 | Map material state ownership: domain, scope, canonical owner, writers/readers, store role, consistency, freshness, backup, recovery. No synchronization store. |
| GP-06 | planned | GP-05 | Bind all fourteen phases and every spine step to actual existing operations — including **ACITL bindings**: which steps the AC executes, which are AC-driven-owner-typed, where grants come from. No invented command names. |
| GP-07 | planned | GP-06 | Review the executable design against normal, partial, denied and interrupted runs; apply the zero-human-turns test per step; reuse the existing task/CallGraph executor. Produce the smallest unresolved implementation backlog. |
| GP-08 | planned | GP-07 | Select the first highest-leverage slice from observed gaps; prefer restoring/reusing an existing capability over new aggregates. Record owning repo, changed surfaces, execution authority, consumer acceptance, rollback. |
| GP-09 | planned | GP-08 | Implement and test that slice in its owning subsystem; deploy only to its approved proving destination. Positive path, denial behavior, retry safety, observable failure. Source commit alone leaves this open. |
| GP-10 | planned | GP-09 | Run a bounded end-to-end workflow through the actual Chief-of-Staff/worker path, including an **ACITL moment** (agent computer executes a consented action remotely). Prove user-visible result + scoped receipt. |
| GP-11 | planned | GP-10 | Prove reproducibility on brownfield: fresh build-out, adoption of partial state, unchanged rerun, interruption/restart, rollback. No duplicate resources; no private-state import; pre-existing resources preserved. |
| GP-12 | planned | GP-11 | Repeat in an explicitly authorized isolated client profile with synthetic principals: authorized function AND cross-tenant denial; consent surface batched as designed; secrets never transit agent storage. |
| GP-13 | planned | GP-12 | Replacement agent runs from documented entry points and durable state; reconcile acceptance rows; publish the reality-grounded next version (normally `0.2.0`) and honest handoff. |

## Completion criteria

- Every spine step: explicit class, existing execution binding, embedded check; no undocumented manual prerequisite.
- Consent surface enumerated and batched; secret-entry moments are AC-driven-owner-typed; agent never holds owner secrets.
- Defaults, scars and checks present per step; scars encoded once and reused.
- Fresh, partial, rerun, interrupted and recovery paths behave as specified on brownfield machines.
- Authorized function and unauthorized-scope denial both proven; no sovereign fallback.
- No secrets or private client data in this doc; receipts attributable.
- A replacement agent continues from durable references, not session memory.

## Findings and evidence limits (iteration 2)

- Locked 2026-09-10: essence = end-to-end agent-executed ground-up build-out, zero human turns; ACITL replaces Human-In-The-Loop; brownfield-first; starter essence adopted (defaults/scars/checks/order), stack not imported.
- Source spine: operator's as-built client sequence (this doc, stages 1–6). Treat as the 0.2.0 content source, alongside live reconciliation.
- Tooling defects found while working (filed, not doctrine blockers): UIAI browser result delivery broken (uiai-engine #224), `wb --format json doctor` JSON banner (wirebot-core #31), `fetch_content` signal error (wirebot-core #32), stale session fingerprint (focusa #599), `focusa_decide` over-validation (#600), Focus State frame unavailable (#601).
- Starter verbatim markdown retrieved from `https://burcs.dev/starter.md` after the UIAI delivery defect (fallback per AGENTS §10.4); saved at `/tmp/burcs-starter-verbatim.md`.
- No live reconciliation, installer, customer rollout or end-to-end acceptance has occurred. GP-04 onward remains open.

Sources: operator as-built process and scars (2026-09-10); [0.1.0](0.1.0.md); [0.1.1](0.1.1.md); [server handoff](SERVER_AGENT_HANDOFF.md); starter verbatim reference.