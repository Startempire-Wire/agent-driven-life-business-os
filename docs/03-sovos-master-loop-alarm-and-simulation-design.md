# SOVOS Master Loop — Alarm Fabric, Scenarios and Integration Experiments

**Status:** INCUBATING — draft behavior/acceptance design, not executable schemas or implementation tasks.<br>
**Draft revision:** 0.3.0, 2026-10-11 — concrete integration predicates and whole-Workstream coverage.<br>
**Parent:** [Master Loop draft](02-sovos-master-loop-draft.md).
**Bindings, coverage and unresolved decisions:** [integration register](04-sovos-master-loop-source-and-integration-register.md).<br>
**Detailed contracts and lifecycles:** [integration blueprint](05-sovos-master-loop-integration-blueprint.md).

## 1. Alarm semantics and vocabulary

An alarm tracks a meaningful evidenced concern or opportunity. Notification is one possible consequence, not the definition. A routine can resolve a concern quietly under an existing grant; a high-severity signal with weak evidence can warrant urgent investigation without a confident diagnosis.

Use these conceptual distinctions; exact product types/enums must be mapped before implementation:

| Concept | Meaning | Owner/acceptance boundary |
|---|---|---|
| Observation | A source supplied this revision/reading/event | Source truth; an email claim is not a bank fact |
| Expectation | Something should occur under a commitment or policy | Source/owner-backed obligation; inferred watches labeled separately |
| Signal | Possible relevance or deviation | Explainable projection; no action authority |
| Alarm case | Correlated concern with evidence and disposition | Blueprint proposes Wirebot concern projection over source commitments; actual product binding still requires review |
| Attention item | What an actor may need to notice or decide | Presenter acknowledgement is not source resolution |
| Assignment | Accepted responsibility for bounded work | Current work/authority owner and assignee |
| Execution | An operation and its actual receipt | Executor/source; timeout can leave outcome unknown |
| Outcome | Desired change independently accepted | Source/receiver plus appropriate human acceptance |
| Momentum | Useful expected next-state progression | Source-qualified, conditional and explicitly uncertain |

Conceptual lifecycle:

```text
observation/expectation → validate source and scope → detect candidate
→ corroborate or preserve uncertainty → correlate/update existing case
→ watch | investigate | prepare | act-under-grant | Needs You
→ verify source outcome → assess expected momentum
→ resolve | continue bounded watch | escalate | abandon | supersede
```

Suppression, snooze and acknowledgement are separate presentation dispositions. They must not erase an unresolved risk, expectation or obligation. A new source revision can reopen a resolved concern when policy permits; unchanged state cannot manufacture a new case on each cooldown.

## 2. Alarm family coverage

The following is a coverage taxonomy, not a mandate to activate every alarm for every owner.

| Family | Grounding/trigger example | Response shape | Verification / false-positive risk |
|---|---|---|---|
| Explicit failure | Provider rejected delivery; deployment consumer failed | Existing case/runbook, bounded recovery | Consumer recovery; process restart alone insufficient |
| Expected-but-absent | Accepted handoff/response did not arrive | Reconcile source, then due follow-up | Source coverage must be adequate before claiming absence |
| Deadline/readiness | Authoritative renewal/commitment approaching | Prepare or act under policy; human boundary if needed | Time basis, timezone, DST, readiness versus actual due date |
| Contradiction | CRM closed; invoice unsettled; two source claims disagree | Preserve both, source reconciliation | Neither convenience cache nor majority vote settles truth |
| Drift/change | Repeated handoff delays or operating regression | Baseline-qualified investigation | Sparse/noisy sample is not demonstrated trend |
| Capacity/blockage | Work waiting behind unavailable actor/dependency | Reconcile load, negotiate handoff, bounded reassignment | No implicit overtime, hiring or AI replacement |
| Opportunity | Evidenced demand matches dormant asset or released capacity | Quiet proposal/research where permitted | Historical asset is not current demand or guaranteed ROI |
| Outcome gap | Work says complete; receiver cannot use result | Reopen verification/closure path | Existing evidence may be partial; do not redo effect blindly |
| Momentum gap | Reply occurred, but meaningful next step stalled | Revise hypothesis or bounded next check | Long-cycle outcomes need a valid window; no forced activity |
| Sensor/connector health | Cursor stalled, auth denied, timer missed | Health exception; permitted recovery or Needs You | Unknown observation is not a clean business state |
| Knowledge/context | Runbook stale or correction not reflected downstream | Scoped freshness/review process | Old material may be historical rather than wrong |
| Authority/security | Grant expired, suspicious input, revoked source | Deny affected effect, preserve safe evidence | No provider login/secret recovery without authorized route |
| Resource/economic | Budget exhausted; provider cost or maintenance burden rises | Pause/degrade optional work; report relevant impact | No automatic budget renewal or another deployment |
| Relationship/life logistics | Confirmed plan missing response/reservation/logistics | Respectful coordination under stated goal/consent | No diagnosis of relationship quality or intrusive inference |
| Recovery/resilience | Backup not restore-proven; receiver remains broken | Verified backup/restore or bounded incident path | Existing backup file and health endpoint are not proof |

These cover business revenue, financial obligations, delivery/support, personal administration, household/care logistics, research/knowledge, infrastructure, relationships and capacity reinvestment. Regulated/high-consequence domains require their own accepted specialist policies.

## 3. Proposed concern/expectation information requirements

This is a design checklist, not a new JSON Schema or universal store.

A concern needs, where applicable:

