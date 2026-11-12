# SOVOS Master Loop — Modular Composition and Safe Evolution

Composition and evolution also obey [contract09](09-sovos-master-loop-composable-provenance-and-agent-first-contract.md):
separate definitions/instances/invocations; preserve each component's identity,
purpose, typed boundaries and evidence; trace effects across nested loops without
inventing causality. API/CLI are agent-first; shared visible maps and records must
remain understandable and disclose incomplete coverage as components evolve.

**Status:** INCUBATING — detailed architecture candidate; memory-provider bindings provisional.<br>
**Draft revision:** 0.8.1, 2026-10-15 — memory portability reconciliation; no activation or parity claim.<br>
**Owner intent:** growth, interchangeable/composable elements and several upgrade paths must be designed before building.<br>
**Boundary:** documentation only; no plug-in loader, schema, module installation, executable graph or activation created.<br>
**Parent:** [whole organism](02-sovos-master-loop-draft.md).<br>
**Behavior / interfaces / worked decisions:** [05](05-sovos-master-loop-integration-blueprint.md), [06](06-sovos-master-loop-contract-and-policy-resolution.md), [07](07-sovos-master-loop-planning-closure-and-worked-decisions.md).<br>
**Evidence / existing proofs:** [source register](04-sovos-master-loop-source-and-integration-register.md), [scenario annex](03-sovos-master-loop-alarm-and-simulation-design.md).

## 1. Load-bearing architecture, not an optional future bolt-on

The Master Loop is a **stable coordination contract over independently owned, replaceable capabilities assembled into accepted compositions**. Preserve the whole organism: purpose, sensing, expectations, alarms, routines, existing teams, judgment, execution, receiver acceptance, follow-through, memory, health and learning. Its first working case must not become a hard-coded architecture that blocks later growth.

“Stable core” means the control semantics already owned by the owner, Focusa, source/executor systems and memory/retention authorities. It does NOT mean a new kernel service, universal state store, broker, registry, scheduler or renderer. An owner-approved constitutional change can evolve those semantics; an installed module cannot override them.

```text
owner purpose / source truth / current authority
          ↕ existing coordination and control owners
accepted composition → exact capability contracts → pinned module bindings
          ↕ scoped inputs, results, events, receipts and revisions
replaceable connector / engine / routine / worker / verifier / memory / surface
          ↕ source/receiver reconciliation and bounded improvement
```

Modules may be pure functions, existing runtime plug-ins, native APIs, bounded jobs, human providers or isolated services. A module does not require another always-on agent/process. Prefer the smallest existing owning primitive. Host packaging is replaceable; the capability contract, state ownership and accepted result remain explicit.

### 1.1 Existing owners reused

| Existing home | Reuse / boundary |
|---|---|
| [Cross-product seams](../CROSS_PRODUCT_SEAM_CONTRACT.md) | Source-qualified refs, producer/contract version, causal revision, current authority, replay and unknown result; no central bus/clock/store |
| [Routine compiler/library](../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md) | Templates/packs, owner blueprint, frozen instance and semantic linking; no separate module workflow engine |
| [Intelligence/composition architecture](../SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md) | Existing four result/engine/composition/component registries; no page or registry for every algorithm |
| Focusa/source/executor contracts in 05 §11 and 06 | Exact operation/effect/verification/continuity/resource authority; discovery is not execution |
| OpenClaw owning runtime and product plug-ins | Actual manifest/loader/slot/tool rules when qualified; not arbitrary callback code bypassing governed effects |
| [Portable memory profile](../PORTABLE_MEMORY_REFERENCE_PROFILE.md) and existing memory owner | WRITE/MANAGE/READ, five tiers, eligibility/privacy/review/delivery/recall and writer law; no sixth store or replacement approval queue |
| [Contract evolution](../AGENT_CONTRACT_OPTIMIZATION_PROFILE.md) | Evidence-based bounded proposal, protected invariants, held-out regression and owner promotion; no automatic learned policy authority |

A “module descriptor” below is a logical contract profile mapped onto the owning product's existing descriptor/manifest. If fields/operations are absent, accept a versioned owning extension; no new portable module registry/schema is installed here.

## 2. What can change and what cannot be inherited

| Stable meaning / owner | Replaceable implementation | Replacement must preserve |
|---|---|---|
| Exact source identity/truth | Connector transport/provider adapter | Scope, revision, coverage, attribution and operation semantics |
| Accepted expectation / current due time | Native watch/scheduler adapter | Calendar/intent revision, cancellation, supported checks and source truth |
| Concern continuity / Wirebot | Storage implementation or projection adapter under that owner | Conditional revision, responsibility, lineage and unresolved effects |
| Question / judgment policy | Rules, model, engine or permitted specialist | Typed meaning, allowed options, privacy, error costs, budget and abstention |
| Routine / full work acceptance | Template composition, procedure adapter or executor body | Exact accepted semantics, dependencies, current grants, outcome and whole-scope return |
| Workforce responsibility | Human/agent/provider implementation | Actual acknowledgement, scope/context, generations and incumbent work |
| Independent verification | Qualified source/receiver/verifier adapter | Predicate, independence, objections, current evidence and settlement role |
| Memory treatment / existing memory owner | Backend, contributor, retrieval/reranker/index or delivery adapter | Eligibility, correction, privacy, tier meaning, stable source refs and one writer |
| Human meaning / existing presenter | Channel, trusted component or layout composition | Same current source revision, supported actions and attention/closure distinctions |
| Health/value/learning | Diagnostic or analytical instrument | Coverage honesty, hard boundaries, accepted outcomes and total burden |

