# Golden Path — the interwoven doctrine (single iterable source)

- Date: 2026-09-10 (iteration 16 — the wrapped process is operator IP, non-functional without the payment and support contract)
- **The artifact:** one process an agent executes to build out the Human Life & Business Agent OS on a current brownfield client workstation, end to end, with the agent performing routine setup rather than directing the owner to operate the computer. Everything below is one woven design: the spine stages carry the law, the scars, the checks, the consent design, and the tracking loop — not parallel sections.
- **Locked invariants** (every revision derives from these):
  1. **Agent-operated setup.** The agent inspects, executes, verifies and recovers through existing tools. The owner supplies goals, business knowledge, consequential choices and required approvals—not routine command execution. Ask only when those inputs are genuinely needed; reuse answers and batch questions where practical.
  2. **ACITL with its execution model.** The Agent Computer (Veragensia, remote access) is the loop's hands; the owner is the grantor. The hands themselves are concrete: **OpenClaw (Chief of Staff) orchestrates the build-out, using Focusa for governed work and UIAI Engine plus local build agents as hands to navigate the web, log in to websites, and fully build out the system.** UIAI is added early so build agents approach *everything in the browser a human can do*, verified capability by capability; agents also perform computer use from Pi. Secret entry is AC-driven, owner-typed: the AC opens the form, the owner types once; entry stays secret-safe only where the environment is verified to isolate it from DOM inspection, recordings and screenshots.
  3. **Brownfield-first.** Start on the client's existing computer; audit what exists; build out. Never assume a clean machine; distinguish pre-existing from newly created resources.
  4. **Starter essence.** Defaults are pre-made decisions; scars are paid-for failures attached to the step that pays them; every step has one embedded check; order is dependency-true. Phase numbering is coverage, never schedule.
  5. **Reuse-first.** Existing mechanisms own every step (Pi, Focusa lifecycle, UIAI, rbw, gog, GitHub/Tailscale auth, OpenClaw, provisioning). This doctrine names owners; it never replaces them.
- **Published lineage:** [0.1.0](0.1.0.md) phases remain the coverage scaffold (mapping table below); [0.1.1](0.1.1.md) clarifications stand. This doc is the single working source targeting **0.2.0**.
- **Acceptance truth:** iteration/documentation only so far. No installer, customer rollout, or end-to-end acceptance is claimed. The end state of all this planning is a **fully documented and working process and system** — executed, verified, and continuously optimizable and tracked.

## How this doc is organized (and why)

Everything is staged on the **spine** — the operator's proven deployment sequence. Each stage weaves together, in one place: what happens (steps + step class), which existing mechanism owns it, what law applies (phase invariants), what scars it pays (with defaults/checks), what owner moments it contains (consent design), and what proves it (stage check). The 14-phase scaffold is a coverage index at the end — proving nothing was dropped — not a second structure. Tasks, optimization, and tracking close the loop.

```text
Stage 0  Engage — engagement, authority, consent design
Stage 1  Workstation substrate — Pi, model provider, Focusa, UIAI Engine early (browser + computer use), secrets
Stage 2  Chief of Staff genesis — local desktop folder, git-backed from day one
Stage 3  Cloud landing — OVH VPS account, verification, login (substrate ready, no CoS yet)
Stage 4  Mesh + identity — GitHub, Tailscale on all machines, agents surf between
Stage 5  Knowledge + audit — document all, gog across G Suite, business categorization
Stage 6  Chief of Staff ascends — relocate the git-backed folder to the VPS; cloud-primary administration
Stage 7  Operating plane — voice profile, systems of common tasks, crons, virtual employees
Stage 8  Ongoing operation and handoff
→ Coverage map (14 phases) → Task ledger → Optimization & tracking loop
```

Per-stage anatomy (identical shape every stage):

```text
STEPS → OWNER MECHANISM → LAW → SCARS → CONSENT → CHECK → EXIT
```

**Dependencies and parallel work.** Start each action when its actual prerequisites are ready: GitHub access before remote backup, authorized mailbox access before email verification, and a working cloud runtime before cutover. Move prerequisite setup earlier when needed; stage numbers are not a rigid schedule. Independent per-machine preparation and interviews/documentation can overlap provider waits. Serialize conflicting account, DNS and state changes. On interruption, verify existing results and resume missing work through existing tracking/execution tools—no additional runner, mandatory S/P tagging or assumed universal check command.

**Mechanism split (deterministic vs probabilistic).** Every step is classified before it runs. **Deterministic** steps get owning code — official installers, provider APIs, forms, scripts — executed idempotently with the agent as *supervisor*: run, read exit codes and checks, intervene only on failure. **Probabilistic** steps keep the agent's judgment in the loop — browser flows with no API, CAPTCHA/bot-checks, the CRIST interview, audit significance calls, role design, exception recovery — with owner moments batched around them. Deterministic parts are written once and reused across clients; the agent's scarce attention is reserved for the parts that actually need it. GP-06's binding pass makes this split explicit per step.

**Proposed vehicle for the deterministic library (planning idea, not built).** A single cross-platform desktop app (Tauri — Windows/macOS) downloaded once per client, connecting to the cloud Agent Operator over a scoped, revocable per-client identity. It would package the deterministic steps as one signed, AV-friendly installer instead of script chains; render the owner moments as real forms (secret entry and approvals typed locally, values going directly to the vault or provider — the agent-driven-browser problem disappears); expose a typed command surface the Agent Computer invokes for deterministic work; report receipts and heartbeats to the operator's existing surfaces; carry a **bounded data bridge** — consent-scoped files and documents uploaded to the client's isolated agent endpoints for the audit and build-out (per-client isolation, secrets never transit, a receipt on every transfer); and open the **support channel** — the customer opens the app and consents to a time-boxed, visible agent session with read-only/controller roles and revocation, the customer-side entry point for Agent-Computer remote support. The same download renders **branded walkthroughs**: the batched consent sitting becomes a guided, on-brand in-app experience instead of scattered asks, and Stage 0's consent design gets its concrete vehicle.

