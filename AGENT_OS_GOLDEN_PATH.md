# Agent OS Golden Path

> A versioned, executable deployment and operations doctrine for turning a fresh environment into a verified, agent-native Life & Business OS.

- **Golden Path version:** `0.1.0-candidate`
- **Foundational contract:** [`AGENTS.md`](./AGENTS.md) — currently `3.3.0`
- **Canonical owner authority:** [`OWNER_AUTHORITY_CONSTITUTION.md`](./OWNER_AUTHORITY_CONSTITUTION.md)
- **Reference Agent Computer profile:** [`AGENT_COMPUTER_REFERENCE_PROFILE.md`](./AGENT_COMPUTER_REFERENCE_PROFILE.md)
- **Current version snapshot:** [`docs/agent-os-golden-path/0.1.0.md`](./docs/agent-os-golden-path/0.1.0.md)
- **Server build-agent handoff:** [`docs/agent-os-golden-path/SERVER_AGENT_HANDOFF.md`](./docs/agent-os-golden-path/SERVER_AGENT_HANDOFF.md)
- **Changelog:** [`docs/agent-os-golden-path/CHANGELOG.md`](./docs/agent-os-golden-path/CHANGELOG.md)

## Purpose

The foundational repository defines *what the Agent-Driven Life & Business OS is and what must remain true*. The Golden Path defines the complementary operational question:

> **How does an authorized agent reliably take an environment from zero or partial state to a working, secure, observable, agent-native, recoverable system — and prove each phase actually works?**

The pattern is inspired by the structural discipline of `burcs.dev/starter`: an end-to-end checklist organized as ordered phases with exact implementation guidance, objective checks, and real failure modes. It is **not** a prescription to copy Burcs' Cloudflare stack. The portable idea is the method.

The Golden Path is therefore both:

1. a concise human-readable operating doctrine; and
2. the upstream specification for increasingly executable installer/doctor/provisioning automation.

## Relationship to the foundational contract

This Golden Path is subordinate to the repository's existing authority, safety, isolation, truth, evidence, and collaboration contracts.

It MUST NOT:

- create a second architecture authority;
- replace Focusa, Agent-KB, UIAI Engine, Veragensia, Wirebot, OpenClaw, or other canonical owners of concerns that already exist;
- turn deployment documentation into canonical runtime truth;
- copy private Startempire/customer state into the portable repository;
- weaken tenant/project/owner isolation to simplify provisioning;
- invent another task, memory, evidence, or mission ledger when a canonical one already exists.

It SHOULD make existing primitives easier for agents to discover, provision, operate, verify, repair, and reproduce.

## Core design principles

### 1. Allowlist, do not rely on denylist

Public surfaces, capabilities, tools, filesystem scopes, network scopes, and mutations are explicit. Nothing becomes reachable or authorized merely because it was not forbidden.

### 2. One source of truth per kind of state

Before adding storage or synchronization, classify the state and name its canonical owner. Other representations must be projections, caches, indexes, evidence, coordination state, or ephemeral runtime state.

Recommended taxonomy:

```text
CANONICAL
DERIVED
CACHE
INDEX
COORDINATION
EVIDENCE
EPHEMERAL
```

Never treat eventual consistency as a hidden substitute for authoritative reads.

### 3. Staging/proving path exists from the beginning

Consequential changes need a bounded non-production or isolated proving route appropriate to the deployment. Production must not be the first place a change is exercised merely because automation can reach it.

### 4. Config is reconstructable; secrets are not committed

Machine-reconstructable identifiers, manifests, service topology, schemas, and non-secret configuration should be versionable where appropriate. Credentials and private runtime data remain in their canonical secret/private stores and are injected or referenced at runtime.

### 5. Boring beats clever

Prefer simple, observable, replaceable components and explicit failure semantics over magical orchestration. Existing primitives beat new frameworks. A recoverable five-step flow beats a sophisticated opaque one.

### 6. Agents are first-class operators and users

