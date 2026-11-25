# Life Workforce Composer — portable App projections and swappable device adapters
**Date:** 2026-11-12 · **Status:** source-design integration contract, **not** evidence of implemented App/IoT integration.
**Parent:** [Life Workforce Catalogue](15-life-workforce-catalogue-and-composable-worker-profiles.md) · [Wirebot App + New Helper PR #21](https://github.com/Startempire-Wire/Wirebot-App/pull/21) · [SOVOS #38](https://github.com/Startempire-Wire/agent-driven-life-business-os/issues/38).

## 1. Architecture and truth boundaries
SOVOS is **doctrine and portable information/operating architecture**, not a second customer app or autonomous runtime. Wirebot App offers the owner-facing compositor; Wirebot Core owns Operating Partner relationship and permitted recommendation; Focusa Workstream/CRIST/Workpoint/CallGraph and Focusa Workforce own governed work and execution evidence; OpenClaw or the appropriate native owner schedules accepted routines; UIAI is a bounded browser/computer adapter; provider-owned apps own calendar/booking/devices/payments and customer domain truth. A profile is never an activated worker. Consumer applications may cache versioned read-only projections but do not create alternate authority/consent/memory/task ledgers.

Authoritative portable inputs:
- `workforce-templates/life-worker-catalogue.v1.json` — 46 outcome-defined owner-neutral profiles, state/lifetime and Focusa/UIAI bundle requirements.
- `workforce-templates/life-task-packs.v1.json` — 46 candidate task-pack drafts; not executable routine instances or provider operations.
- `contracts/sovos-life-workforce-catalogue.v1.schema.json` — schema for the role catalogue; version separately from App UI.
- `docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md` — canonical CRIST/workforce lifecycle and tool-choreography precedence.
- Focusa `docs/current/focusa-tool-contracts.json` — current **static** tool-contract projection, with live version/readiness checked at admission.

## 2. Headless projection API requirements (proposed consumer contract, not implemented endpoint)
A future authenticated API/CLI adapter should expose only approved readings and commands. **Names here describe semantic operations, not actual installed endpoints.**

| Logical operation | Data contract | Authority/result |
| --- | --- | --- |
| `catalogue.list` | version, role IDs, life domain, outcomes, tool requirements, explicit design/deploy status | Public generic catalogue may be read-only; no private client records |
| `composition.preview` | owner outcome + permitted scope + current tool readiness + existing roster | Returns minimal role/routine/team candidate, grants required, estimated effort and blockers; *proposal only* |
| `assignment.preflight` | exact owner, CRIST revision, role revision, tools, source scopes, budget, duration and model/deployment entitlement | Focusa/provider-granted admission verdict; no auto-create from preview |
| `assignment.commission` | accepted proposal ref + current grants and idempotency token | Focusa governed work/roster receipt, not a new App roster |
| `assignment.observe` | assignment/workstream/run refs | Evidence, status, budget, owner approval needs, last completed useful result |
| `assignment.pause|resume|stop|revoke` | exact role instance and action scope | Confirmed owning-system receipt, including cleanup of timers, grants and device subscriptions |
| `adapter.list|preflight|swap` | required capability, source/version/owner, effect/readiness and client consent | No device/voice provider inferred from template; swap requires re-verification and rollback |

All writes need authenticated principal, scoped policy, consequence classification, idempotency, audit and owner-controlled revocation. No direct browser-created alternative permission ledger. Error contract distinguishes `not_supported`, `not_installed`, `not_connected`, `consent_required`, `entitlement_missing`, `scope_denied`, `stale`, `temporarily_unhealthy`, `requires_human`, `pending_external_confirmation` and `verified_complete`. UI must not collapse these into "working".

## 3. App "+ New helper" UX (Life, Business or Both)
1. Owner chooses **the result**: "Arrange a meaningful dinner with five friends", "Keep the household running", "Prepare a trip", "Coordinate the kids' schedules" or enters a constrained goal. Show life and business as equally first-class options.
2. App reuses existing role/routine first. Recommend a flash worker, campaign worker, standing role, approved deterministic routine or small group. Show **what result, what Wirebot handles, what the owner still decides, first useful result, available proof**. Never pitch 46 agents as a mandatory bundle.
3. Expand a preview for data sources, consent, permissions, schedule/quiet hours, actual supported adapter, spend/inference limits, human provider roles and privacy. Keep a short main path, progressive disclosure for detail.
4. Only after explicit authorized commission, create/bind the real Focusa assignments, source-owned grants and routines. Tabs display actual work receipt and verified provider/device outcome, not a fabricated progress bar.
5. Accessible controls: pause/stop, correct a preference, grant/revoke a capability, swap role/worker/provider, inspect evidence, escalate to real human. Preserve cross-device continuity through stable work/intent IDs; app identity is not a specific device.
6. Show true provider readiness. Offer a useful **illustrative** blueprint when unsupported; never imply a real booking, IoT action or customer result occurred.

### State model
`catalogue_candidate → previewed → owner_accepted → preflight_passed → assigned → active → proposed_effect → authorized_effect → provider_confirmed → independently_accepted → completed`. Valid alternate states include `blocked`, `awaiting_owner`, `awaiting_provider`, `paused`, `stopped`, `revoked`, `failed_with_receipt`. Not every role requires every stage; do not imply a preview is authorization. Source-specific completion remains authoritative.

## 4. Portable component boundaries
A life role template is a **pure portable description**: stable ID/version, purpose, life domain, input/output contract, required tool families, risk class, CRIST requirements, owner-effort/approval pattern, state/lifetime, evidence and exit conditions. It contains **no** client secrets, friend records, home IP addresses, voice profiles, payment IDs or device commands.

A client assignment binds:
```yaml
schema_version: sovos.life_worker_assignment.proposed.v1
owner_ref: private-existing-canonical-owner
profile_ref: LIF-04@1.0.0
source_catalogue_ref: workforce-templates/life-worker-catalogue.v1.json
accepted_crist_ref: private-focusa-bound-packet
outcome_ref: private-source-owned-goal
data_scope_refs: [private-validated-scope]
authority_grant_refs: [private-existing-grants]
tool_requirement_refs: [F-TRAJ, F-TIME, F-EVID, U-RESEARCH]
adapter_selection_refs: [private-verified-calendar, private-verified-booking]
budget_ref: private-approved-budget
lifetime: campaign
state_policy_ref: private-expiring-project-state
approval_policy_ref: private-human-action-policy
acceptance_policy_ref: private-source-and-owner-check
status: illustrative_proposed_schema_only
```
This is a **schematic**, not a new runtime schema or claim of installed parser. Do not build an extra storage system to use it.

## 5. Swappable adapter contract for home, voice, car and other interfaces
A compatible adapter advertises `adapter_id/version`, `source owner`, `supported capability classes`, read/write consequence classification, required principal/device pairing, scopes, no-ambient-credential policy, event freshness, rate limits, budget class, correlation/receipt IDs, failure/retry/idempotency and safe unpair/rollback. **The consumer verifies live operation.**

| Candidate adapter | Example permitted use | Critical guard |
| --- | --- | --- |
| Home Assistant / compatible home hub | read entity state or trigger an owner-approved lighting scene | entity allowlist, authenticated local service and exact permission; dangerous devices require stronger checks |
| Alexa/Echo Dot or supported wake-word channel | interpret owner request and read back concise approved result | speaker/wake detection is *not* identity proof; no unauthorized household-member information |
| Mobile/web/desktop Wirebot App | preview worker, grant action, see proof and interrupt | same canonical partner and assignment IDs; app is a projection, not source authority |
| Vehicle / automotive-safe interface | simple voice response and deferred itinerary, parking or arrival logistics | no driving control, distracting UIs, unsafe voice leakage; defer high-consequence tasks |
| Calendar / mail / contacts / booking | authorized coordination, event proposals, owner-approved sends and real provider bookings | no fabricated availability, no social scraping, third-party opt-in, irreversible send/booking gate |
| Human service directory / contractor | prepare and request authorized caregivers, cooks, repair staff and event vendors | human validation, child safety, employment/vendor law, physical task not assigned to software |

**Swapping**: resolve old role assignment/work and source refs → discover new adapter capabilities → compare the required action/evidence semantics → get any necessary consent → stage and test read-only → route exact new operations → verify independent actual outcome and no duplicates → retire prior subscriptions/timers/grants only when safe; rollback to old adapter if result fails. Never silently migrate protected context or change model/voice controls as a substitute for provider approval. A swappable adapter is not a promise that any provider pair is interchangeable today.

## 6. Concrete end-to-end acceptance scenarios
**Social dinner:** A consented owner asks to gather five friends. `LIF-03` recognizes an owner-declared social goal, `LIF-04` coordinates explicitly permitted outreach/availability, `LIF-09` finds cited options, and `LIF-06` handles the approved reservation and event logistics **if a verified booking provider exists**. A receipt must separate suggested venue from requested booking from provider-confirmed booking. The owner determines social success, not the agent's messages.

**Home scene:** A consented person requests an evening ambiance scene through a supported voice entry. `LIF-46` binds session/intent and identity, `LIF-18` checks device allowlist and current source state, and a connected hub executes only an approved non-dangerous scene. Verify actual device response or report no connector. No unattended locks/ovens/alarms/cameras, no magic AI home-control claim.

**Family logistics:** `LIF-10` reconciles authorized calendars, `LIF-11` requests a known adult's confirmation for childcare pickup, and `LIF-15` coordinates household staff where delegated. Unknown confirmation is surfaced to a responsible adult; software does **not** assert a child is safe or alter custody.

**Worker portability:** Owner replaces a travel-provider adapter or moves Wirebot App from web to mobile. Accepted role identity, consent and work evidence retain canonical refs; incompatible capability triggers a transparent stop/reconfirm instead of making up completion.

## 7. Tests/acceptance before calling it integrated
- JSON catalogue schema validates; every profile/task-pack ID is unique and source-linked; every referenced Focusa/UIAI bundle exists in its authoritative source catalogue.
- Authenticated client role projection and machine-readable source version are reproducible; generic catalogue contains no private payload.
- Test Live vs Planned status on each adapter; absent integration is visibly absent.
- One real end-to-end owner-authorized task shows worker admission and provider/source-verified accepted outcome; another intentionally blocked run has honest failure.
- Prove a stateless flash worker and durable standing role cannot read each other's unrelated family/friend context; cross-tenant denial and revocation verified.
- Prove a device/voice swap, missed event reconciliation, and stopping all standing schedules/capabilities without losing retained accepted owner results.
- Verify desktop/mobile/keyboard accessible composition and clear owner approval flow.
- Compare commercial entitlements to actual contracts; neither marketing model naming nor UX selection mints authority.
- Record real source version, live route, runtime evidence, limitations and rollbacks before claiming deployment.

**Implementation responsibility:** SOVOS defines the transferable roles/policies; Wirebot App consumes them, Wirebot Core and Focusa remain system owners. This documentation creates **no new working API, scheduler, connector or GUI on its own**.
