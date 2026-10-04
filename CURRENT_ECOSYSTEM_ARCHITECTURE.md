# Current Ecosystem Architecture — Operator, Wirebot, Focusa Workforce, and Sovereign Federation

**Status:** LIVE architecture reconciliation  
**Effective:** 2026-09-27<br>
**Authority:** Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`  
**Purpose:** current cross-product architecture for the Agent-Driven Life & Business OS ecosystem.

This document reconciles the current Operator Deployment, Wirebot App, Focusa Workforce, Focusa, UIAI Engine, Veragensia, Startempire Wire, W.I.N.S., Draftees and MeriFolio directions into one architecture.

It does **not** create another product, runtime, entitlement authority, task store or constitution. ADLBOS remains the portable integration substrate and architecture doctrine. Product repositories remain authoritative for their own domain behavior.

Where older Golden Path or application-planning text conflicts with this document on current product ownership, app identity, Operator Deployment, Wirebot App, Focusa Workforce or current packaging direction, this document is the current reconciliation. Historical deployment scars, sequencing, checks and field-proven Golden Path mechanics remain valuable unless explicitly contradicted here.

---

## 0. Information infrastructure beneath the topology

The product topology in this document is an implementation view over a deeper SOVOS information infrastructure.

SOVOS first defines portable laws for:

~~~text
identity
source ownership
semantic objects and relationships
provenance
scope / tenancy
authority and delegation
freshness / revision
uncertainty
Evidence / verification / receipts
causal correlation
accepted outcomes
~~~

Then the product architecture assigns canonical ownership of those concerns to independent systems.

This is why interoperability does not require one global database or one product-owned ontology. Products keep canonical state in their own domains; portable references and contracts preserve enough meaning for safe cross-system operation.

See SOVOS_INFORMATION_INFRASTRUCTURE.md.

---

## 0.1 Human altitude and agent-driven operation

SOVOS is an **Agent-Driven Life & Business Operating System** under human sovereignty.

The target is not maximum human-in-the-loop interaction. It is correct human placement:

~~~text
HUMAN SOURCE
purpose · values · ownership · direction · reserved authority

HUMAN ON THE LOOP
visibility · pause · revoke · redirect · takeover · challenge

HUMAN IN THE LOOP
new authority · consequential exception · owner truth · high-level judgment

HUMAN OUT OF ROUTINE OPERATIONAL LOOP
already-authorized execution · monitoring · coordination · retries · routine decisions

AGENTS IN THE OPERATIONAL LOOP
persistent governed work across life/business systems
~~~

Routine work should escalate when it reaches a true authority/judgment boundary, not merely because an agent acted.

The corresponding altitude rule is:

> **Do not confuse the wing with the flight.**

Models, workers, agents, automations and Agent Computers are instruments below the human-purpose layer. Architecture quality is partly judged by whether those instruments return usable human capacity rather than creating a larger machine-maintenance burden.

See `SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md`.

For the connected Capacity, Economic and Life Enrichment frontiers; Revenue, Financial Recovery and Relationship/Life spines; and capacity-reinvestment completion tests, see `SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`.

---

## 0.2 Driverless Business target

SOVOS supports a **Driverless Business** operating posture: ordinary business operation can continue under mapped purpose, routines, information, decision policies and bounded delegated authority without requiring the owner to continuously intervene.

Driverless does not mean ownerless or autonomous architecture authority.

~~~text
owner purpose / direction / reserved authority
        ↓
mapped operating knowledge + routines + policy
        ↓
bounded delegated agent authority
        ↓
routine autonomous operation
        ↓
Evidence / outcomes / feedback
        ↓
human only at genuine exception or authority boundaries
~~~

The owner retains inspect, interrupt, pause, redirect, revoke and takeover powers.

See `SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md`.

---

## 1. System law

> **One concern, one canonical owner. Many surfaces may project it; no surface becomes a second authority merely because it renders or initiates an operation.**

```text
CANONICAL OWNER PRINCIPAL
human / legal owner
        |
        +--> delegated humans, if explicitly granted
        |
        v
OPERATING PARTNER / CHIEF OF STAFF
Wirebot implementation family
customer-selected presentation identity, e.g. "Spock"
        |
        | orient · recommend · govern · delegate
        v
FOCUSA
canonical governed work plane
Project · Workstream · Foreman · Workpoint · authority · Evidence · Receipts
        |
        v
