# SOVOS Documentation Index

**Status:** CURRENT documentation router  
**Purpose:** give humans and agents one short path to current truth without forcing them through historical/versioned material.

## Start here

1. [`../README.md`](../README.md) — product/doctrine overview.
2. [`REPOSITORY_INTEGRITY.md`](REPOSITORY_INTEGRITY.md) — status vocabulary, anti-drift rules, compatibility-protected paths.
3. [`../OWNER_AUTHORITY_CONSTITUTION.md`](../OWNER_AUTHORITY_CONSTITUTION.md) — architecture authority.
4. [`../CURRENT_ECOSYSTEM_ARCHITECTURE.md`](../CURRENT_ECOSYSTEM_ARCHITECTURE.md) — current product ownership/topology.
5. [`../AGENTS.md`](../AGENTS.md) — build/operations behavior.
6. [`../AGENT_OS_GOLDEN_PATH.md`](../AGENT_OS_GOLDEN_PATH.md) — current deployment doctrine.
7. [`agent-os-golden-path/SERVER_AGENT_HANDOFF.md`](agent-os-golden-path/SERVER_AGENT_HANDOFF.md) — current-state vs target-state server handoff.

## Current SOVOS doctrine by concern

| Concern | Canonical current document |
|---|---|
| Human freedom / operating outcome | [`../SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md`](../SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md) |
| Driverless Business | [`../SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md`](../SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md) |
| Information infrastructure | [`../SOVOS_INFORMATION_INFRASTRUCTURE.md`](../SOVOS_INFORMATION_INFRASTRUCTURE.md) |
| Freedom, leverage, Perpetua, frontiers | [`../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`](../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md) |
| Routine compiler / templates | [`../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`](../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md) |
| Mathematical intelligence / composable UX target | [`../SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md`](../SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md) |
| Owner notification / response channels | [`../SOVOS_OWNER_NOTIFICATION_AND_RESPONSE_CHANNEL.md`](../SOVOS_OWNER_NOTIFICATION_AND_RESPONSE_CHANNEL.md) |
| Cross-product refs / freshness / replay | [`../CROSS_PRODUCT_SEAM_CONTRACT.md`](../CROSS_PRODUCT_SEAM_CONTRACT.md) |

## Master Loop — incubating whole-system draft

**Latest draft revision: 0.3.0, 2026-10-11.** This operator-requested draft preserves the whole Chief-of-Staff organism, Tononi/Koch research and reciprocal Master Loop–memory connection. The new pass makes compiler-to-outcome handoffs and failure behavior precise, including whole Workstreams/full Trajectory and relevant Focusa core primitives under issue #618. It references current owners rather than replacing their doctrine.

- [Master Loop draft](02-sovos-master-loop-draft.md) — integrated architecture; §3.2 connects the full Focusa journey, §11.1 the reciprocal memory seam.
- [Detailed integration blueprint](05-sovos-master-loop-integration-blueprint.md) — proposed owners, compiler linking/effect mapping, logical pre/postconditions, guarded lifecycles, Jev/local judgment, human coordination, correction/recovery and receiver proof; §11 maps Workstreams, Full/Medium/Short, CallGraphs and core primitive consumers/guards.
- [Alarm and simulation design](03-sovos-master-loop-alarm-and-simulation-design.md) — sixteen falsification predicates, concrete synthetic inquiry/absence/memory trace, two-branch/shared-dependency Workstream overlay, original life/business/client scenarios and independent IIT/operational controls.
- [Source and integration register](04-sovos-master-loop-source-and-integration-register.md) — pinned current versus older local source, exact-support gaps and review dispositions; §6.1 is the memory-agent handoff, §6.2 separates paper-defined proposals from remaining qualification, §7 gates decomposition.

Memory agents should read that handoff alongside the existing [portable memory profile](../PORTABLE_MEMORY_REFERENCE_PROFILE.md). Publishing these proposals does not promote them to canonical memory policy, activate native writes, or supersede another agent's verified assignment.

**INCUBATING; not implementation-ready.** No coding, activation or task/CallGraph decomposition until the complete bounded specification is reviewed. A saved draft or existing source artifact is not a deployed capability.

## Commercial revenue work — first consumer Wirebot