**Posture and embedding.** The app sits quietly until needed — a governed background presence, not an invisible daemon: any local agent activity is owner-visible, pausable and revocable from the app itself. Its steady state is a **customer-facing dashboard** over the Chief of Staff: workflows, schedules, receipts, spend, support — the customer watches the OS work instead of trusting a black box. Pi SDK, Focusa and UIAI Engine ship **embedded in the one download**, each component updating through the governed channel with its own versioned release — one download, many components, no loose-install scar. This surface is deliberately distinct from the planned operator/DIY products (Focusa Desktop, UIAI Engine Cockpit, the Focusa.work spec): those serve an operator assembling their own deployment; this app serves the customer whose system the Agent Operator builds and runs. Two audiences, one substrate — shared governance contracts, no duplicate authority, no second OS.

**Sovereignty and licensing boundary.** Focusa and UIAI Engine are self-hosted sovereign software — on-prem, long-running, client-owned infrastructure. The bundled app must never blur that: it is a **wrapped process**, not a separate licensed product. Licenses attach to the components themselves (Focusa, UIAI Engine, Pi SDK) and apply identically whether bundled, individually downloaded, or self-hosted; a client who wants to DIY a different process **without any ongoing support contract** can — their infra, their process, their ownership stays intact. The boundary sharpens in both directions: the wrapped app is **inert without the operated service behind it** — no support contract means no Agent Operator, no CoS, no owner moments, so the app must never ship a standalone mode that pretends to operate on its own; DIY means the individual sovereign components (which do run standalone), not a license-only app. Two honest paths, never a hybrid that muddles both. Ownership is therefore precise: the client owns their infrastructure, their data, and the sovereign components under their own licenses; **the wrapped process — the client app, the deterministic library inside it, the operated design — is the operator's intellectual property**, delivered as a functioning surface only under the active payment and support contract. Non-functionality is enforced structurally (the app exists to connect to the operated service), not just contractually — no cracked or offline approximation is shipped, and component licenses in the about-surface make plain what the client does and does not hold. The app's about-surface therefore names component licenses plainly rather than wrapping them in a bundle license. The commercial emphasis follows from that honesty: the download is a fraction of the value — the operator's positioning is that the **operated process** (Agent Operator, CoS, managed workflows, ongoing support) is orders of magnitude beyond what a DIY download alone delivers. Conditions before it becomes the default: prove the plain-script path first (GP-06); code-signing/notarization cost accepted in the spend envelope; per-client scoped revocable tokens, least-privilege command surface, governed update channel; and it never becomes a second OS — it orchestrates existing owners (Bitwarden importers, official installers, Cloudflare API, Tailscale), never replaces them. *Scar guard: an unmanaged local endpoint with ambient access is the failure mode — the app is a governed endpoint, not an open remote agent.*

---

# Stage 0 — Engage: engagement, authority, consent design

**Steps.** Open the engagement; establish the Canonical Owner Principal for this deployment (owner constitution, portable owner binding); agree the outcome, scope, data boundaries and the **spend envelope** — plans, subscriptions, hosting — with visibility and reconciliation owned by the Canonical Owner Principal and the business's primary owner/operator; enumerate the **consent surface** for this client; record what exists (machines, accounts, software) before touching anything.

**Owner mechanism.** Owner constitution + `OWNER_AUTHORITY_CONSTITUTION.md` pattern; Focusa project identity for the engagement; existing audit/engagement docs.

**Law.** Phase 0 (identity/owner/profile) and Phase 4 invariants govern from the first action: authentication is not authority; tenant identity is never inferred from hostname, user, or directory; private operations fail closed on unknown scope.

**Scars.** Client machines carry prior admin accounts, stale AV, and unknown software; assuming a clean machine produces duplicate installs and broken personalization. Default: audit before install, always; record pre-existing state and reuse it.

