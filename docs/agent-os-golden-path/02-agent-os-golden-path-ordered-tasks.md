# Golden Path — ordered implementation and iteration tasks

- Date: 2026-09-10
- Goal: an authorized replacement agent can set up, adopt, repair and operate our Life & Business OS end to end, without the original builder's memory.
- Starting point: upstream `3658ecc` and the [server handoff](SERVER_AGENT_HANDOFF.md).
- Current candidate: [0.1.1](0.1.1.md), incorporating the unchanged [0.1.0 phase definitions](0.1.0.md).
- Current acceptance: documentation review only; no installer, customer rollout or full-system acceptance is claimed.

## One task list, not another control plane

This is the single ordered project-local list for this assignment. Initial inspection found no project-local Beads database and no open upstream issues representing it. Do not use the parent directory's task database. Reuse these IDs when admitting executable work to the existing task/CallGraph system; link that record here rather than maintaining a second execution ledger. Runtime receipts remain with their canonical owners.

`ready` means dependencies are satisfied, not permission to mutate infrastructure. The current requested pass is draft iteration and planning. Operational changes need their exact repository/environment, capability, acceptance and rollback resolved before execution. An upstream suggestion is not an installation, credential, purchase or production-deployment grant.

## Ordered tasks

| ID | Status | Depends on | Task and done-condition |
|---|---|---|---|
| GP-01 | done | — | Pull upstream without overwriting local work; read the candidate, root guide and handoff; locate an existing task owner. Evidence: clean fast-forward to `3658ecc`; four new docs; no matching open issues or project-local task database. |
| GP-02 | done | GP-01 | Compare the starter method; publish this list and the first clarification candidate with explicit limits. Done means lineage preserved, links checked and review findings recorded—not deployed behavior. |
| GP-03 | ready | GP-02 | Establish the exact reference-owner setup profile and input/acceptance matrix. Inspect canonical owner, Agent Computer and provisioning contracts; distinguish new setup, existing adoption, repair and upgrade. List required inputs, their source, validation, permissible defaults and irreducible human actions. Resolve conflicting instructions and source/mirror drift without overwriting concurrent policy changes. |
| GP-04 | planned | GP-03 | Reconcile the live estate through approved read-only routes. For each subsystem record source-stated, implemented, configured, reachable, usable by the intended agent, and behaviorally verified separately, with scoped evidence/freshness. Consult existing Wirebot access/operability work before creating any replacement tasks. Private deployment details stay in Agent-KB/runtime evidence. |
| GP-05 | planned | GP-04 | Map material state ownership: domain, scope, canonical owner, writers/readers, store role, consistency, freshness, backup and recovery. Reuse the handoff taxonomy. Every ambiguity has a named resolution owner; do not introduce a synchronization database. |
| GP-06 | planned | GP-05 | Bind all fourteen phases to actual existing operations, inputs, dependencies, checks, failure handling and recovery. Every applicable phase has a verified binding or an explicit gap; no invented command names. Resolve first-install/bootstrap prerequisites without circular dependency on an uninstalled control plane. |
| GP-07 | planned | GP-06 | Review the executable design against normal, partial, denied and interrupted runs. Reuse the existing task/CallGraph executor and validate its dependency graph. Confirm no second capability registry, task store, universal installer or memory layer is needed. Produce the smallest unresolved implementation backlog. |
| GP-08 | planned | GP-07 | Select the first highest-leverage slice from observed gaps. Prefer restoration/reuse of an existing capability over a new aggregate dashboard. Record owning repo, exact changed surfaces, execution/deployment authority, consumer acceptance and material rollback. Do not preselect a new manifest or service merely because the handoff mentions one. |
| GP-09 | planned | GP-08 | Implement and test that slice in the owning subsystem, then deploy only to its approved proving destination. Demonstrate positive authorized operation, relevant denial behavior, retry safety and observable failure. A source commit alone leaves this task open. |
| GP-10 | planned | GP-09 | Run a bounded reference-owner end-to-end workflow through the actual Chief-of-Staff/worker tool path. Demonstrate a useful user-visible result plus the underlying scoped receipt. Shell reachability or direct administrator access is insufficient proof of agent usability. Publish the first evidence-grounded milestone version (normally `0.2.0`) with its limited scope; do not wait for every profile. |
| GP-11 | planned | GP-10 | Prove reproducibility: authorized fresh setup, adoption of partial state, unchanged rerun, interruption/restart and rollback/forward repair. Verify no duplicate resources, private-state import or hidden manual repair; exercise backup restoration where material. |
| GP-12 | planned | GP-11 | Repeat the relevant path in an explicitly authorized isolated client profile with synthetic principals. Verify authorized functionality AND cross-tenant denial, independent owner binding, revocation and no sovereign fallback. No real customer mutation solely to obtain proof. |
| GP-13 | planned | GP-12 | Have a replacement agent run from documented entry points and durable state without original-session memory. Reconcile every acceptance row, unresolved gap and consumer evidence reference. Publish the next appropriate version and an honest handoff; do not promote unknown/blocked rows to complete. |

