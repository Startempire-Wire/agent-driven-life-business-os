# Agent OS Golden Path — Current Seam and Autonomy Gap Audit

**Status:** CURRENT architecture-gap audit  
**Reconciled:** 2026-09-15, semantic-integrity pass 2 complete  
**Architecture owner:** `CURRENT_ECOSYSTEM_ARCHITECTURE.md`  
**Purpose:** track missing cross-product seams that prevent the current Life & Business OS architecture from operating as one coherent system.

This document replaces the older gap framing where product ownership or app identity has since been settled. It preserves still-valid gap IDs where useful so existing issues and historical references remain legible.

The dominant constraint is not missing product ideas. It is unfinished **joins between already-owned systems**.

```text
owner / delegated humans / partner
  -> governed assignment
  -> Workstream / Foreman
  -> worker/runtime execution
  -> evidence
  -> settlement
  -> accepted outcome
  -> learning / portable trust
```

No gap below authorizes a second task database, workforce database, approval store, entitlement service, federation authority, credential vault or evidence system.

---

## 1. Architecture now considered settled

The following are no longer open architecture questions:

- ADLBOS is the portable integration/deployment doctrine, not another runtime product;
- Wirebot App is the current owner-facing application-family repository;
- a customer may white-label the Operating Partner presentation while retaining the Wirebot implementation family;
- Operating Partner identity is distinct from optional AI architecture-authority delegation;
- delegated human operators are bounded operational principals, not additional owner roots;
- Focusa owns governed work/Workstream/Foreman/Workpoint/Evidence semantics;
- Wirebot Workforce Composer designs/commissions roles and assignments;
- Focusa Workforce operates the active governed workforce;
- UIAI owns browser/computer execution and takeover/proof;
- Veragensia owns Agent Computer/body/runtime/enforcement;
- W.I.N.S. owns accepted outcome/portfolio semantics;
- MeriFolio is portable identity/trust/standing, not local workforce authority;
- Startempire Wire federation is explicit and optional;
- one Operator's multiple daemons/bodies are a fleet/aggregation, not sovereign federation;
- Operator Deployment is an implementation/deployment offer mapped onto existing dimensions, not a new authority/runtime tier;
- capability support, entitlement, activation, authority and consent are distinct;
- raw long-lived secrets do not cross normal product handoffs;
- actionable shared projections require explicit compatibility/freshness/replay semantics;
- presenter acknowledgement of an attention item is not canonical source-domain resolution.

---

## 2. P0 — identity, ownership and account joins

### SAG-03 — cross-product identity/link/revoke

**Gap:** there is still no proven end-to-end link connecting the exact owner, Operating Partner, Wirebot tenant/workspace, Focusa environment/project, devices/bodies, optional Startempire account and Sovereign federation node with explicit unlink/revoke semantics.

**Required closure:** a versioned link envelope plus denial tests showing that linking identities does not merge authorities or private data.

### NEW-P0-01 — Operating Partner principal + presentation profile

**Gap:** the architecture now distinguishes durable Operating Partner identity from the customer-visible name, but no shared machine-readable `operator.partner_profile.v1` is implemented.

**Required closure:** stable partner ref, owner ref, implementation family, presentation profile, deployment ref, optional network presentation, rotation/rename semantics and consumer tests in Wirebot App.

### NEW-P0-02 — Operating Partner versus architecture-authority proof

**Gap:** documentation now separates these concepts, but runtime/account schemas can still accidentally treat a privileged Chief of Staff identity as architecture authority.

**Required closure:** explicit fields/contracts and negative tests proving that partner status alone never satisfies architecture-authority verification.

### NEW-P0-08 — delegated human principal + revocation proof

**Gap:** the constitution now defines `DelegatedHumanPrincipal`, but deployment/runtime identity schemas do not yet prove a bounded human operator can act without becoming owner/co-owner or inheriting architecture authority.

**Required closure:** `agent_os.human_delegation.v1` implementation or equivalent product-owned contract with exact principal, operations/resources, data/credential visibility, consequence limits, validity, re-delegation policy and revoke/audit proof.