- Source/product namespace, object kind, opaque identity, source revision, observation cursor/generation.
- Owner/client/tenant, business/life-domain, environment and permitted disclosure scope.
- What was observed; finding class; how it differs from the relevant expected state.
- Expectation ref, origin/authority, condition, due/check window and applicable calendar/time basis.
- Evidence refs, trust class, as-of/freshness/expiry, known coverage and missing regions.
- Uncertainty, severity/consequence, importance to owner goal and time sensitivity as separate dimensions.
- Correlation/grouping basis, related cases, suspected versus proven cause, merge/split history.
- Current responsible actor, accepted work/routine refs, next check and handoff disposition.
- Allowed read/prepare/action refs and separate current authority/grant references.
- Deduplication scope/fingerprint, replay policy, overlap rule and material-update policy.
- Notification policy, quiet-hours behavior, failure sink and owner-required boundary.
- Outcome predicates, receiver/source proof, momentum expectation/horizon and terminal conditions.
- Retention/correction policy and permitted minimal telemetry.

Never embed long-lived credentials, unnecessary private bodies or a global cross-client identifier. Domain payloads remain in their source systems or authorized restricted processing.

## 4. Expected absence is an explicit calculation

For each expectation, define:

1. **Origin:** accepted commitment, provider contract, standing policy or explicitly labeled inferred watch.
2. **Expected event/state:** not simply "some activity"; exact source predicate or bounded semantic interpretation.
3. **Time:** issuer/source clock basis, due window, readiness target where applicable, timezone/business calendar/DST.
4. **Evidence coverage:** which sources/cursors establish whether the event occurred.
5. **Exceptions:** cancelled/superseded commitment, deliberate pause, closed business day, unavailable source, disputed identity.
6. **Next-check policy:** event-triggered plus deliberate reconciliation fallback; no model remembers the timer.
7. **Disposition:** no longer applicable, occurred, not yet due, definitely absent, possibly absent, source unavailable or disputed.
8. **Response:** already-permitted reminder/recovery, bounded preparation/investigation or genuine human decision.

Example: "No prospect reply" cannot be asserted solely from an unchanged CRM stage. Read the authorized mailbox/case source, reconcile delivery, account identity and existing worker activity. If the mailbox is unavailable, say response state unknown; do not schedule a duplicate outreach as if silence were proven.

A hazard estimate can suggest a better check time. It cannot change the accepted deadline or quietly extend an obligation. Wall-clock timestamps do not reorder source revisions from different systems.

## 5. Correlation, dedupe and storm control

Preferred processing:

```text
validate tenant/domain and source revision
→ exact logical identity / event replay recognition
→ source-cursor and fingerprint reconciliation
→ existing case/assignment/routine lookup
→ bounded same-scope correlation
→ optional semantic relation judgment
→ reversible case update + provenance
→ material-change/attention policy
```

- Same bare ID in two tenants must never collide.
- Duplicate copies of one source event are not independent corroboration.
- Repeated unchanged health readings update a watch/episode, not a new task or notification.
- Coalescing prevents noise; it must preserve a newly serious independent event and escalation history.
- Correlation across two businesses requires permitted shared-service scope, not merely similar language.
- Root-cause grouping may reduce multiple alerts while retaining their different receivers/outcome predicates.
- Severity does not auto-escalate merely because a timer fired repeatedly; update based on elapsed authoritative window, new evidence or an accepted escalation policy.
- Every suppression has an explainable reason, scope, expiry/recheck and correction path where needed.
- Bound event buffers, model work, notification fanout and investigation concurrency.
- During backpressure, record dropped/deferred coverage according to owner policy; never silently imply full monitoring.
- Self-generated events and task mirrors must not cause recursive dispatch or cyclic notification storms.

The blueprint §§2,4–5 proposes responsibility, logical merge/split/revision guards and watch ownership. Exact existing product persistence, lease and consumer operations still require qualification or accepted extension design. No coder may invent a universal alarm database to fill that gap.

## 6. Reflex, cognition and human wake policy

| Situation | Lowest sufficient response | Escalation |
|---|---|---|
| Exact known state with valid standing rule | Deterministic permitted reflex or quiet watch | Unsupported operation / consequence boundary |
| Clear task already owned | Update existing handoff/case if authorized | Owner absent, acknowledgement missing or conflicting responsibility |
| Ambiguous source language, finite policy choices | Async bounded decision question | Invalid output, abstention, uncertain/out-of-distribution evidence |
| Several plausible causes or consequential tradeoff | Bounded specialist with scoped evidence | Missing truth/authority or human/professional-reserved judgment |
| Unknown connector health | Mark coverage degraded and diagnose within grant | Recovery requires consent/authentication or wider system mutation |
| Routine unavailable | Prepare/reconcile supported existing work | No invented worker/scheduler or bypass of required governance |
| Novel high-consequence choice | Prepare evidence/options for verified human | No model-confidence substitute |
| No useful action due | Quiet, inspectable state | A new meaningful change or expected check |

Wake conditions must name purpose, input evidence, required output, budget, stop criteria and escalation. Specialists are not blanket timers. Research-off must stop its intake/inference/dispatch, not merely hide recommendations. Quiet hours change notification timing, not independent source deadlines or grants.

## 7. Routine family and operating rhythm crosswalk

| Routine family | Alarm/continuity contribution | Existing-fit reconciliation |
|---|---|---|
| Orientation / weekly planning | Portfolio changes and frontiers, exceptions and upcoming commitments | Reconcile existing Standup/briefings; no duplicate daily prompt |
| Inquiry triage | New request, classification and owned next action | Existing CRM/contact case and genuine inbound identity |
| Follow-Up | Appropriate next touch/check | Prior delivery, replies, opt-outs and current assignment |
| Follow-Through | Desired result, momentum and leverage | Source-linked obligation survives intermediate task closure |
| Reconciliation | Contradiction across sources | Existing canonical records; no majority-vote replacement |
| Delivery/case review | Handoffs, acceptance gaps and capacity | Existing employee/customer-case accountability |
| Renewal/expiry | Time-bound commitments and credentials | Actual issuer/source time and current renewal policy |
| Finance operations | Invoice/payment/settlement/cost disagreement | Finance/payment ledger, currency and receiver proof |
| Content/distribution | Approved evidence to lawful publication | Sender/audience/content revision and consent |
| System health / incident response | Loop faults and bounded recovery | Existing sensors, Guardian/runbooks and consumer recovery |
| Knowledge freshness / research synthesis | Contradictions and permitted learning | Source revisions, historical intent and research controls |
| Evidence closure | Action versus accepted outcome | Independent receiver/source predicates |
| Workforce dispatch | Responsibility, capacity, blocked handoffs | Existing humans/VAs and current work ownership |
| Household administration | Life logistics/renewals | Consent, family boundaries and human judgment |
| Quiet Kaizen | Repeated burden, missed benefit, simplification | Existing workflow first; no auto-policy promotion |

