# Wirebot Application Family and Startempire Wire Integration Architecture

**Status:** CURRENT architecture  
**Effective:** 2026-09-15  
**Depends on:** `CURRENT_ECOSYSTEM_ARCHITECTURE.md`, `OWNER_AUTHORITY_CONSTITUTION.md`, Golden Path, current Wirebot App and Focusa Workforce repositories.

This document defines the current application-family and ecosystem integration architecture. It replaces earlier wording that treated the Wirebot application family, repository ownership, and packaging direction as unresolved.

The current Wirebot application implementation lives in:

```text
Startempire-Wire/Wirebot-App
```

Wirebot App is the owner-facing partner application family. It integrates domain-owned capabilities without absorbing their canonical state or authority.

---

## 1. Product thesis

Wirebot App is the application through which an owner works with their persistent Operating Partner across life, business, workforce, outcomes and optional network participation.

The Operating Partner may be presented as `Wirebot` or as a customer-selected identity such as `Spock`. White-label presentation does not fork the underlying architecture.

The application should feel coherent while preserving strict domain ownership.

```text
OWNER
  |
  v
WIREBOT APP
Operating Partner / Chief of Staff
  |
  +-- life/business orientation
  +-- priorities and recommendations
  +-- Workforce Composer
  +-- owner-wide Needs You
  +-- network/opportunity context
  +-- outcomes / W.I.N.S.
  |
  v
FOCUSA GOVERNED WORK
  |
  +-- Project / Workstream / Foreman / Workpoint
  |
  v
FOCUSA WORKFORCE
live workforce operations
  |
  +-- UIAI execution
  +-- Veragensia bodies/runtime
  +-- workers / Pi / Silent Sessions
```

Wirebot App is not a second Focusa, second Workforce runtime, second UIAI Cockpit, or second Startempire Wire backend.

---

## 2. Current ownership map

| Concern | Canonical owner | Wirebot App role |
|---|---|---|
| Operating Partner relationship and partner-facing experience | Wirebot family | primary presenter and typed intent client |
| Portfolio goals/priorities and owner-level synthesis | Wirebot family + owning business sources | synthesize and recommend |
| Governed work, Workstreams, Foremen, Workpoints, scoped authority, Evidence | Focusa | project bounded projections and typed requests |
| Active workforce operations | Focusa Workforce | summary/deep-link/specialist handoff |
| Browser/computer execution | UIAI Engine | request supported operations and project execution status |
| Bodies/Agent Computers/runtime enforcement | Veragensia | device/body posture and exact specialist handoff |
| Accepted outcomes | W.I.N.S. | portfolio/outcome projection |
| Portable worker trust | MeriFolio | selective import/projection; never local authority |
| Community/distribution/federation | Startempire Wire | native modules/adapters where entitled |
| Public worker marketplace | AI Draftees | discovery/hire candidate path |
| Commerce/billing/membership | owning Startempire/commerce systems | account/entitlement projection and hosted flows |

One function has one owner. App modules never become alternate domain databases.

---

## 3. Operating Partner identity and white-labeling

Wirebot App MUST distinguish:

```text
CanonicalOwnerPrincipal
OperatingPartnerPrincipal
partner presentation profile
runtime/provider/model
optional ArchitectureAuthorityPrincipal
```

A customer can name the partner `Spock` while the implementation family remains Wirebot.

Conceptual profile:

```yaml
schema: operator.partner_profile.v1
owner_principal_ref:
partner_principal_ref:
implementation_family: wirebot
presentation:
  display_name: Spock
  avatar_ref:
  voice_profile_ref:
  brand_ref:
deployment_ref:
network_presentation_ref:
```

Presentation changes MUST NOT create a new partner identity or authority chain.

A Chief of Staff does not gain architecture authority merely because it has broad context. Any such authority remains separately delegated under ADLBOS owner-rooted contracts.

---

## 4. Wirebot App versus Focusa Workforce

The products converge deeply but at different altitudes.

### Wirebot App

Answers:

```text
What matters across my life/business?
What should happen next?
What should be delegated?
What capability or role is missing?
What genuinely needs me?
What outcomes were accepted?
What network opportunity is relevant?
```

### Focusa Workforce

Answers:

```text
Who is working right now?
What Workstream are they operating?
What is each actor doing?
What is blocked?
What needs the owner in this workforce?
Where is execution happening?
What evidence/verification exists?
```

