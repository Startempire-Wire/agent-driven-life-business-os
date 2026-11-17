# SOVOS Portable Scope Reconciliation and Decision Closure Doctrine

**Status:** PROPOSED portable doctrine (becomes live only after owner-authorized promotion)  
**Date:** 2026-11-17  
**Architecture authority:** [Owner Authority Constitution](OWNER_AUTHORITY_CONSTITUTION.md)  
**Agent operating contract:** [AGENTS.md](AGENTS.md)  
**Owning project/specification:** always remains the authority for product requirements

## 1. Purpose and boundaries

Provide a **portable, repeatable, retrospective** procedure that brings new and legacy projects back into alignment with attributable owner decisions when planning, documentation, issue backlogs, agent execution, or implementations have accumulated unauthorized additions, omissions, deferrals, alternatives, or complexity.

This doctrine is a **review and execution discipline**, not a new decision database, project authority, memory authority, or approval system. Reuse the canonical project specification, Focusa-governed work/evidence when available, and the deployment's actual owner-rooted authority. Private source material stays with its owning system.

**Invariant: no silent scope trimming and no silent scope adding.** Neither a faster implementation nor a better idea authorizes a change to an accepted outcome. No implementation changes, deletions, deployments, or task cancellations are authorized by merely running this review.

## 2. Exact scope semantics

1. **Approved:** an explicit, attributable, still-effective owner decision or validly delegated architecture decision, supported by source evidence; approval for a specification *for implementation* binds all its required outcomes, dependencies, negative paths, and acceptance criteria.
2. **Proposed:** an unaccepted suggestion, recommendation, inferred enhancement, draft, agent interpretation, or item without verifiable approval. A proposal is **not** implementation scope.
3. **Deferred:** a requirement whose deferral was explicitly authorized, with a named phase or review trigger. "Later," "not MVP," or a task move by an agent alone cannot create a valid deferral.
4. **Rejected:** an explicitly declined proposal; do not keep presenting it as an open alternative unless the owner reopens it.
5. **Superseded:** an older decision replaced by an attributable later approved decision; retain lineage, including exact affected sections.
6. **Unverified:** insufficient provenance or contradictory material. Do not quietly classify unverified items as approved or rejected. Report the precise uncertainty.

Status applies **per decision or requirement**, not globally to an entire document. A document may contain approved parts, proposed options, historical variants, and unverified claims.

**Two-sided change control:**
- *No trimming:* do not remove, narrow, weaken, reword into optional, defer, or declare complete while approved obligations remain unmet.
- *No adding:* do not silently add requirements, screens, workflows, mandatory dependencies, acceptance gates, architectural layers, integrations, or infrastructure.
- Internal implementation choices remain agent discretion **only if** they preserve the approved outcomes, current interfaces, existing product authority, risk limits, and actual task grant, and do not establish new product obligations.
- An implementation decision that materially changes operational cost, security/consent, users' experience, infrastructure ownership, or the accepted specification is a scope proposal, not a silent optimization.
- A change requires explicit owner-rooted approval (or a valid delegation), a recorded decision reference, and a revised owning specification. Silence, optimistic summaries, commits, merged PRs, runtime behavior, or repeated mentions are not authorization.

## 3. Portable invocation

Apply to **any** existing or future project, regardless of repository, runtime, model, language, client, or project maturity. Trigger when:
- a project seems to have spiraled in complexity, open-ended choices, dependencies, costs, or time;
- a new agent inherits a spec or prepares work;
- scope disagreement, contradictory revisions, or unexplained changes appear;
- the owner asks for a retrospective cleanup or a decision-complete implementation handoff.

Inputs: project identifier, canonical owner/product, current owner grant, current source-of-truth spec and revisions, relevant decision conversations/docs/issues/PRs, implemented behavior/evidence, and current tasks. If access is missing, classify coverage as partial; do not invent historical consent.

**Default audit is read-only.** A request to reconcile and recommend is not a grant to rewrite history, close work, drop functionality, change permissions, deploy, or delete code. Separate later implementation actions follow normal authority and grant checks.

## 4. Retrospective reconciliation procedure

**Phase A — Establish authority and a baseline.**
1. Identify the canonical owner principal and product/spec owner from existing SOVOS authority and cross-product contracts. Do not create a new project ledger.
2. Freeze a review baseline: exact spec revision, repository/branch/commit where applicable, target milestone, source/time coverage, and observed runtime state. Distinguish design claims from verified running behavior.
3. Record which decision sources were accessible and unavailable; prioritize explicit recent owner decisions over historical plans, but never treat mere recency or merged implementation as authority.