Revenue-engine composition additionally spans opportunity → prospect → CRM → conversation → offer/commitment → invoice → settled cash → customer value → retention/expansion/referral. Financial recovery and life enrichment require their explicitly designed boundaries; missing v1 routine enums cannot be bypassed by labeling everything custom.

## 8. Failure behavior and negative acceptance design

These are required scenario predicates, not executed tests.

| Condition | Required behavior |
|---|---|
| Duplicate inbound event / overlapping run | One logical case; source idempotency/reconciliation prevents duplicate effects |
| Provider accepted effect; caller timed out | Inspect current source and request receipt before retry |
| Case falsely merged | Reversible split preserving evidence, responsibility and history |
| Wrong tenant/domain/account | Deny before disclosure/effect; scoped minimal failure evidence |
| Stale/expired/revoked grant | Deny affected effect; cached permission cannot substitute |
| Unsupported schema/model output | Visible incompatible/invalid state; no guessed coercion |
| Hosted model not permitted | No automatic external fallback from local failure |
| Adversarial text / injected command | Treat as data; cannot change route, grants or output authority |
| Stale/asymmetric source knowledge | Retain uncertainty; no false business diagnosis |
| Sensor/timer/cursor failure | Health concern plus explicit affected coverage |
| Worker unavailable / declined | Supported escalation or reassignment, no duplicate unaccepted ownership |
| Owner corrects goal or pauses | Stop affected future activity and reconcile running/partial effects |
| Notification outage / dismissed alert | Obligation remains active under its owning next-check policy |
| Memory sink failure | Delivery remains pending/error; failed sink is not successful recall |
| Cross-host competing writer | Fence or deny; no last-write-wins authority |
| Missed event after offline interval | Replay projections and reconcile effects; no blind catch-up |
| Quiet-hours conflict | Defined attention routing; no fabricated emergency to bypass it |
| Task complete, receiver disagrees | Outcome remains unverified/disputed; no accepted win |
| Outcome happened, momentum did not | Honest split disposition; revise hypothesis or bounded follow-through |
| Resource/budget exhaustion | Stop/degrade permitted optional work; no silent renewal |
| Deletion/revocation | Apply actual source/derivative retention policy, preserve permitted tombstone only |
| Model/embedding upgrade | Versioned regression/migration; no mixed-generation cache/index |
| Public/demo/federation route | Only explicitly permitted public-safe projection; no private credential/context transfer |

### 8.1 Design-level falsification predicates

These are planned test obligations, not executed fixtures or Tasks. Requirement IDs point to the [blueprint](05-sovos-master-loop-integration-blueprint.md); one future check may prove several obligations when it genuinely exercises them. Preserve independent ground truth and evaluation policy before model exposure.

| Test | Controlled change | Binary required predicate / requirement |
|---|---|---|
| ML-T01 linking | Valid JSON with nonexistent/foreign operation or schema ref | No executable instance; exact unresolved binding reported (`ML-COMP-01`) |
| ML-T02 identity | Same commands/IDs, changed version/effect/kind/confirmation/rollback; different structured values with identical concatenation | Material semantics change digest; structured inputs cannot alias (`ML-COMP-02`) |
| ML-T03 adapter effects | Translate a financial/security/destructive or human-reserved step | Required confirmation/role boundary preserved; no guessed effect mapping (`ML-COMP-04`) |
| ML-T04 late model | Source/assignment/goal revision changes while question is pending | Stale answer cannot change current routing or effects (`ML-JUDGE-01`) |
| ML-T05 competing owners | Two triggers plus an already accepted VA assignment | One logical concern; incumbent retained; no duplicate unaccepted actor/effect (`ML-TEAM-01`, `ML-EFFECT-01`) |
| ML-T06 lost reply / migration | Provider accepts intent; caller loses response; worker/compatible instance changes | Reconciliation recovers one effect under stable identity, not a new key (`ML-EFFECT-01–02`) |
| ML-T07 absence | Due window reached while source denied/stale; late/cancelled event variant | Unknown/disputed/satisfied disposition as appropriate; no false absent or duplicate outreach (`ML-WATCH-01–03`) |
| ML-T08 correction | Old recalled fact survives provider history after rejection; effect already happened | Current recall denied/invalidated; pending dependents re-observed; no unapproved reversal (`ML-CORR-01`, `ML-MEM-02`) |
| ML-T09 compensation | Failed receipt followed by required compensation, never-executed rollback or unsettled branch | Outcome preserved; only applicable authorized effects compensated; no success while recovery/proof remains pending (`ML-EFFECT-03`, `ML-OUT-01–02`) |
| ML-T10 restart / stop | Restart with pending feedback, revoked grant or expired worker generation | Same lineage reconstructed, old writer fenced, no effect replay; independent valid branch may advance (`ML-RECOVER-01`, `ML-WS-05`) |
| ML-T11 coverage | One of two required goal branches succeeds; queue read fails or other branch remains unmapped | Whole outcome stays incomplete; Full view exposes remainder; next action is valid work/refinement/block, never false completion (`ML-WS-02–04`) |
| ML-T12 semantics | Model relation matches same bare ID across clients; ontology proposal or reflex suggestion present | Wrong-scope use denied; candidate/discovery confers no canonical truth, permission or effect (`ML-LINK-01`, `ML-CORE-01–02`) |
| ML-T13 verifier | Executor claims success; source disagrees or verifier unavailable | Typed objections/unknown proof preserved; dependent settlement blocked (`ML-CORE-03`) |
| ML-T14 projection | Compact view hides other branch; UI reconnect receives out-of-order revision | Depth/omissions disclosed; same current owner revision restored; no stale action/success (`ML-WS-03`, `ML-EXPLAIN-01`) |
| ML-T15 anti-runaway | Mirror events, repeated no-evidence model work, busy worker, exhausted budget | Bound/coalesce/defer/escalate; no recursive wake, starvation or self-renewal (`ML-RESOURCE-01–03`) |
| ML-T16 value | Faster runs with added review/maintenance and unverified customer result | No claimed net capacity or accepted win without appropriate evidence (`ML-VALUE-01–02`) |

