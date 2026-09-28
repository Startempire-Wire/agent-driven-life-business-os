# Full-Surface Business Discovery Audit and Workforce Inference

> **Status:** proposed Stage 5 operating procedure; not a new data store, architecture authority, credential grant, workforce deployment or automatic customer contact.
> **Applies to:** owner-authorized fresh and brownfield Agent-Driven Life & Business OS deployments.
> **Canonical sequence:** Golden Path Stage 5 discovery → Wirebot Workforce Composer proposal → owner/governance acceptance → Focusa Workstream/Foreman/CRIST assignment → bounded execution → evidence and accepted outcome.

## Purpose and finish line

The owner may run several businesses, hold dormant product assets, work across many devices and accounts, and have undocumented obligations hidden in files, correspondence and customer systems. A generic agent roster cannot be commissioned safely from a short interview or an old business plan.

This audit creates an **evidence-backed portfolio map of the owner's actual businesses, products and life/business domains; desired outcomes; customers and obligations; recurring workflows; neglected assets; and candidate system/workforce needs**. Several businesses are normal and may share services, people, software or routines without becoming one business. It produces a private portfolio/business matrix, routine-blueprint set, and workforce/system proposal. It does **not** activate the proposed employees or schedules. Completion means the auditor can explain what was examined, what remains inaccessible, which findings are current versus historical, and exactly which first bounded workflow is ready for an authorized pilot. A list of files or an attractive agent org chart is not completion.

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

For each real or proposed workflow, map:

```text
portfolio/business/life-domain scope
→ trigger
→ source/input
→ actor and canonical owner
→ steps and step class
→ handoff/exception
→ customer/life/business effect
→ evidence
→ approval gate
→ repeat frequency
→ measurement baseline
```

Then compile a **routine blueprint** that distinguishes deterministic code/API/CLI steps, agentic judgment, UIAI browser/computer work and human-reserved steps. One routine may serve multiple businesses only when scope, data separation, attribution and authority are explicit.

Classify it as a deterministic procedure, recurring scheduled process, event-driven case, judgment/coordination role, bounded project, or human-reserved action. Identify slack: unanswered leads, uncollected/unclear invoices, expiring contracts/domains, neglected customer promises, outdated offers, disconnected metrics, stalled distribution, duplicate manual work, missing backup/acceptance, or dormant assets that could serve a measured demand.

Separate **renewal of existing obligations** from **revival of historical ideas**. Prioritize real customer value and cash preservation before staffing a new product. No historical idea becomes active solely because its old plan is detailed; no new outreach is sent merely because a candidate contact was found.

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

Wirebot's Portfolio Operating Compiler / Workforce Composer recommends routines, systems, roster and assignments. Owner/governance acceptance precedes Focusa binding. Focusa Workforce then operates exact Workstream work with Workpoints, Silent Sessions, Work Loops or background jobs under grants. OpenClaw Automations on the persistent remote VPS is the default durable scheduler for approved recurring assignments; the schedule does not create Focusa authority. UIAI/Veragensia provide bounded execution surfaces; W.I.N.S. records accepted outcomes and owner-facing momentum/leverage, not merely agent activity.

## 7. Prioritize, review and pilot

Rank candidate workflows by **customer/revenue importance, evidence quality, repeatability, integration readiness, human sensitivity, consequence risk, cost, and time saved**. Produce no more than a small active core and one first bounded pilot; keep the rest conditional or dormant. Batch owner decisions into clear decision cards instead of interrupting with incremental questions.

Pilot path:
1. operator accepts the entity/workstream and outcome;
2. CRIST assignment and Focusa scope/authority are verified;
3. flash/session worker shadow-runs without external side effects;
4. source/tenant/negative-path and failure/rollback tests pass;
5. one approved real action executes, with send/dispatch/consumer receipts;
6. independent verifier confirms the customer/business effect;
7. only repeatable success warrants scheduling or a durable staff role.

Do not market a financial result from disconnected telemetry, treat a drafted message as sent, or treat an agent run as a sale. A high-scoring automation idea may still be prohibited by privacy, consent, legal or owner-reserved-power rules.

## 8. Deliverables, completion test and re-audit

Deliver a **private source inventory and coverage manifest**, **portfolio/business/asset matrix**, **routine-blueprint and renewal map**, **workforce assignment/schedule proposal**, **routine measurement plans**, **evidence and contradiction register**, **decision cards**, and **7/30/90-day sequence** tied to the owner's actual outcomes. Record unreviewed content, unavailable accounts and stale evidence rather than filling gaps with invention.

An audit is complete enough to enter Stage 7 only when:
- every granted source is inventoried or explicitly unavailable, with pagination and content-review coverage disclosed;
- businesses and major operating areas are represented or explicitly excluded;
- recurring work and owner bottlenecks have source references and a current/old distinction;
- proposed workers have a bounded supervisor, scope, capability, authority, cost and acceptance;
- proposed schedules have owner, OpenClaw activation path, Focusa assignment ref, dependency, quiet hours, idempotency, overlap/missed-run policy, failure alert, rollback and revocation;
- each material routine has a baseline/measurement plan for outcomes, reliability, cost and owner attention/capacity;
- economic/life outcomes are distinguished from activity and system health;
- contradictions and unknowns are visible and prioritized;
- no external mutation occurred during discovery absent a separate exact approval;
- the owner can review one viable first pilot and its proof gate without another exhaustive interview.

Refresh by **delta**, not a blind complete re-ingest: compare source revision and current owner decision, recheck high-risk/expiring records, record supersession and revoked grants, and preserve a prior audit's evidence handles. Re-audit after material business change, onboarding, scope correction or failed acceptance. Store canonical facts in their owning product and a bounded source-linked synthesis in the owner-private knowledge surface; never create a second cross-business authority database just for this audit.

## Placement and ownership

This procedure **decomposes Golden Path Stage 5** in [`02-agent-os-golden-path-ordered-tasks.md`](./02-agent-os-golden-path-ordered-tasks.md) and feeds its accepted requirements into Stage 7 Workforce Composer. It does not duplicate Focusa's Workpoint/authority store, the customer CRM, W.I.N.S. outcomes, Google Drive, or Wirebot's private memory. Exact collection adapters and product API/CLI operations remain owned by their products and are verified live per deployment.
