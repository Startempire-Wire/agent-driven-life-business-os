# SOVOS Master Loop — Distribution, Portability and Extension Contract

**Status:** PROPOSED amendment to [contract09](./09-sovos-master-loop-composable-provenance-and-agent-first-contract.md).
Drafted 2026-10-28. **Not canonical until the Canonical Owner Principal approves it.**
Nothing here expands execution permission, credential scope or architecture authority.

## Why this amendment exists

Contract09 states the semantics: composition without a blob, reconstructable
records, agent-first surfaces, no second registry/scheduler/permission store, and
"portable deployments keep these semantics and replace local bindings". It does
not state what those obligations *require of a deployment that runs many tenants
on many nodes*, so each implementation currently re-decides them in code. That is
how a specification becomes boutique: the semantics stay written, the mechanics
get improvised per deployment.

This document adds only the missing mechanics. It does not restate or override 02–09.

## 1. Extension points extend, never duplicate

A deployment already has registered sources, conditions and effects. New capability
joins **that** registration surface; it does not introduce a parallel registry, a
second scheduler, a second permission store or a second workflow authority
(contract09 §Cross-component acceptance).

- Registration is metadata. Registration is **not** permission to execute
  (contract09 §Agent-first).
- An unbound or unavailable primitive stays listed and marked unavailable. It is
  never omitted to make a catalogue look complete, and never faked into
  availability.
- Adding a source, condition or effect must require **no edit to loop core**: a
  registration plus deployment configuration.
- What is registered, what is installed, and what the caller is granted remain
  three distinct facts, each independently inspectable.

## 2. The component contract is data, not prose in three places

Every contract the system publishes — event/fact schemas, relation and state
vocabularies, validation rules, bounds, compatibility declarations — has exactly
one machine-readable source. Server readers, CLI validators and human vocabulary
are **generated or derived** from it. Hand-maintained copies are defects, including
"small" ones: a schema version that must be added in three files has already
diverged once.

- Versioned contracts are additive. New readers accept all supported versions;
  old readers must not silently misread a newer fact; unknown versions fail closed.
- Compatibility tables live in the same source as the contract, not in prose.
- Generated consumers are build-reproducible; a check fails when a generated
  consumer is stale.

## 3. Tenancy is explicit at every boundary

- No ambient tenant on a shared singleton. Every read, write, schedule decision and
  fact carries an explicit scope; a missing or foreign scope fails closed.
- Composition (which source, effect adapter, policy, credential reference and clock
  a tenant uses) is resolved per tenant per request from configuration, not by
  reassigning a process-global field.
- Cross-tenant reads, cursors, replay identifiers and cursors in URLs are rejected
  as scope errors, never served as empty success.
- One tenant's unavailable store or source cannot make another tenant's request
  succeed quietly.

## 4. Distribution: state the guarantees a deployment actually provides

Multi-node operation changes what "once" means. A deployment must declare, and
enforce, the following; where it cannot, it must say so instead of implying safety.

- **Fact identity is enforced by storage**, not by process-local dedupe: a stable
  fact key (tenant, subject, fact type, decision, revision) is unique in the store.
  Two nodes writing the same fact yield one row, not two.
- **Scheduled work is leased.** A routine executes once per due window across the
  fleet; local tickers may propose work but cannot be the exclusivity mechanism.
- **Effect boundaries state their authorization atomicity.** If a claim and a
  dispatch cannot be made atomic across nodes, the deployment says so where the
  effect is recorded, and the recovery path is reconciliation, not retry.
- **Readers scale horizontally** without coordinated in-process state; ordered
  fact logs plus cursors are the read model.
- **Opt-in + conditional writes** remain the concurrency primitive for projections;
  a stale expected revision is refused by the owning writer, not by caller etiquette.

## 5. Portability is configuration, not code branches

Deployment-specific values — tenant identity, host and endpoint bindings, storage
driver, queue/lease provider, clock source, credential references, surface origins —
are configuration resolved at composition time. Code paths do not branch on
"which customer this is".

- Swapping storage, queue or clock changes no semantics and no contract version.
- Credentials are references to an existing owner's broker, never inline values,
  never surfaced in records or logs.
- A portable export replaces local bindings and owner identity; it does not inherit
  another deployment's data, credentials or authority.

## 6. Deployment profiles gate what may be observed

- A deployment declares a profile (for example production, staging, qualification).
- A source may declare the profiles in which it is observable. A synthetic or
  fixture source is legitimate **only** in a non-production profile; in production
  it is refused by configuration, not by code review discipline.
- Fixture output can qualify machinery and can never be presented as a business
  outcome or as live consumer proof (contract09 §Cross-component acceptance).
- "No source configured" is a normal, visible state — with an explicit reason and
  next action — not a dead end and not an empty success.

## 7. Acceptance is falsifiable, and shared by every deployment

A deployment satisfies this amendment only when these hold as automated checks:

1. Adding a source/condition/effect requires registration plus configuration only.
2. Adding a fact type changes one contract source; server, CLI and vocabulary are
   regenerated, and a stale generated consumer fails the build.
3. Two tenants with different sources and credentials run in one process; a
   cross-tenant read fails closed.
4. A storage or clock implementation swap leaves the full suite green.
5. Two reader processes against one store lose no facts and duplicate none.
6. Two scheduler nodes step one routine once per due window.
7. A fact written concurrently on two nodes produces exactly one stored record.
8. A production profile refuses a fixture source; a qualification profile accepts it.
9. A surface artifact can be replaced and pinned by digest without rebuilding the
   runtime, and the runtime reports which artifact it serves.

Absent evidence for any item remains *unknown*, never satisfied.

## 8. Explicit non-goals

- No universal store that copies other owners' facts, memory or outcomes; owners
  keep their facts and the loop links them (contract09 §Feedback).
- No second registry, scheduler, permission store, identity or workflow authority.
- No component catalogue that becomes an execution surface.
- No specification-by-code: a mechanic that changes semantics is written here first.

## 9. Owner decision required

Approval of this amendment is the Canonical Owner Principal's. Until approved it is
a proposal, and implementations must not claim conformance to it. The Core adapter
records its own coverage and gaps; its presence does not prove portable conformance.
