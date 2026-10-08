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

## Golden Path implementation set

Use these as a connected set, not competing plans:

- [`agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md`](agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md) — current working spine / dependency order.
- [`agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md`](agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md) — current gap owner.
- [`agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md`](agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md) — discovery/audit procedure.
- [`agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md`](agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md) — compiler/analytics target.
- [`agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md`](agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md) — exact runtime closure plan; `SAG-10` / `SAG-18` remain open until proven.

## Environment evaluation and agent activation handoff

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