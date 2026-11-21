# Wirebot five-expression inclusion matrix

**Package-family version:** 0.1.0
**Date:** November 21, 2026
**Models:** Proto → Tempo → Crew → Chief → Sovereign
**Status:** Source-grounded capability reference. Not a billable SKU, fixed version, or installed-bundle guarantee.
**Canonical sibling:** `16-wirebot-five-expression-package-bill-of-materials.md` (installer BOM, v0.1.0).

## Purpose

A customer-safe, portable matrix of what is included in each of the five Wirebot Expressions, derived from the five-expression bill of materials. It exists so readers who dig into the technical substance of Wirebot can see, at a glance, what belongs to each Expression without consulting the full installer contract.

The five Expressions are an **ascending progression of capability** — not separate AI models and not a hierarchy of human worth:

- **Proto — Maker:** one bounded, useful, inspectable result.
- **Tempo — Steward:** dependable recurring follow-through, routines, schedules and alarms.
- **Crew — Foreman:** a coordinated specialist workforce for a larger goal.
- **Chief — Chief of Staff:** persistent owner-wide coordination across life and business.
- **Sovereign — Operating Partner:** owner-controlled private environment, data custody and full governance.

Each Expression is a **superset** of the previous one (cumulative deltas). Upgrades apply the next delta; downgrades remove only Wirebot package rights and never destroy customer data or independently owned capabilities.

## Inclusion matrix

| Area | Proto | Tempo | Crew | Chief | Sovereign |
| --- | --- | --- | --- | --- | --- |
| Wirebot Core — the operating relationship | Included | Included | Included | Included | Included |
| Focusa — direction, work and governance | Included | Included | Included | Included | Included |
| UIAI Engine — browser, research and visual work | Included | Included | Included | Included | Included |
| Context Core — present operating context | Current-task view | Routine-aware view | Workforce-aware view | Owner-wide view | Full owner-controlled view |
| Memory continuity — owner-scoped memory | Included | Included | Included | Included | Included, plus portable data custody |
| Recurring automations — routines and schedules | Not included | Bounded routines | Inherited | Owner-wide cadence | Owner portfolio cadence |
| Alarms and event watchers | Not included | Bounded routine alarms | Workforce-aware | Cross-domain triage | Owner sensing and escalation policy |
| Packaged workforce — Composer, Foreman, specialists | Not included | Not included | Bounded missions | Multiple coordinated workforces | Full workforce estate |
| Persistent Chief-of-Staff coordination | Not included | Not included | Not included | Included | Included with Sovereign control |
| Cross-domain connectors and work sync | Current task only | Routine scope | Mission scope | Included | Full SOVOS scope |
| Agent runtime — OpenClaw | Not required | If the routine owner requires it | If the workforce owner requires it | Required | Required, within the contracted architecture |
| Private environment and dedicated topology | No default | No default | No default | No default | Required where contracted |
| Custom extension and plugin rights | Catalog baseline | Approved routine packages | Approved workforce packs | Approved Chief and portfolio packs | Owner-controlled, under security policy |
| Additional services — Agent KB, Autonomy Guard, Server Guardian | Selected when needed | Selected when needed | Selected when needed | Selected when needed | Selected or contracted |
| AI inference | BYOK or agreed | BYOK or agreed | BYOK or agreed | BYOK or agreed | BYOK unless separately contracted |

## Component applicability (tedious pass)

Each software component is classified by its applicability per Expression using the vocabulary **foundation**, **optional**, **higher-level**, **excluded**, **contract-dependent**.

| Component | Proto | Tempo | Crew | Chief | Sovereign |
| --- | --- | --- | --- | --- | --- |
| Wirebot Core | foundation | foundation | foundation | foundation | foundation |
| Context Core | foundation | foundation | foundation | foundation | foundation |
| Focusa | foundation | foundation | foundation | foundation | foundation |
| UIAI Engine | foundation | foundation | foundation | foundation | foundation |
| Memory continuity (Sync + stores) | foundation | foundation | foundation | foundation | foundation |
| Flow Mesh (work sync) | excluded | optional | higher-level | higher-level | contract-dependent |
| OpenClaw (runtime) | excluded | optional | optional | foundation | foundation |
| Additional services | optional | optional | optional | optional | contract-dependent |
| Sovereign collection (dedicated stack) | excluded | excluded | excluded | excluded | contract-dependent |

### Foundation (in every Expression)

- **Wirebot Core** — the operating partner API plane; the "conversational Wirebot expression" is included in all five (BOM §2).
- **Context Core** — present operating context; present in all five, with the world-model scope growing per Expression (BOM §2 "Operator World Model").
- **Focusa** — direction, work and governance; explicit "Foundation" row for all five (deep technical specifications).
- **UIAI Engine** — browser, research and visual work; explicit "Foundation" row for all five (deep technical specifications).
- **Memory continuity** — baseline identity/authority (BOM Proto §3) and owner-scoped memory sync; portable data custody is a Sovereign delta (BOM Sovereign §7).

### Not foundation

- **OpenClaw** is an external runtime, not a universal Proto requirement. The BOM §2 "OpenClaw requirement" row reads: Proto "No", Tempo "only if the selected routine owner requires it", Crew "required when the chosen workforce owner requires it", Chief "required persistent Chief runtime", Sovereign "required within contracted Sovereign architecture". Proto's channel can use a compatible approved adapter.
- **Flow Mesh** (project/work synchronization across supported tools) is a higher-level connector; it is not a Proto/Tempo baseline and appears where the Expression's work coordination scope calls for it.
- **Sovereign collection** is the dedicated private stack, excluded from lower Expressions and included only where contracted.
- **Additional services** (Agent KB, Autonomy Guard, Server Guardian) are selected supporting capabilities, never default inclusions for any Expression.

## Topology is private and never prescribed

The BOM's own "Dedicated owner VPS/private mesh/local body" row reads **"No default"** for Proto, Tempo, Crew and Chief, and **"Required where contracted"** for Sovereign. No Expression presumes a dedicated server, a dual-server topology, or any specific hosting shape. Server topology is a private deployment binding under a contracted Sovereign agreement — never shipped as a customer default.

## Website presentation (progressive disclosure)

When surfaced on the public website, this matrix is **deep-dive, progressive-disclosure content**. It is not part of the primary purchase journey, the primary header/footer navigation, or the homepage. It lives under the Tech Specs path and is reachable only by readers who choose to dig deeper. The primary marketing pages (expression selection and the five Expression profiles) remain human-first and do not surface this tool list.

The rendered website data lives in `wirebot-website/wordpress/technical-reference.json` (`inclusion_matrix`), which is a customer-safe projection of this document — never a second authority.

## Sources

- `16-wirebot-five-expression-package-bill-of-materials.md` (five-expression BOM, v0.1.0)
- `wirebot-website/docs/website/2026-11-14-wirebot-expressions-language-contract.md`
- `wirebot-website/docs/website/2026-11-14-wirebot-deep-technical-specifications-architecture.md`
- `wirebot-website/docs/website/2026-11-14-wirebot-sovereign-api-technical-reference-matrix.md`
- `wirebot-core/docs/47-wirebot-expression-package-runtime-enforcement.md`

## Honesty boundaries

- "Included" means "within the intended scope of this Expression under its package contract", not "installed for every buyer". The source audit does not yet supply one signed release manifest joining every component.
- AI inference is always BYOK or a separately agreed arrangement; it is never silently bundled into the software price.
- Independently purchased Focusa, UIAI, Pi, scheduler, model, data and machine rights are detected and preserved; a lower Expression never disables them.
