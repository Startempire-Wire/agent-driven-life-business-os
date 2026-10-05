# Server / Chromebook Build-Agent Handoff — Agent-Driven Life & Business OS

**Status:** CURRENT  
**Audience:** build/operations agents with authorized access to the real server, Chromebook, cloud and customer deployment environments.

## Assignment

Improve and execute the Agent-Driven Life & Business OS using the existing product owners and the current Golden Path. Do not rediscover the architecture from old conversation history or create a parallel system because one seam is incomplete.

Start here:

```text
1. AGENTS.md
2. OWNER_AUTHORITY_CONSTITUTION.md
3. CURRENT_ECOSYSTEM_ARCHITECTURE.md
4. AGENT_OS_GOLDEN_PATH.md
5. docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md
6. docs/agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md
7. the owning product repository/spec for the work you are about to change
```

Historical version docs, audits and Git history remain useful evidence. They do not override the current architecture.


## Current-state versus target-state rule

Agents MUST distinguish three layers before implementation:

~~~text
CURRENT IMPLEMENTED STATE
  code + owning runtime/service + current consumer evidence

CURRENT PLANNING / TARGET STATE
  accepted architecture/specification not yet proven end to end

ORDERED TRANSITION
  existing task/dependency graph + exact missing seams required to move from current to target
~~~

For the new mathematical-intelligence/composable-experience work, read:

~~~text
SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md
Startempire-Wire/Wirebot-App/docs/20-wirebot-intelligence-composition-architecture.md
Startempire-Wire/Wirebot-App/docs/21-wirebot-current-state-to-target-state-handoff.md
Startempire-Wire/focusa/docs/65-visual-ui-focusa-integration.md
~~~

Do not infer implementation from those target documents. Current reality is:

- Wirebot already has a real trusted Focusa/A2UI generated-UI adapter, the pinned 31-component catalog, replay-safe generated-surface handling, explainable layout composition and partial Perpetua/routine/Kaizen contracts;
- Focusa already has governed Context/Evidence/Prediction/Constraint/Trajectory/Workpoint/Metacognition primitives and the trusted generated-UI substrate;
- the new normalized Intelligence Result registry, mathematical engine registry and higher-order Wirebot composition registry are target implementation work, not current product capability;
- the SOVOS routine compiler runtime and steady recurring execution path remain unproven until `SAG-10` and `SAG-18` close with runtime evidence;
- UIAI remains the browser/computer execution and proof owner and must not be replaced by a new SOVOS/Wirebot browser subsystem.

The current task trackers and dependency graphs remain the execution-order authority for implementation. These architecture documents refine the destination and seam contracts; they do not authorize skipping unresolved prerequisites or marking dependent work complete.

When the task changes agent instructions, load-on-trigger skills/procedures or instruction-loading behavior, also read `AGENT_CONTRACT_OPTIMIZATION_PROFILE.md` and run `bash tests/run-contract-tests.sh`. A material semantic change must use held-out behavioral cases that were not used to derive the proposal.

---

## Current architecture

```text
Canonical Owner Principal
        ↓
Operating Partner / Chief of Staff
Wirebot implementation family; customer name may be Spock/etc.
        ↓
OpenClaw
persistent partner runtime / channels / automations on private remote VPS
        ↓
Focusa
Project / Workstream / Foreman / governed work
        ↓
Focusa Workforce
live workforce operations
        ↓
UIAI / Veragensia / Pi / workers / Agent Computers
        ↓
Evidence / settlement
        ↓
source-domain accepted outcome
        ↓
Wirebot/Perpetua private leverage + Quiet Kaizen
        ↓ optional by setup
W.I.N.S. progression / recognition / community projection
```

Startempire Wire federation is optional and outside the private critical path unless explicitly engaged.

Do not conflate:

```text
Operating Partner
with architecture authority

Wirebot
with global Foreman

Workforce Composer
with Focusa Workforce

fleet
with sovereign federation

entitlement
with authority

Evidence
with accepted outcome
```

---

## Product ownership

### Wirebot / Wirebot App

