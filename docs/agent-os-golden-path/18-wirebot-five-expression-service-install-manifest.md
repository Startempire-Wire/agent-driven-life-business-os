# Wirebot five-expression service install manifest

**Package-family version:** 0.1.0
**Date:** November 21, 2026
**Models:** Proto → Tempo → Crew → Chief → Sovereign
**Status:** Portable logical service manifest. Not a billable SKU, fixed version, installed-bundle guarantee, or a prescription of any customer's server topology.
**Canonical siblings:** `16-wirebot-five-expression-package-bill-of-materials.md` (installer BOM), `17-wirebot-five-expression-inclusion-matrix.md` (customer-safe inclusion matrix).

## Purpose

This document codifies the complete logical service and API estate that belongs to the Wirebot product line, and maps each service to the five Expressions and to its infrastructure shape. It is the single canonical manifest for "what Wirebot is made of and where each piece sits" — replacing the earlier tier/track matrices that mixed membership products with the package Expressions.

It is **portable**: it names logical services and shared-vs-dedicated infrastructure shape only. It never presumes a specific server count, hosting provider, or the operator's own private deployment.

## The five Expressions (recap)

- **Proto — Maker:** bounded useful tasks, active interaction only.
- **Tempo — Steward:** + routines, schedules, alarms, follow-through.
- **Crew — Foreman:** + packaged workforce (Composer, Foreman, specialists).
- **Chief — Chief of Staff:** + persistent owner-wide coordination and connectors.
- **Sovereign — Operating Partner:** + dedicated owner-controlled environment and data custody.

Each is a cumulative superset of the previous. See `16-…bill-of-materials.md` and `17-…inclusion-matrix.md`.

## Service estate

### A. Foundation (present in every Expression)

| Service | Language | Role |
| --- | --- | --- |
| Wirebot Core API | Go | Operating partner interactions, event/intent surfaces, proposals, integration coordination |
| Context Core | Go | Present operating context, decisions, guarded control proposals |
| Focusa | Rust | Direction, work governance, Workpoints, evidence, evaluation |
| UIAI Engine | Go | Browser work, document reading, diagnostics, screenshots, research, evidence delivery |
| Wirebot Memory Sync | Go | Owner-scoped memory synchronization between established components |

### B. Runtime and channels

| Service | Language | Role | Note |
| --- | --- | --- | --- |
| OpenClaw Gateway | TypeScript / Node.js | Agent runtime, channels, orchestration, approvals, scheduling, model routing, skills | External runtime; not a universal Proto requirement (BOM §2) |

### C. Memory and continuity stores (supporting)

| Service | Role |
| --- | --- |
| Mem0 | Graph/vector memory store |
| Letta | Archival memory and agent state |
| Local embeddings | Embedding service for memory stores |

### D. Knowledge, voice and support services (optional / selected)

| Service | Role |
| --- | --- |
| Agent KB API | Curated operating knowledge and runbook lookup |
| Wiki.js / Agent Wiki API | Wiki knowledge surface |
| Local speech recognition (STT) | Voice input |
| Voice relay / TTS | Voice output |
| Identity API | Identity and pairing |
| Compatibility proxy | LLM model routing and failover |
| Advisory API | Bounded decision advisory |
| Autonomy Guard | Failure classification and recovery advice |
| Server Guardian | Host safeguards, resource health, controlled cleanup |

### E. Workflow and workforce (Expression deltas)

| Capability | Introduced by | Role |
| --- | --- | --- |
| Scheduler and automations | Tempo | Routines, cron, alarms, event watchers, retry/backoff |
| Workforce Composer + Foreman + specialists | Crew | Packaged workforce dispatch, handoffs, evidence |
| Persistent Chief coordination | Chief | Owner-wide world model, connectors, operating pulse, cross-domain alarms, portfolio prioritization |
| Flow Mesh | Crew / Chief | Project/work synchronization across supported tools (Asana ⇄ Beads ⇄ Discord) |

### F. Dedicated environment (Sovereign, contracted)

