# Current Ecosystem Architecture — Operator, Wirebot, Focusa Workforce, and Sovereign Federation

**Status:** LIVE architecture reconciliation  
**Effective:** 2026-09-15  
**Authority:** Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`  
**Purpose:** current cross-product architecture for the Agent-Driven Life & Business OS ecosystem.

This document reconciles the current Operator Deployment, Wirebot App, Focusa Workforce, Focusa, UIAI Engine, Veragensia, Startempire Wire, W.I.N.S., Draftees and MeriFolio directions into one architecture.

It does **not** create another product, runtime, entitlement authority, task store or constitution. ADLBOS remains the portable integration substrate and architecture doctrine. Product repositories remain authoritative for their own domain behavior.

Where older Golden Path or application-planning text conflicts with this document on current product ownership, app identity, Operator Deployment, Wirebot App, Focusa Workforce or current packaging direction, this document is the current reconciliation. Historical deployment scars, sequencing, checks and field-proven Golden Path mechanics remain valuable unless explicitly contradicted here.

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
                  W.I.N.S.
                    |
             optional projection
                    v
                MERIFOLIO
portable identity / trust / standing

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
- agent-operation completeness.

ADLBOS is not another customer-facing runtime or database.

### Wirebot / Wirebot App

Owns the Operating Partner experience:

- life/business orientation;
- priorities and portfolio synthesis;
- recommendations;
- broad owner conversation;
- organization design;
- Workforce Composer;
- delegation into governed work;
- owner-wide attention;
- network/community context;
- owner-facing outcomes.

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

Owns accepted outcome / portfolio semantics.

### MeriFolio

Owns portable worker identity, selective presentation, evidence-backed standing, opportunity eligibility and portable trust. It is not the Operator's local workforce runtime.

### Startempire Wire / Network

Owns community, distribution, relationships, opportunities and sovereign federation.

### AI Draftees

Owns the public worker marketplace/discovery/reputation path. Once selected into an Operator's private workforce, local work/authority is governed by that Operator's Focusa deployment.

### Task trackers / beads

A task tracker may hold legitimate implementation/task-ledger state. It does not replace Focusa's governed Workstream/Workpoint/work authority.

---

## 4. Workforce Composer versus Focusa Workforce

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
  -> accepted outcome / W.I.N.S.
  -> optional MeriFolio standing
```

---

## 5. Chief of Staff versus Foreman

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

## 6. Operator Deployment

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
+ customer-named Operating Partner (Wirebot implementation family)
+ explicitly delegated human operators, if any
+ Focusa
+ Focusa Workforce
+ UIAI as entitled/needed
+ customer/private infrastructure
+ optional Veragensia bodies
+ optional Startempire federation
```

`Sovereign` describes ownership/isolation/authority posture. It does not inherently mean DIY, offline, unmanaged, non-networked or one hosting model.

---

## 7. Current application direction

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

## 8. Capability, entitlement, activation, authority, and consent

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

## 9. Fleet versus federation

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

## 10. Shared cross-product seams

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
```

These contracts are small reference envelopes, not a new orchestration database.

### 10.1 Common envelope law

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

### 10.2 Credential/secret seam law

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

## 11. Attention / `Needs You`

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

## 12. Evidence and closure

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
  -> accepted outcome
  -> W.I.N.S. where applicable
  -> MeriFolio presentation/standing where applicable
```

---

## 13. Surface boundaries

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

## 14. Design and implementation rules

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

---

## 15. Current reconciliation actions

1. formalize Operating Partner identity + white-label presentation;
2. formalize delegated-human principal and revocation semantics;
3. formalize Chief-of-Staff → Focusa/Foreman delegation;
4. formalize Workforce Composer → assignment → Focusa Workforce lifecycle;
5. implement shared attention projection;
6. implement exact surface handoff;
7. implement universal cross-product correlation refs;
8. implement capability/entitlement/activation posture;
9. implement Evidence → settlement → W.I.N.S. closure refs;
10. implement opaque credential-use references without moving secrets;
11. require shared-envelope compatibility/freshness/replay metadata;
12. distinguish fleet from sovereign federation everywhere;
13. keep MeriFolio outside local workforce authority;
14. update historical app/packaging language to current Wirebot App ownership;
15. compile Golden Path/task ledgers into existing Focusa-governed work rather than creating another task authority.

---

## 16. Non-negotiable summary

```text
ONE OWNER ROOT
BOUNDED DELEGATED HUMAN OPERATORS WHERE NEEDED
ONE DURABLE OPERATING PARTNER RELATIONSHIP
ONE GOVERNED WORK PLANE: FOCUSA
ONE SPECIALIST WORKFORCE OPERATIONS SURFACE: FOCUSA WORKFORCE
ONE COMPUTER EXECUTION AUTHORITY: UIAI ENGINE
ONE BODY/RUNTIME/PLACEMENT SUBSTRATE: VERAGENSIA
ONE ACCEPTED-OUTCOME LAYER: W.I.N.S.
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
