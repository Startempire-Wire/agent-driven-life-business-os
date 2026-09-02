# Agent-Driven Life & Business OS

> A portable operating substrate for a sovereign human, an AI Chief of Staff,
> governed agent employees, real computers and tools, connected life/business
> systems, and evidence-backed learning.

- **Contract version:** `1.0.0`
- **Reference stack:** OpenClaw / Wirebot + Focusa + UIAI Engine + Veragensia
- **Primary contract:** [`AGENTS.md`](./AGENTS.md)

---

## Why this exists

Most “AI agent systems” start with a model and a pile of tools. That is not enough
for real life or business. A durable system also needs:

- a sovereign person or business owner;
- private, source-aware context;
- explicit goals and authority;
- bounded roles for human and AI workers;
- safe access to browsers, computers, APIs, and business systems;
- proof that work produced the requested outcome;
- correction, revocation, recovery, and learning loops;
- strict isolation between clients, projects, and trust classes.

This repository captures those **underlying primitives**. Verticals, models,
providers, products, and tools can change. The substrate remains stable.

It is based on a working Startempire reference architecture and intentionally
separates:

1. **portable core contracts** that any person or business can adopt;
2. **replaceable adapters** for products, providers, and vertical systems;
3. **runtime state** that must be discovered live rather than copied from docs.

## Outcomes Over Process

Prioritize working implementation and mission progress over ceremony.

> **Is this moving the mission forward, or am I creating work about the work?**

Prefer implementation over deliberation, simple solutions over elaborate ones,
existing primitives over new abstractions, and evidence from running systems over
theoretical proof. Process is valuable only where it protects authority, safety,
coordination, rollback, provenance, or delivery truth.

Ship the smallest correct solution. Verify it. Improve only where reality proves
necessary.

---

## The system at a glance

```text
SOVEREIGN HUMAN / BUSINESS OWNER
  values · goals · consent · correction · reserved powers
       ↓
PRIVATE CONTEXT + AI CHIEF OF STAFF
  signals · memory · synthesis · recommendations · exceptions
       ↓
GOVERNANCE / COHESION
  tenant · project · Trajectory · capabilities · Workpoints · budgets
       ↓
HUMAN TEAM + AGENT EMPLOYEES + COMPUTERS / TOOLS
       ↓
LIFE / BUSINESS SYSTEMS → EVIDENCE → OUTCOMES → LEARNING
```

The same loop works at three deliberately separated scales:

- **Personal life:** time, communication, learning, health, home, documents,
  finances, and commitments.
- **Business/portfolio:** customers, products, sales, delivery, code, websites,
  operations, finance, and teams.
- **Market/community:** opportunities, distribution, reputation, partnerships,
  education, and network effects.

Share proven contracts and skills across those scales—not ambient private memory
or authority.

---

## Reference implementation

The product names below are a concrete implementation, not mandatory vocabulary.
A client can replace an adapter while preserving its contract.

| Layer | Startempire reference | Responsibility |
|---|---|---|
| Sovereign principal | Sir V3 / authorized client owner | Goals, values, consent, corrections, reserved powers |
| AI Chief of Staff | OpenClaw + Wirebot/`wb` | Orient, synthesize, recommend, delegate, observe, escalate |
| Knowledge/context | Context Core + Agent-KB | Private memory, policy, topology, source-aware retrieval |
| Governance/cohesion | Focusa | Project identity, Trajectory, Workpoints, authority, evidence, learning |
| Agent computer | Veragensia | Provisioned, streamable, revocable execution environment |
| Browser/computer control | UIAI Engine | Observation, interaction, diagnostics, visual evidence |
| Agent workforce | Build agents, specialists, Pi workers, humans | Bounded execution under role contracts |
| Outcome ledger | WINS | Plan → Ship → Prove, corrections, confidence, economics |
| Outbound distribution | Wire Launch | Governed campaign execution and evidence |
| Inbound opportunity | WorkRouter | Provenance, qualification, matching, routing, outcomes |
| Portable trust | MeriFolio | Evidence-backed identity and selective disclosure |
| Health/recovery | Guardian + Focusa receipts + Wirebot audit | Diagnostics, audit, checkpoints, recovery |

