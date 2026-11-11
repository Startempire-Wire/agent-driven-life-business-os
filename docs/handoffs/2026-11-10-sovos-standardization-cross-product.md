# Cross-product handoff — SOVOS standardized Wirebot operating model (2026-11-10)

**READ BEFORE CONTINUING MASTER LOOP, PORTABLE MEMORY, WIREBOT CORE OR WIREBOT APP ARCHITECTURE WORK.**

Canonical proposed standard: https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/spec/wirebot-standard-operating-model-20261110/docs/11-sovos-wirebot-standardized-operating-model.md
Review PR: https://github.com/Startempire-Wire/agent-driven-life-business-os/pull/37
Infrastructure evidence: https://github.com/Startempire-Wire/Wirebot-App/pull/23

This is a future-looking integration draft, not a claim of implemented runtime behavior and not a new execution grant. Continue independently authorized work now; do not wait for implementation defects from PR #23 to be repaired before aligning specifications. Domain-owning contracts retain authority over their primitives. Record conflicts against source/version, reconcile with the owning repository, and do not silently overwrite established designs.

## Architecture decisions to inherit

- SOVOS owns portable integration doctrine; no second identity, workspace, project, task, scheduler, memory, conversation, permission, receipt or outcome authority.
- Focusa Spec 162 and existing Rust remote workspace bindings own host-aware project identity; one operational Focusa daemon can bind remote project checkouts. Do not invent a Wirebot host/path registry or require daemon-per-server/multiplexing.
- Reference installation: OVH hosts OpenClaw, Wirebot App and agentic services; KnownHost hosts root Pi and the single operational Focusa daemon; Tailscale connects the hosts. Placement and transport are configuration; do not hardcode hostnames/paths as universal invariants.
- OpenClaw remains the persistent Operating Partner runtime. Wirebot App, Discord and future voice/device surfaces project the same owner/workspace/partner relationship. Wirebot Core and existing source owners retain tenant/runtime/conversation admission and governance.
- Focusa owns Workstream, Foreman, CRIST, Trajectory, Workpoint, Workset, CallGraph, Silent Sessions, governed execution, Evidence, receipts and recovery. A Foreman is a persistent Workstream role projection, not a permanently running process.
- Workforce Composer designs/commissions roles; Focusa Workforce operates active governed work. Draftees is public/network discovery; Flow Mesh is task projection, neither is private execution authority.
- Master Loop contracts 09/10 already specify nested composable loops, typed source-owned records, multi-node leases, tenant isolation and four version axes. Perpetua and proposed Master Observer/Wirebot Fusion Engine compose through existing sources and permissions; do not create competing loops or schedulers.
- Portable Memory is an approved replacement direction still being implemented; preserve Mem0 and other currently owned providers until parity, migration and rollback qualify cutover. Preserve source-domain truth and role-scoped access.
- Dedicated full-Sovereign and managed-isolated profiles are distinct. App development continues through the existing task catalogue and code → authorized dev hot-deploy → changed-path verification cycle.

## Required agent action

1. Read canonical SOVOS PR #37 and the existing domain-owned specs/code relevant to your assignment; reconcile rather than re-specify.
2. Identify affected interfaces, exact existing contract/schema references, implementation maturity, and any contradiction with the proposed SOVOS draft.
3. Update your existing task/Workpoint or PR with source-linked alignment notes and a minimal owner-specific implementation sequence. Do not create a parallel tracker.
4. Preserve ongoing work, branch boundaries and existing grants. Implement independently ready slices without treating future architecture or unrelated defects as gates.
5. Report which decisions were inherited, which source conflicts remain, and the exact responsible repository for each unresolved seam. Do not claim acceptance from documentation or a passing health check.

## Cross-repo ownership assignments

- **SOVOS/Master Loop agents:** reconcile Contracts 09/10, nested loop composition, Perpetua, Observer, WFE, portable installation, reference profiles and evidence/acceptance.
- **Portable Memory agents:** reconcile approved Portable Memory reference profile, Mem0/Letta/current bridges, tenant/role projections, lifecycle/correction/forgetting, migration and rollback; do not cut over based on this handoff.
- **Wirebot Core agents:** reconcile persistent OpenClaw partner/tenant LBI, conversation continuity, owner scope, memory adapter, source-owned routine projections, delegation and runtime readiness.
- **Wirebot App agents:** reconcile selected workspace, Core runtime projection, Discord continuity, GUI/workforce presentation, generated UI, and owner dogfooding through the existing App task catalogue and PR #23 evidence.

**Completion:** leave a source-grounded status update on your existing task/PR and link the SOVOS canonical draft. This handoff itself authorizes no production cutover or cross-repository code changes.