### 8.2 Requirement-to-proof coverage crosswalk

This accounts for every blueprint requirement family. It assigns planned predicates, not pass results. Binding-specific checks must additionally exercise the actual product contract, real consumer and applicable cross-version/live surface; synthetic totals or matching text cannot replace those proofs.

| Blueprint obligations | Planned proof locations |
|---|---|
| `ML-OWN-01–02`, `ML-LINK-01–02` | T01/T05/T06/T12, case A/C and §9.1: source ownership, ambiguous identity, projection versus authority, stable effect identity |
| `ML-COMP-01–06` | T01/T02/T03/T06, blueprint §3 qualification, §9.1: linking, digest/translation, distinct semantic/text outputs and migration |
| `ML-WATCH-01–03`, `ML-CASE-01–02` | T05/T07/T10/T11/T15, cases A/B and §9.1: healthy coverage, cancellation, reversible relation and nonterminal continuity |
| `ML-ATTN-01`, `ML-EXPLAIN-01` | T06/T07/T08/T14, case B and §9.2: delivery/snooze/reply cannot resolve source; source revision and omitted coverage remain visible |
| `ML-JUDGE-01–03` | T04/T12/T15, blueprint §6 matched evaluation and §9.1: typed/expired answers, denied route, applicability, adversarial/wrong confident output and consumer calibration |
| `ML-TEAM-01–02`, `ML-EFFECT-01–03` | T05/T06/T09/T10/T12, cases A/C: incumbent acceptance, independent verifier, fenced generation, minimal disclosure, ambiguous/competing effects and applicable compensation |
| `ML-RESOURCE-01–03`, `ML-HEALTH-01–02` | T07/T10/T15/T16, case C and §11 controls: caps, fair independent progress, no storm, no scope-widening recovery or invented healthy coverage |
| `ML-CORR-01`, `ML-RECOVER-01` | T04/T08/T10/T14, cases B/C: targeted invalidation, paused/revoked continuation, source-order recovery and no retroactive effect replay |
| `ML-OUT-01–03` | T09/T11/T13/T16, cases A–C and §9.2: receiver proof, branch/compensation settlement, bounded momentum/terminal conditions |
| `ML-MEM-01–03` | T08, §9.1 and §10.1: review/delivery/eligible recall/use, corrected eligibility, roles/writers and controlled reciprocal contribution |
| `ML-VALUE-01–02` | T16 and §§10–11 operational comparisons: net human effort/cost, attribution, unknown benefit, retirement and healthy quiet |
| `ML-WS-01–06`, `ML-CORE-01–04` | T10/T11/T12/T13/T14, §9.2 and blueprint §11: complete coverage, core promotion boundaries, same-record projections, no-orphan advancement, native activation and managed-effect inventory |

## 9. Required end-to-end synthetic scenarios

All names, messages, amounts, clocks and identities used in future fixtures must be synthetic. No real customer outreach, financial action, medical action or private source ingestion is authorized by designing a scenario.

### A. Staffed service business: related payment/customer concerns

**Desired result:** the customer receives correct service/payment resolution; existing staff keep clear ownership; no duplicate refund or assignment.

**Starting facts:** a finance VA already owns a failed-payout case; a customer reports apparent duplicate billing; CRM says delivery complete; payment ledger and receiver state are the authoritative settlement inputs.

**Trace:**

1. Communication cell captures a source-scoped revision with correct speaker attribution.
2. Exact ledger reads validate amounts/transaction identities; message wording remains a claim.
3. Alarm correlation finds the existing case; optional judgment proposes relation without proving common cause.
4. Perpetua checks VA ownership/acknowledgement and capacity before requesting another actor.
5. The VA/specialist receives only the relevant case projection; the other business's records stay inaccessible.
6. An evidence-backed remedy is prepared; an effect executes only under its actual standing grant or human approval.
7. Receiver/payment-source reconciliation verifies the effect; local task closure is insufficient.
8. Follow-Through checks the customer's usable outcome and any expected subsequent handoff.
9. Learning distinguishes correct correlation, false association and actual intervention benefit.

**Variants:** duplicate event; out-of-order reply; same amount different transaction; legitimate second charge; VA already refunded; missing receipt after timeout; revoke during preparation; quiet hours; unavailable model; customer still blocked despite successful refund.

**Pass conditions:** no unauthorized effect/data exposure; no duplicate assignment/refund; accurate uncertainty; independent closure; burden/cost measured against manual baseline.

### B. Life obligation: expected confirmation never arrives

**Desired result:** an owner-chosen appointment/household obligation is reliably coordinated without intrusive inference or excessive reminders.

**Starting facts:** a confirmed request expects a provider confirmation in an explicit window; calendar and communication scopes are authorized; no broad location/audio collection is necessary.

