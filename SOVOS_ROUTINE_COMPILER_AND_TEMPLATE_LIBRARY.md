# SOVOS Routine Compiler and Template Library Doctrine

**Status:** CURRENT portable doctrine; contract surfaces defined, runtime compiler implementation remains partial  
**Effective:** 2026-10-03  
**Architecture authority:** `OWNER_AUTHORITY_CONSTITUTION.md`  
**Human freedom doctrine:** `SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md`  
**Driverless Business doctrine:** `SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md`  
**Information infrastructure:** `SOVOS_INFORMATION_INFRASTRUCTURE.md`  
**Discovery procedure:** `docs/agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md`  
**Portfolio compiler:** `docs/agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md`
**Runtime closure plan:** `docs/agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md`

## 1. Why this layer exists

SOVOS already has a strong discovery audit and a portable routine blueprint. Real operator audits, however, show a repeated gap:

~~~text
audit discovers recurring work
→ a good prose routine is suggested
→ a schedule may be proposed
→ implementation quality varies
~~~

That is not enough for a Driverless Business.

A routine must be reusable **without becoming generic**, personalized **without becoming improvised**, and autonomous **without becoming unstable**.

The missing layer is a compiler:

~~~text
evidence-backed audit
→ routine candidate
→ reusable template match
→ owner-specific blueprint
→ determinization pass
→ compiled routine instance
→ shadow / pilot
→ durable trigger binding
→ steady execution
→ Evidence / accepted outcome
→ Quiet Kaizen
~~~

A calendar event or cron entry is not a routine. A prompt that runs every morning is not automatically a stable routine. A role profile is not a routine. A template is not authority.

---

## 2. The routine object model

SOVOS distinguishes five objects.

### 2.1 Routine Template

A **Routine Template** is an owner-neutral reusable pattern.

It describes:

- what class of problem the routine addresses;
- signals that make the template relevant;
- signals that make it inappropriate;
- preferred trigger type;
- generic step skeleton;
- which steps should be deterministic;
- where bounded semantic judgment may be useful;
- human-reserved boundaries;
- default reliability behavior;
- evidence and outcome classes;
- parameters that must be bound before use.

A template contains no customer's private payload, credentials, active grant, exact schedule or canonical task state.

Portable contract:

`operator.routine_template.v1`

### 2.2 Routine Candidate

A **Routine Candidate** is an audit inference.

Portable contract:

`operator.routine_candidate.v1`

It must be machine-valid before owner-specific blueprint compilation.

It says:

> this observed or owner-declared pattern may benefit from a routine, and these templates appear relevant.

A candidate carries source evidence, current burden, recurrence, closure gap, consequence posture and template-fit reasoning.

It is not yet a schedule, authority grant or active worker.

### 2.3 Routine Blueprint

A **Routine Blueprint** is the owner-specific proposed routine already represented by:

`operator.routine_blueprint.v1`

It binds real:

- owner / business / life-domain scope;
- purpose;
- source evidence;
- trigger;
- steps;
- supervision;
- authority requirements;
- execution placement;
- reliability policy;
- measurement;
- revoke / retire semantics.

A blueprint may derive from a template, several templates, or a novel audit finding.

### 2.4 Routine Instance

A **Routine Instance** is the compiled executable binding of one accepted blueprint revision.

It freezes enough information for reproducible operation:

- exact blueprint revision;
- template lineage if any;
- exact owner/domain scope;
- exact trigger binding;
- exact Focusa assignment;
- exact operation / decision-policy / prompt-contract refs;
- authority and credential-use refs;
- concurrency / lock behavior;
- idempotency strategy;
- timeout / retry / missed-run behavior;
- evidence and acceptance requirements;
- compiler version and instance revision.

Portable contract:

`operator.routine_instance.v1`

A later template update MUST NOT silently mutate an active instance.

### 2.5 Routine Run

A **Routine Run** is one execution occurrence owned by the applicable scheduler / work / execution systems.

SOVOS does not create another run database.

A run is correlated through references and receipts to:

- routine instance;
- assignment;
- worker/session;
- tool/API/UIAI execution;
- Evidence;
- settlement;
- accepted outcome.

---

## 3. Evidence inputs from the current operating record

Recent operator material demonstrates why this distinction is necessary.

The October 2 routine inventory contained patterns including:

