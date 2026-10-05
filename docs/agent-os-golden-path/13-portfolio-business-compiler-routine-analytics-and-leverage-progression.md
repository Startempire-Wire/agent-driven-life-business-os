# Portfolio Business Compiler, Routine Analytics, Leverage and Momentum

**Status:** CURRENT owner-directed architecture under the 0.2.5 correction; implementation remains partial<br>
**Version stream:** ADLBOS Golden Path 0.2.5-candidate<br>
**Freedom & leverage model:** `../../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`<br>
**Primary experience owner:** Wirebot / Wirebot App<br>
**Governed work owner:** Focusa<br>
**Persistent Operating Partner runtime / scheduler:** OpenClaw<br>
**Computer/browser execution owner:** UIAI Engine<br>
**Base feedback/leverage synthesis owner:** Wirebot / Perpetua over source-owned outcomes  
**Optional progression/recognition owner:** W.I.N.S. when enabled for the setup  
**Persistent transport/body baseline:** Tailscale + at least one remote VPS

## 1. Purpose

ADLBOS exists to advance the owner's life and businesses.

The end state is not "many agents" or "many automations." It is a living operating system that:

1. understands an owner's portfolio of businesses, products and life domains;
2. discovers how work actually happens;
3. turns recurring patterns into reviewable routines;
4. decides which parts should become deterministic software, agentic work, UIAI computer work or human-reserved decisions;
5. composes the required workforce and authority;
6. runs repeatably through the persistent OpenClaw/Focusa/UIAI substrate;
7. measures real outcomes and operating burden;
8. continuously finds the next compounding leverage move.

The leverage target is not automation volume. The system should reduce operational gravity and return usable human capacity while preserving purpose and authority upstream. In the Philoveracity flight metaphor:

> **Do not confuse the wing with the flight.**

A routine, worker or automation is valuable because of the outcome and capacity it returns, not because autonomous machinery exists.

Several businesses are normal. Shared services and routines may serve several businesses without merging their canonical records or authority.

### 1A. Freedom Flywheel and three frontiers

The compiler SHOULD synthesize three distinct owner frontiers:

~~~text
Capacity Frontier
  what removes operational gravity?

Economic Frontier
  where can high-quality income, cash realization, margin preservation
  or financial breathing room most credibly improve?

Life Enrichment Frontier
  given the owner's desired life and current released capacity,
  what relationship / experience / rest / learning / creative / purpose
  opportunity is worth considering?
~~~

The system MUST NOT collapse these into one numeric score or automatically route every released hour back into work.

For business scopes, the economic loop extends beyond inbound inquiry handling:

~~~text
opportunity → prospect / relationship → CRM → conversation → pipeline
→ offer / proposal → accepted commitment → invoice / checkout
→ settled cash → customer value → retention / expansion → referral
~~~

For personal financial-recovery scopes, the loop may include liabilities discovery, lawful status/rights classification, stability-floor/reserve modeling, validation/dispute/negotiation, settlement/closure, credit rehabilitation and recovered monthly cash flow.

For life scopes, released capacity may become a Capacity Reinvestment candidate such as relationship stewardship, a social/experience opportunity, rest/open-space protection, learning, creation or another owner-defined desired state.

## 2. The causal loop

```text
AUTHORIZED SOURCES / OWNER TRUTH
            ↓
PORTFOLIO + LIFE/BUSINESS MAP
            ↓
PATTERN / ROUTINE INFERENCE
            ↓
ROUTINE CANDIDATES
            ↓
REUSABLE TEMPLATE MATCHING
            ↓
OWNER-SPECIFIC ROUTINE BLUEPRINTS
            ↓
OWNER COMPOSITION / CORRECTION
            ↓
DETERMINIZATION PASS
            ↓
ROUTINE INSTANCE COMPILATION
            ↓
SYSTEM + WORKFORCE BINDING
            ↓
FOCUSA ASSIGNMENT + AUTHORITY
            ↓
EXECUTION PLACEMENT
  ├─ OpenClaw script/agent turn on remote VPS
  ├─ deterministic API/CLI/program
  ├─ Pi/worker under Focusa
  ├─ UIAI browser/computer work
  └─ human Needs You
            ↓
PILOT / SHADOW / ACCEPTANCE
            ↓
ACTIVE ROUTINE
            ↓
EVIDENCE + SOURCE-DOMAIN BUSINESS/LIFE RESULT
            ↓
BASE OPERATOR.LEVERAGE_SNAPSHOT
            ↓
QUIET KAIZEN
            ↓
OPTIONAL W.I.N.S. PROGRESSION WHEN ENABLED
            ↓
DELETE / SIMPLIFY / IMPROVE / REUSE / COMPOUND
```

