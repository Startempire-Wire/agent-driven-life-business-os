# Golden Path — Current Interwoven Deployment Doctrine

**Status:** CURRENT iterable Golden Path spine targeting `0.2.1-candidate`<br>
**Reconciled:** 2026-09-27<br>
**Architecture authority:** `../../OWNER_AUTHORITY_CONSTITUTION.md`  
**Current ecosystem ownership:** `../../CURRENT_ECOSYSTEM_ARCHITECTURE.md`  
**Historical lineage:** `0.1.0.md`, `0.1.1.md`, Git history before this reconciliation

This is the current field-derived process an authorized agent follows to build, reconcile, operate and hand off a Human Life & Business Agent OS deployment.

It preserves the deployment sequence and scars learned through the first customer deployments while aligning product/application ownership with the current architecture.

It does **not** create another runtime, application, task database, workforce database or entitlement model.

---

## 0. Locked invariants

Every iteration derives from these laws.

### Agent-operated setup

The agent inspects, executes, verifies and recovers through existing product/tool owners.

The owner supplies:

- goals and desired outcomes;
- business/life truth unavailable elsewhere;
- consequential choices;
- reserved-power approvals;
- corrections.

Do not make the owner execute routine commands an authorized agent can perform itself.

### Brownfield first

Start from what the customer actually has.

Never assume:

```text
clean machine
empty accounts
one computer
one cloud
one provider
one website
one mailbox
one exact topology
```

Distinguish:

```text
pre-existing
configured
reachable
healthy
usable
entitled
authorized
verified
newly created
```

### Reuse first

Existing owners remain owners.

Typical reference mechanisms include:

```text
Wirebot / Operating Partner runtime
Focusa
UIAI Engine
Veragensia / Agent Computers
Pi / compatible build agents
Tailscale
GitHub
Cloudflare
credential/vault tooling
Google/business-system adapters
Agent-KB / knowledge systems
W.I.N.S.
```

The Golden Path composes them. It does not replace them.

### Deterministic versus probabilistic work

Classify each operation by its true shape.

**Deterministic:** use owning code/API/CLI/form contracts; run idempotently where possible; verify output.

**Probabilistic:** keep agent judgment for interviews, ambiguous browser flows, audit significance, role design, exception recovery and other genuinely uncertain work.

Do not use an LLM to repeatedly improvise stable deterministic work that should have an owning adapter.

### Agent-operation complete

First-party applications should expose canonical structured operations. Normal first-party integration is:

```text
canonical API / CLI / typed operation
→ semantic platform interface where needed
→ computer use as final fallback
```

UIAI computer use is essential for external/legacy applications; it is not an excuse for missing first-party operations.

### Evidence over claims

A command returning zero, an agent saying “done,” a route existing, or a UI rendering is not sufficient completion evidence by itself.

The expected real effect must be verified.

---

# The deployment spine

```text
Stage 0  Engage and bind ownership
Stage 1  Workstation substrate and secure agent capability
Stage 2  Operating Partner genesis
Stage 3  Cloud/private execution landing where applicable
Stage 4  Mesh, identity and reachable execution bodies
Stage 5  Knowledge, business audit and system map
Stage 6  Primary administration/runtime cutover
Stage 7  Operating plane and workforce commissioning
Stage 8  Ongoing operation, outcomes and handoff
```

Stages are dependency guides, not rigid calendar phases. Work can proceed in parallel when prerequisites do not conflict.

Each stage follows:

```text
PURPOSE
→ STEPS
→ OWNER MECHANISMS
→ CONSENT / AUTHORITY
→ SCARS / DEFAULTS
→ CHECK
→ EXIT
```

---

# Stage 0 — Engage and bind ownership

## Purpose

Establish who owns the deployment, what outcome matters, what systems are in scope, and which owner moments are genuinely required.

## Steps