FOCUSA WORKFORCE
specialist workforce-operations surface
people · work · direction · attention · proof · topology
        |
        +-----------------------+
        |                       |
        v                       v
UIAI ENGINE                VERAGENSIA
browser/computer           bodies · runtime · placement
execution/proof            enforcement · control
        |                       |
        +-----------+-----------+
                    v
              EXECUTION FABRIC
Pi · compatible agents · Silent Sessions · workcells · Agent Computers
                    |
                    v
             EVIDENCE / RECEIPTS
                    |
                    v
             ACCEPTED OUTCOMES
                    |
                    v
        BASE PRIVATE FEEDBACK LOOP
   Wirebot / Perpetua · leverage · Quiet Kaizen
                    |
          +---------+---------+
          |                   |
          v                   v
 optional W.I.N.S.       optional MeriFolio
 progression /           portable identity /
 recognition             trust / standing

---------- OPTIONAL SOVEREIGN NETWORK BOUNDARY ----------

STARTEMPIRE WIRE NETWORK
community · opportunities · Draftees · collaboration · federation
```

ADLBOS owns the portable laws that keep these systems coherent. It does not absorb their implementations.

---

## 2. Identity model

### 2.1 `CanonicalOwnerPrincipal`

The human or legal owner is the root architecture authority for one deployment. Client deployments establish their own owner principal and never inherit Startempire authority by copying software or infrastructure.

### 2.2 `OperatingPartnerPrincipal`

The persistent AI operating partner / Chief of Staff serving that owner.

Customer-facing presentation names may include:

```text
Wirebot
Spock
Athena
Jarvis
Chief
```

A customer-selected name is not a new architecture. The current implementation family is Wirebot, but presentation identity is configurable.

The partner persists across model, runtime, host and body changes. Changing OpenClaw, Pi, model provider, VPS or computer MUST NOT silently create a new partner identity.

### 2.3 `DelegatedHumanPrincipal`

A deployment may authorize humans other than the Canonical Owner Principal to operate bounded parts of the system: assistants, employees, family members, administrators, contractors or service operators.

A delegated human principal is **not** a second owner root merely because the person can operate the system.

A delegation must bind, as applicable:

- delegating owner principal;
- exact human principal identity;
- allowed domains/resources/operations;
- consequence classes and approval limits;
- data/credential visibility limits;
- validity window;
- delegation/redelegation policy;
- revocation and audit references.

```text
DelegatedHumanPrincipal != CanonicalOwnerPrincipal
operator access          != architecture authority
```

Delegated humans may receive operational authority under owner policy. Architecture authority remains owner-rooted unless separately and explicitly delegated under the constitution.

### 2.4 `ArchitectureAuthorityPrincipal`

Optional. A durable AI principal may receive owner-rooted cryptographic authority to make specified canonical architecture decisions.

```text
OperatingPartnerPrincipal != ArchitectureAuthorityPrincipal
```

Being the Chief of Staff, Wirebot, Spock, a root process or a highly capable agent does not create architecture authority.

### 2.5 Runtime / workload identity

Processes, sessions, models, workers, nodes, browsers, containers and Agent Computers are runtime identities/incarnations. They never substitute for durable owner, delegated-human or partner identity.

---

## 3. Product and domain ownership

### ADLBOS

Owns portable integration doctrine:

- Canonical Owner Principal;
- identity/tenancy separation;
- human-delegation boundary law;
- common handoff semantics;
- cross-product correlation requirements;
- capability/entitlement/authority separation;
- evidence-to-outcome handoff law;
- federation boundary law;
- Golden Path deployment/operations doctrine;
- agent-operation completeness;
- portable agent-contract optimization/evolution law.

ADLBOS is not another customer-facing runtime or database. It does not own runtime learning truth or transcript memory; `AGENT_CONTRACT_OPTIMIZATION_PROFILE.md` governs how source-bearing operating evidence may propose portable contract changes without moving canonical state out of its owner.

### Wirebot / Wirebot App

Owns the Operating Partner experience:

- life/business orientation;
- priorities and portfolio synthesis;
- recommendations;
- broad owner conversation;
- organization design;
- Portfolio Business Compiler;
- Workforce Composer;
- delegation into governed work;
- owner-wide attention;
- **base cross-domain feedback / leverage / Quiet Kaizen synthesis**;
- setup-aware optional W.I.N.S. projection;
- network/community context where applicable;
- owner-facing outcome interpretation.

Wirebot/Perpetua can derive source-qualified `operator.leverage_snapshot.v1` projections from owning metrics, Focusa Evidence/settlement, OpenClaw execution history, UIAI proof and owner correction. This base feedback/optimization loop is available independently of W.I.N.S.

Wirebot App is the current application-family repository.

### Focusa

Owns canonical governed work and continuity:

- Project identity;
- Workstream;
- Foreman;
- Trajectory;
- Workpoint;
- work/task/CallGraph projections under Focusa contracts;
- capability and authority enforcement at the work plane;
- Evidence and receipts;
- conversation/work continuity;
- recovery and settlement semantics.

### Focusa Workforce

Owns the specialist workforce operations experience:

- roster and responsibility;
- active work and dependency progression;
- Foreman and worker projections;
- Direction into exact Workstreams;
- workforce-scoped Needs You/attention;
- approvals as projections of owning authority;
- Evidence inspection;
- execution/topology projection;
- exact handoffs into UIAI/Veragensia;
- multi-daemon owner view.

It is a projection and intent client, not another work database or authority system.

### UIAI Engine

Owns browser/computer observation, actuation, diagnostics, control leases, takeover/reconciliation and execution proof.

### Veragensia

Owns Agent Computer/body/runtime concerns: runtime incarnation, body identity, enforcement, resource/placement posture, trusted human control and Agent Computer lifecycle.

### W.I.N.S.

W.I.N.S. is an **optional setup-aware progression, recognition and community projection**, not the base feedback/optimization engine and not the only accepted-outcome path.

When enabled for the current Wirebot setup, W.I.N.S. may project seasons, streaks, score, progress, portfolio patterns, routine contribution, buyback/delegation gains, milestones and community/recognition views over source-qualified outcomes and leverage snapshots.

It must preserve:

```text
activity metric
!= Evidence
!= source-domain accepted outcome
!= base leverage snapshot
!= optional W.I.N.S. progression projection
```

A deployment that does not participate in W.I.N.S. MUST still retain full private routine analytics, outcome verification, momentum/leverage inference and Quiet Kaizen optimization.

W.I.N.S. participation never grants work authority, creates business truth, or substitutes for source-owned analytics.

### MeriFolio

Owns portable worker identity, selective presentation, evidence-backed standing, opportunity eligibility and portable trust. It is not the Operator's local workforce runtime.

### Startempire Wire / Network

Owns community, distribution, relationships, opportunities and sovereign federation.

### AI Draftees

Owns the public worker marketplace/discovery/reputation path. Once selected into an Operator's private workforce, local work/authority is governed by that Operator's Focusa deployment.

### Task trackers / beads

A task tracker may hold legitimate implementation/task-ledger state. It does not replace Focusa's governed Workstream/Workpoint/work authority.

### Flow Mesh

Flow Mesh is the **cross-surface projection and synchronization fabric**. It exists because a task tracker — Beads included — gives a human no easy visible surface to work on a task beside an agent. Flow Mesh supplies that missing face: one normalized projection rendered onto every surface a human or agent actually uses, kept synchronized in both directions.

It owns:

- its own integration state — the cross-surface identity map, per-surface revisions, the event ledger, and projection cursors;
- synchronized projection of task state across surfaces;
- provider synchronization, task attempts, dependency execution, retries, joins, compensation, and runtime events bound to Focusa CallGraph frames;
- bounded execution of a task Focusa has already dispatched and authorized.

It owns **no task authority**. Task status, backlog, dependencies, queue order, and completion state belong to the surface that owns them: **Beads is the local task truth**, while Asana and Google Tasks own their own surface history. Flow Mesh holds a **materialized projection view** of that state — used for revision diffing, conflict merging, rendering, and drift detection — and never a second store. Authority for any given task is resolved **per disagreement**, not by a blanket owner.

Rules that travel with it:

1. Projection receipts are recorded separately from canonical mutations.
2. Dispatch is never completion.
3. An adapter may not redefine project, work, progress, authority, or evidence semantics.
4. A second engine instance must never write the same ledger; one active engine owns a mesh.
5. Flow Mesh may not become an independent task authority, a second Focusa, or a second scheduler.

At scale this is the substrate that carries human-and-agent task collaboration across every surface, so it must remain a projection layer: its per-tenant isolation and its projection correctness are load-bearing, and its blast radius must stay bounded to the surfaces it serves.

---

## 4. Wirebot setup modes and the base optimization loop

Customer-facing architecture recognizes four Wirebot setup modes:

| Wirebot setup | Base private feedback / optimization loop | W.I.N.S. |
|---|---|---|
| **Wirebot Sovereign Operator** | required/base capability | **optional, explicit opt-in** |
| **Wirebot Sovereign** | required/base capability | **optional, explicit opt-in** |
| **Wirebot Direct** | required/base capability | included according to the Direct offer; Network/federation/public sharing remain separate permissions |
| **Wirebot Network** | required/base capability | native to the Network relationship under its owning participation/sharing policy |

These setup modes are customer/relationship topologies. They are **not the same thing as Wirebot's internal technical entitlement levels** and MUST NOT be collapsed into numeric level ordering.

In particular:

```text
Wirebot Sovereign Operator
!= sovereign_builder technical/admin role