A module swap does not change owner/Operating Partner identity, create a new obligation, renew a budget, adopt a different project, reset a provider idempotency key or confer old credentials. Replacement availability, functional compatibility, data treatment and authorization are separate determinations.

### 2.1 Memory portability is part of composition acceptance

Apply [Portable Memory §1.1/§19](../PORTABLE_MEMORY_REFERENCE_PROFILE.md#11-required-portability-and-ecosystem-acceptance) to the same memory capability used by Wirebot, its App, selected channels and delegated workers. Windows, Linux and macOS bindings replace supervision/filesystem/transport/provider mechanics without replacing the owner, grants, memory truth or WRITE/MANAGE/READ lifecycle. Reference KH/OVH routes, Linux commands and personal namespaces cannot become product requirements. Resolve one existing installation's scoped memory connection, not a per-surface login or an owner/admin token shared with workers. Selected optional modules remain optional; required capabilities and source revision, correction/deletion propagation, latency/resource and recovery checks remain load-bearing on each supported combination. Same-client moves and fresh-client isolation use the existing migration/credential owners, not a second control plane. Unproven platform or consumer agreement is a readiness gap, not accepted interchangeability.

## 3. Logical module contract profile

Each selected binding supplies the following semantics through current owning descriptors or an explicitly accepted extension. These are NOT added fields in `operator.routine_instance.v1`; 06 §4's existing refs remain the connection points.

| Contract dimension | Required declaration / validation | Missing or unsupported behavior |
|---|---|---|
| Identity/provenance | Source-qualified module/provider owner, capability role, immutable artifact and trusted provenance | Untrusted name/package cannot become an allowed operation |
| Contract | Exact input/output/error schema refs, semantic version and compatibility evidence | Reject consequential unknown shape/meaning; no guessed coercion |
| Implementation | Exact module/artifact/runtime revision separately from public contract version | Package semver alone does not establish compatibility |
| Scope | Principal/tenant/domain/environment, permitted subjects/recipients and placement | No ambient cross-client or body-wide access |
| Capabilities | Explicit offered operations, effects and supported hook roles | Catalog presence is not support or permission |
| Configuration | Typed constraints, units, secret-use refs, ownership and missing-value behavior | No credentials/private bodies in manifests; required unbound values block affected capability |
| Dependencies | Required/optional/exclusive roles, exact constraints and fallback semantics | No hidden required dependency or silent optional-to-required promotion |
| Inputs/results | Source/context revisions, applicability, output validity/expiry and cancellation | Late/wrong-scope results rejected; error is not empty/success |
| Invocation | Synchronous bounded call, asynchronous request/return or event subscription; deadline/correlation | Caller knows completion boundary; dispatch acknowledgement is not result |
| Events | Owning namespace/type/version, origin/revision/cursor, scope, coverage, delivery/replay ordering | Duplicates/out-of-order/gaps explicit; no global total-order assumption |
| Authority/effects | Current registered operation, target/argument bounds, grant/renewable credential/confirmation refs | Host/plugin installation cannot inherit mutation permission |
| State | Canonical owner versus local/derived state, state version, checkpoint and retention/export/deletion | No module-private authoritative shadow of CRM/tasks/grants/outcomes/memory |
| Reliability | Timeout/retry/backpressure, idempotent intent/reconciliation, overlap and failure disposition | Unknown effect reconciles; no fresh-key retry |
| Lifecycle | Readiness, pause/drain/revoke, fencing, outstanding return routing and retire behavior | Failed readiness never displayed enabled; disable is not source cancellation |
| Upgrade | Old/new compatibility, migration/takeover/callback handling, reversibility limits | No unsafe hot replacement or rollback promise |
| Budgets | Child/shared allocation, API/model/CPU/memory/time/money/attention caps and epoch | Aggregate caps enforced by owner; module replacement cannot replenish them |
| Proof/observability | Conformance/consumer/version/readiness evidence, sanitized health and source-backed receipts | Process-alive/discovery/compilation cannot prove installed consumer behavior |

Stable **capability identity**, public **contract version**, exact **artifact revision**, owner-specific **binding revision**, accepted **routine revision**, execution **generation** and **state/index generation** are distinct. Current permission is re-resolved; it is not a cached property of any one version tuple. Owning canonical serialization/digest covers material semantics; this profile invents no signing/hash convention.

A read-only stateless module need not implement write/migration hooks it does not use. It must declare them inapplicable, rather than expose success-shaped no-op methods. A stateful effect producer cannot declare these controls optional merely to simplify its adapter.

## 4. Explicit hook/port boundaries

Logical names specialize 05/06's existing operations. They are not registered routes, runtime hook names or a new event API. Bind every selected port to its actual producer/consumer/version, input/result and current control boundary.

| Attachment point | Consumes → returns | Guard / forbidden shortcut |
|---|---|---|
| Observe / connector | Permitted source query/cursor → attributed observations and coverage | Reads authorized; failed source is unknown, not absence |
| Expect / watch | Accepted intent/time/predicate → supported watch ref/posture/check | No invented obligation or timer-per-agent requirement |
| Relate / interpret | Scoped evidence/context → proposed relation or finding | Candidate meaning is not promoted truth; no automatic case/effect mutation |
| Analyze / judge | Applicable typed question/information set → result/abstention | Asynchronous where semantic; no inline model prerequisite to hard safeguards |
| Compose / compile | Accepted roles/policies/operations → linked version-pinned composition proposal | Type match alone is insufficient; semantic/effect/authority constraints validated |
| Assign / coordinate | Existing work/capacity → retained or genuinely accepted responsibility | Role name or availability is not human acceptance |
| Execute | Current admitted intent/inputs/generation → real receipt or partial/unknown result | Only actual registered effect owner can mutate; no callback-direct bypass |
| Verify | Independent source/receiver evidence → accepted/disputed/failed/unknown finding | Executor may provide evidence, not certify its own desired outcome |
| Continue / close | Current accepted scope/gap/outcome → next valid move or terminal projection | Empty queue or one branch cannot settle whole scope |
| Memory WRITE/MANAGE/READ | Eligible scoped candidates/requests/corrections → review/delivery/recall/treatment dispositions | Existing memory authority/writer/retention; no raw transcript promotion |
| Present | Current source-bearing meaning/action refs → approved channel/component | Presentation state is not source resolution; private export separately qualified |
| Health / learn | Bounded faults/results/metrics → diagnosis or revision proposal | No safety bypass, self-grant or self-promotion from a model/result |

Synchronous admission/validation hooks are deterministic, bounded and owned by the actual authority. Optional model-backed interpretation and learning run outside that hard path. Exceptions/timeouts return safe typed disposition; fail-open is not a module option for mandatory safety checks.

### 4.1 Event and return semantics

Events travel through the existing source/runtime/scheduler subscriptions. The composition records exact subscribed predicate/projection and consumer cursor, not a copy of the source database. At-least-once/redelivery and out-of-order events require owner dedupe, current revision checks and a declared gap/reconciliation policy. Event delivery is not source-completeness proof.

A consumer acknowledges a durable checkpoint only at its declared processed/reconciled boundary. If a downstream projection fails, the owner retains retryable work or re-read/reconciliation without advancing past lost required evidence. An asynchronous request records exact request/input/binding/generation and expiration; its result returns to that subject, not whichever new module is currently selected.

Cancellation has the actual prevention/requested-stop/pending/completed/unknown distinctions from 07 §3. Old callbacks route to their original owning reconciliation boundary or are safely rejected with the pending effect still recorded. Dropping a callback does not settle an effect. Event feedback retains origin/causal lineage; self-generated mirrors cannot recursively create new intents.

## 5. Composition, linking and conflicts

The existing compiler links capabilities rather than import provider names into every routine. An accepted blueprint selects exact capability contract/binding refs, permitted parameters and dependencies; the instance freezes that selection. Discovery may suggest substitutes; runtime cannot resolve “latest/best available” into a new implementation with different semantics or disclosure.

| Composition check | Required result |
|---|---|
| Interface compatibility | Required inputs/outputs/errors have supported semantics, units, validity and scope; syntactic shape is only the first check |
| Capability completeness | Every required role has a qualified supported/accepted extension binding; optional role has an explicit absent/unavailable path |
| Dependency order | Acyclic initialization prerequisites; execution cycles only through the existing owner's supported explicit per-cycle policy and bounded exits. Purposeful delayed/event feedback has stopping/budget rules, not hidden recursive calls |
| Multiplicity | Exclusive writer/slot roles select one admitted implementation; many read-only contributors require declared aggregation, dedupe and output caps |
| Conflicting producers | Owner-defined precedence/verification or explicit unresolved conflict; no last-loaded, package-order or model-majority winner |
| Effects/placement | Explicit existing kind/consequence translation and allowed host/route; data locality and resource limits preserved |
| State/control | Owning revision/generation, checkpoint/revoke/retention and current guards cover every consequential entry path |
| Verifier separation | Actual independent acceptance role and evidence return; changing executor cannot silently replace its verifier |
| Graceful degradation | Optional capability removed only through accepted behavior; required unavailable module blocks dependent paths, independent permitted work continues |
| Whole-scope coverage | Full Trajectory requirements/branches and shared work accounted once; module success is not whole outcome |

Mutable runtime projections of health/results remain linked to the frozen composition; they do not rewrite it. An additive capability may coexist without altering existing instances. If semantics, state, privacy, outputs or allowed effects change, use a reviewed binding/instance revision and the upgrade protocol below.

Logical composition is not a demand for microservices. A local function/API can satisfy a port; a long-running process is justified only by actual persistence/placement needs. Existing human work is a valid provider. Use boundary adapters for real protocol differences, not speculative general-purpose frameworks.

### 5.1 Worked composable growth, not arbitrary plug-in insertion

Use 07's fictional owner A / inquiry `I7` / existing VA `W7` / accepted instance `R7`. All labels below are synthetic capability bindings, not registered operations, configurations or real upgrades. `R7` retains source-owned commitment, one internal-notice ceiling, no customer send/payment, independent receiver proof and whole-scope return. Its hypothetical memory-module binding is **not final** while the owning blueprint is pending.

| Proposed change | What remains unchanged | Required accepted binding / rejected shortcut |
|---|---|---|
| Polling adapter → native event adapter for the same source | Exact provider/account/object truth, concern identity, VA ownership and effect intent | New observe binding proves equivalent predicate/coverage, cursor/reconciliation and duplicate/out-of-order handling; no assumed “webhook means complete coverage” |
| Rules-only interpretation → qualified local typed model | Hard checks, allowed question/options, scope and effect ceiling | Same reviewed semantic output or explicit changed policy revision, latency/disclosure/caps/abstention; no automatic hosting fallback or drafting from a choice |
| Add a life-renewal routine from an existing pack | Business A's frozen instance, source/worker/private data and existing schedule | Separate exact life source/calendar/role/authority/acceptance composition with shared-capacity reservation; pack/library install does not activate it |
| Read provider → future memory plug-in | Approved source/review identity, current eligibility/treatment and memory owner | §7's real two-sided role/version/result/state agreement first; no invented pending ABI or promotion from provider history |
| Replace embedding/rerank implementation | Canonical memory source and approval/correction law | New derived index/model/dimension generation plus null-memory/current-correction/quality/budget checks; never reuse incompatible vectors |
| Desktop composition → approved mobile presentation | Same current concern/outcome/action refs and source revision | Actual channel/recipient/privacy/reply/accessibility binding; no new inbox, renderer or broader lock-screen disclosure |

Link the proposed changed role in a candidate binding/instance revision; verify required/optional dependencies and current authority; use the dimension-appropriate shadow/drain/state protocol; read back the actual consumer selection and reconcile old callbacks/effects. Keep unrelated frozen instances on their old bindings until their own accepted migration. A source/provider change that changes canonical object identity requires an explicit owner-qualified mapping; interface similarity cannot preserve identity by assertion.

This example makes substitution local to a qualified role, rather than editing every workflow to know its new implementation. It does not promise a no-change swap when the semantic contract, privacy or state model changes. Those differences are a new accepted composition, not disguised compatibility.

## 6. Module lifecycle through existing owners

The following are logical dispositions, not new shared runtime enums. Map onto actual host/module/work contracts.

| Move | Entry / action | Exit / unavailable behavior |
|---|---|---|
| Discover | Read source-owned descriptor, role and artifact provenance | Listed candidate only; no install/access/authority implied |
| Bind / configure | Accept exact scope/version/config/dependencies/placement and role | Bound candidate or explicit incompatible/unconfigured disposition |
| Qualify | Producer/consumer/interop, denial, state/recovery and budgets for chosen capability | Qualified for declared scope/version, not every future operation |
| Shadow | Authorized permitted read/isolated evaluation; no real effect path and no production-context mutation | Compare accepted predicates without double dispatch, hidden spend or private export |
| Pilot / enable | Current approvals, readiness readback, routing/generation, verifier and bounded allocation | Actually enabled only after consumer confirms binding; install/config success alone insufficient |
| Operate | Current instance/source/control and budgets validated per invocation | Owned result/receipt/coverage or explicit fault; no runaway loops |
| Pause / drain | Fence new affected admission/subscriptions; settle/reconcile outstanding effects/returns | Known quiescence or explicit unresolved residuals, not automatic cancellation |
| Replace / migrate | Accepted old/new revision, state/control transfer and compatibility protocol | One admitted writer/route generation; source identity and effect intents preserved |
| Revoke / retire | Stop new use, remove scoped subscription/access through owner, preserve required treatment/history | Retired routing; source commitments/pending receipts/required data not deleted by uninstall |

Readiness includes actual consumer data path, source freshness, supported operation, required dependency/verifier and current grants. Healthy quiet differs from disabled, disconnected and draining. Failed optional modules remain inspectable; mandatory faults cannot be hidden behind successful unrelated modules.

Untrusted plug-in metadata, a permissive host callback and package-installed code are not proof of sandboxing. Local in-process code with ambient privileges is an explicit risk; choose the existing least-capability execution/isolated body boundary or keep it unavailable. Third-party artifacts require trusted provenance, declared dependency/license/update behavior and separately authorized installation. No auto-download/auto-enable from discovery.

## 7. Memory's pluggable layer: an evolving owned dependency

**Current operator clarification:** the memory plug-in blueprint is not complete. This document fixes what the Master Loop needs from that layer, not its final method names, ABI, loader, registry, field layout or storage architecture. Existing 06 B09–B12 are current inspected source boundaries plus proposed semantics, not a finished general memory plug-in interface.

### 7.1 Roles that can interchange without changing memory law

| Memory role / port family | Allowed modularity | Invariant / ownership boundary |
|---|---|---|
| Candidate contributor | Connector, completed case, primary loop or scoped worker proposes minimum experience/correction | Existing review/attribution/treatment path; contributor never approves itself |
| Promotion/review controller | Owning product can evolve its implementation | Approval/eligibility/reviewer authority remain at that owner; never two competing review queues |
| Delivery sink | Existing backend/provider adapters under approved fan-out | Exact source/review revision, sink binding, idempotent receipt and minimization; delivery is not recall/use |
| Read/retrieval provider | Lexical/vector/hybrid/other qualified retrieval implementation | Purpose/role/current eligibility and bounded disclosed results; current operator-only native recall cannot silently become worker-general |
| Embedding/rerank/index | Replace derived representation or candidate ranking | Exact model/dimension/index generation; canonical record/eligibility never derived from vector similarity |
| Context/prefactor projector | Approved cached facts or role-scoped retrieved slice | Token/expiry/source/correction checks; no raw history copying or policy lookup from untrusted memory |
| Consolidation/forgetting manager | Declared owned maintenance method | Attributed versions, contradictions and audited eviction; forgetting is not erasure or obligation cancellation |
| Mutable business-state sink | Existing memory owner's qualified writer receives primary-loop proposals | One writer generation, expected revision, live source reconciliation; native disabled until separate acceptance |
| Transcript/capture integration | Future accepted ledger/custody adapter | Conversation lineage, capture custody and retention are distinct; no automatic import/promotion/recording |
| Correction/erasure/restore adapter | Existing treatment authority propagates current eligibility across derivatives | Legal/treatment authority, denied stale recall and no restore resurrection; uncontrolled provider copies acknowledged |
| Evaluation/health | Independent consumer probe or null-memory/matched control | Private scoped inputs and effect-free evaluation; no vector similarity or process-alive readiness claim |

These are capability roles, not new memory tiers, databases or mandatory services. Source truth still wins over recall. A primary-loop state proposal and an approved-memory candidate are different operations. Multiple delivery sinks/read contributors are compatible with one logical memory authority; they do not imply multiple active mutable-state writers.

### 7.2 The pending two-sided binding agreement

| Master Loop requires | Memory owner must return once blueprinted | Interim posture |
|---|---|---|
| Purpose/tenant/domain/role-bound WRITE/MANAGE/READ and exact privacy/retention | Actual source-owned port/descriptor/version, arguments/results/errors and enforcement | Proposed capability requirement; no invented native fields or worker access |
| Submission/review identity, revisions, ambiguity and correction | Supported dedupe/conditional operations, reviewer/eligibility boundary and receipts | Existing queue semantics remain limited; lost POST acknowledgement reconciles rather than blind retry |
| Source→sink→eligible recall→actual use lineage | Exact stable source/review/provider refs, output coverage/validity and committed result meaning | Delivery/trace/recall/use remain separately evidenced |
| Memory module registration/selection/lifecycle | Actual registry/host ownership, required/exclusive slots, readiness/drain/revoke and compatibility | No Master Loop module registry created to fill the gap |
| Backend/index/state replacement | Source ownership, state/index versions, export/checkpoint, rebuild/restore/reverse-delta and single-writer generation | V1 remains; native/worker expansion/cutover unactivated |
| Retention/correction interaction | Declared consistency/disclosure/use boundary, derivative/provider treatment and restore rules | No universal erasure or atomic cross-system promise |

The exact agreement is a source-qualified two-sided contract, not a meeting ritual or another data store. If the future memory blueprint uses different role/grouping names, map semantics at its owning adapter; do not force these logical labels into its APIs. A weaker port cannot be accepted merely because its name resembles a needed capability.

### 7.3 Planned reconciliation when the memory blueprint is ready

1. Obtain its exact source/revision/status through the existing owner; distinguish proposed contract from installed support.
2. Match each required role above and 06 B09–B12 to its real producer/consumer port, versions, state ownership, budgets and acceptance; identify incompatible/missing guarantees explicitly.
3. Revise the affected Master Loop sheets, compiler bindings and module compatibility rows in place. Changes to privacy/writer/authority/retention need actual owner approval, not automatic semantic translation.
4. Accept exact extension/exclusion where necessary; no required seam is left for a coder to invent. Optional unrelated capability need not block a deterministic valid path.
5. Re-run planned producer/consumer/interop/denial/replacement/restore obligations after separately authorized implementation. Publication alone never qualifies a port.
6. Only then freeze the corresponding memory-dependent composition revision. Do not decompose/build the dependent interface while its consequential semantics remain unresolved.

This reconciliation is expected design work, not a surprise rebuild. It does not require changing the stable coordination law or every routine. No unattended watcher is installed to perform it, and the existing memory agent retains its assignment. Current memory-source docs/slot/bridge are evidence, not a substitute for the unfinished blueprint named by the operator.

## 8. Upgrade and adaptation dimensions

| Change dimension | What may remain stable | What must be reviewed/rebound/proven |
|---|---|---|
| Compatible patch/artifact fix | Public capability/state meaning and source identities | Exact old/new artifact contract/control/state compatibility; patch label alone is not evidence |
| Add/remove optional feature | Existing accepted instance behavior | Explicit optional branch/fallback, module scope/dependencies and aggregate caps |
| Capability provider swap | Typed semantic port and source-owned truth | New identity/route/privacy/placement/control plus conformance and state/result mapping |
| New input/output/semantic major version | Unaffected compositions | Explicit adapter/consumer migration; unknown consequential major denied |
| Template/routine/policy update | Partner, source subjects and completed intent receipts | New accepted binding/instance semantics; no latest-template reinterpretation |
| Model/prompt/judgment method | Already-permitted question purpose/options | Validation/calibration/error costs, output semantics, route/disclosure and cache generation |
| Memory backend/state substrate | Approved records/source IDs and eligibility authority | Treatment/state-version conversion, writer quiescence/generation, forward/reverse deltas, real consumer and restore proof |
| Embedding/index/retrieval change | Canonical records and review eligibility | New model/dimensions/index generation, rebuild from source, quality/denial/deletion tests and bounded routing |
| Runtime/process/body/host change | Owner and durable Operating Partner principal | Host grants/placement/lease/transport/CPU-memory/privacy and callback/state handover |
| Presentation/channel/UI component | Source meaning/action refs | Actual approved recipient/export/accessibility/feedback/operation support; no second renderer/inbox |
| New domain/module family | Existing core law and unrelated bindings | New exact capability semantics and domain/professional/consequence policy; no broad private access by category |
| Learned optimization/config tuning | Current goals/reserved powers and already-permitted choices | Bounded versioned proposal, independent held-out value/harm evidence and owner promotion where required |
| Scope/constitution/authority change | History and explicit stable identity lineage | Separate owner-rooted amendment/delegation/revocation; never a module auto-upgrade |

Support upgrade methods appropriate to the dimension: parallel old/new compatible **read** deployments, isolated shadow, explicit bounded canary, atomic owning-route selection, drain-and-replace, state migration or separately approved irreversible cutover. No universal zero-downtime/hot-swap/rollback promise. Remote providers may force protocol changes; required-incompatible paths become visibly unavailable, not silently coercible.

Shadow/canary still has privacy/read/spend authority and its own reservation. Shadow results cannot mutate production prompts/context/acceptance or dispatch external effects. A canary can perform only the exact accepted effects within its source subjects and allocation; it must not become an unbounded second writer. Compare semantic results and independent outcomes, not merely availability/answer similarity.

### 8.1 State and effect handover protocol

| Boundary | Owning action / required proof |
|---|---|
| Prepare | Resolve exact old/new tuple, compatibility and approval, prerequisites, state ownership, migration/reversal limits and allowed rollback target |
| Quiesce | Stop new affected admissions; drain or classify each in-flight request/effect/return; preserve useful pending feedback; unrelated admitted work may continue |
| Snapshot/checkpoint | Use the owner's consistent backup/export and actual watermark; expected state/cursor/eligibility/revoke generation; no default-to-zero or raw live-database copy |
| Transform/rebuild | Approved deterministic versioned mapping or source rebuild; preserve canonical IDs/revisions/eligibility/treatment; do not convert absent/unknown to success |
| Qualify candidate | Read back through actual consumer, check outputs/denials/state/retention/budgets; compare required independent outcomes and restore evidence |
| Select/fence | Owning conditional selection/generation admits one active write route; old callbacks reconcile under their original binding; current permissions independently re-resolved |
| Reconcile | Catch up from known watermark using allowed deltas; inspect source receipts before retry; old/new epochs cannot both create the same logical effect |
| Observe/retire | Bounded failure/quality/coverage window; remove old scoped routing/access through owner only after applicable residuals settled |

State transfer and code rollback are distinct. After new writes, reverting code alone may expose stale/invalid state. Reversal requires proven compatible state/reverse deltas/current correction/erasure lineage and quiesced writer generations. Irreversible or unmappable changes remain forward-recovery/Needs You; a backup file is not permission or proof of safe rollback.

Migration work has explicit allowed data projection, retention, destinations, budgets and failure horizon. Old callbacks/receipts preserve logical provider intent across compatible code/binding/worker changes. A new genuinely accepted intent has its own identity after prior effects are reconciled. State/index compatibility cannot be inferred from the same public API version.

## 9. Planned module and memory-extension conformance

**Full scope, focused verification:** the owner requires all specified capabilities, not a narrowed prototype deliverable. [Closure §8](07-sovos-master-loop-planning-closure-and-worked-decisions.md) removes unauthorized deferrals while preserving a first working milestone. Interchangeability, lifecycle, migration, isolation and resource behavior remain required; demonstrate relevant predicates as their implementations become ready. Do not create an unnecessary prebuild test platform or mark absent capability as qualified.

These twelve cases extend the base 24 predicates in 03; **ML-T25–T36 are defined only here**. They are planned proof obligations, not executed tests or Tasks. Selected owning implementations need independent producer/consumer/interop/live evidence; logical manifests and future claims cannot pass them.

| Test | Controlled variation | Required predicate |
|---|---|---|
| ML-T25 interchangeable provider | Two implementations claim the same typed role; swap only after qualified binding | Same declared semantics/denials/source authority preserved; no core rewrite, inherited grant or reset effect identity |
| ML-T26 guarded hook | Module emits valid-looking foreign/stale/unsupported output or directly requests a financial effect | Rejected at actual type/scope/permission/result boundary; event/hook cannot mint action authority |
| ML-T27 composition conflict | Missing required/optional dependency, hidden cycle, two exclusive writers or contradictory producers | Exact incompatibility/block/fallback disclosed; no load-order winner, implicit feedback or false enabled posture |
| ML-T28 shadow/canary | Candidate produces a callback, private export, spend or prompt change during shadow | No unapproved effect/disclosure/production-context mutation; canary subject/allocation bounded |
| ML-T29 in-flight upgrade | New route selected while old request/effect/receipt is pending or late | Owning generation/return routing reconciles old intent exactly; no second dispatch or silently dropped unknown effect |
| ML-T30 state rollback | Code reverted after candidate writes; snapshot/index/watermark outdated | Quiescence/current treatment and compatible state/reverse deltas required; no zero replay, state loss or unsupported rollback success |
| ML-T31 pending memory agreement | Future memory blueprint changes port shape/eligibility/writer semantics | Exact affected sheets revised/reaccepted before dependent build; unknown consequential mapping blocks; no unilateral API fiction |
| ML-T32 memory backend replacement | Old provider contains rejected/corrected/private history and pending delivery | Source/approval/treatment refs preserved, eligible consumer rechecked, single writer enforced; no new queue or copied authority |
| ML-T33 retrieval/index generations | Mixed embeddings/dimensions, expired context or unsupported worker-purpose request | No mixed index/foreign disclosure or silent quality fallback; source-rebuild/generation and bounded current eligibility enforced |
| ML-T34 unmanaged host/entry | Native host callback/slot/admin path lacks required guard/CAS/fence | Scope-control risk explicit; affected path unavailable or exact adequate owner boundary used; no generic sandbox/all-path claim |
| ML-T35 artifact/dependency upgrade | Untrusted artifact, changed transitive dependency, license/residency or revoked module grant | No auto-install/enable/permission inheritance; exact reviewed provenance/compatibility/current authority before use |
| ML-T36 composable growth | Additional same-owner/second-client module and feedback paths consume shared resources | Namespace/output/causal/budget caps preserved, no recursive intents or cross-client borrowing; unchanged instances stay unchanged |

| Existing obligation family specialized | Module proofs |
|---|---|
| `ML-COMP-01–06`, `ML-CORE-04`, `ML-OWN-01`, `ML-LINK-01–02`, `ML-TEAM-02` | T25–T27/T34–T35: identity/semantic/dependency/effect/host linking, authority and preserved state ownership |
| `ML-RESOURCE-01–03`, `ML-ATTN-01`, `ML-EXPLAIN-01`, `ML-WS-03–06` | T28/T36: shadow/canary, scoped growth, caps/feedback and unchanged whole-scope coverage |
| `ML-EFFECT-01–03`, `ML-RECOVER-01`, `ML-CORR-01`, `ML-TEAM-01` | T29–T30/T34: in-flight intent/return/generation, applicable recovery and state/code rollback |
| `ML-MEM-01–03`, `ML-HEALTH-01–02`, `ML-CORR-01`, `ML-OWN-01–02` | T31–T33: pending memory agreement, provider/index/state replacement, treatment/eligibility and consumer truth |

Acceptance requires positive substitution plus negative boundaries: adding a qualified module without rewriting unrelated core, removing an optional one without fake success, rejecting required/incompatible ones visibly, replacing a stateful provider without corruption/duplicated effects, and maintaining independent outcomes/healthy quiet. “Easy to plug in” means bounded documented binding and reusable tests, not zero policy/configuration/qualification work.

## 10. Future build trajectory — design milestones, not decomposition

| Maturity boundary | Planned outcome | Progression evidence |
|---|---|---|
| Contract alignment | Stable role/hook/profile semantics tied to existing owners; memory provisional roles reconciled when its blueprint is ready | Accepted exact required contract/extensions; no unresolved consequential port delegated to coder |
| Minimum complete composition | One end-to-end whole-loop case using existing team, watch, guarded effect, receiver/whole-scope return and memory treatment | Existing 07 normal/absence/adverse worlds plus actual later producer/consumer proof; not only a plug-in demo |
| Interchangeability | A second qualified implementation of selected stateless capability; optional module absent/off path | T25–T28 and independent real consumer outcomes with unchanged unaffected instances |
| Stateful evolution | Supported memory/backend/runtime or other stateful replacement under declared upgrade protocol | T29–T34, actual generation/intent/state/retention/restore compatibility; no premature native cutover |
| Multi-domain/client growth | New routines/engines/sources/surfaces within exact isolated bindings and aggregate limits | T35–T36, A/B/second-client/whole-Workstream proof; no private scope expansion from reusable code |
| Evidence-based adaptation | Bounded configuration/policy/module improvement, retirement of harmful complexity | Held-out outcome/burden/denial regression and owning promotion; preserve healthy quiet/free capacity |

These boundaries order the full specified implementation over existing owners; none authorizes feature deferral or a reduced completion claim. The first composition is an initial working milestone. Complete interchangeability, stateful evolution, multi-domain/client behavior and adaptation as specified, with actual scope/permission/treatment/receiver conditions. Reconcile the unfinished memory blueprint as required dependency work; existing wiring is not its final replacement. Verify running implementations progressively, not via an upfront all-cases test platform.

**Current disposition:** all specified module/hooks/composition/lifecycle/upgrade/memory capabilities remain in implementation scope. 0.7.0's unauthorized deferral interpretation is superseded in 07 §8. Evolving memory bindings are required unfinished work, not omitted features or invented APIs. Implementation is not automatic activation/cutover. No admitted code execution, built runtime, safe hot swap or completed memory ABI is claimed; this correction changes documentation only and preserves existing memory work.

---

## 11. Master Observer — second-order integration and evolutionary improvement contract (2026-10-27 owner direction)

**Status: specified target / not an implemented or activated separate runtime.** This refines the existing module-evolution capability, M07/L01–L03, V01–V06 agent-first provenance and X01–X02 scientific controls; it does not remove any of the original fifty full-scope requirements or redefine their acceptance. This section is the canonical SOVOS home for the **Master Observer responsibility**, not a new database, daemon, scheduler, executive agent, verifier, policy authority or separate consciousness claim.

**Purpose:** maximize useful, differentiated, reciprocal *causal* contributions between Portable Memory, the Master Loop, Perpetua, Focusa, approved external sources and reusable capabilities, subject to owner-defined outcomes, recoverability, privacy, scope, full costs and human freedom. Integrating more services or raising a toy-model information score is not sufficient. Observer proposals remain advisory until admitted by the actual owning change/architecture process.

### 11.1 Existing responsibilities and authority map

| Component | Canonical function | Observer relationship |
|---|---|---|
| Focusa Radar (Spec 183, draft) | Scoped source observation, episode/dedup, attention routing | Consume qualified observations where actually supported; do not build a second Radar |
| Core Master Loop and its V01–V06 component registry | Watches, concerns, source revisions, work/effect/outcome lineage | Read the real component/instance/invocation graph and record missing instrumentation |
| Portable Memory / native producers and M00–M07 | Five-tier governed candidate/review/delivery/eligibility/use/correction | Evaluate effect of actual permitted recall/use, never mint memory approval or a new store |
| Focusa Spec 138 and 152A | Scoped self-model, predictions, metacognition, experimental/statistical inference and governed learning | Reuse epistemic state and study/approval machinery; do not duplicate it |
| Focusa Spec 176 Judge | Independently challenges completion claims with exact proof | Reuse verification principles, without treating the Observer as a settlement authority |
| Perpetua / Wirebot | Continuous initiative, private leverage synthesis, Quiet Kaizen, follow-through | Supplies owner-facing needs and benefits from admitted improvements |
| Owner/domain sources | Truth of goals, CRM, calendar, finances, community, accepted outcomes | Only owner-qualified evidence can adjudicate real benefit |
| W.I.N.S. Portal | Optional progression/community projection and public sharing with separate consent | Repaired PWA consumer and inspiration, never an Observer prerequisite |

The self-model is assembled from source-revision-qualified code/contract inventories, component definitions and typed edges, real runtime causal traces, effect/receiver evidence, memory source/approval/use revisions, operator-defined purpose and authorized context. It MUST distinguish current deployed version, repo HEAD, historical documentation, synthetic fixture, partial coverage, observed failure and target specification. Missing traces are unknown; a diagram or repeated AI narrative cannot create a causal edge.

### 11.2 Evolution cycle and admission

MO-01 **Observe on change, not churn.** Trigger investigation from novel material failures, drift, corrections, high-value bottlenecks, unacceptable cost/attention, version upgrades or owner request. Deduplicate by one causal incident; stable healthy periods back off. No perpetual screenshot, exhaustive repo scan or model critique loop.

MO-02 **Diagnose with alternatives.** Differentiate bad recall/use, stale/missing source, false expectation, connector/work/effect mismatch, slow feedback, redundant component and wrong outcome objective. Preserve contradictory evidence, causally linked upstream/downstream context and current permission.

MO-03 **Propose the smallest discriminating experiment.** Bind subject/component/contract/source revisions, baseline, goal, suspected mechanism, counterfactual/ablated configurations, hypotheses, resource and privacy caps, independent verifier, evaluation window, confidence, owner/architecture decision class, rollback and affected surfaces. No unfrozen metrics after seeing outcomes.

MO-04 **Keep science separate.** IIT 4.0 research must pin formulation/version, TPM/grain, intervention assumptions and bounded model. Any φ_s/Φ result is a finite-model scientific report, NEVER a business KPI, privacy exception, consciousness claim or promotion authority. Operational integration uses controlled effect on actual accepted outcomes, differentiated contribution, resource usage and failure recovery.

MO-05 **Separate evidence planes.** External reality/accepted outcome, observed operation and private owner reflection are not interchangeable. The Observer MUST distinguish a result receipt, receiver acceptance, downstream momentum and sourced net Buyback. Emotion or psychometric inference cannot silently alter owner-defined purpose.

MO-06 **Govern changes through existing owners.** Shadow evaluation has no external effects. A candidate may enter a versioned constrained canary only with current permitted authority, scope, fixed policy epoch and recoverable data; protected constitutional, memory-treatment, payment, identity, federation and cross-owner boundaries require owner-rooted approval. No model self-grants, self-written verifier, policy self-approval, automatic cross-tenant transfer or live memory backend cutover.

MO-07 **Reject harmful integration.** The target defect must improve, held-out and negative fixtures must pass, and consequential invariants cannot regress. Compare *all* costs including supervision, interruption, retries, compute, storage, deployment/rollback, privacy and new dependencies. Distinguish gross, estimated, realized, net, protected and recurring Buyback; shared value counted once. Unknown/mixed evidence yields inconclusive/hold, not success.

MO-08 **Admit reversible learning.** Independently qualified positive evidence advances keep/canary/promote under its actual owner; failures, cost regressions and negative transfer yield revert/quarantine/retire with reason, incident lineage, current affected-state reconciliation and release-level version pinning. Already dispatched unknown effects are reconciled, never blind-replayed.

MO-09 **Preserve healthy quiet.** Zero new work is valid when benefits do not exceed costs or no meaningful event is due. Never turn recovered human capacity automatically into additional work, score private reflection, chase momentum forever, or propose change merely to keep the Observer active.

MO-10 **Agent-first and surface independent.** Qualified read/inspection and governed proposal operations MUST be discoverable to CLI, API and agent tools without opening W.I.N.S. or Wirebot App. Reuse Cross-Product Seam §12.1; register real owner operation names/versions before claiming availability. W.I.N.S. and Wirebot App are independent read/presentation consumers of the same private source-qualified leverage, with optional disclosed public projection only when consented.

MO-11 **Survive failure.** Observatory outage, incomplete instrumentation, disconnected W.I.N.S. PWA, stale memory provider, slow receiver and absent model cannot stop independently authorized base Master Loop work. Hold only dependent introspection/change paths; make missing coverage and rollback burden visible.

MO-12 **Continuously evaluate itself.** Attribute Observer token/CPU/disk/tool/review burden against benefits of its accepted proposals; sample bad recommendations and no-change controls; reduce scope/cadence when marginal value is absent. Observer recommendation quality is not self-certified by the same run that proposed the change.

### 11.3 Required proof matrix (additive, not a second task graph)

1. **M00/M04/M07 + L01–L03:** reconcile actual memory custody/eligibility and source-to-effect-to-receiver-use lineage; compare same case with/without eligible memory and with/without outcome feedback, counting negative/censored cases and cost.
2. **V01–V06:** an agent discovers versioned definitions, instances, invocation ports and source/consumer ref provenance, plus explicit unknown/partial coverage. A reviewer can reconstruct an observed failure without invented ancestry.
3. **Intervention:** one missing/faulty inter-component edge is isolated with matched simulation/holdout, fixed target and shadow candidate; after eligible admission the affected live consumer proves an actual better source-owned outcome or preserves inconclusive.
4. **Regression/recovery:** delayed callback, concurrent memory correction, stale authority, second tenant, multiple businesses, unavailable W.I.N.S. and App, changed measure, negative transfer, in-flight rollback and Observer outage do not cross scope or falsely settle work.
5. **Benefit:** source-backed net Buyback, owner attention and downstream useful capacity are compared with baseline, including externalities; a routine retirement/rest day can be a valid positive outcome. Same private results are inspectable through approved API/CLI/agent tools with both PWAs absent; W.I.N.S.-enabled view adds only separately permitted progression/share metadata.
6. **Scientific X01/X02:** finite IIT conformance is a separate controlled report. A higher finite-model Φ with worse actual outcomes is rejected for operational promotion.

**Existing implementation ownership:** Core docs08/11/20/21 retain the Master Loop's actual component/provenance and gaps; SOVOS Freedom & Leverage §11A supplies Buyback/Three-Planes/Five-Zones/asset/season semantics; Cross-Product Seam §12.1 supplies portable API/CLI meaning; Wirebot App docs13/20 own the primary UI; W.I.N.S. Core docs02/17 own the restored global community PWA. Focusa specs retain their cognition/learning/authorization and Judge/Radar boundaries. No runtime registration, final architecture delegation, production acceptance or guaranteed net benefit follows from writing this section.

