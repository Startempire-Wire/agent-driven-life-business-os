# Agent OS Golden Path

> A versioned deployment and operations doctrine for turning a fresh or brownfield environment into a verified, agent-native Life & Business OS. Executable coverage remains partial; the field-tested deployment spine remains valuable, while current product ownership is reconciled against the live ecosystem architecture.

- **Golden Path target:** `0.2.0-candidate`
- **Canonical owner authority:** [`OWNER_AUTHORITY_CONSTITUTION.md`](./OWNER_AUTHORITY_CONSTITUTION.md)
- **Current cross-product architecture:** [`CURRENT_ECOSYSTEM_ARCHITECTURE.md`](./CURRENT_ECOSYSTEM_ARCHITECTURE.md)
- **Foundational operating contract:** [`AGENTS.md`](./AGENTS.md)
- **Reference Agent Computer profile:** [`AGENT_COMPUTER_REFERENCE_PROFILE.md`](./AGENT_COMPUTER_REFERENCE_PROFILE.md)
- **Field-tested working spine:** [`docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md`](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md)
- **Composable workforce catalogue:** [`docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md`](./docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md)
- **Current Wirebot application integration architecture:** [`docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md`](./docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md)
- **Current cross-product gap audit:** [`docs/agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md`](./docs/agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md)

## Purpose

ADLBOS defines the portable laws and deployment doctrine for a human-owned life/business operating system. The Golden Path answers:

> **How does an authorized agent take a real environment from zero or partial state to a working, secure, observable, agent-native, recoverable system using the existing product owners—and prove it works?**

The Golden Path is not another runtime, application, workforce database, task system or commercial tier.

It is the repeatable implementation doctrine for composing the ecosystem correctly.

## Architecture relationship

Current product/system ownership is defined by `CURRENT_ECOSYSTEM_ARCHITECTURE.md`.

The core chain is:

```text
Canonical Owner Principal
        +--> DelegatedHumanPrincipal identities where explicitly granted
        ↓
Operating Partner / Chief of Staff
Wirebot implementation family; customer-named presentation allowed
        ↓
Focusa governed work
Project → Workstream → Foreman → Workpoint
        ↓
Focusa Workforce
operate / steer / inspect workforce
        ↓
UIAI + Veragensia + Pi/agents/workcells
        ↓
Evidence / receipts
        ↓
accepted outcome / W.I.N.S.
```

Optional Startempire Wire federation and MeriFolio portable-trust projections remain outside the private critical execution path unless explicitly engaged.

## Current reconciliation of historical Golden Path material

The detailed Stage 0–8 working spine in `docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md` contains field-derived process, scars, checks, customer setup sequence and real deployment learning. Preserve those operational lessons.

However, some September 10–13 productization assumptions predate the current Wirebot App and Focusa Workforce architecture. When those older passages conflict with current ownership, apply this rule:

```text
CURRENT_ECOSYSTEM_ARCHITECTURE.md
    owns current cross-product/product ownership

02-agent-os-golden-path-ordered-tasks.md
    owns field-tested deployment sequence, scars and operational learning
```

In particular:

- `Startempire-Wire/Wirebot-App` is now the current Wirebot application-family implementation, rather than an unresolved hypothetical app repository;
- Focusa Workforce is the specialist browser-resident workforce-operations surface;
- Wirebot's Workforce Composer designs/commissions roles and assignments; Focusa Workforce operates active governed work;
- a proposed Tauri wrapper may remain a future packaging/support adapter but is not the product identity or architecture root;
- per-client branded routes may present Wirebot App but should not create separate Chief-of-Staff application implementations;
- Operator Deployment is an implementation/deployment offer mapped onto existing dimensions, not a new authority/runtime tier;
- `Sovereign` describes ownership/isolation/authority posture, not automatically DIY, self-hosted, unmanaged or non-networked;
- Startempire Wire federation remains explicit and optional;
- multi-daemon aggregation inside one Operator is called a fleet/aggregation, not sovereign federation;
- legal/business ownership may differ from the day-to-day human operator; bounded human operation must use explicit delegation rather than implied co-ownership.

## Foundational laws

### 1. One source of truth per concern

Before adding storage, workflow, schema or UI state, identify the existing canonical owner.

Other representations are one of:

```text
projection
cache
index
coordination state
evidence
ephemeral runtime state
```

Never create a second mission/work/authority database because a UI needs a convenient model.

### 2. Identity is layered

Keep distinct:

```text
Canonical Owner Principal
Delegated Human Principal
Operating Partner Principal
optional Architecture Authority Principal
worker/agent identity
runtime/session identity
machine/body identity
```

A customer can call their partner `Spock` while the underlying implementation family remains Wirebot. Branding does not grant authority or change canonical identity automatically.

A delegated human operator remains bounded by the owner-issued grant. Operator access is not owner identity and is not architecture authority.

### 3. Composition is not operation

Wirebot/ADLBOS Workforce Composer answers:

```text
What organization/role should exist?
What should it own?
What tools/data/budget/authority should it receive?
```

Focusa Workforce answers:

```text
Who is working?
What are they doing?
What is blocked?
What needs the owner?
What is proven?
Where is it executing?
```

### 4. Chief of Staff is not global Foreman

The Operating Partner owns portfolio-level orientation and delegation.

The Focusa Foreman owns responsibility for one Workstream's state, frontier, delegation and acceptance path.

Broad partner context never implies broad worker disclosure.

### 5. Capability is not authority

Keep separate:

```text
supported
entitled
activated/connected
authorized
consented for this effect
```

Buying or enabling a product must never silently widen runtime authority.

### 6. Federation is explicit