1. Establish the deployment's `CanonicalOwnerPrincipal`.
2. Identify business/legal owner and primary human operator where those differ.
3. Record the first useful outcome the deployment should produce.
4. Define explicit exclusions and reserved powers.
5. Establish spend/hosting/provider constraints.
6. Map high-consequence consent moments before implementation.
7. Identify whether the engagement is private, network-enabled, managed, customer-owned, or some combination of independent dimensions.
8. Define whether an Operating Partner already exists or will be created.

## Owner mechanisms

Use the ADLBOS owner-authority contract plus the engagement/customer systems that already own commercial/legal consent.

Operator Deployment is an **offer/implementation profile**, not a new runtime identity.

## Consent / authority

The owner supplies values, goals, private business truth and consequential approvals.

Do not treat:

```text
payment
repository access
root access
support contract
network membership
```

as blanket execution or architecture authority.

## Scars / defaults

### Too many owner interruptions

Default: identify owner moments early, batch them when safe, and let agents handle routine setup.

### Vague “build me an AI system” engagements

Default: name one initial business/life outcome and its acceptance before expanding scope.

### Confusing product purchase with runtime permission

Default: keep support, entitlement, activation, authority and consent distinct.

## Check

A replacement agent can answer:

```text
Who owns this deployment?
What is the first desired outcome?
What is explicitly out of scope?
Which choices require the owner?
What commercial/runtime/federation posture applies?
```

## Exit

Owner, objective, constraints and consent plan are explicit enough to start substrate work without guessing authority.

---

# Stage 1 — Workstation substrate and secure agent capability

## Purpose

Make the customer's existing computer usable as an agent-operated starting body while preserving honest capability/trust boundaries.

## Steps

1. Audit OS/platform, resources, package managers, network/DNS/time posture and existing tools.
2. Install only missing approved base prerequisites through owning installers/package managers.
3. Establish the selected model/provider access through renewable approved auth.
4. Establish Pi/reference build-agent access where applicable.
5. Install/pair Focusa according to current owning contracts.
6. Install/pair UIAI early enough that agents can perform browser/computer workflows where structured APIs are absent.
7. Establish GitHub and Cloudflare tooling when required by the engagement.
8. Establish vault/credential retrieval through approved secret-safe paths.
9. Consolidate scattered credentials only through owner-approved credential custody; never copy recovery codes into agent context.
10. Capture a bounded machine/capability report.

## Owner mechanisms

```text
OS/package manager
Pi/reference harness
Focusa
UIAI Engine
GitHub
Cloudflare
credential/vault authority
Golden Path diagnostic scripts
```

## Consent / authority

Secret entry may be owner-typed into an isolated trusted context when necessary.

Never automate recovery codes or other nonrenewable break-glass resources.

## Scars / defaults

### Missing terminal / Node / Git / CLI prerequisites

Default: preflight and install deterministic base prerequisites before heavier product setup.

### AV/script friction

Default: prefer signed/product-owned installers or standard package managers; do not respond by weakening host security broadly.

### “CLI missing” incorrectly interpreted as “runtime missing”

Default: runtime/service health and local CLI presence are different states. Do not install duplicate local services when a healthy remote runtime is already the intended topology.

### Secrets scattered across browser/password manager/sticky notes

Default: consolidate under the customer's approved credential owner; use refs/scoped use rather than prompt-visible values.

### Computer-use optimism

Default: test real representative browser/computer capabilities; do not infer “can do everything a human can” from one successful action.

## Check

For each required capability classify:

```text
not required
missing
installed
configured
reachable
healthy
usable
authorized
verified
```

A representative agent operation and one representative browser/computer action succeed under intended scope.

## Exit

The starting body can participate safely in the rest of the build, or the documented plan routes heavy/missing capability to a remote body.

---

# Stage 2 — Operating Partner genesis

## Purpose

Create or bind the customer's persistent Operating Partner relationship without conflating that identity with its current runtime.

## Steps

1. Establish `OperatingPartnerPrincipal` under the customer owner.
2. Configure customer-selected presentation identity/name/voice profile as desired.
3. Bind the Wirebot Operating Partner to its OpenClaw runtime path and verify the tenant/runtime binding.
4. Create a git-backed source/config workspace where source belongs in Git.
5. Bind current customer/deployment references rather than hardcoding Startempire identity.
6. Begin CRIST/business orientation for the first useful outcome.
7. Establish the initial owner-facing Wirebot App route/surface.
8. Verify partner identity survives restart/runtime changes.

