# SOVOS — Standardized Wirebot Operating Model and Deployment Contract
**Status:** Proposed canonical integration standard, review draft 1.0 (2026-11-10)  
**Authority:** Canonical Owner Principal, subject to OWNER_AUTHORITY_CONSTITUTION.md  
**Scope:** SOVOS/Wirebot ecosystem; architecture specification, not live-runtime certification.

## 1. Decision and normative precedence
Wirebot installations share **one portable logical operating model** while retaining product-owned authoritative state, existing physical repositories and configurable execution placement. SOVOS owns portable integration law, not a new database, scheduler, permission service or runtime. Existing domain-owned contracts remain authoritative for their respective primitives. Conflicts must be logged and resolved with those owners; this document does not silently supersede them.

Normative dependencies: [Current Ecosystem Architecture](../../CURRENT_ECOSYSTEM_ARCHITECTURE.md), [Cross-Product Seam Contract](../../CROSS_PRODUCT_SEAM_CONTRACT.md), [Owner Authority Constitution](../../OWNER_AUTHORITY_CONSTITUTION.md), [Golden Path](agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md), [Master Loop 09](09-sovos-master-loop-composable-provenance-and-agent-first-contract.md), [Master Loop 10](10-sovos-master-loop-distribution-portability-and-extension-contract.md), [Portable Memory Reference Profile](../../PORTABLE_MEMORY_REFERENCE_PROFILE.md), [Focusa Spec 162](https://github.com/Startempire-Wire/focusa/blob/main/docs/162-remote-workspace-binding-design.md), [Focusa Spec 182](https://github.com/Startempire-Wire/focusa/blob/main/docs/182-focusa-project-foreman-workstream-intelligence-projection-spec.md), [Wirebot App workspace contract](https://github.com/Startempire-Wire/Wirebot-App/blob/main/docs/17-wirebot-workspace-selection-and-membership-contract.md), [Wirebot App current-to-target handoff](https://github.com/Startempire-Wire/Wirebot-App/blob/main/docs/21-wirebot-current-state-to-target-state-handoff.md), [Wirebot App delivery policy](https://github.com/Startempire-Wire/Wirebot-App/blob/main/docs/15-wirebot-algorithm-continuous-delivery.md), and [App PR #23 evidence](https://github.com/Startempire-Wire/Wirebot-App/pull/23).

## 2. Portable logical workspace
Every installation exposes logical Inbox, Life, Businesses, Projects, Assets, Knowledge, Routines, Results and Archive categories. They are navigational views, **not required physical directories**. The initializer MAY create empty directories idempotently, but MUST NOT move existing repos, claim existing resources or manufacture authoritative records. Logical entries contain source-owned typed references, with owner/environment scope, revision/freshness and provenance; resolution and mutation use the owning service. No new workspace registry is authorized by this spec.

App workspace selection remains explicit and tenant-scoped under App Doc 17. Switching workspace fences pending private actions. Workspace membership, offer level, runtime readiness and owner-rooted authority are separate axes.

## 3. Project identity and remote binding
**Focusa is canonical** for project identity, Workstream, Trajectory, Workpoint, authority, Evidence and Receipts. Adopt `focusa.remote_workspace_binding.v1` (Spec 162) with controller identity, project/repository identity, SSH/remote transport, host and remote roots, continuity principal, freshness and revocation. Never infer source identity from an equal path string on two hosts. Remote working hosts need not host another Focusa daemon. The current code implements core binding types, SQLite persistence and API routes; transport probes and writer-lease integration are not assumed accepted until proven. Root/SSH/Tailscale access does not grant mutation authority.

## 4. Operating Partner and interfaces
Canonical Owner Principal and durable Operating Partner Principal survive model, process, channel, host and device changes. OpenClaw is the operating-partner orchestration substrate; Wirebot Core owns applicable conversation/runtime contracts. Wirebot App becomes the primary GUI, while Discord remains first-class and voice/Android/Echo interfaces remain additional projections. All channels resolve the same owner/workspace/partner and source-owned conversation and work references. App consumes `wirebot.openclaw_runtime.v1`; no shared operator fallback, second partner identity, second conversation authority or silent cross-tenant continuation. Veragensia owns bodies/placement; UIAI owns browser/computer execution and proof.

## 5. Workforce and execution
Wirebot Workforce Composer designs and proposes roles; Focusa owns governed assignments and Workpoints; Focusa Workforce owns active operations; Flow Mesh projects task state without owning it; Draftees provides optional network hiring/discovery, not execution authority. Reuse the [Composable Workforce Catalogue](agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md): flash, session, campaign, staff-profile and scheduled forms, with CRIST Context, Role, Interview, Spec and Tasks. A role profile is not a live process, schedule or grant. Focusa Spec 182 defines one default persistent Foreman role projection per Workstream Root, independent of Pi/model/session. Pi and compatible workers execute bounded work; Silent Sessions are not schedulers. Work operations preserve scoped intent, authorization, project/Workpoint, performer, progress, evidence, independent verification and accepted outcome.

## 6. Master Loop, Observer, Perpetua and Fusion
Master Loop is one coordinating composition of nested loops, not a monolithic scheduler. Inherit Contracts 09/10: typed component interfaces, source-owned state, explicit tenant scope, negotiated versions, leases for distributed schedules, replay/idempotency, evidence and independent outcome verification. Master Observer is an observing/improvement role within this existing architecture, not a new authority. Perpetua uses existing scheduling ownership. Wirebot Fusion Engine (WFE) is a **proposed compositional skill/operating-procedure layer** over OpenClaw skills, Focusa CRIST/CallGraphs/Workpoints, UIAI, Portable Memory and Master Loop; it may register reusable skill definitions and request governed execution, but cannot mint permissions or add another scheduler/task store. Detailed WFE/Observer contracts remain owner-repository reconciliation items, not invented implemented interfaces.

## 7. Portable Memory
Inherit `agent.memory_contract.v1` reference profile and approved replacement direction. Capture, authorized recall, correction, forgetting, provenance, bounded context, migration and recovery remain source-governed. Mem0, Letta and existing Wirebot services may remain operational during qualification; retirement requires parity, migration, rollback and separately authorized cutover. No new memory-specific login, second memory authority or fabricated cross-channel recall.

## 8. Deployment profiles and reference topology
**Full-Sovereign dedicated** retains `operator.environment.v1`: owner-specific persistent VPS, owner private Tailscale mesh, at least one owner-controlled local body, durable partner and isolation. OVH is a reference provider, not hardcoded. **Managed** uses operator-hosted isolated workloads with separately verified tenancy, credentials, memory, persistence and lifecycle; it is not full-Sovereign certification. **Local/Mac** is a portable alternative subject to OS-user/credential isolation and offer-specific eligibility; a shared macOS account is not automatically a sovereign boundary. **Hybrid** binds remote execution locations through existing owners without splitting identity.

PR #23 observed: OVH runs OpenClaw, App and other agentic services; KnownHost runs root Pi and the single operational Focusa daemon; OVH-to-KH Focusa HTTP reads traverse Tailscale. The additional Pi-side daemon and multiplexing are not operational assumptions. Tailscale ACL/grants and complete agent dispatch remain to be qualified.

## 9. Initialization, migration, recovery
Inherit the existing Golden Path stages: owner binding; workstation; partner genesis; VPS; mesh; discovery; administration; workforce commissioning; ongoing operation. Brownfield-first, idempotent, non-destructive, platform-adapted installation. Detect installed versus reachable versus healthy versus entitled versus authorized versus verified. Preserve owner/partner identity, existing files, source refs, memory provenance and Workpoint history during migrations. Declare backup, restore, version compatibility, host placement, isolation, offline/degraded behavior and rollback per profile. No daemon-per-host mandate.

## 10. Dogfooding and continuous improvement
The owner reference environment is `dev.wirebot.chat`. First acceptance journey: authenticated owner → selected workspace and existing Operating Partner → bounded documentation development assignment → Focusa/Pi execution and scoped progress → evidence and independent verification → reload continuity → Discord continuity. Preserve existing App tasks Q00.03/Q00.04 and Core dependencies, and current Focusa work. Development agents may cover frontend, backend, middleware, product and QA as episodic governed roles. Follow App Doc 15: implement bounded change → authorized dev hot-deploy → verify changed user path → continue. Do not create a parallel task catalogue or browser runner. Full 40-page/seven-journey acceptance remains separate.

## 11. Traceability and conflict dispositions
| Evidence | Decision | Owner | Acceptance / unresolved |
|---|---|---|---|
| SOVOS ecosystem + seam contracts | One source owner per concern, typed cross-product refs | SOVOS/product owners | No duplicate state/authority |
| Focusa 162 + Rust core/API | Reuse remote binding; host-aware identity | Focusa | Verify transport/lease slices |
| App Doc 17 | Explicit selected workspace and fencing | Wirebot App/Core | Cross-tenant tests |
| PR #23 OVH/KH mismatch | Same path is not same checkout | Focusa/App | Resolve host-aware binding |
| PR #23 workpoint GET 405 | API/schema and trajectory mismatch is implementation defect | Focusa | Correct endpoint/contract proof |
| PR #23 guest UI | No authenticated owner acceptance | Core/App/UIAI | Owner journey |
| Workforce catalogue + Focusa 182 | Persistent role ≠ persistent process | Focusa/Wirebot | Delegation and evidence |
| Master Loop 09/10 | Reuse composition/lease/version mechanisms | SOVOS/owning services | Distributed qualification |
| Portable Memory profile | Replacement with controlled migration | Memory owners | Parity and rollback |
| App Doc 15 | Bounded delivery; no whole-product gate | App | Changed-path proof |
| App family architecture | Composer vs live Workforce vs Draftees | Wirebot/Focusa/Network | Source-owned handoffs |

## 12. Conformance and next implementation handoffs
Architecture conformance is distinct from runtime acceptance. A profile must prove owner/tenant isolation, source-owned identity, correct project/remote binding, explicit grants, safe failure/recovery, portable references and truthful capability states. An unavailable optional feature must not masquerade as accepted.

Existing owner repositories should receive implementation tasks for (a) Focusa remote binding/Workpoint API and Pi admission, (b) Core owner-bound conversation, (c) App dogfood journey and continuous development, (d) memory migration, (e) Master Loop distributed capability, and (f) WFE/Observer detailed contract reconciliation. PR #23 remains the read-only evidence baseline, not an implementation merge. This standard does not itself authorize production changes, credential mutations, new spend or cross-repository writes.