---

## 3. P0 — workforce composition and governed assignment

### SAG-09 — workforce profile/task-pack schemas

**Gap:** employee profiles/task packs remain primarily documented concepts; there is no complete versioned profile, task-pack, employment/assignment packet, roster and lifecycle schema family shared across Wirebot/Focusa consumers.

**Required closure:** versioned schemas with validation/migration and exact domain ownership.

### SAG-10 — audit gap → proposed roster → CRIST → assignment compiler

**Gap:** the pipeline from observed business deficiency to an explainable proposed role/assignment is not executable end-to-end.

**Required closure:** preview-first compiler that creates a proposed assignment, shows rationale/prerequisites/conflicts, receives owner/governance acceptance and emits an immutable assignment receipt.

### SAG-14 — assignment → least-capability grants

**Gap:** role/task/autonomy intent is not yet deterministically compiled into exact tools, data scopes, credential requirements, budgets, consequence classes and confirmation rules.

**Required closure:** least-capability preview/commit path with denied-operation, expiry and revocation proof.

### NEW-P0-03 — Workforce Composer → Focusa binding → Workforce projection

**Gap:** the product boundary is settled, but the handoff is not yet one executable lifecycle.

**Required closure:** one accepted test where a Wirebot Workforce Composer assignment resolves through Focusa into a Workstream/Foreman/worker binding and appears in Focusa Workforce without duplicate roster/task authority.

---

## 4. P0 — Chief of Staff and Foreman handoff

### NEW-P0-04 — Operating Partner delegation contract

**Gap:** ADLBOS defines the semantic handoff but lacks a versioned machine contract for owner/partner → governed work.

**Required closure:** bounded delegation envelope carrying owner/partner refs, project/workstream target where known, desired outcome, constraints, context refs, budget/authority/acceptance refs and correlation ID. Focusa remains responsible for validating/resolving the Workstream, Foreman, Workpoint and execution plan.

### NEW-P0-12 — OpenClaw operating-partner continuity

**Gap:** The shared OpenClaw gateway and private KnownHost Core → OVH route are deployed, and the WordPress plugin already owns MemberPress tier/lifecycle plus Core tenant/workspace provisioning. The missing seam is narrower: provisioning does not create, persist, verify, revoke or recover the entitled tenant LBI on that gateway, and WordPress may mark the lifecycle active before runtime proof. Remote reachability, tenant/workspace creation or a healthy sovereign-operator agent is not member-runtime proof.

**Required closure:** complete Wirebot App `R00.01`–`R00.09`, beginning by extending the existing WordPress → Core provisioning path rather than creating new infrastructure. Shared eligible tiers bind to the existing OVH gateway; only an explicitly approved Sovereign flow may create a dedicated runtime. Identity, consent, capability, receipts, outcomes and learning remain in their owning systems. Unsupported tenants retain explicit `unavailable` state, and wrong-tenant/operator-agent fallback probes fail closed.

### SAG-20 — complete work lifecycle

**Gap:** Workset, CallGraph, Workpoint, Work Loop, assignment and runtime execution exist but are not proven as one customer lifecycle from accepted assignment to terminal settlement.

**Required closure:** one real assignment traverses the whole chain with exact refs and receipts.

### SAG-42 / SAG-44 — Golden Path and task trackers versus Focusa work authority

**Gap:** Golden Path rows, GitHub issues, Beads/task trackers and Focusa Workpoints can still exist as separate planning/execution views without one approved binding.

**Required closure:** compile/bind the execution-ready task representation into Focusa-governed work without creating a new task authority. External trackers retain their appropriate domain role and stable refs.

---

## 5. P0 — shared human attention

### SAG-23 — unified approval/exception attention

**Gap:** approvals, owner-truth questions, provider authentication, UIAI takeover, budget/resource exceptions, recovery decisions and network opportunities can surface independently.

**Required closure:** implement `operator.attention.v1` as a source-bearing projection. Wirebot shows owner-wide attention; Workforce shows workforce scope; UIAI/Veragensia show specialist context. The source domain resolves the item.

**Non-goal:** a central approval database.

