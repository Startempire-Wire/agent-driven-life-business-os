# Agent OS Golden Path Changelog

This changelog tracks the Golden Path version stream independently from the repository's foundational Agent OS contract version.

## 0.2.0-candidate — 2026-09-12

### Recorded work and bounded evidence

- **Ordered ledger reconciled:** GP-01–03 planning/lineage work is done; GP-04–07 estate, ownership, bindings and run review remain in progress with bounded reference evidence. GP-08/09 remain in progress; documentation never substitutes for their acceptance tests.
- **Field provenance woven into the spine:** `field_repeated` / `field_observed` / `derived` labels per stage, reconciling the ~65% field-derived estimate; orthogonally recorded against implementation-state vocabulary.
- **Founder-dependency test encoded and applied:** every step audited for genuine constitutional authority vs productizable procedure; preserved owner moments identified (Stage 4 authority, Stage 7 role approvals, Stage 8 benefit review).
- **HITL reconciled:** human authority is foundational, supervision conditional — verification follows the owning systems' completion architecture (Focusa/UIAI), referenced not duplicated.
- **Top-10 value additions woven** into their spine stages; candidates 1–17 retained with triggers. Candidate 18 is withdrawn: the proposed fleet/enrollment coupling was an assistant invention.
- **Slice 1 — substrate checker** (`scripts/substrate-bootstrap.sh`): ten CLI presence/version checks and three health paths. Historical reference run after KB access repair: ten present, three healthy, seven n/a. Synthetic missing-tool exit 1 and route printing without installation were tested. Unhealthy results do not change the exit code; this is not a full readiness gate.
- **Slice 2 — provisioning surface bindings:** `wb provision`/`wb sovereign` help/list inspection and invocation gotchas recorded. No provisioning writes, denial/interruption handling or end-to-end lifecycle proof claimed.
- **Slice 3 — reference KB account access:** existing bearer file made group-readable (root:wirebot 0440); historical wirebot-account checks succeeded. This is not per-client least-privilege provisioning. Rollback restores root:root and 0600; no token value is included here.
- **Slice 4 — brownfield report prototype** (`scripts/brownfield-audit.sh`): reuses the checker; Linux report and local HTTP sink tested. Raw machine-id and the tested synthetic bearer were absent from captured output. Hashed identity remains pseudonymous/linkable; comprehensive privacy, HTTPS enforcement and real receiver receipt/readback are unproven. This is neither production intake nor enrollment.
- **State-ownership map** (12 store classes, one canonical owner each) and **phase→reality mapping** (nine stage blocks with verified commands and mechanism classes) added to the handoff.

### Cohesion reconciliation — iteration 32 (2026-09-12)

- Preserve the nine-stage spine and existing component owners; distinguish participation, runtime, hosting/operation, federation and interfaces.
- Correct the two product doors to Focusa.dev + Wirebot.chat; identify os.focusa.dev separately by its operator-confirmed Agent Computer role, not by a misleading live-verification claim.
- Reconcile the existing ledger: GP-04–07 and GP-08/09 remain in progress; retain bounded proofs without promoting them to full completion.
- Update the topology visual, entry pages and server handoff; withdraw fleet/enrollment assumptions. Audit observations, authoritative identity, readiness and business outcomes remain distinct.
- Settled economics, wrapped-process IP, service tether and independent component licensing are unchanged. Documentation only; scripts, credentials, hosts and public website copy unchanged.

### Honest limits

- Only Linux reference/local-sink behavior has been exercised here; macOS and Windows remain unproven, as do real client requirements, grants and operated-run bindings. The prototype checks ten CLIs, not all ecosystem capabilities; UIAI/OpenClaw are omitted and remote/not-required states are not implemented.
- First sovereign-tier member provision is unproven end-to-end (surface verified; deferred to an authorized run).
- Script JSON/argument handling, bounded checks, truthful privacy/status and an approved real receiver with permissions, retention and readback remain local work—not merely externally blocked proof.
- 0.2.0 remains a candidate until its acceptance evidence and authorized publication are complete; no tag or release is created by these edits.

## 0.1.1-candidate — 2026-09-10

### Clarified

- Phase numbering is coverage, not permission to delay prerequisite authority, security, budgets, evidence or safe proving.
- Fresh setup, partial adoption, repair and upgrade have different preconditions and retry/recovery obligations.
- Executable claims require real owning interfaces and consumer checks; unsupported mandatory phases cannot become "not applicable."
- Source-starter public-app defaults are not private-system defaults; instruction refresh and agent-tool usability require separate checks.
- Added one dependency-ordered task list with acceptance, authority boundaries and candidate owner mappings for all fourteen phases.
- Updated entry points to the current candidate and task list; preserved `0.1.0` unchanged.

### Evidence scope and compatibility

Patch clarification over `0.1.0`; no renamed phases, new runtime schema or replaced subsystem authority. The current candidate references the base definitions rather than duplicating them. Evidence covers repository/candidate/handoff review, public starter inspection, and existing instruction-loading observations. No installer, production change, customer test or full-system verification is claimed. The handoff's implemented-slice milestone and subsequent reality-grounded version remain outstanding.

## 0.1.0-candidate — 2026-09-08

Initial portable candidate.

### Added

- End-to-end 14-phase Golden Path from deployment identity through launch/ongoing operation.
- Structural phase contract: `PURPOSE → INVARIANTS → IMPLEMENTATION → CHECK → GOTCHAS → RECOVERY/ROLLBACK → EXIT CONDITION`.
- Core principles adapted from the executable-starter pattern:
  - allowlist surfaces/authority;
  - one source of truth per data kind;
  - staging/proving path from the beginning;
  - reconstructable config with secrets kept out of source;
  - boring/simple mechanisms over clever orchestration;
  - agents as first-class operators/users;
  - behavioral checks instead of proof theater.
- State role taxonomy: `CANONICAL`, `DERIVED`, `CACHE`, `INDEX`, `COORDINATION`, `EVIDENCE`, `EPHEMERAL`.
- First-class Agent Surface phase covering progressive machine discovery and subsystem interoperability.
- Candidate portable profiles for reference-sovereign, sovereign-customer, shared-tenant, and personal-life deployments.
- Versioning and iteration rules designed for server-driven learning.
- Dedicated on-server handoff requiring live reconciliation, reuse-first implementation, one high-leverage executable slice, and publication of the next version.

### Evidence scope

This version was prepared from the portable repository, connected reference repositories, recent architecture discussion, and the user-provided `burcs.dev/starter` screenshots. It was **not** prepared from direct access to the live server/customer environments and therefore has `candidate` status.

### Required next iteration

The authorized on-server build agent should reconcile `0.1.0` against live operational authority, implement the smallest high-leverage executable slice, and normally publish `0.2.0` with real observed gotchas, checks, and reusable mappings.
