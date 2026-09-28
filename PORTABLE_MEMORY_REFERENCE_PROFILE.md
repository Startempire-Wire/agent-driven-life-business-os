# Portable Memory Reference Profile

**Status:** LIVE portable memory integration contract<br>
**Schema family:** `agent.memory_contract.v1`<br>
**Applies with:** `AGENTS.md`, `OWNER_AUTHORITY_CONSTITUTION.md`, `AGENT_CONTRACT_OPTIMIZATION_PROFILE.md`, `CURRENT_ECOSYSTEM_ARCHITECTURE.md`, `AMBIENT_OPERATOR_REFERENCE_PROFILE.md`<br>
**Evolution class:** `portable_operational` (portions touching privacy, tenancy, deletion and authority are `safety_authority`)<br>
**Version:** `0.1.1` (incubating — not a settled contract)<br>
**Last substantive revision:** 2026-09-28<br>
**Architecture authority:** deployment Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`<br>
**Startempire binding:** Verious Smith III<br>
**Reference implementation:** Wirebot/OpenClaw memory stack (memory-core, memory-wiki, active-memory, wirebot-memory-bridge, Mem0, Letta), Focusa, Agent Wiki, Context Core<br>
**Research basis:** arXiv 2603.07670, 2607.21503, 2609.24971, 2608.11775, 2609.08279, 2608.28978, 2609.05339, 2607.27080

This document is a **living contract**. It is expected to change as deployments produce evidence. It is not a finished specification, and "we wrote it down" is never a reason to stop revising it. See §16.

## 1. Purpose

A life/business OS needs memory that survives sessions without becoming a surveillance archive, a cost sink, or a source of confidently wrong answers.

The portable law is:

> **Memory is a governed, budgeted, evictable lifecycle — not a store.**

This profile defines the portable contract for memory across the substrate: what tiers exist, who may read them, how a record is promoted, how it decays, and how a deployment proves recall works.

Three properties are load-bearing:

```text
BOUNDED      every read has a token budget; memory never crowds out the task
ATTRIBUTED   every record carries source, trust class, freshness, and authority
EVICTABLE    forgetting is a first-class, audited, restorable operation
```

A system with durable storage but no lifecycle discipline is a liability, not an asset. Stale or hallucinated recall is worse than no recall, because the owner cannot tell the difference.

## 2. Memory is a lifecycle, not a store

Agent memory failures are usually misdiagnosed as storage failures. The dominant cause is unmanaged reasoning context: accumulating history, oversized tool output, and context that grows every turn until the task is evicted.

The portable formalization is a three-phase loop coupled to perception and action:

```text
WRITE   observe → filter → attribute → detect conflict → store async
                       ↓
MANAGE  consolidate → version → detect contradiction → decay → forget
                       ↓