Wirebot setup mode
!= MemberPress numeric level
!= runtime topology alone
!= W.I.N.S. participation state
```

For Sovereign Operator and Sovereign, W.I.N.S.-off is a complete valid operating state.

The mandatory feedback loop is:

```text
source-owned life/business signals
+ routine execution telemetry
+ Focusa Evidence / settlement
+ OpenClaw run history
+ UIAI proof where applicable
+ owner correction
        ↓
operator.leverage_snapshot.v1
        ↓
Wirebot / Perpetua synthesis
        ↓
dominant constraint / opportunity
        ↓
smallest leverage proposal
        ↓
owner/governance path as required
        ↓
measured implementation
        ↓
keep / improve / retire
        ↓
next compounding opportunity
```

W.I.N.S., when enabled, consumes/provides an enhanced progression view over this loop. The loop never routes *through* W.I.N.S. as a prerequisite.

---

## 5. Portfolio Business Compiler and Workforce Composer

The owner may operate **one, several, or many businesses plus personal/life domains**. ADLBOS therefore models a portfolio, not a single-business funnel.

Wirebot's Portfolio Business Compiler is a causal compilation pipeline, not a new database or runtime:

```text
authorized source coverage
→ portfolio/business/life map
→ evidenced routine candidates
→ reusable template matching
→ owner-specific typed routine blueprints
→ owner review/composition
→ determinization pass
→ compiled routine instance
→ role/workforce + least-capability binding
→ Focusa governed binding
→ durable event/schedule supervision
→ deterministic / agentic / UIAI / human execution lanes
→ Evidence / settlement
→ source-domain accepted outcome
→ base operator.leverage_snapshot.v1
→ Quiet Kaizen / optimization
→ optional W.I.N.S. progression projection when enabled
→ revised routine, role, system or retirement proposal
```

A Routine Template is reusable owner-neutral structure; a Routine Candidate is an audit inference; a Routine Blueprint is owner-specific proposed semantics; a Routine Instance is the compiled executable binding of one accepted blueprint revision; a Routine Run is one execution occurrence in owning systems. Templates never grant authority, and template changes never silently mutate active instances. See `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`.

### 5.1 Workforce Composer versus Focusa Workforce

### Workforce Composer — Wirebot/ADLBOS concern

Answers:

```text
What organization should exist?
What role is missing?
What objective should the role own?
What task packs/capabilities does it need?
What authority, budget, data and supervisor should it receive?
Should an existing worker or Draftee fill it?
```

It produces a proposed/approved employment or assignment packet. It does not directly create ambient runtime authority.

### Focusa Workforce — Focusa specialist operations concern

Answers:

```text
Who is working now?
What are they doing?
What is blocked?
What needs the owner?
Where is work executing?
What evidence exists?
What should happen next?
```

Lifecycle:

```text
business/life audit
  -> Wirebot identifies capability gap
  -> Workforce Composer proposes role/assignment
  -> CRIST + owner/governance acceptance
  -> Focusa binds governed work/authority
  -> Focusa Workforce operates the active organization
  -> Evidence / settlement
  -> source-domain accepted outcome
  -> base private leverage / feedback
  -> optional W.I.N.S. projection when enabled
  -> optional MeriFolio standing