The order is dependency-driven. Independent inspection may run in parallel after scope is established; completing an unrelated easy row must not displace a ready acceptance-critical action. New findings amend this list rather than spawn parallel plans.

## GP-03/06 implementation-map starting points

These are source-stated candidate owners to inspect, **not claims of installed capability or final execution order**. The actual bindings and private endpoints belong in their owning operational references.

| Phase | Candidate owning surface(s) | Required binding/proof before acceptance |
|---|---|---|
| 0 Identity/profile | Owner constitution; existing deployment identity and Focusa project identity | Correct owner, deployment, profile, scope and action grant; no inferred tenant identity. |
| 1 Baseline | Existing provisioning and Agent Computer lifecycle | Inspect-before-create; exact source/state/config owners; clean and partial setup behavior. |
| 2 State | Agent-KB, Focusa, Context Core, memory, business systems and provisioning owners | One owner per fact class/scope, with reader/writer and recovery map. |
| 3 Freshness | Each canonical writer and its consumers | Changed state becomes visible within its documented tolerance; unknown is not empty. |
| 4 Identity/session | Existing gateway, login, tenant and credential authorities | Intended principal works; foreign/unknown principal fails; revocation works. |
| 5 Agent execution | Wirebot/OpenClaw; Focusa; worker harness; UIAI/Veragensia | Actual registered tools, bounded real action and restart/worker-replacement continuity. |
| 6 Routing | Existing private networking, edge and service owners | Correct backend from the agent's network position; private controls remain private. |
| 7 Knowledge | Agent-KB and subsystem documentation | Fresh authenticated orientation; explicit degraded recovery and instruction refresh. |
| 8 Discovery | Existing Focusa, UIAI, CLI/API/MCP catalogs | Discover schema and invoke the narrowest authorized operation without guessing. |
| 9 Evidence/cost | Existing Focusa/UIAI/WINS and service observability | Request through user-visible result, attributable cost and durable receipt. |
| 10 Controls | Credential authority, secret injection and budget owners | Renewable authorization, scoped exposure, cancellation/limits and revocation before dependent action. |
| 11 Entitlement | Existing licensing and commercial provisioning | Installed-system licenses resolved; commercial lifecycle only where the selected profile requires it. |
| 12 Delivery | Owning subsystem's canonical release/install/repair mechanism | Known installed revision, consumer compatibility, bounded rollout and recovery. |
| 13 Acceptance | Intended human surface plus replacement agent | Useful outcome, repeatability, evidence and maintainable handoff—not just green components. |

Reference-specific invariants: KnownHost remains the current reference Focusa authority; remote compute/display must not create another reference writer. Client installations resolve their own owner and authority. Full owner capability and member isolation are complementary tests, not excuses for blanket restrictions. Client replication follows demonstrated reference-owner usefulness.

## Iteration protocol

For each pass: identify the dominant open requirement → inspect its owning source → propose the smallest correction → review against actual behavior → update the candidate and this list → proceed to the next ready item. Record assumptions and source limits at the affected claim. Ask only for choices that materially affect owner authority, scope, consent, cost, data safety or destination.

Preserve superseded snapshots. A clarification-only candidate is not the handoff's promised implementation milestone. Do not label the draft "perfect": use these completion criteria instead:

- Every applicable phase has explicit inputs, dependencies, an existing execution binding and a consumer check; no undocumented manual prerequisite.
- Optional phases have a profile-backed reason; missing mandatory capabilities are blocked/unknown, never silently skipped.
- Fresh, partial, rerun, interrupted and recovery paths behave as specified.
- Both authorized functionality and unauthorized-scope denial are proven.
- No secret/customer payload is exported; receipts and resource costs are attributable.
- One real owner workflow works through the intended agent and human surfaces.
- A replacement agent can reproduce and maintain the result from durable references.
- Unresolved mandatory requirements prevent acceptance; optional limitations are explicit.

## First review findings and evidence limits

- `0.1.0` already has valuable phase purposes/checks/recovery guidance, but portable implementation directions are not executable bindings.
- Phase numbering can mislead a literal executor into treating auth, secrets, budgets and observability as late additions. The clarification makes them prerequisites of dependent actions.
- The source starter is app/Cloudflare-specific. Reuse its explicit checks and gotchas, not its purchases, stack, public CORS, telemetry or alert thresholds for private systems.
- Existing instruction-loader work demonstrates why updated files, refreshed context and usable native tools require separate verification. The current source/mirror revision mismatch needs reconciliation in GP-03, not an automatic overwrite.
- No live all-system inventory, customer setup or end-to-end acceptance was performed in this documentation pass. GP-04 onward remains open.

Sources: [starter reference](https://burcs.dev/starter), fetched 2026-09-10; [0.1.0](0.1.0.md); [server handoff](SERVER_AGENT_HANDOFF.md); [foundational contract](../../AGENTS.md); [Agent Computer profile](../../AGENT_COMPUTER_REFERENCE_PROFILE.md). Detailed runtime evidence remains in the existing scoped evidence/knowledge surfaces.