- buyer / inquiry triage;
- morning business and calendar orientation;
- prospecting and overdue follow-up;
- customer-case and pipeline/cash reconciliation;
- evening and weekly orientation;
- infrastructure exception triage;
- unanswered-message watchdog;
- nightly learning and workforce assignment.

Those are not unique to one company. They are instances of recurring routine families.

The September foundational systems material likewise described reusable cadences for:

- governance / frontier review;
- system exceptions;
- opportunity / offer review;
- content distribution;
- pipeline;
- delivery;
- Evidence / quality;
- resilience / economics.

The longitudinal audit found the deeper failure mode:

> **Cadence is designed more often than it is instrumented.**

It also identified a reusable cross-business control pattern:

~~~text
discover
→ classify
→ qualify
→ prepare
→ obtain required authority
→ execute
→ verify
→ follow up / close
→ record outcome and reusable procedure
~~~

SOVOS therefore generalizes the **pattern**, not the owner's private data.

---

## 4. Audit → inference → template matching

The audit should not jump directly from a discovered workflow to a scheduled prompt.

For every routine candidate, derive:

### 4.1 Evidence class

Mark the candidate as one or more of:

- `observed_recurring` — recurrence exists in current source evidence;
- `owner_declared` — the owner says the routine should exist;
- `historical_recurring` — history shows a former cadence that may need renewal;
- `archetype_expected` — a template is commonly useful for this operating shape but current evidence is incomplete;
- `gap_inferred` — evidence shows a missing control / closure step;
- `existing_automation` — a job already exists and must be reconciled rather than duplicated.

The system MUST tell the owner why a suggestion exists.

### 4.2 Routine-fit dimensions

Do not collapse fit into one magic score.

Record dimensions independently:

- recurrence strength;
- owner burden / attention cost;
- desired-outcome importance;
- closure gap;
- determinism potential;
- source / integration readiness;
- consequence risk;
- privacy sensitivity;
- cross-domain reuse;
- template fit;
- evidence confidence.

A routine can be high-value but not yet ready to automate.

### 4.3 Template match

Match candidate signals against template:

~~~text
required signals
+ optional signals
- exclusion / contraindication signals
+ evidence floor
+ archetype / domain relevance
~~~

Return:

- `strong_match`;
- `partial_match`;
- `novel_pattern`;
- `template_suggestion_only`;
- `not_applicable`.

No template activates itself.

### 4.4 Template suggestions without observed recurrence

SOVOS MAY suggest a routine from a life/business archetype even when the audit has not yet observed it.

It must label the reason clearly:

> **Suggested from archetype; not evidenced as a current recurring burden.**

This makes the library useful without turning assumptions into facts.

---

## 4.5 Routine Packs

SOVOS also defines `operator.routine_pack.v1`: a composable bundle of template suggestions for a life domain or business operating shape.

Starter packs live under `routine-packs/`.

A pack asks: **Given this operating shape, which routine families are worth checking for fit?** It does not decide which routines a person or business must run.

Every pack suggestion still becomes an explicit Routine Candidate with evidence class and fit reasoning before blueprint compilation.

---

## 5. Archetypes are composition aids, not identities

Avoid rigidly classifying a person as one "type of life."

Instead, compose **domain packs**.

One owner may simultaneously have:

~~~text
founder/operator
+ household administrator
+ creator
+ researcher
+ caregiver
+ traveler
+ investor
~~~

Likewise a business may combine:

~~~text
professional service
+ software/SaaS
+ membership/community
+ content/media
~~~

Templates are selected from the evidence and owner goals, not from a demographic stereotype.

---

## 6. Core routine families

The template library should begin with reusable families that recur across many life and business domains.

| Family | Generic job |
|---|---|
| Orientation | Convert current commitments, changes, risks and opportunities into a bounded briefing / next-action view |
| Intake & triage | Detect new requests/events, deduplicate, classify, route and establish next action |
| Follow-up | Detect unresolved commitments and perform or prepare the next authorized action |
| Reconciliation | Compare multiple sources, find disagreement, settle through canonical owners |
| Delivery / case review | Review open work/cases, blockers, acceptance and next handoff |
| Renewal / expiry | Track time-bound obligations, subscriptions, contracts, credentials, maintenance and renewals |
| Finance operations | Reconcile invoice/payment/settlement/cost states without treating notification as ledger truth |
| Content / distribution | Convert accepted evidence/ideas into approved publication/distribution loop |
| System health | Exception-oriented service/security/backup/capacity review |
| Incident response | Detect impact, diagnose, execute bounded recovery, verify consumer recovery |
| Knowledge freshness | Detect stale procedures, superseded facts, unresolved contradictions and source drift |
| Evidence / closure | Prove that a completed action produced the intended receiver-side result |
| Learning / Kaizen | Extract repeated friction/corrections, propose smallest improvement, validate, promote or reject |
| Workforce dispatch | Match accepted ready work to bounded roles/capabilities without creating ambient authority |
| Planning | Reconcile outcomes, commitments, capacity and constraints into the next operating frontier |