### NEW-P0-11 — presenter acknowledgement versus source resolution

**Gap:** without explicit state semantics, dismissing/acknowledging an item in Wirebot or Workforce could be mistaken for approving/resolving the source-domain action.

**Required closure:** attention contract distinguishes presenter UX acknowledgement from source-domain `resolved/cancelled/expired`; consequential action always revalidates current source state.

---

## 6. P0 — exact surface handoff

### NEW-P0-05 — `operator.surface_handoff.v1`

**Gap:** Wirebot, Workforce, Focusa Desktop, UIAI and Veragensia can deep-link conceptually but there is no common exact reference+intent envelope.

**Required closure:** versioned handoff with source/target surface, owner/project/workstream/foreman/work/attention/evidence/execution/body refs as applicable, intent, return reference, expiry and correlation. It carries no broad credential or transferred authority.

---

## 7. P0 — universal cross-product correlation

### SAG-35 — causal reference envelope

**Gap:** no single minimum reference envelope joins client/owner, partner, assignment, Workstream, work, worker, session, tool/job execution, UIAI execution, Evidence, receipt and outcome.

**Required closure:** implement `operator.correlation.v1` as references only. Do not centralize the underlying state.

This is required for reliable replay, audit, support, outcome economics and cross-product UX.

---

## 8. P0 — capability / entitlement posture

### SAG-02 — entitlement projection

**Gap:** product/runtime tiers, component licenses, Operator services and available capabilities remain difficult for clients to render deterministically without conflating commercial access with runtime authority.

**Required closure:** `operator.capability_posture.v1` with at least:

```text
supported
entitled
activated/connected
authorized/current authority posture
available/healthy
setup_required
```

The projection MUST NOT itself grant entitlement or authority.

### NEW-P0-06 — contextual expansion/upsell contract

**Gap:** the ecosystem has natural expansion paths, but without a shared posture client apps may hard-code commercial logic or create misleading locked states.

**Required closure:** product-owned capability metadata/recommendation refs that explain an observed gap and route to the owning purchase/setup surface. Recommendation is never permission.

---

## 9. P0 — credential/secret use references

### NEW-P0-09 — `operator.credential_use_ref.v1`

**Gap:** credential custody is documented, but cross-product execution still lacks one portable rule/schema for requesting use without moving the reusable secret through partner/workforce/task/handoff context.

**Required closure:** opaque credential reference with provider/account ref, requesting principal/work ref, requested operation/scope, consequence/approval policy, validity/expiry and correlation. The owning credential authority resolves or denies at execution time.

**Negative proof:** URLs, prompts, task descriptions, Evidence and receipts contain no reusable secret material; possession of the ref alone does not grant use.

---

## 10. P0 — shared contract compatibility, freshness and replay

### NEW-P0-10 — common envelope metadata law

**Gap:** the shared contract families are named, but product implementations can drift without one compatibility/freshness/replay baseline.

**Required closure:** actionable envelopes carry schema/version, producer/version, source ref, source revision, correlation, issued/observed time, expiry where applicable and idempotency/replay information for retryable mutations.

Required behavior:

- unsupported major/schema versions fail closed for consequential action;
- allowed additive compatibility is explicit, not assumed;
- stale/expired projections may be rendered but do not authorize mutation;
- offline/cached approvals, grants, entitlement posture and execution state are revalidated after reconnect;
- ambiguous consequential writes reconcile through the owning system rather than blind replay.

---

## 11. P0 — Evidence, settlement and outcome closure

### SAG-36 — explicit closure chain

**Gap:** execution proof, Focusa Evidence, verification, Focusa completion/settlement, W.I.N.S. acceptance and correction/dispute remain distinct systems without one reference chain.

**Required closure:** `operator.closure.v1` links refs and states while preserving each owner's state machine.

Required distinction:

```text
activity
!= Evidence
!= verified Evidence
!= settlement/receipt
!= accepted life/business outcome
!= portable standing
```

### SAG-28 — W.I.N.S. reusable modules/contracts