No new central runtime or database is introduced by this loop.

## 3. Wirebot setup modes and W.I.N.S. participation

The compiler and optimization loop must work across all four customer/setup modes:

```text
Wirebot Sovereign Operator
Wirebot Sovereign
Wirebot Direct
Wirebot Network
```

The base compiler/feedback loop is mandatory/common capability. W.I.N.S. is not.

| Setup | Private feedback / optimization | W.I.N.S. posture |
|---|---|---|
| Wirebot Sovereign Operator | full | optional, explicit opt-in |
| Wirebot Sovereign | full | optional, explicit opt-in |
| Wirebot Direct | full | Direct-offer participation; never infer Network membership/federation |
| Wirebot Network | full | native to Network relationship under its owning policy |

For the top two setups, `W.I.N.S.=off` is a first-class complete operating state. Routine analytics, leverage snapshots, momentum inference and Quiet Kaizen continue privately.

The six technical entitlement levels may still exist underneath implementation, but they are not the customer setup taxonomy and do not determine W.I.N.S. by numeric ordering.

## 4. Portfolio model

The compiler works over an owner portfolio:

```text
Owner
├─ life domains
├─ Business A
│  ├─ products/services
│  └─ routines
├─ Business B
│  ├─ products/services
│  └─ routines
├─ Business C
└─ shared functions
   ├─ finance
   ├─ administration
   ├─ legal/compliance
   ├─ research
   └─ infrastructure
```

A routine scope may be one business, one product/service, a life domain, a shared service across several businesses, or the owner portfolio.

Cross-business routines must retain per-business data/authority boundaries and explicit attribution. "Primary business" is a UI convenience only.

## 5. Mandatory operating substrate

The current architecture assumes:

```text
OpenClaw
  durable Operating Partner runtime + Automations scheduler

Focusa
  Workstream / Foreman / assignment / authority / Evidence

UIAI Engine
  browser/computer hands and execution proof

Tailscale
  private execution mesh

persistent remote VPS
  always-on scheduling/execution body
```

Specific runtime incarnations and hosts are replaceable.

The remote VPS is where unattended recurring work normally lives. The user's Chromebook/laptop remains an interactive body and may execute work, but routine continuity does not depend on it being awake.

## 5A. Routine object model

Keep these distinct:

~~~text
Routine Template
  reusable owner-neutral pattern

Routine Candidate
  evidence-backed audit inference + template matches

Routine Blueprint
  owner-specific proposed routine

Routine Instance
  compiled executable binding of an accepted blueprint revision

Routine Run
  one execution occurrence in the owning scheduler/work/execution systems
~~~

Portable contracts:

~~~text
operator.routine_template.v1
operator.routine_blueprint.v1
operator.routine_instance.v1
~~~

A template never grants authority. A blueprint does not become a schedule merely by being accepted. A schedule launches an exact compiled instance; it does not launch a free-form interpretation of the latest template.

See `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`.

## 5B. Template library and archetype composition

The template library is a set of reusable patterns, not a universal checklist for every person or business.

Use composable domain packs such as:

~~~text
life
  personal administration
  household / family operations
  learning / research
  creator / media
  finance oversight
  wellness / care coordination

business
  professional services
  software / SaaS
  membership / community / education
  ecommerce
  content / media
  local / field service
  multi-business portfolio
~~~

The audit may recommend a template from archetype evidence even when recurrence is not yet observed, but must label it as a suggestion rather than a discovered burden.

Core families include orientation, intake/triage, follow-up, reconciliation, delivery review, renewal/expiry, finance operations, content/distribution, system health, incident response, knowledge freshness, Evidence/closure, learning/Kaizen, workforce dispatch and planning.

