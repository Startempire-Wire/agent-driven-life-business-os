# Agent OS Golden Path Changelog

This changelog tracks the Golden Path version stream independently from the repository's foundational Agent OS contract version.

## 0.1.2-candidate — 2026-09-10 (planning stream, unreleased)

### Changed

- Agent-centric rewording: setup is agent-operated; the owner supplies goals, business knowledge, consequential choices and approvals — not command execution.
- Consent surface is designed and batched at Stage 0 but no longer promises a fixed ask count; consequential discoveries may add asks.
- Stage 2: the folder carries directives/soul/configuration; runtime memory and task state remain with owning services; the OpenClaw-local assumption is removed.
- Ascension: source moves through git; private state moves through its owning backup/migration mechanisms.
- Correspondence style derives from approved examples and feedback; audio samples optional.
- Scar provenance marked: observed (operator-reported) vs hypothesized defaults pending real runs.

### Reclassified

- `0.1.1` is superseded planning input, retained for lineage; the ordered-tasks working document is the single iterable planning source toward 0.2.0.

### Evidence scope

Documentation iteration only: no installer, live reconciliation, customer rollout or end-to-end acceptance is claimed. GP-03 remains in progress; GP-04 onward are future work, not authorization to begin.

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
