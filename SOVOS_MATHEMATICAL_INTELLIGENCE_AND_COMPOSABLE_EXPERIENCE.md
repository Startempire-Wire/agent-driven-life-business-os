# SOVOS Mathematical Intelligence and Composable Experience Architecture

**Status:** CURRENT implementation architecture; staged implementation required  
**Effective:** 2026-10-05  
**Authority:** `OWNER_AUTHORITY_CONSTITUTION.md`, `CURRENT_ECOSYSTEM_ARCHITECTURE.md`  
**Related:** `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`, `SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`

## Purpose

SOVOS should become more intelligent without becoming more complicated to use. Mathematical engines reduce uncertainty, detect structure, estimate state, optimize bounded choices and measure verified change. Focusa turns those results into governed, evidence-linked cognition and trusted generated UI. Wirebot turns that state into a small human-facing composition vocabulary. UIAI Engine supplies browser/computer observation, actuation, diagnostics and visual proof.

Normal users should experience: **Wirebot notices what matters, understands why, knows what probably happens next, shows the best move, carries authorized work through, verifies the result and learns without becoming noisy.**

## Canonical layering

~~~text
owner purpose / life / business
→ SOVOS domain semantics
  routines · Perpetua · follow-through · frontiers · leverage
→ mathematical intelligence
  belief · state · time · pattern · change · graph · capacity
  decision · causal · optimization · reliability · learning
→ Focusa
  Context · Evidence · Prediction · Constraint · Trajectory
  Workpoint · Metacognition · Reflex · Verification · Receipt
→ Wirebot intelligence projection
  insight · opportunity · constraint · decision · thread · momentum
→ Wirebot composition registry
→ Focusa trusted elements + existing A2UI renderer
→ Wirebot design system
→ user

UIAI Engine feeds bounded browser/computer Evidence into Focusa and performs authorized execution/proof.
~~~

No layer creates a second owner for state already canonically owned elsewhere.

## Four implementation registries

### 1. Intelligence Result Registry

All mathematical engines, bounded inferences and Perpetua analyses normalize before UI composition. A result carries a subject ref, finding kind, human meaning, Evidence/provenance, freshness, uncertainty posture, importance posture, optional recommendation/recheck, owner-attention posture, allowed action refs and optional advanced model details. It is a projection, not a new database or authority grant.

### 2. Mathematical Engine Registry

| Family | Candidate methods | Primary job |
|---|---|---|
| Belief | Bayesian updating / evidence fusion | evidence-backed belief posture |
| State | state machines, Markov / semi-Markov | state and transition reasoning |
| Time | survival, hazard, renewal | next-check / response / failure timing |
| Pattern | process and sequence mining, clustering | recurring workflow discovery |
| Change | SPC, EWMA, CUSUM, change points | meaningful drift |
| Graph | centrality, critical path, min-cut/max-flow | bottlenecks and systemic leverage |
| Capacity | queueing, Little's Law, assignment/flow | workload and workforce pressure |
| Decision | expected utility, value of information, Pareto | bounded next move |
| Causal | causal DAGs and controlled before/after | outcome contribution |
| Optimization | CSP/SAT/SMT, LP/MIP, matching | valid compilation and allocation |
| Reliability | MTBF/MTTR, Weibull, fault trees | reliability and recovery |
| Learning | contextual bandits, preference learning | bounded adaptation |

Each engine declares typed inputs/outputs, applicability, evidence floor, uncertainty/failure behavior, evaluation/calibration and its human-meaning translation. Learned behavior may optimize among already-permitted choices; it never creates authority.

### 3. Wirebot Composition Registry

Keep a small stable vocabulary instead of one screen per algorithm:

~~~text
I Noticed · Worth Your Attention · Quietly Watching · Still Moving
Something Is Stuck · Opportunity · Better Way Found · Ready to Automate
Needs You · Handled · What Changed? · Best Next Move
~~~

Each composition declares semantic inputs, allowed Focusa/A2UI elements, allowed actions, responsive/accessibility rules, human-language rules, advanced disclosure and unknown/recovery behavior. Perpetua decides whether, where and when a composition appears; Perpetua is not a separate inbox.

### 4. Focusa Component Binding Registry

