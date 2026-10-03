# SOVOS Starter Routine Template Catalog

**Status:** CURRENT starter catalog; templates are portable suggestions, not assignments or authority grants  
**Effective:** 2026-10-03  
**Schema:** `contracts/operator-routine-template.v1.schema.json`

This directory converts the SOVOS routine-template doctrine into concrete reusable artifacts.

The initial catalog is grounded in the recurring patterns found in:

- the connected Drive document **Foundational Systems, Teams & Autonomous Operating Routines** (2026-09-27);
- **Operating Routines — Cadence, Tools, Agent Capabilities & Implementation** (2026-10-02);
- the SOVOS Full-Surface Business Discovery Audit;
- the Portfolio Business Compiler and workforce catalogue.

## Catalog

| Template | Family | Typical applicability |
|---|---|---|
| `orientation.json` | orientation | founder/operator, multi-business, personal executive |
| `follow-up.json` | follow-up | unresolved commitments across life/business |
| `reconciliation.json` | reconciliation | finance, records, multi-system truth |
| `delivery-case-review.json` | delivery review | services, SaaS, membership, support |
| `renewal-expiry.json` | renewal/expiry | contracts, subscriptions, credentials, obligations |
| `system-health-exceptions.json` | system health | software/technical operations |
| `weekly-planning.json` | planning | portfolio/life operating frontier |
| `knowledge-freshness.json` | knowledge freshness | research, software, policy/runbook-heavy work |
| `household-admin.json` | life orientation | household/family logistics and exceptions |
| `research-synthesis.json` | learning/improvement | researcher, author, student, creator |
| `inquiry-triage.json` | intake/triage | services, SaaS, local service, commerce |
| `content-distribution.json` | content/distribution | media, education, community, product distribution |
| `workforce-dispatch.json` | workforce dispatch | multi-business, services, SaaS, governed agent workforce |

The existing contract fixture `tests/fixtures/operator-routine-template.valid.json` remains a compact **business inquiry-triage** example and regression fixture.

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


## Canonical-path rule

`routine-templates/` is the **canonical portable template catalog**.

The older `templates/routines/` path is retained only as a compatibility/incubation path while unique useful templates are promoted or reconciled. New portable routine templates MUST be added here, not to both locations.

Routine Packs live separately in `routine-packs/` and point only to canonical template IDs.
