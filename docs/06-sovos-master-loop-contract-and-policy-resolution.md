# SOVOS Master Loop — Contract and Policy Resolution

**Status:** INCUBATING — proposed binding decisions and paper contracts; not runtime authority.<br>
**Draft revision:** 0.8.0, 2026-10-12.<br>
**Parent:** [Master Loop](02-sovos-master-loop-draft.md).<br>
**Design obligations:** [integration blueprint](05-sovos-master-loop-integration-blueprint.md).<br>
**Coverage and evidence:** [integration register](04-sovos-master-loop-source-and-integration-register.md).<br>
**Planned falsification:** [scenario annex](03-sovos-master-loop-alarm-and-simulation-design.md), §8.<br>
**Concrete decisions and final acceptance boundary:** [planning closure](07-sovos-master-loop-planning-closure-and-worked-decisions.md).<br>
**Module/hook/upgrade and provisional memory agreement:** [modular composition](08-sovos-master-loop-modular-composition-and-evolution-blueprint.md).

## 1. What this pass resolves

Replace open-ended ownership and parameter questions with a source-grounded recommendation, exact existing field mappings and specified extension behavior. Preserve all 50 blueprint obligations and the whole Workstream journey. These sheets are design artifacts, not Tasks, executable CallGraphs, schemas, registered operations or a new registry.

Three dispositions must remain distinct:

- **Existing contract/source:** the exact artifact or call-site was inspected; its installed consumer may still be unqualified.
- **Proposed owner extension:** behavior is specified here for review within the existing owning product; no implementation exists by implication.
- **Deployment parameter:** its type, constraints, owner and unavailable behavior are specified; actual private values/calibrated limits are bound during approved commissioning.

Paper completeness requires accepted semantics and falsifiable behavior, not pre-existing code for every extension. Conversely, a runtime effect requires actual supported operations, permissions and consumer proof. Neither paper approval nor a method name grants execution.

### 1.1 Finite review boundary

| Included now | Conditional binding before affected use | Explicitly outside this pass |
|---|---|---|
| Source/expectation/concern handoffs; routine v1 field mapping; scheduler privilege/replay; accepted actor responsibility; exact outcome and memory boundaries; complete Workstream ancestry | Actual provider account/API, actor, calendar, notification route, operation version, grant, numerical resource/error-cost profile and independent verifier | Customer-source ingestion, schedules/jobs, model installation/calls, native-memory cutover, services/demos, code/schema changes, task decomposition |
| Existing Wirebot Core/App source; pinned Focusa `b10c605`; installed OpenClaw package documentation and selected scheduler code | UIAI/Veragensia exact execution/privacy binding when computer/body work is selected; optional engine-specific inputs and consumer proofs | Full ecosystem source audit, all engines/models being installed, public UI release, operational/finite-IIT simulations |

Unselected alternatives remain in the organism's design reservoir. Conditional does not mean optional when a chosen workflow depends on that capability. Required unavailable bindings block their dependent path, not unrelated proven paths.

## 2. Recommended responsibility decisions

These are proposed resolutions under the [Owner Constitution](../OWNER_AUTHORITY_CONSTITUTION.md), not amendments to controlling product contracts.

| Subject | Recommended allocation | What the builder must not invent |
|---|---|---|
| Source-backed commitments | Their existing calendar/task/CRM/provider owner; Focusa Temporal Authority represents relevant governed-work time with source refs | A Wirebot obligation database, memory fact as authoritative due time, or invented project for every personal reminder |
| Owner-declared expectation | An authenticated explicit instruction can be the accepted source. Bind its durable source revision, exact intent/time/target and correction/cancel authority through the existing capture/conversation and watch owners; use a native task/calendar record when that domain actually requires one | No compulsory new task/calendar artifact for every reminder. Unattributed inference or unavailable durable source/binding cannot become authoritative absence; an agent cannot invent a provider appointment/deadline |
| Concern continuity | Minimal Wirebot Operating Partner/Perpetua projection in the existing product persistence, with conditional revision and source links | A second task/CRM/outcome/grant store; App's pure helper objects as backend enforcement |
| Watch runtime | Stronger source-native scheduler where available; otherwise the existing OpenClaw scheduler | Another timer daemon, mandatory model-backed watcher, hand-edited scheduler storage or ungoverned admin command |
| Conversation meaning/lineage | Converge qualified Master Loop conversations on Focusa Core's Spec 181 Conversation Ledger direction | A competing Wirebot transcript canon or automatic project binding. Spec 181 is DRAFT; selecting it on paper does not prove an available ledger |
| Physical session/capture custody | The actual runtime, such as OpenClaw's Gateway/session writer; providers retain their own transport records | Capture files as architecture authority or proof of durable policy-compliant retention |
| Transcript/audio retention | Deployment owner policy, enforced by the declared conversation/capture owners; exact content and derived-copy scope must be assigned | Model-chosen retention, generic telemetry consent, permanent raw audio or deletion guarantees the provider cannot supply |
| Mutable memory-state maintenance | Primary Chief-of-Staff loop proposes source-reconciled updates; the existing memory owner/consumer is the sole admitted sink writer | A second feeder/direct worker writer; native writes remain disabled and V1 cutover independently gated |
| Accepted outcomes | Domain/receiver and required human acceptance; Focusa verifies/settles governed work | Run completion or memory acceptance becoming business truth; optional W.I.N.S. becoming a dependency |