```

---

## 6. Chief of Staff versus Foreman

```text
Operating Partner / Chief of Staff
  understands life/business portfolio
  decides/recommends what deserves attention
  delegates desired outcomes
        |
        v
Workstream Foreman
  responsible for one governed Workstream
  understands exact state/frontier/acceptance
  delegates operational subsets
        |
        v
Manager / Worker / Verifier / Specialist
  performs bounded execution
```

The Chief of Staff MUST NOT become a global Foreman simply because it has broad context. The Foreman MUST NOT gain owner-wide life/business memory merely because it operates one project.

---

## 7. Mandatory operating substrate and replaceable bodies

A normal ADLBOS Operator deployment includes:

```text
OpenClaw
  persistent Operating Partner runtime / channels / automations

Focusa
  governed work / continuity / authority / Evidence

UIAI Engine
  browser/computer observation and execution when required

Tailscale private mesh
  authenticated private transport among Operator bodies

at least one persistent remote VPS
  always-available OpenClaw/automation/service execution body
```

These architectural roles are stable while individual implementations and bodies remain replaceable. Replacing one VPS, model, Pi worker, browser, or machine does not replace the Operating Partner identity or widen authority.

The remote VPS is the default placement for durable headless/scheduled coordination when the workload fits. Reachability never grants authority. Focusa validates governed work and assignment authority; OpenClaw scheduling never turns a schedule into a grant.

OpenClaw's built-in Gateway automations scheduler is the preferred default scheduler for recurring agent-turn/system-event/condition-triggered work where its contract fits. Native deterministic services, systemd timers, provider schedulers, queues or webhooks remain valid when they are the correct owner/mechanism.

## 8. Operator Deployment

**Operator Deployment** is an implementation/commissioning offer and deployment profile, not a new authority model or runtime tier.

It maps onto independent dimensions:

| Dimension | Operator Deployment may select |
|---|---|
| Purchase / participation | component licenses, implementation/support offer, optional network benefits |
| Runtime isolation | shared where allowed or dedicated/Sovereign for private deployments |
| Hosting / operation | customer-owned, operator-managed, hosted, or hybrid |
| Federation / sharing | private/off by default; optional explicit federation |
| Interface / access | Wirebot App, Focusa Workforce, Focusa Desktop, UIAI, voice, Veragensia and other supported surfaces |

A normal sovereign Operator deployment may include:

```text
customer owner
+ customer-named Operating Partner (Wirebot implementation family) on OpenClaw
+ explicitly delegated human operators, if any
+ Focusa
+ Focusa Workforce
+ UIAI Engine
+ Tailscale private mesh
+ at least one persistent remote VPS
+ optional additional Veragensia bodies
+ optional Startempire federation
```

`Sovereign` describes ownership/isolation/authority posture. It does not inherently mean DIY, offline, unmanaged, non-networked or one hosting model.

---

## 9. Current application direction

The current customer/partner application family is **Wirebot App** (`Startempire-Wire/Wirebot-App`).

Older Golden Path material proposed a Tauri wrapped client and separate per-client Svelte Chief-of-Staff surfaces before the current Wirebot App crystallized. Those proposals remain historical implementation evidence, not current app-ownership authority.

Current rule:

- Wirebot App owns the partner/customer application experience;
- branded customer routes/domains MAY project the same application family;
- desktop/mobile packaging may use Tauri or another appropriate adapter later;
- packaging technology does not define product identity;
- a per-client web route MUST NOT evolve into a separate Chief-of-Staff frontend with duplicated logic;
- DIY component sovereignty remains distinct from managed/operated service delivery.

---

## 10. Capability, entitlement, activation, authority, and consent

These MUST remain separate:

```text
SUPPORTED
  != ENTITLED
  != ACTIVATED/CONNECTED
  != AUTHORIZED
  != CONSENTED FOR THIS EFFECT
