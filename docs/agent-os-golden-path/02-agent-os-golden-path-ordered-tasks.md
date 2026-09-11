# Golden Path — the interwoven doctrine (single iterable source)

- Date: 2026-09-10 (iteration 3 — woven, not appended)
- **The artifact:** one process an agent executes to build out the Human Life & Business Agent OS on a current brownfield client workstation, end to end, with zero human turns during setup. Everything below is one woven design: the spine stages carry the law, the scars, the checks, the consent design, and the tracking loop — not parallel sections.
- **Locked invariants** (every revision derives from these):
  1. **Zero human turns.** A step passes when a fresh agent, holding granted credentials, executes it without asking. Failures get an authorized automation path or are classified as an owner moment — exact, batched, minimal.
  2. **ACITL.** The Agent Computer (Veragensia, remote access) is the loop's hands. The owner is the grantor. Secret entry is AC-driven, owner-typed: the AC opens the form, the owner types once, the agent never sees or stores the secret.
  3. **Brownfield-first.** Start on the client's existing computer; audit what exists; build out. Never assume a clean machine; distinguish pre-existing from newly created resources.
  4. **Starter essence.** Defaults are pre-made decisions; scars are paid-for failures attached to the step that pays them; every step has one embedded check; order is dependency-true. Phase numbering is coverage, never schedule.
  5. **Reuse-first.** Existing mechanisms own every step (Pi, Focusa lifecycle, UIAI, rbw, gog, GitHub/Tailscale auth, OpenClaw, provisioning). This doctrine names owners; it never replaces them.
- **Published lineage:** [0.1.0](0.1.0.md) phases remain the coverage scaffold (mapping table below); [0.1.1](0.1.1.md) clarifications stand. This doc is the single working source targeting **0.2.0**.
- **Acceptance truth:** iteration/documentation only so far. No installer, customer rollout, or end-to-end acceptance is claimed. The end state of all this planning is a **fully documented and working process and system** — executed, verified, and continuously optimizable and tracked.

## How this doc is organized (and why)

Everything is staged on the **spine** — the operator's proven deployment sequence. Each stage weaves together, in one place: what happens (steps + step class), which existing mechanism owns it, what law applies (phase invariants), what scars it pays (with defaults/checks), what owner moments it contains (consent design), and what proves it (stage check). The 14-phase scaffold is a coverage index at the end — proving nothing was dropped — not a second structure. Tasks, optimization, and tracking close the loop.

```text
Stage 0  Engage — engagement, access, owner consent design
Stage 1  Workstation substrate
Stage 2  Remote control plane
Stage 3  Mesh + identity
Stage 4  Knowledge + audit
Stage 5  Operating plane
Stage 6  Ongoing operation (handoff)
→ Coverage map (14 phases) → Task ledger → Optimization & tracking loop
```

Per-stage anatomy (identical shape every stage):

```text
STEPS → OWNER MECHANISM → LAW → SCARS → CONSENT → CHECK → EXIT
```

---

# Stage 0 — Engage: engagement, authority, consent design

**Steps.** Open the engagement; establish the Canonical Owner Principal for this deployment (owner constitution, portable owner binding); agree the outcome, scope and data boundaries; enumerate the **consent surface** for this client; record what exists (machines, accounts, software) before touching anything.

**Owner mechanism.** Owner constitution + `OWNER_AUTHORITY_CONSTITUTION.md` pattern; Focusa project identity for the engagement; existing audit/engagement docs.

**Law.** Phase 0 (identity/owner/profile) and Phase 4 invariants govern from the first action: authentication is not authority; tenant identity is never inferred from hostname, user, or directory; private operations fail closed on unknown scope.

**Scars.** Client machines carry prior admin accounts, stale AV, and unknown software; assuming a clean machine produces duplicate installs and broken personalization. Default: audit before install, always; record pre-existing state and reuse it.

**Consent.** This stage *designs* the consent surface for the whole deployment: one batched owner moment per provider (below), plus any client-specific exclusions. The count of owner moments is fixed here — later stages may not invent new asks.

**Check.** The engagement record answers: owner (verified, not assumed), machines in scope, accounts in scope, consents required (enumerated, with their providers), and what must not be touched. A second agent reading it reaches the same conclusions.

**Exit.** Engagement record + consent surface exist and are the only owner moments for the whole build-out.

# Stage 1 — Workstation substrate

**Steps.** Install Pi; connect the model provider (OpenAI subscription or OpenRouter); download Focusa; download UIAI Engine; set up Bitwarden (shared vault); set up rbw for agent-side secret retrieval.