The transcript recommendation narrows a genuine gap: Spec 181 names Focusa Core for conversation meaning/lineage, while the portable memory profile still records transcript ownership as unassigned. Resolve this exact crosswalk through owner review; do not edit that profile or claim the gap constitutionally closed here. Capture custody, retention authority, canonical lineage and approved memory remain separate responsibilities.

### 2.1 Minimal concern projection — proposed extension, not a new service

Use Wirebot's product-owned persistence and existing source-qualified reference law. Its logical operations are the blueprint's `ProjectConcern` and `ContinueOrClose`; their public binding is not currently established.

| Owned record obligation | Required semantics |
|---|---|
| Identity | Exact owner/tenant/environment/domain and opaque concern ID; source-qualified identity never inferred from a bare ID |
| Revision | Conditional expected projection revision; conflict returns current revision/ref, never last-write-wins |
| Evidence | Linked observation/commitment revisions, coverage ref, relation proposal/disposition and contradiction refs; no authoritative copied source facts |
| Continuity | Current responsible actor/work refs, guard-derived disposition, next useful event/check or explicit blocker, terminal predicate/ref |
| Lineage | Correlation, merge/split/supersession links and relevant logical-effect refs; merge cannot reset effect deduplication |
| Privacy | Purpose/recipient/retention binding; minimum disclosure; materialized caches/indexes are derived and rebuildable |

Create/replay must converge on the same scoped source origin under a product-owned key. Compare-and-update validates current inputs. Merge/split is an authorized conditional revision that preserves old links, responsibility and completed effects. Closure records independent terminal evidence; withdrawal hides neither source obligations nor unknown effects. If the current product lacks these operations, accept a versioned extension in that product rather than force these semantics into App arrays or memory text.

## 3. Common handoff obligations

All following labels are logical requirements, not newly created JSON fields. Map them onto the owner contract or review its extension. Do not smuggle unsupported authority/retention semantics into a text field and claim enforcement.

| Obligation | Type / validation | Failure / minimization rule |
|---|---|---|
| Source identity | Owning namespace + object kind/ID + account/tenant/environment where required; opaque stable refs | Ambiguous/foreign scope denied; resolve only permitted projections |
| Version | Producer identity/version, supported contract version and exact immutable binding revision | Unknown consequential version blocked; additive compatibility must be explicit |
| Causality | Source revision/ETag/cursor, predecessor and attempt generation as applicable | Wall-clock ordering cannot resolve conflicting writes |
| Observation | Observed versus source-claimed versus inferred; source time, receipt time and coverage interval | A customer assertion is not a payment-ledger fact; failed read is not empty |
| Validity | Current policy/grant/eligibility refs, issuer time basis, freshness/expiry and uncertainty | Recheck at effect/disclosure; unsafe uncertainty blocks dependent use |
| Intent | Accepted semantic revision, exact target/arguments, purpose and consequence ceiling | Identity/hash is not authorization; changing intent requires accepted revision |
| Replay | Correlation separate from product request key, logical-effect key and receipt ref | Same intent survives attempts/body change; unknown completion reconciles first |
| Concurrency | Expected source/projection revision, current actor/lease/writer generation where required | Reject stale writer; a process mutex is not cross-host fencing |
| Privacy | Minimum payload/ref projection, allowed recipients/residency, class and retention | References/digests may still be sensitive; redact logs and discovery views |
| Result | Required outputs, native error plus semantic disposition, evidence/receiver acceptance refs | Unsupported, denied, stale, conflict, unavailable, exhausted, partial, unknown and disputed must not become success/empty |

A coverage witness identifies the exact source/query predicate, event class, account, time interval, pagination/cursor completeness, provider lag and cancellation/exclusion checks. Absence is permitted only when that witness covers the accepted expectation. A healthy scheduler or empty cached list is insufficient. A bounded filtered view may be complete for one predicate without exposing the whole mailbox.

### 3.1 Native errors versus logical dispositions