**Phase B — Mine decisions without promoting them.**
4. Extract atomic, testable outcomes and constraints from sources with quotation/location links, source date, owner attribution, and approval evidence.
5. Classify every item as Approved, Proposed, Deferred, Rejected, Superseded, or Unverified. Preserve ambiguous and conflicting cases instead of guessing.
6. Reconcile chronology: explicit owner corrections supersede only the affected dimensions of older decisions. An agent's proposal remains a proposal, even when repeated.

**Phase C — Detect scope drift in both directions.**
7. Compare (i) approved outcome baseline, (ii) written current spec, (iii) queued work, and (iv) implemented/running behavior.
8. Flag **missing/trimmed**, **unauthorized added**, **changed**, **duplicated**, **unverified**, and **accepted but unimplemented** requirements; note whether a mismatch is documentary, planned, or actual.
9. Separate essential current commitments from legitimately authorized later phases. A small successful MVP is an early milestone, **not** permission to erase full accepted scope.

**Phase D — Apply First Principles and Leverage² twice.**
10. Run **Question → Delete → Simplify → Accelerate → Automate** on the project-level *method and critical path*, then again on each implementation task.
11. Question unnecessary assumptions and constraints; delete ceremony and duplicate machinery; simplify through proven primitives; accelerate the route to a real outcome; automate only stable repeatable work.
12. Apply deletion to **unnecessary process**, never approved capabilities. A proposed feature addition or removal remains a proposal until authorized. Preserve safety, consent, tenancy, payment integrity, evidence, and operational consequences where they apply.
13. Sequence the accepted scope into dependency-ordered deployable increments; preserve a complete trace from each approved requirement to work and verification. No artificial prebuild test wall; use direct running evidence and changed-path smoke checks, plus targeted tests for consequential risks.

**Phase E — Close decisions and execute only within grants.**
14. Produce **one recommended resolution per unresolved decision**, with reason, impact, dependencies, and what remains unchanged. Avoid option menus and speculative backlog expansion.
15. Present an exact proposed revision/diff to the owner for approval. Unless approved, the current canonical requirement remains in force and the new item remains only proposed.
16. After attributable approval, update **the owning product specification** with decision ID, changed requirements, exact supersession and provenance, then update its governed tasks. Do not rewrite earlier decisions to appear as though they never existed.
17. Implement only with appropriate task/deployment authorization, verify changed behavior in the running system, and retain evidence and explicit remaining gaps. Report *partial*, *blocked*, or *complete* accurately.

## 5. Minimal reconciliation record (portable report, not a new authority)

For each item, include only the fields needed to make its status and consequence inspectable:

```yaml
project_ref: <canonical project>
review_baseline: <spec revision + source coverage + implementation ref>
requirement_id: <stable existing ID or review-local identifier>
requirement: <one observable outcome or constraint>
decision_status: approved | proposed | deferred | rejected | superseded | unverified
authority_source_refs: []
approval_evidence_ref: null
supersedes_refs: []
spec_state: present | missing | modified | not_checked
work_state: aligned | added | omitted | deferred | unknown
runtime_state: verified | not_verified | divergent | not_applicable
drift: none | added | trimmed | changed | duplicated | ambiguous
recommendation: <one specific resolution, if needed>
owner_approval: pending | accepted | rejected | not_required
next_action: <specific, authorized step or owner decision>
```

Use this record as a temporary report or projection linked to existing source-of-truth records. Do not install a new ledger, approval service, decision mining daemon, or database merely to apply this doctrine. Integration into existing Focusa decision governance is a separate owner-approved implementation concern.

## 6. Exit conditions and report shape

A reconciliation pass is **complete as an audit** when source coverage/limitations are disclosed, every inspected item has a provenance-aware status, both types of drift are listed, a single recommended correction exists for each unresolved decision, and the preserved accepted obligations are traceable. The project itself is **not complete** until its entire accepted specification is implemented and verified.

The user-facing report should state, in this order: approved baseline; detected additions; detected trims/deferrals; unknowns/conflicts; one recommended minimal correction per unresolved decision; owner approvals needed; next authorized implementation step. Use business language and prioritize critical-path progress. Do not force all decisions to be reopened simply because an audit runs.

## 7. Relationship to SOVOS governance

- [OWNER_AUTHORITY_CONSTITUTION.md](OWNER_AUTHORITY_CONSTITUTION.md) owns approval and delegation.
- [AGENTS.md](AGENTS.md) remains the live operational contract and Leverage² source.
- [CURRENT_ECOSYSTEM_ARCHITECTURE.md](CURRENT_ECOSYSTEM_ARCHITECTURE.md) owns cross-product responsibility.
- Each product's own repository/spec owns its requirements and completion evidence.
- Focusa (where used) governs work, authority, Evidence, receipts and continuity.

This is a reusable **doctrine and review procedure**. Its acceptance does not retroactively authorize any project-specific scope change; each correction must be separately attributed and approved.
