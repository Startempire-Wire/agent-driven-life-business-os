# SOVOS Life Workforce Catalogue — composable worker profiles and customer outcomes
**Status:** proposed portable **source-design catalogue**, not proof of deployed workers, live integrations, public availability, legal services or entitlement.  
**Prepared:** 2026-11-12 · **Related:** [SOVOS #38](https://github.com/Startempire-Wire/agent-driven-life-business-os/issues/38), [Wirebot website #92](https://github.com/Startempire-Wire/wirebot-core/issues/92), [Wirebot App PR #21](https://github.com/Startempire-Wire/Wirebot-App/pull/21).  
**Canonical authorities:** `OWNER_AUTHORITY_CONSTITUTION.md`, `SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md`, `SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md`, `SOVOS_INFORMATION_INFRASTRUCTURE.md`, `CURRENT_ECOSYSTEM_ARCHITECTURE.md`, `SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md`.  
**Pattern copied from:** [business/general workforce catalogue #09](09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md), including its CRIST, lifecycle/state codes, capability bundles, least-authority commissioning, canonical roster manifest and outcome-acceptance rules.

## 1. Product thesis and limits
An owner should be able to employ the **coordination, research, scheduling, memory-assisted follow-through and organization** of a sophisticated private life staff—*without having to oversee each handoff*. This raises actual quality of life, time, family attention and meaningful experiences alongside business success. Neither AI nor software physically parents a child, cooks a meal, drives a car, acts as a doctor, replaces friendship, or guarantees bookings. Some completed experiences require explicitly authorized human service providers.

**Role profile is not an employee, schedule, runtime, permission, credential, client identity, or purchase entitlement.** Workforce Composer recommends an economical composition from owner-consented discovery. Focusa binds governed Workstream/CRIST/Workpoint/CallGraph work. OpenClaw supplies applicable durable automations; UIAI or typed domain adapters perform permitted actions. Source systems and owner acceptance establish outcome truth. No parallel stores.

## 2. Reusable employment contract
Every selected life worker uses the existing business catalogue's full/delta/inherited/deterministic **CRIST** packet:
- **Context:** exact owner, life-domain scope, outcome, source coverage, third-party consent and current limits.
- **Role:** immutable template reference/version, approved objective, supervisor, bundles, allowed systems/data/actions, budget, duration and escalation.
- **Interview:** only missing consequential information; never create forced questionnaires for everyday work.
- **Spec:** accepted output, steps, source-of-truth system, time/cost bounds, failure/rollback, proof, human decision classes.
- **Tasks:** dependency-ordered ready work with exact done conditions; Focusa is the authority, not a copied website or UI roster.

**Lifecycle** (matching #09): `F` flash task; `S` session; `C` campaign/project; `P` standing role contract with episodic execution; `E` emergency/incident. **State** is separately stateless/receipt-only, checkpointed, or client-scoped durable—with correctable consented metadata in canonical sources. Standing role ≠ process permanently running; dormant roles incur no routine token spend. Choose shortest state/lifetime that fits.

**Assignment statuses:** required staff, scheduled worker, on-demand bench, pilot, conditional, blocked, excluded, unknown. New third-party data, higher consequence, spending, send, booking, unlocking/actuation, recording, recurring surveillance or information sharing always requires its actual owner-governed grant, not just a remembered preference.

## 3. Capability bundles grounded in existing catalogues
Reuse `F-DISC` discovery; `F-SCOPE` project and scope; `F-TRAJ` direction; `F-WP` Workpoints; `F-FOCUS` current state; `F-EXEC` Workset/CallGraph/background jobs; `F-LOOP` continuous-work controls; `F-SILENT` session lifecycle; `F-EVID` evidence; `F-CTX` bounded context; `F-TIME` temporal authority; `F-LEARN` prediction/metacognition; `F-RUNTIME` integrity; `F-SEC` credentials/communications; `F-COCKPIT` read-only operations; `F-DX` diagnostics. UIAI: `U-RESEARCH`, `U-READ`, `U-ACT`, `U-EVID` among others. **These are semantic bundles and selected source-verified tool names—not blanket availability or access grants.**

**Source check:** Focusa `docs/current/focusa-tool-contracts.json` presently contains 157 **static** contracts (`spec90.tool_contracts.v1`) and product-owned `apps/pi-extension/src/tool-contracts.ts`; the SOVOS business catalogue recorded an older 2026-09-13 capability snapshot. Examples present in current static contracts: `focusa_project_identity`, `focusa_project_verify`, `focusa_trajectory_view`, `focusa_trajectory_assess`, `focusa_context_cognition_curate`, `focusa_temporal_authority`, `focusa_workpoint_checkpoint`, `focusa_workpoint_resume`, `focusa_callgraph_validate`, `focusa_callgraph_observe`, `focusa_silent_sessions`, `focusa_evidence_capture`, `focusa_workpoint_link_evidence`, `focusa_credentials_verify`, `focusa_browser_workflow_plan`, `focusa_metacog_retrieve`, `focusa_predict_record`. **Static registry is source evidence, not customer runtime verification.** Dynamically discover exact schema, route, side-effect profile and installed/admitted status prior to commissioning. OpenClaw/Home Assistant/Alexa/Echo Dot/car/calendar/booking/cooking/IoT are **separate candidate adapters**, not Focusa tool names.

### 3.1 Tool choreography by task, not role-title
| Need | Focusa operations/families | Real effect owner |
| --- | --- | --- |
| New scoped life outcome | `focusa_project_verify`, `focusa_trajectory_view`, `focusa_trajectory_assess`, `focusa_project_genesis` when applicable | Owner + Focusa governed work |
| Bound worker's context | `focusa_context_cognition_curate`, `focusa_workpoint_resume`, scoped Portable Memory projection | Owner data systems / privacy owner |
| Schedule or expectation | `focusa_temporal_authority`; routine compiler D2/D3 trigger policy | OpenClaw/provider/native scheduler under grant |
| Multi-worker campaign | `focusa_callgraph_validate`, `focusa_workset_projection`, `focusa_callgraph_observe`, `focusa_silent_sessions` | Focusa work/run authority; Wirebot Composer |
| Browser-dependent operation | `focusa_browser_workflow_plan`; UIAI `U-READ/U-ACT/U-EVID` after typed API check | Actual external provider |
| Sensitive access | `focusa_credentials_verify` and owning consent/credential authorization | Source owner/credential broker |
| Evidence / repeat learning | `focusa_evidence_capture`, `focusa_workpoint_link_evidence`, `focusa_predict_evaluate`, metacog review | Source domain + owner-accepted outcome |

## 4. Proposed life worker master grid
The same profile columns as catalogue #09 apply. `P` standing *role*, not permanent computation. Specific actions remain conditional on verified adapters and permission.
| ID | Life worker | Customer result | Focusa bundles | UIAI bundles | Life/state | Activation |
| --- | --- | --- | --- | --- | --- | --- |
| `LIF-01` | Personal Life Chief of Staff | A coherent personal agenda with important responsibilities and chosen experiences actually advanced | `F-TRAJ/F-CTX/F-TIME/F-WP/F-EVID/F-COCKPIT` | `U-RESEARCH` | `P` / client-scoped durable | event, weekly review, on-demand |
| `LIF-02` | Personal Administrative Steward | Personal correspondence, appointments and obligations organized with fewer owner interruptions | `F-FOCUS/F-CTX/F-TIME/F-EVID` | `U-READ/U-ACT` | `P` / client-scoped durable | event, schedule, on-demand |
| `LIF-03` | Relationship Steward | Thoughtful, owner-directed contact and meaningful opportunities to reconnect | `F-CTX/F-TIME/F-LEARN/F-EVID` | `U-RESEARCH` | `P` / selective preferences; no third-party dossier | owner declaration, bounded periodic review |
| `LIF-04` | Social Circle Coordinator | A group gathering brought from intention to confirmed arrangements | `F-TRAJ/F-TIME/F-WP/F-EVID/F-EXEC` | `U-RESEARCH/U-READ/U-ACT` | `C` / event-scoped checkpoints | on-demand/event |
| `LIF-05` | Occasion & Gift Steward | Important celebrations remembered and thoughtful gifts prepared | `F-TIME/F-CTX/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `P` / owner-scoped recurring dates | calendar/renewal/event |
| `LIF-06` | Event & Celebration Producer | A meaningful occasion planned with guests, venue, budget and contingency | `F-SCOPE/F-TRAJ/F-WP/F-EXEC/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `C` / project checkpoint | accepted event project |
| `LIF-07` | Hospitality & Hosting Coordinator | Visitors comfortably hosted with practical arrangements handled | `F-CTX/F-TIME/F-EVID` | `U-RESEARCH` | `S` / event-scoped minimal state | owner-planned visit |
| `LIF-08` | Travel Concierge | A coherent trip prepared with researched options and confirmed reservations when authorized | `F-TRAJ/F-TIME/F-WP/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `C` / itinerary and booking checkpoint | trip request, travel-change event |
| `LIF-09` | Local Experience Curator | Suitable leisure experiences selected for available time, interests and budget | `F-CTX/F-TIME/F-EVID` | `U-RESEARCH` | `F` / stateless/receipt-only | on-demand |
| `LIF-10` | Family Schedule Manager | Family obligations aligned into an actionable, conflict-aware schedule | `F-TIME/F-CTX/F-EVID` | `U-READ/U-ACT` | `P` / family-scope durable | calendar changes, daily reconciliation |
| `LIF-11` | Childcare Logistics Coordinator | Authorized adult caregivers, pickups and care arrangements coordinated | `F-TIME/F-SEC/F-EVID/F-WP` | `U-READ/U-ACT` | `P` / restricted family logistics records | event, schedule, emergency escalation |
| `LIF-12` | School & Activities Coordinator | School deadlines, extracurricular commitments and parent logistics followed through | `F-TIME/F-CTX/F-EVID` | `U-READ/U-ACT` | `P` / student-scoped durable | calendar, bounded inbox events |
| `LIF-13` | Elder-Care Logistics Coordinator | Appointments, household help and caregiver communications coordinated respectfully | `F-TIME/F-SEC/F-EVID` | `U-RESEARCH/U-READ` | `P` / separately consented care-scope state | event, schedule |
| `LIF-14` | Pet-Care Coordinator | Pet needs, visits and delegated care scheduled with fewer missed tasks | `F-TIME/F-CTX/F-EVID` | `U-RESEARCH/U-ACT` | `P` / household pet record scope | due date, request |
| `LIF-15` | Household Operations Manager | Household services and responsibilities coordinated without repeated owner micromanagement | `F-TRAJ/F-TIME/F-EXEC/F-EVID` | `U-READ/U-ACT` | `P` / household-scoped durable | schedule/event/exception |
| `LIF-16` | Home Maintenance Steward | Repairs and preventative maintenance kept current | `F-TIME/F-CTX/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `P` / property-scoped maintenance ledger references | equipment-event, schedule |
| `LIF-17` | Home Inventory & Warranty Clerk | Important household assets and their coverage easy to locate | `F-CTX/F-EVID/F-WP` | `U-READ` | `C` / document-index checkpoints | document upload/on-demand |
| `LIF-18` | Home Automation Coordinator | Owner-selected comfort and convenience automations proposed and operated within safety rules | `F-RUNTIME/F-TIME/F-SEC/F-EVID` | `U-READ/U-ACT` | `P` / scoped device state projections | device event, schedule, approved command |
| `LIF-19` | Energy & Comfort Steward | Comfort preferences met while avoiding waste and unnecessary interventions | `F-TIME/F-LEARN/F-EVID` | `U-READ` | `P` / minimal telemetry with retention | schedule, conditions |
| `LIF-20` | Home Safety & Incident Coordinator | A verified home alert routed to an appropriate adult with clear next steps | `F-SEC/F-TIME/F-EVID/F-DX` | `U-READ` | `E` / incident evidence only | trusted alert |
| `LIF-21` | Meal Planning Steward | An achievable week's meals and shopping list suited to preferences | `F-CTX/F-TIME/F-EVID` | `U-RESEARCH` | `P` / owner preferences and periodic plans | weekly schedule/on-demand |
| `LIF-22` | Chef & Grocery Service Coordinator | Ingredients, delivery and qualified human cooking services coordinated | `F-TRAJ/F-SEC/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `C` / order/appointment checkpoints | meal plan/owner request |
| `LIF-23` | Dinner Party Menu Producer | A guest-conscious menu and food-production run sheet ready for host or caterer | `F-CTX/F-TIME/F-EVID` | `U-RESEARCH` | `S` / event-scoped limited state | planned meal event |
| `LIF-24` | Health Appointment Coordinator | Medical appointments and pre-visit paperwork organized | `F-TIME/F-SEC/F-EVID` | `U-RESEARCH/U-READ` | `P` / sensitive care-scope references | due date, owner request |
| `LIF-25` | Movement & Recreation Planner | Enjoyable recreation and personally chosen activity time planned | `F-TIME/F-CTX/F-EVID` | `U-RESEARCH` | `P` / low-sensitivity interests | weekly review/on-demand |
| `LIF-26` | Care Reminders Steward | Owner-prescribed care-related reminders delivered and exceptions escalated | `F-TIME/F-SEC/F-EVID` | `U-READ` | `P` / restricted reminders only | approved schedule/exception |
| `LIF-27` | Personal Finance Administrator | Bills, renewal evidence and financial documents organized for owner decisions | `F-TIME/F-SEC/F-EVID` | `U-READ` | `P` / restricted financial-scope references | statement event, scheduled review |
| `LIF-28` | Household Expense & Subscription Watch | Wasteful renewals and anomalies surfaced before they become unnoticed costs | `F-TIME/F-LEARN/F-EVID` | `U-RESEARCH/U-READ` | `P` / minimal recurring-obligation state | renewal event/monthly review |
| `LIF-29` | Personal Records & Identity Steward | Important documents indexed with renewal reminders and privacy controls | `F-TIME/F-SEC/F-EVID` | `U-READ` | `P` / encrypted/ref-only sensitive metadata | document updates/renewal |
| `LIF-30` | Learning & Study Guide | A chosen subject progressed into retained understanding and useful practice | `F-TRAJ/F-CTX/F-LEARN/F-EVID` | `U-RESEARCH` | `P` / owner-scoped learning goals/progress | session/weekly review |
| `LIF-31` | Creative Project Producer | A personal book, artwork, video or hobby project advanced to finished artifacts | `F-TRAJ/F-WP/F-EXEC/F-EVID` | `U-RESEARCH/U-READ` | `C` / project checkpoint | accepted project milestones |
| `LIF-32` | Personal Historian & Memory Curator | Selected personal stories and records organized for the owner's future use | `F-CTX/F-WP/F-EVID` | `U-READ` | `C` / private curated references | owner-supplied content |
| `LIF-33` | Community & Volunteer Coordinator | Service commitments and community opportunities progressed into real participation | `F-TRAJ/F-TIME/F-EVID` | `U-RESEARCH/U-ACT` | `C` / event-specific checkpoints | owner goal/opportunity event |
| `LIF-34` | Personal Shopping & Gift Researcher | A well-matched shortlist or authorized purchase prepared without endless browsing | `F-CTX/F-EVID` | `U-RESEARCH/U-READ` | `F` / stateless/receipt-only | on-demand |
| `LIF-35` | Transportation & Ride Coordinator | Ground transportation arranged with pickup, accessibility and fallback understood | `F-TIME/F-EVID/F-SEC` | `U-RESEARCH/U-READ/U-ACT` | `S` / journey-scoped state | appointment/travel event |
| `LIF-36` | Vehicle Maintenance Steward | Vehicle servicing, documents and maintenance exceptions tracked | `F-TIME/F-CTX/F-EVID` | `U-RESEARCH/U-READ` | `P` / vehicle-scoped metadata | due-date/service event |
| `LIF-37` | Moving & Relocation Producer | Move milestones, vendors, utilities and family logistics coordinated | `F-TRAJ/F-WP/F-EXEC/F-EVID` | `U-RESEARCH/U-READ/U-ACT` | `C` / project checkpoints | accepted move project |
| `LIF-38` | Personal Emergency Preparedness Steward | Household plans, contacts and supplies kept accessible and reviewed | `F-TIME/F-SEC/F-EVID` | `U-RESEARCH` | `P` / restricted emergency-plan references | quarterly review/verified alert |
| `LIF-39` | Household Human Staff Coordinator | Authorized cleaners, caregivers, cooks and contractors coordinated as a team | `F-EXEC/F-TIME/F-SEC/F-EVID` | `U-READ/U-ACT` | `P` / vendor roster refs and service receipts | scheduled service/exception |
| `LIF-40` | Personal Technology & Digital Steward | Owner devices, subscriptions and digital services kept understandable and maintainable | `F-DISC/F-DX/F-SEC/F-EVID` | `U-READ` | `P` / owner/device-scoped inventory | device change, monthly review |
| `LIF-41` | Privacy & Consent Coordinator | Personal and household sharing preferences honored across worker assignments | `F-SEC/F-RUNTIME/F-EVID` | `U-READ` | `P` / policy refs; no duplicate consent ledger | assignment preflight/review |
| `LIF-42` | Experience Reflection & Renewal Steward | Useful feedback turns completed experiences into better future choices | `F-LEARN/F-CTX/F-EVID` | `U-READ` | `P` / owner-controlled preference feedback | completed experience/optional review |
| `LIF-43` | Life Goals & Seasons Planner | Longer-term personal aims translated into achievable seasons and milestones | `F-TRAJ/F-CTX/F-TIME/F-EVID` | `U-RESEARCH` | `P` / owner-defined goals in canonical systems | quarterly review/on-demand |
| `LIF-44` | Personal Correspondence Companion | Human relationships supported with thoughtfully drafted, owner-approved messages | `F-CTX/F-EVID` | `U-READ` | `F` / stateless/receipt-only | owner-requested message |
| `LIF-45` | Caregiver Handoff Coordinator | Consenting caregivers receive the correct minimum instructions at the right time | `F-SCOPE/F-TIME/F-SEC/F-EVID` | `U-READ` | `C` / care-event checkpoints | authorized care event |
| `LIF-46` | Life Interface & Device Adaptation Steward | One approved life role remains accessible through web, voice, home, mobile and car without changing identity or grants | `F-DISC/F-RUNTIME/F-SEC/F-EVID` | `U-READ` | `P` / interface-capability refs, minimal session state | user request/device availability |

## 5. Detailed reusable worker profiles
Every profile below specifies a scenario, task pattern, permitted source class, consequences, and independently reviewable acceptance. **No role self-activates from this document.**

### Executive & direction

#### LIF-01 — Personal Life Chief of Staff
- **Outcome sold:** A coherent personal agenda with important responsibilities and chosen experiences actually advanced.
- **Illustrative scenario (not a customer claim):** Owner says they want more time with family; coordinate household, social and travel work without turning freed time into more business.
- **Employment / state:** `P` standing owner-approved role; execution episodic; client-scoped durable. Activation: event, weekly review, on-demand.
- **Tool/capability contract:** Focusa `F-TRAJ/F-CTX/F-TIME/F-WP/F-EVID/F-COCKPIT`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** goals; owner-approved calendars; delegated worker status. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** direction, priorities and high-consequence spending. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** accepted priorities; verified completed delegated outcomes; exception brief. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-02 — Personal Administrative Steward
- **Outcome sold:** Personal correspondence, appointments and obligations organized with fewer owner interruptions.
- **Illustrative scenario (not a customer claim):** Prepare important forms, sort authorized correspondence and follow through on renewals.
- **Employment / state:** `P` standing owner-approved role; execution episodic; client-scoped durable. Activation: event, schedule, on-demand.
- **Tool/capability contract:** Focusa `F-FOCUS/F-CTX/F-TIME/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** scoped mail, calendar, documents, renewal records. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** external sends, legal declarations and irreversible document edits. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** review queue; approved sends/updates; closed obligation receipts. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-43 — Life Goals & Seasons Planner
- **Outcome sold:** Longer-term personal aims translated into achievable seasons and milestones.
- **Illustrative scenario (not a customer claim):** Plan the next quarter around family time, learning and one meaningful journey.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner-defined goals in canonical systems. Activation: quarterly review/on-demand.
- **Tool/capability contract:** Focusa `F-TRAJ/F-CTX/F-TIME/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner-stated values and constraints. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** never dictate the owner's purposes or infer mental state as fact. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** accepted milestones, real progress, revised priorities. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-44 — Personal Correspondence Companion
- **Outcome sold:** Human relationships supported with thoughtfully drafted, owner-approved messages.
- **Illustrative scenario (not a customer claim):** Draft a thank-you note, family update, or difficult but respectful invitation.
- **Employment / state:** `F` task-bounded flash worker; stateless/receipt-only. Activation: owner-requested message.
- **Tool/capability contract:** Focusa `F-CTX/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner-provided context and target relationship. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** human voice, sensitive interpersonal decisions and sends remain owner-approved. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** editable draft and exact approved delivery receipt if sent. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Relationships & social

#### LIF-03 — Relationship Steward
- **Outcome sold:** Thoughtful, owner-directed contact and meaningful opportunities to reconnect.
- **Illustrative scenario (not a customer claim):** Notice that an owner-approved friend catch-up is overdue and suggest a dinner, never silently contacting friends.
- **Employment / state:** `P` standing owner-approved role; execution episodic; selective preferences; no third-party dossier. Activation: owner declaration, bounded periodic review.
- **Tool/capability contract:** Focusa `F-CTX/F-TIME/F-LEARN/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner-provided relationship notes and consented dates only. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** relationships, intimacy, gifts and outreach remain human-led. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** owner accepted reconnect suggestion; consented communication receipt. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-04 — Social Circle Coordinator
- **Outcome sold:** A group gathering brought from intention to confirmed arrangements.
- **Illustrative scenario (not a customer claim):** Arrange five friends' dinner from voluntary availability, preferences and owner-approved invitations.
- **Employment / state:** `C` bounded project/campaign; event-scoped checkpoints. Activation: on-demand/event.
- **Tool/capability contract:** Focusa `F-TRAJ/F-TIME/F-WP/F-EVID/F-EXEC`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** limited participant responses; approved locations and availability. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no unsolicited invitations, scraping friends or fabricated reservations. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** agreed date; confirmations; venue status and owner handoff. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-05 — Occasion & Gift Steward
- **Outcome sold:** Important celebrations remembered and thoughtful gifts prepared.
- **Illustrative scenario (not a customer claim):** Plan an anniversary, propose gift options under a budget, obtain approval before purchase.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner-scoped recurring dates. Activation: calendar/renewal/event.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** consented birthdays, dates, budgets and gift preferences. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** purchases and sensitive personal inferences require approval. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** occasion plan; approved order tracking or explicit pending state. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-06 — Event & Celebration Producer
- **Outcome sold:** A meaningful occasion planned with guests, venue, budget and contingency.
- **Illustrative scenario (not a customer claim):** Coordinate a birthday weekend including invitations, suppliers and fallback weather plan.
- **Employment / state:** `C` bounded project/campaign; project checkpoint. Activation: accepted event project.
- **Tool/capability contract:** Focusa `F-SCOPE/F-TRAJ/F-WP/F-EXEC/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** event brief; guest consent; provider responses. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** all guest outreach, contracts and deposits require owner authority. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** event run sheet; supplier confirmations; reconciled budget. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-07 — Hospitality & Hosting Coordinator
- **Outcome sold:** Visitors comfortably hosted with practical arrangements handled.
- **Illustrative scenario (not a customer claim):** Prepare guest arrival plan, accessibility needs, menu and household preparation.
- **Employment / state:** `S` bounded working session; event-scoped minimal state. Activation: owner-planned visit.
- **Tool/capability contract:** Focusa `F-CTX/F-TIME/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** guest-submitted requirements; host preferences. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** never infer vulnerabilities; host confirms arrangements. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** welcome plan; agreed logistics; task completion evidence. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Travel & experiences

#### LIF-08 — Travel Concierge
- **Outcome sold:** A coherent trip prepared with researched options and confirmed reservations when authorized.
- **Illustrative scenario (not a customer claim):** Develop a family vacation itinerary and coordinate booking decisions without hiding travel costs.
- **Employment / state:** `C` bounded project/campaign; itinerary and booking checkpoint. Activation: trip request, travel-change event.
- **Tool/capability contract:** Focusa `F-TRAJ/F-TIME/F-WP/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** travelers' voluntarily provided requirements, passports only when essential. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** travel purchases, identity documents and cross-border decisions human-authorized. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** costed itinerary; real provider references; booking proofs where granted. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-09 — Local Experience Curator
- **Outcome sold:** Suitable leisure experiences selected for available time, interests and budget.
- **Illustrative scenario (not a customer claim):** Find a Saturday outing with driving, accessibility and budget constraints.
- **Employment / state:** `F` task-bounded flash worker; stateless/receipt-only. Activation: on-demand.
- **Tool/capability contract:** Focusa `F-CTX/F-TIME/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** approximate area, interests, restrictions, budget. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** availability and venue conditions must be checked; no silent booking. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** ranked options with sources; owner-selected next action. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Family & caregiving

#### LIF-10 — Family Schedule Manager
- **Outcome sold:** Family obligations aligned into an actionable, conflict-aware schedule.
- **Illustrative scenario (not a customer claim):** Reconcile school events, adult appointments and a weekend visit.
- **Employment / state:** `P` standing owner-approved role; execution episodic; family-scope durable. Activation: calendar changes, daily reconciliation.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** separately consented family calendars and scheduling rules. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** minors' data strictly scoped; no automatic custody decisions. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** resolved schedule proposal; approved updates and conflict receipts. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-11 — Childcare Logistics Coordinator
- **Outcome sold:** Authorized adult caregivers, pickups and care arrangements coordinated.
- **Illustrative scenario (not a customer claim):** Prepare pickup coverage with approved caregivers and confirmation checks.
- **Employment / state:** `P` standing owner-approved role; execution episodic; restricted family logistics records. Activation: event, schedule, emergency escalation.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID/F-WP`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** approved caregivers, emergency contacts, limited logistics. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** AI never supervises a child; safeguarding, custody and emergency decisions require responsible adults. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** explicit adult coverage acknowledgment; escalations; handoff confirmation. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-12 — School & Activities Coordinator
- **Outcome sold:** School deadlines, extracurricular commitments and parent logistics followed through.
- **Illustrative scenario (not a customer claim):** Surface consented school notices and prepare permission slips for parent review.
- **Employment / state:** `P` standing owner-approved role; execution episodic; student-scoped durable. Activation: calendar, bounded inbox events.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized school communications and calendars. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no signing for parent, impersonation or sharing child records broadly. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** reviewed notices; parent decisions; verified schedule/status. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-13 — Elder-Care Logistics Coordinator
- **Outcome sold:** Appointments, household help and caregiver communications coordinated respectfully.
- **Illustrative scenario (not a customer claim):** Organize rides and appointment details for a consenting older relative.
- **Employment / state:** `P` standing owner-approved role; execution episodic; separately consented care-scope state. Activation: event, schedule.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** adult's authorized care plan and family contacts. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no medical judgment, consent substitution, coercion or unauthorized disclosure. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** confirmed logistics and informed human-caregiver handoff. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-14 — Pet-Care Coordinator
- **Outcome sold:** Pet needs, visits and delegated care scheduled with fewer missed tasks.
- **Illustrative scenario (not a customer claim):** Arrange sitter, vaccination record reminder and vet visit transport.
- **Employment / state:** `P` standing owner-approved role; execution episodic; household pet record scope. Activation: due date, request.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-RESEARCH/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** pet care preferences and service-provider details. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** medical/medication decisions reserved for veterinarian/owner. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** care calendar; approved provider booking proof; exceptions. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-45 — Caregiver Handoff Coordinator
- **Outcome sold:** Consenting caregivers receive the correct minimum instructions at the right time.
- **Illustrative scenario (not a customer claim):** Prepare a limited appointment handoff to an authorized family caregiver.
- **Employment / state:** `C` bounded project/campaign; care-event checkpoints. Activation: authorized care event.
- **Tool/capability contract:** Focusa `F-SCOPE/F-TIME/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** consented specific care task and contact. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no medical delegation or child responsibility reassignment without qualified human. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** acknowledged handoff, unresolved exception and source-safe closure. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Home & property

#### LIF-15 — Household Operations Manager
- **Outcome sold:** Household services and responsibilities coordinated without repeated owner micromanagement.
- **Illustrative scenario (not a customer claim):** Coordinate cleaning, repairs, bills and staff arrival windows.
- **Employment / state:** `P` standing owner-approved role; execution episodic; household-scoped durable. Activation: schedule/event/exception.
- **Tool/capability contract:** Focusa `F-TRAJ/F-TIME/F-EXEC/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner premises/vendors; maintenance logs. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** contractor access, locks, payments and personal data require precise grant. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** household workboard; receipts; unresolved-item owner brief. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-16 — Home Maintenance Steward
- **Outcome sold:** Repairs and preventative maintenance kept current.
- **Illustrative scenario (not a customer claim):** Track HVAC service interval, compare qualified contractors and follow appointment through.
- **Employment / state:** `P` standing owner-approved role; execution episodic; property-scoped maintenance ledger references. Activation: equipment-event, schedule.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** asset inventory, warranties, vendor communications. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** home access, financial commitments and hazardous repairs human-handled. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** accepted repair status; contractor receipt; next inspection. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-17 — Home Inventory & Warranty Clerk
- **Outcome sold:** Important household assets and their coverage easy to locate.
- **Illustrative scenario (not a customer claim):** Index owner-approved appliance receipts, warranties and serial-number documents.
- **Employment / state:** `C` bounded project/campaign; document-index checkpoints. Activation: document upload/on-demand.
- **Tool/capability contract:** Focusa `F-CTX/F-EVID/F-WP`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized receipts and manuals. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** minimize serial numbers and financial information in worker context. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** source-linked inventory; warranty dates; owner export. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-18 — Home Automation Coordinator
- **Outcome sold:** Owner-selected comfort and convenience automations proposed and operated within safety rules.
- **Illustrative scenario (not a customer claim):** Use a verified Home Assistant adapter to run an approved evening lighting scene.
- **Employment / state:** `P` standing owner-approved role; execution episodic; scoped device state projections. Activation: device event, schedule, approved command.
- **Tool/capability contract:** Focusa `F-RUNTIME/F-TIME/F-SEC/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** device capabilities and owner-approved scene definitions. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** locks, alarms, ovens, heat, cameras and access are sensitive; fail closed; no imagined Home Assistant integration. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** device command and resulting device-state receipt or clear unavailable status. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-19 — Energy & Comfort Steward
- **Outcome sold:** Comfort preferences met while avoiding waste and unnecessary interventions.
- **Illustrative scenario (not a customer claim):** Recommend thermostat schedule based on explicitly allowed presence/preferences.
- **Employment / state:** `P` standing owner-approved role; execution episodic; minimal telemetry with retention. Activation: schedule, conditions.
- **Tool/capability contract:** Focusa `F-TIME/F-LEARN/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** limited environmental readings and household comfort policy. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** never silently override health/safety temperature constraints. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** policy-compatible recommendation; meter/device confirmation if integrated. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-20 — Home Safety & Incident Coordinator
- **Outcome sold:** A verified home alert routed to an appropriate adult with clear next steps.
- **Illustrative scenario (not a customer claim):** Surface a trusted smoke/water detector event, advise evacuation or professional help and notify configured recipient.
- **Employment / state:** `E` incident-bounded emergency workflow; incident evidence only. Activation: trusted alert.
- **Tool/capability contract:** Focusa `F-SEC/F-TIME/F-EVID/F-DX`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** verified incident alert, emergency contact policy. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** never promise emergency dispatch, physical rescue, or sensor reliability; fail safe. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** alert provenance; delivery result; responsible human handoff. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-46 — Life Interface & Device Adaptation Steward
- **Outcome sold:** One approved life role remains accessible through web, voice, home, mobile and car without changing identity or grants.
- **Illustrative scenario (not a customer claim):** Receive a spoken request on Echo Dot and continue review on Wirebot App; only execute devices through authenticated adapters.
- **Employment / state:** `P` standing owner-approved role; execution episodic; interface-capability refs, minimal session state. Activation: user request/device availability.
- **Tool/capability contract:** Focusa `F-DISC/F-RUNTIME/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** verified device/channel capabilities, owner session identity. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** voice speaker identity, vehicle motion and device actions must pass separate authorization; no blind relay. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** same work/intent ID across surfaces; safe fallback when adapter unavailable. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Meals & hospitality

#### LIF-21 — Meal Planning Steward
- **Outcome sold:** An achievable week's meals and shopping list suited to preferences.
- **Illustrative scenario (not a customer claim):** Prepare a simple five-night menu with budget and allergy constraints supplied by owner.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner preferences and periodic plans. Activation: weekly schedule/on-demand.
- **Tool/capability contract:** Focusa `F-CTX/F-TIME/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner-supplied dietary preferences, budget, kitchen inventory. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no medical nutrition treatment; confirm allergies and food safety. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** accepted menu; consolidated list; clear substitutions. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-22 — Chef & Grocery Service Coordinator
- **Outcome sold:** Ingredients, delivery and qualified human cooking services coordinated.
- **Illustrative scenario (not a customer claim):** Compare grocery fulfillment choices or prepare a brief for a human personal chef.
- **Employment / state:** `C` bounded project/campaign; order/appointment checkpoints. Activation: meal plan/owner request.
- **Tool/capability contract:** Focusa `F-TRAJ/F-SEC/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** shopping list; approved household service contact. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** AI does not physically cook; purchase and access approval required. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** confirmed delivery/service arrangement or actionable plan. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-23 — Dinner Party Menu Producer
- **Outcome sold:** A guest-conscious menu and food-production run sheet ready for host or caterer.
- **Illustrative scenario (not a customer claim):** Plan a six-person dinner with consented allergies, quantities and preparation timing.
- **Employment / state:** `S` bounded working session; event-scoped limited state. Activation: planned meal event.
- **Tool/capability contract:** Focusa `F-CTX/F-TIME/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** guest-provided restrictions, host cooking capabilities. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** unverified allergies or food safety assumptions escalate. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** approved menu; quantities; sourcing list; prep timeline. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Health & wellness logistics

#### LIF-24 — Health Appointment Coordinator
- **Outcome sold:** Medical appointments and pre-visit paperwork organized.
- **Illustrative scenario (not a customer claim):** Find available provider appointment options and compile questions for clinician.
- **Employment / state:** `P` standing owner-approved role; execution episodic; sensitive care-scope references. Activation: due date, owner request.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** consented healthcare contacts, scheduling constraints. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no diagnosis, treatment, medical advice or proxy medical consent. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** confirmed appointment when authorized; prepared question/record checklist. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-25 — Movement & Recreation Planner
- **Outcome sold:** Enjoyable recreation and personally chosen activity time planned.
- **Illustrative scenario (not a customer claim):** Plan accessible weekend walks, classes or hobbies around the owner's calendar.
- **Employment / state:** `P` standing owner-approved role; execution episodic; low-sensitivity interests. Activation: weekly review/on-demand.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** activity preferences and mobility limitations if supplied. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no exercise prescription for medical conditions. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** viable options; accepted calendar plan; feedback. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-26 — Care Reminders Steward
- **Outcome sold:** Owner-prescribed care-related reminders delivered and exceptions escalated.
- **Illustrative scenario (not a customer claim):** Remind an adult about an appointment or an existing clinician-directed medication schedule.
- **Employment / state:** `P` standing owner-approved role; execution episodic; restricted reminders only. Activation: approved schedule/exception.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** user-entered or clinician-documented reminder times. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no autonomous dose adjustment, medical advice, or claim care occurred without acknowledgment. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** delivery receipt; acknowledgment or missed-reminder escalation. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Money & records

#### LIF-27 — Personal Finance Administrator
- **Outcome sold:** Bills, renewal evidence and financial documents organized for owner decisions.
- **Illustrative scenario (not a customer claim):** Prepare a list of payments due, source links and which ones require review.
- **Employment / state:** `P` standing owner-approved role; execution episodic; restricted financial-scope references. Activation: statement event, scheduled review.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized account summaries and due-date records. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no unauthorized transfers, disputes, debt acknowledgment or disclosure. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** reconciled obligations; owner review list; source citations. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-28 — Household Expense & Subscription Watch
- **Outcome sold:** Wasteful renewals and anomalies surfaced before they become unnoticed costs.
- **Illustrative scenario (not a customer claim):** Identify an owner-authorized subscription renewal and assemble cancellation options.
- **Employment / state:** `P` standing owner-approved role; execution episodic; minimal recurring-obligation state. Activation: renewal event/monthly review.
- **Tool/capability contract:** Focusa `F-TIME/F-LEARN/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** scoped statements and service contracts. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no silent cancellation, refund claim or access termination. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** source-grounded renewal alert; approved action receipt. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-29 — Personal Records & Identity Steward
- **Outcome sold:** Important documents indexed with renewal reminders and privacy controls.
- **Illustrative scenario (not a customer claim):** Prepare a passport/insurance expiration review without copying credentials to a general worker.
- **Employment / state:** `P` standing owner-approved role; execution episodic; encrypted/ref-only sensitive metadata. Activation: document updates/renewal.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized document metadata, safe storage handles. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no raw identity-document dissemination, impersonation or application submission without consent. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** verified metadata index; deadlines; owner-held source links. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Learning & creativity

#### LIF-30 — Learning & Study Guide
- **Outcome sold:** A chosen subject progressed into retained understanding and useful practice.
- **Illustrative scenario (not a customer claim):** Build a six-week language learning plan with weekly review and exercises.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner-scoped learning goals/progress. Activation: session/weekly review.
- **Tool/capability contract:** Focusa `F-TRAJ/F-CTX/F-LEARN/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** learning goals, resources, accepted progress. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no fabricated mastery scores or educational credentials. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** completed practice deliverables; owner-recognized progress. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-31 — Creative Project Producer
- **Outcome sold:** A personal book, artwork, video or hobby project advanced to finished artifacts.
- **Illustrative scenario (not a customer claim):** Coordinate research, draft reviews and a home video project through delivery.
- **Employment / state:** `C` bounded project/campaign; project checkpoint. Activation: accepted project milestones.
- **Tool/capability contract:** Focusa `F-TRAJ/F-WP/F-EXEC/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner-created assets and permissions. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** copyright, likeness and publication remain owner-controlled. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** finished file; review receipt; publication only if authorized. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-32 — Personal Historian & Memory Curator
- **Outcome sold:** Selected personal stories and records organized for the owner's future use.
- **Illustrative scenario (not a customer claim):** Help assemble an oral-history collection from voluntarily shared interviews.
- **Employment / state:** `C` bounded project/campaign; private curated references. Activation: owner-supplied content.
- **Tool/capability contract:** Focusa `F-CTX/F-WP/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** explicitly consented photos, stories and interviews. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no covert recording, speculative biography or sharing of others' stories. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** editable source-linked archive with contributor permissions. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Purpose & community

#### LIF-33 — Community & Volunteer Coordinator
- **Outcome sold:** Service commitments and community opportunities progressed into real participation.
- **Illustrative scenario (not a customer claim):** Find a local volunteer day and coordinate the owner's approved signup.
- **Employment / state:** `C` bounded project/campaign; event-specific checkpoints. Activation: owner goal/opportunity event.
- **Tool/capability contract:** Focusa `F-TRAJ/F-TIME/F-EVID`; UIAI `U-RESEARCH/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** owner interests and approved organization list. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no unsolicited political/religious affiliation inference or signup. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** confirmed opportunity details, approved signup receipt. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-34 — Personal Shopping & Gift Researcher
- **Outcome sold:** A well-matched shortlist or authorized purchase prepared without endless browsing.
- **Illustrative scenario (not a customer claim):** Compare a durable home appliance against budget and owner preferences.
- **Employment / state:** `F` task-bounded flash worker; stateless/receipt-only. Activation: on-demand.
- **Tool/capability contract:** Focusa `F-CTX/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** item requirements, spend limit. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no automatic purchases, tracking of third parties or counterfeit claims. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** source-linked comparison; owner decision or approved purchase confirmation. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-42 — Experience Reflection & Renewal Steward
- **Outcome sold:** Useful feedback turns completed experiences into better future choices.
- **Illustrative scenario (not a customer claim):** After a group dinner, ask the owner whether it was worthwhile and whether another is wanted.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner-controlled preference feedback. Activation: completed experience/optional review.
- **Tool/capability contract:** Focusa `F-LEARN/F-CTX/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** optional feedback, accepted outcome. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no automated rating of friends or compulsive engagement loops. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** owner-accepted learning record and improved next proposal. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Mobility & travel

#### LIF-35 — Transportation & Ride Coordinator
- **Outcome sold:** Ground transportation arranged with pickup, accessibility and fallback understood.
- **Illustrative scenario (not a customer claim):** Coordinate a ride to an airport or medical appointment for a consenting adult.
- **Employment / state:** `S` bounded working session; journey-scoped state. Activation: appointment/travel event.
- **Tool/capability contract:** Focusa `F-TIME/F-EVID/F-SEC`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** limited pickup/dropoff and rider accessibility data. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no unsafe driving interaction or unverified booking. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** confirmed ride where authorized; live status only if actual source provides. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-36 — Vehicle Maintenance Steward
- **Outcome sold:** Vehicle servicing, documents and maintenance exceptions tracked.
- **Illustrative scenario (not a customer claim):** Prepare maintenance appointment when mileage/due signal is verified.
- **Employment / state:** `P` standing owner-approved role; execution episodic; vehicle-scoped metadata. Activation: due-date/service event.
- **Tool/capability contract:** Focusa `F-TIME/F-CTX/F-EVID`; UIAI `U-RESEARCH/U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** vehicle maintenance history and safe metadata. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no actuation of a moving vehicle or safety-critical control. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** service plan, verified booking and maintenance records. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-37 — Moving & Relocation Producer
- **Outcome sold:** Move milestones, vendors, utilities and family logistics coordinated.
- **Illustrative scenario (not a customer claim):** Organize a home move without missing address-change deadlines or appointments.
- **Employment / state:** `C` bounded project/campaign; project checkpoints. Activation: accepted move project.
- **Tool/capability contract:** Focusa `F-TRAJ/F-WP/F-EXEC/F-EVID`; UIAI `U-RESEARCH/U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized addresses, mover quotes and utilities. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** contracts, payments and disclosure of address require approval. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** reconciled move checklist, confirmed appointments, owner acceptance. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

### Safety & resilience

#### LIF-38 — Personal Emergency Preparedness Steward
- **Outcome sold:** Household plans, contacts and supplies kept accessible and reviewed.
- **Illustrative scenario (not a customer claim):** Prepare a family wildfire evacuation checklist and periodic replenishment prompts.
- **Employment / state:** `P` standing owner-approved role; execution episodic; restricted emergency-plan references. Activation: quarterly review/verified alert.
- **Tool/capability contract:** Focusa `F-TIME/F-SEC/F-EVID`; UIAI `U-RESEARCH` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** consented needs, contacts and safe plans. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no claim of emergency authority, dispatch, medical rescue or real-time monitoring without integration. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** owner-reviewed plan, verified supply list, last review. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-39 — Household Human Staff Coordinator
- **Outcome sold:** Authorized cleaners, caregivers, cooks and contractors coordinated as a team.
- **Illustrative scenario (not a customer claim):** Schedule a vetted cleaner and personal cook without overlapping access windows.
- **Employment / state:** `P` standing owner-approved role; execution episodic; vendor roster refs and service receipts. Activation: scheduled service/exception.
- **Tool/capability contract:** Focusa `F-EXEC/F-TIME/F-SEC/F-EVID`; UIAI `U-READ/U-ACT` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** approved workers, contracts and least data. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** employment law, background checks, child safety and payments remain proper human/provider functions. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** verified service schedule, human check-in, payment approval state. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-40 — Personal Technology & Digital Steward
- **Outcome sold:** Owner devices, subscriptions and digital services kept understandable and maintainable.
- **Illustrative scenario (not a customer claim):** Prepare home-network/device inventory and recommend backup or renewal steps.
- **Employment / state:** `P` standing owner-approved role; execution episodic; owner/device-scoped inventory. Activation: device change, monthly review.
- **Tool/capability contract:** Focusa `F-DISC/F-DX/F-SEC/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** authorized devices, versions and account metadata. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** no blanket LAN scanning, credential disclosure or automatic security changes. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** source-backed inventory, approved remediation receipts. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

#### LIF-41 — Privacy & Consent Coordinator
- **Outcome sold:** Personal and household sharing preferences honored across worker assignments.
- **Illustrative scenario (not a customer claim):** Review whether an outing worker needs every family member's calendar details.
- **Employment / state:** `P` standing owner-approved role; execution episodic; policy refs; no duplicate consent ledger. Activation: assignment preflight/review.
- **Tool/capability contract:** Focusa `F-SEC/F-RUNTIME/F-EVID`; UIAI `U-READ` only when a structured source interface cannot accomplish the authorized task. Selected actual tools must be discovered from the versioned contract registry, checked for grants and current runtime status; external provider actions are not supplied by Focusa merely because a bundle appears here.
- **CRIST inputs:** consent/grant refs, intended audience, data minimization. Compose with existing business `COS-01` / `EAA-01` / `TMP-01` / `AUT-01` / `EVD-01` / `OUT-01` as needed; do not duplicate their underlying authority.
- **Task/acceptance path:** resolve current goal and minimal evidence → select approved template/task pack → check source/permission/freshness → perform bounded read, proposal or accepted action → independently reconcile source → offer owner proof and next step.
- **Reserved human decisions / failure handling:** actual grants and policy remain with owners; no self-approval. Missing consent, integration, availability or contradictory evidence results in blocked/pending status, not invented success.
- **Done evidence:** privacy scope verdict, correction and revoke evidence. Report status as proposed, prepared, sent, confirmed, completed or blocked using the actual source; dispatch/booking attempt ≠ accepted outcome.

## 6. Life discovery → worker composition
1. Ask what **life the owner wants** (relationships, connection, family, household calm, learning, celebration, financial breathing room), not which AI job titles they want to buy.
2. Inventory only **consented** personal systems: calendars, household tasks, registered devices, vendor/service contacts, personal documentation, voluntary friend-group responses, family care scopes, and existing routines. Audit coverage and exclusions explicitly.
3. Distinguish actual observed recurring burdens from owner-declared aspirations and speculative archetype suggestions. No surprise social profiling or silent family-data imports.
4. Compute candidate **outcomes** and choose minimal role+task packs; reuse existing staff and deterministic operations before spinning up an agent army.
5. Propose flash/session for isolated task, campaign for one experience, standing role only for confirmed repeated need. Decide statefulness independently; keep third-party data at source with least projection.
6. Compile exact bounded routine through current Routine Compiler; owner grants applicable data/action permissions; Focusa validates Workstream/CRIST/CallGraph.
7. Run supervised pilot; verify outcome with original source and recipient; measure owner interruptions, elapsed time, spend, reliability and **felt margin** only when the owner reports it.
8. Retire, pause, replace, or reconfigure workers without erasing owner records, changing partner identity or leaving orphaned scheduled work.

## 7. Deterministic routines and alarms (not a generic always-on LLM)
An alarm means a **source-backed condition needing a permitted response**, not automatically an owner interruption. Prefer source event/webhook → source queue → condition watch → schedule → manual, with separate reconciliation jobs for missed signals. D3 deterministic actions, D2 deterministic shell with bounded semantic islands, D1 agent-led pilots, D0 human/manual. Unattended operation ordinarily requires proven D2/D3. Compiled instances bind timezone/DST, lease/idempotency, overlap, missed run, retries/backoff, quiet hours, budget, preflight, failure sink, expiry/revoke and evidence. The owner receives `Needs You` only for real decisions or failures.

Suggested reusable routines: personal morning briefing, appointment lead-time alerts, family conflict reconciliation, child pickup adult-confirmation check, social-date invitation follow-through, vendor confirmation, preventive home maintenance, grocery reorder review, medical visit preparation, subscription renewal exception, trusted home-sensor incident escalation, transport arrival exception, trip change monitoring, and post-event follow-through. Each remains conditional on the actual provider, consent, schedule and runtime.

## 8. Composability, portability, reusability, and whole-life interfaces
**Portable role =** versioned owner-neutral outcome contract + tool requirements + task-pack references + input/output schemas + acceptance + consequence classification, with no tenant secrets, vendor IDs, personally identifying defaults, or runtime bindings.
**Composed instance =** private owner identity, CRIST packet, canonical Workstream, admissible data refs, grants, budget, trigger, platform/adapter selection, accepted profile revision, stop and evidence.
**Swappable adapter =** provider-owned capabilities advertised with version and real proof. Swapping a Home Assistant service for another authorized home provider, a voice surface for mobile, or an LLM does **not** widen actions, change owner identity, silently migrate data, or corrupt accepted work. The target adapter must meet the same action/evidence/rollback contract before cutover.
**Interfaces** include Wirebot App web/PWA/mobile/desktop, voice (possible Echo Dot/Alexa-compatible connector), chat/Discord, local home panel, home automation platform, IoT event feeds, automotive-safe interfaces and human staff/vendor services. **These are candidate channels, not already implemented connectors.** Home commands should use typed source-native APIs rather than brittle browser automation where available. Wake word or speaker identity is not by itself consent. **In-car:** no distracting interactions or safety-critical actuation while driving; voice-only minimal disclosures where law/platform allow, nonessential actions defer until parked.
**Physical safety:** Locks, door codes, alarm disablement, cameras, heating/cooking and dangerous appliances require specific safety policy, device verification and stronger confirmation; ambiguous state fails closed. AI nanny/chef/driver is coordination software plus appropriate humans/robots only when separately proven.
**Third-party dignity:** Relationship memory stores only owner-contributed, directly relevant and authorized facts; friends and family are independent people with privacy rights. No hidden social surveillance, manipulation, stalking, automated intimacy or fabricated outreach. Minors and medical/financial information get strict compartmentalization and retention.

## 9. Wirebot App consumption contract (source-first)
Wirebot App `+ New helper` and `Workforce Composer` should **read this canonical versioned catalogue**, not copy its role truth into an App-specific hard-coded list. The GUI must show:
- Search by desired **result** (e.g. “plan a dinner”, “keep my home running”), with Life/Business/Both categories.
- Proposed shortest acceptable combination: existing worker / deterministic routine / temporary worker / standing role / mixed team / qualified outside human.
- Human-friendly description of what Wirebot handles, what the owner still decides, expected time/effort, requested permissions, recurring cost/runs and available proof.
- Actual role identity vs profile vs assignment vs worker run vs device adapter vs optional Network listing; clear `proposed`, `available`, `connected`, `admitted`, `running`, `blocked`, `stopped`, `verified` states.
- Swappable approved adapters and execution bodies with preflight, consent and rollback; mobile/keyboard/voice parity.
- One role/tab can be stopped without destroying the owner's persistent partner identity or historical accepted outcomes. Failed reconnection cannot create duplicate staff or hidden recurring costs.
- Provider-issued entitlements determine availability; five marketing models ≠ four setup modes ≠ technical entitlement levels 0–5.

See [Wirebot App PR #21](https://github.com/Startempire-Wire/Wirebot-App/pull/21); this document is architectural source and does not claim current UI/runtime support.

## 10. Three cross-worker example compositions
### A. Five friends. One great evening
Owner opts into a dinner for five friends. LIF-03 identifies a *user-declared* reconnection goal; LIF-04 coordinates consented availability; LIF-09 offers suitable venues; LIF-06 manages the event; LIF-35 arranges travel only if requested; LIF-42 asks owner whether it was meaningful. A P relationship role may delegate C event and F research workers. Consent precedes invitations; bookings and payments use approved providers; independent receipt determines what's confirmed. **Outcome:** owner enjoys an actual gathering, not an agent-activity dashboard.
### B. A home that runs without constant reminders
LIF-15 supervises LIF-16 maintenance, LIF-21 weekly menu, LIF-39 human providers, LIF-18 limited verified lighting scenes, LIF-28 renewal watch. Event-triggered deterministic reconciliations replace frequent LLM polling. Private role instances share only need-to-know refs; safety-critical IoT actions require extra grants. **Outcome:** documented completed household responsibilities and fewer owner escalations, not fictional robotic labor.
### C. Family trip without a coordination burden
LIF-08 handles itinerary, LIF-10 family schedule, LIF-11 authorized caregiving coverage, LIF-14 pet arrangements and LIF-35 transportation. Campaign worker stops after owner-accepted arrangements, while standing family role remains. **Outcome:** viable itinerary and verified arrangements; no claim any reservation occurred before provider confirmation.

## 11. Completion gates and unresolved runtime dependencies
- [ ] Validate every selected Focusa tool against **current installed** discovery/strict input-output schema and route; snapshot 157 static contracts is not runtime proof.
- [ ] Verify Home Assistant / Echo / IoT / vehicle adapter support separately; no unsafe default actuation.
- [ ] Prove exactly one real consented life outcome end-to-end: CRIST → approved roster → routine/worker admission → action/proof → independent owner acceptance → stop/revoke.
- [ ] Prove temporary/standing and stateless/checkpointed/durable worker pair with no cross-tenant or unauthorized family/friend data leakage.
- [ ] Demonstrate deterministic alarm absence/retry/reconciliation, quiet hours, budget and human escalation.
- [ ] Verify Wirebot App actually consumes versioned roles and supports connect/swap/stop/reconnect; cannot claim UI shipped from this doc.
- [ ] Reconcile worker templates with real model/SKU entitlements and commercial availability before website product promises.

**Source precedence:** SOVOS doctrine and existing workforce/routine contracts → Focusa exact work/tool authority → provider/device source truth → Wirebot App typed consumer → public website **verified** illustrative/real result presentation. Documentation is not deployment.
