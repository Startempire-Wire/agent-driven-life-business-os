# SOVOS Drives & Integrated Organism — Source/Runtime Evidence and Dependency Audit

**Research date:** 2026-10-29 (Pacific)  
**Status:** substantive research handoff / candidate architecture; **NOT** a finalized or owner-accepted drives specification, executable Workset, new authorization, or production release.  
**Companion:** [initial handoff](drives-integrated-organism-server-agent-handoff-2026-10-29.md), draft SOVOS [PR #34](https://github.com/Startempire-Wire/agent-driven-life-business-os/pull/34).  
**Methods:** connected GitHub repository searches and reads of Focusa default branch; SOVOS main + active PR branches; Wirebot Core selected branch docs and source-mapped audits. No SSH, deployed-binary inspection, fresh production invocation, code compilation, or tests were executed in this research pass. **Code presence, historical test proof, and actual installed production acceptance are different evidence classes.**

## 1. Executive conclusion

**Do not create a parallel “Drives Engine,” cognition store, observer daemon, scheduler, authority table, or artificial brain.** Compose intrinsic motivation from purpose and commitment, differentiated observation, priority/authority arbitration, bounded prediction and secondary cognition, verified action/outcome, governed memory, and second-order experimental improvement. Persistent drive pressure is a *derived, inspectable decision signal* that changes eligible attention and initiative; it never creates permission or decides truth.

The deepest missed issue in the earlier discussion is **Spec 71 precedence, not just weighted conflict resolution**. Focusa requires non-overridable/constitutional/current-scope/mission/execution/optimization bands in that order; local drive weights only operate within a decision space permitted by the higher bands. Likewise, **Spec 73 CompletionDrive is a named intended ontology primitive, not proof of a fully working conative state machine**. Some adjacent commitment lifecycle behavior is implemented; the exact intended objects and end-to-end lifecycle remain to be shown.

The later spec families deepen the architecture: Focusa **136** settlement truth, **137** temporal authority, **139** presence and execution placement, **164** Workstream identity, **176** adversarial completion verification, **182** Foreman, **183** Radar, **149 (Recursive Improvement Foundry, by filename)**, and **152A statistical experimentation**. They are not peripheral embellishments. Their roles affect what “motivation to act” can mean, whether a state change actually happened, what should be remembered, and how improvement can be measured.

**Current repository architecture is already reciprocal but implementation is not yet complete.** SOVOS Master Loop includes reciprocal memory and control, IIT-inspired ablation and real outcome checks. The new Master Observer is specified on **open PR #31**, not installed by that documentation. Portable Memory v0.4.0 is explicitly incubating, and some owner-of-transcript-memory and native transport agreements are unqualified. Wirebot Core has a real partial Master Loop adapter, not the full accepted organism.

### Source authority and overlap

- [SOVOS AGENTS.md, first principles and full-spec law](../../AGENTS.md), especially §7.
- [SOVOS main Master Loop](../02-sovos-master-loop-draft.md), §§3, 11, 13, 14; [composability/provenance contract](../09-sovos-master-loop-composable-provenance-and-agent-first-contract.md).
- [Portable Memory v0.4.0](../../PORTABLE_MEMORY_REFERENCE_PROFILE.md), §§2–13, 18–20.
- [Master Observer branch §11](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/spec/2026-10-27-wirebot-wins-observer-flywheel/docs/08-sovos-master-loop-modular-composition-and-evolution-blueprint.md) / [PR #31](https://github.com/Startempire-Wire/agent-driven-life-business-os/pull/31).
- [Stewardship branch docs10](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/spec/2026-10-28-asset-stewardship-master-loop-callgraph/docs/10-sovos-asset-stewardship-master-loop-implementation-contract.md) / [PR #32](https://github.com/Startempire-Wire/agent-driven-life-business-os/pull/32).
- [Focusa Unified Organism](https://github.com/Startempire-Wire/focusa/blob/main/docs/UNIFIED_ORGANISM_SPEC.md) and [Brain/Body Gap Map](https://github.com/Startempire-Wire/focusa/blob/main/docs/current/FOCUSA_BRAIN_BODY_ANALOGY_GAP_MAP.md). The organism snapshot includes dated 2026-04-02 service/port observations: **historical**, not today's installed-state inventory.

## 2. Evidence-class legend (do not flatten)

- **CODE-FOUND:** executable source/route/reducer or test contract inspected in current GitHub source; does not prove that version is installed.
- **HISTORICAL-RUNTIME:** prior dated production smoke/live test or certificate; its original narrow scope may be real, but not a fresh 2026-10-29 qualification.
- **PARTIAL:** some relevant real code and documented proofs, but specific full-spec behavior not demonstrated.
- **DESIGN-TARGET:** normative or draft source describes intended behavior without currently qualified running consumer.
- **UNRESOLVED:** required source owner, binding, authority, proof, or live product behavior remains unknown.
- **SPEC-ONLY:** no relevant named code found by current indexed search; search misses are not absolute absence proof. Confirm in an actual checkout.

GitHub source inspection and stored evidence qualify an implementer to *investigate and build*, not to claim a deployed completion receipt.

## 3. Focusa high-priority spec-to-primitive trace

| Family | Exact existing contract and behavior | Evidence classification / critical gap |
|---|---|---|
| **71 — governing priors/scalar weights** | Six bands: non-overridable → constitutional → scope-governing → mission-governing → execution-governing → optimization. GoverningPrior and PriorityBand outrank local ScalarWeight; urgency, importance, completion, cost, reliability, attention cost act only *inside allowed choices*. No “flat weighted soup.” | **PARTIAL/CODE-FOUND:** apps/pi-extension/src/turns.ts emits governing_priors_applied; API telemetry handler and tests/work_loop_governing_priors_consumer_path_test.sh exist. This does not demonstrate full typed-prior ontology + all consumers or that current deployed Wirebot honors the precedence. |
| **73 — intention/commitment/self-regulation** | Distinguishes Intention vs Commitment; InhibitionRule, DistractionCandidate, PersistencePolicy, AbandonmentCondition, CompletionDrive, GoalConflict and SelfRegulationState; explicit promotion, persistence, switching, completion/release, abandonment. | **PARTIAL, consequential gap:** tests/doc73_first_consumer_path_test.sh checks work-loop commitment release state and 2026-04-18 status matrix marks consumer paths passing. **BUT** later 2026-04-23 skeptical code/runtime audit identifies vocabulary-only higher conation, and current crates/focusa-api/src/routes/ontology.rs OBJECT_TYPES does not enumerate exact Intention, Commitment, CompletionDrive classes; search for CompletionDrive finds documentation, not implementation. Do **not** present CompletionDrive as live. |
| **78 — bounded secondary cognition** | Verify/critique, candidate extraction/proposal, bounded projection, reflection, prediction/anticipation; fixed evaluation, continuation guards, scoped authority, trace, retention, fail closed. End-to-end model-backed proactive thinking is more than a generic autonomous state. | **CODE-FOUND + HISTORICAL-RUNTIME / scope-limited:** core types SecondaryLoopLedgerEntry; replay, daemon, work-loop API and tests. 2026-04-18 certificate reports 16/16 single-run and 6/6 sustained production smoke runs for F1–F5 closure/replay/governance. Earlier callsite audit warns that autonomy state alone is not a complete model-backed secondary-cognition program. Re-qualify each drive-specific role and actual live model execution. |
| **80 — Pi tree/LI metacognition tooling** | Branch-lineage snapshot/restore/diff; tool-first capture→retrieve→reflect→adjust→evaluate, runtime/API/CLI parity; ontology-aware provenance, branch restoration and compounding. | **CODE-FOUND, doc status conflict:** docs/80 header says planned/design-only and old endpoint binding matrix calls snapshots/metacognition planned, **but** current crates/focusa-api/src/routes/snapshots.rs and metacognition.rs implement those routes and CLI implementations and dedicated tests exist. Spec §20 says “implemented-now.” Reconcile obsolete header/matrix with current installed route/CLI/live proof. API-local prose fields still exist, so workflow presence ≠ Spec138 epistemic promotion maturity. |
| **138/138A — prediction, metacognition, epistemic authority** | Forecast question + immutable information-set commitment, typed distributions and uncertainty, source independence, counterfactuals, scoring/calibration, outcome resolver authority, learning assessment/promotion, transfer, negative transfer, correction, self-model, bias and memory lifecycle. | **CODE-FOUND/PARTIAL:** core prediction_authority{_ledger,_storage,_validation}.rs, generated operation list, canonical typed API adapters and tests. 2026-07-30 foundation evidence: 542 combined source requirement rows/629 primitive registry entries, typed ledger PASS; explicitly **not full 138/138A conformance**. Later Aug acceptance records prove individual areas, but do not justify global live acceptance without feature ledger and installed consumer evidence. |
| **183 — Radar observation/episodes/signal economics** | Exact Workstream scope. RadarObservation→fingerprint/dedupe→RadarEpisode→RadarSignal→R0 remember/R1 notice/R2 prepare/R3 investigate/R4 act-under-existing-grant/R5 escalate. Calculate salience net of attention, privacy, compute and duplicate costs; use Foreman for project interpretation. | **DESIGN-TARGET:** 2026-09-05 draft, eight implementation slices F183-S1–S8. Indexed search for RadarObservation/RadarEpisode/RadarSignal yields spec text but not named runtime object code; do not call Radar installed. Observation ≠ canonical fact, Signal ≠ Workpoint, suggestion ≠ grant. |

**Exact primary sources:** [71](https://github.com/Startempire-Wire/focusa/blob/main/docs/71-governing-priors-and-scalar-weights.md), [73](https://github.com/Startempire-Wire/focusa/blob/main/docs/73-intention-commitment-and-self-regulation.md), [78](https://github.com/Startempire-Wire/focusa/blob/main/docs/78-bounded-secondary-cognition-and-persistent-autonomy.md), [80](https://github.com/Startempire-Wire/focusa/blob/main/docs/80-pi-tree-li-metacognition-tooling-spec.md), [138](https://github.com/Startempire-Wire/focusa/blob/main/docs/138-focusa-prediction-outcome-calibration-metacognitive-learning-transfer-and-epistemic-governance-spec.md), [183](https://github.com/Startempire-Wire/focusa/blob/main/docs/183-focusa-radar-proactive-observation-episodes-signal-economics-and-attention-routing-spec.md).

### Contradictory / temporally scoped implementation evidence to preserve

1. **Spec 73:** [Apr 18 pre-78 parity status](https://github.com/Startempire-Wire/focusa/blob/main/docs/PRE78_ONTOLOGY_PARITY_STATUS_2026-04-18.md) records successful first-consumer path while [Apr 23 skeptical implementation audit](https://github.com/Startempire-Wire/focusa/blob/main/docs/evidence/SPEC_INTENT_VS_ACTUAL_CODE_RUNTIME_GAP_AUDIT_2026-04-23.md) finds missing named ontology objects. Both can be true: a commitment-related status projection exists but full conative ontology and behavior remain unproven.
2. **Spec 78:** [Apr 18 production closure certificate](https://github.com/Startempire-Wire/focusa/blob/main/docs/evidence/DOC78_COMPLETION_CERTIFICATE_2026-04-18.md) validates F1–F5 closure-path behaviors; do not extrapolate it to all future drive-based secondary processing.
3. **Spec 80:** [Apr 21 old endpoint matrix](https://github.com/Startempire-Wire/focusa/blob/main/docs/evidence/SPEC80_ENDPOINT_FALLBACK_BINDING_MATRIX_2026-04-21.md) calls route set missing, but [current snapshot route source](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/snapshots.rs) and [metacognition route source](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/metacognition.rs) include explicit endpoints. Defer *claims of deployment*, not obligations.
4. **Spec 138:** [Jul 30 foundation acceptance](https://github.com/Startempire-Wire/focusa/blob/main/docs/evidence/spec138/S138-foundation-acceptance.txt) explicitly excludes later requirements. Code for [canonical prediction authority HTTP adapter](https://github.com/Startempire-Wire/focusa/blob/main/crates/focusa-api/src/routes/prediction_authority_canonical.rs) establishes a real surface; separate full test and installed proof still necessary.
5. **Organism spec:** Apr 2 running/isolated service inventory is a time-stamped baseline, **never** current-live proof.

## 4. Additional relevant cognitive/organism families that must not be overlooked

**Direct dependencies; read source owners, not just headings:**

- [04 Focus Gate](https://github.com/Startempire-Wire/focusa/blob/main/docs/04-focus-gate.md): *advisory* salience filter; never changes active focus or dispatches actions. Pinned attention bypasses decay but not focus/authority.
- [05 Intuition Engine](https://github.com/Startempire-Wire/focusa/blob/main/docs/05-intuition-engine.md): async, explainable weak signals/aggregation; never decides, speaks or acts; pressure is a candidate, not consent.
- [54A/54B](https://github.com/Startempire-Wire/focusa/blob/main/docs/54a-operator-priority-and-subject-preservation.md): newest operator input and minimal scoped injection; [67](https://github.com/Startempire-Wire/focusa/blob/main/docs/67-query-scope-and-relevance-control.md)–69 current ask, excluded context, wrong-question/hijack protection.
- [61 domain cognition](https://github.com/Startempire-Wire/focusa/blob/main/docs/61-domain-general-cognition-core.md), [70 shared interfaces](https://github.com/Startempire-Wire/focusa/blob/main/docs/70-shared-interfaces-statuses-and-lifecycle.md), [72 identity/role](https://github.com/Startempire-Wire/focusa/blob/main/docs/72-agent-identity-role-and-self-model-ontology.md), [74–77 identity/view/retention/governance](https://github.com/Startempire-Wire/focusa/blob/main/docs/76-retention-forgetting-and-decay-policy.md): current scope, verified claims, lifecycle and memory invalidation.
- [79 continuous work loop](https://github.com/Startempire-Wire/focusa/blob/main/docs/79-focusa-governed-continuous-work-loop.md): implemented foundation, end-to-end acceptance open, provider-neutral WorkItem; no separate autonomous coordinator needed.
- [96 Trajectory](https://github.com/Startempire-Wire/focusa/blob/main/docs/96-trajectory-projection-and-daemon-stability-spec.md), [97 reflexes](https://github.com/Startempire-Wire/focusa/blob/main/docs/97-focusa-reflex-primitives-spec.md): schedule and orient by goal/working set; deterministic local recovery/action-advisory reflexes. Reflex registry API route and semantic_reflex core code exist and older live dogfood proof recorded; reflex suggestion ≠ action authority.
- [104 scoped CRDT](https://github.com/Startempire-Wire/focusa/blob/main/docs/104-typed-scoped-runtime-and-singleton-elimination-spec.md), [119 receipts](https://github.com/Startempire-Wire/focusa/blob/main/docs/119-verifiable-agent-work-receipts-and-governed-execution-ledger-spec.md), [131 closure](https://github.com/Startempire-Wire/focusa/blob/main/docs/131-focusa-workpoint-item-timing-velocity-and-closure-authority-spec.md), [133 silent sessions](https://github.com/Startempire-Wire/focusa/blob/main/docs/133-daemon-native-durable-silent-sessions-and-governed-autonomous-execution-spec.md): continuity, proof, no duplicate work.
- [135F reactive context](https://github.com/Startempire-Wire/focusa/blob/main/docs/135f-domain-general-ontology-core-semantic-graph-domain-packs-and-reactive-context-spec.md) and [136 settlement](https://github.com/Startempire-Wire/focusa/blob/main/docs/136-governed-proposal-to-settlement-protocol-and-outcome-truth-infrastructure-spec.md): source/proposal/execution/receiver truth are distinct. *A tool response, work-item “done,” delivered message or perceived success does not satisfy a drive*.
- [137 time](https://github.com/Startempire-Wire/focusa/blob/main/docs/137-focusa-temporal-authority-deadlines-urgency-grounded-forecasting-spec.md): deadlines, calibrated urgency, clock authority, progress/delay opportunity and aging; no second clock/scheduler.
- [139 presence and placement](https://github.com/Startempire-Wire/focusa/blob/main/docs/139-distributed-presence-environment-awareness-execution-placement-and-multi-daemon-coordination-spec.md): actual machine/session/lease presence, avoid double-working across agents, verify intended execution body; this affects eligibility, cost and recovery of autonomous drives.
- [141 agent-first release](https://github.com/Startempire-Wire/focusa/blob/main/docs/141-focusa-agent-first-tool-skill-runbook-and-documentation-release-gate-spec.md): supported operations callable through machine-readable API/CLI/tools and evidence, not GUI-only.
- [164 Workstream Root](https://github.com/Startempire-Wire/focusa/blob/main/docs/164-workstream-rooted-canonical-runtime-design.md) and [182 Foreman](https://github.com/Startempire-Wire/focusa/blob/main/docs/182-focusa-project-foreman-workstream-intelligence-projection-spec.md): one project-scoped intelligence/worker continuity, not a global Foreman singleton or another chatbot. Foreman is draft.
- [176 Judge](https://github.com/Startempire-Wire/focusa/blob/main/docs/176-focusa-closure-proof-capsule-and-verdict-architecture-spec.md): independent verification of finished work; draft verification architecture plus some core code, not an automatic deployment claim.
- [149 Recursive Improvement Foundry](https://github.com/Startempire-Wire/focusa/blob/main/docs/149-evidence-grounded-recursive-improvement-secondary-cognition-foundry-and-private-control-plane-boundary-spec.md): 78 specialization for codebase/system improvement, research-only candidates until approved source changes; not an unbounded self-modification loop or a substitute for Master Observer's outcome/cross-system evaluation.
- [152A statistical inference](https://github.com/Startempire-Wire/focusa/blob/main/docs/152a-statistical-inference-probability-uncertainty-experimentation-and-causal-analysis-spec.md), [152B quantitative integration](https://github.com/Startempire-Wire/focusa/blob/main/docs/152b-quantitative-scientific-runtime-integration-ontology-reflex-secondary-cognition-reducer-and-surface-parity-spec.md): fixed estimands/eval protocols, dependence/missingness, causal vs predictive claims, measurable benefit, no “higher Phi = valuable” shortcut.

**Collision warning:** Focusa has **two different files titled Spec 149** (recursive Foundry *and* Workset Flow Ledger) and **two distinct files titled Spec 152A** (statistical inference *and* private feature anti-tamper). Reference **full filename and owning subject** in all code/dependency plans; do not silently select the wrong document by number. Also historical “Radar 164” is a superseded *proposal number*: current 164 is Workstream Root, Radar is 183. This is a concrete source-routing hazard for a server agent.

## 5. Current SOVOS / Wirebot/Core source ownership and status

| Area | Owning home | Read evidence | Current conclusion |
|---|---|---|---|
| Master Loop portable meaning and nonoptional IIT integration | SOVOS docs02–09, AGENTS; mathematical intelligence registries | Main documented reciprocal anatomy and exact component provenance; §13 intact/partition/ablated comparison; §7 Algorithm Squared and full-spec commitment | **SPECIFIED**; not an executable runtime from this repo. |
| Native source/concern coordination | Wirebot Core, docs08/09/20/21 on branch reconcile/scoreboard-complete | Core docs08 describes existing cmd/scoreboard/master_loop*.go, source router, stored source-qualified concerns, POST /v1/master-loop/step, follow-through readbacks, source-side fences; historical installed smoke and 90 App test files/557 tests | **REAL PARTIAL CORE**, NOT full business-life accepted outcome. Repo's documented remaining gaps include qualified live effects, independent receiver acceptance, real follow-through and comprehensive consumer/pixel validation. Reverify active deployed commit. |
| Full Master Loop implementation work | Wirebot Core docs/09-wirebot-master-loop-callgraph.json on reconcile/scoreboard-complete | 77 frames / 149 dependency edges, 50 obligations, 36 proof predicates, many null execution bindings | **UNBOUND SOURCE GRAPH**, not admitted runtime Workset or completion. Extend existing graph, not second tracker. |
| Portable Memory | SOVOS reference profile; Wirebot Core plugin memory bridge and actual provider memory product | SOVOS §§2–13/18–20; Core docs20 audit recognizes capture, scoped native receipt/revision operations but task→memory→consumer→receiver is not fully demonstrated | **INCUBATING + PARTIAL ADAPTERS**. Single qualified writer and two-sided binding remain pending. No transcript canonical owner explicitly assigned in SOVOS profile. |
| Master Observer | SOVOS PR #31 §11 (open) | MO-01–MO-12 and existing Core/Mem/Focusa binding/proof matrix | **DESIGN TARGET**, no separate daemon. Reuse actual Focusa 138/152, Radar 183, Judge 176 and Core source traces. |
| Asset stewardship | SOVOS PR #32; Core corresponding spec/2026-10-28-asset-stewardship-master-loop-callgraph | 23-node / 30-edge additive native extension; source owners and CUT-0..CUT-5 | **UNBOUND DOCUMENTED WORK**, complementary drive domain, not asset sensor/deployed financial book. |
| Owner-facing presentation | Wirebot App primary; W.I.N.S. Portal separate optional PWA; agent-first headless Core/Focusa | SOVOS cross-product contracts; PR #31 companions | PWA restoration and GUI are **not prerequisites** for headless drive/organism proof. No assumed production deployed surfaces from docs. |

Relevant Core source docs: [master loop runtime](https://github.com/Startempire-Wire/wirebot-core/blob/reconcile/scoreboard-complete/docs/08-wirebot-master-loop-runtime.md), [unbound full callgraph](https://github.com/Startempire-Wire/wirebot-core/blob/reconcile/scoreboard-complete/docs/09-wirebot-master-loop-callgraph.json), [gap audit](https://github.com/Startempire-Wire/wirebot-core/blob/reconcile/scoreboard-complete/docs/20-wirebot-master-loop-gap-reconciliation.md), [component adapter](https://github.com/Startempire-Wire/wirebot-core/blob/reconcile/scoreboard-complete/docs/21-wirebot-master-loop-composability-provenance-and-agent-first-contract.md).

## 6. Candidate organism drive taxonomy (curated from SingleEye + Focusa, not a competing subsystem)

Each drive is a versioned **purpose-bound interpretation** over existing source refs, commitments, qualified observations and predictions; includes scope/owner, evidence grade, horizon, possible permitted outcomes, resource/attention budget, inhibition and satisfaction criteria, state revision, provenance and reason for cessation. Do not create another ledger when existing Focusa/Core can express the record.

| Drive family | Reused primitive owners | Satisfies/settles only when | Negative / quiet control |
|---|---|---|---|
| **Completion and commitments** | 73 Intention/Commitment/CompletionDrive, Workpoint, 79, Core Master Loop, Perpetua | independent task/receiver completion or legitimately released/abandoned commitment is qualified | blocked/abandoned/reassigned/unknown are distinct; no fabricated “done” |
| **Curiosity and discovery** | 05 intuition, 04 gate, 78 investigation, 138 VOI, Radar 183 proposed, scoped memory | verified question resolved, decision improved, or no positive expected value to investigate remains | evidence/compute budget, novelty dedupe, idle backoff |
| **Protection and resilience** | Radar/97 reflexes/137 urgency/139 presence/136 settlement/owner asset source | real risk is mitigated or disproven by qualified current source; no universal risk score | suppress unqualified alerts, no surveillance or risk-as-permission |
| **Achievement/economic stewardship** | Core purpose/three Frontiers, Perpetua, existing stewardship extension | realized qualified positive change in owner-defined capacity/economics/quality, not agent busyness | shared benefit counted once; cash/forecast/social value distinct |
| **Relationship and obligation care** | owner-scoped goal/context/consented relationship facts, Perpetua follow-through, 73 persistence | qualified promise fulfilled or owner-rightfully revised | people are not assets; no presumed outreach grant or private disclosure |
| **Learning / competence calibration** | 138/138A, 80, 152A, Portable Memory; Observer MO-03..08 | independent held-out transfer/calibration improves within applicability | no automatic policy promotion, negative transfer holds/reverts |
| **Rest, homeostasis and restraint** | 71 resource/attention priors, Focus Gate, Spec 139 resource state, Core and Observer healthy quiet | bounded resource/attention load and owner well-being constraints hold | **zero work / no alert** can be a successful terminal condition |

SingleEye's **Will-to-Act**, bounded motivational signals, selective analytical/creative/critical debate, quiet associative discovery, reinforcement from independently verified outcomes, and recovery are useful; hormone mirroring, EEG pairing and separate neural-cognition runtime are not necessary dependencies for these behaviors. Its “hunger” metaphor is a governed, revisable **unmet purpose/commitment signal**, not a biological claim or machine-interest entitlement.

## 7. Proposed type/transition seam (candidate only; bind to existing owner APIs)

The organism is one reciprocal, scoped graph containing nested cognition and action loops:

    [Owner purpose and current source truth]
                  ↕
    [Core Master Loop / Perpetua commitments and expectations]
                  ↕
    [Qualified event/absence + Focusa scoped Intuition/Radar observations]
                  ↕
    [Spec 71 PRIOR BAND FILTER: hard, identity, current ask, mission, execution]
                  ↕
    [Spec 73 intentions/commitments/inhibitions + temporal/resource constraints]
                  ↕
    [Eligible choices → scalar priority / information value / causal hypothesis]
                  ↕
    [Spec 78 secondary cognition when warranted; Spec 138 predictions]
                  ↕
    [Source-bound initiative candidate, bounded existing-authority revalidation]
                  ↕
    [Native Workpoint / Foreman / Core concern / approved action dispatch]
                  ↕
    [Spec 136 settlement + independent evidence/receiver acceptance]
                 ↕  ↘
    [Reviewed Portable Memory WRITE→MANAGE→READ] ↔ [Master Observer experiment]
                  ↕                               ↕
    [Next eligible interpretation / revised pressure, forecasts and QUIET]

**Hard ordering:** Drive pressure does **not** precede or override 71 non-overridable/constitutional/current-ask priors. Agent motivation may select between admissible options, not authorize forbidden options. Radar/Intuition and Predictive observations are candidate evidence with explicit confidence, never equivalent to source truth. A remembered grant is not a grant. A previous standing authorization may be reused **only** through the current owning authority resolver, within its real scope, expiry, revocation and consequence class. No repeated approvals merely because a thought cycle restarts.

**Minimum event/edge contract to bind to existing implementations:** exact tenant/principal/workstream and source owner, typed original concern/commitment reference + causal predecessor, version/revision and observed/effective time, source evidence and coverage, privacy/trust, hypotheses vs facts, derived salience/drive kind and rationale, competing signals/inhibitions, 71 resolution band/result, current permission/grant resolution reference, actual execution attempt/idempotency, source/receiver result, verifier identity, disposition (unknown/blocked/verified/accepted), memory eligibility/revision, observer intervention/replay, resource spend and suppression/recovery. Extend actual owner envelopes only where missing; SOVOS is a meaning/provenance reference and must not claim a new storage schema.

**Candidate scoring research (not final arithmetic contract):** in an eligible decision set, drive pressure can combine separately normalized unmet commitment/owner-outcome impact, time-dependent risk/urgency, novelty/expected information value, expected outcome utility and persistence, offset by recently verified satisfaction, duplicate work, attention interruption, privacy/execution costs, cooldown and available capacity. Use bounded deterministic pressure/decay and per-driver explainability. Calibrate domains rather than one global dopamine proxy. Abstain when expected net gain is nonpositive. Do not conflate all domain priorities into one absolute score. Formal weights should be selected/validated by existing 138/152 and domain authorities.

## 8. IIT 4.0 and mathematics-of-mind requirement — testable, not ceremonial

**Non-optional system-design foundation:** useful, differentiated, reciprocal causal contributions between otherwise clearly owned components; inspectable state and typed dependency/feedback edges; bounded compositional nesting, perturbation and consequence tracing; no mere bus fan-out or transitive causal fiction. In this design:
1. Memory must **change** a permitted interpretation or decision versus a null-memory condition (or be honestly marked no marginal effect); its corrections must invalidate dependent interpretation.
2. A verified receiver outcome must **change** prediction/learning/commitment state rather than only append a success string. Model correction must influence future eligible attention/initiative.
3. Bounded observation must **change** timeliness or accuracy of eligible action, compared with observation suppression; repeated identical events back off.
4. Observer proposals must **change** measured real owner outcomes relative to fixed baseline/ablated candidate and include their own total monitoring/oversight cost; inconclusive remains inconclusive.
5. Specialized modules must have distinct causally attributable contributions and preserve consent/tenancy/rollback; a single high global “integration score” never replaces benefit evaluation.

**Two separate experiment planes:**
- **Operational:** compare intact vs controlled ablation/partition of Memory, Radar, 138 learning, Observer, and return feedback under matched events, grants, budgets and source/receiver baselines. Measure acceptance, missed obligations, time-to-verified-outcome, duplicate work, nuisance interruptions, signal coverage, false alarms, calibration, negative transfer, cost, protected rest and actual human capacity. Include multi-business and isolated second tenant, outages, stale grants, corrections, in-flight unknown action, healthy quiet.
- **Scientific IIT:** an *optional separate numerical finite-model study* may pin transition-probability model, states/grain, intervention distribution, partitions, formulation and the IIT 4.0 φ_s/Φ-structure terms. This **does not make mathematical integration philosophy optional**; it means not every production deployment must run an expensive Phi solver. No deployed consciousness claim, no “Phi grants authority,” no promotion of a variant with worse real outcomes just because a toy-model Φ increased. See Master Loop §13 and Observer MO-04/MO-07.

## 9. Algorithm Squared critical path to FULL delivery — without scope shrinkage

Apply the repo's actual Leverage² sequence: **Question → Delete unnecessary mechanics → Simplify → Accelerate → Automate**, but never delete accepted behavior or safety/evidence requirements. The “critical path” minimizes *time to the fully integrated organism*, not the feature set.

**CUT A — pin real ownership and runnable versions (parallelizable reads).** Source agent checks exact current OVH Core deployed checkout/binary, Focusa daemon version and registered routes, OpenClaw/Perpetua interfaces, provider/credential and permission owners, live memory writer, all existing branches/PRs and real source/receiver fixtures. Resolve Spec 71/73/80 doc-vs-code discrepancies, the Spec149/152A naming collisions and transcript memory owner. Document unknowns; do not start a new runtime or duplicate store. Tests: show current source revision/tenant/machine and API/CLI discovery with both PWAs off.

**CUT B — reuse the native Core source→concern→completion spine.** Extend existing Master Loop component/callgraph nodes (77/149 parent; 50 requirements) and Focusa scoped Workpoint/Trajectory/reducer/settlement to carry one reviewable drive-driven source-owned concern with exact permission revalidation, actual result and independent receiver evidence. This proves the real effect path without implementing a new scheduler. A first complete case is a progress milestone, **not** acceptance of every drive family or full spec.

**CUT C — close the conative and observation seams.** Build missing typed Commitment/CompletionDrive/inhibition transitions in Focusa 73 owning reducer/API if genuine code audit confirms missing. Connect 71 precedence and source-scoped Radar/Intuition/Foreman routing with dedup, time, provenance and true quiet behavior. Implement all F183 acceptance slices as part of accepted Radar scope rather than classifying absent projections “future work.” Keep Focus Gate advisory.

**CUT D — close epistemic and reciprocal Memory/Observer seams.** Reuse 80 actual endpoints and 138 typed authority ledger; eliminate unverified promotion, wire feedback from real outcomes to calibration/decision and reviewed Portable Memory with a single authoritative writer. Resolve cross-product memory binding under its owner. Implement Observer MO01–MO12 as functions/compositions on existing product owners with fixed experiments, receipts and negative controls; **no observer daemon**.

**CUT E — integrate all accepted drive families, surfaces, migrations and adverse paths.** Complete completion, discovery, protection, stewardship, relationships/consented obligations, competence, homeostasis/quiet and source/receiver proof. Ensure agent-first API+CLI parity, Wirebot app presentation if in accepted scope and optional W.I.N.S. stays independent; two-tenant isolation, recovery, model/OS portability as specified. Keep the same acceptance backlog until all required predicates are verified.

**Production-first protocol:** use **existing authorized** OVH/product release route, reversible narrowly scoped changes, exact installed-artifact/consumer readback and focused negative tests *in production*. Add backups and rollback/forward recovery for schema, privacy, credential and financial consequences; no new global staging bureaucracy, but “production-first” is not authorization for unreviewed destructive changes or customer data exposure. Independent portions may run in parallel when source/authority/state do not collide. Track every required capability to proof; no hidden deferrals or “prototype = complete.”

## 10. Acceptance/proof matrix required for final specification

| Case | Must be demonstrated on actual owning system |
|---|---|
| Current ask vs old drive | New owner steering suppresses outdated initiative despite old commitment, high completion score and queued work; no hidden topic hijack. |
| Standing consent vs permission crossing | Reuses real valid standing grant with no redundant prompt; expired/revoked/foreign/high consequence operation is held/escalated; memory never mints grant. |
| Completion truth | Actual receiver rejects/accepts work distinctly; no satisfaction from model narrative, task status, HTTP 200 or screenshot alone; unknown in-flight effect reconciled without blind replay. |
| Curiosity and no-information gain | Question/prediction/candidate has traceable expected value; duplicate unanswered issue deduped; no continual multi-model debate on stable cases. |
| Protection and false alarms | True scope-qualified risk starts permitted response; mismatch/expired evidence/tenant bleed suppresses alarm; incident != hypothetical risk != payable liability. |
| Memory causality/correction | Same case WITH eligible memory performs demonstrably better than null-memory; corrected/erased/foreign memory cannot continue deciding; reader/writer/sink receipts and OS portability as applicable. |
| Radar and Foreman | One developing episode across repeated events, no notification storm, exact Workstream identity and no global singleton; no ungranted external action. |
| Prediction and learning | Immutable forecast/information-set before observation; independent resolver+calibration and promotion/negative transfer; learning changes next qualified choice. |
| Observer value | Fixed intervention/ablation or matched rollout proves outcome improvement **net of** compute, supervision, interruption, privacy and rollback; harmful/no-benefit proposals revert or rest. |
| Homeostasis and human freedom | Resource pressure triggers degradation/quiet rather than activity compulsion; freed owner time not automatically refilled; net capacity/three Frontiers sourced. |
| Multi-owner/project/physical environments | Isolated second tenant, concurrent agents, duplicate source events, missing sensor, stale machine lease, unsupported app/Portal, revoked credentials and recovery paths do not cross scopes. |
| Full-spec and delivery integrity | Every accepted requirement traced to actual code/owner, test (including negative), installed version, live readback and independently accepted effect; no phantom partial-to-complete promotion. |

Actual Core parent callgraph, Focusa source bead/Workset and current release proof must be inspected and updated **in their owning repos** by the responsible server agent. This SOVOS handoff is source research, not an admitted runtime TaskGraph.

## 11. Open owner decisions and unsatisfied acceptance, without silent deferral

1. **Portable Memory transcript truth owner** remains explicitly unassigned by current SOVOS reference profile §18.1. Must be handled through owner-rooted architecture decision; do not assume Wiki/Mem0/Letta/Focusa silently own transcripts.
2. **Native memory producer/consumer contract** (two-sided writer, eligible recall, correction, deletion, migration and exact tenant) is still provisional; Wirebot Core memory-bridge presence ≠ end-to-end memory-driven business outcome proof.
3. **Spec 73 named conation objects**: reconcile exact current reducer/ontology/CLI/API and whether CompletionDrive is materialized; some commitment lifecycle projection exists, not end-to-end conative organism proof.
4. **Spec 80 status inconsistency**: obsolete planned header/evidence vs real current route code; independently qualify current daemon/API/CLI and update documentation at Focusa owner, no duplicate tooling.
5. **Spec 78 program scope**: historical closure certificate does not settle every distinct reactive/secondary cognition role in future drives.
6. **Spec 138/138A full maturity**: current feature-ledger and release proof need verification beyond early foundation and individual atom records.
7. **Spec 183 Radar and 182 Foreman**: draft target scopes, with no verified named Radar runtime code in search or live producer/consumer proof here; versioned actual API/CLI and Workstream ownership must be qualified.
8. **Observer §11** lives only in open SOVOS PR #31; do not implement conflicting copy or claim merged authority/deployed daemon.
9. **IIT integration proof**: no actual controlled intact/ablated operational report for the complete drives+memory+observer organism was executed in this research. The separate finite-model mathematical study may be bounded, but design and operational ablation are required.
10. **Current installed Core/Focusa state**: repo and historical proof do not establish present production version, working credentials/tenant binding, or independent external receiver satisfaction; the server agent must collect first-party live evidence before reporting completion.
11. **Document label collisions** (#149 and #152A) and historical Radar164 alias require explicit pathname resolution to prevent wrong dependency import.
12. **Scope/acceptance remains whole**. The project may stage implementation; none of these open rows is permission to relabel specified requirements optional or silently skip them.

## 12. Exact server-agent handoff

> Work from SOVOS draft PR #34 and this audit, preserving the open master observer #31 and stewardship #32 changes. Inspect owning Focusa and Wirebot Core live source/deployed binaries and the full native 77-frame callgraph before editing. Reconcile the historical contradictions above, resolve exact owner/memory/contracts and implement in product owner repositories using the current authorized production-first deployment route. Map each accepted requirement to source, executable consumer, grant, negative proof, installed commit and independent outcome; never invent task closure. Treat 71 precedence, 73 conation, 78 bounded secondary cognition, 80 tool parity, 138 epistemics, 183 Radar, 136 settlement, 137 time, 139 presence, 176 Judge, 182 Foreman, 152 statistics, Portable Memory, Master Loop and Master Observer as interdependent owners, not duplicate engines. Apply Algorithm Squared to mechanics, not capability scope. This research is not itself the final accepted spec or a production access grant.

**Research outcome:** the architectural direction and concrete dependency/gap trace are substantially sharpened; spec drafting can now use this evidence map, but **full installed-runtime audit, full final spec, and deployment acceptance remain outstanding**.