| Service | Role |
| --- | --- |
| Sovereign collection | Dedicated private stack: backup, migration, failover, export, observability, private mesh, local body |

### G. Integration relationships (external — never bundled as Wirebot-owned software)

GitHub, Google Workspace (Gmail/Calendar), Cloudflare, Stripe, HubSpot, Discord, Telegram, and similar providers are integration relationships. They are not Wirebot-owned software and are never represented as universal inclusions.

## Service → Expression → infrastructure matrix

Infrastructure shape is **shared** (multi-tenant gateway, the default for Proto–Chief) or **dedicated** (owner-specific environment, Sovereign-contracted). It is never a fixed server topology.

| Service / capability | Proto | Tempo | Crew | Chief | Sovereign | Infrastructure |
| --- | --- | --- | --- | --- | --- | --- |
| Wirebot Core API | Included | Included | Included | Included | Included | Shared or dedicated |
| Context Core | Included (current-task) | Included (routine-aware) | Included (workforce-aware) | Included (owner-wide) | Included (full SOVOS) | Shared or dedicated |
| Focusa | Included | Included | Included | Included | Included | Shared or dedicated |
| UIAI Engine | Included | Included | Included | Included | Included | Shared or dedicated |
| Wirebot Memory Sync | Included | Included | Included | Included | Included, plus data custody | Shared or dedicated |
| OpenClaw Gateway | Not required | Conditional | Conditional | Required | Required | Shared or dedicated |
| Mem0 / Letta / embeddings | Selected | Selected | Selected | Selected | Selected | Shared or dedicated |
| Agent KB / Wiki / STT / TTS / identity / proxy / advisory | Selected | Selected | Selected | Selected | Selected | Shared or dedicated |
| Autonomy Guard / Server Guardian | Selected | Selected | Selected | Selected | Selected or contracted | Shared or dedicated |
| Scheduler and automations | Not included | Included (bounded) | Inherited | Owner-wide cadence | Owner portfolio cadence | Shared or dedicated |
| Workforce Composer / Foreman / specialists | Not included | Not included | Included (bounded) | Multiple workforces | Full workforce estate | Shared or dedicated |
| Persistent Chief coordination | Not included | Not included | Not included | Included | Included with Sovereign control | Shared or dedicated |
| Flow Mesh | Not included | Optional | Mission scope | Cross-domain | Full SOVOS scope | Shared or dedicated |
| Sovereign collection (dedicated stack) | Not included | Not included | Not included | Not included | Included where contracted | Dedicated |

## Topology invariant

Dedicated environment, private mesh, and local body are **"No default"** for Proto, Tempo, Crew and Chief, and **"Required where contracted"** for Sovereign (BOM §2). No Expression presumes a dedicated server, a dual-server topology, or any specific hosting shape. A customer may run one server, several, or none (fully managed); the manifest does not decide this for them.

The operator's own private deployment (separate servers for the control plane versus the heavy execution plane) is a **private deployment binding under the Sovereign expression**, documented in the private infrastructure record — never shipped as a customer default and never copied into this portable manifest.

## Disposition of earlier tier/track matrices

The older capability matrices that mixed membership products (Standalone Free–Power; Network Free–Sovereign) with infrastructure shape are superseded by this manifest and by `16-…bill-of-materials.md` / `17-…inclusion-matrix.md`. The shared-vs-dedicated infrastructure distinction is retained here; the membership tier names are not Wirebot package Expressions and are retired from the Wirebot product surface.

## Honesty boundaries

- "Included" means "within the intended scope of this Expression under its package contract", not "installed for every buyer".
- Supporting services (Mem0, Letta, embeddings, STT, identity, wiki, proxy, advisory) are environment choices, not universal first-party inclusions.
- AI inference is always BYOK or separately agreed; it is never silently bundled.
- No single signed release manifest yet joins every component; this remains a source-grounded logical manifest, not a certified bundle.
- Independent customer-owned Focusa, UIAI, Pi, scheduler, model, data and machine rights are preserved; a lower Expression never disables them.