Wirebot App should project summary state from Workforce/Focusa and deep-link into the exact operational context rather than recreating the operations room.

---

## 5. Workforce Composer versus Workforce operations

`Workforce Composer` remains a Wirebot/ADLBOS product concept for organization design and commissioning.

It answers:

- which role or team should exist;
- why that role is justified;
- objective and acceptance;
- capabilities/tool bundle;
- data scope;
- budget/spend envelope;
- supervisor/Foreman relationship;
- activation/lifetime posture;
- whether a Draftee or existing worker can fill the role.

It produces an assignment/employment proposal and, after owner/governance acceptance, hands exact refs into Focusa.

It does not itself create ambient tool authority or a second roster database.

Focusa Workforce then operates the active organization.

```text
audit / deficiency
   ↓
Wirebot recommendation
   ↓
Workforce Composer
   ↓
CRIST + role/assignment packet
   ↓
Focusa governed binding
   ↓
Focusa Workforce
   ↓
execution / Evidence / outcome
```

---

## 6. Chief of Staff → Focusa/Foreman delegation

Wirebot delegates desired outcomes, not implementation-private reducer writes.

The shared delegation seam should carry refs and intent approximately like:

```yaml
owner_ref:
partner_ref:
project_ref:
workstream_ref:
requested_outcome:
priority:
constraints: []
context_refs: []
authority_refs: []
budget_ref:
acceptance_refs: []
correlation_ref:
origin_conversation_ref:
```

Focusa resolves or validates the Workstream, Foreman, Workpoint, graph/frontier and worker execution according to its own contracts.

Wirebot must not fabricate Focusa state merely to complete a delegation UI.

---

## 7. Shared `Needs You`

Human attention should be one source-bearing concept with different projections.

Wirebot App renders **owner-wide attention** across life/business/network/workforce.

Examples:

```text
business decision
owner truth / clarification
workforce approval
UIAI authentication/takeover
resource/budget exception
recovery decision
network opportunity
```

A shared `operator.attention.v1` reference identifies the item and its source owner.

Wirebot does not recreate a Focusa approval; Workforce does not recreate a UIAI takeover; each surface resolves the source object through its owner.

---

## 8. Exact specialist handoff

The app should never send the user to another product and force them to find the object again.

Use the ADLBOS shared `operator.surface_handoff.v1` family.

Examples:

```text
Wirebot → Workforce
project + Workstream + Foreman + work/attention + intent

Wirebot → UIAI
exact execution/browser context + intent=watch/intervene

Workforce → UIAI
exact execution ref + work refs

Wirebot → Veragensia
body/runtime ref + intent=inspect/resolve
```

Handoff envelopes carry references and intent, not broad credentials or transferred authority.

---

## 9. Operator Deployment

`Operator Deployment` is a professional implementation/deployment offer. It is not another product runtime or authority class.

A normal private Operator deployment can include:

```text
customer Canonical Owner Principal
customer-named Wirebot Operating Partner
private/dedicated Focusa
Focusa Workforce
UIAI where entitled/needed
private/customer infrastructure
optional Veragensia Agent Computers/bodies
optional Startempire federation
```

Wirebot App is the natural owner-facing application for such deployments.

A branded route may present the customer's partner identity without creating a separate app implementation.

Example:

```text
partner presentation: Spock
implementation family: Wirebot
work governance: Focusa
workforce operations: Focusa Workforce
computer execution: UIAI
runtime/body: Veragensia
```

---

## 10. Independent dimensions

Do not turn commercial/deployment combinations into mutually exclusive architecture lanes.

| Dimension | Examples |
|---|---|
| Purchase / participation | component purchase, Wirebot Direct, network benefits, implementation/support engagement |
| Runtime isolation | shared, dedicated/Sovereign |
| Hosting / operation | platform-managed, customer-owned, operator-managed, hybrid |
| Federation / sharing | private, selected federation, broader network participation |
| Interface / access | Wirebot App, Workforce extension, Focusa Desktop, UIAI Cockpit, voice, Agent Computer |

`Sovereign` describes ownership/isolation/authority posture. It does not inherently mean DIY, unmanaged, offline, self-hosted, or non-networked.

---

## 11. Capability and commercial expansion

Use one architecture with progressively available capabilities.

Every capability preserves separate posture for:

```text
supported
entitled
activated/connected
authorized
currently available
consented for this effect
```

Wirebot may recommend an adjacent product/service when a real need appears:

- UIAI when computer/browser actuation is required;
- cloud/Agent Computer capacity when local resources are constrained;
- Draftees when a role is unfilled;
- federation when external opportunities/collaboration are useful;
- premium support/Operator services when operational complexity warrants it.

A recommendation never grants the capability. Purchase never grants worker authority.

Avoid generic upgrade spam; expansion should explain the observed gap and why the adjacent capability helps.

---

## 12. Startempire Wire and sovereign federation

Startempire Wire is strategically important, but private operation remains independently useful.

Federation is explicit.

A sovereign node exposes only approved projections and operations.

Cross-node requests should bind, as applicable:

- protocol/schema version;
- issuer identity/node;
- subject organization/principal ref;
- audience;
- exact operation/resource scope;
- entitlement/capability reference;
- freshness/expiry;
- nonce/idempotency/replay protection;
- minimized payload;
- evidence/provenance refs;
- correction/revocation/dispute state;
- trust/signature chain.

Federation never grants the network ambient private memory, credentials, files, messages, projects, UIAI control or owner authority.

---

## 13. AI Draftees relationship

Recommended boundary:

```text
AI Draftees
public marketplace / reputation / discovery
       ↓
select / hire
       ↓
Wirebot Workforce Composer
private role + assignment
       ↓
Focusa governed binding
       ↓
Focusa Workforce
private operations
```

Public marketplace identity and private worker assignment are linked, not merged.

A worker's public standing never automatically authorizes access to a private Operator environment.

---

## 14. W.I.N.S. and MeriFolio

Keep the closure ladder explicit:

```text
execution
  → Focusa Evidence
  → verification / settlement
  → accepted life/business outcome
  → W.I.N.S.
  → optional MeriFolio presentation/standing
```

W.I.N.S. owns accepted outcomes/portfolio semantics.

MeriFolio owns portable identity/trust/standing and selective disclosure. It is not the local workforce control plane.

---

## 15. Wirebot App module map

Current high-level module architecture:

```text
Today / Home
Life & Business
Workforce Composer
Work / Results
Needs You
Community / Network
Opportunities
W.I.N.S.
Systems / Readiness
Devices / Bodies
Settings
```

Specialist handoffs:

```text
Focusa Workforce → detailed active workforce operations
Focusa Desktop   → deep governed project/work/cognition
UIAI Cockpit     → detailed computer/browser execution
Veragensia       → body/runtime/Agent Computer detail
```

The App may render bounded summaries from those systems, but it must not silently absorb their domain logic.

---

## 16. First-party operation completeness

Every consequential first-party UI action should map to a canonical versioned operation with appropriate:

- authentication;
- principal/tenant scope;
- entitlement check;
- authority/consequence semantics;
- schema validation;
- idempotency/revision handling;
- receipts;
- diagnostics and recovery;
- API/CLI/tool parity.

Wirebot must not click through its own web products as the normal integration method.

Missing structured operations are parity defects.

---

## 17. Application packaging

Older Golden Path material proposed a Tauri wrapper before the current Wirebot App product crystallized.

Current rule:

- `Startempire-Wire/Wirebot-App` is the application-family implementation owner;
- Web/PWA is a current surface;
- desktop/mobile packaging remains an implementation choice;
- Tauri may be selected later if it remains the best packaging/support bridge;
- packaging technology never defines canonical partner identity or product authority;
- separate tier-specific app forks are prohibited;
- customer-specific domains/branding should project the same application family rather than copy the app.

---

## 18. Current architecture gaps

The remaining work is mostly seams, not new products:

1. machine-readable Operating Partner + presentation profile;
2. owner/account/tenant/partner/Focusa/Sovereign-node link and revoke contract;
3. Chief-of-Staff → Focusa/Foreman delegation contract;
4. Workforce Composer assignment compiler/schema;
5. shared `Needs You` attention projection;
6. exact surface handoff contract;
7. cross-product correlation envelope;
8. entitlement/capability posture projection;
9. Evidence → settlement → W.I.N.S. closure references;
10. sovereign federation live end-to-end proof;
11. Draftees ↔ private workforce identity mapping;
12. W.I.N.S. reusable modules and tenancy proof;
13. tenant-isolated OpenClaw operating-partner continuity from conversation through verified learning.

### 18.1 OpenClaw operating-partner seam

OpenClaw supplies the persistent conversation, synthesis and coordination runtime for Wirebot. It does not own principal identity, tenant admission, consent, credentials, execution authority, durable outcomes or learning truth.