### Division of responsibility

- The **Chief of Staff** coordinates; it does not silently become every worker.
- **Focusa** governs work; it does not become every product, CRM, or memory store.
- **UIAI Engine** supplies hands and eyes; machine access is not business authority.
- **Agent employees** execute scoped jobs; a role is not permission to access
  everything the Chief of Staff knows.
- **Business systems** remain authoritative for their own records.
- **Receipts and outcomes** connect the layers without duplicating authority.

---

## The portable substrate

These primitives should survive changes in vendors, models, verticals, and user
interfaces.

| Primitive | Required meaning |
|---|---|
| **Sovereign principal** | The person or entity with final authority, values, consent, and correction rights |
| **Identity and tenancy** | Stable client, principal, project, environment, and lifecycle boundaries |
| **Source and provenance** | Where information came from, when, its trust class, freshness, and supersession |
| **Context and memory** | Private, source-aware retrieval with retention and bounded disclosure |
| **Intent and Trajectory** | Desired state, current state, gap, constraints, and next direction |
| **Capability and policy** | Who may do what, to which resource, for how long, under which conditions |
| **Work unit** | Scoped objective, owner, dependencies, budget, and done-condition |
| **Orchestration** | Selection, sequencing, delegation, pause/resume, and escalation |
| **Execution adapter** | Typed tool, computer, browser, or API action with diagnostics |
| **Workforce role** | Job, supervisor, tools, limits, quality bar, escalation, and revocation |
| **Evidence and receipt** | Actor, authority, target, action, result, time, and supporting references |
| **Outcome and correction** | Accepted real-world effect, confidence, dispute, correction, and economics |
| **Learning and policy change** | Evaluation, reusable skill, approval, versioning, and rollback |
| **Observability and recovery** | Health, audit, retry, rollback, continuity, and incident response |
| **Resource and leverage** | Time, money, tokens, capacity, marginal value, and reinvestment |

### Common object envelope

Durable objects should carry the fields that apply to them:

```yaml
schema_version: example.v1
id: stable-identifier
scope: {tenant_id: client-or-household, project_id: exact-project}
owner_id: sovereign-or-delegate
actor_id: human-or-agent
status: active
provenance: {source_ref: evidence-ref, observed_at: 2026-01-01T12:00:00Z, trust_class: private}
authority_ref: capability-or-decision
related_refs: []
evidence_refs: []
correction_or_revocation_ref: null
```

The exact schema can vary. Stable identity, scope, authority, provenance, state,
and correction semantics cannot disappear.

---

## Chief-of-Staff operating contract

A capable AI Chief of Staff performs five loops:

1. **Orient** — assemble an accurate view of goals, commitments, customers, cash,
   risks, blockers, and opportunities.
2. **Recommend** — expose priorities, trade-offs, uncertainty, assumptions, and the
   shortest reliable path.
3. **Govern** — translate approved intent into exact projects, Trajectories,
   Workpoints, tasks, capabilities, budgets, and acceptance criteria.
4. **Delegate** — route each work unit to the owning person, business system, or
   agent employee with only the context and authority required.
5. **Observe and learn** — collect receipts, verify outcomes, escalate exceptions,
   capture corrections, and improve future execution.

Broad context does not imply broad execution. The Chief of Staff may understand
the whole portfolio while disclosing only a narrow slice to each worker.

### Reserved powers

Every deployment should explicitly list actions that remain human-controlled, such
as:

- destructive or irreversible changes;
- entering material legal or financial commitments;
- changing identity, ownership, or governance;
- granting broad or persistent credentials;
- publishing sensitive/private information;
- overriding safety or compliance controls;
- using emergency or nonrenewable authentication resources.

---

## Agents as employees