## 6. Routine blueprint

`operator.routine_blueprint.v1` is the portable compilation envelope.

A useful blueprint answers:

```text
WHY
  desired outcome / deficiency / leverage hypothesis

WHERE
  portfolio/business/life-domain scope

WHEN
  event / condition / cadence / manual trigger

WHO
  Operating Partner / Foreman / role / human-reserved actor

HOW
  ordered steps and each step class

WITH WHAT
  product operations / tools / data / credentials / budget

WHERE IT RUNS
  persistent VPS / Agent Computer / owner device / UIAI context

WHAT CAN GO WRONG
  timeout / overlap / retry / missed run / recovery / revoke

HOW WE KNOW
  Evidence / receipts / accepted outcome / measurement baseline
```

The blueprint references source-owned objects. It is not the task graph, schedule, grant, credential store or Evidence ledger.

## 7. Step classes

Every material routine step is classified before automation.

**Deterministic:** stable code/API/CLI/query/transformation. Do not repeatedly spend model reasoning on stable mechanical work.

**Agentic:** interpretation, synthesis, prioritization, research, drafting or ambiguity handling under a bounded Focusa assignment.

**UIAI:** browser/computer interaction when no stronger supported interface is available.

**Human-reserved:** owner truth, relationship judgment, reserved authority, consequential approval or another step where human comparative advantage is real.

Human-reserved steps become source-bearing Needs You items rather than hidden workflow stalls.

## 7A. Determinization and compiled instances

Stable autonomy should minimize repeated improvisation.

For every step:

~~~text
canonical deterministic operation if possible
→ deterministic transform / rule / state machine
→ bounded semantic step when judgment is genuinely required
→ UIAI only when no stronger interface exists
→ human-reserved when the human boundary is real
~~~

Use the maturity of the execution shape:

~~~text
D3 deterministic
D2 deterministic shell + bounded semantic islands
D1 agent-led
D0 human/manual
~~~

Steady unattended routines should normally reach D2 or D3.

An agentic step in a D2 routine should have typed inputs, narrow purpose, evidence scope, versioned decision/prompt contract, output schema, capability bundle, consequence class, deterministic validation and fail/escalate behavior.

After acceptance, compile `operator.routine_instance.v1`. The instance binds the exact blueprint revision, template lineage, trigger, Focusa assignment, operations/policies, authority, reliability, Evidence and acceptance requirements. Material changes create a new instance revision or governed update.

## 8. Scheduling and remote execution

OpenClaw's built-in Gateway automations scheduler is the default durable scheduler for owner/business routines when its semantics fit. Explicit product-native/provider/native deterministic schedulers remain valid when they are the stronger owning mechanism.

A scheduled routine record references:

```text
routine blueprint ref
Focusa assignment ref
owner/tenant scope
OpenClaw agent/runtime ref
cadence/trigger + timezone
idempotency/replay policy
overlap policy
missed-run policy
timeout
budget/expiry
failure-attention route
pause/revoke path
```

At execution time:

```text
OpenClaw due/event
→ resolve routine + assignment refs
→ Focusa revalidates current scope/authority
→ execute deterministic/agentic/UIAI steps
→ capture Evidence/receipts
→ resolve exceptions through Needs You
→ emit source-qualified analytics/outcome refs
```

A schedule never becomes an authority grant by existing. The routine contract records the scheduler class/owner reference explicitly; OpenClaw is the normal default, not a forced wrapper around stronger deterministic/provider-native scheduling.

Prefer causal triggers:

~~~text
native event / webhook
→ source queue
→ condition
→ schedule
→ manual
~~~

A periodic reconciliation routine may coexist with event handling to detect missed events or stale state; it is a separate routine with its own acceptance.

For steady scheduled execution, bind timezone/DST behavior, lease/lock, overlap, missed-run, timeout, retry/backoff, idempotency-key strategy, ambiguous-state reconciliation, failure destination and pause/revoke semantics.

Do not promise distributed exactly-once execution. Prefer idempotent operations, source reconciliation and replay-safe contracts.

Conceptual run lifecycle:

~~~text
due/event
→ admission
→ lease
→ instance revision
→ authority/freshness preflight
→ bounded inputs
→ execute
→ verify
→ settle / receipts
→ accepted outcome
→ checkpoint
→ release
~~~


## 9. Routine maturity

Use a visible progression model:

```text
Observed → Modeled → Pilot → Proven → Automated → Compounding
                                             ↘ Paused / Retired
```

Promotion is evidence-based and reversible. Higher maturity may make greater autonomy eligible, but maturity never self-grants authority.

## 10. Analytics hierarchy

Analytics should coalesce at several levels without one giant telemetry database.

### Routine

Measure, where meaningful:

- runs / admitted / skipped / failed / recovered;
- accepted-output rate;
- cycle time and latency;
- missed/overlap/retry behavior;
- model/tool/provider/runtime cost;
- owner interventions and interruption burden;
- estimated and measured owner time bought back;
- deterministic-versus-agentic execution ratio;
- UIAI fallback frequency;
- reliability and recovery;
- downstream outcome refs;
- attribution confidence.

### Worker / role

Measure accepted outcomes, reliability, escalation quality, owner attention consumed, cost, scope violations/denials, reuse across assignments and revoke/offboarding correctness.

### Business / life domain

Measure desired-outcome movement, appropriate customer/revenue/retention or life results, operating cycle time, unresolved obligations, owner capacity, routine/system health and leverage created/lost.

### Portfolio

Measure where owner attention is going, which businesses/domains are gaining or losing momentum, cross-business shared capability, portfolio bottlenecks, capacity unlocked, risk concentration, reusable systems and the next highest-leverage opportunity.

System health remains distinguishable from life/business success.

## 11. Leverage dimensions

Leverage means one change increases future capacity. It is not one mandatory percentage.

`operator.leverage_snapshot.v1` can describe:

```text
outcome gain
capacity / time buyback
attention reduction
cycle-time improvement
reliability / recovery
cost efficiency
risk reduction
reuse across routines
reuse across businesses
new opportunity unlocked
compounding capability
```

Every claimed gain carries source/evidence refs and confidence/attribution limits.

A future additive leverage-contract revision SHOULD represent economic and lived-freedom dimensions explicitly, including `income_generation`, `cash_realization`, `gross_margin_contribution`, `retention_value`, `financial_breathing_room`, `life_enrichment` and `relationship_enrichment`. Current v1 consumers remain valid until that extension is implemented and regression-tested.

Avoid double-counting. A shared CRM integration that benefits five routines is one reusable capability with several downstream effects, not five independent copies of the same leverage.

## 12. Momentum

Momentum is sustained verified progress toward owner-defined outcomes: the direction and durability of meaningful progress, not merely consecutive app usage.

Signals may include accepted outcomes increasing, manual recurring work staying reliably handled, owner interruption burden falling, bottlenecks disappearing, cycle time improving, useful systems being reused, new capacity being converted into higher-value work, and fewer repeated failures.

Momentum may be described as:

```text
accelerating
building
steady
cooling
blocked
unknown
```

Unknown is preferable to invented certainty.

## 13. Optional W.I.N.S. projection and game dynamics

When a setup participates, W.I.N.S. adds a strong sports/game vocabulary: score, game clock, possession/focus, seasons, streaks, portfolio views and Wrapped retrospectives.

The underlying momentum/leverage truth exists before that projection. ADLBOS preserves the motivating language but tightens what counts.

Good game dynamics include:

- seasons around meaningful owner objectives;
- visible momentum from verified progress;
- evidence-backed milestones;
- routine maturity progression;
- "capacity unlocked" when owner work is genuinely bought back;
- meaningful missions/pilots;
- retrospectives/Wrapped;
- optional streaks when they reflect a behavior the owner actually values;
- unlocks that expose higher autonomy only after proof and owner policy;
- celebration of deletion/simplification when doing less creates more leverage.

Bad game dynamics include points for agent chatter/tool calls, streak pressure that punishes rest or long-cycle work, arbitrary badges disconnected from outcomes, loss-aversion or shame, manufactured urgency, addictive variable rewards, hidden scoring formulas controlling authority, or maximizing activity/engagement rather than life/business advancement.