```

Commercial expansion unlocks capability or service availability. It MUST NOT silently mint operational authority.

Upsells SHOULD arise contextually from real capability gaps while remaining non-authoritative recommendations.

---

## 11. Fleet versus federation

Reserve **federation** for independent sovereign participants.

One Operator may have multiple Focusa daemons, machines, Agent Computers or execution bodies. Use:

```text
fleet
multi-daemon aggregation
environment fleet
runtime fleet
```

All projected items retain source environment/daemon identity.

**Sovereign federation** means independent Operators exchanging explicitly approved projections/requests through Startempire Wire or another compatible network.

Federation never implies pooled private memory, inherited owner authority, ambient files/messages/projects, shared credentials or automatic remote control.

---

## 12. Shared cross-product seams

Cross-product seams are ADLBOS-level portable contracts. Individual products implement adapters; they do not invent competing semantics.

Required shared contract families:

```text
operator.partner_profile.v1
operator.surface_handoff.v1
operator.attention.v1
operator.correlation.v1
operator.capability_posture.v1
operator.closure.v1
operator.credential_use_ref.v1
operator.routine_template.v1
operator.routine_blueprint.v1
operator.routine_instance.v1
operator.leverage_snapshot.v1
```

These contracts are small reference envelopes, not a new orchestration database.

### 12.1 Common envelope law

Every actionable shared envelope MUST make compatibility, authority source and freshness machine-readable. As applicable, include:

```text
schema
schema_version
producer / producer_version
source_ref
owner / tenant ref
correlation_id
revision or source version
observed_at / issued_at
expires_at for time-bounded or actionable state
idempotency/replay key where a mutation may be retried
```

Rules:

- unsupported major/schema versions fail closed for consequential actions;
- additive fields may be ignored only where the consumer's compatibility contract explicitly permits it;
- stale/expired projections may remain inspectable but MUST NOT silently authorize a consequential action;
- offline caches are projections, not authority stores;
- after reconnect, revalidate current source state before mutating from cached attention, entitlement, grant or execution state;
- ambiguous mutation completion must use owning-system idempotency/reconciliation semantics rather than blind replay.

### 12.2 Credential/secret seam law

Raw long-lived secret material does not cross normal product handoffs.

`operator.credential_use_ref.v1` carries only opaque references and bounded use intent, for example:

```text
credential_ref
provider/account ref
requested operation/scope
requesting principal/work ref
consequence/approval policy ref
validity/expiry
correlation ref
```

The owning credential/secret authority resolves the reference at execution time and may deny it. Existence of a credential reference never proves current authorization to use it.

No shared envelope, URL, task description, Evidence object or Receipt should contain the reusable secret itself.

---

## 13. Attention / `Needs You`

Human attention is a scarce shared resource and should not fragment into unrelated inboxes.

One source-bearing attention projection may describe:

```text
approval
owner truth / clarification
authentication
UIAI takeover
blocker
budget/resource exception
recovery decision
network opportunity
```

Wirebot renders owner-wide attention. Workforce renders workforce-scoped attention. UIAI renders immediate execution attention. The source owner resolves the item.

**Acknowledging, hiding or dismissing an attention item in one surface is not source-domain resolution.** A presenter may store local UX acknowledgement, but canonical resolved/cancelled/expired state comes from the source owner and must be revalidated before consequential action.

---

## 14. Evidence, analytics, momentum and closure

Preserve the chain:

```text
execution/activity
    !=