Owns the Operating Partner experience, life/business orientation, Workforce Composer, broad owner conversation, owner-wide Needs You, organization design, network context and owner-facing synthesis/projection. Source business/life domains plus owner acceptance retain outcome truth.

### Focusa

Owns governed work: Project, Workstream, Foreman, Workpoint, authority, Evidence/receipts, continuation/recovery and work settlement.

### Focusa Workforce

Owns specialist live workforce operations: roster, active work, Direction, workforce Needs You, Evidence inspection, execution/topology projection and exact specialist handoffs.

### UIAI Engine

Owns browser/computer observation, actuation, diagnostics, takeover/reconciliation and execution proof.

### Veragensia

Owns Agent Computer/body/runtime identity, placement, enforcement, human control and lifecycle.

### Base outcome / feedback / W.I.N.S.

Source business/life domains and owner acceptance retain outcome truth.

Wirebot/Perpetua owns the private cross-domain feedback/leverage/Quiet Kaizen synthesis.

W.I.N.S. is optional/setup-aware progression, recognition and community projection. Wirebot Sovereign Operator and Wirebot Sovereign remain complete without it.

### MeriFolio

Owns portable worker identity/trust/standing. It is not local workforce authority.

---

## Operator Deployment

Operator Deployment is an implementation/deployment offer, not another runtime or authority class.

A customer deployment may combine:

```text
customer owner
+ customer-named Wirebot Operating Partner on OpenClaw
+ dedicated/private Focusa
+ Focusa Workforce
+ UIAI Engine
+ owner-specific Tailscale private mesh / tailnet
+ dedicated persistent remote VPS for this owner
+ at least one owner-controlled local computer/body joined to the tailnet
+ optional additional Veragensia bodies
+ optional Startempire federation
```

Treat purchase/participation, runtime isolation, hosting/operation, federation and interface as independent dimensions.

Do not infer a deployment mode from one product name, site, server or customer count.

---

# Operating rules

## Outcomes over process

Use:

```text
inspect → reconcile → implement → verify → clean up → continue
```

not:

```text
inspect → plan → document → re-plan → create process about process
```

A failed route/tool is not mission failure when another valid path exists.

Do not stop unrelated productive work because one connector, provider, CLI or host path is unavailable.

## DRY / one owner

Before adding storage/schema/workflow/policy, find the canonical owner.

Do not create duplicate:

- task/work authority;
- role/roster state;
- approval store;
- Evidence ledger;
- entitlement system;
- memory store;
- federation registry;
- conversation authority.

## Security

No raw long-lived secrets, recovery codes, reusable PINs, private keys or customer credentials in repositories, prompts, receipts or logs.

Break-glass authentication resolves through the current deployment secret/verifier mechanism, never an inline value from documentation.

## Delivery truth

A command, commit, route, task closure or agent assertion is not completion.

Verify the actual requested effect at the narrowest practical layer and through a real vertical flow when material.

For agent-contract evolution, derivation/training evidence is not independent proof. Compare the baseline and candidate on held-out representative cases, preserve protected invariants, and re-observe behavior after rollout before calling the change verified.

---

# Real-estate reconciliation

When a task depends on current deployment state, inspect only authorized environments and classify what is actually present.

Relevant systems may include:

```text
Wirebot / current runtime adapter
Wirebot App
Focusa
Focusa Workforce
UIAI Engine
Veragensia / Agent Computers
Pi / build agents
Agent-KB / Context Core / memory owners
Tailscale / network
Cloudflare / DNS
GitHub
credential/vault systems
Beads / GitHub Issues / CallGraphs / task providers
business systems
W.I.N.S.
Startempire federation
```

Classify independently:

```text
installed
configured
reachable
healthy
entitled
authorized
usable
verified
not applicable
unknown
```

Do not turn an observation into enrollment, ownership or authority.

---

# Golden Path execution

Follow the current Stage 0–8 spine:

```text
0 Engage and bind ownership
1 Workstation substrate and secure agent capability
2 Operating Partner genesis
3 Persistent remote VPS + OpenClaw landing
4 Mesh, identity and reachable execution bodies
5 Knowledge, portfolio/business audit and system map
6 Primary administration/runtime cutover
7 Operating plane and workforce commissioning
8 Ongoing operation, outcomes and handoff
```

Use dependencies rather than blindly following stage numbers.

The current working spine is `02-agent-os-golden-path-ordered-tasks.md`; do not create another parallel process doc.

---

# Workforce path

When an audit identifies a recurring capability/role gap:

```text
portfolio/business/life evidence
→ routine / deficiency / leverage inference
→ routine blueprint
→ Wirebot recommendation
→ Workforce Composer
→ CRIST / assignment packet
→ owner/governance acceptance
→ Focusa Project / Workstream / Foreman / authority binding
→ Focusa Workforce projection
→ worker execution
→ Evidence / settlement
→ accepted outcome
```

Do not directly spawn a broadly privileged “employee” from a role title.

Profiles are templates. Assignments bind real scope and authority.

---

# Shared seam contracts

Cross-product joins belong to ADLBOS reference envelopes:

```text
operator.environment.v1
operator.partner_profile.v1
operator.surface_handoff.v1
operator.attention.v1
operator.correlation.v1
operator.capability_posture.v1
operator.closure.v1
operator.routine_blueprint.v1
operator.leverage_snapshot.v1
```

Implement the minimum seam exercised by the current vertical slice. Do not build a new centralized integration service merely to host these refs.

---

# Current priority gaps

Use `11-agent-os-golden-path-seamless-autonomy-gap-audit.md` as the current gap owner.

Important current seams include:

```text
Operating Partner principal/presentation
cross-product account/link/revoke
Workforce Composer assignment schemas/compiler
Chief-of-Staff → Focusa/Foreman delegation
shared Needs You attention
exact surface handoff
universal correlation refs
capability/entitlement posture
Evidence → settlement → source outcome → base leverage closure → optional W.I.N.S. projection
worker/partner memory isolation
sovereign federation proof
Golden Path/task tracker → Focusa executable binding
```

Do not create another backlog for the same gaps.

---

# Task trackers and Focusa

Beads, GitHub Issues and other trackers may hold legitimate project/implementation state.

They do not automatically become Focusa's governed work authority.

Where a tracker/CallGraph is the approved executable task source, preserve stable refs and bind it into the exact Focusa project/continuity rather than reproducing the plan in multiple stores.

---

# Chromebook / cloud topology

Treat the Chromebook and cloud/server agents as one development topology sharing authoritative Git repositories.

Chromebook strengths:

```text
UI/UX dogfood
browser extension behavior
voice/interaction testing
lightweight implementation
```

Cloud/server strengths:

```text
heavy builds/tests
runtime/services
multi-agent implementation
Veragensia/UIAI integration
deployment
```

Do not create Chromebook-only and server-only source forks.

---

# Product application direction

Wirebot App is the current owner-facing application family.

Older Tauri-wrapper and bespoke per-client Svelte CoS assumptions are historical design input, not current product ownership.

Tauri may be used later as a packaging/support adapter if justified.

A customer-branded domain should normally present the same Wirebot App family with that customer's partner identity, not a separate CoS implementation.

Focusa Workforce remains the specialist workforce browser surface.

---

# Federation

Reserve `federation` for independent sovereign participants.

One Operator's multiple machines/daemons/bodies form a fleet.

Federation must be explicit, scoped and revocable. It never implies pooled memory, shared credentials, ambient project access, UIAI control or inherited owner authority.

---

# Completion standard

A server/build-agent task is complete when:

1. the requested real behavior exists;
2. the owning runtime/product confirms the relevant state;
3. denied/stale/unknown states remain truthful;
4. no duplicate authority/state was created;
5. tests/build and relevant live vertical flow pass;
6. current docs were updated if the architecture/contract changed;
7. temporary branches/workflows/files created for the task are removed;
8. the next agent can continue from durable state without relying on this agent's memory.

> **Leave the environment cleaner and more coherent than you found it. Do not hand the owner cleanup you created and could finish yourself.**