These families are intentionally more durable than any particular app.

---

## 7. Suggested life-domain packs

### 7.1 Personal executive / administrative pack

Candidate templates:

- morning orientation;
- communication intake / triage;
- commitment follow-up;
- calendar conflict / preparation;
- weekly personal review;
- renewals / expiring obligations;
- document / record freshness.

### 7.2 Household / family operations pack

Candidate templates:

- shared calendar / logistics reconciliation;
- bills / renewals exception review;
- household maintenance;
- document / warranty / subscription tracking;
- travel / appointment preparation.

Personal/family data remains private and purpose-limited.

### 7.3 Learning / research pack

Candidate templates:

- capture / intake;
- reading / research queue;
- source verification;
- weekly synthesis;
- experiment / question follow-up;
- knowledge freshness / supersession.

### 7.4 Creator / author / media pack

Candidate templates:

- idea intake;
- research / source pack;
- drafting cadence;
- production checklist;
- publication gate;
- distribution;
- response / audience learning.

### 7.5 Personal finance oversight pack

Candidate templates:

- transaction / invoice reconciliation;
- subscription / renewal review;
- recurring-obligation exception review;
- document preparation;
- cash-flow orientation.

Default posture is informational / preparatory. Money movement requires the exact applicable authority.

### 7.6 Wellness / care coordination pack

Candidate templates may support:

- appointment preparation;
- record gathering;
- schedule / adherence reminders;
- questions for a professional;
- logistics.

Diagnosis, treatment changes and other high-stakes medical decisions remain human/professional-reserved under their owning systems.

---

## 8. Suggested business-archetype packs

### 8.1 Professional service / agency / consulting

- inquiry triage;
- prospect follow-up;
- proposal / scope preparation;
- onboarding;
- delivery / open-case review;
- client status / acceptance;
- invoice / payment reconciliation;
- renewal / expansion review;
- case-study / proof extraction.

### 8.2 Software / SaaS

- inquiry / trial triage;
- entitlement / provisioning reconciliation;
- onboarding;
- support / incident triage;
- release readiness;
- deployment / consumer verification;
- usage / outcome review;
- renewal / churn-risk review;
- security / backup / dependency exceptions.

### 8.3 Membership / community / education

- new-member intake;
- benefit / entitlement delivery;
- event / class production;
- attendance / follow-up;
- newsletter / content cadence;
- support;
- renewal;
- community opportunity routing;
- outcome / participation evidence.

### 8.4 E-commerce / product commerce

- order exception triage;
- inventory / fulfillment exception;
- customer inquiry;
- return/refund preparation;
- supplier / replenishment review;
- payment reconciliation;
- product-content freshness;
- retention / repeat-customer follow-up.

### 8.5 Content / media

- source / idea intake;
- editorial planning;
- production;
- QA / fact check;
- publication;
- distribution;
- audience response;
- repurposing;
- archive / freshness review.

### 8.6 Local / field service

- lead intake;
- qualification;
- scheduling / dispatch;
- pre-visit preparation;
- service completion / evidence;
- customer follow-up;
- invoice / payment reconciliation;
- recurring maintenance / renewal.

### 8.7 Multi-business portfolio

- portfolio morning orientation;
- cross-business Needs You;
- shared finance / obligations reconciliation;
- shared systems health;
- shared opportunity scan;
- weekly portfolio outcome review;
- dormant-asset review;
- workforce / capacity allocation;
- Quiet Kaizen / leverage review.

---

## 9. Determinization pass

A routine becomes stable by reducing improvisation where reality is already understood.

For every step ask, in this order:

1. Can this be a deterministic product operation / API / CLI / query?
2. Can it be a deterministic transform / rule / state machine?
3. Does it require bounded semantic judgment?
4. Does it require UIAI because no structured interface exists?
5. Is it genuinely human-reserved?

### Determinism classes

**D3 — Deterministic**

Every material execution step is typed / deterministic. A model may summarize but is not required for correctness.

