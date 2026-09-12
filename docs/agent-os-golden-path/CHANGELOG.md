# Agent OS Golden Path Changelog

This changelog tracks the Golden Path version stream independently from the repository's foundational Agent OS contract version.

## 0.2.0-candidate — 2026-09-12

### Executed with evidence (not prose claims)

- **Ordered task ledger executed live:** GP-01 through GP-07 completed on the reference estate with verified components and evidence handles (substrate, state ownership, phase→reality binding).
- **Field provenance woven into the spine:** `field_repeated` / `field_observed` / `derived` labels per stage, reconciling the ~65% field-derived estimate; orthogonally recorded against implementation-state vocabulary.
- **Founder-dependency test encoded and applied:** every step audited for genuine constitutional authority vs productizable procedure; preserved owner moments identified (Stage 4 authority, Stage 7 role approvals, Stage 8 benefit review).
- **HITL reconciled:** human authority is foundational, supervision conditional — verification follows the owning systems' completion architecture (Focusa/UIAI), referenced not duplicated.
- **Top-10 value additions woven** into their spine stages; 14 remaining candidates parked with explicit inclusion triggers.
- **Slice 1 — substrate check as owning code** (`scripts/substrate-bootstrap.sh`): idempotent, value-free, fail-closed; presence + version verified live for all ten components; functional health verified for the three that expose checks (focusa, tailscale, agent-kb); missing-component failure exit 1 and install-route denial (never executes) both proven by injected-fault test.
- **Slice 2 — Stage 2 provisioning bound** to the canonical `wb provision`/`wb sovereign` command surface (root invocation gotcha and dry-run/confirm gates recorded); capability existed, binding was missing.
- **Slice 3 — knowledge-plane auth provisioned** for agent accounts: KB bearer token group-readable (root:wirebot 0440, matching the estate's existing token pattern); freshness/doctor/search verified live under the agent account.
- **Slice 4 — brownfield audit script** (`scripts/brownfield-audit.sh`): value-free client-system audit reusing the owning substrate checker; one-way sha256 machine fingerprint for uniqueness; operator-supplied label only; POST delivery to an operator-deployed endpoint with optional bearer (token never printed); explicit NOT REPORTED without endpoint. Verified locally and against a local throwaway sink (HTTP 200); no raw machine id reaches the report. This is the productized enrollment/actuation qualification diagnostic from the Stage 1 value additions.
- **State-ownership map** (12 store classes, one canonical owner each) and **phase→reality mapping** (nine stage blocks with verified commands and mechanism classes) added to the handoff.

### Honest limits

- Windows substrate path is proof-gated on a real client machine (AV/UAC scars recorded); per-client grants and operated-run bindings remain proposed until executed. The brownfield audit covers bash (Linux/macOS) systems only; a Windows audit path is future work in the same proof-gated lane.
- First sovereign-tier member provision is unproven end-to-end (surface verified; deferred to an authorized run).
- 0.2.0 is a candidate until the operator confirms release.

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
