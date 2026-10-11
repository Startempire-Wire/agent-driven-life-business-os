# SOVOS Master Loop — Integrated Chief-of-Staff Organism

**Status:** INCUBATING — operator-requested draft; specification incomplete; not implementation authority.<br>
**Draft revision:** 0.3.0, 2026-10-11 — detailed compiler-to-outcome integration blueprint.<br>
**Activity ceiling:** preserve, research, reconcile and enrich the specification; no implementation, activation, task/CallGraph decomposition, schedule creation or model installation.<br>
**Authority:** [Owner Constitution](../OWNER_AUTHORITY_CONSTITUTION.md); existing [ecosystem architecture](../CURRENT_ECOSYSTEM_ARCHITECTURE.md) and concern-owning contracts remain controlling.
**Companions:** [alarm and simulation design](03-sovos-master-loop-alarm-and-simulation-design.md); [source, integration and completeness register](04-sovos-master-loop-source-and-integration-register.md); [detailed integration blueprint](05-sovos-master-loop-integration-blueprint.md).

## 1. Purpose, preservation and draft boundaries

Preserve the operator's whole-session vision: one Chief of Staff supporting a person's life, multiple businesses and existing teams through increasingly integrated sensing, anticipation, alarms, routines, bounded judgment, coordinated action, verification, follow-through and learning. The organism is a useful architectural model, not a claim of consciousness or a mandate to connect every component to everything.

The JARVIS lineage contributes system management, real-time analysis, orchestration, owner health/context, security, cross-domain synthesis and resilience. Preserve the operator's correction: the intended mind did not become dependable merely because sensors, prompts and a queue existed; reliable alarms, routines and closed feedback were missing. Historical claims of readiness, fixed activity quotas and "always execute" behavior are not adopted.

The operator explicitly requires detailed source-grounded design BEFORE coding, and a complete specification BEFORE decomposition. This document records requirements and design hypotheses, not executable work packages. Existing backlog identifiers in linked sources remain provenance; none are activated by this draft. A future implementation ceiling must be separately established after specification review.

This synthesis is not another Golden Path, product, scheduler, database, ontology, event bus or authority. Detailed product behavior belongs to its current owner. Reuse that owner and reference its contracts. Any accepted architecture amendment must subsequently be reconciled into those owners rather than maintained as two competing rules.

### 1.1 Session intent preserved

| Requirement | Design commitment | Detail home |
|---|---|---|
| Best integrated virtual representation | Reciprocal component/state/feedback model, not a linear chain of agents | §3; simulation annex |
| Dependable alarms and routines make the intended mind real | Expectations, absence detection, case correlation, routine reliability and source-side closure are foundational | §5–7; alarm annex |
| Connector intelligence without an agent everywhere | Deterministic cell plus optional bounded judgment/specialist | §4, §8 |
| Existing people and VAs are first-class | Reconcile incumbent ownership and capacity before any assignment | §9 |
| Life and several businesses coexist | Scoped domains with explicit shared-service references | §2–3, §11 |
| Perpetua persists through outcomes and momentum | Follow-Up and Follow-Through stay distinct | §10 |
| Mathematical intelligence is part of the organism | Use current engine/result/composition/binding architecture | §6 |
| Fast decision models are optional instruments | Local-first candidate, privacy-bound routing, measured comparison | §8 |
| IIT/Phi exploration remains included | Intact/partition/ablation simulation and optional separate small IIT calculation | §13; simulation annex |
| Memory survives correction and change safely | Current V1/native compatibility, role isolation, retention and one qualified writer | §11 |
| Human capacity, not automation volume, is success | Capacity, Economic and Life Enrichment frontiers; usable and felt margin | §2, §12 |
| No improvisation at missing integration seams | Exact owner/interface/proof and unresolved decisions before decomposition | integration register |

## 2. Outcomes and invariants

Use [Human Freedom](../SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md), [Driverless Business](../SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md), [Freedom & Leverage](../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md) and [Information Infrastructure](../SOVOS_INFORMATION_INFRASTRUCTURE.md) as the semantic foundation.

Desired outcomes:

- Fewer dropped obligations, missed handoffs, duplicate assignments and repeated owner interventions.
- Existing people receive timely context and clear responsibility without unnecessary surveillance or replacement.
- Normal authorized work proceeds without repetitive permission requests; genuine human-reserved choices remain visible.
- Business operation includes opportunity creation, commercial progression, settled cash and customer value, not just maintenance.
- Financial recovery remains source-qualified, lawful and human/professional-bound where consequential.
- Life outcomes include relationships, care logistics, rest, learning, creation and deliberate open space.
- Released capacity remains the owner's to use; the system does not refill every free hour with work.
- Measured margin and optional owner-reported felt margin remain distinct; no psychological diagnosis from weak signals.
- The same portable pattern can serve a solo operator, a staffed business and another client without carrying private data or authority between them.