- [Commercial Work v1 profile](../commercial-work/revenue-engine.v1.json) — portable, owner-neutral lifecycle composition; not an activated customer job.
- [Commercial Work contract](../contracts/operator-commercial-work.v1.schema.json) and [private customer binding contract](../contracts/operator-commercial-work-binding.v1.schema.json) — versioned machine-readable conformance; all customer grants and source refs remain private.
- [Business Revenue Engine Routine Pack](../routine-packs/business-revenue-engine.json) — reuses canonical v1 routines without introducing v1 prospecting enum drift.
- [Read-only customer binding validator](../scripts/validate-commercial-work.py) — static version/shape/source-ref checks only, no provider authentication or effects.
- [Agent skill](../skills/sovos-revenue-work/SKILL.md) — existing Wirebot/OpenClaw/Focusa-consumable first-value procedure; loading/activation remains deployment-specific.
- [Wirebot × HubSpot pilot](commercial-work/WIREBOT_HUBSPOT_PILOT.md) — read-only observed baseline, tier-aware offer routing and acceptance path.

## Golden Path implementation set

Use these as a connected set, not competing plans:

- [`agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md`](agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md) — current working spine / dependency order.
- [`agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md`](agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md) — current gap owner.
- [`agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md`](agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md) — discovery/audit procedure.
- [`agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md`](agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md) — compiler/analytics target.
- [`agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md`](agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md) — exact runtime closure plan; `SAG-10` / `SAG-18` remain open until proven.

## Environment evaluation and agent activation handoff

- [`../starter.md`](../starter.md) — single-page **canonical general SOVOS Agent Starter**: setup rules, supported commands, phase checks, common failures and handoff. Does not contain any customer-specific details.
- `../scripts/activation-blueprint.py --format starter` — compiles a **complete customer-specific starter.md** from the general Starter plus the existing read-only host audit and an owner-private intent/status JSON. This is a local, advisory document generator, not an installer or authority grant. Output MUST be outside the shared repository. Example:

  ```sh
  python3 scripts/activation-blueprint.py --audit /PRIVATE/observations/brownfield.json \
    --intent /PRIVATE/owner-intent.json --format starter \
    --output /PRIVATE/customer/starter.md
  ```

  Rerunning with new evidence updates a previously generated, unedited file; manual edits or unknown existing files are never overwritten silently. Refine the same canonical base and generator and add focused regression cases for newly found setup failures; do not create a parallel Golden Path.

- `../scripts/substrate-bootstrap.sh` — host-local CLI/runtime/environment observations, **not** complete tenant or business readiness.
- `../scripts/brownfield-audit.sh` — value-free setup markers, service/fleet reports and missing-capability observations; Bash/SSH sweeps do not establish Windows/managed-host parity.
- `../scripts/fleet-diff.py` — observed fleet drift, not a work authorization.
- `../scripts/activation-blueprint.py` — local read-only owner-private first-value plan plus long-form receiving-agent instructions; uses existing report JSON and separate confirmed business/hosting intent.
- `agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md` — canonical operating sequence including first-value lane. No parallel Golden Path document.

## Portable machine contracts and catalogs

- `contracts/` — versioned portable schemas; contracts are not runtime proof.
- [`../routine-templates/README.md`](../routine-templates/README.md) — canonical routine-template catalog.
- [`../routine-packs/README.md`](../routine-packs/README.md) — canonical routine-pack catalog.
- `../templates/routines/` — SUPERSEDED compatibility/incubation path; do not treat as second catalog.
- `../data/` — structured portable data such as economic model inputs.

## Product-specific implementation truth

SOVOS is doctrine/integration architecture. For code/runtime truth, go to the owning product repo:

- Wirebot / Wirebot App — owner-facing Operating Partner experience.
- Focusa — governed work, cognition, Evidence, continuity, trusted generated UI.
- UIAI Engine — browser/computer observation, actuation, diagnostics and proof.
- Veragensia — Agent Computer/body/runtime placement/enforcement.

Never infer product implementation from SOVOS target prose alone.

## Historical, candidate and compatibility material

- `agent-os-golden-path/0.x.x.md` files are version lineage/candidates; they do not replace current authority.
- `agent-os-golden-path/CHANGELOG.md` is history, not current runtime status.
- dated audits/evidence remain useful for provenance but require re-verification before present-tense claims.
- SUPERSEDED files are retained only when compatibility/lineage matters and must point to their replacement.

## Documentation hygiene rule

Before adding a new document, ask whether the concern already has a canonical owner above. Prefer updating the current owner or adding a bounded appendix over creating a parallel architecture file. New docs must declare `LIVE`, `CURRENT`, `INCUBATING`, `DATED SNAPSHOT`, `candidate`, `SUPERSEDED` or historical status where ambiguity is possible.

Do not move or rename compatibility-protected files merely for tidiness; migrate consumers first.