**D2 — Deterministic shell with bounded semantic islands**

The routine has deterministic triggers, inputs, state transitions, retries, receipts and acceptance. Agentic steps consume typed inputs and must emit schema-valid outputs under versioned policy/prompt contracts.

**D1 — Agent-led**

Major parts still depend on open-ended reasoning or broad tool selection. Suitable for shadow/pilot or low-consequence work, not preferred steady-state unattended operation.

**D0 — Human/manual**

Useful as discovered process or procedure, not yet automated.

A routine promoted to steady unattended operation should normally reach **D2 or D3**.

---

## 10. Bounded semantic steps

An agentic step inside a stable routine should have:

- exact input refs / schema;
- narrow purpose;
- allowed evidence sources;
- output schema;
- decision policy ref;
- prompt / skill / instruction revision where material;
- allowed tools / capability bundle;
- consequence class;
- confidence / uncertainty output where meaningful;
- deterministic validation after the model;
- fail / escalate behavior.

A semantic step MUST NOT be a hidden replacement for an operation that should have been code.

---

## 11. Routine Instance compilation

Acceptance of a blueprint does not directly create a cron job.

The compiler produces an immutable/versioned **Routine Instance**.

Compilation binds:

~~~text
template lineage
+ exact blueprint revision
+ exact owner/business/life scope
+ exact Focusa assignment / Workstream
+ exact operation refs
+ exact agent decision / prompt contracts
+ exact credential-use refs
+ exact human boundary policy
+ exact trigger binding
+ exact reliability policy
+ exact Evidence / acceptance policy
+ compiler version
= routine instance revision
~~~

Any material change produces a new instance revision or governed update. Do not silently mutate a running routine because a template/library file changed.

---

## 12. Trigger selection

Prefer the narrowest causal trigger.

Order of preference when semantics allow:

~~~text
native event / webhook
→ source queue
→ condition watch
→ schedule
→ manual
~~~

Do not poll every five minutes when a trustworthy event exists.

However, a periodic **reconciliation routine** may intentionally coexist with events to detect:

- missed events;
- stale source state;
- delivery gaps;
- failed downstream projections.

The reconciliation routine is a separate job with its own purpose and evidence.

---

## 13. Stable schedule binding

For a scheduled routine, compile at least:

- scheduler class / owner;
- schedule ref;
- timezone;
- DST semantics;
- quiet hours where relevant;
- jitter / exact-time requirement where relevant;
- lock / lease;
- overlap behavior;
- missed-run behavior;
- timeout;
- retry / backoff;
- idempotency key strategy;
- ambiguity reconciliation;
- failure destination;
- pause / revoke;
- current authority revalidation.

OpenClaw remains the default durable scheduler for agent/system-event work when appropriate.

A product/provider/native scheduler remains preferable for a deterministic workload when it is the stronger owner.

---

## 14. Run state machine

A steady routine should have an observable run lifecycle.

Recommended conceptual state machine:

~~~text
DUE / EVENT
→ ADMISSION
→ ACQUIRE LEASE
→ RESOLVE INSTANCE REVISION
→ AUTHORITY + FRESHNESS PREFLIGHT
→ LOAD BOUNDED INPUTS
→ EXECUTE
→ VERIFY OUTPUT
→ SETTLE / RECORD RECEIPTS
→ RESOLVE ACCEPTED OUTCOME
→ CHECKPOINT
→ RELEASE LEASE
→ COMPLETE
~~~

Failure path:

~~~text
failure
→ classify
→ safe retry if permitted
→ reconcile ambiguous state
→ bounded recovery if permitted
→ Needs You / failure sink
→ terminal receipt
~~~

Do not promise magical distributed "exactly once" execution.

Prefer idempotent operations, leases, source reconciliation and replay-safe semantics.

---

## 15. Shadow and promotion gates

Before a routine becomes steady state:

### Shadow

- read / prepare only where possible;
- compare proposed decisions with real owner/worker decisions;
- measure false positives / missed cases;
- test source isolation;
- test no-effect failure.

### Pilot

- one bounded real effect;
- exact authority;
- receiver-side proof;
- duplicate trigger test;
- retry / outage test;
- missed-run test;
- stale-authority denial;
- takeover / revoke test.

### Proven

- repeated accepted outcomes;
- known failure posture;
- owner burden lower than baseline;
- no hidden manual reconciliation requirement.

### Active / steady

