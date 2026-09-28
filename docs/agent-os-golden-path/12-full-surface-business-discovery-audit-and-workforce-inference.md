# Full-Surface Business Discovery Audit and Workforce Inference

> **Status:** proposed Stage 5 operating procedure; not a new data store, architecture authority, credential grant, workforce deployment or automatic customer contact.
> **Applies to:** owner-authorized fresh and brownfield Agent-Driven Life & Business OS deployments.
> **Canonical sequence:** Golden Path Stage 5 discovery → Wirebot Workforce Composer proposal → owner/governance acceptance → Focusa Workstream/Foreman/CRIST assignment → bounded execution → evidence and accepted outcome.

## Purpose and finish line

The owner may run several businesses, hold dormant product assets, work across many devices and accounts, and have undocumented obligations hidden in files, correspondence and customer systems. A generic agent roster cannot be commissioned safely from a short interview or an old business plan.

This audit creates an **evidence-backed portfolio map of the owner's actual businesses, life/operating domains, desired outcomes, customers and obligations, recurring workflows, neglected assets, shared capabilities, and candidate team/employee needs**. Several businesses are a normal case, not an exception. It has two outputs: a private business-revival matrix and a private workforce/automation proposal. It does **not** activate the proposed employees or schedules. Completion means the auditor can explain what was examined, what remains inaccessible, which findings are current versus historical, and exactly which first bounded workflow is ready for an authorized pilot. A list of files or an attractive agent org chart is not completion.

## 1. Intake, authority and protected scope

1. Identify the canonical owner and any delegated human authority. Record the exact business/client/tenant scope, geography, devices, accounts, retention limits, exclusion list and desired outcome.
2. Obtain explicit access grants for each source. An OAuth token, filesystem mount, browser session, or root account proves reachability, **not consent to export or share its data with every worker**. A client may authorize metadata inventory without full-body review.
3. Apply CRIST at audit depth: **Context** (owner/businesses and current state), **Role** (auditor and supervisor), **Interview** (only unresolved material facts), **Spec** (coverage, privacy, acceptance, budget), **Tasks** (dependency-ordered source work). New/high-consequence clients use Full CRIST; a recurring delta audit may inherit an accepted scope.
4. Discover the canonical owner of each record and Focusa project/Workstream binding before promoting findings to authority. The partner's private memory, another client tenant, employee transcript or a public search index is not the audit's universal database.
5. Run discovery read-only by default: no customer outreach, account creation, message marking/deletion, file move, payment, deployment, publication or schedule activation. Separate approval/consent gates govern any follow-on effect.

## 2. Source inventory and coverage manifest

Inventory **all authorized source classes**, not only the easiest account:

| Source class | Minimum inventory | Bounded content pass |
|---|---|---|
| Computer/device files | authorized roots and devices, document types, counts, owner, dates, hashes/IDs where available, exclusions | business plans, contracts/SOPs, customer delivery, product designs; OCR only if consented |
| Cloud Drive/Docs and other stores | account/drive, folders, file IDs, MIME type, owner, modification, shared visibility, page/continuation count | choose current/high-signal and contradictory documents; never treat title alone as proof |
| Mailboxes and attachments | each authorized account, date range, labels/threads, total or query caps, business categories | bounded message bodies for leads, invoices, renewals, delivery and commitments; exclude OTP, recovery, private unrelated mail |
| Calendar and collaboration | calendars, projects/channels, participants and scope | recurring meetings, handoffs, commitments, outcomes and abandoned cadences |
| CRM, billing and customer systems | provider and tenant, contract/invoice/payment authority, access level | reconcile deal → contract → invoice → settlement → renewal; avoid mixing notices with settled cash |
| Repositories, sites and products | org/private/public inventory, repository owner, commit, release/deploy/route, documentation | source/deployment/consumer acceptance; code existence is not customer use |
| Runtime and automation | agents, hosts, scheduled jobs, queues, tools, alert routes, backups, budgets | exact running assignment versus dormant profile, success/failure evidence, rollback |

For each source, record: **scope, consent/ref, collection time, method, owner, object count or denominator, pages/continuations, content reviewed, excluded objects, staleness, errors and last verified time**. Distinguish `metadata-complete for accessible returned set` from `content-reviewed` and `all owner sources covered`. If one account or device is inaccessible, record it as a visible gap and continue other sources rather than falsely claiming completeness or stopping the whole audit.