Preserve native codes/messages safely; derive logical disposition through the reviewed adapter. Examples actually inspected: Temporal Authority `scope_mismatch`, `confirmation_required`, `claim_validation_failed`, `revision_rejected`; memory HTTP 400/401/403/404/405/500/502 paths; scheduler throws validation/conflict errors. This is not a claim that every owner already emits the same enum.

Partial enumeration/scan failure requires an incomplete-coverage result even if the native response returns a successful HTTP status. A native empty result is accepted as empty only under known query scope and sufficient coverage. A timeout after a possible effect remains unknown, not a retryable read failure.

## 4. Exact field mapping into current routine v1

The full `operator-routine-instance.v1.schema.json` was read. Root and nested objects are strict. Use its existing fields; this pass changes no schema.

| Existing path | Intended connection / semantic check |
|---|---|
| `instance_id`, `blueprint_ref`, `blueprint_revision`, `lifecycle.instance_revision` | Accepted immutable lineage; instance revision is not a new provider-effect identity |
| `scope.owner_ref`, `business_refs`, `life_domain_refs`, optional `portfolio_ref` | Owning domain refs; resolve actual tenant/account/project bindings, not merely nonempty strings |
| `trigger_binding.kind`, `binding_ref`, `scheduler_class`, `scheduler_owner_ref` | Actual persistent trigger owner/ref; `condition` does not mean a headless script is permitted |
| `trigger_binding.schedule_ref`, `timezone`, `event_ref`, `condition_ref` | Link accepted time/condition policy; scheduling defaults cannot rewrite due semantics |
| `supervision.operating_partner_ref`, `focusa_assignment_ref`, `workstream_ref`, `foreman_ref` | Current coherent governed work. Nullable schema fields are not permission for an active orphan assignment |
| `compiled_steps[].input_binding_refs`, `output_schema_ref` | Exact permitted arguments/source/context bindings and typed output; missing required operation arguments reject compilation |
| `compiled_steps[].operation_ref` | Current supported operation descriptor/version/effect; deterministic kind requires a resolvable operation, not executable prose |
| `decision_policy_ref`, `prompt_contract_ref`, `attention_policy_ref` | Separate bounded choice, text drafting and owner presentation; do not alias them |
| `consequence_class`, `idempotency_key_strategy` | Reviewed native effect translation and owning logical-effect reconciliation; strategy text alone is not implemented deduplication |
| `authority_binding.grant_refs`, `credential_use_refs`, `budget_ref`, `human_boundary_policy_ref`, `expires_at` | Live authority/renewable custody, per-binding limits and confirmation; budget nullable in shape is not an unlimited workload |
| `reliability_binding.lock_ref`, `overlap_policy`, `missed_run_policy`, `timeout_seconds`, `retry_policy_ref`, `failure_attention_ref`, `rollback_ref`, `revoke_ref` | Owning locks, bounded retries/reconciliation and control return; define applicable compensation rather than rollback everything |
| `acceptance.evidence_requirement_refs`, `acceptance_policy_ref`, `accepted_outcome_refs` | Exact acceptance predicates and known provenance. Empty prior outcome refs are not failure; never fabricate future achieved outcomes |
| `privacy.contains_private_payload`, `contains_secret_material` | Both are fixed false: instance contains allowed refs, not private content or credentials |

Newly achieved results belong in owning runtime Evidence/outcome projections linked to the frozen instance. They cannot rewrite approved executable semantics in place. Additional record requirements belong in supported referenced owner objects; if no adequate object exists, review an explicit extension before building that seam.

## 5. Source and time binding sheets

### B01 — Observe: source adapter → qualified concern input

- **Producer/consumer:** exact provider adapter/account/version → Wirebot's minimal concern projection and relevant Focusa candidate context.
- **Input:** allowed source ref/query/filter/cursor, field projection, read grant, snapshot/freshness and bounded page/time policy.
- **Output:** source-qualified observation refs plus coverage witness; statements retain speaker/claim attribution; denied/stale/partial reads preserve uncertainty.
- **Concurrency/replay:** source cursor/ETag under its owner; repeated origin/revision converges without generating duplicate concerns. Cursor advance must not discard a failed dependent projection; re-read/reconcile through owned checkpoints.
- **Acceptance:** actual consumer sees the right scoped revision, detects gap/pagination/out-of-order/cancellation and wrong-account input. No universal connector API is claimed.

### B02 — BindWatch: accepted commitment → durable trigger

