# Agent OS Golden Path Changelog

This changelog tracks the Golden Path version stream independently from the repository's foundational Agent OS contract version.

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