## Current architecture correction

The customer-facing application family is **Wirebot App**.

Do not create a separate bespoke Svelte Chief-of-Staff application for each customer merely because the customer has a custom domain.

A branded route such as:

```text
spock.customer.example
```

may project the same Wirebot App family with the customer's partner presentation.

Older Tauri-wrapper proposals remain packaging/support history. Tauri may later be used where appropriate, but packaging technology does not define the Operating Partner or app architecture.

## Owner mechanisms

```text
Wirebot / Wirebot App
OpenClaw persistent Operating Partner runtime
Git
ADLBOS partner identity contract
knowledge/context systems
```

## Consent / authority

The customer may choose partner name/personality/presentation.

That choice does not grant architecture authority.

## Scars / defaults

### Partner identity tied to one runtime

Default: partner identity is durable; the OpenClaw **runtime incarnation/host**, Pi worker, model and individual VPS host are replaceable. OpenClaw as the persistent Operating Partner runtime layer is foundational in the current ADLBOS topology.

### Customer-specific UI fork

Default: one application family, configurable presentation and entitled modules.

### Workspace copy-paste loses history

Default: source moves through Git; private runtime state moves through owning mechanisms.

## Check

The owner can interact with the correct named partner through Wirebot App, and the runtime can restart/move without creating a different partner identity.

## Exit

A persistent customer-owned partner relationship exists with source/runtime boundaries documented.

---

# Stage 3 — Persistent remote execution landing

## Purpose

Establish the always-available remote execution/scheduling body required by the current ADLBOS operating topology.

Every production Operator topology includes at least one persistent remote VPS reachable through the private Tailscale mesh. The VPS may be shared/managed, customer-owned, operator-managed or dedicated/Sovereign according to the deployment contract; the requirement does not imply one dedicated machine per customer.

Additional cloud capacity, extra Agent Computers and heavy-compute workers remain demand-driven rather than copied from a reference estate.

## Steps

1. Determine the exact managed/shared/dedicated remote execution topology.
2. Create or verify the persistent remote VPS/body and renewable authentication.
3. Install/verify the OpenClaw Gateway/runtime and built-in Automations scheduler on the intended always-on body.
4. Establish Tailscale private-network posture before sensitive administration.
5. Pair/verify Focusa and UIAI routes needed by the deployment without treating reachability as authority.
6. Provision only additional resources required by actual workload.
7. Configure DNS/public routing only for intended product/app needs.
8. Establish backup/recovery before cutover.
9. Verify cost/resource posture and replacement/restore path.

## Owner mechanisms

Provider APIs/CLI, OpenClaw Gateway/Automations, Focusa, UIAI Engine, Tailscale/private network, Veragensia/Agent Computer contracts where applicable, DNS owner.

## Scars / defaults

### Reference topology copied blindly

Default: capability/need determines topology, not historical server shape.

### Public exposure before private control path

Default: private administration first; expose only intended customer/public surfaces.

### Cloud capacity treated as authority

Default: compute capacity and work authority are independent.

## Check

Remote body/runtime is reachable through the intended private path, correctly identified, and within resource/spend policy.

## Exit

The required cloud/private execution body exists and is safe to enroll into the deployment.

---

# Stage 4 — Tailscale mesh, identity and reachable execution bodies

## Purpose

Connect the customer's approved machines and runtimes without confusing reachability with ownership or authority.

## Steps

1. Establish/verify the Operator's Tailscale private mesh and enroll relevant approved machines/nodes.
2. Record stable node/body/runtime refs through owning systems.
3. Verify administration paths in both directions where required.
4. Pair Focusa/UIAI/Veragensia surfaces according to their contracts.
5. Distinguish integrated computers from Full Agent Computers.
6. Verify one representative remote execution path.
7. Record unavailable/offline/not-applicable devices honestly.

