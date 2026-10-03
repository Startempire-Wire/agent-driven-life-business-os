# Routine Compiler Runtime Closure Plan

**Status:** CURRENT implementation plan; portable planning complete, runtime proof still required  
**Effective:** 2026-10-03  
**Depends on:** `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`, Stage 5 discovery, Portfolio Business Compiler, Focusa authority/Evidence, OpenClaw durable automations  
**Closes when proven:** `SAG-10` and `SAG-18` in `11-agent-os-golden-path-seamless-autonomy-gap-audit.md`

## 1. Purpose

SOVOS now has the portable object model and starter library needed to describe reusable routines. The remaining problem is not another layer of architecture. It is one executable path from an evidence-backed audit finding to a steady, revocable, measurable routine.

This plan defines that path and its acceptance tests.

The first proof uses the reusable **inquiry triage** family because the current operating record contains a concrete unresolved buyer/inquiry-response need and because the pattern can be rebound to more than one business shape without changing the portable template.

No customer message is authorized merely by this plan.

## 2. Closure target

The runtime slice must prove this exact causal chain:

~~~text
source-owned observation
→ operator.routine_candidate.v1
→ canonical operator.routine_template.v1 match
→ owner-specific operator.routine_blueprint.v1
→ owner/governance acceptance
→ Focusa Workstream + assignment + current grants
→ determinization
→ operator.routine_instance.v1
→ exact event/schedule binding
→ shadow run
→ bounded pilot effect
→ Evidence + receiver-side verification
→ source-domain accepted outcome
→ operator.leverage_snapshot.v1
→ Quiet Kaizen keep / improve / retire proposal
~~~

The slice is not complete if it stops at a prompt, draft, cron entry, agent run, internal receipt, or healthy process.

## 3. Canonical ownership

| Responsibility | Canonical owner |
|---|---|
| Portfolio/life interpretation, candidate inference, template match, blueprint preview, owner-facing synthesis | Wirebot / Portfolio Business Compiler |
| Workstream, assignment, authority, worker scope, Workpoints, Evidence, settlement | Focusa |
| Persistent Operating Partner runtime and default durable agent/system-event automation | OpenClaw |
| Browser/computer actuation when no stronger interface exists | UIAI Engine |
| Machine/body/runtime placement | Veragensia where applicable |
| Inbox/message truth | owning communication provider |
| CRM/customer record truth | owning CRM/customer system |
| Business/life accepted outcome | source domain plus owner acceptance where required |
| Private leverage synthesis and Quiet Kaizen | Wirebot / Perpetua |
| Optional progression/recognition/community projection | W.I.N.S. when enabled |

No implementation may create a second roster, schedule-authority store, Evidence ledger, CRM, or outcome authority to make this slice convenient.

## 4. First vertical slice: inquiry triage

### 4.1 Candidate

The compiler emits one `operator.routine_candidate.v1` from current source-backed evidence.

Minimum candidate content:

- exact owner/business/domain refs;
- evidence class: observed, owner-declared, historical, inferred gap, archetype suggestion, or existing automation;
- source refs rather than copied private message bodies;
- current burden and desired outcome;
- template matches with rationale;
- determinism potential;
- preferred trigger;
- human-reserved boundary;
- authority, source and reliability gaps;
- evidence and accepted-outcome requirement;
- next state.

A candidate created only from a pack/archetype must remain visibly labeled as a suggestion rather than observed recurrence.

### 4.2 Template match

Use the canonical:

`routine-template://business/inquiry-triage@1.0.0`

The template remains owner-neutral. It must not receive customer private payload, credentials, active grants, exact schedule state or canonical CRM state.

The compiler records a match classification and rationale. It may reject the match without modifying the template.

### 4.3 Blueprint

Compile an owner-specific `operator.routine_blueprint.v1` that binds:

- purpose and desired outcome;
- exact business/domain scope;
- message/inquiry source refs;
- customer/contact-system refs where available;
- event or reconciliation trigger;
- classification policy;
- verified offer/context source;
- response-preparation policy;
- human/external-commitment boundary;
- role/assignment intent;
- execution placement;
- authority and credential-use refs;
- idempotency, overlap, retry, missed-event and ambiguous-state rules;
- Evidence and receiver-side acceptance;
- baseline/measurement plan;
- pause, revoke and retire semantics.

The owner-facing preview should explain **why**, **when**, **who**, **how**, **Needs You when**, **proof**, and **expected measurement** without requiring the owner to read scheduler syntax.

### 4.4 Acceptance before compilation

Owner/governance acceptance authorizes the proposed semantics, not unlimited future work.

Before compilation, resolve:

- exact source identity;
- exact business/tenant;
- exact Focusa Workstream;
- exact assignment/Foreman;
- least-capability tool/data bundle;
- current grant refs;
- external-send posture;
- budget/expiry where applicable;
- human boundary;
- evidence and outcome policy.