**The game is the owner's real life/business progress.** The UI merely makes that progress legible and motivating.

## 14. W.I.N.S. relationship

W.I.N.S. is an optional setup-aware progression/recognition/community projection. It does **not** own the base outcome, momentum or leverage loop.

Source domains/owner acceptance establish outcome truth. Wirebot/Perpetua synthesizes the private cross-domain feedback/leverage loop through source-qualified refs. W.I.N.S., when enabled, presents additional progression/season/score/community semantics over that same truth.

Existing activity-weighted scoreboard mechanics are useful historical/product evidence, not universal ADLBOS law. Future scoring should increasingly privilege:

```text
accepted outcome
+ proven buyback
+ reliability
+ reuse
+ compounding leverage
```

over raw task/event volume.

A W.I.N.S. score is a projection. It never creates Focusa authority, OpenClaw scheduling rights, business truth or execution success.

## 15. Quiet Kaizen / optimization

Use the existing Leverage² order:

```text
Question
→ Delete
→ Simplify
→ Accelerate
→ Automate
```

Then close the loop:

```text
measure baseline
→ identify dominant constraint
→ propose smallest leverage move
→ adversarially review
→ pilot
→ compare
→ keep / improve / retire
→ search for reuse
→ invest released capacity into the next higher-value constraint
```

Optimization proposals never self-authorize.

## 16. Surface responsibilities

### Wirebot App

Owner-facing design and portfolio experience: "How Your Life & Businesses Run", portfolio/business map, routines, proposals, Workforce Composer, routine analytics, leverage/momentum, owner decisions and Quiet Kaizen recommendations.

The owner should see meaningful language, not cron expressions, CallGraphs or raw telemetry by default.

### OpenClaw conversation/runtime

Continuous Operating Partner, conversational access to the same canonical routine/business objects, Automations scheduling, proactive/quiet review, and delivery of useful updates and Needs You.

### Focusa Workforce

Specialist live operations: Workstream/Foreman, roster/responsibility, working now, routine-run operating posture when projected, Needs You, Evidence/verification, Direction and execution/topology.

It does not own portfolio leverage scoring.

### UIAI / Cockpit

Deep browser/computer execution, takeover, diagnostics and proof.

### W.I.N.S.

Optional setup-aware progression, seasons, score, retrospectives, recognition and community projections over source-domain outcomes and the base leverage loop. Sovereign Operator and Sovereign remain complete with this surface disabled.

## 17. Owner-facing routine experience

A routine should read like:

```text
New Lead Follow-Up

Why
  Keep qualified inquiries from being lost.

When
  When a new website inquiry arrives.

Who
  Sales Coordinator, supervised by your Operating Partner.

How
  Read inquiry → reconcile CRM → qualify → enrich → update CRM → prepare next action.

Needs You when
  pricing/terms are unusual or first outreach exceeds the standing grant.

Runs on
  private Operator server.

Proof
  CRM receipt + source refs + accepted follow-up state.

30-day effect
  94% handled without intervention
  2.1h/week owner capacity bought back
  median lead latency ↓ 61%
  one unresolved attribution caveat
```

Technical details remain available progressively.

## 18. First vertical slice

Prove one routine from beginning to compounding feedback:

```text
multi-source discovery
→ routine candidate
→ reusable template match
→ owner-specific routine blueprint
→ owner correction
→ determinization pass
→ compiled routine instance
→ Focusa binding
→ durable event/schedule binding
→ deterministic + agentic execution
→ UIAI only if required
→ Evidence
→ source-domain accepted outcome
→ operator.leverage_snapshot.v1
→ Quiet Kaizen proposal
→ optional W.I.N.S. projection if enabled
→ owner keeps/improves/retires
```

Acceptance requires denial/revocation, failed run/recovery, missed-run handling and truthful unknown analytics in addition to the happy path.

## 19. Non-goals

Do not create a new orchestration service, scheduler beside OpenClaw without an owning need, second Focusa work authority, W.I.N.S.-required base analytics path, second outcome authority, central raw telemetry lake merely for this compiler, one-business-only information architecture, infrastructure-first user experience, an "AI employee" for every routine, or gamification that rewards screen time/activity over meaningful life/business progress.