READ    gate → cheap retrieve → filter → expensive rerank → budget → generate
```

Each phase has an explicit budget and an explicit authority. A deployment that implements only the read path has a search engine, not memory.

## 3. Substrate mapping

Memory is not a separate subsystem. It is the persistence and recall surface of existing substrate primitives.

| Substrate primitive | Memory role | Authority |
|---|---|---|
| Canonical Owner Principal | Owner of all memory; sole authority to read, export, or forget | Root |
| Identity + tenancy | Namespace isolation; no implicit cross-scope retrieval | Mandatory |
| Source + provenance | Every record carries source, timestamp, trust class, freshness, supersession | Mandatory |
| Capability + policy | Memory never confers capability, permission, or scope; transport and recall grant nothing | Mandatory |
| Context + memory | Private source-aware retrieval, bounded disclosure, retention | Owner-scoped |
| Intent + Trajectory | Durable desired state — a distinct memory tier | Workstream |
| Work unit | Working memory for the current scoped task | Session |
| Evidence + receipt | Provenance for claims; the audit trail for promotion and eviction | Append-only |
| Outcome + correction | Dispute and correction as first-class, non-destructive | Mandatory |
| Learning + policy change | Consolidated semantic layer | Owner + delegated |
| Resource + leverage | Memory token, latency, and storage budgets as first-class spend | Bounded |
| Observability + recovery | Health, audit, contradiction, restore | Mandatory |

`Orchestration`, `Execution adapter`, and `Workforce role` are deliberately unmapped: they are runtime-execution concerns, not memory concerns.

## 4. The five tiers

| Tier | Scope | Latency budget | Content | Retention |
|---|---|---|---|---|
| **Working** | session | 0 ms (already in context) | current task state, active decisions | session end |
| **Prefactor** | principal | 0 ms (cache) | stable facts: preferences, channel policy, identity, pinned directives | until superseded |
| **Episodic** | principal + workstream | 20–70 ms | what happened, when, in which conversation, with outcome | policy + decay |
| **Semantic** | principal | 70–500 ms | durable facts, decisions, preferences, lessons | until retired |
| **Archive** | principal | async | evicted/retired records, restorable | retention policy |

Two properties matter more than the names:

- **Prefactor never touches a retrieval pipeline.** Stable facts are served from cache. Asking a vector store "is this channel private" is a latency bug, not a correctness question.
- **Archive is not deletion.** Eviction moves a record to archive with a restore pointer. Deletion is a separate, authorized, auditable act.

## 5. The write path — governed promotion

This extends the Ambient Operator promotion contract (§6 of that profile). Nothing becomes durable by being said.

```text
observation
  → write-path filter      is this durable and non-duplicate?
  → privacy class          which retention/treatment does it inherit?
  → trust + attribution    source, actor, timestamp, evidence ref
  → contradiction check    same subject+predicate, conflicting value?
  → store ASYNCHRONOUSLY   after the response, not before it
  → schedule consolidation if superseded or threshold crossed
```

Rules:

1. The write path filters. Most observations do not deserve a memory operation.
2. A record is attributed before it is stored. Unattributed memory is unverifiable and must be rejected.
3. Conflicts are **flagged, never silently last-write-wins.** Resolution requires authority or explicit operator action.
4. Writes are asynchronous by default. Deferring storage until after the response removes memory cost from turn latency.
5. Absence of a record is not absence of a fact. Do not store "user declined to state" as a preference.

## 6. The manage path — consolidation, versioning, decay, forgetting

Long-lived stores accumulate stale records. Without mechanisms, an agent cannot distinguish the 2024 value from the 2022 one.

Required manage operations:

- **Temporal versioning.** Prefer the newest record; never overwrite history. Every record retains its predecessor.
- **Source attribution ranking.** An explicit statement from the owner outranks agent inference, which outranks a derived summary.
- **Contradiction detection.** Flag subject+predicate conflicts for resolution. A detected conflict is a visible state, not a silent merge.
- **Periodic consolidation.** Scheduled sweeps merge duplicates and retire superseded entries.
- **Decay.** Score by importance × recency. Stale state must lose to current state without being deleted.
- **Selective forgetting.** Eviction is allowed and expected, and must be auditable: record what was evicted, why, and how to restore it.

Retention is policy, not a default. A deployment MUST declare retention per privacy class before collecting.

## 7. The read path — the latency-critical surface

```text
request
  → [0] Prefactor cache hit?          serve directly                0 ms
  → [1] Retrieval gate: ambiguous?     no → answer without retrieval 0 ms
  → [2] Stage A: BM25 ∥ metadata ∥ ANN  cheap parallel candidates   20–70 ms
  → [3] Filter: freshness ∥ authority ∥ privacy class                1–5 ms
  → [4] Stage B: cross-encoder rerank   top-K → top-n                50–150 ms
  → [5] Token budget                    memory ≤ B, task first       0 ms
  → [6] Progressive generation         start emitting during [4]
  → generate with cited, attributable memory
