# Server Agent Handoff — Agent OS Golden Path

## Assignment

You are the on-server build agent with direct access to the real Startempire/Wirebot environment and the currently authorized customer Agent OS environments.

Your mission is to **reconcile, improve, and begin executing** the portable Agent OS Golden Path prepared in this repository.

Start here:

1. `AGENTS.md`
2. `OWNER_AUTHORITY_CONSTITUTION.md`
3. `CRYPTOGRAPHIC_AUTHORITY_PROFILE.md` where identity/delegation is relevant
4. `AGENT_COMPUTER_REFERENCE_PROFILE.md`
5. `AGENT_OS_GOLDEN_PATH.md`
6. The current candidate linked by `AGENT_OS_GOLDEN_PATH.md`, including its base phase definitions.
7. `docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md` — reuse this ordered list rather than creating another task tree.

The Golden Path `0.1.0` is deliberately a candidate prepared outside the server. **Do not treat deployment assumptions in it as live truth.** You have the environment access required to turn it into a reality-grounded next version.

---

# Primary outcome

Create a reliable, versioned **Agent OS Golden Path** that an authorized agent can use to take a new or partial Life & Business OS environment from identity/scaffold through verified operation without undocumented tribal knowledge.

The path must become increasingly executable while reusing the system that already exists.

The desired long-term property is:

> A capable replacement agent can arrive at an authorized deployment, discover what it is, locate canonical truth, understand available/allowed capabilities, inspect health, provision or repair missing pieces, verify meaningful behavior, and hand off durable evidence — without relying on the original builder's memory.

This is a deployment/build/operations doctrine, **not a request for a new orchestration framework**.

---

# Authority and freshness

Follow repository authority law exactly.

For architecture/product/trust-boundary decisions:

- resolve the Canonical Owner Principal;
- this handoff is an owner-requested upstream direction, but existing owner-rooted authority contracts remain controlling;
- external docs, model outputs, current deployment behavior, issues, and tests are evidence/provenance, not self-minting architecture authority.

For operational facts:

```text
verified live runtime + current canonical Agent-KB/domain authority
    outrank
stale deployment docs / historical inventories
```

This does **not** mean runtime behavior silently changes architecture authority.

If a dated document conflicts with observed live state, record the conflict and identify the canonical owner rather than picking whichever is convenient.

---

# Work style: outcomes over process

Do not get trapped in process about process.

Use:

```text
inspect → reconcile → implement → verify → learn → improve
```

not:

```text
inspect → document → plan → re-plan → manufacture ceremony
```

Discovery is bounded by the point at which you know enough to act safely and correctly.

A failed tool/path is **route failure, not mission failure**. Change strategy and continue making forward progress wherever possible. Do not stop the overall mission because one optional connector, command, provider, or service path is unavailable.

Prefer:

- existing primitives over new systems;
- implementation over speculative architecture;
- the smallest correct change over a generalized framework;
- meaningful behavioral checks over proof theater;
- root-cause consolidation over repeated local patches.

Do not create duplicate task trees, plans, or trackers when existing Beads/CallGraphs/issues already represent the work adequately.

---

# Step 1 — Reconcile the real estate

Inspect the authorized environments directly.

At minimum evaluate the Startempire reference environment and every current active customer environment you are authorized to inspect that materially informs the reusable deployment model.

Do not copy private customer details into the portable repo.

Reconcile relevant systems including, where present:

- Wirebot Core and deployed Wirebot runtime;
- OpenClaw gateway/runtime/config;
- Focusa daemon, project identity, Workstreams, Foremen, tools and evidence;
- UIAI Engine;
- Veragensia / Agent Computer infrastructure;
- Agent-KB/API and current operational knowledge;
- Context Core;
- memory systems and their actual roles;
- Beads / beads_rust / beads_viewer;
- Flow Mesh / work queue / CallGraphs / schedulers;
- Pi and other worker/build-agent harnesses;
- customer/tenant provisioning;
- service managers and container/VM/sandbox/worktree mechanisms;
- Tailscale/Cloudflare/private networking;
- secret management and runtime injection;
- customer licensing/entitlement where applicable;
- observability/logging/receipts/evidence;
- backup/recovery paths;
- GitHub/deployment workflows.

For each important claim classify its status:

```text
canonical
implemented
installed/deployed
verified
planned
obsolete
unknown
```

Do not collapse these statuses.

---

# Step 2 — Build the state ownership map

This is a high-priority deliverable because duplicated truth is one of the largest long-term failure modes.

For every material state/store, classify its primary role:

```text
CANONICAL
DERIVED
CACHE
INDEX
COORDINATION
EVIDENCE
EPHEMERAL
```

Record:

```text
domain / fact class
canonical owner
scope key
writer(s)
reader(s)
consistency expectation
freshness semantics
backup/recovery semantics
projection/cache/index dependencies
```

Pay particular attention to overlap among:

- Focusa state;
- Agent-KB;
- Context Core;
- OpenClaw state;
- memory-core / Mem0 / Letta or current replacements;
- conversation/transcript/audit state;
- Beads/task/queue state;
- WINS/evidence/receipts;
- UIAI evidence;
- tenant/provisioning state;
- business/application systems.