- **Producer/consumer:** source commitment/accepted source instruction → existing scheduler, linked from Wirebot's projection and compiled instance.
- **Input:** exact accepted provider or explicit-owner origin/revision, event/state predicate, coverage domain, due semantics/window, calendar/version, exception/terminal policy and bound instance. Owner instructions need durable attributable intent, not a manufactured external task; recurrence or model inference alone does not supply it.
- **Output:** accepted persistent watch/job ref plus definition revision, current enabled/posture and first supported next check, or explicit failed binding. An acknowledgement alone cannot mark it active.
- **Control:** cancel/revise disarms the affected definition/generation, rechecks pending effects and preserves history. A new due projection is not a new obligation.
- **Acceptance:** cold restart, install failure, duplicate declaration, late/cancelled event and unknown coverage cannot yield false absence or repeated external action.

**Focusa Temporal Authority source binding:** `GET /v1/temporal/status` takes `project_root`, `continuity_id`, optional host/operator/workpoint/item/task dimensions and RFC3339 `as_of`. `POST /v1/temporal/commit` / `revise` use those dimensions, `idempotency_key`, `claim` and `confirm`. The inspected claim carries `claim_id`, numeric `revision`, exact `scope`, `kind`, `status`, `subject_ref`, target/duration, timezone, source/ref, operator confirmation, confidence/uncertainty, observed/effective/expiry times, predecessor and evidence refs. External commitments require confirmation; scope mismatch and invalid revisions reject.

Commit/revise return versioned result, appended events and receipt ref; status returns projection/integrity evidence. Source references and exact subject checks are stronger than optional query filters: unspecified dimensions may match broader claims. The native `TemporalScope` requires project root/continuity, so it is not an assumed universal personal-obligation store. Status/claim APIs do not implement a business-response watch by themselves. Calendar civil intent, folds/gaps, holiday/source precedence and completion meaning must map to the owning Spec 137 contracts, not only a UTC string.

## 6. Scheduler binding: the concrete OpenClaw boundary

**Observed artifact:** installed package reports `OpenClaw 2026.7.1-2 (0790d9f)`. Its package-owned cron/session documents were read fully; selected CLI/tool/runtime source was inspected. This proves installed artifact/source availability, not the gateway's configured authorization, a live watch or consumer acceptance. No customer job list, config, transcript or database was read.

### B03 — Instance/watch → OpenClaw scheduler and governed execution

| Inspected native surface | Exact source contract / Master Loop boundary |
|---|---|
| `cron.add` / CLI `cron add` | CLI sends name, optional `declarationKey`, description/displayName, enabled/deleteAfterRun, agent/session refs, schedule, trigger, sessionTarget, wakeMode, payload and delivery; returned job must be read back |
| `cron.get`, `cron.list`, `cron.status`, `cron.runs` | Exact-job definition, bounded views, health and terminal run history; installed source implements read-only maintenance for status/read/list |
| `cron.update` / `cron edit` | Inspected CLI sends `id` + `patch`. Runtime has store-locked internal `updateWithPrecondition`; public conditional-revision support is NOT established by that helper |
| `cron.remove`, enable/disable | Actual scheduler control; disable/remove does not cancel a provider obligation or recall an already-sent message |
| Schedule | `at`, `every`, `cron`, `on-exit`; explicit timezone/calendar/anchor as appropriate. Top-hour staggering, host timezone and day-of-month/day-of-week OR semantics must not violate the accepted check window |
| Payload | `systemEvent` wakes/queues context, `agentTurn` invokes a model, `command` executes a process on Gateway host. None proves domain outcome by itself |
| Delivery | `announce`, `webhook`, `none` describe runner fallback. `none`/`--no-deliver` do NOT prohibit a model's `message` tool |
| Persistence | Shared SQLite scheduler state; legacy `cron.store` path is not a live JSON file to hand-edit. Job/session/run-log retention is separate from source obligations/Evidence |

**Recommended baseline:** an approved native deterministic check, or a model-free command invoking a supported bounded owner adapter, with explicit source read scope, exact immutable instance/watch refs, no private payload/credential arguments, bounded sanitized output and no external action by default. An unresolved adapter is an explicit extension—not shell improvisation. Resource placement still follows the owning deployment, including OVH execution in the reference topology.

Admin command jobs execute as Gateway automation and do not inherit model-visible `tools.exec` policy. Every effect entry must therefore resolve current scope/grants/revoke/budget/instance and generation through its actual owning operation; admin creation is not permanent permission. `toolsAllow` may narrow an agent turn, but it does not make a command safe. Headless trigger scripts run with the owning agent's full tools including `exec`; keep that optional path unavailable until explicitly permitted and tested.

A trigger script's `fire:false` persists evaluation state/counters without a payload run-history row; `fire:true` after failed payload may repeat because new trigger state is not persisted. These are wake mechanics, not proof of sufficient source coverage or new-effect intent. Bind independent read-health and effect reconciliation; do not diagnose quiet checks from run-history absence alone.