## Terminology

One customer's nodes form a **fleet / multi-daemon aggregation**.

Do not call this federation.

`Sovereign federation` is reserved for explicit cross-Operator/network sharing.

## Scars / defaults

### Machine hash treated as customer identity

Default: machine/node identity is runtime evidence, not proof of customer ownership or enrollment.

### Reachable means authorized

Default: network reachability is transport capability only.

### Chromebook treated as Full Agent Computer

Default: show actual integration/trust/enforcement profile. Rich integration does not imply full Veragensia enforcement parity.

## Check

The Operating Partner can identify and reach intended bodies through approved routes, while an unapproved route/body cannot exercise work merely because it is on the network.

## Exit

The execution fleet is reachable, identified and bounded correctly.

---

# Stage 5 — Portfolio knowledge, life/business audit and system map

## Purpose

Understand the owner's real portfolio of businesses, products and life domains—their goals, processes, data, people, obligations, opportunities and recurring work—before inventing workforce structure. Multiple businesses are normal; no audit or UI may assume a single primary business is the complete operating scope.

For a full-surface customer audit, use the [Business Discovery Audit and Workforce Inference procedure](./12-full-surface-business-discovery-audit-and-workforce-inference.md). Its source-coverage manifest, business/asset matrix, contradiction register and guarded workforce proposal are Stage 5 outputs, not permission to activate agents or schedules. Read-only discovery and private client scope remain the defaults.

## Steps

1. Inventory business/life systems and canonical record owners.
2. Connect approved data sources through scoped adapters.
3. Audit documents, calendars, correspondence, projects, customers, operations and existing workflows as applicable.
4. Interview the owner for undocumented processes, preferences, tribal knowledge and priorities.
5. Separate facts, unknowns, assumptions and recommendations.
6. Classify repeated work by shape:
   - deterministic procedure;
   - scheduled process;
   - recurring judgment/coordination;
   - bounded temporary project;
   - human-only/reserved work.
7. Identify high-leverage deficiencies and opportunities.
8. Map canonical state ownership/freshness/retention.
9. Compile each material recurring pattern into a source-backed routine blueprint before deciding whether it should become software, a schedule, an agent responsibility or a human-reserved step.
10. Feed routine blueprints and candidate workforce requirements into the Wirebot Portfolio Operating Compiler / Workforce Composer rather than directly spawning broad agents.
11. Attach a measurement plan so activation can later compare real outcomes, owner attention, reliability, cost and leverage against a baseline.

## Owner mechanisms

```text
Wirebot / partner context
Agent-KB / source-aware knowledge
business-system APIs
Google/business adapters
Focusa project/work context
Golden Path audit
```

## Scars / defaults

### “Installed tools” used as role eligibility

Default: installed/reachable tools do not imply an employee may use them.

### General personal/business memory handed to every worker

Default: worker context is scoped by role/assignment/Workstream. Partner-wide memory stays private unless explicitly projected.

### Audit produces another permanent database

Default: store durable facts in their owning systems and retain provenance refs; no synchronization store merely for the audit.

## Check

The system can explain:

```text
what the customer is trying to achieve
which systems own which truth
which repeated workflows exist
which capability/role gaps matter
which data is private or restricted
which findings remain uncertain
```

## Exit

There is enough real context to commission governed work without guessing the business.

---

# Stage 6 — Primary administration/runtime cutover

## Purpose

Move persistent administration/execution to its intended primary runtime without resetting partner/work identity or losing rollback.

This may mean moving an Operating Partner runtime to a VPS, adopting a cloud Agent Computer, or another topology selected by current requirements.

## Steps

1. Verify source state is committed/backed up.
2. Provision/verify destination runtime.
3. Transfer source through Git and private state through its owning mechanisms.
4. Establish a fresh runtime incarnation/body binding.
5. Reissue applicable credentials/grants rather than copying stale leases blindly.
6. Verify private mesh/admin routes.
7. Cut over explicitly.
8. Retain source body/runtime as rollback until destination proof passes.
9. Verify Wirebot App/customer route continues to represent the same Operating Partner.