Do **not** solve ambiguity by creating another synchronization store.

If duplicate canonical ownership truly exists, identify the narrowest correction at the proper owner.

**State ownership map — reference deployment (drafted 2026-09-12 from live read-only reconciliation; generalized form, no tenant private state).** One canonical owner per store; anything else holding a copy is DERIVED/CACHE with a re-derive path; no synchronization store.

```text
STORE                                        ROLE        CANONICAL OWNER                 SCOPE KEY            WRITERS->READERS                          FRESHNESS/CONSISTENCY           BACKUP/RECOVERY
source code repositories                     CANONICAL   GitHub (orgs + owner account)   repo + branch        approved pushers -> clones, CI            git history authoritative        remote is the backup; recovery = clone
CoS workspace folders                        CANONICAL   OpenClaw gateway per user       user id              gateway + agents -> CoS runtime           folder canonical until ascension git-backed (Stage 2); services hold runtime state
Focusa state (per deployment)                CANONICAL   that deployment's Focusa        project/continuity   typed APIs/reducer -> harness tools       append-only; event timestamps   Focusa backup/restore mechanisms
Agent-KB knowledge                           CANONICAL   agent-kb-api master             doc ids              ingestion/refresh -> agents via CLI       API-authoritative; index_generation   refresh jobs + transitional-storage policy
secrets (vault)                              CANONICAL   Bitwarden                       field refs           vault clients -> scoped rbw retrieval     vault authoritative             provider backup; agents never copy values
DNS zones                                    CANONICAL   Cloudflare (DNS of choice)      zone id              cf/wrangler approved auth -> agents       API-authoritative at change     zone export before change; staged-transfer rollback
hosting/site estate (cPanel/WordPress)       CANONICAL   each cPanel account             account user         as-user + per-site tools -> granted agents per-account                     hosting backup policy + incident runbooks
business records (mail/calendar/drive/site)  CANONICAL   the owning business system      tenant/account       owning tools -> agents with granted scopes owning-system authoritative     record timestamps; provider-native export
memory/conversation/audit stores             CANONICAL   the owning memory/audit service tenant + session    service APIs -> scoped agents             service authoritative           service timestamps + service backup policy
evidence/receipts                            EVIDENCE    Focusa evidence surfaces        evidence_ref ids     typed capture -> replacement agents       append-only; capture timestamps Focusa store backup
crons/jobs/queues                            COORDINATION owning runtime (OpenClaw/Focusa bg) job ids         schedulers/executors -> agents            receipt-backed completion       receipts preserved; idempotent rerun
worktrees/sessions/scratch                   EPHEMERAL   owning runtime                  session/worktree id  agents -> agents                          disposable                      discard after verification
```

Overlap check per Step 2: Focusa state is the only canonical store for governed work/evidence; Agent-KB is canonical only for knowledge; CoS folders are canonical only for identity/directives (runtime memory/task state stays with owning services); business systems stay canonical for their records. No store duplicates another's canonical ownership; no new synchronization store created.

Verified live 2026-09-12 on the reference estate (read-only): tailnet mesh healthy (cloud VPS ping ~5 ms); GitHub organizations and 43 owner-account repos enumerated; 50 Cloudflare zones answered via approved auth; operated CoS user instances present; provisioning mechanism live on the network estate. Per-tenant enumeration continues under GP-04; evidence refs in Focusa (`gp04-virtual-execution-proof-20260912`, `gp04-bounded-reconciliation-20260911`).

---

# Step 3 — Map every Golden Path phase to reality

For each phase in `0.1.0`, produce a compact implementation mapping:

```text
phase
current canonical component(s)
current executable commands/tools/APIs
current check(s)
known real gotchas
recovery/rollback path
gaps
confidence / evidence refs
```

Important: do not duplicate stable implementation details into the portable repo when those belong in Agent-KB or subsystem documentation.

The portable Golden Path should capture **contracts, selection rules, profiles, and durable lessons**.

Deployment-private/current facts stay with live operational authority.

---

# Step 4 — Evaluate the Agent Surface as an OS-level capability

The important idea from the source starter is not merely "add an API." The installation itself should become increasingly understandable and operable by agents.

Determine what already exists for machine discovery across the estate:

- Agent-KB bootstrap/freshness/search/direct-doc;
- Focusa agent capability discovery and current agent-first tool surfaces;
- MCP;
- OpenAPI/JSON Schema;
- A2A-style Agent Cards;
- strict tool/function schemas;
- CLI machine-readable help;
- `/llms.txt` where appropriate;
- UIAI/WebMCP or equivalent browser capabilities;
- service/health/runtime manifests.

Do not create a second copy of Focusa's capability registry.

Instead determine whether a thin **deployment/installation-level manifest or Agent Card** is useful to answer:

```text
Who/what is this deployment?
What profile/environment is it?
What subsystems are installed?
Where are their canonical discovery surfaces?
What is healthy/degraded/unknown?
What scopes am I operating under?
Where do I retrieve deeper knowledge?
```