`declarationKey` convergence exists in selected runtime source and is forwarded by CLI/tool. Reusing a key can update schedule/payload on the existing job. Bind the accepted scoped watch/instance-definition revision, reject inconsistent replay and perform explicit old/new drain/fence/reconciliation. Do not regenerate from latest templates. Provider logical-effect identity remains stable independently of declaration/run/worker revision.

If public scheduler CAS is unavailable, a read-then-edit is not atomic. Use the owning single admitted/fenced mutator and supported conditional boundary, or accept the exact conditional-operation extension. If another admin can mutate definitions without that boundary, consumer admission must detect the changed definition and reject affected work; generic all-path enforcement cannot be claimed.

Startup rescheduling and generic transient retries cannot authorize replay of an external effect. Reconcile the source watch, due/coverage window and prior effect before catch-up. Preserve the ownership reference even if a one-shot job deletes itself after success. Manual run acknowledgement is dispatch; only its terminal run/receiver evidence can advance acceptance.

## 7. Judgment, actors and effects

### B04 — Enrich: exact uncertainty → optional bounded result

- **Producer/consumer:** existing Decision-family/secondary-cognition owner → Wirebot/Focusa's current subject interpretation, never an effect writer.
- **Input:** resolved `decision_policy_ref`, finite question type/options/range, applicability, immutable eligible information set, current subject/source/instance/steering refs, exact allowed route/version, expiry and budgets.
- **Output:** typed answer or abstention/error, request/information-set identity, provider/model/method, actual supplied distribution only, validation, source lineage and transport-inclusive duration/cost.
- **Policy:** deterministic facts first; local failure cannot disclose externally. Model/fallback switches recheck route/residency and accepted question semantics, rather than inherit a scheduler fallback blindly.
- **Acceptance:** stale/late/foreign/confidently wrong output cannot change current work; required drafting is separately bound; missing optional judgment does not block exact safeguards or independent work.

### B05 — ReconcileAssignment: concern → existing or accepted actor

- **Producer/consumer:** live source assignment/roster plus Wirebot Composer intent → actual Focusa/task/human provider owner.
- **Input:** exact concern/source revision, incumbent owner and pending work/effects, accountable actor versus contributor, proposed role/context, capacity/ack policy and independent verifier.
- **Output:** existing assignment retained, offered/accepted/declined/unacknowledged handoff, or blocked capacity/identity. Source acknowledgement and assignment revision are evidence, not role-name inference.
- **Extension if needed:** actual provider must expose scoped offer, acknowledge/decline and conditional takeover/fencing semantics. A task assignee field or App `approveRoutine` helper cannot manufacture human acceptance.
- **Acceptance:** old-generation worker cannot act/settle after takeover; absent human response never creates a new deadline, consent or duplicate assignment.

### B06 — AdmitAttempt / ExecuteIntent: accepted work → actual effect

- **Producer/consumer:** pinned instance + whole Trajectory/Workstream/Workset/graph/frame → actual governed executor and provider operation.
- **Input:** dependency-valid frontier, current source/argument preconditions, approved semantic identity, grants/renewable credential use, lease/generation, budget, required confirmation and verifier availability.
- **Output:** actual admission/dispatch receipt separately from terminal effect result; stable intent/request identity and bounded evidence; native partial/unknown result survives projections.
- **Control:** acquire owning exclusion/conditional-write boundary; reconcile a lost response before replay; propagate cancellation without assuming completed effects vanished. Compensate only applicable executed effects under current authority.
- **Acceptance:** pure graph validation, ledger dispatch insertion or shell exit zero cannot substitute for adapter execution/receiver proof. Existing compiler digest/outcome/compensation qualification concerns remain owned by Focusa, not patched here.

### B07 — Computer/body fallback when actually selected

UIAI's known open/read/snapshot/action/diagnostics/close interfaces and Veragensia's body enforcement are adapters, not authority. Bind exact supported descriptor, session/origin, target state, scope/grant, takeover, cleanup and proof. Revalidate a snapshot/ref after page/source change. Browser-scope annotations or `focusa_scope` echoes cannot mint permission.

Screenshot tools can deliver a share artifact automatically. Before private-source capture, qualify the actual privacy/delivery settings and allowed audience; an evidence handle/digest can also be sensitive. Unknown export posture blocks private capture, not source-native verification. Public website visual claims require inspected pixels; a DOM/text/result status is not visual proof. Neither package/source inventory nor this sheet claims an authoritative UIAI checkout or qualified body binding.

## 8. Outcomes and memory interfaces

**Memory plug-in agreement is provisional.** The operator confirms its blueprint is not finished. B09–B12 document inspected current source and required semantics, not the final new memory-layer ABI. [Modular §7](08-sovos-master-loop-modular-composition-and-evolution-blueprint.md) defines required roles and two-sided reconciliation: map the future owning blueprint, revise affected sheets/version/state/lifecycle guarantees and obtain acceptance before freezing or decomposing dependent memory interfaces. This pass does not prescribe its loader/registry/field layout or edit that agent's implementation.