```text
owner → Wirebot App → Wirebot Core / owning services
      → entitled tenant LBI on the existing shared OVH OpenClaw gateway
         (or separately approved dedicated Sovereign runtime)
      → typed accepted operation
      → Focusa / owning executor / UIAI
      → evidence + terminal receipt + consumer outcome
      → owning outcome/learning services
      → same OpenClaw thread + App state
```

The seam requires: value-free exact-tenant runtime identity/topology; isolated revocable agent/workspace binding; stable relationship-thread continuity; minimum consented context with correction return; accepted-intent to typed-operation compilation; separately governed execution; meaningful progress/interruption/recovery; shared receipt/outcome return; inspectable later behavioral learning; and tier/topology/isolation/degraded-mode conformance.

Post-migration deployment is explicit: Startempire Wire/MemberPress on KnownHost owns entitlement and triggers the WordPress provisioning lifecycle; Wirebot Core on KnownHost owns tenant admission and the OpenClaw adapter; Core reaches the existing OVH gateway privately through `GATEWAY_URL=http://ovh-openclaw:18789`. WordPress's legacy loopback gateway option is not an active route or authority. Current provisioning creates the Core tenant and workspace but does not yet create and verify the LBI, so WordPress `active` is not runtime-readiness proof.

A local command, open port, configured URL or healthy sovereign-operator agent does not prove a member runtime. Missing tenant isolation remains `unavailable`; it never licenses a shared-runtime fallback. Gateway transport never grants tool, credential, scope or budget authority.

Wirebot App journey graph revision 6 decomposes this as `R00.01`–`R00.09`. Golden Path gap `NEW-P0-12` consumes that path without creating another runtime or authority owner.

Close these through the existing owners and shared ADLBOS contracts. Do not create a new integration backend merely to host the seam.

### 18.2 Wirebot level integration across the full relationship

Levels change relationship depth, topology, budgets and available capabilities; they do not create separate identity, consent, authority, outcome or learning systems. The canonical matrix lives in Wirebot Core `docs/TIER_RUNTIME_CONTRACT.md` §12.

The Full Trajectory must cross every applicable level through the same causal stages:

```text
identity + entitlement
  → consented understanding
  → evidence-bound anticipation/recommendation
  → owner alignment and approval
  → typed, separately governed execution
  → progress/interruption/recovery
  → verified outcome and owner correction
  → later behavior that demonstrably learned
```

The level-specific obligations are:

- **Level 0 `free`:** truthful orientation only; never simulate a partner relationship.
- **Level 1 `freewire`/`advertiser`:** owner-controlled identity, preferences and consent preparation; runtime-dependent stages remain explicitly unavailable.
- **Level 2 `wire`/`wirebot_direct`:** shared-gateway isolated LBI and the core relationship loop, with separate execution authority.
- **Level 3 `extrawire`:** level 2 plus multi-business coordination, analytics, presets and owner-visible budget controls, still without cross-tenant authority.
- **Level 4 `sovereign`:** separately approved dedicated runtime, BYOK/custom model/domain/branding, portability and teardown.
- **Level 5 `sovereign_builder`:** explicit purpose-bound tenant administration with full audit; never ambient cross-tenant access or impersonation.

Acceptance is a matrix of level × relationship stage × lifecycle transition × topology/failure mode. Purchase, upgrade, downgrade, suspend, cancel, refund, reactivation, Sovereign migration and Builder action must preserve identity/evidence while revoking no-longer-entitled capability before presentation changes.

MemberPress mapping, provisioning level, PWA presentation and Core/App capabilities must consume one versioned entitlement projection. Conflicts fail closed. Authoritative product titles settle the target mapping: `32073` is `advertiser`, while `48595` and `48596` are `wirebot_direct`. The live PWA map must be corrected from `32073 → extrawire` and must add the two Wirebot Direct products; until then, neither discrepancy may grant runtime authority.

---

## 19. Non-negotiable application rule

```text
Wirebot App runs the relationship.
Workforce Composer designs/commissions the organization.
Focusa governs the work.
Focusa Workforce runs the workforce.
UIAI runs computer execution.
Veragensia supplies/enforces bodies and runtime.
W.I.N.S. records accepted outcomes.
Startempire Wire connects sovereign participants when they choose.
```

The user experience should feel integrated. The canonical state should remain correctly separated.