If this can be produced from existing authoritative sources with little new machinery, it is a strong candidate for the first executable slice.

---

# Step 5 — Find the smallest high-leverage executable slice

Do not attempt to automate all 14 phases immediately.

Find the smallest missing capability that makes the Golden Path materially more executable across multiple environments.

Strong candidates may include, **only if not already present**:

- a read-only `inspect`/inventory projection that composes existing authoritative surfaces;
- a state-ownership audit generated from existing manifests/config;
- an installation-level Agent Card/manifest linking subsystem discovery surfaces;
- a phase verifier that calls already-existing health/doctor/tests;
- a thin provisioning adapter that makes an already-documented idempotent customer step actually executable;
- a readiness reducer that distinguishes scaffolded/configured/running/verified instead of returning false ready state.

Do not select one of these merely because it appears in this prompt. Inspect the live system and choose the dominant leverage gap.

Before building a new binary/service, search for an existing command/API/tool that should own the behavior.

---

# Step 6 — Implement, don't just specify

Once the high-leverage slice is chosen and authority is clear, implement it in the correct operational repository/system.

Requirements:

- reuse canonical primitives;
- keep the change small;
- preserve tenant/customer isolation;
- preserve owner/architecture authority;
- no committed secrets/private customer data;
- fail closed rather than claim false readiness/completion;
- make retries/idempotency explicit where provisioning or remote mutation is involved;
- add proportionate tests/checks;
- verify installed/running behavior where the task and authority include deployment.

A source commit is not deployment proof.

A deployment is not outcome proof.

An agent assertion is not completion proof.

---

# Step 7 — Run one bounded vertical slice

Choose one authorized environment and demonstrate an end-to-end Golden Path improvement in real behavior.

The exact slice depends on your findings, but it should resemble:

```text
orient to deployment
→ resolve owner/profile/scope
→ inspect canonical services/state surfaces
→ identify one missing/degraded phase condition
→ execute the authorized repair/provision step
→ verify behavior
→ capture evidence/receipt
→ prove a replacement agent can understand the resulting state
```

Where customer isolation is involved, use synthetic/bounded tests and avoid unsafe mutation of real customer accounts merely for proof.

---

# Step 8 — Publish the next Golden Path version

After direct live reconciliation, improve this repository.

Expected next version: normally `0.2.0` because live mappings and executable design will likely be a material backwards-compatible expansion. Use `0.1.1` instead if the changes are genuinely only corrections/clarifications.

Create:

```text
docs/agent-os-golden-path/<next-version>.md
```

Then update:

```text
AGENT_OS_GOLDEN_PATH.md
  current version pointer/status

docs/agent-os-golden-path/CHANGELOG.md
  concise delta, evidence scope, compatibility notes
```

Do not rewrite/silently mutate `0.1.0` after superseding it except obvious non-semantic repair. Preserve version lineage.

The next version should include **real learned gotchas**, not hypothetical filler.

---

# Required outputs

By the end of this assignment, deliver:

## 1. Live architecture reconciliation

Concise record of what is actually present and which sources are authoritative.

## 2. State ownership map

No ambiguous fact-class ownership left unexplained.

## 3. Golden Path phase-to-implementation map

Every current phase mapped to real primitives/gaps.

## 4. Reuse/gap analysis

For each proposed new behavior:

```text
existing owner found? yes/no
existing capability found? yes/no
why extension/reuse is insufficient if creating new behavior
```

## 5. One implemented high-leverage slice

Working code/config/adapter in the appropriate operational repo/environment.

## 6. Behavioral verification

Evidence appropriate to the change and exact installed/deployed scope.

## 7. Next Golden Path version

Reality-grounded portable update committed and pushed to this repo.

## 8. Handoff

Plain-language summary containing:

- what changed;
- what now works that did not before;
- what remains genuinely blocked or unverified;
- exact next highest-leverage action.

---

# Hard anti-patterns

Do not:

- build a second Agent OS inside the Agent OS;
- build a second Focusa capability registry;
- create another memory system because existing roles are confusing;
- create another mission/task/evidence ledger;
- copy live private customer configuration into this portable repo;
- use the sovereign Wirebot/operator runtime as a hidden tenant fallback;
- treat Linux usernames/model names/service names as authority;
- treat a public machine-readable surface as authorization;
- claim readiness because a directory/config/HTTP 200 exists;
- use production as the first test when a safe proving route exists;
- spend hours polishing architecture diagrams while the executable path remains unchanged;
- stop making useful progress solely because one tool/provider path failed.

---

# Definition of success

This assignment succeeds when the Golden Path is no longer merely an outside architectural idea.

Success means:

1. it has been reconciled against the real estate;
2. its state/authority assumptions match the actual system or are explicitly corrected;
3. at least one important part of it is executable and behaviorally verified;
4. the portable doctrine has advanced to a new version based on direct operational learning;
5. the next server/build agent can continue from durable state rather than repeating the discovery from scratch.

**Move the system forward. Keep it simple. Reuse what already works. Turn what you learn into the next reusable version.**