Wirebot compositions reuse Focusa's existing trusted generated-UI substrate rather than create a parallel renderer. Useful existing elements include `FocusaContextSummary`, `FocusaContradictionCard`, `FocusaQuestionCard`, `FocusaRecommendationCard`, `FocusaReadinessMeter`, `FocusaTaskPlan`, `FocusaDependencyGraph`, `FocusaEvidenceSummary`, `FocusaReceiptCard`, `FocusaRecoveryCard` and `FocusaAdvancedDetails`. Focusa names remain implementation detail; Wirebot owns the human-facing presentation.

## Human Meaning Contract

Every intelligence result should answer, as applicable: what happened, why it matters, how strong the evidence is, what could make the interpretation wrong, what happens if nothing is done, what Wirebot recommends, whether Wirebot can handle it within current authority, and whether the owner is actually needed.

Technical results translate into stable human language: posterior support becomes **Strong evidence** or **Some evidence**; rising stall likelihood becomes **This may be stalling**; a hazard estimate becomes **Best next check**; a change point becomes **Something changed**; high centrality becomes **This system matters more than it looks**; high queue pressure becomes **Capacity is getting tight**. Raw equations/model details remain available only under advanced inspection.

Every composition supports three disclosure levels: **Human** (what matters / next action), **Explain** (why, sources, uncertainty, alternatives), and **Inspect** (Evidence, provenance, model/method, assumptions, ranges, graph, receipts).

## Initial ten capabilities

1. Perpetua Attention Engine.
2. Follow-Through Intelligence.
3. Smart Routine Discovery.
4. Routine Readiness / Compiler Preview.
5. Operational Drift Detection.
6. Quiet Kaizen.
7. Bottleneck Finder.
8. Capacity, Economic and Life Enrichment Frontiers.
9. Momentum & Leverage.
10. Smart Onboarding / Active Discovery.

The broader mathematical ideas remain a capability reservoir. Promote one only when it improves a real owner outcome, has lawful/source-qualified inputs, normalizes through the Intelligence Result contract, fits an existing composition or justifies a reusable new composition, introduces no new authority/store/renderer, and can be evaluated against accepted outcomes.

## Focusa / Wirebot / UIAI ownership

Focusa owns governed cognition, Evidence, continuity, verification, Workpoints, prediction/metacognition and the trusted generated-UI substrate. It does not absorb SOVOS product semantics such as Perpetua, the three Frontiers, Routine Candidate/Template/Instance ownership or leverage ownership.

Wirebot owns owner-facing life/business interpretation, composition and product experience.

UIAI Engine owns browser/computer observation, actuation, diagnostics, screenshots and visual/browser proof. UIAI outputs become bounded Focusa Evidence; UIAI does not become a second cognition, routine, outcome or authority store.

## Existing implementation seam

Wirebot App already consumes the same Focusa 31-component trusted catalog and A2UI-compatible renderer strategy, pins the catalog artifact, rejects unknown components/unregistered actions and explicitly forbids a second A2UI engine or approval store. Therefore this architecture extends the existing trusted composition path rather than introducing another UI framework.

Implementation work should center on: normalized Intelligence Result contracts; math-engine adapters; a Wirebot Composition Registry; composition-to-Focusa binding metadata; human-meaning translation; contextual surface placement; and composition-level acceptance tests.

## First vertical slice

~~~text
authorized observations
→ detect one recurring follow-up pattern
→ source-backed Routine Candidate
→ recurrence/readiness inference
→ Wirebot: I Noticed
→ Routine Preview
→ Evidence + hard constraints
→ owner accepts pilot
→ exact Routine Instance
→ bounded execution
→ receiver/source verification
→ Wirebot: What Changed? / Handled
→ Perpetua + Quiet Kaizen
~~~

Proof must show: no second renderer/store/approval path; unknown remains unknown; advanced math is optional to view; authority is revalidated independently of confidence; UIAI stays inside execution/proof ownership; replay/reconnect does not duplicate effects; and verified outcomes feed learning.

## Non-goals

No statistical dashboard product, generic AI-insights feed, Perpetua inbox, second Focusa ontology, second A2UI renderer, universal intelligence database, confidence theater, universal productivity score, model-derived authority or bespoke page per mathematical method.

## Success condition

A new mathematical capability should normally require **engine adapter → normalized Intelligence Result → existing Focusa/SOVOS semantics → existing Wirebot composition**, not a new page, store, approval path or design language. The system should become smarter while the user-facing vocabulary stays stable, understandable and calm.