**Owner mechanism.** Pi installer; provider signup; Focusa install lifecycle (`focusa` installer/update path); UIAI install; Bitwarden app + rbw CLI. Each installs through its own official route — this doctrine sequences and checks them, never forks them.

**Law.** Phase 1 (scaffold: inspect first, idempotent, discoverable locations), Phase 3 (freshness: `agent-kb bootstrap` establishes knowledge freshness from the start), Phase 7 (discovery: agent orients from documented entry points, not tribal memory), Phase 10 (secrets: Bitwarden holds secrets; rbw retrieves exact approved fields; nothing secret in config).

**Scars (Windows brownfield).**
- *AV/script blocking kills installers, npm lifecycle scripts, downloaded scripts* → signed official installers only; no silent exclusions. Check: installer completes; signed binary runs.
- *No proper terminal* → Windows Terminal + PowerShell 7; WSL-vs-native decided once per engagement. Check: agent harness runs in the installed terminal.
- *No node/npm* → official Node installer; PATH set. Check: `node -v && npm -v` succeed in the agent's shell.
- *UAC prompts scattered* → batch elevation into one moment. Check: elevation prompts per build-out = 1.
- *PowerShell execution policy / Defender ASR blocks agent scripts* → per-script unblock; blanket policy change is a consent item, never silent. Check: authorized scripts execute; unrelated scripts stay blocked.

**Consent.** Provider account/billing (OpenAI/OpenRouter) = one owner-typed moment through an AC-opened browser. Bitwarden master password = AC-driven, owner-typed, never seen by the agent. AV exclusions, if any = owner consent item with named scope.

**Check.** From a cold shell, the agent runs: Pi answers a model round-trip; `focusa` status is healthy; UIAI health responds; `rbw` retrieves an exact approved field (value never printed); `agent-kb bootstrap` returns fresh knowledge state.

**Exit.** Workstation substrate is agent-operable: the AC on this machine can run the harness, retrieve renewable secrets, and reach the knowledge plane — with the owner's typed moments already spent.

# Stage 2 — Remote control plane

**Steps.** Create the OVH VPS account; respond to verification emails; log in via browser to the VPS; install OpenClaw on the VPS as Chief of Staff.

**Owner mechanism.** OVH provisioning; email verification via the client's consented mailbox (gog, Stage 4 — dependency: consent ordered before it is needed); OpenClaw install per its canonical path on the VPS.

**Law.** Phase 2 (state ownership: VPS runtime is *coordination/execution*, not canonical truth), Phase 5 (agent runtime: CoS role explicit; worker isolation), Phase 6 (routes: private control plane stays private), Phase 10 (renewable-only authentication for automated access; verification emails are owner-consented automation, not recovery codes).

