# Agent-Driven Life & Business OS

> A portable operating substrate for a sovereign human, an AI Chief of Staff,
> governed agent employees, real computers and tools, connected life/business
> systems, and evidence-backed learning.

- **Repository contract version:** `3.3.0` (the checked-in `AGENTS.md`; host-local policy can differ and is not silently synchronized here)
- **README scope:** explanatory architecture and adoption guide; expanded 2026-09-12, not a live capability or fleet inventory
- **Reference stack:** OpenClaw / Wirebot + Focusa + UIAI Engine + Veragensia
- **Agent integration examples:** Claude Code, Letta, OpenCode, Pi and compatible harnesses; suitability and native governance integration must be verified in the actual deployment
- **Primary agent contract:** [`AGENTS.md`](./AGENTS.md)
- **Architecture authority constitution:** [`OWNER_AUTHORITY_CONSTITUTION.md`](./OWNER_AUTHORITY_CONSTITUTION.md)
- **Cryptographic authority profile:** [`CRYPTOGRAPHIC_AUTHORITY_PROFILE.md`](./CRYPTOGRAPHIC_AUTHORITY_PROFILE.md)
- **Agent Computer reference profile:** [`AGENT_COMPUTER_REFERENCE_PROFILE.md`](./AGENT_COMPUTER_REFERENCE_PROFILE.md)
- **Agent-driven setup:** [Golden Path](./AGENT_OS_GOLDEN_PATH.md) — 0.2.0 candidate with partial prototype proof, not a verified installer or client rollout
- **Ecosystem relationships:** [intent-led doctrine](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md#ecosystem-fit--preserve-the-parts-strengthen-the-connections) · [topology visual](./docs/agent-os-golden-path/04-agent-os-golden-path-ecosystem-topology-map.html) — products, deployment distinctions and diagnostic flow; not a new registry
- **Setup iteration tasks:** [ordered implementation list](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md)

---

## Reading this repository

**ADLBOS** means **Agent-Driven Life & Business OS**. It describes how a human,
Chief of Staff, workers, computers and existing systems cooperate; it is not a new
kernel, a replacement for every application, or proof that all described features
are deployed. The Startempire reference is concrete enough to guide engineering,
but client deployments retain their own owners, context, infrastructure and choices.

| If you need to understand… | Start here |
|---|---|
| Purpose, responsibilities and connections | This README: [system loop](#the-system-at-a-glance), [reference roles](#reference-implementation), [handoffs](#how-the-handoffs-connect) |
| Which actions an agent may take | [AGENTS.md](./AGENTS.md) and the deployment's current authority/grants |
| Who can decide architecture, and how identity is verified | [Owner constitution](./OWNER_AUTHORITY_CONSTITUTION.md) and [cryptographic profile](./CRYPTOGRAPHIC_AUTHORITY_PROFILE.md) |
| What an Agent Computer profile requires | [Agent Computer reference profile](./AGENT_COMPUTER_REFERENCE_PROFILE.md); feature-specific implementation and proof remain with its owners |
| How to adopt or operate the system | [Golden Path](./AGENT_OS_GOLDEN_PATH.md), its [working doctrine/task ledger](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md), and [server handoff](./docs/agent-os-golden-path/SERVER_AGENT_HANDOFF.md) |
| How the products and deployment choices relate | [Reference modes and surfaces](#reference-modes-and-surfaces), the [topology visual](./docs/agent-os-golden-path/04-agent-os-golden-path-ecosystem-topology-map.html), and the [product UI options audit](./docs/agent-os-golden-path/06-wirebot-product-ui-options-inventory-and-consolidation-audit.md) |
| How reusable AI employee roles/tasks are composed | [Composable AI Workforce Catalogue and Client Assignment Matrix](./docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md) |
| How the proposed Wirebot app may integrate Startempire Wire | [Wirebot Application Family and Startempire Wire Integration Architecture](./docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md) |
| What exists versus what still needs proof | [Evidence and implementation state](#evidence-and-implementation-state); live operational sources for the actual deployment |

These documents have different jobs. An architectural requirement, example object,
source file, passing test and installed working feature are not interchangeable.
Examples below explain contracts; they do not establish a second schema registry.

## Why this exists

Most “AI agent systems” start with a model and a pile of tools. That is not enough
for real life or business. A durable system also needs:

- a sovereign person or business owner;
- private, source-aware context;
- explicit goals and authority;
- bounded roles for human and AI workers;
- safe access to browsers, computers, APIs, and business systems;
- **machine-enforceable boundaries so policy cannot be bypassed by ambient OS access;**
- **natural human interaction that does not require a keyboard or mouse;**
- attributable, auditable conversation across humans and multiple agents;
- proof that work produced the requested outcome;
- correction, revocation, recovery, and learning loops;
- strict isolation between clients, projects, and trust classes.

This repository captures those **underlying primitives**. Verticals, models,
providers, products, and tools can change. The substrate remains stable.

It is based on a working Startempire reference architecture and intentionally
separates:

1. **portable core contracts** that any person or business can adopt;
2. **replaceable adapters** for products, providers, speech systems, and vertical systems;
3. **runtime state** that must be discovered live rather than copied from docs.

The desired result is not maximum automation or maximum component count. It is
more capacity for meaningful life and business work: fewer missed commitments,
less routine coordination, useful customer delivery, better decisions and preserved
human attention and wellbeing. A component earns its place by improving that loop.
Protect genuine owner judgment; reduce dependence on the owner for uncaptured,
repeated procedure. Measure the benefit in the engagement, rather than assuming
that more agents, dashboards or infrastructure mean more value.

## Owner-rooted architecture authority

The portable system now makes one distinction explicit that must never be blurred:

```text
Canonical Owner Principal
    = constitutional / architecture authority root

Focusa + Agent-KB + business systems
    = scoped operational/domain truth

Veragensia + UIAI Engine + tools
    = enforced execution and observation

Voice / UI / API surfaces
    = modalities into the same authority

AI Chief of Staff / workers
    = delegated reasoning and action
```

Every deployment establishes a **Canonical Owner Principal** through the portable
[`OWNER_AUTHORITY_CONSTITUTION.md`](./OWNER_AUTHORITY_CONSTITUTION.md). For the
Startempire reference deployment that owner is **Verious Smith III (Sir V3)**. A
client deployment replaces that binding with its own legitimate owner; it does not
inherit Startempire authority.

A GitHub username, organization, issue, PR, commit, customer request, contributor,
email, forwarded analysis, test result, model output, voiceprint, speaker-recognition
result, or deployed implementation is **provenance/evidence, not architecture
authority**. Technical input from any source can be valuable, but it remains
advisory until the deployment owner explicitly promotes it or a valid owner-delegated
authority does so.

AI authority is also identity-bound rather than name-bound. A future authority AI
uses separate cryptographic objects for stable principal identity, authority
constitution, and current runtime attestation as specified in
[`CRYPTOGRAPHIC_AUTHORITY_PROFILE.md`](./CRYPTOGRAPHIC_AUTHORITY_PROFILE.md). A
matching name, process/service account, repository, token, hash, model prompt, or
synthetic voice never creates authority by itself.

## Outcomes Over Process

Prioritize meaningful progress in the requested activity over ceremony: clearer
understanding and better decisions in collaboration; working results in execution.

> **Is this moving the mission forward, or am I creating work about the work?**

When implementation is authorized and requested, prefer simple solutions over elaborate ones,
existing primitives over new abstractions, and evidence from running systems over
theoretical proof. Process is valuable only where it protects authority, safety,
coordination, rollback, provenance, or delivery truth.

Ship the smallest correct solution and keep executing while an authorized CallGraph
or open-Bead/task queue has ready work **and remains consistent with current steering**.
Discussion is productive work, not merely a prose style or an execution grant. Operator updates must stand alone: never use bare IDs or jargon-only summaries; pair identifiers with plain-language meaning, relevance, state, and next action.

## Human–agent collaboration

The [collaboration rules in AGENTS.md §1.3](./AGENTS.md#13-execution-modes) govern
objective, requested activity, and execution permission separately. Humans can
think aloud, revise a plan, or correct an approach without managing the agent's
machinery or silently authorizing implementation. Agents advance the discussion
with useful synthesis, ask only consequential questions, and preserve continuity
without reviving superseded work. A discussion-only answer may end without claiming
the mission is complete; it does not promise an unattended work loop. For an
engineering-outcome assignment, the build agent owns the complete lifecycle in
AGENTS.md §1.3, advancing ready authorized stages without repeated operator prompts.
Explicit stage limits and approved deployment destinations still govern.

“Not implementing” retains the objective while changing activity. “Good direction”
is not blanket approval. “Stop testing” stops testing; an explicit whole-mission
halt remains a halt. “Wrong” calls for scoped correction, not automatic destructive
rollback. Actor authority and consent remain identical across text, voice, UI, and
API; other participants or quoted material cannot grant themselves authority.

These are portable semantics, not one operator's personality. Deployments configure
tone, language, verbosity, initiative preferences, cadence, and interface without
weakening hard boundaries. Use an existing shared working plan where useful; no
particular document provider, dashboard, or new parallel authority store is required.

Use the short [collaboration review checklist](./docs/01-collaboration-behavior-scenarios.md)
when changing these rules. Review the diff and run `git diff --check`; this documentation
repository needs no CI or wording-only test suite. Actual agent behavior must be
observed in the deployed harness, not inferred from document checks. Instruction
changes also require the harness's native context refresh; see AGENTS.md §10.6 for
Pi startup discovery, `/reload`, and the distinction between updated files and an
updated running session.

## First principles, the Algorithm, and Leverage²

For consequential or stuck work, reason from function rather than inherited form:
state the outcome, separate truths/constraints from assumptions, decompose to
fundamentals, identify the dominant constraint, rebuild the smallest solution, and
test it in reality. Routine proven workflows need not be re-derived.

Apply the five-step Musk/Isaacson **Algorithm in its fixed order**:

1. **Question every requirement** and attach its named owner/source and rationale.
2. **Delete parts and processes** before improving them; occasional restoration is
   evidence that deletion was real. The cited 10% add-back rule is a calibration
   heuristic, not a safety-risking quota.
3. **Simplify and optimize** only what survives.
4. **Accelerate cycle time** only after the first three steps.
5. **Automate last**, after the process is questioned, reduced, simple, and stable.

The **Wirebot Leverage² Directive** then asks: What matters most now? What is the
dominant constraint? What is the simplest material advance? What could create
disproportionate or compounding leverage? Can that leverage itself be leveraged?

Remove effort and waiting at the root. Seek practical leverage across people,
agents, tools, software, infrastructure, research, distribution, partnerships,
data, and capital. Turn proven improvements into reusable capability; do not
prematurely systemize an unproven idea. Use the learning loop
**Identify → Act → Measure → Keep, Improve, or Remove**.

Priority: **hard invariants and authority → mission outcome → simplicity → constraint removal → leverage → systemization**.

Sources: [Focusa adoption](https://github.com/Startempire-Wire/focusa/blob/main/docs/current/2026-08-20-elon-5-step-ota-simplification.md),
[James Clear](https://jamesclear.com/first-principles), and
[Corporate Rebels](https://www.corporate-rebels.com/blog/musks-algorithm-to-cut-bureaucracy).
The operating rules—not celebrity authority—are normative.

---

## API-first knowledge migration

`agent-kb-api` is canonical **for knowledge retrieval in its domain**, not for
constitutional architecture. Agents use executable `agent-kb` in this order:
`bootstrap → freshness → search → direct_doc`; responses must be authenticated,
fresh, provenance-bearing, and checked for `fallback_used`/`stale`. Shell helpers
are convenience only. `/root/.agent-kb` Markdown is transitional import/export and
explicit degraded recovery—not a normal read path—and is removable only after
structured storage, parity, consumer tests, rollback, and offline recovery are
proven. Tracker: Wirebot Core issue #13.

---

## The system at a glance

```text
CANONICAL OWNER PRINCIPAL / SOVEREIGN HUMAN OR BUSINESS OWNER
  architecture · values · goals · consent · correction · reserved powers
       ↓
NATURAL HUMAN INTERACTION
  voice · visual UI · text · touch · API · assistive modalities
       ↓
PRIVATE CONTEXT + AI CHIEF OF STAFF
  signals · memory · synthesis · recommendations · exceptions
       ↓
GOVERNANCE / COHESION
  tenant · project · Trajectory · capabilities · Workpoints · budgets
       ↓
MACHINE-ENFORCED EXECUTION
  workload identity · resource identity · containment · control leases
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

The names below map the **reference responsibilities**, not a blanket statement of
installed completeness. A client can replace an adapter while preserving its
contract. Full enforcement, desktop, voice and conversation requirements come from
the named profiles and need their own consumer/runtime proof; listing them here
does not certify that every deployment implements them.

| Layer | Startempire reference | Responsibility |
|---|---|---|
| Canonical Owner Principal / sovereign principal | Verious Smith III (Sir V3); client deployments bind their own owner | Root architecture authority, goals, values, consent, corrections, reserved powers, AI delegation |
| Community and distribution | Startempire Wire + Startempire Wire Network | Relationships, opportunities, member-site/extension integration and distribution; not mandatory network participation for all product buyers |
| AI Chief of Staff | OpenClaw + Wirebot/`wb` | Orient, synthesize, recommend, delegate, observe, escalate; no architecture authority by name |
| Knowledge/context | Context Core + Agent-KB | Private memory, policy, topology, source-aware retrieval; domain knowledge authority only |
| Governance/cohesion | Focusa | Project identity, Trajectory, Workpoints, Context Authority, Evidence, learning, Expression and conversation semantics; operational authority only |
| Voice/conversation provenance | Focusa Expression Engine + Voice/Conversation primitive | Semantic expression, attributable utterances, transcript correction lineage, group conversation, Conversation Ledger; conversation is not memory |
| Governed desktop presenter | Focusa Desktop | Default human work/cognition/conversation presentation in supported full Veragensia profiles; presenter over Focusa authority |
| Reference Focusa harness | Pi + Focusa Pi extension | Default/reference Focusa-aware agent harness; fundamental reference integration, no parallel cognitive authority |
| Agent computer + enforcement | Veragensia | Provisioned/streamable host, workload enforcement, secure attention, resource/runtime identity, audio UI, lifecycle and human control reserve |
| Browser/computer control | UIAI Engine + Cockpit/browser surfaces | Canonical first-party browser/computer observation, interaction, diagnostics, control-lease/takeover, visual evidence |
| Agent workforce | Build agents, specialists, Pi workers, humans | Bounded execution under role contracts |
| Outcome ledger | WINS | Plan → Ship → Prove, corrections, confidence, economics |
| Outbound distribution | Wire Launch | Governed campaign execution and evidence |
| Inbound opportunity | WorkRouter | Provenance, qualification, matching, routing, outcomes |
| Portable trust | MeriFolio | Evidence-backed identity and selective disclosure |
| Health/recovery | Guardian + Focusa receipts + Wirebot audit | Diagnostics, audit, checkpoints, recovery |
| Repeatable adoption and support | Golden Path + diagnostic prototype + proposed Tauri experience | Capture repeated work and expose applicable gaps; not automatic enrollment, a universal local install or completed production intake |

**Agent-operation complete is the default.** Every first-party UI action and readable state must derive from a canonical versioned operation with complete API and CLI routes, shared authority/entitlement semantics, machine-readable results and parity evidence. Computer-use automation (CUA) is the absolute last resort; a first-party workflow that requires visual clicking because its structured operation is missing carries an explicit API/CLI parity defect. The testable baseline is the [Agent-Operation-Complete Software Contract](./docs/agent-os-golden-path/07-agent-operation-complete-software-contract.md); the [ecosystem parity audit](./docs/agent-os-golden-path/08-wirebot-ecosystem-agent-operation-parity-audit.md) records current structured foundations and operation-level gaps without treating route or source presence as completion.

The full Startempire Agent Computer composition is intentionally documented in
[`AGENT_COMPUTER_REFERENCE_PROFILE.md`](./AGENT_COMPUTER_REFERENCE_PROFILE.md). It
references the canonical Veragensia implementation specs rather than forking them
into this portable repository.

### Division of responsibility

- The **Canonical Owner Principal** defines constitutional architecture and the
  root delegation boundary.
- The **Chief of Staff** coordinates; it does not silently become every worker or
  architecture authority. Portfolio awareness does not make it a global project
  foreman: project execution resolves its own scoped workstream and responsible role.
- **Focusa** governs work and conversation semantics; it does not become every
  product, CRM, memory store, or owner of organizational architecture.
- **Conversation history** is attributable provenance/audit; it does not become
  canonical memory, policy, Workpoint, ontology, or knowledge merely because it is
  extensive and durable.
- **Focusa Desktop** presents governed Focusa state/operations/conversation; it does
  not become a second reducer, memory store, or authority.
- The proposed **Wirebot Web/PWA/Desktop/Mobile family** is a newly directed professional customer application shell, not a proven current product. It may integrate Startempire Wire through domain-owned structured operations; it does not turn WordPress pages into runtime authority or copy every backend.
- **Startempire Wire and AI Draftees** retain their observed community/marketplace domain evidence while their future app relationship is re-evaluated; older WordPress UX does not settle the new application architecture.
- **Pi** is the reference/default Focusa harness integration; that reference role
  does not make canonical Focusa state Pi-private or exclude compatible harnesses.
- **Agent-KB** may be canonical for source-aware knowledge retrieval without
  becoming constitutional architecture authority.
- **UIAI Engine** supplies hands and eyes; machine access is not business or
  architecture authority. It is deliberately listed as a canonical first-party
  Agent Computer execution surface rather than treated as an incidental browser.
- **Veragensia** turns semantic grants into machine restrictions; root/UID/container
  access is not a substitute for a scoped capability.
- **Voice/audio** is an interaction modality into the same operations. A voiceprint,
  TTS voice, wake word, or speech provider does not create identity or permission.
- **Agent employees** execute scoped jobs; a role is not permission to access
  everything the Chief of Staff knows. Stateful workers may use an architecture similar to Wirebot Core Memory, but whether stores or records are shared remains an explicit unresolved design choice; isolation is the default until proven otherwise.
- **Golden Path tools** are assigned to workers through a verified capability inventory. Installation or presence does not grant use, credentials, data scope or authority.
- **Business systems** remain authoritative for their own records.
- **Receipts and outcomes** connect the layers without duplicating authority.

---

## How the handoffs connect

The system is cohesive because each owner exposes a bounded result the next owner
can use—not because every system shares a database or becomes a feature of Focusa.
The same principle applies to life, business and market work.

| Handoff | What crosses the boundary | What remains with the owner |
|---|---|---|
| Human → Chief of Staff | Goals, constraints, preferences, corrections and approved context | Reserved decisions and authority; discussion does not automatically authorize execution |
| Sources → knowledge/context → Chief of Staff | Relevant records or summaries with provenance, scope and freshness | Original business records, private memory and access controls; retrieval is not ownership transfer |
| Chief of Staff → governed work | Requested outcome, exact scope, resources, acceptance and existing permission | Architecture authority and policy; a generated task cannot mint a grant |
| Governed work → worker/tool | Bounded action, necessary context, capability, budget and evidence requirements | Credential values and unrelated tenant context; a worker sees only what the job needs |
| Tool → evidence/completion mechanism | Actual result, affected object, errors and durable proof references | Acceptance and settlement follow the owning contract; dispatch is not completion |
| Accepted result → business record / W.I.N.S. where applicable | The outcome and supporting references under the relevant product rules | The diagnostic is not automatically a business-score event; no universal approval policy is inferred |
| Experience → learning → next work | A tested improvement, correction or reusable procedure | Owner approval where required; observations cannot silently rewrite architecture or policy |

### A concrete operating loop

Consider an owner asking for a preparation brief before a customer meeting:

1. The Chief of Staff establishes the desired brief and the permitted customer,
   calendar and document scope. Missing context is distinguished from a negative fact.
2. Existing knowledge/context adapters retrieve only the relevant sources; the CRM
   remains the customer-record owner and the calendar remains the schedule owner.
3. The agent can synthesize the brief in the requested discussion/drafting mode.
   If the request also authorizes a calendar change or outbound message, those are
   separately scoped actions using the existing execution and permission path.
4. A worker uses the appropriate API or approved computer/browser context. It does
   not get the owner's entire inbox or vault merely because a meeting is involved.
5. The consumer-visible brief or authorized change is checked. A returned tool
   success without the expected document/event/message is not enough.
6. The owner can correct the result. Useful, repeatable preparation steps become
   candidates for reuse only after they work; private client contents do not become
   a reusable template or another client's memory.

This is an illustrative flow, not a newly deployed feature. The point is the
connection between existing responsibilities. The same pattern can support a
weekly business review, an approved recurring report or a narrow operational task
without adding a new orchestration or evidence system.

### Keep the identities distinct

A **principal** owns or acts; a **tenant** bounds data and access; a **project**
bounds an objective; a **workstream/Workpoint** identifies execution continuity and
its current action. An **agent role** names a worker's job; a **runtime** executes
agents; a **machine** hosts workloads; an **Agent Computer** supplies computer-use
capabilities. A website is an access surface, not necessarily any of these objects.

Bind the relevant references through the owning contracts instead of collapsing
them into one ID. A customer may have multiple machines or remotely provided
capabilities. A stable machine hash can help correlate observations, but cannot
prove a customer relationship, ownership, authority, uniqueness or enrollment.
Scope and consent survive any approved cross-project or cross-tenant connection.

## Reference modes and surfaces

These are distinctions already present in the ecosystem, not a new mode engine or
a license to combine every option:

| Dimension | Questions it answers | What it does not imply |
|---|---|---|
| Purchase / participation | Wirebot Direct or network bundle; which benefits were bought? | Direct is not DIY, and shared billing infrastructure does not require network participation |
| Runtime isolation | Shared or dedicated execution boundary? | A personal bot identity is not necessarily a dedicated process or computer |
| Hosting / operation | Platform-managed or client-owned infrastructure; who operates it? | Managed Sovereign does not require self-hosting; client-owned infrastructure can still be managed by agreement |
| Federation / sharing | Which independently scoped participants may exchange what? | Pooled private memory, inherited owner authority or an already functioning federation in every installation |
| Interface / access | Web, extension, channels, individual components or a proposed operated wrapper? | The interface does not create entitlement, deployment scope or credential-use permission |

The reference product doors are **Focusa.dev and Wirebot.chat**. The separately
named **os.focusa.dev** hosts the Veragensia Agent Computer by operator direction;
its public-door credential restrictions remain. The Wirebot gateway, W.I.N.S.
application, parent community and network distribution sites have their own roles.
A site name or loaded script does not prove end-to-end functionality. Exact surface
relationships and source limits are in the [topology visual](./docs/agent-os-golden-path/04-agent-os-golden-path-ecosystem-topology-map.html). The current [cross-product UI inventory and options audit](./docs/agent-os-golden-path/06-wirebot-product-ui-options-inventory-and-consolidation-audit.md) distinguishes Focusa Desktop, Focusa Menubar, Focusa browser extension, UIAI Cockpit and Evidence PWA, Wirebot browser extension, Wirebot Desktop/mobile, W.I.N.S. screens and Veragensia while preserving unresolved choices for explicit evaluation.

The operated Golden Path offering belongs under Wirebot without absorbing the
independent component products. **Full AITL Setup is the existing scalable middle
path:** it is delivered remotely through the operated service without requiring the
Canonical Owner Principal on site. Its customer endpoint is the same proposed Tauri
app used throughout the wrapped process—not a separate tier-specific app. The app
carries deterministic setup, local owner moments, evidence and the support
connection; the Agent Operator, Chief of Staff and Agent Computers supply the
operated side. Personal owner presence is the scarce premium layer over that same
system, and scaled Full AITL adoption increases demand for it. The Tauri
implementation remains unfinished; Full AITL Setup itself is not a newly invented
offer. DIY users retain independent component use under component licenses, while
the wrapped app has no standalone mode. The operator's wrapped-process IP,
structural service tether and engagement/support economics remain in the [single
Golden Path doctrine](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md), not a second pricing table here or an assumed price for Wirebot tiers.

For implementation details, see the owning Wirebot [runtime contract](https://github.com/Startempire-Wire/wirebot-core/blob/main/docs/TIER_RUNTIME_CONTRACT.md),
[client-owned deployment blueprint](https://github.com/Startempire-Wire/wirebot-core/blob/main/docs/SOVEREIGN_WHITE_LABEL_DEPLOYMENT.md)
and [productization route](https://github.com/Startempire-Wire/wirebot-core/blob/main/docs/PRODUCTIZATION_ROUTE.md).
Historical hypothetical pricing in source documents does not supersede approved
engagement terms. Public website planning and delivery are separate work.

## The portable substrate

These primitives should survive changes in vendors, models, verticals, and user
interfaces.

| Primitive | Required meaning |
|---|---|
| **Canonical Owner Principal / sovereign principal** | Root architecture authority, values, consent, correction rights, reserved powers, and delegation root |
| **Owner authority identity** | Versioned owner principal manifest, deterministic identity SHA-256, key fingerprint, scope, revocation, and authority-transfer semantics |
| **AI authority identity** | Stable AI principal hash kept separate from constitution/runtime attestation; owner-rooted signed delegation required |
| **Identity and tenancy** | Stable client, principal, project, environment, and lifecycle boundaries |
| **Workload / execution identity** | Which exact executable/runtime is acting, on which node/incarnation, independently of conceptual agent identity |
| **Platform/runtime attestation** | Explicit software/image/policy/boot trust posture; evidence for eligibility, never authority by itself |
| **Source and provenance** | Where information came from, when, its trust class, freshness, and supersession; provenance is not authority |
| **Context and memory** | Private, source-aware retrieval with retention and bounded disclosure |
| **Conversation lineage** | Attributable utterances, speaker/agent refs, ASR hypotheses/corrections, expression/spoken-output links, action/evidence relationships; not automatic memory |
| **Intent and Trajectory** | Desired state, current state, gap, constraints, and next direction |
| **Capability and policy** | Who may do what, to which resource, for how long, under which conditions |
| **Machine enforcement** | Deterministic translation of allowed capability into actual filesystem/network/device/input/credential/resource restrictions |
| **Stable resource + revision** | Durable logical resource identity, expected revision, replica and current locator; path/PID/window name is not durable identity |
| **Human control lease / secure attention** | Protected stop/takeover/approval path with one active actuator holder, fencing, reconciliation and re-observation |
| **Modality parity** | Important supported outcomes remain available through applicable voice/nonvisual/visual/text surfaces using the same canonical operations |
| **Work unit** | Scoped objective, owner, dependencies, budget, and done-condition |
| **Orchestration** | Selection, sequencing, delegation, pause/resume, escalation, and bounded topology/fanout |
| **Execution adapter** | Typed tool, computer, browser, or API action with diagnostics |
| **Workforce role** | Job, supervisor, tools, limits, quality bar, escalation, and revocation |
| **Evidence and receipt** | Actor, authority, target, action, result, time, and supporting references |
| **Outcome and correction** | Accepted real-world effect, confidence, dispute, correction, and economics |
| **Learning and policy change** | Evaluation, reusable skill, approval, versioning, and rollback |
| **Observability and recovery** | Health, audit, retry, rollback, continuity, and incident response |
| **Resource and leverage** | Time, attention, money, tokens, capacity, marginal value, and compounding reuse |

### Common object envelope

Durable objects carry a schema version, stable ID, tenant/project scope, owner and
actor, state, source/freshness/trust, authority, evidence, and correction/revocation
references. Exact schemas vary; those semantics cannot disappear.

Architectural decisions additionally carry owner/delegated-authority provenance so
the system can distinguish **who proposed a decision** from **who had authority to
make it canonical**.

---

## Chief-of-Staff operating contract

A capable AI Chief of Staff performs five loops:

1. **Orient** — assemble an accurate view of goals, commitments, customers, cash,
   risks, blockers, and opportunities.
2. **Recommend** — expose priorities, trade-offs, uncertainty, assumptions, and the
   shortest reliable path.
3. **Govern** — translate approved intent into exact projects, Trajectories,
   Workpoints, tasks, capabilities, budgets, enforcement requirements, and acceptance criteria.
4. **Delegate** — route each work unit to the owning person, business system, or
   agent employee with only the context and authority required.
5. **Observe and learn** — collect receipts, verify outcomes, escalate exceptions,
   capture corrections, and improve future execution.

Broad context does not imply broad execution. The Chief of Staff may understand
the whole portfolio while disclosing only a narrow slice to each worker.

A Chief of Staff also does not gain architecture authority merely from broad
context. If the deployment wants an AI to make canonical architecture decisions,
that AI must satisfy the owner-rooted cryptographic delegation contract.

The Chief of Staff may be spoken to naturally. Voice changes the interface, not its
scope, delegation, or reserved powers.

### Reserved powers

Every deployment names owner/human-only powers: destructive/irreversible changes;
material legal or financial commitments; identity, ownership, or governance;
broad credentials; sensitive publication; safety overrides; and emergency or
nonrenewable authentication resources.

Voice-complete deployments provide a trusted, non-keyboard path for permitted human
approvals but do not use voice recognition alone as universal authorization.

---

## Agents as employees

An agent employee is a **governed role**, not a personality with ambient access.
Start with one narrow job and real work. Expand only after safe escalation,
consumer acceptance, repeatable evidence, useful economics, and enforceable runtime
boundaries.

### Employment packet example

Illustrative field relationships only; use the owning system's versioned role schema
for execution rather than implementing this example as another authority store.

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

### Capability grant

A grant binds a subject and tenant/project scope to named resource actions, limits,
expiry/use bounds, evidence policy, and revocation. It is not a password:
credentials remain in the owning broker/provider boundary while the agent receives
the narrow ability to perform an approved action.

A capability grant is operational authority; it is not automatically architecture
authority and is not fully enforced until the execution environment has compiled
and verified the corresponding machine restrictions.

---

## Work and evidence lifecycle

```text
CAPTURE → ORIENT → DECIDE → PLAN → DELEGATE → ACT → PROVE → LEARN → COMPOUND
```

A consequential action should produce a durable receipt. Dispatch is not
completion, and a passing producer test is not proof that the consuming system or
customer received the outcome.

### Receipt example

Illustrative receipt shape, not a replacement for Focusa or another owning
completion mechanism's actual contract. References connect the records without
copying their private payloads.

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
verified with the appropriate runtime, visual/nonvisual, consumer, and outcome
evidence.

Likewise, implemented/deployed architecture is not evidence that its proposer had
authority to make it canonical.

---

## Replaceable vertical adapters

Vertical adapters connect real systems to the substrate. They may evolve without
changing sovereignty, identity, authority, Workpoint, conversation, receipt, or
correction semantics.

| Vertical | Example systems |
|---|---|
| Personal life | Calendar, email/SMS, documents, learning, health, home, devices |
| Customer operations | CRM, support, onboarding, proposals, contracts, scheduling |
| Revenue | Commerce, billing, accounting, subscriptions, payouts, tax |
| Product and delivery | Project management, repositories, CI/CD, websites, hosting |
| Workforce | Hiring, role packets, scheduling, reviews, payroll, contractors |
| Market | Research, campaigns, social, opportunities, partnerships, community |
| Infrastructure | Cloud, cPanel, containers, databases, networking, observability |
| Speech/audio | ASR, TTS, speech-to-speech, microphone arrays, remote/mobile audio endpoints |

Every adapter declares its owner/source, schema/version, tenant/project and trust
scope, capabilities/consent, renewable authentication, typed inputs/outputs,
idempotency, budgets, evidence/redaction, and failure/retry/rollback/revoke/teardown
behavior. An adapter may consume substrate authority; it must never silently
redefine it.

Speech providers are render/capture adapters. They do not become canonical speaker,
conversation, memory, authority, or settlement stores.

---

## Security and tenancy

### Nonnegotiable boundaries

- Never automate with a nonrenewable resource.
- Never retrieve, inspect, request, expose, test, or use recovery codes.
- Transport, root, browser, CDP, machine, UID, container, device, or API access is not authorization.
- A semantic grant must be backed by machine enforcement for a fully governed execution claim.
- Repository ownership/admin permission alone is not a self-authenticating human
  architecture identity; architecture uses the owner constitution.
- Voice recognition, voiceprint, speaker label or synthetic voice is not authorization.
- Use renewable, revocable, least-privilege credentials and capabilities.
- Keep client credentials, memory, files, sessions, conversations, evidence, and audit records isolated.
- Never use one tenant's ambient context, conversation, microphone/audio stream, or authority for another.
- Unknown renewability, ownership, consent, speaker attribution, or architecture-authority provenance fails closed where consequential.
- Public demo environments remain credential-free.
- Corrections and revocations are first-class durable events.
- Human stop/takeover/secure-attention resources remain protected from agent workload exhaustion.

### Trust classes

A practical deployment distinguishes at least:

1. **Public** — safe for unrestricted disclosure.
2. **Customer-authorized** — scoped to a tenant and approved purpose.
3. **Private operator** — personal/portfolio context unavailable to customers.
4. **Credential-bearing** — isolated broker/provider boundary; never ordinary context.
5. **Emergency/break-glass** — operator-only, non-automatable resources.

Platform/workload trust is separately declared; a public/private data class is not a
boot/runtime attestation class.

Shared infrastructure is acceptable only when these boundaries are enforced and
proven end to end.

---

## Truth, uncertainty, and correction

Decision quality requires epistemic integrity:

- distinguish observed facts, source statements, inferences, assumptions, and
  unverified claims;
- distinguish source/proposal provenance from authority provenance;
- distinguish speech hypothesis from accepted transcript and interpreted intent;
- expose material uncertainty and knowledge gaps where they affect action;
- expose uncertain speaker attribution where it affects authority or meaning;
- cross-check high-impact claims against authoritative sources or running behavior;
- correct errors immediately and preserve the correction trail;
- preserve transcript/speaker correction lineage rather than rewriting prior observations;
- never present partial knowledge as complete or speculation as fact.

Do not turn truthfulness into response theater. Routine internal checks need not be
narrated. Surface the uncertainty that changes a decision, then return to work.

---

## Evidence and implementation state

Read architectural requirements, source implementations and deployment evidence as
separate layers. An owner-approved direction can be settled while implementation
is unfinished; an implementation can be present without being loaded, configured
or proven for the requested consumer.

| Evidence class | What it supports | What remains to prove |
|---|---|---|
| Owner-approved contract / reference profile | Intended responsibilities, boundaries and acceptance requirements | Implemented behavior and actual deployment conformance |
| Source / configuration exists | A mechanism or configured route can be inspected | Native loading, correct scope, effective configuration and authorized use |
| Bounded test passes | That test's inputs and asserted behavior | Other platforms, failure paths, consumer integration and field applicability |
| Runtime / consumer proof | The tested outcome in the named scope and environment | Untested tenants, platforms or conditions; later changes may invalidate evidence |
| Accepted outcome and reuse evidence | Useful effect and a basis for repeating the procedure | New scope or broader rollout still needs its own permission and checks |

**Repository snapshot, 2026-09-12:** the portable contracts and Golden Path planning
exist; the Golden Path targets **0.2.0-candidate**, not a released complete installer.
Its two scripts are partial prototypes. The checker covers ten CLI presence/version
checks and three health paths, not the whole ecosystem. Linux reference/local HTTP
sink behavior was tested; production diagnostic intake, client rollout and
macOS/Windows acceptance are not established by those tests. See the
[working ledger](./docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md#task-ledger-execution-tracking)
and [changelog](./docs/agent-os-golden-path/CHANGELOG.md) for authoritative task status
and bounded evidence. This README does not re-declare their tasks complete.

### Diagnostic observations, readiness and acceptance

Start with the desired outcome and actual engagement. A relevant capability can be
local, remotely provided, not required, blocked or unknown; those applicability
states describe the needed workflow, not capabilities the current scripts already
implement. A managed-service customer does not need every server CLI installed on
their laptop. A local process check cannot verify a remote consumer path.

The intended flow is **outcome → applicable checks → observations → relevant gaps →
existing governed work → recheck → usable result**. It feeds the owning setup and
support mechanisms; it is not a fleet registry, identity system or enrollment act.
Receiver ownership, permitted data, client binding, retention, isolation and durable
readback must be established before production reports are sent there.

Readiness should first expose required capabilities working, blocked and untested.
An optional later percentage needs a meaningful denominator and must not hide a
critical blocker. W.I.N.S. business outcomes are a different concern; missing a
local tool is not automatically a negative business score. The existing
[candidate list](./docs/agent-os-golden-path/03-agent-os-golden-path-future-addition-candidates.md)
holds future scoring, extension and site work rather than silently activating it.

## Minimum viable client deployment

Do not begin with dozens of agents and every connector. Begin with one useful,
auditable loop. These are functional obligations for an adopted governed system,
not a command to reinstall a complete reference stack on every customer device.
Brownfield adoption preserves existing working systems and discovers which
capabilities already satisfy the engagement, locally or remotely.

1. **Owner constitution:** establish the Canonical Owner Principal, create the
   stable owner principal manifest/key, bind owner GitHub/account/tenant scope,
   reserved powers, authority transfer, constitution hash, and AI delegation policy.
2. **Context:** connect only mission-required sources with provenance, freshness,
   ownership, disclosure, briefing, and correction rules.
3. **Governance:** create the exact Focusa project, canonical Trajectory, current
   Workpoint, capabilities, budget, done-condition, Evidence, and escalation.
4. **Hands:** provide a private Agent Computer/browser or typed API; prove workload
   identity, machine enforcement, diagnostics, rollback, revocation, teardown, and
   brokered credentials.
5. **Interaction:** if the deployment claims voice completeness, prove a useful
   workflow without keyboard/pointer, with attributable conversation/transcript
   lineage and trusted stop/approval.
6. **First employee:** hire one narrow role with minimum context/capability/budget;
   test success, ambiguity, denial, retry, escalation, correction, and enforcement.
7. **Outcome loop:** complete real work; prove producer, consumer, runtime,
   visual/nonvisual, and business outcomes as applicable; measure value and risk.
8. **Compound:** version repeated success, retire stale access/process, and add
   roles/connectors/tenants only after isolation and economics hold.

A minimum viable system therefore has:

```text
1 canonical owner + 1 stable owner principal identity
+ 1 authority constitution + 1 client/tenant + 1 project
+ 1 Trajectory + 1 Workpoint + 1 agent role
+ 1 real connector + 1 enforceable execution boundary
+ 1 verified outcome loop
```

Voice completeness is an additional profile claim, not required for every minimal
headless/special-purpose deployment.

---

## Operating rhythm

| Cadence | Loop |
|---|---|
| **Daily** | Refresh context/health → brief commitments, customers, cash, risks, opportunities → select Workpoint → delegate bounded work → observe exceptions → verify outcome/corrections |
| **Weekly** | Review outcomes over activity → compare expected/actual value and cost → revoke stale grants/process → promote proven skills → reallocate → expand only where evidence supports it |
| **Incident** | Stop affected mutation → preserve state/evidence/conversation refs → recover with exact identity/scope → fix canonical root cause → verify consumer/rollback behavior → add durable prevention |

These loops may be conducted conversationally. Spoken control does not weaken their
identity, authority, evidence, or settlement requirements.

---

## Porting this architecture

Treat a deployment as configuration of the substrate, not a fork of one person's
private operating state.

### Replace these bindings

| Reference binding | Client-specific replacement |
|---|---|
| Verious Smith III / Sir V3 owner binding | Client Canonical Owner Principal + new stable owner principal manifest/key |
| Startempire owner/constitution/delegation refs | Client-owned principal digest, key fingerprint, constitution hash, GitHub/account/tenant scope, revocation and transfer policy |
| Startempire tenant/project IDs | Customer-owned stable identifiers |
| Agent-KB/Context Core | Approved private knowledge and policy authority |
| OpenClaw/Wirebot | Approved Chief-of-Staff runtime/interface; no AI architecture authority without owner delegation |
| Focusa | Focusa deployment and exact project/conversation governance |
| Focusa Desktop / Pi / Veragensia / UIAI | Approved governed presenter, compatible/reference harness, enforceable Agent Computer and browser/computer execution environment |
| Voice/Conversation adapter set | Customer-approved ASR/TTS/audio endpoints preserving portable utterance/participant/transcript semantics |
| Provider adapters | Customer-owned calendar, CRM, finance, code, and operations systems |
| Credential broker | Customer-approved renewable authentication authority |
| WINS/outcome ledger | Customer outcome, correction, and evidence store |

### Never copy

- the reference owner's authority principal, private key, delegated AI authority, or
  GitHub/tenant authority scope;
- credentials, tokens, cookies, recovery artifacts, device state, voiceprints, or biometric speaker material;
- private operator/client memory or private conversation/audio history;
- tenant IDs, project attachments, or old Workpoints;
- machine paths, ports, hostnames, runtime IDs, or health claims as standing truth;
- permissions merely because the reference deployment possessed them;
- issue/PR/contributor/customer authorship as architecture authority;
- incident snapshots as permanent architecture.

### Portable export checklist

- [ ] Core contract version selected.
- [ ] Canonical Owner Principal and stable owner principal manifest created.
- [ ] Owner principal SHA-256 and public-key fingerprint established.
- [ ] Authority constitution hash established.
- [ ] GitHub/account/tenant scope bound explicitly.
- [ ] Any AI architecture delegate has a stable principal identity plus a valid owner-rooted signed delegation.
- [ ] Runtime-attestation policy defined for authority-capable AI.
- [ ] Node/workload/execution identity and enforcement policy defined.
- [ ] Principal, tenant, project, and ownership identities replaced.
- [ ] Local products/paths/endpoints moved into deployment configuration.
- [ ] Trust classes, reserved powers, retention, and revocation defined.
- [ ] Credentials and private conversation/audio excluded and secret/privacy scan passed.
- [ ] Focusa project, Trajectory, Workpoint, and task agree.
- [ ] Conversation/transcript retention and speaker-attribution policy defined if voice is enabled.
- [ ] Agent roles and capabilities are client-scoped and machine-enforced.
- [ ] Producer and consumer tests pass.
- [ ] Recovery and teardown are proven.
- [ ] Voice-complete claims pass a no-keyboard/no-pointer workflow when applicable.
- [ ] First real outcome is independently accepted.

---

## Repository structure

```text
.
├── README.md                            # Explanatory architecture and adoption guide
├── AGENTS.md                            # Normative operating contract for agents and harnesses
├── OWNER_AUTHORITY_CONSTITUTION.md      # Portable owner identity + architecture authority root
├── CRYPTOGRAPHIC_AUTHORITY_PROFILE.md   # Principal/constitution/runtime hashing + delegation profile
├── AGENT_COMPUTER_REFERENCE_PROFILE.md  # Reference composition and required proof boundaries
├── AGENT_OS_GOLDEN_PATH.md              # Adoption/operations entry and version target
├── scripts/
│   ├── substrate-bootstrap.sh          # Partial CLI checker; install routes printed, not executed
│   └── brownfield-audit.sh              # Report prototype; not production intake or enrollment
└── docs/
    ├── 01-collaboration-behavior-scenarios.md # Short human review checklist
    └── agent-os-golden-path/
        ├── 0.1.0.md / 0.1.1.md        # Versioned planning lineage
        ├── 02-agent-os-golden-path-ordered-tasks.md # Single working doctrine and ledger
        ├── 03-agent-os-golden-path-future-addition-candidates.md # Parked/withdrawn candidates
        ├── 04-agent-os-golden-path-ecosystem-topology-map.html # Offline relationship visual
        ├── SERVER_AGENT_HANDOFF.md     # Scoped continuation and mechanism references
        └── CHANGELOG.md               # Work/evidence limits; not deployment proof
```

`README.md` explains the system. `AGENTS.md` governs agent behavior.
`OWNER_AUTHORITY_CONSTITUTION.md` governs who may create canonical architecture.
`CRYPTOGRAPHIC_AUTHORITY_PROFILE.md` governs how owner/AI identities, constitutions,
runtimes, and delegations are cryptographically distinguished.
`AGENT_COMPUTER_REFERENCE_PROFILE.md` binds the portable substrate to the Startempire
Veragensia reference composition while leaving detailed Agent Computer architecture
canonical in the Veragensia repository. Volatile runtime state, credentials,
customer data, private conversations/audio, and private operational runbooks do not
belong in this portable repository.

## Using and versioning `AGENTS.md`

Read the owner constitution, cryptographic profile, Agent Computer reference, and
AGENTS contract before deployment; preserve the portable core; create a new owner
binding for the destination; replace client bindings; install AGENTS through the
harness's canonical instruction mechanism; mechanically validate hard stops;
exercise green, degraded, wrong-project, correction, auth, delivery,
owner-mismatch, external-proposal, delegated-AI, runtime-attestation, enforcement,
voice/speaker-ambiguity where applicable, and recovery scenarios; then
review/version before distribution.

Semantic Versioning applies: **major** changes incompatible substrate/safety/
authority semantics; **minor** adds compatible primitives/adapters/workflows;
**patch** clarifies or repairs. Version `3.2.0` adds portable collaboration semantics
and scoped correction without changing owner or cryptographic authority. Version `3.0.0` introduced the explicit owner-rooted
architecture-authority constitution and cryptographically delegated AI-authority
boundary. Validated snapshots use `agents-contract-v<version>`; the version string
alone does not assert that a matching Git tag has been published.

---

## Anti-patterns

Avoid omnipotent agents, ambient cross-client context, ambient same-UID/root access
presented as governance, dashboards replacing authority or proof, adapters creating
parallel truth, issue/PR/customer provenance being mistaken for architecture
authority, AI identity by name alone, voice identity by sound alone, transcript
history being mistaken for memory/authority, mutable runtime state being confused
with stable AI/resource identity, unbounded recursive fleet spawning, and scaling
before isolation, acceptance, human-control survivability, and economics hold.

## Questions answered by the contract

This is a portable contract, not a framework: the deployment owner roots
architecture authority; Focusa governs scoped identity/work/conversation semantics;
Agent-KB governs its knowledge domain; Focusa Desktop presents governed work; Pi is
the reference Focusa harness; UIAI supplies observable hands; Veragensia hosts and
enforces the Agent Computer and supplies trusted voice/audio integration; and
employees remain narrow. Multi-client use requires proven isolation; voice and
other modalities route into the same authority; autonomy and delegated architecture
authority expand only through explicit owner-controlled contracts.

---

## Final principle

A trustworthy ecosystem connects **owner-rooted sovereign intent**—spoken or
otherwise—to **bounded authority**, **machine-enforced capability**, **scoped work**,
**observable execution**, **durable attributable conversation**, **durable proof**,
**human correction**, and **compounding learning**. Architecture authority remains
rooted in the deployment's Canonical Owner Principal; runtime systems and agents
earn only the authority explicitly delegated to them. Stable principal identity,
resource/runtime identity, authority constitution, and runtime attestation remain
distinct. The human should be able to speak naturally instead of operating the
computer mechanically, while the system still proves exactly who acted, under what
authority, on what resource, and what happened. Build the smallest useful loop,
prove it in reality, and scale what works.