## Current application rule

Do not treat a customer subdomain as a separate Chief-of-Staff product implementation.

Use the current Wirebot App family with customer presentation/routing unless a future owner-approved architecture deliberately defines another product.

## Scars / defaults

### Copy-paste migration

Default: Git for source; owner-specific state migrates via owning service/export/transfer contracts.

### “Which runtime is primary?” ambiguity

Default: explicit cutover and rollback point.

### Stale browser/control leases copied between bodies

Default: fresh runtime incarnation, re-observation and reissuance of body/runtime-specific authority.

## Check

From the primary runtime, the partner can reach required enrolled bodies/services and complete one bounded governed action. The owner-facing app still resolves the same partner identity.

## Exit

Primary administration/execution posture is explicit and verified.

---

# Stage 7 — Operating plane and workforce commissioning

## Purpose

Turn the audited system into a real operating organization: recurring workflows, governed roles, temporary workers, scheduled work and owner-visible results.

## Steps

### 7.1 Owner operating rhythm

Configure the partner to produce useful recurring orientation such as:

```text
priorities
important changes
blocked work
decisions that genuinely need the owner
verified recent outcomes
resource/spend exceptions
opportunities
```

### 7.2 Portfolio Operating Compiler / Workforce Composer

Translate the multi-business/life-domain audit into proposed routines, systems, roles and teams.

The compiler first asks what should become deterministic software, what should remain agentic judgment, what requires UIAI computer work, and what should remain human-reserved. Roles are derived from grouped responsibilities; the UI should not make the owner invent an agent org chart from scratch.

For each role/assignment define:

```text
objective
supervisor / Foreman relationship
CRIST context / interview disposition
spec / task pack
capabilities/tools
data scope
credential requirements
autonomy ceiling
budget/spend
activation mode
lifetime / expiry
acceptance/evidence
escalation/revocation
```

A role/profile is not authority.

Each material routine also carries portfolio/business/life-domain scope, desired outcome, source-backed trigger/frequency, ordered step classes, deterministic operation refs, agent/task-pack refs, UIAI requirements, human-reserved gates, execution placement, reliability policy, measurement baseline and keep/improve/retire criteria.

### 7.3 Governed binding

After owner/governance acceptance:

```text
assignment
→ Focusa Project / Workstream
→ Foreman
→ exact authority/capability refs
→ worker/session/runtime execution
```

Focusa Workforce then becomes the live operations surface.

### 7.4 Activation modes

Use the work's natural shape:

```text
fixed deterministic schedule
→ OpenClaw Automations on the persistent remote VPS invoking/revalidating an approved Focusa assignment

recurring judgment or multi-system coordination
→ durable staff profile / Operating Partner delegation

bounded one-off work
→ temporary worker/session with expiry

parallel project effort
→ Foreman-managed crew / Focusa graph/fanout

human-only occasional step
→ documented owner procedure / attention item
```

A schedule is not blanket authority. OpenClaw owns the durable scheduling/runtime record; Focusa owns whether the referenced work remains authorized; UIAI owns any browser/computer action the run later requires.

### 7.5 Voice/presentation

Configure customer voice/style/presentation where desired. Style profile is not authority or identity proof.

### 7.6 Workflow acceptance tests

For material recurring workflows, preserve representative customer-specific examples and expected outcomes.

Changes to model/tool/process should rerun relevant examples before they silently break the customer's workday.

For material agent-contract, skill or instruction-placement changes, separate derivation examples from held-out regression examples under `AGENT_CONTRACT_OPTIMIZATION_PROFILE.md`; a case used to derive the change is not independent validation.

## Owner mechanisms

```text
Wirebot App / Workforce Composer
Focusa
Focusa Workforce
Pi / compatible agents
UIAI
Veragensia bodies
OpenClaw Automations / persistent remote VPS
provider/business systems
W.I.N.S. outcome, momentum and leverage projection
```

## Scars / defaults

### Employee has ambient tools

