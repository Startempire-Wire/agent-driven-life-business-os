# SOVOS Starter Routine Template Catalog

**Status:** CURRENT starter catalog; templates are portable suggestions, not assignments or authority grants  
**Effective:** 2026-10-03  
**Schema:** `contracts/operator-routine-template.v1.schema.json`

This directory converts the SOVOS routine-template doctrine into concrete reusable artifacts.

The starter catalog is grounded in recurring patterns found in:

- the connected Drive document **Foundational Systems, Teams & Autonomous Operating Routines** (2026-09-27);
- **Operating Routines — Cadence, Tools, Agent Capabilities & Implementation** (2026-10-02);
- the SOVOS Full-Surface Business Discovery Audit;
- the Portfolio Business Compiler and workforce catalogue.

It intentionally contains **portable abstractions only**. Private operator/customer payload, active credentials, grants, schedules and canonical work state remain in their owning systems.

## Catalog

| Template | Family | Typical applicability |
|---|---|---|
| `orientation.json` | orientation | founder/operator, multi-business, personal executive |
| `inquiry-triage.json` | intake/triage | services, SaaS, local service, commerce |
| `follow-up.json` | follow-up | keep momentum alive after initial contact/action; ensure the next appropriate touch/check occurs |
| `follow-through.json` | follow-through | carry an important thread through verified successful result, momentum and leverage |
| `reconciliation.json` | reconciliation | finance, records, multi-system truth |
| `delivery-case-review.json` | delivery review | services, SaaS, membership, support |
| `renewal-expiry.json` | renewal/expiry | contracts, subscriptions, credentials, obligations |
| `finance-operations.json` | finance operations | invoices, payment events, settlements, recurring obligations, costs |
| `content-distribution.json` | content/distribution | media, education, community, product distribution |
| `system-health-exceptions.json` | system health | software/technical operations |
| `incident-response.json` | incident response | impact detection, bounded recovery, consumer verification |
| `knowledge-freshness.json` | knowledge freshness | research, software, policy/runbook-heavy work |
| `evidence-closure.json` | evidence/closure | receiver-side acceptance, proof, outcome closure |
| `quiet-kaizen.json` | learning/improvement | constraint discovery, evidence-backed continuous improvement |
| `workforce-dispatch.json` | workforce dispatch | multi-business, services, SaaS, governed agent workforce |
| `weekly-planning.json` | planning | portfolio/life operating frontier |
| `household-admin.json` | life administration | household/family logistics and exceptions |
| `research-synthesis.json` | learning/improvement | researcher, author, student, creator |

The contract fixture `tests/fixtures/operator-routine-template.valid.json` remains a compact **business inquiry-triage** regression example.

## Composition rule

Do not assign a person one rigid archetype. Compose relevant templates from the owner's actual domains and observed evidence.

A template can be:

- discovered from current recurrence;
- requested by the owner;
- renewed from historical cadence;
- suggested from archetype.

If it is suggested only from archetype, say so explicitly.

## Activation rule

~~~text
template
→ audit candidate
→ owner-specific blueprint
→ determinization
→ compiled routine instance
→ shadow
→ pilot
→ proven
→ active
~~~

A template file never creates a schedule, grant, employee, credential, task, or external effect.

## Coverage rule

The machine-readable starter catalog must cover the core routine families named by `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`. Regression tests fail when a core family is described in doctrine but has no canonical template artifact.

The starter catalog is not a universal list of routines every owner should activate. Coverage means the compiler has reusable patterns to check for fit; it does not manufacture recurrence or authority.

## Freedom & leverage expansion

The 2026-10-03 catalog was the first operationally balanced starter set; the 2026-10-04 refinement adds a distinct first-class `follow_through` family so intermediate contact and final result can no longer be conflated. `../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md` identifies additional high-priority families for economic freedom, financial recovery, relationship stewardship, social/experience planning and capacity reinvestment.

Do **not** add those families by silently weakening the current schema or labeling everything `custom`. Extend the portable contract additively, add fixtures/regressions, then materialize canonical templates in small proof-backed slices. The first recommended proofs are:

1. prospecting/CRM → commercial progression → settled cash;
2. financial exposure → lawful resolution → recovered monthly cash flow / breathing room;
3. released capacity → owner-selected life/relationship outcome → verified feedback.

## Canonical-path rule

`routine-templates/` is the **canonical portable template catalog**.

The older `templates/routines/` path is retained only as a compatibility/incubation path while unique useful templates are promoted or reconciled. New portable routine templates MUST be added here, not to both locations.

Routine Packs live separately in `routine-packs/` and point only to canonical template IDs.