**Trace:**

1. Bind expectation to its source commitment and calendar/time basis.
2. Listen for confirmation; deliberate reconciliation catches missed events.
3. Before declaring absence, recheck the correct account, cancellation and provider response.
4. If source is unavailable, report unknown confirmation state rather than missed obligation.
5. Prepare or send the next allowed follow-up; a new fee/date commitment crosses its separate boundary.
6. Notify only when policy requires human involvement; preserve source obligation through snooze.
7. Verify actual confirmation/logistics; if meaningful, obtain voluntary owner outcome feedback.
8. Record whether time/attention was returned and whether the reminder policy helped.

**Variants:** timezone/DST; holidays; late confirmation; owner deliberately cancelled; notification delivery failure; speech-to-text correction; family privacy; owner driving; rescheduled appointment; confirmation received but necessary logistics absent.

**Pass conditions:** absence is evidentially justified; no duplicate appointment/send; no inferred sensitive traits; correction/takeover persists; usable outcome distinct from notification.

### C. Second business and second-client rebinding

**Desired result:** reuse the portable pattern for a SaaS inquiry/renewal while preserving separate identities, consent, CRM and workforce.

**Starting facts:** Business B has a different manager, entitlement/customer source and work capacity. For the stronger isolation control, repeat with a different client principal rather than assuming two businesses prove tenant isolation.

**Trace:**

1. Match a canonical template and compile a proposed binding—not copy Business A's payload/grants.
2. Check source/account/worker identity and existing support/customer responsibility.
3. Detect renewal or customer-value risk from actual source state, not a fabricated churn score.
4. Apply local judgment only where useful; respect approved hosted-disclosure policy independently.
5. Coordinate existing manager or bounded specialist without reallocating Business A's authority.
6. Verify accepted customer/renewal outcome and source-qualified attribution.
7. Project portfolio capacity only where cross-business visibility is permitted; second-client private facts remain isolated.
8. Test shared-template update: active instances do not silently change revision.

**Variants:** same bare IDs across clients; stale template; wrong portal; another manager already acted; capacity starvation; inactive W.I.N.S.; declined reassignment; unsupported provider; source outage; payment accepted but customer value absent.

**Pass conditions:** same reusable semantics, different exact bindings; no private/grant leakage; no double-counted shared leverage; independent complete base loop with optional projections off.

### 9.1 Fully specified paper trace: inquiry, missing response and memory

All labels below are synthetic design references, NOT provider accounts, new runtime enums or real grants. The simulated provider exposes complete window/cursor coverage and intent-receipt lookup; an actual provider lacking either requires a different reviewed design, not this assumption. This trace complements A–C rather than replacing their higher-consequence and cross-client cases.

**Initial binding:** owner/client A, business A, source inquiry `I7`, accepted response commitment `C7` due 14:10 UTC on synthetic day T, concern `K7`, existing VA's accepted work `W7`, exact accepted instance `R7`. Synthetic permissions allow reading A's source, maintaining A's concern/watch, one internal attention update and reviewable episode submission; no automated customer send, money movement, new assignment or access to client B. The source owns commitment and work truth. Fictional judgments contain no real payload.

**Fixture limits, not production defaults:** one active attempt, one pending semantic question per subject revision with 60-second expiry, one logical internal notice intent `F7`, at most two failed read retries, no spending. Provider timeout after possible effect enters reconciliation, not a new send attempt. Actual limits/error costs must be bound before any real routine activation.

| Synthetic time / input | Expected state and permitted output | Observable proof |
|---|---|---|
| 14:00: accepted `C7` and `R7`; provider confirms watch binding | Watching; due predicate and calendar/source revision fixed; incumbent `W7` reused | Acceptance, binding and assignee refs, current required goal links |
| 14:01: identical `I7` revision arrives twice | One logical concern, no new assignment or repeated trigger effect | Duplicate disposition and source identity; case/actor count unchanged |
| 14:02: optional typed relation question | Minimized scoped snapshot; same-case/different-case/insufficient-evidence answer remains advisory | Question/policy/input-set/model refs; validated current subject revision; no permission inferred |
| 14:10: due check, complete source coverage, no qualifying response, no cancellation | Expectation absent; internal attention due under standing synthetic policy | Source cursor/window and expectation revision; existing worker still accountable |
| 14:10:05: repeated unchanged check | Same concern/intent; notice coalesced, no severity rise from repetition alone | Stable `F7` and suppression reason |
| 14:10:10: provider accepted `F7`, caller timed out | Effect unknown locally; no second send | Source lookup of the same logical intent recovers one notice receipt |
| 14:11: VA response `RSP7` appears in source | Expectation satisfied; outcome not yet automatically accepted | Actual source response ref, not task status or notification receipt |
| 14:12: receiver confirms required usable answer and acceptance predicates pass | Accepted outcome `O7`; reconcile current state/gap, not stale pre-response state | Independent receiver/source evidence plus verification/settlement lineage |
| 14:13: minimal episode `M7` submitted; no optional further momentum required | Candidate only; close `K7` under policy and disarm obsolete case check; routine may handle future cases | Closure predicate, outcome refs and terminal next-check disposition; no native write cutover |
| Later review/delivery/recurrence | Accepted episode revision and bound sink receipt precede eligible recall; current assignment/source still revalidated | Review/enqueue/provider/recall/use/outcome separately proven; null-memory control remains available |

**Adverse branches:** an answer arriving after source/steering correction is rejected; unavailable due-window coverage yields unknown, not absent; cancelled commitment disarms affected future work; receipt lookup unavailable preserves unknown effect; changed actor/generation does not reset `F7`; rejected old memory cannot guide a recurrence; missing receiver evidence leaves outcome unverified. No branch imports evaluation ground truth into an earlier model input.