### B08 — VerifyOutcome / ContinueOrClose → state, gap and next work

Declare receiver predicate, allowed source read, completion meaning, independent verifier, objection/dispute handling, freshness and terminal policy before dispatch. Return accepted/failed/partial/unknown/disputed outcome through its owner to Focusa verification/settlement, state/gap and whole-coverage assessment; then choose the valid frontier, refinement, bounded wait or true scoped completion. Missing proof remains a gap.

Required branches and applicable compensation must settle; one completed Workpoint cannot close the project. Shared prerequisite evidence is counted once and linked to each affected acceptance condition. Ongoing services use explicit epochs/admission; optional momentum needs a hypothesis/source/horizon and terminal rule, not an infinite work generator. This preserves #618's Prepare → Act → Reconcile → Advance rather than another workflow authority.

### B09 — SubmitEpisodeOrCorrection: experience → existing review

**Inspected local source:** Wirebot Core `84eee29` plus concurrent changes, not certified deployed. `main.go`/`tenant.go` register `POST/GET /v1/memory/queue` and `POST /v1/memory/queue/{id}/{approve|reject|correct}` through scoped auth. POST consumes `memory_text`, `source_type`, `source_file`, `source_context`, `confidence`; response gives `ok`/new `id`. It is not a new versioned episode contract. Source confidence is not correctness or approval.

Review uses `X-WB-Reviewer`; a header supplies attribution representation, not authenticated reviewer authority. Derive/validate identity against the actual session/delegation. Correct consumes `correction`; approve/correct acknowledgement means transactionally accepted review plus allowed jobs, not provider delivery. Current SQL handles changed payload/source and guarded in-flight completion; do not duplicate that logic or resurrect an older correction-deduplication diagnosis.

**Required binding:** submit minimal source/outcome refs and approved treatment; preserve observation/inference/unknown and correction predecessor. Current POST creates a new ID and has no inspected caller request-key/expected-revision field. Therefore lost acknowledgement cannot be blindly retried. Typed scope/purpose/retention/sink enforcement must exist before richer episodes/workers use it; text/source-context strings are not that proof.

**Recommended owning extension, not a new API/schema here:** submission carries an owner-resolved request identity, source episode identity/revision, minimized summary/evidence/outcome disposition, exact privacy/purpose/recipient/sink policy and payload identity. Identical scoped replay returns the same review ID/revision; same key with changed semantics returns conflict. Review consumes that ID, expected review revision, authenticated reviewer/authority and exact approve/reject/correction intent. Correction advances eligibility/review revision and schedules changed allowed payloads through the existing transaction/job mechanism. Rejection makes pending disclosure ineligible before acknowledgement under the declared consistency policy; provider erasure and cleanup have separate verified receipts. Missing expected revision, unsupported policy or uncertain submission stays blocked/reconciling—never a fresh duplicate, automatic approval or second queue.

### B10 — Delivery health / eligible recall → actual consumer

| Registered local source surface | Native bounds/meaning | Master Loop restriction |
|---|---|---|
| `GET /v1/memory/delivery/jobs` | Optional status/sink/limit; default 100, max 500; items/count/totals | Scope/minimize; error strings are not inherently value-free; incomplete reads cannot be clean health |
| `GET /v1/memory/trace/{id}` | Queue text, delivery timeline, destinations and summary | Private-content surface, not a generic worker/status feed; trace success is not later recall/use |
| `GET /v1/memory/letta-approved-recall` | Main operator-only route; query ≤500, limit 1–10/default 3, 15-second context, ≤200 candidates; schema `wirebot.letta_approved_recall.v1` | Current-approved lexical native sources only; no worker-wide/vector/all-archive claim |
| Native recall result | Memory ID/text/accepted commit; current approval, payload hash and exact provider binding checked around provider retrieval | Revalidate role/purpose/live source before use; body may contain private data |
| `GET/POST /v1/memory/source-mode` | reviewed/hybrid/raw; hybrid currently reviewed-equivalent in docs | Raw pending context is not approved memory; this pass changes no mode |

Recall absence is not proof no prior obligation/assignment exists. Current endpoint does not implement generalized role/purpose/token/expiry request fields; require accepted owning extension before worker disclosure. Review rejection/correction and provider retrieval races need explicit linearization/revalidation policy and consumer tests, not an assumed atomic cross-system transaction. Correction/erasure must invalidate eligible caches/derived context despite provider history. Outcome handling need not await asynchronous sink fan-out.

### B11 — Native mutable state: primary-loop proposal → single sink writer