Every mature deployment should expose enough machine-readable capability, identity, scope, health, documentation, and recovery information that an authorized replacement agent can orient and operate without undocumented tribal knowledge.

### 7. Checks prove behavior, not paperwork

Every phase has an objective check against the running or built system. A file, route, schema, commit, push, deployment, or agent assertion is not automatically proof of the requested outcome.

## The phase contract

Every Golden Path phase uses the same structure:

```text
PURPOSE
INVARIANTS
IMPLEMENTATION
CHECK
GOTCHAS
RECOVERY / ROLLBACK
EXIT CONDITION
```

A deployment adapter may change commands and products while preserving this contract.

## Current phase map

```text
0  Identity, ownership, deployment profile, domains
1  Scaffold and environment baseline
2  State ownership and canonical stores
3  Derived state, cache, indexes, freshness
4  Human/agent identity, auth, sessions, tenancy
5  Agent runtime and execution surfaces
6  Network, domains, staging and production routes
7  Human + machine discovery and documentation
8  Agent surface and interoperability
9  Observability, evidence, analytics and cost
10 Secrets, permissions, limits, budgets and revocation
11 Entitlements, licensing, billing/BYOK where applicable
12 Tests, migration, CI/CD, deploy, rollback and repair
13 Launch, acceptance, handoff and ongoing operation
```

The normative `0.1.0` candidate is in [`docs/agent-os-golden-path/0.1.0.md`](./docs/agent-os-golden-path/0.1.0.md).

## Versioning model

The Golden Path has its own semantic version stream so it can evolve faster than the foundational OS contract.

- **PATCH (`0.1.x`)** — clarifications, corrected checks, additional gotchas, non-structural refinements.
- **MINOR (`0.x.0`)** — new phase capability, new portable contract, materially improved executable workflow, backwards-compatible profile expansion.
- **MAJOR (`x.0.0`)** — breaking change to phase semantics, state/authority assumptions, or compatibility contract.

Version snapshots under `docs/agent-os-golden-path/` are immutable after they are superseded except for obvious non-semantic repair such as broken links. A new iteration gets a new file and a changelog entry. This root file points to the current candidate/adopted version.

Status vocabulary:

```text
candidate   proposed upstream contract awaiting meaningful live reconciliation
adopted     accepted portable contract
implemented behavior exists in at least one reference environment
verified    behavior has direct acceptance evidence in named scope
deprecated  retained for lineage but no longer current
```

A document version and a deployment's implementation version are distinct. Documentation never proves deployment.

## Iteration loop

Each meaningful iteration follows:

```text
1. Read current Golden Path + foundational authority contracts.
2. Inspect authoritative live environment(s).
3. Reconcile portable doctrine against what actually exists.
4. Reuse existing primitives; identify genuine gaps only.
5. Implement the smallest useful vertical slice.
6. Run behavioral checks and collect evidence.
7. Record real gotchas/recovery lessons.
8. Publish the portable delta as the next Golden Path version.
9. Keep deployment-private details in their proper runtime/knowledge stores.
```

The server agent is expected to improve this artifact, not merely consume it.

## Future executable shape

The Golden Path should progressively become machine-executable without prematurely inventing a framework. A future adapter may expose operations resembling:

```text
agent-os inspect
agent-os plan <profile>
agent-os provision <profile>
agent-os verify <phase|all>
agent-os status
agent-os doctor
agent-os repair
```

These names are illustrative, not currently canonical CLI requirements. First reuse existing Wirebot/Focusa/UIAI/Veragensia/OpenClaw/provisioning/Beads/Agent-KB capabilities. Consolidate only where a stable repeated orchestration gap is proven.

## Immediate next step

The first server-side iteration is defined in [`SERVER_AGENT_HANDOFF.md`](./docs/agent-os-golden-path/SERVER_AGENT_HANDOFF.md): reconcile this `0.1.0` candidate against the real Startempire reference environment and current authorized customer environments, then publish the next version from direct operational knowledge while implementing the smallest high-leverage executable slice.