Missing material bindings produce `blocked`, not guessed defaults.

## 5. Determinization

The implementation should reduce improvisation in this order:

~~~text
provider/API/CLI operation
→ deterministic transform / state machine
→ bounded semantic decision
→ UIAI only when no stronger interface exists
→ human-reserved decision
~~~

For inquiry triage, the target steady shape is D2 or better:

1. deterministic event ingestion and deduplication;
2. bounded semantic fit/urgency/next-action classification;
3. bounded response preparation from verified offer/context;
4. deterministic authority check for any external effect;
5. deterministic source/CRM receipt and next-action recording;
6. deterministic receiver/delivery verification where the provider exposes it.

Every semantic island needs typed inputs, versioned policy or prompt contract, output schema, allowed evidence, allowed capabilities, consequence class, validation and fail/escalate behavior.

## 6. Routine Instance compilation

After acceptance and determinization, emit one immutable/versioned `operator.routine_instance.v1`.

The instance must bind:

- exact blueprint revision;
- template lineage;
- owner/business/domain scope;
- trigger binding;
- Focusa assignment and Workstream;
- compiled deterministic/semantic/human steps;
- operation, policy and prompt-contract refs;
- current grant and credential-use refs;
- lock/lease and idempotency strategy;
- overlap behavior;
- timeout and retry/backoff;
- missed-event or missed-run behavior;
- ambiguous-completion reconciliation;
- failure-attention destination;
- rollback where applicable;
- pause/revoke;
- Evidence requirements;
- acceptance policy;
- compiler version and instance revision.

A later template or blueprint edit does not mutate the active instance. Material change creates a governed new revision.

## 7. Trigger and scheduler binding

Prefer the narrowest causal trigger:

~~~text
native inbound event / webhook
→ source queue
→ condition
→ schedule
→ manual
~~~

For inbound inquiry triage, an event/queue trigger is preferred when trustworthy. A periodic reconciliation job may coexist to detect missed events; it is a separate routine with its own purpose and receipts.

OpenClaw is the default durable automation owner when its semantics fit. Provider-native or product-native deterministic scheduling remains valid when stronger.

A scheduler binding launches the exact compiled instance revision. It never supplies authority by existing.

## 8. Run admission and lifecycle

Each run follows:

~~~text
DUE / EVENT
→ ADMISSION
→ DEDUPLICATE
→ ACQUIRE LEASE
→ RESOLVE INSTANCE REVISION
→ REVALIDATE CURRENT AUTHORITY + FRESHNESS
→ LOAD BOUNDED INPUTS
→ EXECUTE
→ VERIFY OUTPUT / DELIVERY
→ SETTLE RECEIPTS + EVIDENCE
→ RESOLVE ACCEPTED OUTCOME
→ CHECKPOINT
→ RELEASE LEASE
→ COMPLETE
~~~

Failure:

~~~text
classify
→ safe retry if allowed
→ reconcile ambiguous state
→ bounded recovery if allowed
→ Needs You / failure sink
→ terminal receipt
~~~

The design assumes replay, duplicate events, outages and partial completion can occur. It does not claim distributed exactly-once execution.

## 9. Promotion gates

### Shadow

- read/prepare only unless a test operation is explicitly authorized;
- compare classification and proposed next action with actual owner/worker decisions;
- measure false positive, false negative and duplicate behavior;
- verify tenant/source isolation;
- test no-effect failure.

### Pilot

One bounded real effect with:

- exact current grant;
- idempotency;
- duplicate-trigger test;
- provider timeout/retry test;
- stale-grant denial;
- ambiguous-delivery reconciliation;
- receiver-side proof;
- owner takeover/revoke test;
- failure routing.

### Proven

Require repeated accepted outcomes over a meaningful sample for the bound workflow, known failure posture and lower owner burden. Do not hard-code a universal run count: consequence, frequency and variability differ by routine.

### Active / steady

Only after the exact instance has:

- durable trigger;
- current assignment/grants;
- run history;
- observable exceptions;
- Evidence/outcome closure;
- pause/revoke;
- monitoring and analytics.

## 10. Mandatory negative-path acceptance matrix

The slice must demonstrate all applicable cases:

| Case | Required result |
|---|---|
| Duplicate provider event | one logical case; duplicate effect suppressed or reconciled |
| Same inquiry already in CRM | reconcile; do not create duplicate customer/work state |
| Stale/revoked grant | deny consequential step before effect |
| Wrong tenant/business binding | deny and emit scoped failure evidence |
| Unsupported contract revision | fail closed for consequential execution |
| Provider timeout before known completion | reconcile source state before retry |
| Delivery accepted but local receipt missing | recover by source reconciliation; do not blindly resend |
| Local receipt exists but receiver state disagrees | surface contradiction; do not claim accepted outcome |
| Scheduler/runtime outage | missed-event policy executes without duplicate external effect |
| Overlapping run | lock/lease/overlap policy is observable and deterministic |
| Semantic result fails schema/policy | reject before consequential deterministic step |
| Owner takeover | agent stops; resumption requires reconciliation |
| Pause/revoke during pending work | no later stale continuation |
| UIAI fallback unavailable | fail/escalate; do not silently broaden tools |
| Evidence incomplete | work cannot be represented as closed |
| Outcome unknown | analytics remains unknown rather than inferred from activity |

## 11. Generalization proof

After Binding A passes, apply the **same canonical inquiry-triage template** to Binding B with materially different owner-specific bindings.

Recommended abstract proof:

- **Binding A:** professional-service inquiry source + service CRM/contact history;
- **Binding B:** software/SaaS commercial inquiry source + product entitlement/customer system.

The template ID and portable semantics remain unchanged. The following are expected to differ:

- source refs;
- business scope;
- offer/context refs;
- classification policy;
- role/assignment;
- grants;
- credential-use refs;
- provider operations;
- acceptance policy;
- outcome metric.

Generalization passes only if neither binding leaks private payload or authority into the shared template and one binding cannot read or mutate the other's state.

## 12. Routine analytics and leverage closure

Measure the routine without hiding dimensions behind one score:

- events/runs admitted, coalesced, skipped, failed and recovered;
- duplicate suppression;
- classification/decision corrections;
- retries, timeouts and ambiguous-state reconciliations;
- stale-authority denials;
- human interventions and human-reserved decisions;
- response/handling latency;
- evidence completeness;
- receiver-side acceptance;
- direct operating cost where known;
- owner time/attention bought back;
- actual business/life outcome refs.

Wirebot/Perpetua then produces a source-qualified `operator.leverage_snapshot.v1`.

Quiet Kaizen uses the evidence order:

~~~text
Question
→ Delete
→ Simplify
→ Accelerate
→ Automate
~~~

and proposes keep / improve / retire. Optimization never self-authorizes protected policy, authority, architecture or purpose changes.

W.I.N.S. may project progression when enabled but is not required for this closure loop.

## 13. Implementation order

1. **Compiler preview:** audit candidate → template match → blueprint, with private payload held behind refs.
2. **Focusa binding:** exact Workstream/assignment/current-grant resolution; deny missing or mismatched scope.
3. **Instance compiler:** accepted blueprint revision → validated `operator.routine_instance.v1`.
4. **Trigger adapter:** bind the exact instance to one event/queue/scheduler owner and persist only the owner's canonical job ref.
5. **Runner admission:** instance resolution, grant freshness, lease, dedupe and bounded inputs.
6. **Step execution:** deterministic operations around bounded semantic islands.
7. **Closure adapter:** Evidence, settlement, receiver/source verification and accepted-outcome ref.
8. **Negative-path harness:** exercise the matrix above.
9. **Promotion:** shadow → bounded pilot → proven → active.
10. **Generalization:** bind the same template to the second business shape.
11. **Leverage loop:** emit base private leverage snapshot and Quiet Kaizen recommendation.
12. **Optional projection:** verify W.I.N.S.-off and, separately, W.I.N.S.-on behavior.

Do not build horizontal infrastructure beyond what this slice exercises.

## 14. Exit criteria

`SAG-10` and `SAG-18` are not closed by documentation or schemas. They close only when a replacement authorized agent can inspect stable refs and demonstrate:

- source-backed candidate and template rationale;
- accepted owner-specific blueprint;
- exact Focusa assignment/current authority;
- immutable compiled instance;
- durable causal trigger;
- safe duplicate/retry/missed-run behavior;
- deny/revoke/takeover paths;
- receiver-side Evidence and accepted outcome;
- truthful failure/unknown state;
- measured attention/outcome effect;
- same template proven across two isolated bindings;
- no duplicate authority, work, schedule, Evidence or outcome store.

## 15. What is complete versus open

**Portable planning/library complete:**

- routine candidate, pack, template, blueprint, instance and leverage contracts;
- starter core-family template coverage;
- composable life/business pack coverage;
- determinization doctrine;
- promotion/reliability/measurement rules;
- this executable acceptance plan.

**Still open until runtime evidence exists:**

- Wirebot compiler implementation;
- Focusa exact assignment/grant binding for the slice;
- exact OpenClaw/provider trigger adapter;
- end-to-end run/recovery/revocation proof;
- two-binding generalization proof;
- measured leverage/Quiet Kaizen proof.

That boundary prevents architecture documentation from being mistaken for operational completion.