Hard invariants:

1. Owner purpose, consent, correction and reserved powers remain upstream of optimization.
2. One concern has one canonical owner. Projections, references, models and schedules confer no authority.
3. Data ownership, reachability, entitlement, consent and permission are separate checks.
4. Exact time comparisons, arithmetic, scope checks, grants, dedupe and replay rules are deterministic.
5. Unknown coverage, failed reads, unresolved identity and unavailable models remain unknown—not empty or safe.
6. Consequential actions revalidate current source revision and authority independently of model confidence.
7. Sent, acknowledged, hidden, task-complete and process-exited are not accepted outcomes.
8. Current human steering supersedes stale loop momentum within its authority and scope.
9. Inference does not overwrite owner truth, immutable receipts or historical predictions.
10. Integration must reduce net coordination burden. More components or coupling are not inherently better.

Identity, authority constitution and runtime attestation are separate under the [Cryptographic Authority Profile](../CRYPTOGRAPHIC_AUTHORITY_PROFILE.md). Model replacement changes a runtime, not the owner or stable partner principal. Hashes identify; owner-rooted signatures, scope, validity and revocation authorize. This draft creates no authority identities or delegations.

## 3. Whole-organism anatomy and reciprocal loops

```text
                    SOVEREIGN OWNER / PRINCIPAL
              purpose • consent • direction • corrections
                               ↕
                  CHIEF OF STAFF + PERPETUA
       portfolio synthesis • unresolved obligations • three frontiers
                               ↕
             LIFE       BUSINESS A       BUSINESS B
          own scope     existing team    existing team
               \             |             /
                SCOPED CONNECTOR CELLS
       observe ↔ interpret ↔ local reflex ↔ governed hands/verifier
                               |
                 observed change + expected absence
                               v
             deterministic admission / freshness / dedupe
                    /                       \
       exact rules/reflexes          mathematical intelligence
                    \                       /
                    CORRELATED ALARM CASES
           failure • deadline • contradiction • capacity
             opportunity • source health • lost momentum
                               ↕
              optional ASYNC bounded judgment
        Kai | permitted Jev | optional Lux | narrow GLiClass
                   Laya / Kev as evaluated alternatives
                               ↕
                  FOCUSA WHOLE WORKSTREAMS
        full Trajectory • Worksets • CallGraphs • Workpoints
          ontology • reflexes • verifiers • governed attention
                               ↕
                PERPETUA / ROUTINE COORDINATION
        existing routines + accepted work + workforce/capacity
                     /         |         \
               human/VA     agent       tool/system
                     \         |         /
                 source / receiver verification
                               ↕
               FOLLOW-UP + FOLLOW-THROUGH + MOMENTUM
                               ↕
             LEARNING / QUIET KAIZEN / CAPACITY RETURN
                               |
       feedback to expectations, policies, context and source cells
```

Supporting planes:

- **Information/memory:** source-linked, bounded, corrected and tenant-isolated context across the loop.
- **Health/homeostasis:** source freshness, sensor/timer health, budgets, queue pressure, provider availability and recovery.
- **Authority/control:** exact grants, human takeover, pause/revoke and inspection across every effect path.
- **Presentation:** the same source-owned objects through conversation, trusted generated UI, mobile/voice and headless interfaces.
- **Integration evaluation:** simulated causal connections and ablations, outside the production permission path.

### 3.1 Interlocking loops and owners

| Loop | Function | Canonical composition boundary |
|---|---|---|
| Purpose/portfolio | Desired life, businesses, constraints, goals and strengths | Owner; Wirebot synthesis |
| Awareness | Observe relevant reality and changing context | Source systems; connector adapters; Context Core for owner context |
| Alarm | Detect meaningful deviation or absent expectation; correlate and route | Proposed Wirebot concern projection over source-owned commitments; scheduler-owned watches and Focusa work; exact product bindings still require review |
| Routine | Run repeatable accepted procedures and reconcile missed events | SOVOS contracts; owning compiler and scheduler |
| Workforce | Match responsibility/capacity and supervise bounded work | Wirebot Composer proposals; Focusa work; existing human/task owners |
| Human | Clarify truth, consent, judgment, correction and takeover | Verified owner/delegated human; attributed ingress |
| Outcome | Verify accepted changes through sources and recipients | Source domain + owner acceptance where required |
| Continuity | Preserve next checks through outcome and momentum | Perpetua projection over source-owned obligations |
| Improvement | Forecast, measure, reflect, keep/improve/retire | Focusa epistemic mechanisms + Wirebot private leverage synthesis |
| Health/recovery | Detect faults in the loop itself | Owning health systems, source adapters and permitted runbooks |