- compiled instance;
- durable trigger;
- run history;
- exception routing;
- evidence / outcome closure;
- monitoring.

A template's popularity is never promotion evidence.

---

## 16. Routine analytics should expose stability

In addition to business/life outcome metrics, measure:

- admitted / skipped / coalesced runs;
- duplicate-trigger suppression;
- retries;
- ambiguous-state reconciliations;
- timeouts;
- missed runs;
- recovery success;
- stale-authority denials;
- owner interventions;
- human-reserved escalations;
- deterministic vs semantic step ratio;
- model/tool variance where meaningful;
- UIAI fallback rate;
- evidence completeness;
- receiver-side acceptance;
- owner time / attention bought back;
- owner-defined capacity returned for higher-purpose work where the owner chooses to measure it.

The routine is an instrument, not the goal. In the flight metaphor, **do not confuse the wing with the flight**: a routine that becomes elaborate, attention-hungry or dependency-producing can reduce leverage even while its execution reliability improves.

SOVOS may measure returned capacity; it MUST NOT define, score or invent the owner's higher purpose.

This lets Quiet Kaizen target instability and unnecessary machinery rather than merely increasing automation.

---

## 17. Template-library governance

Templates should evolve from evidence.

A template may be created or strengthened when:

- the same pattern recurs across independent owners/domains;
- a real implementation repeatedly closes the loop;
- failure/recovery behavior is known;
- the abstraction does not erase important domain differences.

Template changes do not mutate active customer instances.

Template lifecycle:

~~~text
candidate
→ recommended
→ stable
→ deprecated
~~~

Keep lineage and migration guidance.

Do not put customer private payload or secrets into the portable template library.

---

## 18. Audit deliverable change

A SOVOS audit should now produce a **Routine Inference Matrix** with at least:

| Field | Meaning |
|---|---|
| Candidate | Owner-specific recurring pattern / missing control |
| Evidence basis | observed / owner-declared / historical / archetype suggestion / existing automation |
| Routine family | reusable family |
| Template match | strong / partial / novel / suggestion-only / not-applicable |
| Current burden | owner attention / delay / risk / repeated work |
| Current implementation | none / manual / partial job / existing automation |
| Determinism class | D0 / D1 / D2 / D3 |
| Preferred trigger | event / queue / condition / schedule / manual |
| Human boundary | what truly needs the owner |
| Required sources | canonical owner refs |
| Authority gap | grants / credentials / budgets still needed |
| Reliability gap | idempotency / overlap / missed-run / retry / failure route |
| Evidence / outcome | what proves the loop closed |
| Next state | reject / blueprint / shadow / pilot / compile / activate |

This matrix bridges discovery and executable implementation.

---

## 19. First generalized proof

The first proof should take one routine already observed in the current operator environment—such as inquiry triage or morning orientation—and demonstrate:

~~~text
private audit evidence
→ generic template match
→ owner-specific blueprint
→ determinization
→ compiled instance
→ shadow
→ pilot
→ duplicate/retry/missed-run tests
→ durable activation
→ Evidence
→ accepted outcome
→ measured attention buyback
~~~

Then apply the **same template** to a second business or life domain with different source bindings.

That proves generalization instead of merely automating one owner's prose.

---

## 20. Non-goals

Do not create:

- a universal list of routines every human "should" run;
- demographic stereotypes disguised as personalization;
- one prompt per routine with no typed operations;
- a cron-per-idea automation sprawl;
- template activation without evidence/owner fit;
- silent authority from learned preferences;
- one global routine database that replaces source owners;
- an "AI employee" for every template;
- schedule success as a substitute for receiver-side outcome;
- autonomous template updates that mutate active instances.

---

## 21. Compact doctrine

> **SOVOS converts observed life and business patterns into reliable autonomy through a staged compiler: reusable template, evidence-backed candidate, owner-specific blueprint, deterministic compiled instance, proven execution and accepted outcome. Templates provide leverage; compilation provides personalization; deterministic shells provide stability; delegated authority provides autonomy; Evidence proves the routine actually closed the loop.**


## 22. Canonical template and pack locations

Use exactly these portable-library roots:

~~~text
routine-templates/
  canonical Routine Template catalog

routine-packs/
  canonical Routine Pack catalog

templates/routines/
  superseded compatibility/incubation path only
~~~

Compiler implementations MUST NOT union both template directories blindly. Duplicate IDs across lineage paths are one conceptual template lineage, not separate routine suggestions.
