# Wirebot Five-Model Golden Path: Greenfield/Brownfield Gap Register

**Date:** 2026-11-13  
**Status:** Planning review; gap flags and acceptance criteria only. **Not** an installation, entitlement implementation, price approval, or production-readiness certification.  
**Scope:** Reuse the existing Golden Path discovery/bootstrap assets and Wirebot App onboarding contracts to plan the five models: Proto, Tempo, Crew, Chief, Sovereign. The four models above Proto must be integrated into the Wirebot App.  
**Authority:** The Golden Path and existing product owners remain authoritative; this document records follow-up work without creating a new runtime, issuer, or task authority.

## 1. Reviewed source and confirmed present behavior

| Existing source | What exists | Current limit / flag |
| --- | --- | --- |
| [Brownfield audit](../../scripts/brownfield-audit.sh) | Local observed-component/system-shape and readiness report; optional remote mesh sweep, JSON/report delivery; v5 semantics | **EXPAND.** Read-only evidence is not enrollment or install. Needs machine/component-to-model dependency evaluation and reliable mixed-estate reuse checks. Sweep needs explicit cross-machine authorization. |
| [Substrate bootstrap](../../scripts/substrate-bootstrap.sh) | Checks base and runtime CLI availability and prerequisites; emits ordered install plan; only `--apply base --yes` installs limited base primitives | **EXPAND.** It does **not** install Pi, Focusa, UIAI Engine, OpenClaw or model-specific Wirebot orchestration. Existing `--install` prints routes, not full deployment. |
| [Activation blueprint](../../scripts/activation-blueprint.py) | Read-only plan from audit + owner intent. Separates dedicated VPS and managed isolation, proposes first-value outcomes | **UPDATE.** `SETUP_MODES` still enumerates older `wirebot_sovereign_operator`, `wirebot_sovereign`, `wirebot_direct`, `wirebot_network`. It must eventually understand the new commercial **models**, independently of hosting/ownership dimensions; not confuse a suggested plan with execution. |
| [Golden Path current doctrine](../../AGENT_OS_GOLDEN_PATH.md) and [ordered tasks](02-agent-os-golden-path-ordered-tasks.md) | Real field deployment sequence, cross-product authority, managed versus full-sovereign distinctions, owner approval and verification | **UPDATE.** Add a five-model installation/profile decision and cross-link this register; keep existing independent commercial offer and deployment topology distinctions. |
| [Wirebot App process contracts](https://github.com/Startempire-Wire/Wirebot-App/blob/main/docs/05-wirebot-app-core-process-contracts.md), [assessment projection](https://github.com/Startempire-Wire/Wirebot-App/blob/main/src/lib/contracts/assessment.ts) | Greenfield/brownfield/mixed assessment, plan/proposals, commissioning authorization, Setup & Readiness user journey | **EXPAND + ARCHITECT.** Current projection/operation resolver is not an executor; App must invoke versioned owning operations and display progress, receipts, errors, recovery. No arbitrary generated shell execution, App-only license check, or duplicate installer. |
| [Existing five-model technical matrix](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-wirebot-model-stack-license-enforcement-matrix.md) | Proposed shared stack/additional model capabilities and tentative enforcement points | **RECONCILE.** This is a planning matrix, not evidence that the five entitlements, installers, or end-to-end runtimes are shipped. Keep the revised model definitions aligned across website, App, Focusa, Core and Golden Path. |

**Greenfield finding:** There is no verified standalone end-to-end Greenfield installer for all five Wirebot packages in this inspected set. The current Greenfield lane is a *fresh-environment condition* handled through substrate preflight and Golden Path planning, not proof of a ready one-command script.

## 2. Proposed model bill of materials — confirm rights and deployments before code

| Model | Shared baseline | Added, pre-integrated offering | What the installer must select/verify | Status |
| --- | --- | --- | --- | --- |
| **Proto** | Pi + Focusa + Focusa Pi extension + UIAI Engine; owner identity, license, evidence and first useful task | No higher orchestration assumed. Custom customer Pi subagents are independent | Detect/reuse/install baseline; verify real Focusa/UIAI connectivity and permissions, first task and recovery | **Baseline to formalize** |
| **Tempo** | Proto | Packaged repeatable routines, alarms, scheduling/follow-through on the actual owning scheduler | Routine package selection, enablement and receipt; avoid replacing customer cron | **Added seam to architect** |
| **Crew** | Tempo | Wirebot Workforce Composer, Focusa workforce coordination/Foremen, specialists and licensed integration with Silent Sessions where allowed | Existing Focusa license rights, component roster, worker launch/dispatch paths and supervisor acceptance | **Rights and dispatch integration to architect** |
| **Chief** | Crew | OpenClaw-led persistent owner-wide chief-of-staff coordination across life and business | Correct isolated OpenClaw/Core bindings, continuity, supervisory recurring jobs and recovery | **Persistent runtime/binding proof needed** |
| **Sovereign** | Contractually defined integrated capability | Customer-controlled full-SOVOS deployment, dedicated VPS/private Tailscale mesh/local body where contracted; portability | Verify host topology, authority, identity, backups/migration and owner control; do not mistake standalone Operator Setup service for a Wirebot model | **Deployment acceptance proof needed** |

**Foundation is common, not necessarily unrestricted:** Focusa/UIAI belong in every Wirebot model, but each product's actual licensed rights must be mapped. A valid independently bought Focusa Operator Lifetime license may confer Silent Session/automation rights regardless of Wirebot level. Do **not** disable those rights when a Wirebot subscription ends. Basic Pi subagents and customer cron are not Wirebot-only resources.

**Separate commercial offers:** Direct Focusa/UIAI lifetime purchases (including separately bundled lifetime rights) remain distinct from the current $5,000 one-time Operator Setup service. The future automated Wirebot product should reuse the lessons and scripts from that service without retroactively reclassifying it as a Wirebot subscription.

## 3. Flagged changes (UPDATE / EXPAND / ARCHITECT)

| Priority | Flag | Owning surface | Required change and acceptance evidence |
| --- | --- | --- | --- |
| P0 | **UPDATE** | Five-model definitions + Golden Path profiles | Publish one precise, agreed bill of materials per model, differentiating commercial model, separate underlying licenses, and hosting profile. Identify optional/required services, dependencies and execution owners; no guessed user quotas or pricing. |
| P0 | **UPDATE** | Activation blueprint | Replace or add a versioned five-model input alongside the old modes, with explicit compatibility/migration handling. Invalid/unknown model must remain unresolved, not silently select a permissive install. Hosting stays an independent dimension. |
| P0 | **EXPAND** | Brownfield audit | Detect supported component *instances/health*, placement, runtime binding, compatible versions, existing license posture and reuse eligibility on the intended machines (without leaking secrets). Mixed estates produce a per-component install/reuse/repair/leave-alone decision with evidence/unknowns. |
| P0 | **EXPAND** | Greenfield substrate bootstrap | Build on base preflight to specify actual approved product-native installers/adapters for Pi, Focusa/Pi extension, UIAI, and higher-model dependencies, including dependencies, OS/platform support, idempotency and exact validation. Do not claim these installs presently exist. |
| P0 | **ARCHITECT** | Golden Path executing installer | One typed, model-aware **plan → preview → authorize → apply → verify → receipt → recover** orchestration, invoking the existing owners. Support greenfield, brownfield, mixed, upgrades/downgrades, safe reentry, backup and rollback. Avoid duplicative shell copies or shadow agent/runtime ownership. |
| P0 | **ARCHITECT** | Wirebot App | Expose model, environment, components and activation status in Setup & Readiness; bind to typed backend operations for each phase. Independent per-operation consent and verifiable receipts; app UI is a client, never the license authority or an execution proof. |
| P0 | **ARCHITECT** | Focusa / UIAI / Wirebot Core | Reconcile existing operator lifetime rights and runtime license policies before adding model-qualified entitlements. Map exact proprietary execution admission points (routine activation/run, workforce dispatch/start/resume, premium skills, Chief coordination) while preserving independent licenses and customer data. |
| P0 | **ARCHITECT** | Purchase/issuance/activation | Define direct Stripe Checkout on wirebot.chat → verified event → existing **wpuiai.com license authority** → correctly scoped product/model grant → installer activation/readiness receipt; idempotent processing/retry/renewal/cancellation. **Documented requirement, not verified implementation.** |
| P1 | **EXPAND** | Runtime verification and support | Prove on clean and previously configured customer-like environments; verify no duplicate installs, supported platform variants, no access/authority spillover, owner-visible first useful result, diagnosis and recovery. |
| P1 | **UPDATE** | Docs / model entitlement source of truth | Reconcile previous Wirebot Core/App legacy tier names with Proto→Sovereign; avoid shipping a marketing matrix whose actual gates/install topology differ. Record decisions and remaining undecided questions before enforcing them. |

## 4. Suggested installation composition (planning, not runnable commands)

1. Resolve exact purchase and license rights from the issuer; keep customer-held Focusa/UIAI lifetime rights separate.
2. Confirm desired commercial **model**, hosting profile and owner/operator authority independently. Do not infer VPS/Tailscale from any non-sovereign model by default.
3. Run authorized Brownfield discovery (even on a new host, to prevent destructive assumptions) and substrate preflight.
4. Produce a Greenfield/Brownfield/Mixed **component-by-component delta**, with supported versions, existing bindings, unknowns, repair needs and explicit owner confirmation for impactful actions.
5. Reuse healthy existing components; invoke product-native installers only for absent/approved components; provision higher-model integrations as separately traceable steps.
6. Bind and verify the actual issued entitlements in their owning services; App presentation alone grants nothing.
7. Execute one authorized useful task and verify its real source-side result; record install, license/activation, runtime-ready and accepted-outcome as distinct statuses.
8. Store nonsecret versioned receipts, recovery/rollback metadata and support handoff; preserve owner-controlled data, scripts and independent runtime capabilities on cancellation.

## 5. Planning decisions still open

- Exact set of **included vs optional** Focusa, UIAI and Pi features and additional packages at each model; how a separately owned license changes bundle pricing, provisioning or duplicate-install behavior.
- Whether Proto is app-wrapped or CLI-first at initial sale, and which higher capabilities live locally, in managed isolated environments, or on a customer Sovereign VPS.
- The precise proprietary distinction between Focusa Silent Sessions and Crew's packaged workforce dispatcher/Composer, including existing Operator Lifetime protections.
- Approved model-specific concurrency/seat/resource policies; whether the Wirebot App *wrapper-only* offering becomes a separate SKU.
- Which scripts/adapters support each OS and hosting topology, and whether migrations and upgrades are backward-compatible with existing four Operator Setup customers.
- Verified purchase-provider mapping and license issuer API contracts at wpuiai.com; subscription expiry, offline grace and restoration policies.

## 6. Completion standard for the planning work

Planning may be called **ready for implementation** only once each model has a signed-off bill of materials and explicit rights; every installed/operated component has one owner; Greenfield/Brownfield deltas are versioned and actionable; the Wirebot App operation contracts and backend executor are defined; and license issuance, runtime enforcement, upgrade/recovery and acceptance behavior are specified. Until those criteria are met, **no model-specific installer or entitlement gate is claimed production-ready**.

**Current outcome:** The reusable audit, base bootstrap, advisory blueprint and App assessment are identified; gaps above are flagged. **No installation script was run or changed, no license policy was altered, and no deployment was attempted in this planning review.**


---

## 7. November 14 reality ledger — one connected buyer-to-working-Wirebot journey

**Recorded:** 2026-11-14. **Nature:** Owner-requested written reconciliation of the November 13 discussion, anchored to the inspected source files. **Status:** design and source inspection; **not** live production acceptance, a new issuer, a new product approval, or proof of runtime delivery. This section supplements the previous gap register, not the owning architecture or commercial catalog.

### Definition of reality

A purchase does not equal a license; a license does not equal installed software; an installed executable does not equal a working integration; a running integration does not equal a verified useful result; and a Wirebot App screen does not grant authority. Record these independently and never label one milestone as proof of a later one.

| Gate (in actual customer order) | Owner and required handoff/proof | Status observed in reviewed source |
| --- | --- | --- |
| **0. Approved offer** | The commercial/website owners publish the exact approved Proto/Tempo/Crew/Chief/Sovereign SKU, scope, rights, license term, price, payer, hosting and support. Maintain a versioned mapping from offer -> separately owned products/License Types -> permitted features -> deployment variants. | **UNVERIFIED:** five-model commercial matrix is a proposal, not five approved saleable SKUs. |
| **1. Accepted payment** | \`wirebot.chat\` launches a server-resolved direct Stripe checkout; record provider account, transaction, customer, product, currency and paid period; independently verify paid state and deduplicate/reconcile webhook events. | **UNVERIFIED:** direct new-model checkout-to-provisioning chain not demonstrated. Do not treat a success redirect as payment truth. |
| **2. Authoritative license issuance** | Verified purchase -> WPUIAI.com / EDD paid order and canonical customer/product/License Type -> signed model/product-scoped grant and issuing receipt. Respect standalone Focusa/UIAI lifetime rights; never use a second local Wirebot issuer. | **UNVERIFIED:** exact five-model Stripe-to-EDD bridge, grant mapping and lifecycle not proven. |
| **3. Owner and target binding** | Verify customer identity, authorized installation/device, owner-controlled credentials, hosting choice and allowed actions. Keep model, legacy setup mode, technical level and tenancy/hosting separate. | **DESIGNED, NOT END-TO-END PROVEN:** no default VPS/Tailscale requirement for Proto/Tempo/Crew/Chief; Sovereign's contracted topology is distinct. |
| **4. Assess and calculate delta** | SOVOS Golden Path runs approved read-only substrate/brownfield discovery; captures actual components, health, versions, existing independent licenses and location. Compute \`reuse / install / repair / leave alone / unknown\` for an approved versioned model manifest. | **PARTIAL SOURCE PRESENT:** \`brownfield-audit.sh\` audits, \`substrate-bootstrap.sh\` checks; \`activation-blueprint.py\` is advisory and still recognizes older setup modes. Model-specific delta is missing. |
| **5. Apply the install** | Show plan and impact; record explicit authorization; invoke each component's owning idempotent installer/configuration adapter; preserve existing installations; return per-step verification/rollback/retry receipts. | **NOT IMPLEMENTED AS ONE CUSTOMER JOURNEY:** bootstrap can apply *base prerequisites only*; current scripts do not fully install Pi/Focusa/Pi extension/UIAI and higher-model packages. |
| **6. Activate and enforce** | Node-bound signed entitlements and customer permissions checked at the protected owning API/CLI/agent/tool, scheduler activation **and run**, worker creation **and dispatch**, Chief start **and resume**. Report actual connected/usable status. | **PARTIAL COMPONENT DESIGN/SOURCE:** Focusa licensing seams and App presentation exist; complete Wirebot five-model execution gates and bypass tests are not proven. |
| **7. Verify first customer value** | On the authorized installed environment, complete one agreed life, business or asset-building task; confirm the target-side effect, customer acceptance, health, support handoff and recovery path. Keep outcome evidence separate from billing/install receipts. | **UNVERIFIED AS A COMPLETE CUSTOMER CHAIN:** demos, contracts and readiness scores do not substitute for a paid/licensed/installed/accepted real task. |
| **8. Hand off to Wirebot App** | As the App matures, attach it to the existing identity, grants, workstreams, runtime, receipts, onboarding state and data without forcing customer reinstallation, re-purchase, or losing continuity. App presents authorized execution and recovery but never becomes the issuer or hidden runtime authority. | **PARTIAL SOURCE PRESENT:** \`Wirebot-App/src/lib/contracts/assessment.ts\` builds proposals/authorized operation descriptors with **no dispatch**. Full guided execution remains future integration. |

**End-to-end flow:** approved SKU -> verified Stripe payment -> WPUIAI.com/EDD order/license -> owner/node binding -> observed target state -> approved model delta -> source-owned authorized installation -> signed runtime activation -> accepted first result -> optional mature App. Every arrow must have an owning system, a durable nonsecret receipt/reference, retry/resume semantics, and failure state. An unknown gate is **UNKNOWN/BLOCKED**, never "ready."

### Five versions, one installer composition

- **Proto / Maker:** Pi + Focusa + Focusa Pi extension + UIAI Engine; verify basic rights and one bounded useful task. OpenClaw is **not** a Proto prerequisite.
- **Tempo / Steward = Proto + delta:** licensed prebuilt routine, alarm/trigger and verified repeat/follow-through; do not claim ownership of customer cron.
- **Crew / Foreman = Tempo + delta:** licensed packaged workforce Composer, Focusa Workforce coordination and bounded worker dispatch; independent Focusa Silent Sessions and Pi subagents are not automatically Crew-only.
- **Chief / Chief of Staff = Crew + delta:** persistent OpenClaw-led life-and-business portfolio orchestration, continuity, supervision and authorized recurring operations; verify actual Core/Focusa bindings.
- **Sovereign / Operating Partner = contracted integrated stack + owner-control delta:** full-SOVOS environment, dedicated customer VPS, Tailscale/private mesh and portability **where included in the signed agreement**; private inference and one-time Operator Setup are separate services, not assumed inclusions.

### Confirmed hosting and VPS/Tailscale rule — November 14 cross-check

**Resolved from pre-existing canonical documentation, not a new assumption:** The customer-specific persistent VPS + owner-specific Tailscale mesh + owner-controlled local body is the **full-Sovereign/SOVOS dedicated-environment requirement** (and may be part of a separately contracted Sovereign Operator/Operator Setup engagement). It is **not an automatic requirement for Proto, Tempo, Crew or Chief**. Their approved managed delivery profiles can use Startempire/operator-hosted, customer-isolated workloads/containers on provider infrastructure without requiring a customer VPS, tailnet or local computer; add customer-side infrastructure only when the accepted offer or an explicitly approved integration needs it. Chief's persistent coordination still needs a reliable runtime, but that runtime does **not** imply a customer-owned VPS. Never map old Sovereign Operator/Sovereign relationship labels, marketing-model rank or numeric entitlement directly to topology. Check the accepted offer and independently verify tenant/data/credential isolation; a container alone does not prove isolation.

**Primary documentation reread:**
- [SOVOS current architecture, §0.3 and §3A](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/main/CURRENT_ECOSYSTEM_ARCHITECTURE.md): non-full-Sovereign customers have managed isolated workloads; dedicated owner VPS + mesh belongs to full-Sovereign.
- [Golden Path ordered tasks, Hosting profile and isolation floor](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/main/docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md): specifically distinguishes dedicated full-Sovereign from managed and says the customer VPS/tailnet is not inherently required for managed.
- [Starter onboarding, Setup modes are not hosting requirements](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/main/starter.md): a purchased setup mode is not itself proof of hosting topology.
- [Wirebot App level operability](https://github.com/Startempire-Wire/Wirebot-App/blob/main/docs/14-wirebot-level-operability-contract.md): historical Sovereign and Sovereign Operator setups have dedicated topology, whereas Direct/other managed relationships may run on the shared, isolated provider runtime.

**Reconciliation outcome:** The November 14 reality ledger's earlier “no default VPS/Tailscale requirement for Proto/Tempo/Crew/Chief” statement is **verified by canonical documentation**. No remaining architecture question about a universal lower-model VPS mandate; only actual model-specific SKU/hosting entitlements and deployment proofs remain open. This is a documentation correction, not a completed deployment.

**Licensing and ownership invariants:** Wirebot models are commercial packaging, not the legacy four setup-mode labels or the 0–5 technical levels. A valid independently purchased Focusa Operator Lifetime or UIAI entitlement survives Wirebot cancellation according to its own terms. Customer data, scripts, model keys, machines and independently lawful Pi/OpenClaw/cron operation are not confiscated or remotely destroyed. Define paid-term suspension, update/support terms, offline grace, and restoration *before* enforcing a five-model license.

### Earliest truthful acquisition path (the App is not a launch dependency)

1. Define and approve exact customer-facing Proto deliverables, pricing, entitlement rights, fulfillment channel, supported environment, support boundaries and refund/cancellation terms. Do **not** display exploratory prices or placeholder Stripe links as live checkout.
2. If continuing sales **before the new automatic stack is complete**, sell only a properly scoped, approved, **human-assisted setup/service** that can actually be fulfilled; disclose the manual onboarding and delivery. Current separate Focusa Operator Setup relationships are field references, **not evidence of five new live subscriptions**. Otherwise use a clearly identified interest/request-access path or explicitly disclosed preorder, not false instant provisioning.
3. For automated Proto sale, close the real Stripe -> EDD -> signed grant seam, complete a resumable minimum viable Proto installer and verify one accepted task on both a clean target and a partially configured target.
4. Implement the four **incremental upgrade deltas** with explicit approval and preserved rights; prove a real upgrade, lifecycle enforcement, cancellation/recovery and customer-visible outcome at each level.
5. Wire the mature App onto the same installer/identity/license/runtime contracts later; never require customers to wait for its final UI to obtain the capabilities actually available in their contracted model.

### Acceptance / release discipline

For every proposed model offer record **Approved SKU**, **Verified payment**, **Issued EDD license**, **Bound node**, **Healthy components**, **Installation receipt**, **Authorized operation**, **Accepted result**, **Recovery verified**, and **App handoff compatibility** as independent statuses, each with \`observed | unverified | blocked | not_applicable\`, source owner, last verified date and evidence reference. No broad "done" status until all required model gates pass on a supported environment. Pilot/demo results do not prove public sale readiness.

**Immediate P0 order:** finalize bill of materials/rights and source-owner boundaries -> specify and integrate Stripe/EDD purchase issuance -> update greenfield/brownfield observation and model-qualified delta -> build and verify Proto apply/activate/recover -> prove first paid-license-to-use outcome. Then Tempo, Crew, Chief and Sovereign increments; App is a parallel consumer, not a blocking prerequisite.

**Source anchors:** [November 13 commercial/license matrix](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-wirebot-model-stack-license-enforcement-matrix.md), [November 13 website installation register](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-five-model-greenfield-brownfield-installation-gap-register.md), [commercial offer inventory](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-wirebot-consolidated-offer-inventory.md), [Wirebot App assessment](https://github.com/Startempire-Wire/Wirebot-App/blob/main/src/lib/contracts/assessment.ts), and the same repository's \`scripts/brownfield-audit.sh\`, \`scripts/substrate-bootstrap.sh\`, \`scripts/activation-blueprint.py\`.

**November 14 disposition:** Written reconciliation only. No checkout, installer, entitlement gate, infrastructure or customer deployment is claimed implemented by this edit.