Default: no employee exists operationally without an explicit role/assignment packet and bounded capabilities.

### Scheduled routine silently dies

Default: use OpenClaw persisted Automations/run history plus typed missing-run/overlap/retry visibility, source-qualified attention and Focusa revalidation. Do not hide a failed schedule behind an "active" UI toggle.

### New model silently changes workflow

Default: acceptance examples and current evidence before rollout.

### Manager authority recursively expands

Default: delegated subsets cannot exceed parent grants; fanout/resource limits remain bounded.

### Workforce UI becomes another planner/database

Default: Focusa remains governed work authority; Workforce is projection/intent client.

## Check

Prove at least one real workflow end-to-end:

```text
trigger / owner delegation
→ Operating Partner / assignment
→ Focusa Workstream / Foreman
→ worker executes through allowed tools/body
→ Evidence / receipt
→ owner-visible result
```

Also prove a denied action outside the worker's role.

## Exit

The first real workload operates with evidence, bounded authority and owner-visible collaboration.

---

# Stage 8 — Ongoing operation, outcomes and handoff

## Purpose

Transition from build-out to daily value while preserving recoverability and independence from the original builder's memory.

## Steps

1. Operate routine work under current policy/authority.
2. Surface `Needs You` only for real owner comparative advantage.
3. Reconcile spend/resources.
4. Verify outcomes, not activity counts.
5. Record accepted outcomes through W.I.N.S. where applicable.
6. Derive source-backed routine/business/portfolio analytics without moving canonical telemetry into a new database.
7. Measure momentum and leverage: owner time/capacity bought back, cycle/reliability improvement, cost/risk reduction, reuse and new opportunity unlocked.
8. Run Quiet Kaizen / optimization against those observations: simplify/delete before adding automation, and retain only measured improvements.
9. Capture reusable improvements only after they prove useful; propagate reusable capabilities across businesses without double-counting benefits.
10. Retire temporary workers/routines that do not help and revoke expired grants/schedules.
11. Keep documentation/current owner maps up to date.
12. Run the replacement-agent test.
13. Maintain optimization loop and incident/recovery routes.

## Shared attention model

Owner decisions should converge into source-bearing attention refs across Wirebot, Focusa Workforce, UIAI and Veragensia rather than invisible separate queues.

## Evidence/outcome law

```text
activity
!= Evidence
!= verified Evidence
!= settlement
!= accepted outcome
```

The owner should see the effect that matters to them, not merely internal agent throughput.

## Replacement-agent test

From documented entry points alone, a fresh authorized agent must be able to:

1. resolve the owner and Operating Partner;
2. understand current deployment posture;
3. discover relevant capabilities/health;
4. find current governed work;
5. complete one representative maintenance/operational action;
6. verify the result;
7. avoid relying on undocumented builder memory.

## Scars / defaults

### “Working system” depends on original builder

Default: durable state, current docs, exact refs, receipts and replacement-agent proof.

### Agent activity mistaken for customer value

Default: owner-benefit view emphasizes accepted outcomes, effort saved and remaining friction.

### Temporary workers never retired

Default: expiry, access revocation, receipt preservation and residual-state scan.

## Check

The replacement-agent test passes and the owner sees at least one accepted useful outcome through the normal product surfaces.

## Exit

The customer operates the system as an ongoing Life & Business OS rather than an unfinished setup project.

---

# Coverage map

The historical 0.1.0 phase coverage remains useful as a completeness index:

| Phase | Current coverage |
|---|---|
| 0 Identity/owner/profile | Stage 0 + Operating Partner binding |
| 1 Scaffold/baseline | Stages 1–2 |
| 2 State ownership | Stages 2, 5, 6 + current ecosystem owner map |
| 3 Derived/freshness | Stages 1, 5, 8 |
| 4 Identity/auth/tenancy | Stages 0, 4, 7 |
| 5 Agent runtime/surfaces | Stages 1–7 |
| 6 Network/routes | Stages 3–6 + optional sovereign federation |
| 7 Discovery/documentation | Stages 1, 5, 8 |
| 8 Agent surfaces | Wirebot App, Focusa Workforce, Focusa Desktop, UIAI, Veragensia according to ownership |
| 9 Observability/evidence/cost | Stages 0, 7, 8 |
| 10 Secrets/permissions/revocation | Stages 0–1, 7–8 |
| 11 Entitlements/licensing | Independent capability/entitlement posture across all stages |
| 12 Tests/deploy/rollback | Per-stage checks + product release paths |
| 13 Launch/acceptance/handoff | Stage 8 |