**Gap:** Wirebot/Workforce surfaces need a tenant-safe accepted-outcome projection without copying W.I.N.S. logic.

**Required closure:** canonical reusable W.I.N.S. operations/modules with tenancy and cross-surface tests.

---

## 12. P0 — sovereign federation and network isolation

### SAG-29 — Direct/network/Sovereign behavior end-to-end

**Gap:** documentation and Wirebot App tests demonstrate important isolation semantics, but one live Sovereign-to-network flow is not yet proven across identity, entitlement, projection, revocation and receipts.

**Required closure:** signed/minimized projection and bounded request path with explicit issuer/audience/scope/expiry/replay/revoke plus denied private-data/authority tests.

### NEW-P0-07 — federation versus fleet cleanup

**Documentation status:** **closed for current canonical docs as of 2026-09-15.** Current architecture, Golden Path spine, build-agent law and topology map reserve federation for independent sovereign participants and use fleet/aggregation for one Operator.

**Remaining proof:** downstream/product docs and runtime/API vocabulary must continue to be checked as those implementations change.

---

## 13. P0 — memory and context isolation

### SAG-11 / SAG-12 — partner/worker memory boundaries

**Gap:** stateful workers need durable context, but whether they share Wirebot stores/records remains unresolved. Focusa work continuity and general life/business memory are distinct.

**Required closure:** exact ownership and one-way refs between partner context, worker memory scope, Focusa Workstream/Workpoint and Evidence. Isolation is default; no ambient worker access to partner-wide memory.

### SAG-13 — offboarding/retention

**Gap:** retirement/export/delete/legal-hold behavior across partner memory, worker context, delegated humans, federation projections and downstream stores is incomplete.

**Required closure:** end-to-end lifecycle and revoke proof.

---

## 14. P0 — execution and intervention lifecycle

### SAG-37 — pause/revoke/takeover/rollback propagation

**Gap:** Focusa, UIAI and Veragensia each own legitimate lifecycle/control primitives, but one intervention is not yet tested across the full causal chain.

**Required closure:** exact-scope stop/pause/revoke/takeover, fencing, re-observation, reconciliation and receipt behavior across the owning systems.

### SAG-31 / SAG-33 — first-party operation parity and UIAI proof

**Gap:** missing first-party structured operations can still force CUA or incomplete acceptance.

**Required closure:** close product-owned API/CLI/tool parity gaps; prove UIAI execution/Evidence flows are consumable by Focusa/Workforce without copying UIAI authority.

---

## 15. P1 — Draftees and MeriFolio boundaries

### SAG-27 — Draftees ↔ private workforce

**Gap:** public worker profile/hire state can still drift from the private Operator roster/assignment.

**Required closure:** explicit profile/candidate ref → private assignment mapping, with no automatic private access.

### NEW-P1-01 — MeriFolio adapters

**Gap:** MeriFolio Worker/Access Session/Work Thread/Receipt vocabulary can overlap Focusa agent/authority/Workstream/receipt semantics.

**Required closure:** explicit adapter/ref mappings and documentation that MeriFolio is portable trust/standing, not local Workstream authority.

---

## 16. P1 — current product/document convergence

### NEW-P1-02 — current Wirebot App ownership propagated everywhere

**Documentation status:** **closed for current canonical ADLBOS/Wirebot/Workforce docs as of 2026-09-15.** Wirebot App is the current partner/customer application family; branded routes are presentation/deployment of that family unless an owner-approved product explicitly differs.

**Remaining proof:** implementation/release topology and any older noncanonical docs should be corrected when encountered rather than treated as authority.

### NEW-P1-03 — historical Tauri wrapper demotion

**Documentation status:** **closed for current canonical docs and topology map as of 2026-09-15.** Tauri is a packaging/technology choice where actually used or later selected, not the defining Wirebot/Operator product architecture.

### NEW-P1-04 — Operator Deployment mapping

**Documentation status:** **closed for current architecture/Golden Path docs as of 2026-09-15.** Operator Deployment maps onto purchase/participation, isolation, hosting/operation, federation and interface dimensions instead of defining a parallel runtime tier.