Evidence candidate
    !=
verified Evidence
    !=
Focusa settlement/receipt
    !=
accepted life/business outcome
    !=
portable standing
```

Preferred flow:

```text
execution
  -> Evidence candidate
  -> Focusa Evidence
  -> verification / settlement
  -> source-domain accepted outcome
  -> base operator.leverage_snapshot.v1
  -> Quiet Kaizen / optimization candidate
  -> optional W.I.N.S. progression projection when enabled
  -> revised governed work only after applicable acceptance
  -> MeriFolio presentation/standing where applicable
```

Routine analytics must stay causal and source-backed. Keep separate run reliability, latency, cost, retries, owner attention, automation/delegation buyback, defects/reversals, and authoritative business/life outcome metrics.

No universal score may hide the underlying dimensions. W.I.N.S. can make progress engaging and game-like, but gamification must reward meaningful verified outcomes, compounding leverage, recovery and learning—not compulsive usage, notification response, raw agent activity or fabricated streak pressure.

---

## 15. Surface boundaries

### Wirebot App
Owner/partner altitude: Today/briefing, life/business, strategic priorities, Workforce Composer, owner-wide Needs You, Network/community/opportunities, W.I.N.S./outcomes, readiness/delegation.

### Focusa Workforce
Operational workforce altitude: Foreman, roster, active work/task progression, Direction, workforce Needs You, Evidence, UIAI links, fleet/topology posture.

### Focusa Desktop
Deep governed project/work/cognition surface.

### UIAI Cockpit
Detailed browser/computer execution/control surface.

### Veragensia
Body/runtime/Agent Computer lifecycle and enforcement surface.

Shared visual language is encouraged. Shared canonical state is not.

---

## 16. Design and implementation rules

1. API/operation first.
2. No CUA between first-party products as the normal integration.
3. No second databases for convenience.
4. No plan-specific app forks.
5. No white-label protocol forks.
6. No partner-wide context leakage into workers.
7. No network authority inheritance.
8. No runtime/identity collapse.
9. No UI ownership drift.
10. No raw reusable secret material in cross-product seams.
11. No consequential action from stale/expired cached authority projections.
12. Outcome over ceremony.
13. Stable semantic objects over generated ambiguity: Business/Domain, Routine, Role, Assignment, Workstream, Needs You, Evidence and Outcome remain identifiable even when UI composition adapts.
14. Generated UI may compose canonical objects; it may not invent authority or canonical objects.
15. Game dynamics reward verified advancement and leverage, not engagement volume.
16. A deterministic stable step should become code/operation before an LLM is repeatedly asked to improvise it.

---

## 17. Current reconciliation actions

1. formalize Operating Partner identity + white-label presentation;
2. formalize delegated-human principal and revocation semantics;
3. formalize Chief-of-Staff → Focusa/Foreman delegation;
4. formalize Workforce Composer → assignment → Focusa Workforce lifecycle;
5. implement shared attention projection;
6. implement exact surface handoff;
7. implement universal cross-product correlation refs;
8. implement capability/entitlement/activation posture;
9. implement Evidence → settlement → source-domain outcome → base leverage closure refs, with optional W.I.N.S. projection;
10. implement opaque credential-use references without moving secrets;
11. require shared-envelope compatibility/freshness/replay metadata;
12. distinguish fleet from sovereign federation everywhere;
13. keep MeriFolio outside local workforce authority;
14. update historical app/packaging language to current Wirebot App ownership;
15. compile Golden Path/task ledgers into existing Focusa-governed work rather than creating another task authority;
16. implement portfolio/business → routine blueprint → assignment compiler;
17. bind durable scheduled assignments to OpenClaw automations on the persistent Tailscale-connected VPS where appropriate;
18. join routine execution analytics to source-domain outcomes through the base leverage loop without requiring W.I.N.S.;
19. make W.I.N.S. a setup-aware optional projection for Sovereign Operator/Sovereign while preserving Direct/Network policy distinctions;
20. expose private momentum/leverage and optimization proposals coherently across Wirebot App and Focusa Workforce even with W.I.N.S. disabled;
21. prove one multi-business portfolio slice where a shared capability improves more than one business without crossing scope;
22. prove the same optimization loop with W.I.N.S. enabled and disabled, with identical underlying outcome/leverage truth;
23. compile audit routine candidates through reusable template → owner-specific blueprint → immutable Routine Instance without creating a new scheduler/work authority;
24. prove one real routine from the operator inventory end-to-end through Focusa assignment, durable trigger, deterministic/bounded-semantic steps, overlap/idempotency/retry/missed-run/revoke behavior, Evidence and source-domain accepted outcome.

---

## 18. Non-negotiable summary

```text
ONE OWNER ROOT
BOUNDED DELEGATED HUMAN OPERATORS WHERE NEEDED
ONE DURABLE OPERATING PARTNER RELATIONSHIP
ONE GOVERNED WORK PLANE: FOCUSA
ONE SPECIALIST WORKFORCE OPERATIONS SURFACE: FOCUSA WORKFORCE
ONE COMPUTER EXECUTION AUTHORITY: UIAI ENGINE
ONE BODY/RUNTIME/PLACEMENT SUBSTRATE: VERAGENSIA
ONE BASE FEEDBACK / LEVERAGE LOOP: WIREBOT/PERPETUA OVER SOURCE-OWNED OUTCOMES
W.I.N.S. OPTIONAL/SETUP-AWARE PROGRESSION LAYER — NEVER A BASE-LOOP PREREQUISITE
ONE OPTIONAL PORTABLE-TRUST LAYER: MERIFOLIO
ONE OPTIONAL SOVEREIGN NETWORK BOUNDARY: STARTEMPIRE WIRE

MANY PRESENTERS.
NO DUPLICATE CANONICAL STATE.
DELEGATION NEVER EQUALS OWNERSHIP.
ENTITLEMENT NEVER EQUALS AUTHORITY.
FEDERATION NEVER EQUALS AMBIENT ACCESS.
BRANDING NEVER EQUALS IDENTITY OR AUTHORITY.
HARDWARE NEVER EQUALS PARTNER.
CACHED STATE NEVER SILENTLY BECOMES CURRENT AUTHORITY.
SECRET REFERENCES NEVER BECOME SECRET DISCLOSURE.
```
