# Agent Computer Reference Profile

**Status:** portable reference integration contract, 2026-09-04.
**Architecture authority:** deployment Canonical Owner Principal under `OWNER_AUTHORITY_CONSTITUTION.md`.
**Startempire binding:** Verious Smith III.

## 1. Purpose

The Agent-Driven Life & Business OS uses Veragensia as its reference Agent Computer implementation. This document records the **portable composition relationship** without duplicating Veragensia's detailed architecture.

For Startempire, the canonical detailed specifications live in `Startempire-Wire/veragensia`, especially:

- Doc 182 — product/root composition;
- Doc 190 — agent-first software, Agentability and capability resolution;
- Doc 191 — Elastic Agent Computing and Cloud Agent Computer runtime;
- Doc 192 — telemetry and improvement plane.

A client deployment may replace products while preserving the portable contracts in this repository.

## 2. Deliberately listed reference defaults

A supported full Startempire Veragensia Agent Computer deliberately composes:

1. **Focusa daemon/core** — scoped cognition, ProjectIdentity, Trajectory, Workpoints, Context Authority, Evidence, receipts, learning and recovery.
2. **Focusa Desktop** — default governed human work/cognition presenter over Focusa authority.
3. **Pi + Focusa Pi extension** — default/reference Focusa-aware agent harness integration. Pi is fundamental to the reference Focusa agent experience but is not a second cognitive authority.
4. **UIAI Engine + Cockpit/browser surfaces** — canonical first-party browser/computer execution, observation, diagnostics, operator oversight and proof stack. UIAI is deliberately listed; it is not merely an optional browser candidate in the reference composition.
5. **Veragensia session/shell integration** — host Agent Computer lifecycle, application composition, interruption, containment, review and recovery.

This list is a reference implementation binding, not portable vendor vocabulary. The portable requirement is that the deployment provide equivalent governed work presentation, agent harness, computer/browser execution, authority/evidence, and host lifecycle contracts.

## 3. Authority boundaries

The composition does not collapse authority:

```text
Canonical Owner Principal
    constitutional architecture authority

Focusa daemon/core
    scoped cognitive/operational authority

Focusa Desktop
    presenter over Focusa operations

Pi
    reference harness-edge consumer/producer

UIAI Engine
    browser/computer runtime authority in its execution domain

Veragensia
    Agent Computer host/integration substrate
```

A UI, harness, runtime, repository, service account or deployment does not gain constitutional authority merely because it is a default component.

## 4. Agent-first software doctrine

The reference Agent Computer prefers:

```text
structured capability
→ semantic application automation
→ visual computer use
```

Full computer use remains required because real life/business work includes legacy, unfamiliar and non-API applications.

Default application selection should optimize for **agentability** as well as human usability. A good Agent Computer application exposes stable machine-operable state, typed/structured actions where possible, clear authority boundaries, inspectable outcomes, and Evidence/receipt paths.

The detailed Agentability classes and resolver belong to Veragensia Doc 190. This portable repository should not fork them into an incompatible local taxonomy.

## 5. Capability-first profiles

Life/business roles should request capabilities rather than hardcode packages wherever practical.

For example:

```yaml
role: client-onboarding-specialist
needs:
  - browser_work
  - correspondence
  - scheduling
  - document_editing
  - crm
```

The Agent Computer may satisfy those needs using desktop-native applications, Agent Apps, web applications through UIAI, headless services, or remote specialist runtimes according to policy and platform.

Exact application pins remain valid when a workflow/customer requires them.

## 6. Elastic workforce relationship

A request such as:

> Give this project another team.

may resolve into a mixed Veragensia topology:

- additional Focusa Silent Sessions;
- headless workcells;
- browser execution contexts;
- Agent Apps;
- a full Cloud Agent Computer;
- or a combination.

The Chief of Staff/workforce layer requests outcomes/capability. It should not need to manually design VM/container topology.

Infrastructure placement never grants broader business or application authority.

## 7. Human/agent collaboration

The reference Veragensia implementation may provide Agent Assist modes such as observe, guide, shared control and delegated control.

Portable invariant: any collaborative computer session must bind the actor, task/work unit, machine/runtime, capability/authority, observation/action scope, revocation and Evidence/receipt posture.

Remote-control transport is not permission.

## 8. Software catalog boundary

The exact best applications for coding, office work, notes/knowledge, communications, meetings, CRM, finance, media, data and vertical workflows are deliberately not frozen here.

Future software evaluation should choose applications using measured agentability, human quality, portability, privacy, isolation, resource use, licensing and accepted-outcome evidence.

Do not promote a software package into portable architecture merely because it appears in one reference image.

## 9. Telemetry boundary

The reference implementation may use Veragensia's privacy-tiered telemetry/improvement plane.

Portable invariant:

```text
metrics / bounded events / sampled traces / explicit Evidence
private content local by default
```

Telemetry may identify improvement candidates. It is evidence, not owner authority or automatic policy change.

## 10. Drift rule

When this document and canonical Veragensia specifications conflict for the Startempire implementation, use the newer owner-authorized Veragensia architecture for Agent Computer implementation details and update this portable reference accordingly.

Do not silently copy temporary implementation quirks, public-demo trust assumptions, customer identities or infrastructure topology into this portable substrate.