`main.go` registers operator-only `/v1/memory/letta-state`. GET returns schema `wirebot.letta_state.v1`, bound agent/backend, blocks and native revision map. Qualified native PATCH accepts exactly `label`, explicit `value` and `expected_revision`, rejects unknown/trailing fields, caps request at 2 MiB and update context at 30 seconds, and returns `wirebot.letta_state_write.v1` with bound agent/backend/label, committed flag, commit SHA and resulting revision. Callers cannot select another agent/file path. Missing binding/unqualified write is 503, invalid body 400, reconciliation/conflict 409, unsupported method 405 and provider read failure 502.

The writer preserves original bound block IDs/read-only/size limits, valid UTF-8, expected 64-hex body revision, current committed content and accepted provider commit. These implementation bounds do not establish an SLA. Its process mutex is explicitly not provider CAS/cross-host fencing; `LETTA_NATIVE_STATE_WRITES` remains disabled unless separately qualified.

The primary loop proposes state from verified source/receiver revisions. The existing memory owner validates and commits; other workers/secondary cognition propose, never write directly. Before native enablement, qualify current writer generation, lease expiry/takeover, stale-source denial, quiescence, ambiguous completion, restore/reverse deltas and V1/native compatibility. Losing a lease cannot become permission to start a replacement unfenced writer. No primary-loop reasoning feeder or new write service is activated here.

### B12 — Transcript provenance, retention and correction

Spec 181 distinguishes source audio, ASR hypothesis, accepted transcript revision, interpreted intent and operation proposal. It carries participants/utterances/correction ancestry, scope, privacy/retention and action/Evidence refs; conversations without a project are allowed only under appropriate operation families. These are draft object contracts, not assumed installed endpoints.

OpenClaw's installed docs identify Gateway-owned session metadata and tree-structured JSONL captures, reset/compaction successors, per-store writers and transcript locks. Reset, compaction, archive, pruning and legal deletion are different. In-context tool pruning is not erasure; default maintenance and cron retention can remove artifacts and cannot satisfy a complete-history promise automatically. No capture/cleanup was performed in this review.

Bind the approved steward/custodian and per-class collection, access, retention, export/deletion/legal-hold policy before new transcript/audio collection. Preserve corrections as superseding lineage while retained; current corrected text/speaker determines eligible interpretation. A deletion/hold conflict follows the actual applicable authority; history rules cannot override lawful erasure, and policy cannot promise erasure of uncontrolled provider copies. Derived embeddings/caches/archives and backups are explicitly in the deletion/restore scope.

Pre-compaction flushes or replay may offer reviewable candidates, not promote conversation to approved memory. Ledger/capture receipts do not grant future effect permission or overwrite a newer source/Workpoint. After lawful deletion, residual metadata must be policy-minimal; even hashes may be sensitive. If canonical ledger/retention support is unavailable, state that boundary and keep captures as provenance-only within current policy rather than silently installing another ledger.

## 9. Operating policy without fabricated production numbers

A portable policy is a validated parameter contract, not one magic threshold. Source-implemented bounds above are reported as facts, not recommended limits for every deployment. Numerical SLA, risk/cost tolerance and data retention are approved per actual consequence/binding; future held-out evaluation supplies calibration. No measurement was executed here.

| Parameter group / owner | Required type, scope and constraints | Unconfigured / exhaustion behavior |
|---|---|---|
| Source freshness/coverage / connector-source owner | Finite durations/cursor-lag bounds, exact predicate/account, allowed page/result/byte budgets; minimum proof coverage | Unknown, not absent; reject dependent effect; preserve owned next check/blocker |
| Calendar/check/reconciliation / source + scheduler | IANA zone/version, due boundary, civil fold/gap/calendar policy, bounded reconciliation interval and authorized grace | No invented grace/timezone/deadline; failed binding cannot be labeled active |
| Overlap/effect coordination / operation owner | Instance's existing overlap enum + owning lock/lease/conditional revision and effect key | Deny conflicting effect; coalesce observation work without dropping independent serious concerns |
| Retry/deadline / executor owner | Nonnegative retry counts; finite child/total monotonic limits capped by remaining parent budget; native error map | No retry after unknown effect without reconciliation; no budget renewal from a new run |
| Optional judgment / cognition owner | Allowed finite question/model/route list, input/result/token/time/money caps, max concurrency, expiry and validation | No automatic hosted fallback; optional costly workload denied until configured; required unresolved semantics remain visible |
| Error costs / domain + owner | Consequence classes, false-positive/miss costs, allowed action/review/abstention, held-out policy selection | No universal confidence cutoff; calibration cannot grant permission |
| Attention / existing attention-policy owner | Approved classes/routes/fallbacks, quiet hours/urgent overrides, coalescing and reply ceiling in current schema | No arbitrary recipient/fallback; obligation survives undelivered/snoozed presentation |
| Human handoff / source assignment owner | Actual actor/capacity, offered/accepted states, authorized ack window, escalation/reassignment policy | Unacknowledged is not accepted/declined; preserve responsibility, not duplicate dispatch |
| Fairness / shared owning executor | Per-domain eligible queues, aging, exception reserve and non-preemptible constraints with explicit caps | Do not starve permitted domains; unrelated authorized work continues; no emergency invented from age alone |
| Retention/disclosure / deployment + product owners | Per privacy class purpose/audience/residency/duration, deletion/hold/backup/index behavior and bounded retrieval | No new sensitive collection or expanded disclosure; memory source cannot silently broaden scope |
| Momentum/value / Wirebot + source outcome owner | Specific optional hypothesis, source predicate/window/stop, matched burden/cost baseline and attribution | Unknown benefit remains unknown; close/retire when purpose is satisfied; healthy quiet is success |