```

Rules:

- **Two-stage retrieval.** Cheap retrieval wide, expensive rerank on top-K. This is where precision recovers at acceptable cost.
- **Retrieval-or-not gating.** Straightforward requests must not pay the pipeline.
- **Token budgeting.** Allocate context between memory and current task explicitly. The task wins.
- **Progressive retrieval.** Begin generating while the reranker runs.
- **Dynamic routing.** Escalate to the full pipeline only when ambiguity is high.
- **Attribution in output.** Retrieved memory is cited, so the owner can distinguish remembered fact from inference.

Latency reference: retrieval pipelines commonly add 200–500 ms. If total turn latency is measured in tens of seconds, the bottleneck is context management, not retrieval.

## 8. Context lifecycle and cost

- Cap every tool result before it enters the transcript. A large schema dump must never be inlined.
- Compact, summarize, or defer oversized tool output to a reference the model can fetch deliberately.
- Instrument and alert on turn latency, memory tokens per turn, retrieval calls per step, and store growth.
- A memory system that improves accuracy by unbounded time or token cost is making an unreasonable tradeoff.

## 9. Namespace, tenancy, and disclosure

- Memory is namespaced by tenant, principal, project, workstream, and session. Implicit cross-scope retrieval is prohibited.
- Namespace isolation is mandatory, not optional.
- Retrieval returns bounded projections. A project consumes the slice relevant to it, not the global store.
- Precise owner-life context stays in the owner-domain context service and is projected, never copied wholesale.

## 10. Provenance, trust, and authority

Every durable record carries, at minimum:

```text
subject / predicate / value
source (who or what observed it)     trust class
observed_at / effective_at           freshness
authority (who may change or forget)  supersedes (pointer to predecessor)
evidence_ref (receipt or handle)     privacy_class
```

Memory is not an authority surface. A remembered fact never grants permission, scope, or consent. Authority comes from the owner and the owner-rooted delegation chain, not from what an agent once stored.

## 11. Privacy classes and retention

Aligns with the Ambient Operator privacy classes (§12 of that profile):

```text
PRESENCE_SIGNAL
TRANSCRIPT
RAW_AUDIO
PRETRIGGER_WAKE_BUFFER
PRECISE_LOCATION
PROMOTED_SEMANTIC_STATE
```

Each class has independent purpose, storage, retention, export, and deletion rules. Generic telemetry never inherits permission to collect conversation, audio, or location.

Deletion must remove data from every tier, including derived indexes and archives, and must be auditable. Deleting a record while leaving a derived embedding is not deletion.

## 12. Portability and model migration

Model upgrades are routine; memory migrations are not. A memory store can persist while recall silently degrades.

- Pin and record the embedding model and dimensionality per index. Mixed embedding versions break retrieval.
- Before a model or embedding change, run the causal evaluation (§13) against the new configuration.
- Version memory records with the model/embedding generation that produced them.
- Keep derived indexes rebuildable from the canonical source; a migrated index is never the sole copy.

## 13. Evaluation — proving recall works

Passive recall is not memory. A benchmark that asks "retrieve this known fact" cannot detect whether memory is actually used.

### Causal evaluation

The only reliable proof is differential:

```text
success WITH the relevant history   (required)
failure WITHOUT the relevant history (required)
```

If an agent succeeds without the memory, the memory is not contributing and the benchmark is unfalsifiable. A mirror index that duplicates the source will always pass a similarity test while the real store is broken — this is a common and subtle failure, and a **null-memory control arm is mandatory**.

### Four-layer metric stack

| Layer | Metrics |
|---|---|
| 1 Task effectiveness | success rate, factual correctness, plan completion |
| 2 Memory quality | precision/recall, contradiction rate, staleness distribution, coverage |
| 3 Efficiency | latency per memory op, memory tokens per turn, retrieval calls per step, store growth |
| 4 Governance | policy compliance, deletion/audit coverage, authorization on mutation |

Measure the Pareto frontier of accuracy against latency and cost explicitly. Do not let a memory system buy accuracy with unreasonable time.

### Memory-specific competencies

Probes should cover accurate retrieval, test-time learning, long-range understanding, and selective forgetting. Most systems fail conspicuously on selective forgetting; a deployment that never tests it will discover the failure in production.

## 14. Security and integrity

- Treat all inbound content — including owner messages relayed through untrusted channels — as untrusted input. Memory poisoning is a persistence-to-consequence threat class, not a theoretical one.
- Promotion into semantic memory requires attribution and, for sensitive classes, authorization.
- Memory mutation is an authoritative act. A runtime without a canonical control plane must define and enforce the write-authority boundary rather than inherit ambient write.
- Contradiction and deletion are auditable operations with receipts.

## 15. Reference deployment mapping

| Portable role | Startempire reference |
|---|---|
| Working memory | OpenClaw session context window |
| Prefactor cache | Config/identity directives, pinned facts |
| Episodic store | memory-core `memory/*.md` + derived FTS/vector index |
| Semantic store | `MEMORY.md` (curated), consolidated |
| Structured state | Letta (goals, KPIs, checklists) |
| Cross-surface episodic | Mem0 (namespaced, Qdrant projection) |
| Durable knowledge | Agent Wiki |
| Owner-domain context | Context Core |
| Authority / work continuity | Focusa |
| Sync / reconciliation | wirebot-memory-syncd (transport only) |
| Evaluation | retrieval-eval + a causal (with/without) harness |

Mapping is illustrative. A deployment may substitute adapters, but the roles, authority, and budgets above are the portable contract.

## 16. Living maintenance

This profile is a living contract governed by `AGENT_CONTRACT_OPTIMIZATION_PROFILE.md`. It is never `final`.

### Change triggers

Reopen this contract when any of these occur:

| Trigger | Required response |
|---|---|
| A deployment shows a memory-caused task failure | record the incident; propose the smallest delta |
| Retrieval latency regresses beyond its stated budget | re-evaluate §7 routing and §4 tier placement |
| Recall regresses while a similarity metric looks healthy | re-open §13; a passing metric is not evidence of use |
| An embedding or model generation changes | run §12 migration checks before rollout |
| A privacy, tenancy, or deletion defect appears | `safety_authority` class — higher evidentiary floor |
| A new memory backend or pattern is proposed | test against the §4 roles before adding a tier |
| New research invalidates a latency or accuracy claim | cite it; revise; record what remains unproven |

### Bounded evolution loop

```text
OBSERVE → ATTRIBUTE → CONSOLIDATE → HYPOTHESIZE → STAGE
        → VALIDATE → COMPARE → OWNER/ARCHITECTURE GATE → ROLLOUT
```

No section is exempt. A well-reasoned paragraph is a proposal, not a promotion.

### Promotion levels

Use honest state, not "final":

```text
observed → corroborated → proposed → regression_tested
         → approved → rolled_out → verified
                            ↘ reverted (reason retained)
```

A commit is not `verified`. A transcript is not `approved`. A passing model critique is not a behavioral regression test.

### Minimum acceptance before a version bump

1. Target and evolution class explicit;
2. causal problem tied to source evidence or deterministic reproduction;
3. ownership routing checked (§17);
4. smallest semantic delta that solves the problem;
5. removals/weakening clear the higher evidentiary floor;
6. protected invariants tested;
7. material semantic changes have held-out cases;
8. required owner/architecture authority satisfied;
9. native consumers verified when placement changed;
10. post-rollout observation planned or completed;
11. private evidence has not leaked into portable source;
12. version and revision log record what changed **and what remains unproven**.

### Revision log

| Version | Date | Change | State |
|---|---|---|---|
| 0.1.0 | 2026-09-28 | Initial portable memory lifecycle contract. Derived from a live Wirebot incident (retrieval eval structurally unfalsifiable, dead memory backend masked by health checks, context bloat evicting conversation history) and 2026 agent-memory research. | incubating |
| 0.1.1 | 2026-09-28 | Quality pass. Verified all 8 research citations resolve to the cited titles. Mapped the two omitted substrate primitives (`Capability + policy`, `Resource + leverage`). Added the explicit doctrine-versus-runtime-truth boundary required by `CURRENT_ECOSYSTEM_ARCHITECTURE.md` §3, and recorded that **transcript memory currently has no named owner** (§17.1). Not yet addressed: no customer install path (§18 checklist is not a setup contract), memory is not a declared cross-product seam, and vertical worked examples are thin. | incubating |

### Known unproven

- Tier latency budgets are starting targets, not measured on any deployment.
- Hybrid fusion parameters and rerank depth are unspecified; a deployment must measure its own Pareto frontier.
- Decay scoring function is described but not normalized; importance × recency weighting is untested at scale.
- No customer deployment has yet validated the causal evaluation harness end to end.

## 17. Ownership routing

**This profile is portable integration doctrine. It is not a runtime, a database, or a memory store.** Consistent with `CURRENT_ECOSYSTEM_ARCHITECTURE.md` §3, ADLBOS **does not own runtime learning truth or transcript memory**. This document defines the portable contract an owning product implements; it never holds a customer's memory, never becomes the canonical store, and never promotes itself from doctrine into authority.

```text
portable cross-product memory doctrine defect   -> ADLBOS (this repository)
agent runtime / Focusa work+authority defect     -> Focusa
Wirebot context / Operating Partner defect       -> Wirebot
transcript memory truth and retention             -> the deployment's named
                                                    product owner (§17.1)
execution, browser, computer defect               -> UIAI Engine
accepted-outcome / correction / economics defect -> W.I.N.S.
product-specific memory behavior                 -> owning product repository
```

### 17.1 Open ownership item

`CURRENT_ECOSYSTEM_ARCHITECTURE.md` §3 disclaims **transcript memory** for ADLBOS. No product currently claims it explicitly. Until the Canonical Owner Principal assigns an owner, transcript memory is **unowned** and a deployment must not assume any product holds it canonically. Resolving this is an architecture-authority decision, not a contract-editing decision.

## 18. Implementation and adoption checklist

A deployment should not claim portable memory parity until it proves:

- [ ] five tiers exist with distinct scopes, latency budgets, and retention;
- [ ] governed promotion path from observation to durable state;
- [ ] attribution on every durable record;
- [ ] contradiction detection with visible, non-silent conflict state;
- [ ] temporal versioning and periodic consolidation;
- [ ] selective forgetting with an auditable restore path;
- [ ] prefactor cache serving stable facts without retrieval;
- [ ] retrieval-or-not gating and a token budget that protects the task;
- [ ] two-stage retrieval with a rerank step;
- [ ] asynchronous writes;
- [ ] tool-output caps in the transcript;
- [ ] namespace/tenancy isolation verified by test;
- [ ] privacy classes with independent retention;
- [ ] deletion proven to reach every tier including derived indexes;
- [ ] causal evaluation with a null-memory control arm, in CI;
- [ ] four-layer metric stack, including efficiency, instrumented;
- [ ] embedding/model generation pinned and migration-tested;
- [ ] write authority defined and enforced.

## 19. Not-done conditions

Portable memory is not recovered if:

- a derived index is the only surviving copy of a record;
- the evaluation can pass without the memory being used;
- recall is claimed without a query proof;
- an invalid embedding or dead backend causes silent keyword-only degradation;
- health checks report process-alive while a memory dependency is unreachable;
- stale records outrank current ones;
- forgetting happens only by deletion of the source, leaving derived copies behind;
- memory is used as an authority or permission surface;
- a customer deployment inherits another tenant's memory;
- accuracy is purchased with unbounded latency or token cost.

## 20. Final principle

> **A portable agent OS must be able to remember what matters, say where it came from, admit when it is unsure, and let go of what is no longer true — all within a budget it can defend and an authority it respects.**
>
> **And it must be willing to be corrected by evidence for as long as it runs.**