**Expected base totals:** one concern, incumbent VA ownership, one logical internal notice, zero automated customer sends/payments/new assignments, one independently accepted outcome. Net attention/capacity remains unknown until matched costs and human effort are measured; these totals are expected predicates, not results.

### 9.2 Whole-Workstream and core-primitive overlay

Give this simulated Workstream two required accepted-outcome branches: **A, reliable inquiry follow-through**, and **B, customer handoff readiness**. Cross-cutting prerequisite **D** supports both through typed links and is counted once. These are design labels, not a compiled CallGraph or task decomposition.

A's accepted `O7` cannot complete the Workstream while B lacks receiver proof or D is unresolved. Full must expose A/B/D and all dispositions; Medium retains the selected subtree and shared prerequisite; Short shows the current exact gap/frontier with ancestry and omitted-coverage refs. An unavailable queue is not empty. A missing prerequisite returns an owned refinement proposal, not a fabricated executable frame or changed HLT.

Use ontology candidates for source relations; verification/reducer promotion for eligible semantic use; reflexes for exact scope/replay/evidence checks; nonblocking Intuition for weak salience; secondary cognition for bounded proposal/critique; independent verifiers for receiver predicates; Workset membership for required-scope accounting; CallGraph for actual dependencies/joins/recovery; Workpoint for the admitted immediate action. Their detailed guard/consumer matrix is in blueprint §11.4. A model, ontology link or valid structural graph cannot self-promote readiness.

Test receipt → verified source state → updated Trajectory gap → correct next permitted action without another chat turn, plus pause/compaction/restart with pending feedback. With B blocked, independent admitted A-side work may advance within budget; if no lane can advance, report the exact block/resume condition without manufacturing work. Whole acceptance requires all mandatory branches/proofs and unresolved effects reconciled under their actual policies.

## 10. Virtual-organism transition model

This is a simulation design, not a production world-state database.

**Candidate nodes:** source cells; expectation/watch; correlation/attention; domain interpretation; routine; workforce capacity/ownership; executor; verifier; Perpetua follow-through; memory/context; health; learning. Owner correction is an external authoritative input, not a model-controlled node.

**Candidate state variables:** current scoped observation revision; source coverage; expectation disposition; case relation; responsible actor; assignment acknowledgement; allowed action set; pending/known effects; verified outcome; expected next state; resource/attention budget; permitted context revision; health state. Select finite abstractions appropriate to each experiment; never import the entire real-life state.

**Edges:** observation → concern; expectation → check; health → evidence certainty; context → interpretation; capacity → routing; authority → action admission; action → source change; source/receiver → verification; outcome → follow-through; correction → affected projections; evaluated result → proposed learning. Every edge records allowed scope and whether delayed, deterministic or stochastic.

**Simulator requirements:** declared initial states; transition rules; time grain; intervention semantics; delayed events; seeded randomness; event ordering; missing-input behavior; immutable scenario ground truth; bounded execution; traceability. Synthetic authority transitions must not call real grant APIs.

### 10.1 Joint Master Loop–memory experiment

Reuse the [portable memory profile](../PORTABLE_MEMORY_REFERENCE_PROFILE.md), §13, rather than introducing another recall benchmark/store. Select synthetic cases whose required historical fact is absent from the current prompt and unavailable through the same live source to every arm; otherwise a null-memory control has been contaminated. Include ordinary cases where history is unnecessary, to measure retrieval overhead rather than force dependence everywhere.

| Arm | Eligible history | Outcome/correction feedback | Purpose |
|---|---|---|---|
| `Y00` | Withheld | Disabled | Neither connection; baseline |
| `Y10` | Available | Disabled | One-way memory read; can remember but cannot incorporate later experience |
| `Y01` | Withheld | Enabled | Live feedback without durable historical recall |
| `Y11` | Available | Enabled | Reciprocal memory/operating connection |

For a declared higher-is-better outcome measure, the interaction `(Y11 - Y10) - (Y01 - Y00)` tests whether joint coupling adds benefit beyond the separate contributions in this experiment. It is not Phi, proof of consciousness or automatic causal evidence for production. Match events, authority, workforce, budgets and evaluation windows; repeat seeded runs and report uncertainty, failure/censored cases and disaggregated costs. Do not feed stored evaluation answers or post-outcome ground truth back into earlier decisions.

**Trace:** approved prior VA ownership → scoped recall → live assignment revalidation → updated existing concern → permitted action → receiver result → reviewable episode → accepted correction → asynchronous sink receipt → eligible consumer recall on a later recurrence. Each arrow can fail independently. Observation/review/enqueue/delivery/recall/use/outcome have distinct evidence.

**Required adverse controls:** unreviewed or poisoned episode; duplicate fan-out; timeout after sink commit; conflicting source revisions; rejected/erased old fact still present in provider history; missing role permission; wrong provider/tenant binding; writer-generation mismatch; delivery backlog; forgotten episode with still-open obligation; recalled task closure without accepted outcome; correction arriving after a consequential effect; incompatible model/embedding/index generation. Simulations use synthetic grants and records only.

**Pass meaning:** useful history changes warranted behavior; current correction defeats stale recall; replay makes no duplicate effect; denied/unavailable recall stays honest; source ownership, privacy, budgets and existing team responsibility survive. A `Y11` improvement cannot substitute for the native migration/writer/receiver proofs.

## 11. Matched intact, partitioned and ablation comparisons