An agent employee is a **governed role**, not a personality with ambient access.
Start with one narrow job and real work. Expand only after safe escalation,
consumer acceptance, repeatable evidence, and useful economics.

### Employment packet example

```yaml
schema_version: agent_role.v1
role_id: client-onboarding-specialist
scope: {tenant_id: client-example, project_id: customer-onboarding}
owner_id: business-owner
supervisor_id: chief-of-staff
mission: Move an approved customer from signed agreement to verified kickoff.
inputs: [approved_customer_record, signed_scope, onboarding_checklist]
capabilities: [crm.customer.read, project.onboarding.create, calendar.kickoff.propose, email.draft]
prohibited: [send_without_approval, alter_signed_scope, cross_tenant_access, recovery_code_use]
budget: {time_minutes: 30, tool_calls: 60, spend_usd: 0}
acceptance: [project_created, fields_validated, kickoff_proposed, receipt_recorded]
escalate_when: [missing_input, scope_change, ambiguous_auth, low_confidence]
retention: minimum_required
revocation: immediate
```

### Capability grant example

```yaml
schema_version: capability_grant.v1
grant_id: grant-example-001
subject_id: client-onboarding-specialist
scope: {tenant_id: client-example, project_id: customer-onboarding}
resource: crm/customer/approved-record
actions: [read]
constraints: {customer_id: customer-123, expires_at: 2026-01-01T13:00:00Z, max_uses: 3}
evidence_policy: metadata_only
revocable: true
```

A capability is not a password. Credentials remain in the owning broker or provider
boundary; the agent receives the narrow ability to perform an approved action.

---

## Work and evidence lifecycle

```text
CAPTURE → ORIENT → DECIDE → PLAN → DELEGATE → ACT → PROVE → LEARN → COMPOUND
```

A consequential action should produce a durable receipt. Dispatch is not
completion, and a passing producer test is not proof that the consuming system or
customer received the outcome.

### Receipt example

```json
{
  "schema_version": "action_receipt.v1",
  "receipt_id": "receipt-example-001",
  "tenant_id": "client-example",
  "project_id": "customer-onboarding",
  "workpoint_id": "workpoint-example-001",
  "actor_id": "client-onboarding-specialist",
  "capability_ref": "grant-example-001",
  "action": "project.onboarding.create",
  "target_ref": "customer-123",
  "idempotency_key": "customer-123-onboarding-v1",
  "status": "completed",
  "started_at": "2026-01-01T12:00:00Z",
  "completed_at": "2026-01-01T12:00:04Z",
  "evidence_refs": ["evidence-example-001"],
  "outcome_ref": "outcome-example-001",
  "rollback_ref": "rollback-example-001"
}
```

### Delivery truth

Keep these states separate:

```text
source → released → installed → configured → deployed → visible → accepted
```

A commit is not a release. A release is not an installed runtime. An endpoint is
not a customer experience. “Done” means the requested destination and behavior are
verified with the appropriate runtime, visual, consumer, and outcome evidence.

---

## Replaceable vertical adapters

Vertical adapters connect real systems to the substrate. They may evolve without
changing sovereignty, identity, authority, Workpoint, receipt, or correction
semantics.

| Vertical | Example systems |
|---|---|
| Personal life | Calendar, email/SMS, documents, learning, health, home, devices |
| Customer operations | CRM, support, onboarding, proposals, contracts, scheduling |
| Revenue | Commerce, billing, accounting, subscriptions, payouts, tax |
| Product and delivery | Project management, repositories, CI/CD, websites, hosting |
| Workforce | Hiring, role packets, scheduling, reviews, payroll, contractors |
| Market | Research, campaigns, social, opportunities, partnerships, community |
| Infrastructure | Cloud, cPanel, containers, databases, networking, observability |

Every adapter declares its owner/source, schema/version, tenant/project and trust
scope, capabilities/consent, renewable authentication, typed inputs/outputs,
idempotency, budgets, evidence/redaction, and failure/retry/rollback/revoke/teardown
behavior. An adapter may consume substrate authority; it must never silently
redefine it.

