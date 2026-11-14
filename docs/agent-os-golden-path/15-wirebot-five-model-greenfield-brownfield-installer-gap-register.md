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