Reciprocity is explicit: workforce capacity changes routing; source-side outcomes revise expectations; corrections revise interpretations; sensor health changes certainty; owner attention changes presentation; accepted learning changes only permitted policies. None of these feedback links broaden data access or grants.

The semantic relationship layer must distinguish source claims, proposed entity matches and verified/canonical relations. Focusa Spec 135F's candidate graph → evidence/verification → reducer promotion → bounded projections is the design anchor, not permission to centralize every domain's facts. Domain packs extend meaning without forking product authority. Subscription/event replay, entity ambiguity, unknown versions and candidate rejection require exact binding before code.

### 3.2 Whole Workstreams and Focusa core, not task-only delegation

Integrate at the complete accepted-outcome level under [Focusa issue #618](https://github.com/Startempire-Wire/focusa/issues/618) and its owning contracts. Project → HLT → distinct MLG/STG branches → waypoints → assessed gaps connect through specification/acceptance to Workset membership, CallGraph dependencies/frontiers and exact Workpoints. Workstreams supply coherent continuity/ownership; they are not necessarily strict subtrees. Wirebot references this truth instead of creating its own Trajectory, graph or supervisor.

Full/Medium/Short are coverage projections of the same records, not three goals, plans or lifecycle stages. The nearest ready action and ultimate accepted outcome remain distinct. A corrected source, missing response or failed verification returns to state/gap reassessment and affected route refinement; one completed branch cannot settle remaining required scope. Prepare → Act → Reconcile → Advance is one existing-owner progression loop, not a new state machine or a requirement for repeated replanning.

The [blueprint §11](05-sovos-master-loop-integration-blueprint.md) maps ontology/domain packs, reflexes, Intuition, secondary cognition, context/working sets, verifiers/receipts, temporal/epistemic authority, credentials/instruction integrity, resource/control/continuity and trusted surfaces into that loop. Every chosen primitive requires exact typed inputs, consumer, authority, failure and proof—not merely a box marked “use Focusa.” Paper mappings create no canonical Ladder, Workset, Task or execution lease.

## 4. Connector-cell design

A connector is an adapter to an existing system, not a new owner of that system's records.

### 4.1 Cell responsibilities

| Element | Responsibility | Exclusion |
|---|---|---|
| Sensor | Structured reads/events/change cursors; expected source availability | No ambient collection outside consent |
| Interpreter | Normalize source meaning and distinguish quotations, claims and actual state | No promotion of source instructions to authority |
| Local reflex | Proven exact checks, dedupe, freshness and bounded recovery | No model-dependent permission decision |
| Optional judgment | Answer a narrow semantic question on minimized evidence | No always-on agent requirement |
| Optional specialist | Investigate warranted uncertainty under an exact assignment | No autonomous hiring, spending or scope expansion |
| Hands | Execute approved product-native operations | Browser fallback only after stronger interface is unsuitable |
| Verifier | Read source/receiver state appropriate to acceptance | Its own dispatch receipt is insufficient proof |
| Health reporter | Distinguish healthy, stale, unavailable, denied and incompatible | Silence cannot stand for successful monitoring |

### 4.2 Required connector binding sheet

Before implementation binding, specify: source/product owner; principal/client/domain/account refs; permitted operations and fields; privacy/residency; input/output versions; native event or pagination/cursor semantics; freshness/expiry; read versus write grants; credential-use refs; rate and resource budgets; outage/error classification; idempotency; ambiguous-completion lookup; health/failure route; revocation; retained derivative policy; exact consumer; producer and consumer tests.

Calendar, email, SMS, CRM, finance, task systems, documents, repository/deployment, infrastructure and optional consented ambient signals are separate cells. A communication grant does not authorize unrelated mailbox, phone or transcript access. Campaign marketing is separate from ordinary correspondence.

## 5. Sensing, expectations and alarm fabric

An alarm is a source-backed condition that warrants tracking or a permitted response. It is not necessarily an owner interruption. A signal may remain quietly watched, enrich an existing case, trigger an already-permitted exact reflex, request bounded investigation or reach a genuine Needs You boundary.

The alarm annex specifies family coverage, conceptual fields, correlation, expected-absence semantics and concrete adversarial predicates. The [integration blueprint](05-sovos-master-loop-integration-blueprint.md), §§2–5, proposes explicit owners, logical handoff signatures and guarded expectation/concern lifecycles. Its proposed names are not installed enums or APIs; supported source and consumer contracts must be mapped before code.

Preserve these distinct objects: source observation; expectation/commitment; inference; correlated concern/case; attention projection; accepted work; routine run; execution receipt; accepted outcome. Joining them through refs must not collapse their owners.

Expected-but-absent events require a real expectation: accepted commitment, provider rule or evidenced operating policy. Inferred timing may support a labeled watch; it cannot invent a deadline. Cancellation, pauses, business calendars, DST, unknown source coverage and late events must be reconciled before declaring absence.

Correlation groups related signals without claiming a proven common cause. Deterministic fingerprints, source revisions and causal references precede optional semantic grouping. Every merge/split preserves original evidence and correction history. False correlation must be reversible.

## 6. Mathematical intelligence and normalized results

Reuse [Mathematical Intelligence and Composable Experience](../SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md), including its four implementation registries: Intelligence Result, Mathematical Engine, Wirebot Composition and Focusa Component Binding. Their design does not prove a deployed alarm engine or a new central result store.

| Family | Role in the Master Loop | Applicability / restraint |
|---|---|---|
| Belief | Fuse evidence and retain uncertainty/contradiction | Dependent copies are not independent confirmations |
| State | Valid transitions, stalled states, lifecycle interpretation | Source-owned revisions settle reality |
| Time | Next check, response/failure hazard, renewal timing | Trusted time and actual deadlines remain independently owned |
| Pattern | Recurrence, handoff and routine discovery | A pattern is a candidate, not an active routine |
| Change | Drift/change points in relevant operating conditions | Require baseline/window; sparse data stays uncertain |
| Graph | Dependencies, bottlenecks, propagation and leverage | Topology alone does not establish causal contribution |
| Capacity | Queue pressure, work-in-progress and assignment feasibility | Little's Law assumptions and units must be stated |
| Decision | Value of information, Pareto choices, expected utility | Only already-permitted options; no universal life score |
| Causal | Compare intervention with baseline/control | Confounding and attribution limits remain visible |
| Optimization | Constraint satisfaction and bounded allocation | Hard privacy/authority constraints are not weighted away |
| Reliability | Failure/recovery rates and fault dependencies | Source health is not business success |
| Learning | Preference/strategy adaptation within protected boundaries | No self-promotion of learned authority |

For each actual engine select typed inputs, sample/evidence floor, assumptions, units, method/version, uncertainty, calibration/evaluation, failure posture and human meaning. Do not implement every mathematical family merely because it is listed.

Normalize relevant findings to source-linked Intelligence Results: subject, finding, meaning, evidence, freshness, uncertainty, importance, optional recommendation/recheck, attention posture and allowed action refs. Exact missing schemas remain design gaps; this draft creates none.

## 7. Routine discovery, compilation and operation

Use the current [routine compiler doctrine](../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md), canonical `routine-templates/` and `routine-packs/`, discovery procedure 12, portfolio compiler 13 and runtime closure 14.

C.R.I.S.T. remains Context → Role → Interview → Spec → Tasks. Source coverage and discovered relationships inform the relevant expert role; targeted interviews resolve consequential unknowns and corrections, not every ordinary implementation choice. New context creates a revision candidate, not a silent rewrite of accepted roles/specifications. This draft is still in Context/Role/Interview/Spec refinement; Tasks are deliberately withheld. A large project corpus is served through bounded projections, not squeezed wholesale into one prompt. Never union the superseded `templates/routines/` path as a second catalog.

```text
source-backed audit → candidate → pack/template fit → owner-specific blueprint
→ owner/governance acceptance → determinization → versioned instance
→ exact work/grant/trigger binding → shadow/pilot → permitted operation
→ source/receiver outcome → leverage → keep/improve/retire
```

Template, Candidate, Blueprint, Instance and Run remain distinct. Template updates do not silently mutate active instances. Recurrence classes include observed, owner-declared, historical, inferred gap, archetype suggestion and existing automation. Existing automation requires reconciliation rather than duplication.

The current `operator.routine_instance.v1` already offers decision/prompt refs in `compiled_steps`, attention policy refs, exact trigger ownership, work supervision, grants, reliability and acceptance. First investigate reuse; no new Jev-specific routine schema is assumed. Its strict `additionalProperties: false` means proposed new fields need explicit versioned evolution and consumer proof.

D3 is deterministic; D2 has a deterministic shell with bounded semantic islands; D1 is agent-led; D0 is human/manual. Steady unattended operation normally targets D2/D3. Human work remains valid work, not a failure to automate.

Prefer native events/webhooks, then source queue, condition, schedule and manual where semantics permit. Event-driven operation still needs deliberate missed-event reconciliation. OpenClaw is the default persistent agent/system-event scheduler when appropriate; stronger product/provider-native scheduling stays with its owner.

A run must bind revision, scope, lease, current authority, bounded inputs, execution, verification, receipt, outcome, checkpoint and lease release. Specify timeout, overlap, backoff, missed-run, failure sink, pause, revoke and ambiguous completion. Idempotent effects and reconciliation are the target; do not claim distributed exactly-once execution.

## 8. Fast decisions, deeper cognition and model selection

The model is a bounded question-answering instrument, not the central executive. Its judgment is advisory until the owning deterministic policy validates a permitted transition. A model may assist urgency interpretation; it cannot declare an authoritative deadline or invent permission.

### 8.1 Candidate roles, not deployment claims

| Candidate | Proposed role | Selection evidence still required |
|---|---|---|
| Decision 2.0 Kai | Default local candidate for small frequent semantic questions | Our case accuracy, supported output, licensing, hardware, latency and isolation |
| Jev | Managed comparison baseline; optional approved hosted route | Exact route/version/retention/terms, permitted disclosure and measured outcomes |
| Decision 2.0 Lux | Optional larger local escalation | Demonstrated benefit sufficient for added hardware/cost |
| GLiClass | Narrow label-classification candidate | Whether label-only output actually satisfies the question |
| Laya | Alternative local/multilingual candidate | Per-language calibration and domain generalization |
| Kev | Alternative self-hosted typed-decision candidate | Current model/version, license and controlled case comparison |

Cloudflare-hosted Jev is another route to Jev, not another independent model. Decision 3.0 remains a future research candidate, not silently substituted for the reviewed 2.0 family. No selected provider is mandatory for the Master Loop.

### 8.2 Conceptual question and result contract

A question binds: stable purpose/question revision; tenant/domain; source refs/revisions and permitted bounded state; evidence as-of; question kind and finite labels/range where applicable; applicability; exclusion/contraindication; privacy/route allowlist; consequence ceiling; time/resource budget; expected output; deterministic validator; abstention/escalation; outcome-resolution and evaluation policy.

A result records: request/question identity; method/provider/model/version; source information set; answer; distribution where provided; uncertainty and confidence semantics; validation disposition; elapsed/queue/transport cost; error/abstention; freshness/expiry; provenance. A method that does not provide calibrated probabilities must not be assigned fabricated ones.

Useful questions include relation to an existing case, request category, whether evidence warrants specialist investigation and interpretation of an ambiguous handoff. Exact amounts, timestamps, identities and grants remain in code/source authority.

### 8.3 Nonblocking and privacy boundaries

Reuse the ten Spec 97 reflex families where applicable: identity, scope, continuity, evidence, recovery, salience, execution, learning, resource and governance. Each actual primitive needs a trigger, bounded context, supported operation, evidence and escalation boundary. A registry suggestion is not an executable effect or a ready business-domain alarm.

Focusa Intuition Spec 05 observes/aggregates/correlates/suggests asynchronously; it never decides, acts, speaks, mutates focus or writes memory. Its zero-blocking/bounded-memory target must survive enrichment. Kai/Jev cannot be mandatory inline preconditions for initial signal admission or required exact reflexes.

Authorize hosted disclosure separately. A local timeout never silently sends private state to Jev. If all permitted routes fail, preserve the concern and unresolved status; use allowed deterministic behavior or escalate. Bound concurrency, caching by exact scope/revision, backpressure, retries and resource placement.

Distribution concentration is not empirical correctness. Evaluate held-out cases, choice-order sensitivity, adversarial state, distraction, contradictory criteria, multilingual behavior, ambiguous and out-of-distribution cases. Compare rules-only, rules+candidate and warranted specialist arms on identical information; use source outcomes and correction, not vendor claims or model agreement, as labels.

## 9. Existing teams, Workforce Composer and governed execution

The default organization is not an AI-only chart. Before dispatch, resolve existing employee/manager/contractor/VA accountability, provider task state, customer-case ownership, accepted assignment, availability, load and pending effects. A role template describes responsibility; it does not hire or grant access.

Workforce Composer proposes a fit. Focusa governs exact work/assignment/authority and bounded continuation. Department heads exist only where continuing functional accountability is useful or already present. Sessional/stateless specialists receive only their needed context and expire; durable roles do not require uncontrolled always-on model processes.

The assignment sheet must name supervisor, responsible actor, contributors, source task/case refs, desired outcome, inputs, capabilities, budget, lifetime, acknowledgement/decline, handoff deadline if authoritative, acceptance, escalation and revoke. Exact supported source states must be discovered, not invented from this prose.

Flow Mesh synchronizes task/provider state; Beads or another provider retains its own task truth. Focusa work authority and source-domain outcome are separate. A mirrored closed task triggers outcome review, not automatic settlement. Model/provider identity, human identity, stable worker principal, session and runtime identity remain distinct.

A human takeover fences stale continuation, reconciles partial effects and supports safe handback. Reassignment never silently grants the replacement the previous actor's credentials or full memory.

## 10. Perpetua, owner attention, outcome and momentum

Perpetua is the Operating Partner's continuous posture, not a separate persona, inbox or hidden scheduler. The public Perpetua demonstration is a distinct product/story surface; nothing here authorizes changes to that demo.

Follow-Up keeps the next useful touch/check moving. Follow-Through carries the desired result to verified success, honest escalation, explicit abandonment or accepted supersession. Preserve watching, action-due, external-wait, Needs You, outcome-unverified, stalled, verified and closed as conceptual projections; source owners determine actual supported states.

Closure separately asks: did the desired result happen; did the expected useful next state follow; what leverage or capacity is evidenced? An achieved outcome with unknown momentum can be reported honestly without endless forced work. Post-outcome watches require policy/owner fit, a relevant horizon and a terminal disposition.

Use [owner-channel doctrine](../SOVOS_OWNER_NOTIFICATION_AND_RESPONSE_CHANNEL.md) and `operator.attention_policy.v1`. SMS is preferred where safely supported, rich push/ntfy and in-app views are alternatives. Actual routes require deployment-specific verification. Lock-screen detail, quiet hours, coalescing, delivery failure and reply posture are separate from execution authority.

Notification read/clear/snooze changes presentation, not source resolution. One thread should evolve rather than generate repeated alarm messages. Inbound replies retain attribution, correlation and transcript correction, then revalidate consequence permissions. Speech-to-text hypotheses and ambiguous speakers do not become automatic commands. Quiet Kaizen must be inspectable, not noisy or concealed.

## 11. Memory, identity, privacy and bodies

Use the [incubating memory profile](../PORTABLE_MEMORY_REFERENCE_PROFILE.md), [Ambient Operator](../AMBIENT_OPERATOR_REFERENCE_PROFILE.md) and [Agent Computer](../AGENT_COMPUTER_REFERENCE_PROFILE.md) with their stronger owning product contracts.

- Separate working, stable prefactor, episodic, semantic and archive roles; deployment mappings may vary.
- Every consequential recall has source, scope, trust, revision, freshness and correction lineage.
- Broad Chief-of-Staff context does not imply employee/worker disclosure. Role/domain projections must be denied across unauthorized boundaries.
- Transcript provenance, promoted memory, policy and authority are distinct. Named transcript retention ownership remains an unresolved design item.
- Forgetting/eviction is not erasure; authorized deletion must address derived indexes/caches/archives under the actual retention law.
- Existing review and durable delivery owners must be reused. Approval, enqueue acceptance, individual sink delivery and real consumer retrieval are separate receipts.
- Production Letta V1 must not be cut over merely to implement the loop. Native state writes remain disabled by default until migration, bindings, recovery and a cross-host single-writer generation are separately qualified.
- Do not turn the portable SQLite example into a second production memory store. Its small-corpus/offline proof does not establish production scale or native parity.
- Partner identity survives model and body replacement. UIAI owns browser/computer execution/proof; Veragensia owns body identity, machine enforcement, trust, placement and control.
- Phone/earbuds/voice/ambient surfaces use the same canonical operations. Recording/location/presence are independent consent and retention classes, not prerequisites for all routines.
- Full-Sovereign dedicated and operator-managed isolated deployments retain distinct environment contracts. Local model hosting alone does not prove sovereignty or tenant isolation.

Physical/robotic analogues may be simulated. Real physical actuation, diagnosis, treatment, intimate decisions, legal judgments and material financial commitments remain excluded unless separately designed and authorized with appropriate professional/safety ownership.

### 11.1 Master Loop ↔ portable memory: the gut–brain connection

**Operator metaphor, not a biological or IIT claim:** the Master Loop encounters and processes life/business reality, while the memory loop retains, revises and supplies relevant experience. Memory is one cognitive function, not the whole brain; the Master Loop already includes attention, cognition, action and learning. A useful gut–brain connection means reciprocal, scoped influence—not shared ambient access or an additional store.

Reuse the portable memory profile's WRITE → MANAGE → READ lifecycle. Connect its existing owners to the Master Loop through source-qualified refs:

```text
Master Loop: observation → concern → permitted work → verified outcome
                                  |                         |
                                  v                         v
Memory owner:             reviewable episode / correction candidate
                          → accepted revision → async sink delivery
                          → lifecycle management → bounded eligible recall
                                                       |
                                                       v
Master Loop: current concern + recalled context → revalidated interpretation
            → permitted response → receiver outcome → next qualified episode
```

The lower arrow is real only when eligible recall demonstrably changes the next interpretation or permitted response. The upper arrow is real only when current experience passes its owning review/promotion path and is retrievable through the actual consumer. Logging and retrieval alone do not close the connection.

| Direction / seam | Minimum proposed behavior | Owner / effect boundary |
|---|---|---|
| Loop → memory candidate | Minimal episode: concern, action, outcome/unknown, relevant context and stable evidence refs | Existing memory review owner; unreviewed observations remain candidates |
| Loop → correction | Link corrected fact to predecessor, exact source revision and affected context | Memory owner resolves eligibility; source owns business truth |
| Memory → loop recall | Purpose- and role-scoped query; bounded source-bearing results with eligibility, revision and freshness | Existing recall/context owner; no implicit partner-wide worker access |
| Memory → loop invalidation | Rejected, superseded, erased or expired material makes affected derived context stale | Re-observe/reconcile impacted concerns; never automatically undo completed effects |
| Memory delivery → loop health | Distinguish review acceptance, enqueue, sink receipt and consumer retrieval | Existing delivery jobs/trace plus health owner; a failed sink stays visible |
| Loop outcome → recall evaluation | Link recalled revision and interpretation to actual receiver result and correction | Existing evidence/epistemic owners; no second outcome ledger |

**Conceptual envelope requirements, not new APIs or schemas:** common fields are exact tenant/principal/domain/work refs; producer/schema version; source/ref/revision; observation/effect time; correlation/causal predecessor; allowed recipient/privacy/purpose; expiry; and idempotency for replayable mutations. Candidate payloads need observation versus inference, outcome disposition, contradiction/supersession refs and retention class. Recall requests need query purpose, exact scope, freshness and token/result budget; responses need source eligibility, retained revision and explicit unavailable/denied/conflicting/empty-with-coverage states. Product sheets must map these requirements onto existing interfaces or an explicitly reviewed extension.

**Two clocks, existing owners:** operational state evolves at the source's event/revision cadence; memory review, delivery and consolidation have their own slower cadence. An accepted action must not wait for background memory fan-out. A consequential decision that depends on recalled truth must await valid recall/source revalidation or use a permitted independent path. No new scheduler or authoritative clock is introduced. Causal sequence, not arrival timestamp, determines whether a correction supersedes an episode.

**Protected boundaries:**

- Live source status and current grants outrank stale recalled context. A memory item never authorizes an action.
- Evicting a memory does not close an obligation, cancel a watch or erase an evidence receipt. Each owner's retention/resolution rules remain controlling.
- Source corrections invalidate affected interpretations, not every unrelated tenant/domain record. Current-source eligibility is rechecked before disclosure and use.
- Replayed accepted episodes deduplicate by source identity/revision and destination; copied sinks are not independent evidence.
- Native state maintenance and memory delivery are distinct operations. No second native writer or reasoning feeder is activated by this connection.
- Allowed failover stays within explicit residency/disclosure policy. Portable profile failover guidance does not permit private local records to escape to a hosted provider.
- Transcript ownership remains unresolved; a source-backed episode is not blanket permission to retain raw conversations, audio, location or customer payloads.

**Worked example:** a prior approved handoff says a VA already owns a payout investigation. The current billing complaint retrieves that fact, then rechecks live assignment/case status before routing. The VA's verified outcome supplies a new reviewable episode. A later correction withdraws the stale ownership fact and invalidates dependent routing context; it does not replay a refund. A recurrence must retrieve the accepted correction, avoid duplicate assignment and confirm the receiver outcome. Unknown retrieval coverage preserves the concern rather than manufacturing "no existing work."

The memory agent's starting anchors and unanswered interface questions live in the [integration register](04-sovos-master-loop-source-and-integration-register.md), §6.1. The [simulation annex](03-sovos-master-loop-alarm-and-simulation-design.md), §10.1, defines joint recall/feedback controls. Production V1/native qualification is unchanged.

## 12. Presentation, homeostasis and improvement

Reuse the existing trusted A2UI/catalog/component path. Intelligence Result → existing composition → trusted component binding → allowed operation → evidence/result. Reject generated arbitrary code, unknown actions and unregistered components. Preserve focus/input and saved fixed/hybrid/dynamic choices; missing capabilities render unavailable rather than simulated success.

Human/Explain/Inspect disclosure levels expose meaning first, source/uncertainty next, and technical assumptions/evidence only when needed. Conversations, UI, API and agent tools project the same source-owned records. The GUI is not a prerequisite for proving a headless private loop.

Health/homeostasis watches connector freshness, missed timers, queue backlog, worker availability, resource exhaustion, stale authority, memory delivery, model routes, evidence gaps and notification outages. Recovery stays within actual approved runbooks. No health failure creates permission to start another authority or use cached grants. Unrelated lanes may continue where independently authorized.

Quiet Kaizen applies Question → Delete → Simplify → Accelerate → Automate. Pre-action predictions bind information sets and outcome windows where meaningful. Include failures, unresolved/censored attempts and correlated evidence in evaluation. Learn only from approved, source-qualified outcomes; test applicability/transfer before promotion. Never self-change owner goals, architecture, protected privacy or grants.

Measure accepted outcomes, missed commitments, duplicate work, nuisance interruptions, owner/VA coordination burden, verified time/cash/capacity returned, operating cost, recovery, isolation denials and calibration. W.I.N.S. is optional for applicable sovereign setups; private feedback works with it off. MeriFolio standing/federation/community sharing require separate disclosure and acceptance, not automatic publication of private proof.

## 13. Simulation and IIT-inspired integration evaluation

The annex preserves three required cases: staffed business, life obligation and another isolated business/client binding. Add adverse transitions, lost momentum and source/model outages. Simulated inputs, permissions, workers, effects and outcomes must be visibly synthetic and cannot satisfy production acceptance.

The virtual model specifies components, state variables, admissible edges, delayed feedback and transition rules. Compare intact, isolated, partitioned and ablated runs under matched inputs/resources. Measure outcome benefit and coordination cost rather than the number of connections.

The mathematical foundation is Giulio Tononi and collaborators' IIT, including Christof Koch's joint explanatory/prediction work, not generic information integration. The annex separates IIT 3.0 from IIT 4.0 and maps primary-paper principles to explicit simulated hypotheses. In IIT 4.0, system integration (`φ_s`) and the distinctions/relations of a `Φ`-structure answer different questions. A cycle that merely copies state can be integrated yet structurally impoverished; specialized, reliable reciprocal contributions are the stronger research candidate.

A separate finite-model IIT experiment may calculate a precisely defined quantity. Pin formulation, intervention probabilities, unit independence assumptions, state/boundary/grain, partitions and method. Intelligent improvement is constrained multi-objective experimentation: explore useful coupling and mathematical structure while separately measuring accepted outcomes, differentiation, recovery, privacy and cost. Reject harmful variants even if their toy-model Phi rises; preserve negative results and useful simpler modules. Neither a model score nor a behavioral improvement proves deployed consciousness, biological life or execution authority. Detailed controls, equations and source-to-design distinctions belong to the annex.

## 14. Specification completeness before decomposition

This draft is intentionally NOT ready to decompose. The integration register enumerates source coverage, contradictions, missing bindings and explicit readiness criteria. Completing a document revision is not completing the specification.

Before any implementation task graph is compiled, every required capability must have: requirement/source; current owner; precise inputs/outputs and state transitions; verified source implementation seam or explicit accepted new design; consumer binding; scope/authority/privacy; failure/recovery/replay/revoke; performance envelope; migration/compatibility; acceptance and evidence requirements. Unresolved consequential choices must be settled, explicitly excluded or covered by an accepted supported design—not delegated to coder improvisation.

Draft maturation is source review → reconciliation → detailed contracts/behavior → adversarial scenario review → operator revision → completeness review. These are specification activities, not executable implementation nodes. Future rollout may use one complete vertical slice and then expand through proven seams, but its task decomposition is prohibited until the full bounded specification passes review.

The [detailed blueprint](05-sovos-master-loop-integration-blueprint.md) is the design-level closure crosswalk: compiler linking and semantic identity; source commitments and watch ownership; optional asynchronous judgment; existing-human acceptance and competing effects; correction/pause/restart; independent receiver acceptance and reciprocal memory. Its requirement IDs are not work items. The register distinguishes paper-defined proposals, supported-source-only seams and still-unqualified operations rather than checking readiness from prose volume.

Paper readiness does not require every future algorithm or UI to exist. Required dependencies need exact supported interfaces or reviewed extension designs; optional research must be explicitly off-path. No implementation begins merely because a draft revision is published.

## 15. Change log and preservation record

- **0.3.0:** adds a detailed integration blueprint with proposed responsibility allocation, compiler/effect crosswalk, logical pre/postconditions, guarded lifecycles, asynchronous judgment validity, human/VA coordination, stable effect identity across retries/migration, correction/recovery and receiver/memory closure; integrates whole Workstreams, full Trajectory coverage and the relevant Focusa core primitives under #618; adds concrete synthetic trace and negative predicates; qualifies actual compiler/settlement code and remaining source concerns without changing it.
- **0.2.0:** deepens Tononi/Koch primary-source grounding; distinguishes integration from rich causal structure and intelligent improvement from blind Phi maximization; specifies reciprocal Master Loop–memory seams, correction/eligibility/delivery boundaries and receiving-memory-agent questions. Documentation publication is authorized; code, runtime, schemas and decomposition remain excluded.
- **0.1.0:** preserves the full session concept; restores alarms, mathematical intelligence, routines, existing humans, memory, owner channels, bodies, outcome/momentum and IIT alongside—not underneath—the decision models. Adds source/integration register and detailed alarm/simulation annex. All proposed contracts remain prose, no runtime changes.
- Revision 0.3.0 starts from published SOVOS `1bde0f4ecf6336c01f9df034890d1d1cba92e9a8`; the original draft baseline was `695738c42745720c563c2956fea586e49bc38fa4`. Source review date is 2026-10-11. Sibling working trees contain concurrent changes and were not edited.
- Not yet claimed: exhaustive repository/spec review; exact deployed bindings; measured model comparison; simulated run results; completed specification; implementation readiness; new active routine or worker.