**Remaining proof:** product/marketing copy should consume the same dimensions when changed.

---

## 17. P1 — deployment/runtime truth

### SAG-05 / SAG-07 — capability and client-system inventory

Installed binaries and reachable services do not prove a worker may use them. The brownfield audit must feed role eligibility, task packs, provider/data scope and capability posture.

### SAG-18 — recurring worker scheduling

Typed recurring assignment/schedule semantics remain incomplete. A schedule is not blanket authority.

### SAG-19 — Manager/Crew delegation proof

Manager allowances, crew subset authority, acceptance and expiry still need a client-scoped runtime proof.

### SAG-21 / SAG-22 / SAG-43 — Focusa runtime readiness

Focusa Work Loop/Focus State/project bootstrap gaps remain owning-product defects and can block true continuous work. Workforce UI must represent these honestly, not hide them.

---

## 18. P1 — terminology cleanup

Keep these internal nouns exact:

```text
CanonicalOwnerPrincipal
DelegatedHumanPrincipal
OperatingPartnerPrincipal
ArchitectureAuthorityPrincipal
OperatorDeployment
OperatorEnvironment
Sovereign posture
fleet / multi-daemon aggregation
sovereign federation
Focusa Workstream / Foreman
Wirebot Workforce Composer
Focusa Workforce
```

Avoid using `Operator`, `federation`, `worker`, `receipt`, `authority`, `acknowledged` or `resolved` without domain qualification in machine contracts where ambiguity matters.

---

## 19. Execution order

Do not attempt all gaps as horizontal infrastructure first.

Close them through vertical slices:

```text
Slice A — partner → assignment → Focusa Workstream/Foreman → Workforce projection
Slice B — shared Needs You item → exact action → source-domain resolution
Slice C — worker executes through UIAI → Evidence → settlement → W.I.N.S. outcome
Slice D — Wirebot exact handoff → Workforce/UIAI → return with same correlation
Slice E — Sovereign Operator exposes one minimized network capability/opportunity → revoke
Slice F — delegated human performs one bounded operation → revoke → denied retry
Slice G — stale/offline attention or grant reconnects → revalidates → no stale mutation
Slice H — worker requests credential use by opaque ref → execution owner resolves → no secret crosses seam
Slice I — tenant conversation → accepted typed operation → governed execution/recovery → verified outcome → corrected later OpenClaw behavior
```

Each slice should implement only the shared envelopes it actually exercises.

---

## 20. Explicit non-goals

Do not create:

- another orchestration database;
- another workforce roster authority;
- another approval store;
- another evidence ledger;
- another credential vault;
- a plan-specific app fork;
- full federation before one isolated Operator loop works;
- shared worker memory by default;
- a MeriFolio replacement for Focusa;
- a Workforce replacement for Wirebot;
- a Wirebot replacement for Foremen;
- UIAI/browser control inside Workforce merely for visual completeness;
- a new entitlement authority inside a client UI;
- a central cross-product cache that becomes accidental authority.

---

## 21. Definition of architecture closure

The ecosystem is meaningfully closed when a replacement authorized agent can trace and operate this chain using stable refs and canonical owners:

```text
owner / valid delegated human where applicable
→ Operating Partner
→ accepted assignment
→ Focusa Workstream/Foreman
→ worker/runtime/body
→ exact execution
→ Evidence
→ settlement
→ accepted outcome
```

and can additionally prove that:

- an unentitled capability stays unavailable;
- an entitled capability still cannot exceed current authority;
- a revoked human delegation stops working;
- a revoked link/federation grant stops working;
- a worker cannot read partner-wide memory by default;
- a credential-use reference does not disclose the credential or grant use by itself;
- a stale cached attention/grant/entitlement projection cannot authorize a consequential mutation;
- unsupported contract versions fail closed where consequences matter;
- a browser takeover reconciles correctly before agent continuation;
- a surface handoff preserves exact context without passing authority in a URL;
- presenter acknowledgement cannot falsely resolve a source-domain action;
- branding/name changes do not create or widen identity;
- a second Operator cannot read or mutate private state without an explicit valid grant.