---

## Security and tenancy

### Nonnegotiable boundaries

- Never automate with a nonrenewable resource.
- Never retrieve, inspect, request, expose, test, or use recovery codes.
- Transport, root, browser, CDP, machine, or API access is not authorization.
- Use renewable, revocable, least-privilege credentials and capabilities.
- Keep client credentials, memory, files, sessions, evidence, and audit records
  isolated.
- Never use one tenant's ambient context or authority for another.
- Unknown renewability, ownership, or consent fails closed.
- Public demo environments remain credential-free.
- Corrections and revocations are first-class durable events.

### Trust classes

A practical deployment distinguishes at least:

1. **Public** — safe for unrestricted disclosure.
2. **Customer-authorized** — scoped to a tenant and approved purpose.
3. **Private operator** — personal/portfolio context unavailable to customers.
4. **Credential-bearing** — isolated broker/provider boundary; never ordinary
   context.
5. **Emergency/break-glass** — operator-only, non-automatable resources.

Shared infrastructure is acceptable only when these boundaries are enforced and
proven end to end.

---

## Truth, uncertainty, and correction

Decision quality requires epistemic integrity:

- distinguish observed facts, source statements, inferences, assumptions, and
  unverified claims;
- expose material uncertainty and knowledge gaps where they affect action;
- cross-check high-impact claims against authoritative sources or running behavior;
- correct errors immediately and preserve the correction trail;
- never present partial knowledge as complete or speculation as fact.

Do not turn truthfulness into response theater. Routine internal checks need not be
narrated. Surface the uncertainty that changes a decision, then return to work.

---

## Minimum viable client deployment

Do not begin with dozens of agents and every connector. Begin with one useful,
auditable loop.

1. **Constitution:** name the principal/client; record goals, trust classes,
   reserved powers, auth, retention, correction, and revocation.
2. **Context:** connect only mission-required sources with provenance, freshness,
   ownership, disclosure, briefing, and correction rules.
3. **Governance:** create the exact Focusa project, canonical Trajectory, current
   Workpoint, capabilities, budget, done-condition, evidence, and escalation.
4. **Hands:** provide a private agent computer/browser or typed API; prove
   diagnostics, rollback, revocation, teardown, and brokered credentials.
5. **First employee:** hire one narrow role with minimum context/capability/budget;
   test success, ambiguity, denial, retry, escalation, and correction.
6. **Outcome loop:** complete real work; prove producer, consumer, runtime, visual,
   and business outcomes as applicable; measure value and risk.
7. **Compound:** version repeated success, retire stale access/process, and add
   roles/connectors/tenants only after isolation and economics hold.

A minimum viable system therefore has:

```text
1 principal + 1 client/tenant + 1 project + 1 Trajectory + 1 Workpoint
+ 1 agent role + 1 real connector + 1 verified outcome loop
```

---

## Operating rhythm

| Cadence | Loop |
|---|---|
| **Daily** | Refresh context/health → brief commitments, customers, cash, risks, opportunities → select Workpoint → delegate bounded work → observe exceptions → verify outcome/corrections |
| **Weekly** | Review outcomes over activity → compare expected/actual value and cost → revoke stale grants/process → promote proven skills → reallocate → expand only where evidence supports it |
| **Incident** | Stop affected mutation → preserve state/evidence → recover with exact identity/scope → fix canonical root cause → verify consumer/rollback behavior → add durable prevention |

---

## Porting this architecture

Treat a deployment as configuration of the substrate, not a fork of one person's
private operating state.

### Replace these bindings

| Reference binding | Client-specific replacement |
|---|---|
| Sir V3 | Authorized principal(s) and preferred address |
| Startempire tenant/project IDs | Customer-owned stable identifiers |
| Agent-KB/Context Core | Approved private knowledge and policy authority |
| OpenClaw/Wirebot | Approved Chief-of-Staff runtime/interface |
| Focusa | Focusa deployment and exact project governance |
| Veragensia/UIAI | Approved computer/browser execution environment |
| Provider adapters | Customer-owned calendar, CRM, finance, code, and operations systems |
| Credential broker | Customer-approved renewable authentication authority |
| WINS/outcome ledger | Customer outcome, correction, and evidence store |