Within hard authority/safety/privacy/resource boundaries, use current explicit owner purpose and supported temporal priority. Then consider consequence/reversibility, critical-path impact, source confidence and eligible capacity. Fairness/aging resolves otherwise comparable work; model concentration is not an urgency score. Conflict or infeasible commitments remain visible through the owning policy instead of claiming every deadline is achievable.

Concrete parameter constraints: event/page/byte/token capacities are finite positive integers where the path is enabled; optional concurrency/retry counts and spend ceilings may be zero to disable that workload. Timeout/expiry/window durations are finite with named units and a declared time basis. Money specifies currency and fixed minor units, not an untyped float. Retry count excludes the initial attempt. Input plus question/output headroom must fit the exact model's context. Child timeout and reservation cannot exceed remaining parent allowance. Grace and acknowledgement windows exist only when source/owner policy authorizes them. Conflicting or negative/nonfinite values reject binding.

Limits belong to a stated principal/domain/instance and budget epoch or explicitly approved recurring allocation. Creating another run, switching model/host or splitting a concern cannot renew them. Hard maxima and reserved exception capacity are enforced by the owning executor; informational cost forecasts are not spend grants. Numeric calibration thresholds require documented consequence/error-cost policy and validation data, not model-distribution shape.

A synthetic fixture may choose finite caps to test exhaustion and comparison. Those values never become deployment defaults by being written into a test. Missing required production parameters block activation of that path; they do not require private account IDs, secrets or empirically tuned values to be published in this shared blueprint.

## 10. Review decisions and remaining evidence

**Full implementation scope:** [closure §8](07-sovos-master-loop-planning-closure-and-worked-decisions.md) preserves the first concrete seam choices but supersedes exclusions. Complete all specified source/concern/watch/judgment/workforce/effect/receiver/memory/conversation/control extensions through their owners. Existing paths can support early wiring; they do not replace required idempotency/review/disclosure/writer/upgrade guarantees. Ambiguous results stop unsafe replay while their required owning solution remains unfinished work. Use focused contract closure and running checks, not another broad planning program.

| Decision package | Recommended paper result | Required review/evidence |
|---|---|---|
| Responsibility | Source commitments; minimal Wirebot concerns; native/OpenClaw watches; Focusa governed work and Spec 181 conversation lineage; capture custody separate | Accept/amend the exact assignment, especially transcript convergence versus portable profile's unresolved ownership |
| Conditional extensions | Concern conditional persistence; idempotent episode submission/review; qualified scheduler mutation and entry guard; purpose-scoped recall; writer fencing | Exact owner contract review and parameter/result/error behavior above; no duplicate store/authority or guessed helper invocation |
| Policies | Bindable typed limits, explicit unavailable behavior, deterministic baseline and no unpermitted fallbacks | Accepted consequence profiles; actual numbers before affected activation, future calibration rather than fabricated certainty |
| Consumer acceptance | T17–T24 augment the existing 16 predicates; B01–B12 specify native-source, denial, replay/correction and return-path proof obligations | Producer/consumer/cross-version/live checks after authorized implementation; source/descriptors alone do not pass them |
| Complete specification | Preserve the whole organism and full-outcome coverage; exact required dependencies or accepted extension/exclusion | Resolve remaining relevant source/contract contradictions and owner review before Tasks, not every future optional engine or UI |

The owner requires implementation of everything specified; modular growth/upgrade and complete memory are part of that outcome, not authorized feature deferrals. First demonstrations support progression but cannot substitute for full capability/receiver acceptance. Apply relevant T01–T36 checks during actual implementation without creating a test wall. The unfinished memory agreement is targeted required work; preserve its implementation agent and V1/disabled-write conditions. This correction creates no runtime and publication proves no consumer support.