**Consent.** This stage *designs* the consent surface for the whole deployment: one batched owner moment per provider (Stage 1 providers including OpenAI device access/Pro billing, OpenCode Go/OpenRouter; gh/cf-wrangler device approvals; OVH; GitHub/Tailscale; Google/gog; the client's website/DNS access; voice samples; employee role batch; any AV/security exclusions). Batch known approvals to reduce interruptions; later discoveries may require a new consequential choice or approval. Do not require owner involvement for routine agent-executable work.

**Check.** The engagement record answers: owner (verified, not assumed), machines in scope, accounts in scope, consents required (enumerated, with providers), and what must not be touched. A second agent reading it reaches the same conclusions. The record also names the **first useful CoS outcome** — the concrete, owner-visible result the build-out must produce first (for example: one owner-approved correspondence drafted and sent, a recurring report produced, or the week's schedule published) — and tallies designed owner moments per stage so the batch stays measurable.

**Exit.** Engagement record + consent surface exist and define the deployment's owner moments; later asks stay consequential-only.

# Stage 1 — Workstation substrate

**Steps.** Install Pi; connect the **model strategy**: OpenAI Pro plan for premium work, with OpenCode Go and OpenRouter provisioned for cheaper-model lanes (OpenAI device access and developer mode enabled early); install **gh CLI and cf CLI/wrangler early** — via device-approval flows where the customer machine lacks them — giving build agents (local and server) CLI access and **full DNS control** — **Cloudflare is the DNS of choice** (its agent tooling is the reason; non-negotiable), and when a client's DNS lives elsewhere (e.g., a prior client on Porkbun) the zone transfers to Cloudflare as part of the build; download Focusa; **download UIAI Engine early**; set up Bitwarden (shared vault); set up rbw for agent-side secret retrieval; **discover and consolidate the client's scattered secrets** into the vault (browser-saved passwords, old managers, sticky notes, whatever exists).

**Why UIAI early (woven rationale).** UIAI Engine is added at substrate time, not later, because it is what gives the local build agents browser tools to do **everything in the browser a human can do** — and the agents also perform **computer use from Pi**. Together with Focusa governance, this is what makes ACITL real on the client machine: from Stage 1 onward, the agents — not the owner — are capable hands on the workstation.

**Owner mechanism.** Pi installer; provider signup (OpenAI/OpenCode Go/OpenRouter); gh CLI and cf CLI/wrangler device-approval installs; Focusa install lifecycle; UIAI install; Bitwarden app + rbw CLI. Each installs through its own official route — this doctrine sequences and checks them, never forks them.

**Law.** Phase 1 (scaffold: inspect first, idempotent, discoverable locations), Phase 3 (freshness: `agent-kb bootstrap` establishes knowledge freshness from the start), Phase 5 (execution surfaces: browser and computer actuation under the same authority/evidence rules), Phase 7 (discovery: agent orients from documented entry points), Phase 10 (secrets: Bitwarden holds secrets; rbw retrieves exact approved fields; nothing secret in config).

**Scars (Windows brownfield).**
- *AV/script blocking kills installers, npm lifecycle scripts, downloaded scripts* → signed official installers only; no silent exclusions. Check: installer completes; signed binary runs.
- *No proper terminal* → Windows Terminal + PowerShell 7; WSL-vs-native decided once per engagement. Check: agent harness runs in the installed terminal.
- *No node/npm* → official Node installer; PATH set. Check: `node -v && npm -v` succeed in the agent's shell.
- *UAC prompts scattered* → batch elevation into one moment. Check: elevation prompts per build-out = 1.
- *PowerShell execution policy / Defender ASR blocks agent scripts* → per-script unblock; blanket policy change is a consent item, never silent. Check: authorized scripts execute; unrelated scripts stay blocked.
- *Secrets scattered in multiple places* — browser saves, old password managers, sticky notes and other odd storage → default: Bitwarden importers for browser/manager sources; non-digital sources are owner-typed in one batched session; consolidate and dedupe; **rbw becomes the single retrieval surface** afterward. Check: `rbw` retrieves a secret that previously lived only in the browser or on paper; browser stores are no longer the sole source.
- *Customer machine lacks gh/cf/wrangler, and auth prompts hang mid-flow* → default: install both CLIs early via **device-approval flows**, batched into the consent sitting; never interactive-password flows. Check: `gh auth status` and `wrangler whoami` succeed from the local agent shell.

**Consent.** OpenAI device access + developer mode + Pro billing = owner moments; OpenCode Go/OpenRouter accounts = owner moments; gh/wrangler device approvals = batched device-flow moments. Provider account/billing (OpenAI/OpenRouter) = one owner-typed moment through an AC-opened browser. Bitwarden master password = AC-driven, owner-typed, never seen by the agent. Non-digital secrets (sticky notes, physical) = owner-typed batch at consolidation. AV exclusions, if any = owner consent item with named scope.

**Check.** From a cold shell, the agent runs: Pi answers a model round-trip; `focusa` status is healthy; UIAI health responds; **a build agent performs one real browser action and one computer-use action a human would otherwise do**; `gh auth status` and `wrangler whoami` succeed from the local shell; `rbw` retrieves an exact approved field **including one consolidated from the client's scattered sources** (value never printed); `agent-kb bootstrap` returns fresh knowledge state.

**Exit.** Workstation substrate is agent-operable and **secret-consolidated**: the AC on this machine can run the harness, drive the browser and computer, retrieve renewable secrets through the approved retrieval surface, and reach the knowledge plane — with the owner's typed moments already spent.

# Stage 2 — Chief of Staff genesis (local, git-backed)

**Steps.** Create the Chief of Staff as a **desktop folder**; `git init` and back it up to GitHub from day one; initialize the CoS workspace (OpenClaw runs where the deployment's chosen path puts it — locally now, cloud-primary later); **run the CRIST project-genesis interview (Focusa Spec 135B)** so the CoS exists as an approved agent role — context ingested from source-linked material, role composed, spec and tasks derived — with the interview corpus persisted for continuous growth. The folder carries the CoS's directives, soul and configuration; runtime memory and task state remain with their owning services until the deployment design moves them. The workspace starts minimal: the engagement/consent record (Stage 0), the CRIST interview corpus, directives/soul drafts and the first-outcome definition — everything else earns its place. The first capability is proven here: the CoS completes one bounded, owner-visible task through the build agents using this context. The folder also carries the **Svelte CoS web UI** — the interface through which the CoS will live at a subdomain of the client's website (deployed at ascension, Stage 6). The UI is a *surface* of the CoS; state remains in the git-backed folder.

**Why git-backed first (woven rationale).** The folder is **portable by design**: it relocates to the VPS in Stage 6. Version control from day one means the CoS's identity and state survive machine loss, are reviewable, and move without loss. The genesis folder *is* the Chief of Staff until ascension.

**Owner mechanism.** Plain git + the owner's GitHub account (renewable routes only); OpenClaw runs per the deployment's chosen path — local genesis now, cloud-primary after Stage 6.

**Law.** Phase 2 (state ownership: this folder is the CoS's canonical home until ascension — after which git history remains its provenance), Phase 12 (version control is part of the delivery path from the start, not an afterthought), Phase 10 (no secrets inside the folder — references only).

**Scars.** Local-only CoS state lost on machine failure or a rushed relocation done by copy-paste → default: git remote backup from day one; relocation later moves source through git and private state through its owning mechanisms. Check: the repo pushes and a fresh clone on a second machine boots the same CoS state — the clone test *is* the portability check.

**Consent.** GitHub repository creation under the owner's account = one owner moment (Stage 0 surface).

**Check.** The CoS answers an orchestration round-trip locally (via Focusa governance + build agents); **its CRIST role packet is approved — context, role, spec, tasks — with the interview corpus persisted**; the folder is committed and pushed; the remote is in sync.

**Exit.** The Chief of Staff runs locally, its state is version-controlled and portable, and its remote is current.

# Stage 3 — Cloud landing (control-plane substrate)

**Steps.** Create the OVH VPS account; respond to verification emails; log in via browser to the VPS. The VPS is **landed here, not yet hosting the CoS** — it becomes the relocation target (Stage 6). Size, OS and hardening are per-client decisions recorded in the engagement record, not defaults invented here.

**Owner mechanism.** OVH provisioning; email verification via the client's consented mailbox (gog, Stage 5 — dependency: consent ordered before it is needed).

**Law.** Phase 2 (state ownership: the VPS is execution/coordination substrate, not canonical truth), Phase 6 (routes: private control plane stays private), Phase 10 (renewable-only authentication for automated access; verification emails are owner-consented automation, not recovery codes).

**Scars.** Verification emails missed/expired mid-flow → default: the AC monitors the consented mailbox and completes verifications within their window. Check: VPS reachable, verified, logged in without further owner action. Fresh VPS lacks the agent toolchain → default: provision through the deployment's documented provisioning path, not ad-hoc package archaeology. Check: the deployment's CLI is healthy on the VPS.

**Consent.** VPS account creation/billing + mailbox consent = owner moments (designed in Stage 0). Everything after them is AC-executed.

**Check.** From the workstation, the AC: SSHes to the VPS on granted credentials and confirms the substrate is ready to receive the CoS.

**Exit.** The control-plane substrate is landed, verified, and waiting; no owner involvement beyond the designed moments.

# Stage 4 — Mesh + identity

**Steps.** Create GitHub (if none — the CoS backup repo from Stage 2 may already have forced this); use GitHub to authenticate Tailscale; install Tailscale on all machines; connected machines allow agents to surf between. **Placement rule:** the CoS and its schedules run cloud-primary (after Stage 6); machine-local build agents serve the machines they sit on; when the primary workstation is off, cloud work continues and machine-local work waits or routes to another enrolled machine.

**Owner mechanism.** GitHub account (renewable credentials only — device OAuth/SSH/app, never recovery codes); Tailscale OAuth via GitHub; Tailscale install per platform.

**Law.** Phase 4 (identity: machine identity is not authority; each machine joins under the deployment's tailnet, named explicitly), Phase 6 (routing: the tailnet is the private control plane; nothing private is exposed publicly for convenience), Phase 10 (renewable ladder).

**Scars.** GitHub MFA prompts mid-flow halt automation → default: device OAuth / approved renewable routes only; MFA consent batched into the owner moment. Machines that missed tailnet join "look online" but are unreachable → default: verify from both sides. Check: `tailscale status` agrees on every machine; agents reach the VPS over the tailnet and cannot reach unenrolled machines.

**Consent.** GitHub account auth + Tailscale approval = owner moments (Stage 0 surface).

**Check.** The AC demonstrates: workstation → VPS over tailnet; second enrolled machine reachable; unenrolled host unreachable. Mesh surfacing proven in both directions.

**Exit.** All in-scope machines enrolled; agents move between them under granted identity; no public exposure of private services.

# Stage 5 — Knowledge + audit

**Steps.** Document all; set up gog CLI across the G Suite products; run the full business audit to categorize the business — on **two lanes**: (1) machine-visible sources (gog, filesystem, existing docs, browser-accessible systems), and (2) an **owner-knowledge interview for what no system shows** — undocumented processes, informal schedules, tribal rules, things the owner simply tells and no tool can discover. The interview is structured (CRIST interview style) and its answers feed roles, crons and processes directly. Core audit categories: people and roles, processes and schedules, tools and systems, communication surfaces, recurring work, money flows, exceptions and tribal rules — deepened as evidence raises questions; interview answers are first-class findings, cited like source handles, never re-collected once recorded. Core interview prompts (deepened per client, never a fixed exam): what a good week looks like; who does what and who approves; which recurring tasks eat the most time; where money comes in and goes out; how clients and staff communicate; what breaks when the owner is away; what was abandoned because it hurt too much; what should have been automated years ago; what must never be delegated.

**Owner mechanism.** Agent-KB/bootstrap + Focusa evidence for documentation; gog CLI with Google OAuth consent. The local CoS (Stage 2) orchestrates; build agents (browser via UIAI, computer use via Pi) execute the reading and documentation.

**Law.** Phase 7 (discovery/documentation: docs derive from canonical sources; runtime facts carry freshness), Phase 9 (evidence: the audit produces attributable findings, not anecdotes), Phase 3 (freshness: audit results carry timestamps and re-derive from canonical sources).

**Scars.** OAuth consent assumed = dead end → default: gog consent is a designed owner moment; scopes least-privilege. Check: gog reads mail/calendar/drive as granted. Audit-from-memory drift → default: audit reads live sources (gog, filesystem, existing docs), never recollection. Check: every audit finding cites a live source handle.

**Consent.** Google OAuth consent = one owner moment (Stage 0 surface). The owner-knowledge interview = one structured owner session (batched, interview-style — not scattered asks). The audit itself is agent-executed.

**Check.** The CoS produces the categorization (business details, systems-of-common-tasks candidates, communication surfaces, recurring workflows) — with **every finding citing a live source handle or an interview reference** — and the operator can see the same categorization in a durable artifact (Agent-KB/Wiki record), not just in chat.

**Exit.** Business categorization exists as durable, attributable knowledge; gog operates under granted scopes.

# Stage 6 — Chief of Staff ascends (relocate to the cloud)

**Steps.** Move the **git-backed** CoS folder to the VPS; OpenClaw runs there; from the cloud it **administers the entire tailnet primarily** — employees, crons, workflows, machine agents. Deploy the **Svelte CoS UI** to a **subdomain of the client's website** (e.g. `cos.<client-domain>`) via wrangler — using the DNS control installed in Stage 1. The CoS now lives web-reachable at its own address: runtime on the VPS, UI on the client subdomain.

**UI access (woven rule).** The CoS interface is never open-by-default. Access is initially restricted to the Canonical Owner Principal (Verious Smith III in the reference deployment) and the business's primary owner/operator; broader access is a later, explicit decision. The authentication mechanism rides the deployment's existing auth surfaces, chosen per deployment.

**Why through git (woven rationale).** The Stage 2 design pays off here: ascension moves source through git (push from workstation / clone on VPS); runtime and private state use their owning transfer mechanisms. History, reviewability and rollback travel with the CoS; the local folder becomes a mirror/backup, no longer the admin point.

**Owner mechanism.** Git remote (already in place from Stage 2); OpenClaw's canonical install/run path on the VPS; tailnet routing from Stage 4.

**Law.** Phase 5 (runtime/execution surfaces: the CoS role continues across relocation; worker continuity preserved — a runtime move must not erase canonical continuity), Phase 6 (cloud-primary administration over the private tailnet; nothing public exposed), Phase 12 (delivery: the relocation is a deployment with verification, not a copy).

**Scars.** Relocation by copy-paste loses git history and diverges state → default: source moves via git; verify history intact after clone; private state moves through its owning mechanisms. Post-relocation limbo ("is it local or cloud now?") → default: one explicit cutover; the VPS is primary, the local folder is mirror/backup and remains the rollback until the cloud path proves itself. *Client's website DNS not on Cloudflare* → default: **transfer the zone to Cloudflare** — the standing choice, non-negotiable; the transfer is a consented, staged change with the old zone records preserved for rollback; never assume zone access before the transfer completes. Check: CoS healthy on the VPS; `git log` intact; tailnet administration answers from the cloud; a test orchestration issued from the VPS reaches an enrolled machine.

**Consent.** None new — designed in Stage 0.

**Check.** From the VPS, the CoS reaches every enrolled machine; from the workstation, the AC reaches the CoS. Cloud-primary administration is proven in both directions. The subdomain resolves from the public internet and the **Svelte CoS UI answers there**, with access authenticated and limited to the designed access list.

**Exit.** OpenClaw administers the tailnet from the cloud primarily; the local genesis folder is a synced mirror.

# Stage 7 — Operating plane

**Steps.** OpenClaw as Chief of Staff (now cloud-primary from Stage 6); create the business owner voice profile for correspondence; create systems of common tasks; create crons for regular workflows; set up virtual employees through **CRIST role packets**: long-running employees get full packets (context, role, spec, tasks, permissions, tool allowances); short-term workers get lightweight worker-role packets spun up and retired per need. **Permissions and tool allowances are explicit per role** — Focusa grants plus provider tool surfaces (UIAI browser, gog scopes, rbw access classes, computer-use permissions). Type each piece of work by its shape: fixed schedule with deterministic steps → cron; recurring judgment or multi-system coordination → persistent employee; bounded one-off effort → temporary worker with expiry and cleanup; occasional steps a human simply runs → documented procedure, not automation. The audit decides; templates only accelerate. **Mechanics:** a temporary worker's lightweight packet carries its bounded scope, expiry and cleanup duties — grants revoked, receipts archived, access removed at end of job; a persistent employee activates only after its packet is approved (batched), starts with limited scope, and rolls back by disabling its crons and revoking its grants — receipts preserved either way.

**Owner mechanism.** OpenClaw chief-of-staff surface (administering from the cloud), **owner-facing web UI at the client's subdomain**; voice profile pipeline; task/employee provisioning per existing role/permission contracts. Local build agents (browser + computer use) remain the hands on client machines; the CoS delegates across the tailnet.

**Law.** Phase 5 (runtime/execution surfaces: role-based employees, exact scopes, no sovereign fallback), Phase 4 (each virtual employee is an explicit principal with scoped grants), Spec 135B (CRIST: role composition, interview corpus, approved profiles for agents), Phase 9 (evidence: crons and employees leave receipts), Phase 11 (entitlements only where the client profile has them), Phase 12 (delivery: changes to employees/crons land through the deployment's own release path).

**Scars.** Correspondence-style drift → default: build the style profile from approved correspondence examples and owner feedback; audio samples only if the owner chooses; validate against real messages before use. Crons silently dying → default: every cron writes a heartbeat/receipt; missing heartbeats surface as alerts, not silence. Employees with ambient tool access → default: per-role toolsets and permissions enumerated at creation; least privilege; **no employee exists without an approved role packet naming its allowances**. Check each: voice round-trip verified; cron heartbeat visible; employee executes its one representative action and cannot act outside its scope.

**Consent.** Correspondence-style review = one owner moment; audio samples only if chosen. Employee role definitions = agent-proposed, owner-approved once as a batch (a design decision, not a repetitive ask).

**Check.** One representative recurring workflow runs end-to-end: cron fires (cloud) → CoS delegates to an employee → employee executes through granted tools on the target machine → receipt lands → owner-visible result. The denial test: the employee cannot act outside its role.

**Exit.** The operating plane runs the first real workflows with evidence, under scoped roles, administered from the cloud.

# Stage 8 — Ongoing operation and handoff

**Steps.** "This is just the beginning": hand off from build-out to life. Working means the owner's week-one reality: the agent operates the routine work, the owner approves and informs, and the first useful CoS outcome named in Stage 0 is delivered. Spend (plans, subscriptions, hosting) stays visible to and reconciled by the Canonical Owner Principal and the business's primary owner/operator; the agent records costs in the deployment's existing evidence surfaces and flags variances — no separate billing dashboard. Document the deployment; verify the replacement-agent test; establish the optimization loop (below) as the operating rhythm.

**Law.** Phase 13 (acceptance/handoff) and the replacement-agent test: a fresh agent orients from durable state — engagement record, Agent-KB, Focusa evidence, this doctrine's per-deployment record — not from the builder's memory.

**Check.** Replacement-agent test: from documented entry points alone, it orients (owner, scope, capabilities, health) and completes one representative maintenance action with evidence. Acceptance rows reconciled; unknowns disclosed.

**Exit.** The client runs. The doctrine (this doc) is updated with that deployment's scars and lessons — feeding the loop below.

---

## Coverage map — spine stages ↔ 0.1.0 phases (coverage aid, not implementation proof)

| 0.1.0 phase | Carried by |
|---|---|
| 0 Identity/owner/profile | Stage 0 (engagement record, owner binding) |
| 1 Scaffold/baseline | Stage 1 (workstation substrate) + Stage 2 (CoS genesis) |
| 2 State ownership | Stage 2 (folder vs owned services) + Stage 3 (substrate) + Stage 5 (audit state) + Stage 6 (source vs private-state relocation) + optimization loop (state map maintained there) |
| 3 Derived/freshness | Stage 1 (agent-kb bootstrap) + Stage 5 (audit findings carry timestamps) + tracking loop (freshness checks) |
| 4 Identity/auth/tenancy | Stage 0 consent design + Stage 4 (mesh identity) + Stage 7 (employee principals) |
| 5 Agent runtime/surfaces | Stage 1 (harnesses) + Stage 2 (CoS genesis, CRIST role) + Stage 6 (ascension) + Stage 7 (CRIST employee/worker roles) |
| 6 Network/routes | Stage 4 (tailnet) + Stage 3/6 (private control plane) + Stage 6 (client-website subdomain via wrangler DNS control) |
| 7 Discovery/documentation | Stage 1 (bootstrap) + Stage 5 (documentation + owner-knowledge interview corpus) + Stage 8 (documented deployment) |
| 8 Agent surface | Stage 1 (UIAI browser parity + computer use) + Stage 2/6 (Svelte CoS UI at the client subdomain) + Stage 5 (gog) + per-stage checks (acceptance descriptions until GP-06 binds them) |
| 9 Observability/evidence/cost | Stage 0 (spend envelope) + Stage 3 (control plane) + Stage 7 (receipts) + Stage 8 (spend visibility/reconciliation) + tracking loop |
| 10 Secrets/permissions/revocation | Stage 1 (Bitwarden/rbw + secrets consolidation) + Stage 0 (consent design) + Stage 7 (role grants, tool allowances) |
| 11 Entitlements/licensing | Client-profile overlay (provider subscriptions; client licensing where applicable) — applied via Stage 0 consent design, not a separate stage. The client-app wrapper adds no separate license: component licenses apply identically to bundled, individually downloaded, or DIY self-hosted use. The wrapped process (app, deterministic library, operated design) is operator intellectual property — functional only under the active payment and support contract |
| 12 Tests/CI/deploy/rollback | Per-stage checks + Stage 2/6 (git-backed portability, staged cutover and DNS-transfer rollback) + optimization loop's verification path |
| 13 Launch/acceptance/handoff | Stage 8 + replacement-agent test in GP-13 |

## Task ledger (execution tracking)

One ordered ledger; task IDs are reused when work enters the existing task/CallGraph system.

| ID | Status | Depends on | Done-condition |
|---|---|---|---|
| GP-01 | done | — | Upstream docs pulled/read; lineage `3658ecc`; no duplicate ledger. |
| GP-02 | done | GP-01 | Starter essence compared; first clarification published; findings recorded. |
| GP-03 | in_progress | GP-02 | This woven doctrine: stages 0–8 carry law/scars/consent/checks. Done when the operator's process, dependencies and open specifics are reviewed as a coherent planning draft. Exact live bindings remain GP-06 work, not a prerequisite for GP-03. |
| GP-04 | planned | GP-03 | Live estate reconciliation through approved read-only routes; configured/reachable/usable-by-agent/verified classified with evidence; consent-surface inventory validated against Stage 0's design. |
| GP-05 | planned | GP-04 | State-ownership map: every material store has canonical owner, scope, freshness, backup, recovery; no synchronization store. |
| GP-06 | planned | GP-05 | Every spine step classified **deterministic** (bound to an owning script/API/form — idempotent, agent-supervised) or **probabilistic** (bound to ACITL judgment and batched owner moments), then bound to real existing commands/APIs — including git-backed CoS genesis/ascension bindings and ACITL bindings (which steps the AC executes; which are AC-driven-owner-typed; where grants live). No invented commands. |
| GP-07 | planned | GP-06 | Design reviewed against normal/partial/denied/interrupted runs; zero-human-turns test applied per step; smallest unresolved implementation backlog produced. |
| GP-08 | planned | GP-07 | First highest-leverage slice selected from observed gaps (prefer restoring an existing capability). Owning repo, surfaces, authority, acceptance, rollback recorded. |
| GP-09 | planned | GP-08 | Slice implemented/tested in its owning subsystem; deployed only to its approved proving destination; positive/denial/retry/failure behaviors proven. |
| GP-10 | planned | GP-09 | Bounded end-to-end workflow through the real CoS/worker path including an ACITL consent moment; user-visible result + scoped receipt proven. |
| GP-11 | planned | GP-10 | Brownfield reproducibility: fresh build-out, partial adoption, rerun, interruption, rollback — including the Stage 2→6 git-backed relocation path; no duplicates, no private-state import. |
| GP-12 | planned | GP-11 | Isolated client profile with synthetic principals: function AND cross-tenant denial; consent surface batched as designed; secrets never transit agent storage. |
| GP-13 | planned | GP-12 | Replacement agent orients and continues from durable state; acceptance rows reconciled; **0.2.0 published from evidence**; honest handoff. |

## The optimization & tracking loop (the "continually optimized and tracked" end state)

The doctrine's end state is not a finished doc — it is a running system with its own improvement loop, which this doc also governs:

```text
RUN (deployments/workflows execute through the spine)
→ TRACK (receipts, heartbeats, consent-surface count, scar ledger, stage checks)
→ DETECT (a failed check, a new scar, a manual moment that should have been automated)
→ ENCODE (fix the default; attach the scar to its stage; adjust the consent surface)
→ PUBLISH (next doctrine revision; normally 0.2.0+)
→ VERIFY (replacement agent can re-orient from durable state)
```

Tracking surfaces (all existing, nothing new built): Focusa workpoint/evidence for stage progress and receipts; Agent-KB for deployment knowledge and freshness; the scar ledger (this doc) for paid-for failures; the task ledger above for execution state. The loop's health check: every stage's checks pass, consent surface still matches its design, and the scar ledger's latest revision reflects the last real deployment.

## Completion criteria (whole doctrine)

- Every spine step: class, owning mechanism, law, scars, consent design, embedded check, exit — no undocumented manual prerequisite. Dependencies are explicit where they matter; existing tracking preserves verified progress and the next action without a separate runner.
- Known consent needs are batched; necessary new approvals remain possible. Consolidated renewable credentials use scoped rbw retrieval or the approved provider-native credential mechanism; secret values stay out of chat, Git and evidence; nonrenewable assets remain untouched.
- **Every agent role — CoS, long-running employees, short-term workers — exists as an approved CRIST role packet with explicit permissions and tool allowances**; audit findings cite live sources or interview references.
- The CoS is web-reachable at the client's subdomain (Svelte UI), runtime cloud-primary; model lanes provisioned (premium for CoS/high-stakes, economy via OpenCode Go/OpenRouter for build agents).
- CoS state is git-backed from day one; ascension preserves history; cloud-primary tailnet administration is verified.
- Fresh/partial/rerun/interrupted/recovery paths behave as specified on real brownfield machines.
- Function AND denial proven; no sovereign fallback; receipts attributable.
- The optimization loop runs on the deployed system (heartbeats visible, scars feeding back, doctrine versioning advancing).
- A replacement agent continues from durable references; no secrets or private client data in this doc.

## Findings and evidence limits (iterations 5–16)

- Iteration 16 (2026-09-10): operator fixed the **IP boundary** — the wrapped process is the operator's intellectual property and is non-functional without the payment and support contract; enforcement is structural (the app exists only to connect to the operated service), while sovereign components stay client-owned under their own licenses. Clean three-layer ownership: client owns infra/data/sovereign components; operator owns the wrapped process and the operation.

- Iteration 15 (2026-09-10): operator sharpened the boundary — **the wrapped app would not work without a support contract either**: it is inert by design without the Agent Operator/CoS behind it, so no standalone mode ships; the DIY path is the individual sovereign components running standalone. The two paths are distinct products of one substrate, and neither pretends to be the other.

- Iteration 14 (2026-09-10): **sovereignty/licensing boundary** recorded — the bundled app is a wrapped process, not a special licensed product; component licenses apply identically to DIY self-hosting without a support contract; the client-app value proposition rests on the operated process (Agent Operator, CoS, ongoing support), positioned by the operator as far exceeding the DIY download. DIY sovereignty remains the standing promise of both engines.

- Iteration 13 (2026-09-10): operator named the app **the potential core product** — quiet governed presence, customer dashboard over the CoS (workflows/schedules/receipts), Pi SDK + Focusa + UIAI embedded as governed component updates. Positioning recorded against the planned operator/DIY surfaces (Focusa Desktop, UIAI Cockpit, Focusa.work): two audiences, one substrate, no duplicated governance. The customer-facing app remains a proposed vehicle; the CoS stays cloud-primary and the script path still precedes packaging (GP-06 first).

- Iteration 12 (2026-09-10): operator scoped the proposed client app further — **branded walkthroughs** (consent sitting as guided UX), **bounded data upload** to isolated agent endpoints (audit/document sources travel consent-scoped with per-transfer receipts; secrets never transit), and **support sessions** (customer opens the app, consents, watches a time-boxed agent session — the Veragensia remote-support entry point, reusing the read-only/controller sharing roles already proven on the Selkies demo). Phasing guard unchanged: script path first (GP-06), then the app packages it.

- Iteration 11 (2026-09-10): operator proposed a **Tauri-based Windows/macOS client app** as the vehicle for the deterministic library — one download, connects to the cloud Agent Operator, hosts owner-moment forms locally, exposes a typed command surface for the AC, reports receipts. Woven as a proposed vehicle with explicit conditions (script path proven first, signing cost in spend envelope, scoped revocable tokens, no second OS). Not a build authorization.

- Iteration 10 (2026-09-10): **mechanism split** woven — deterministic steps (installs, provisioning, git, DNS via Cloudflare API, crons, checks, receipts) get owning idempotent code with the agent supervising; probabilistic steps (API-less browser flows, bot-checks/CAPTCHA, interview, audit judgment, role design, recovery) keep agent-in-the-loop with batched owner moments. GP-06's done-condition updated to produce that split as its binding output. This is the operator's mental model now encoded in the spine.

- Iteration 9 (2026-09-10): placement rule woven into Stage 4 (cloud CoS runs schedules; machine-local agents wait or reroute when a workstation is off); temporary-worker lifecycle and employee-activation rollback defined in Stage 7; Stage 0 first-outcome examples added; coverage map reconciled — state ownership now spans Stages 2/3/5/6, spend visibility joins row 9, and stage checks are labeled acceptance descriptions until GP-06 binds them. Remaining planning gap: absent-prerequisite variations (client without a website for the CoS subdomain; client without Google Workspace for gog).

- Operator specifics woven, second pass (2026-09-10): the CoS ships as a **Svelte UI living at a subdomain of the client's website** (deployed at ascension via wrangler); **cf CLI/wrangler and gh CLI installed early** — device-approval flows when absent locally — giving build agents CLI access and **full DNS control**; **OpenAI device access + developer mode enabled early**; model strategy = **OpenAI Pro for premium work plus OpenCode Go and OpenRouter for cheaper-model lanes**.
- Agent-centric pass (2026-09-10, iteration 7): invariant 1 reworded to agent-operated setup; 'everything in the browser' restated as a verified capability target; secret-entry requires verified environmental isolation; Stage 2 no longer assumes OpenClaw must run locally from the folder; relocation moves source through git and private state through its owning mechanisms; consent surface is primary but not exhaustive; audit schema seeded; Stage 8 defines the owner's week-one working test.
- Scar provenance: observed scars come from operator-reported friction (AV/script blocking, missing terminal, missing Node, scattered secrets, missed verification windows); others (correspondence-style drift, cron heartbeats, per-role denials) are hypothesized defaults to validate in real runs — not claimed incidents.
- Flesh-out pass (2026-09-10): Stage 0 names the first useful CoS outcome and tallies owner moments; Stage 2 defines the minimal workspace start and first capability; Stage 5 adds the core interview prompts; Stage 7 adds the cron/employee/worker/procedure decision rule. Interview prompts and examples are planning defaults — refined by real runs, never fixed exams. Version-stream metadata is consolidated in this document (the separate changelog entry for the planning stream was withdrawn) to keep this the single iterable record.
- Gap-fill pass (2026-09-10, iteration 8): **Cloudflare is the DNS of choice** — agent tooling, non-negotiable; zones elsewhere (Porkbun precedent) transfer to Cloudflare during the build. **CoS UI access starts restricted** to the Canonical Owner Principal and the business's primary owner/operator. **Spend visibility and reconciliation belong to the same two people**, recorded through existing evidence surfaces. Open planning item for future iterations: absent-prerequisite variations (client without a website to host the CoS subdomain; client without Google Workspace for gog).
- 0.1.1 status corrected: it is superseded planning input — retained for lineage, not an active candidate.
- Operator refinements woven (2026-09-10): dependencies and independent lanes are explicit without mandatory per-step tags; **secrets consolidation** added to Stage 1 (browser imports, old managers, sticky notes → one vault, rbw as the single retrieval surface); the audit gains an **owner-knowledge interview lane** for what no system shows (undocumented processes, schedules, tribal knowledge); **CRIST (Focusa Spec 135B)** integrated — CoS genesis runs the CRIST interview, long-running employees get full role packets, short-term workers get lightweight packets, permissions and tool allowances explicit per role.

- Operator key facts woven in (2026-09-10): the Chief of Staff **starts as a desktop folder backed by git**, then **moves to the VPS later**, where OpenClaw **administers the entire tailnet from the cloud primarily**; OpenClaw uses Focusa and UIAI Engine plus local build agents to navigate the web, log in to websites, and fully build out the system; UIAI Engine is added **early** to give local build agents tools to do everything in the browser a human can do; agents also do **computer use from Pi**. The spine now carries CoS genesis (Stage 2) and ascension (Stage 6) as first-class stages.
- Locked invariants evolved: zero-human-turns reworded to agent-operated setup in iteration 7; ACITL, brownfield-first, starter essence (defaults/scars/checks/order), reuse-first unchanged.
- Still documentation-iteration only: no installer, live reconciliation, customer rollout, or end-to-end acceptance has occurred. GP-04 onward open.
- Tooling defects filed this week (not doctrine blockers): uiai-engine #224 (browser delivery), wirebot-core #31/#32, focusa #599/#600/#601.

Sources: operator as-built process, scars, and directives (2026-09-10); [0.1.0](0.1.0.md); [0.1.1](0.1.1.md); [server handoff](SERVER_AGENT_HANDOFF.md); starter verbatim reference (`https://burcs.dev/starter.md`).