### Never copy

- credentials, tokens, cookies, recovery artifacts, or device state;
- private operator/client memory;
- tenant IDs, project attachments, or old Workpoints;
- machine paths, ports, hostnames, or runtime health claims as standing truth;
- permissions merely because the reference deployment possessed them;
- incident snapshots as permanent architecture.

### Portable export checklist

- [ ] Core contract version selected.
- [ ] Principal, tenant, project, and ownership identities replaced.
- [ ] Local products/paths/endpoints moved into deployment configuration.
- [ ] Trust classes, reserved powers, retention, and revocation defined.
- [ ] Credentials excluded and secret scan passed.
- [ ] Focusa project, Trajectory, Workpoint, and task agree.
- [ ] Agent roles and capabilities are client-scoped.
- [ ] Producer and consumer tests pass.
- [ ] Recovery and teardown are proven.
- [ ] First real outcome is independently accepted.

---

## Repository structure

```text
.
├── README.md   # Explanatory architecture and adoption guide
└── AGENTS.md   # Normative operating contract for agents and harnesses
```

`README.md` explains the system. `AGENTS.md` governs agent behavior. Volatile
runtime state, credentials, customer data, and private operational runbooks do not
belong in this portable repository.

## Using and versioning `AGENTS.md`

Read it before deployment; preserve the portable core; replace client bindings;
install it through the harness's canonical instruction mechanism; mechanically
validate hard stops; exercise green, degraded, wrong-project, correction, auth,
delivery, and recovery scenarios; then review/version before distribution.

Semantic Versioning applies: **major** changes incompatible substrate/safety/
authority semantics; **minor** adds compatible primitives/adapters/workflows;
**patch** clarifies or repairs. Validated tags use `agents-contract-v1.0.0`.

---

## Anti-patterns

- One omnipotent agent holding every credential and every client's context.
- Chat or dashboards replacing project authority, delivery, or outcome evidence.
- Installed tools treated as authorized; agents inventing identity or continuity.
- Adapters creating parallel authority stores; source described as live prematurely.
- Scaling agents/process before tenant isolation, acceptance, and economics hold.

---

## Frequently asked questions

| Question | Answer |
|---|---|
| **Is this a software framework?** | Not alone. It is a portable contract/architecture; products implement its relationships and invariants. |
| **Chief of Staff or employee?** | The Chief of Staff orients/co-ordinates broadly; employees receive narrow jobs, context, capability, budget, and acceptance. Neither self-authorizes. |
| **Why Focusa?** | It binds project identity, Trajectory, Workpoints, authority, receipts, learning, recovery, and cross-agent continuity to the mission. |
| **Why UIAI/agent computers?** | Real outcomes often need observable browser/computer hands, diagnostics, and evidence—not API access alone. Machine access still is not authority. |
| **Can products change?** | Yes. Replacements must preserve identity, capability, evidence, correction, recovery, and tenancy contracts. |
| **Multiple clients?** | Only with proven isolation across credentials, memory, files, sessions, computers, Workpoints, evidence, audit, retention, and revocation. |
| **How much autonomy?** | The minimum for the role; expand after real outcomes, safe escalation, repeatability, and economics; revoke when need ends. |
| **What is done?** | The requested outcome exists on its requested surface and is verified across the applicable source, release, install, configuration, runtime, visual, consumer, and business layers. |

---

## Final principle

A trustworthy agent ecosystem is not built by giving a model everything. It is
built by connecting **sovereign intent** to **bounded authority**, **scoped work**,
**observable execution**, **durable proof**, **human correction**, and
**compounding learning**.

Build the smallest useful loop. Prove it in reality. Then scale what works.