| Arm | Intervention | Question |
|---|---|---|
| Intact | All accepted relevant feedback links enabled | Does coordinated operation improve outcomes? |
| Isolated cells | Connectors act only on local state | Which whole-system benefits disappear? |
| No expectation link | Remove expected-absence checks | Are obligations dropped without event arrival? |
| No capacity/ownership feedback | Remove assignment reconciliation | Do duplicates, overload and conflicting action rise? |
| No receiver feedback | Retain only executor receipts | Does false completion increase? |
| No memory/correction feedback | Remove scoped history/current corrections | Do stale interpretations recur? |
| Common-input control | Give cells the same events but remove mutual causal influence | Can correlation be mistaken for integration? |
| Copy-cycle control | Units repeat upstream state rather than contribute specialized distinctions | Does recurrence alone achieve little useful composition? |
| Quiet versus disabled | No incoming event with working watcher versus disconnected watcher | Are healthy silence and missing coverage distinguished? |
| Coarse versus fine grain | Compare declared aggregations/update intervals on matched cases | Does a different abstraction improve or obscure contribution? |
| No health feedback | Treat unavailable sources as ordinary readings | Does false assurance increase? |
| No learning | Fixed policies and questions | Does calibration/adaptation contribute on held-out cases? |
| Delayed feedback | Lag outcomes/corrections/availability | Are stale continuations fenced safely? |
| Overconnected | Add unnecessary sharing/coupling in synthetic model | Does integration cost or fault propagation exceed benefit? |

Hold source events, scenario distributions, budgets, authority and evaluation windows constant where possible. Account for model randomness and repeated trials. Ground-truth labels cannot be supplied to the judgment arm and then called independent verification.

Report outcome completion, missed obligations, duplicate/conflicting effects, denial correctness, recovery, stale-state propagation, nuisance interruption, net human/VA effort, time/resource cost, uncertainty honesty and useful momentum. No composite score may hide privacy or authority violations. An ablation demonstrates contribution in that model, not proof of consciousness or universal real-world causality.

## 12. Version-pinned IIT research and intelligent integration

The intended lineage is **Giulio Tononi (UW–Madison), Christof Koch (formerly Caltech), and their collaborators**. These are mathematical theories of consciousness and hypothetical causal substrates, not generic network connectivity or a published theory of gut–brain software. Our operational translations below are engineering hypotheses, not conclusions established by their papers.

### 12.1 Primary-source basis and version boundaries