This table is coverage, not another scheduler.

---

# Current execution task map

The current detailed gap owner is:

```text
11-agent-os-golden-path-seamless-autonomy-gap-audit.md
```

Highest-priority seams include:

```text
Operating Partner machine identity/presentation
cross-product identity/link/revoke
Workforce Composer assignment schema/compiler
Chief-of-Staff → Focusa/Foreman delegation
shared Needs You / attention
exact surface handoff
universal correlation refs
capability/entitlement posture
Evidence → settlement → W.I.N.S. closure
worker/partner memory isolation
sovereign federation proof
Golden Path/task-ledger → Focusa executable binding
```

Do not duplicate these into a second backlog.

---

# Optimization loop

Use:

```text
Observe portfolio/business/routine reality
→ measure accepted outcome + operating burden
→ identify dominant constraint
→ delete/simplify before automating
→ implement the smallest leverage move
→ pilot / compare against baseline
→ verify outcome + capacity/reliability effect
→ keep / improve / retire
→ reuse across routines/businesses where valid
→ capture the next compounding opportunity
```

The loop must improve customer outcomes or system reliability, not manufacture process work.

For agent-contract or load-on-trigger procedure evolution, expand the same loop without creating a second learning system:

```text
observe operating evidence
→ attribute owner / cause / correlation
→ consolidate independent recurrence
→ stage the smallest candidate delta
→ protected-invariant checks
→ held-out baseline vs candidate comparison
→ required owner / architecture gate
→ narrow rollout
→ observe real behavior
→ keep / improve / revert
→ encode only the reusable lesson
```

Raw session count is not independent corroboration: observations from one causal incident share one correlation identity. Low frequency, token cost, one ignored rule or one failed session never by themselves justify weakening/removing a constitutional, safety/authority or architecture-boundary rule. Product-local findings route to their canonical owner.

Useful periodic questions:

```text
What owner attention was avoidable?
What blocked the workforce?
What recurring work should become a typed assignment?
What tool/API gap forced CUA?
What capability/entitlement gap limited value?
What verification failed or was missing?
What improvement can be reused across Operator deployments?
```

---

# Current productization law

Historical packaging/economic experiments remain in Git history and historical version docs.

Current architecture law is:

```text
Wirebot App
  current owner-facing application family

Focusa Workforce
  specialist workforce browser operations surface

Focusa / UIAI
  independent sovereign component products according to their current licenses/contracts

Operator Deployment
  implementation/deployment offer using the existing architecture

Tauri
  optional future packaging/support technology where useful,
  not a product-identity or architecture boundary

customer custom domain
  presentation/routing for the same app family by default,
  not a separate CoS application
```

Commercial pricing/support terms should be maintained in the current owning commercial/product source, not embedded as architecture invariants in this deployment spine.

---

# Definition of Golden Path success

A deployment is meaningfully successful when an authorized replacement agent can follow this causal chain without hidden builder knowledge:

```text
owner
→ Operating Partner
→ accepted role/assignment or owner delegation
→ Focusa Workstream / Foreman
→ bounded worker/runtime/body
→ exact execution
→ Evidence
→ settlement
→ accepted owner-visible outcome
```

and the system can prove:

- denied work stays denied;
- stale/unknown state is shown honestly;
- entitlement does not become authority;
- worker context does not become partner-wide memory;
- federation does not expose private state by default;
- a human takeover reconciles before autonomous continuation;
- bodies/runtimes can change without resetting partner/work identity;
- recovery/rollback paths remain usable;
- no parallel authority store was introduced for convenience.