**Scars.** Verification emails missed/expired mid-flow → default: the AC monitors the consented mailbox and completes verifications within their window. Check: VPS reachable, verified, logged in without further owner action. Kernel/OS defaults on fresh VPS lack the agent's toolchain → default: provision through the deployment's documented provisioning path, not ad-hoc apt historics. Check: `wb` (or the deployment's CLI) healthy on the VPS.

**Consent.** VPS account creation/billing + mailbox consent = owner moments (designed in Stage 0). Everything after them is AC-executed.

**Check.** From the workstation, the AC: SSHes to the VPS on granted credentials, confirms OpenClaw healthy, and confirms the control plane answers only on the private route.

**Exit.** Chief of Staff runs on the VPS; the workstation agent reaches it over the private route; zero owner turns after the designed moments.

# Stage 3 — Mesh + identity

**Steps.** Create GitHub (if none); use GitHub to authenticate Tailscale; install Tailscale on all machines; connected machines allow agents to surf between.

**Owner mechanism.** GitHub account (renewable credentials only — device OAuth/SSH/app, never recovery codes); Tailscale OAuth via GitHub; Tailscale install per platform.

**Law.** Phase 4 (identity: machine identity is not authority; each machine joins under the deployment's tailnet, named explicitly), Phase 6 (routing: the tailnet is the private control plane; nothing private is exposed publicly for convenience), Phase 10 (renewable ladder).

**Scars.** GitHub MFA prompts mid-flow halt automation → default: device OAuth / approved renewable routes only; MFA consent batched into the owner moment. Machines that missed tailnet join "look online" but are unreachable → default: verify from both sides. Check: `tailscale status` agrees on every machine; agent can reach the VPS over the tailnet and cannot reach unenrolled machines.

**Consent.** GitHub account creation/auth + Tailscale approval = owner moments (Stage 0 surface).

**Check.** The AC demonstrates: workstation → VPS over tailnet; second enrolled machine reachable; unenrolled host unreachable. Mesh surfacing proven in both directions.

**Exit.** All in-scope machines enrolled; agents move between them under granted identity; no public exposure of private services.

# Stage 4 — Knowledge + audit

**Steps.** Document all; set up gog CLI across the G Suite products; run the full business audit to categorize the business.

**Owner mechanism.** Agent-KB/bootstrap + Focusa evidence for documentation; gog CLI with Google OAuth consent.

**Law.** Phase 7 (discovery/documentation: docs derive from canonical sources; runtime facts carry freshness), Phase 9 (evidence: the audit produces attributable findings, not anecdotes), Phase 3 (freshness: audit results carry timestamps and re-derive from canonical sources).

**Scars.** OAuth consent assumed = dead end → default: gog consent is a designed owner moment; scopes least-privilege. Check: gog reads mail/calendar/drive as granted. Audit-from-memory drift → default: audit reads live sources (gog, filesystem, existing docs), never recollection. Check: every audit finding cites a live source handle.

**Consent.** Google OAuth consent = one owner moment (Stage 0 surface). The audit itself is agent-executed.

**Check.** The AC produces the categorization (business details, systems of common tasks candidates, communication surfaces, recurring workflows) with source handles — and the operator can see the same categorization in a durable artifact (Agent-KB/Wiki record), not just in chat.

**Exit.** Business categorization exists as durable, attributable knowledge; gog operates under granted scopes.

# Stage 5 — Operating plane

**Steps.** OpenClaw as Chief of Staff (from Stage 2); create the business owner voice profile for correspondence; create systems of common tasks; create crons for regular workflows; set up virtual employees with role-based toolsets and permissions.

**Owner mechanism.** OpenClaw chief-of-staff surface; voice profile pipeline; task/employee provisioning per existing role/permission contracts.

**Law.** Phase 5 (runtime/execution surfaces: role-based employees, exact scopes, no sovereign fallback), Phase 4 (each virtual employee is an explicit principal with scoped grants), Phase 9 (evidence: crons and employees leave receipts), Phase 11 (entitlements only where the client profile has them), Phase 12 (delivery: changes to employees/crons land through the deployment's own release path).

**Scars.** Voice profile trained on wrong sample quality → default: owner records the consented sample once, pipeline validates before use. Crons silently dying → default: every cron writes a heartbeat/receipt; missing heartbeats surface as alerts, not silence. Employees with ambient tool access → default: per-role toolsets and permissions enumerated at creation; least privilege. Check each: voice round-trip verified; cron heartbeat visible; employee executes its one representative action and cannot act outside its scope.

**Consent.** Voice samples = one owner moment. Employee role definitions = agent-proposed, owner-approved once as a batch (this is a design decision, not a repetitive ask).

**Check.** One representative recurring workflow runs end-to-end: cron fires → employee executes through granted tools → receipt lands → owner-visible result. The denial test: the employee cannot act outside its role.

**Exit.** The operating plane runs the first real workflows with evidence, under scoped roles.

# Stage 6 — Ongoing operation and handoff

**Steps.** "This is just the beginning": hand off from build-out to life. Document the deployment; verify the replacement-agent test; establish the optimization loop (below) as the operating rhythm.

**Law.** Phase 13 (acceptance/handoff) and the replacement-agent test: a fresh agent orients from durable state — engagement record, Agent-KB, Focusa evidence, this doctrine's per-deployment record — not from the builder's memory.

**Check.** Replacement-agent test: from documented entry points alone, it orients (owner, scope, capabilities, health) and completes one representative maintenance action with evidence. Acceptance rows reconciled; unknowns disclosed.

**Exit.** The client runs. The doctrine (this doc) is updated with that deployment's scars and lessons — feeding the loop below.

---

## Coverage map — spine stages ↔ 0.1.0 phases (proves nothing was dropped)

| 0.1.0 phase | Carried by |
|---|---|
| 0 Identity/owner/profile | Stage 0 (engagement record, owner binding) |
| 1 Scaffold/baseline | Stage 1 (workstation substrate) |
| 2 State ownership | Stage 4 + optimization loop (state map maintained there) |
| 3 Derived/freshness | Stage 1 (agent-kb bootstrap) + tracking loop (freshness checks) |
| 4 Identity/auth/tenancy | Stage 0 consent design + Stage 3 (mesh identity) + Stage 5 (employee principals) |
| 5 Agent runtime/surfaces | Stage 1 (harnesses) + Stage 2 (OpenClaw) + Stage 5 (employees) |
| 6 Network/routes | Stage 3 (tailnet) + Stage 2 (private control plane) |
| 7 Discovery/documentation | Stage 1 (bootstrap) + Stage 6 (documented deployment) |
| 8 Agent surface | Stage 1 (UIAI) + Stage 4 (gog) + per-stage checks as machine-readable checks |
| 9 Observability/evidence/cost | Stage 2 (control plane) + Stage 5 (receipts) + tracking loop |
| 10 Secrets/permissions/revocation | Stage 1 (Bitwarden/rbw) + Stage 0 (consent design) + Stage 5 (role grants) |
| 11 Entitlements/licensing | Client-profile overlay (provider subscriptions; client licensing where applicable) — applied via Stage 0 consent design, not a separate stage |
| 12 Tests/CI/deploy/rollback | Per-stage checks + optimization loop's verification path |
| 13 Launch/acceptance/handoff | Stage 6 + replacement-agent test in GP-13 |

## Task ledger (execution tracking)

One ordered ledger; task IDs are reused when work enters the existing task/CallGraph system.

| ID | Status | Depends on | Done-condition |
|---|---|---|---|
| GP-01 | done | — | Upstream docs pulled/read; lineage `3658ecc`; no duplicate ledger. |
| GP-02 | done | GP-01 | Starter essence compared; first clarification published; findings recorded. |
| GP-03 | in_progress | GP-02 | This woven doctrine: stages carry law/scars/consent/checks. Done when stages 0–6 above are each bound to real mechanisms in GP-06's pass and scars stop being append-only. |
| GP-04 | planned | GP-03 | Live estate reconciliation through approved read-only routes; configured/reachable/usable-by-agent/verified classified with evidence; consent-surface inventory validated against Stage 0's design. |
| GP-05 | planned | GP-04 | State-ownership map: every material store has canonical owner, scope, freshness, backup, recovery; no synchronization store. |
| GP-06 | planned | GP-05 | Every spine step bound to real existing commands/APIs including ACITL bindings (which steps the AC executes; which are AC-driven-owner-typed; where grants live). No invented commands. |
| GP-07 | planned | GP-06 | Design reviewed against normal/partial/denied/interrupted runs; zero-human-turns test applied per step; smallest unresolved implementation backlog produced. |
| GP-08 | planned | GP-07 | First highest-leverage slice selected from observed gaps (prefer restoring an existing capability). Owning repo, surfaces, authority, acceptance, rollback recorded. |
| GP-09 | planned | GP-08 | Slice implemented/tested in its owning subsystem; deployed only to its approved proving destination; positive/denial/retry/failure behaviors proven. |
| GP-10 | planned | GP-09 | Bounded end-to-end workflow through the real CoS/worker path including an ACITL consent moment; user-visible result + scoped receipt proven. |
| GP-11 | planned | GP-10 | Brownfield reproducibility: fresh build-out, partial adoption, rerun, interruption, rollback — no duplicates, no private-state import. |
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

- Every spine step: class, owning mechanism, law, scars, consent design, embedded check, exit — no undocumented manual prerequisite.
- Consent surface fixed at Stage 0; secret-entry is AC-driven-owner-typed; the agent never holds owner secrets; nonrenewable assets untouched.
- Fresh/partial/rerun/interrupted/recovery paths behave as specified on real brownfield machines.
- Function AND denial proven; no sovereign fallback; receipts attributable.
- The optimization loop runs on the deployed system (heartbeats visible, scars feeding back, doctrine versioning advancing).
- A replacement agent continues from durable references; no secrets or private client data in this doc.

## Findings and evidence limits (iteration 3)

- Operator directive (2026-09-10): all content must be **properly interwoven, not appended**; end state = a fully documented working process and system, continually optimizable and tracked. This iteration restructured the doc onto the spine accordingly.
- Locked invariants unchanged: zero human turns, ACITL, brownfield-first, starter essence (defaults/scars/checks/order), reuse-first.
- Still documentation-iteration only: no installer, live reconciliation, customer rollout, or end-to-end acceptance has occurred. GP-04 onward open.
- Tooling defects filed this week (not doctrine blockers): uiai-engine #224 (browser delivery), wirebot-core #31/#32, focusa #599/#600/#601.

Sources: operator as-built process, scars, and directives (2026-09-10); [0.1.0](0.1.0.md); [0.1.1](0.1.1.md); [server handoff](SERVER_AGENT_HANDOFF.md); starter verbatim reference (`https://burcs.dev/starter.md`).