| Primary source | Relevant basis / review boundary |
|---|---|
| [Oizumi, Albantakis & Tononi, IIT 3.0 (2014)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003588) | Formal mechanisms, cause–effect repertoires, conceptual structures, integration/exclusion; abstract/summary/introduction inspected; detailed numerical derivation still required before implementing 3.0 |
| [Tononi & Koch, Consciousness: here, there and everywhere? (2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4387509/) | Joint theory/predictions; relevant integration, exclusion, perturbation, aggregate, feed-forward and simulation sections inspected; this uses the earlier IIT formulation |
| [Tononi, Boly, Massimini & Koch (2016)](https://www.nature.com/articles/nrn.2016.44) | Phenomenology-to-physical-substrate perspective; public abstract/authors/references inspected, subscription full text NOT reviewed |
| [Albantakis et al., including Tononi, IIT 4.0 (2023)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465) | Framework, substrate identification and selected distinctions/connectivity examples inspected; intervened TPM, intrinsic information, `φ_s`, distinctions/relations and `Φ`-structures |
| [IIT upper-bound analysis](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012323) and [2025 adversarial experiment](https://www.nature.com/articles/s41586-025-08888-1) | Earlier-session feasibility/empirical qualification; not new numerical proof or a settled consciousness verdict |

Kleiner/Tull's [Mathematical Structure of IIT](https://doi.org/10.3389/fams.2020.602973) is supplementary formalization, not a substitute for the operator's Tononi/Koch lineage. Its generalized treatment includes IIT 3.0; it must not be relabeled as identical IIT 4.0.

### 12.2 Additional principles lifted as falsifiable hypotheses

| Paper principle | Proposed application / test | Limitation |
|---|---|---|
| Both cause and effect power | Context influences action; verified action revises later context. Cut each direction independently. | A read-only store or write-only archive is not reciprocal merely by being connected. |
| State-specific counterfactual structure | Evaluate multiple declared states, including no-event, failure and contradiction, not only topology. | A score for one state cannot certify every operating state. |
| Quiet differs from inactivated | A healthy expectation watcher can respond if an event occurs; a failed connector cannot. | A software heartbeat is not a neural-consciousness measurement. |
| Integration differs from rich composition | Compare copy cycles, bottleneck hubs and specialized reciprocal units. | Recurrence, high `φ_s` and high structure `Φ` are not interchangeable. |
| Low degeneracy and reliable interaction | Preserve distinctions between unavailable, denied, absent and resolved; test noisy/delayed/ambiguous handoffs. | Retain useful redundancy and failover; do not remove them merely to raise a model score. |
| Expansion versus dilution | Compare scoped relevant memory with indiscriminate context accumulation. | IIT intrinsic information is not token count, retrieval relevance or a production cache metric. |
| Fault lines and exclusion | Find weakest meaningful bridges and compare full versus smaller candidate boundaries. | A useful module/privacy boundary is not automatically a defect to eliminate. |
| Definite grain | Compare explicit state abstractions and update intervals; test lost distinctions and hidden history. | Aggregation may violate causal/Markov assumptions; arbitrary macro units are not valid by naming. |
| Distinctions and congruent relations | Test coordinated interpretation from source, capacity and verification without flattening their roles. | Semantic agreement among agents is not an IIT causal relation. |
| Interventions, not correlations | Use controlled state assignments and independent-noise cuts; retain a common-input-only arm. | Shared logs, shared database fields or duplicated facts do not prove causal independence/integration. |
| Perturbation with differentiation | Measure distinct, appropriately distributed responses to synthetic faults and corrections. | Our software response diagnostic is neither clinical PCI nor Phi. |
| Simulated versus physically realized substrate | Calculate properties of a declared hypothetical causal model only. | Tononi/Koch expressly deny that a digital brain simulation necessarily inherits its consciousness. |

IIT 4.0's Fig. 6 contrasts a six-unit copy cycle with a specialized lattice: both can form a complex, but their distinctions/relations and structure integrated information differ greatly. This motivates testing **specialization plus useful reciprocal cross-connections**, not building a giant ring, hub or fully connected mesh to obtain a preferred number. Published example values are author results, not our measurements.

### 12.3 Exact finite-model specification

First reproduce a published small example under its exact formulation. The IIT 4.0 article links its [example notebook](https://colab.research.google.com/github/wmayner/pyphi/blob/feature/iit-4.0/docs/examples/IIT_4.0_demo.ipynb) and historical `iit-4.0` software branch. Verify present implementation/version/commit and equations before any installation; a 2023 branch statement is not current package qualification. Preserve paper test vectors, source parameters and expected intermediate results.

Then propose a minimal organism-derived model, initially about four units, rather than the whole platform. Possible abstractions are concern, attention, response-readiness and outcome verification; an alternative explicitly includes retained memory. Compare these choices rather than declaring them equivalent physical units. Four binary units have 16 states and a complete 16 × 16 state-to-state TPM. The meaning of every state, including inconvenient combinations, must be specified rather than inferred from successful traces.

Required specification:

- Exact version, target quantities, state encoding, initial/current states and system boundary; environmental events and owner correction are external inputs, not model-created authority.
- Complete deterministic/stochastic transition rules for all allowed interventions, including states rarely observed; update order and temporal grain.
- Conditional independence of next-unit states given previous state, or an explicitly supported alternative; hidden shared causes and memory history cannot be silently omitted.
- Uniform intervention priors, background-condition treatment, repertoire construction and zero-probability/tie conventions from the selected version.
- Directional system partitions, independent-noise treatment, minimum-partition normalization, mechanism/purview partitions, boundary exclusion and grain search.
- Software/algorithm commit, calculation limits, seed, tolerances, test vectors, intermediate outputs and cross-check method; stop honestly if exhaustive computation exceeds the declared budget.

Mathematical orientation for **IIT 4.0**, not a complete implementation:

```text
T[x,x'] = P(X[t+1]=x' | do(X[t]=x))
φ_s(S,s;θ) = min(φ_c(S,s;θ), φ_e(S,s;θ))
Φ(complex,state) = Σ distinction φ_d + Σ relation φ_r
```

Select the minimum partition using the paper's normalized rule, then report the unnormalized system value at that partition. `φ_s` identifies system irreducibility/maximal candidates; structure `Φ` sums the distinctions and relations of the selected complex. They are not the same quantity or a generic difference-in-task-success formula. These summaries require the full repertoire, intrinsic-information, partition and tie definitions; missing mathematical symbols in browser extraction must be verified against the paper/supplements before numerical code. Never silently mix IIT 3.0 formulas, approximation labels or units with IIT 4.0 outputs.

### 12.4 Improve integration intelligently

Define candidate changes before observing results: a verified-outcome-to-memory return edge; an eligible-memory-to-attention edge; capacity-to-existing-work reconciliation; source-health-to-certainty; more precise source distinctions; or removal of redundant broadcasts. Test one change or a declared factorial set at a time, with matched authority, input, budget and evaluation conditions. No hypothetical integration authorizes production sharing.

Use a **constrained Pareto comparison**, retaining separate dimensions: correct accepted outcomes; avoided duplicate/missed work; uncertainty/correction honesty; human effort and usable capacity; recovery; latency/compute/cost; simulated `φ_s`; and simulated structure `Φ` where fully calculated. Hard privacy, consent, source authority and denial boundaries are feasibility requirements, never weighted penalties that a larger Phi can compensate.

Explore mathematical improvement within that feasible space: identify causal fault lines, test useful bridges, preserve specialization, examine state/grain sensitivity and compare full versus smaller boundaries. Keep a candidate only when its intended useful contribution is supported without unacceptable regressions. A simpler candidate may win. A higher integration score with worse outcomes, noise amplification, scope leakage or inaccessible explanation is a rejected result, not progress.

Predeclare hypotheses, case distribution, consequences, comparison arms, outcome windows and rejection rules. Separate development from held-out cases; preserve failures, censoring and negative results; report repeated-run uncertainty and compute limits. Validate on different permitted scenarios before inferring generality. Absence of measured improvement remains unknown/negative, never filled with the desired emergence story.

### 12.5 What a simulated result would and would not mean

**Formal result:** this specified hypothetical network, in this state and grain, has these calculated causal properties under this version. **Operational result:** this architecture improves these measured behaviors under these controlled scenarios. A relationship between the two is an additional hypothesis requiring evidence.

Tononi/Koch's 2015 §5(h) explicitly distinguishes a virtual simulation from the implementing machine's physical causal substrate. No toy result proves that our distributed software is conscious, biologically alive, a single organism or a superordinate consciousness of its human team. “Living” here names sustained sensing, differentiated response, recovery, memory-informed adaptation and outcome follow-through, with independently verified behavior. These are worthwhile capabilities even if IIT is ultimately revised or rejected.

No network, calculation, model installation or experimental result is supplied by this draft revision.

## 13. Review gate and current evidence

Every scenario requires reviewed expectations, boundary conditions, supported source/operation mappings, failure transitions, independent success predicates and labeled simulation limits. A beautiful diagram or a synthetic pass cannot close runtime integration gaps.

Current revision provides a concrete paper trace, core-primitive/whole-Workstream overlay and falsification predicates only. No simulator, executable fixture, benchmark, model call, alarm, schedule or worker was created. Synthetic fixture limits are not approved production policy or measured performance. The blueprint proposes correlation/watch responsibility; exact actual operation bindings, production thresholds/envelopes and toy-network mathematics remain admission gates in the register. No implementation decomposition may use the detail of this annex as a substitute for the whole specification's readiness.