Use structured APIs/CLIs before browser or visual automation. Batch bounded reads and respect provider rate limits. Keep raw bodies in their owning systems or temporary restricted processing, not the shared catalogue or worker handoff. Do not print secrets, recovery material or other customers' data into logs or reports.

## 3. Extract entities, outcomes and obligations

From the authorized sources, extract candidate **business/legal entities, brands, products, service lines, customers, partners, assets, software, channels and human/agent roles**. Resolve aliases and parent-child relationships before counting "number of businesses." A duplicate checklist record, client project, domain, repository or concept is not automatically a separate business.

For each entity, preserve at least one source-backed record of:
- owner and relationship to other entities (or `unknown`);
- current operator goal and desired customer outcome, using direct owner language when available;
- past and current offers, customers, revenue notices, invoices and renewal obligations—each at the proof level its source supports;
- websites, apps, code, distribution channels and client delivery surfaces;
- existing people/agents, processes and bottlenecks;
- dependencies, legal/privacy boundaries, current status and evidence freshness.

Classify source material as **direct current owner steering**, **live external/system observation**, **current business record**, **historical plan**, **assistant proposal**, or **unverified inference**. Later owner corrections supersede older exploration. An email payment alert is a lead for ledger reconciliation, not a bank statement; a running daemon is not accepted customer value.

## 4. Mine workflows and renewal opportunities

For each real or proposed workflow across every in-scope business/domain, map:

```text
trigger → source/input → actor and owner → steps → handoff → exception
→ customer/business effect → evidence → approval gate → repeat frequency
```

Classify it as a deterministic procedure, recurring scheduled process, event-driven case, judgment/coordination role, bounded project, or human-reserved action. Identify slack: unanswered leads, uncollected/unclear invoices, expiring contracts/domains, neglected customer promises, outdated offers, disconnected metrics, stalled distribution, duplicate manual work, missing backup/acceptance, or dormant assets that could serve a measured demand.

Separate **renewal of existing obligations** from **revival of historical ideas**. Prioritize real customer value and cash preservation before staffing a new product. No historical idea becomes active solely because its old plan is detailed; no new outreach is sent merely because a candidate contact was found.

### 4.1 Compile routine blueprints

For each corroborated recurring pattern, produce a reviewable typed routine blueprint containing:

```text
portfolio/business/domain refs
purpose / desired outcome
trigger / cadence / event
inputs and canonical owners
deterministic operations
semantic/judgment responsibilities
human-reserved decisions
exceptions / recovery
candidate worker/role
execution placement
authority/data/credential refs
idempotency / overlap / missed-run / retry
Evidence / acceptance
measurement plan
revoke / retire
```

A blueprint remains proposed until accepted. It is not an activated worker, schedule or authority grant.

## 5. Triangulate and build the private matrices

Maintain a source-backed evidence register. Resolve contradictions explicitly: accounting versus notification, public site versus internal release, active service versus stale checklist, repository versus deployment, role template versus assigned worker. If sources differ, state what each can prove and what would settle the conflict.

### Business and software matrix fields

| Field | Required meaning |
|---|---|
| Entity and relationship | owner/business/brand/product/client distinction; canonical source |
| Activity class | `active_evidenced`, `revive_pilot`, `conditional`, `dormant_candidate`, `blocked`, `unknown` |
| Past versus present | last direct operator decision, historical source date, most recent independent observation |
| Economic path | customer outcome, offer, lead/contract/invoice/settlement/retention evidence; never invented precision |
| Renewal or slack | existing obligations, unresolved work and measured opportunity |
| Software and distribution | canonical owner, actual release/consumer proof, acquisition channel |
| Workforce | required staff, scheduled, on-demand, pilot, blocked, excluded or unknown profiles |
| Routine analytics | intended outcome, baseline if known, reliability/cost/attention dimensions, authoritative business metric refs and measurement cadence |
| Leverage path | what constraint is removed, future effort/cost avoided, reusable capability created, other businesses/routines enabled and how double-counting is avoided |
| Gate and proof | next bounded action, prerequisite, acceptance, confidence and source refs |

The status is **an audit inference for owner review**, not a mutation of billing, the project registry, checklist or employee roster. Keep client-specific documents, private contacts and sensitive amounts in the private owner scope; publish only a permission-safe abstraction if a public product lesson is needed.

## 6. Derive teams and assignments, not an indiscriminate agent army

Group repeated work by outcome and canonical owner. Match to the existing [Composable AI Workforce Catalogue](./09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md) before inventing a new title:

- executive Chief of Staff and authority/dispatch;
- systems/security/integrations/recovery;
- market intelligence and offer readiness;
- content/distribution and sales/pipeline;
- delivery, customer success and billing;
- evidence, knowledge and quality.

For each proposed employee, record role profile, task pack, supervisor/Foreman, client/project/Workstream, allowed capabilities/data, credential-use reference, budget, lifetime, activation, acceptance, evidence, escalation and revoke/stop path. Select **required staff**, **scheduled worker**, **on-demand bench**, **pilot**, **conditional**, **blocked**, **excluded** or **unknown** based on verified frequency and readiness. A template does not hire itself. Dormant profile means no timer and no runtime cost.

Wirebot Portfolio Business Compiler recommends routine blueprints and leverage opportunities; Workforce Composer recommends the roster and assignment. Owner/governance acceptance precedes Focusa binding. Focusa Workforce then operates exact Workstream work with Workpoints, Silent Sessions, Work Loops or background jobs under grants. OpenClaw's durable automations scheduler on the persistent Tailscale-connected VPS is the default launcher for recurring agent/system-event assignments when appropriate; other owning schedulers may be used for deterministic/provider-native work. A schedule never creates authority. UIAI/Veragensia provide bounded execution surfaces. Source business/life systems plus owner acceptance retain outcome truth; Wirebot/Perpetua builds the base private leverage/optimization synthesis; W.I.N.S. may project progression when enabled.

## 7. Prioritize, review and pilot

Rank candidate workflows by **life/business outcome importance, customer/revenue importance where relevant, evidence quality, repeatability, integration readiness, human sensitivity, consequence risk, cost, time saved, reusable capacity and cross-portfolio leverage**. Produce no more than a small active core and one first bounded pilot; keep the rest conditional or dormant. Batch owner decisions into clear decision cards instead of interrupting with incremental questions.

Pilot path:
1. operator accepts the entity/workstream and outcome;
2. CRIST assignment and Focusa scope/authority are verified;
3. flash/session worker shadow-runs without external side effects;
4. source/tenant/negative-path and failure/rollback tests pass;
5. one approved real action executes, with send/dispatch/consumer receipts;
6. independent verifier confirms the customer/business effect;
7. only repeatable success warrants scheduling or a durable staff role; promoted routines enter ongoing analytics and Quiet Kaizen review.

Do not market a financial result from disconnected telemetry, treat a drafted message as sent, or treat an agent run as a sale. A high-scoring automation idea may still be prohibited by privacy, consent, legal or owner-reserved-power rules.

## 8. Deliverables, completion test and re-audit

Deliver a **private source inventory and coverage manifest**, **business/asset matrix**, **workflow and renewal map**, **workforce assignment/schedule proposal**, **evidence and contradiction register**, **decision cards**, and **7/30/90-day sequence** tied to the owner's actual outcome. Record unreviewed content, unavailable accounts and stale evidence rather than filling gaps with invention.

An audit is complete enough to enter Stage 7 only when:
- every granted source is inventoried or explicitly unavailable, with pagination and content-review coverage disclosed;
- businesses and major operating areas are represented or explicitly excluded;
- recurring work and owner bottlenecks have source references and a current/old distinction;
- proposed workers have a bounded supervisor, scope, capability, authority, cost and acceptance;
- proposed schedules have owner, dependency, quiet hours, idempotency, failure alert, rollback and revocation;
- economic outcomes are distinguished from activity and system health;
- contradictions and unknowns are visible and prioritized;
- no external mutation occurred during discovery absent a separate exact approval;
- the owner can review one viable first pilot and its proof gate without another exhaustive interview.

Refresh by **delta**, not a blind complete re-ingest: compare source revision and current owner decision, recheck high-risk/expiring records, record supersession and revoked grants, and preserve a prior audit's evidence handles. Re-audit after material business change, onboarding, scope correction or failed acceptance. Store canonical facts in their owning product and a bounded source-linked synthesis in the owner-private knowledge surface; never create a second cross-business authority database just for this audit.

## Placement and ownership

This procedure **decomposes Golden Path Stage 5** in [`02-agent-os-golden-path-ordered-tasks.md`](./02-agent-os-golden-path-ordered-tasks.md) and feeds its accepted requirements into Stage 7 Workforce Composer. It does not duplicate Focusa's Workpoint/authority store, source business/life outcome records, the customer CRM, optional W.I.N.S. projections, Google Drive, or Wirebot's private memory. Exact collection adapters and product API/CLI operations remain owned by their products and are verified live per deployment.