A sovereign Operator remains useful and complete without Startempire federation.

Federation never means pooled private memory, inherited owner authority, ambient files/messages/projects, shared credentials or automatic remote control.

### 7. API/operation complete

Every consequential first-party UI action should map to one canonical versioned operation with API/CLI/tool parity where applicable.

Normal first-party integration must not require computer-use automation. CUA is a fallback for legacy/external systems and an explicit parity defect when used between first-party products.

### 8. Evidence is not outcome

Preserve:

```text
activity
  != Evidence
  != verification
  != settlement
  != accepted life/business outcome
  != portable standing
```

### 9. Secret reference is not secret disclosure

Cross-product operations carry opaque credential-use references or bounded usage grants, not reusable long-lived secrets.

The owning credential/secret authority resolves or denies the reference at execution time.

### 10. Cached projection is not current authority

Actionable shared projections carry explicit schema/version, source revision, time/freshness and replay/idempotency metadata where appropriate.

Stale/expired cached state may be displayed but must be revalidated before a consequential action.

Acknowledging an item in a presenter is not the same as source-domain resolution.

## Golden Path phase contract

Each deployment phase retains the same useful shape:

```text
PURPOSE
INVARIANTS
IMPLEMENTATION
CHECK
GOTCHAS
RECOVERY / ROLLBACK
EXIT CONDITION
```

The field-tested Stage 0–8 spine remains the operational ordering aid:

```text
0 Engage
1 Workstation substrate
2 Operating Partner genesis
3 Cloud landing where applicable
4 Mesh + identity
5 Knowledge + audit
6 Primary runtime/administration cutover
7 Operating plane + workforce
8 Ongoing operation + handoff
```

Actual work follows prerequisites rather than rigid phase numbers.

## Operator Deployment mapping

Operator Deployment is represented by existing independent dimensions:

```text
purchase/participation
runtime isolation
hosting/operation
federation/sharing
interface/access
```

A typical customer Operator deployment may combine:

```text
customer Canonical Owner Principal
+ optional DelegatedHumanPrincipal identities
+ customer-named Wirebot Operating Partner
+ dedicated/private Focusa
+ Focusa Workforce
+ UIAI where entitled/needed
+ private/customer infrastructure
+ optional Veragensia Agent Computers/bodies
+ optional Startempire federation
```

No new mode engine is required.

## Workforce activation path

The canonical organizational path is:

```text
audit / observed deficiency
  → proposed role or staffing change
  → Workforce Composer
  → CRIST / assignment packet
  → owner/governance acceptance
  → Focusa authority/work binding
  → active Workforce projection
  → execution
  → Evidence / receipt
  → accepted outcome
```

Draftees may provide candidates. MeriFolio may later provide portable trust. Neither becomes the local work authority.

## Shared ecosystem contracts

Cross-product seams belong at the ADLBOS portable layer and should be implemented as minimal reference envelopes, not another orchestration service.

Required families are defined in `CURRENT_ECOSYSTEM_ARCHITECTURE.md`:

```text
operator.partner_profile.v1
operator.surface_handoff.v1
operator.attention.v1
operator.correlation.v1
operator.capability_posture.v1
operator.closure.v1
operator.credential_use_ref.v1
```

Product repositories own adapters and behavior behind those references.

Shared actionable envelopes follow the common metadata law from `CURRENT_ECOSYSTEM_ARCHITECTURE.md`: compatibility/version, source, correlation, revision/freshness, expiry where applicable and idempotency/replay semantics for mutations.

## Current phase map

The 0–13 coverage map remains useful:

```text
0  Identity, ownership, deployment profile
1  Environment baseline
2  State ownership
3  Derived state / freshness
4  Human/agent identity, auth, tenancy
5  Agent runtime and execution surfaces
6  Network/routes
7  Discovery/documentation
8  Agent surfaces/interoperability
9  Observability/evidence/cost
10 Secrets/permissions/budgets/revocation
11 Entitlements/licensing
12 Tests/migration/deploy/rollback
13 Launch/acceptance/handoff
```

These are coverage labels, not a second workflow engine.

## Current priorities

The next architectural closures are not additional products. They are seams:

1. Operating Partner principal + white-label presentation;
2. delegated-human principal/grant/revoke proof;
3. Chief-of-Staff → Focusa/Foreman delegation;
4. Workforce Composer → governed assignment → Workforce lifecycle;
5. shared `Needs You` attention projection + source-resolution semantics;
6. exact surface handoff between Wirebot/Workforce/UIAI/Veragensia;
7. cross-product correlation envelope;
8. capability/entitlement/activation posture;
9. opaque credential-use reference path;
10. shared contract compatibility/freshness/replay behavior;
11. Evidence → settlement → accepted outcome/W.I.N.S. closure;
12. sovereign federation account/link/revoke proof;
13. executable Focusa binding for Golden Path/task-ledger work without another task authority.

## Iteration discipline

For each Golden Path improvement:

```text
1. Read current owner/architecture contracts.
2. Inspect actual runtime/product state.
3. Reuse the owning product's primitive.
4. Implement the smallest useful vertical slice.
5. Verify running behavior.
6. Record real scars and recovery lessons.
7. Update the owning document rather than stacking a parallel architecture.
```

Do not preserve obsolete product assumptions merely because they are older. Do not discard proven deployment learning merely because the product surface evolved.

## Completion principle

The Golden Path is successful when a replacement authorized agent can orient from durable state, identify the owner, valid delegated humans and operating partner, discover the applicable products/capabilities, continue governed work through the existing owners, and produce an owner-visible verified outcome without relying on undocumented builder memory or stale cached authority state.
