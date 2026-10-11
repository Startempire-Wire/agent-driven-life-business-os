# Wirebot × HubSpot — Revenue Work Pilot

**Status:** CANDIDATE read-only first-value pilot, not a deployed automation or grant.
**Effective:** 2026-10-10.
**Canonical reusable profile:** [Commercial Work v1](../../commercial-work/revenue-engine.v1.json) validated by [schema](../../contracts/operator-commercial-work.v1.schema.json).
**Customer binding contract:** [Commercial Work Binding v1](../../contracts/operator-commercial-work-binding.v1.schema.json).
**General worker procedure:** [SOVOS Revenue Work skill](../../skills/sovos-revenue-work/SKILL.md).
**Routine composition:** [Business Revenue Engine Pack](../../routine-packs/business-revenue-engine.json).
**Owner documents:** [Stage 5 audit](../agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md), [Workforce Catalogue #09](../agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md), [Routine Compiler](../../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md), [Routine runtime closure #14](../agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md).

## Observed operating situation versus desired result

The owner has declared that a steady prospecting/sales routine is missing despite existing contacts and past commercial relationships. First pilot business: **Startempire Wire**, the operator of software commercial sales; an existing **Philoveracity** relationship portal may supply *read-only, independently authorized* relationship context. Do not collapse the businesses or imply combined account administration authority.

2026-10-10 private interactive discovery establishes that **both existing HubSpot portals are accessible through ChatGPT**, but does not establish Wirebot runtime credentials. Full contact counts, identifiers, account health, individual prospect details, sales history, CRM deal data, payment balances and customer status are **private operating facts**. Keep them in their owning systems or an approved customer-private audit/handoff, not this public repository. The first read-only routine must paginate all authorized records, distinguish automated senders from humans, reconcile consent/opt-outs and duplicates, and report source coverage and remaining unknowns. Previous email/template and sales-cycle evidence must be verified in the authorized mailbox before use. Do not invent conversion rates or winning templates.

The first commercial objective is **five additional $5,000 Operator Deployment setups** with full payment preferable but installment terms available. The advertised Operator Deployment offer remains **$5,000**; owner permits **up to five payments**. The owner has established an initial capped cohort with existing customers; **read current availability and installment balances only from owner-private records at each sale**, never publish fluctuating customer counts in portable contracts. Focusa standalone, UIAI Engine standalone, their bundle and other approved Wirebot offers remain distinct product routes with distinct licensing/entitlements. Software licenses and third-party operating costs must not be silently bundled into the $5,000 fee.

Customer-facing Wirebot relationship modes: **Sovereign Operator, Sovereign, Direct and Network**. They do not collapse into numeric technical tiers or imply that every offer receives a dedicated environment. Full-Sovereign deployments require customer-specific VPS, Tailscale private mesh and owner-controlled local body. Wirebot App is optional and not a prerequisite for the actual installation; W.I.N.S. remains an opt-in for the two sovereign modes. The exact approved offer, support, feature readiness and payment terms control sales claims.

## Private binding: Wirebot is first, not a special schema

[Sanitized wirebot fixture](../../tests/fixtures/operator-commercial-work-binding.wirebot.valid.json) names separate CRM source classes without real IDs or credentials. Copy and replace it **outside this repository** in the customer-authorized work environment; bind the exact source account IDs, owner/business refs, payment provider, offer catalog, contact/suppression policy, canonical Focusa workstream/assignment and owner communication channel. This profile is not allowed to copy contact bodies or long-lived tokens into source control.

The private binding can be checked without provider calls using:\n\n~~~sh\npython3 scripts/validate-commercial-work.py --binding /PRIVATE/customer/revenue-binding.json --json\n~~~\n\nThis checks only schema, source classes and private-reference hygiene; it cannot verify live grants, contact permissions or successful execution.\n\nThe ChatGPT HubSpot connector was verified interactively; **Wirebot's independent HubSpot authentication, API operations, provider permissions and send channel have not been verified**. A working ChatGPT connector does not authorize OpenClaw or Focusa. Until those bindings are verified, Wirebot may review owner-supplied results/drafts under existing permitted tools but must not claim native CRM automation.

## Existing composition, with no duplicate stack

| Sales responsibility | Existing reusable pieces | Next proof |
|---|---|---|
| Prospect discovery | OPP-01 / TP-OPPORTUNITY-01; Stage 5 and reconciliation | Source-backed, qualified opportunities; eliminate automated/vendor contacts |
| CRM continuity | EAA-01 / TP-CRM-01; reconciliation template | Exact-portal dedupe and reversible cross-business references |
| Offer match | OFF-01; current product/entitlement sources | Focusa, UIAI, bundle, or exact Wirebot setup without feature overclaims |
| Outreach and responses | COM-01 / TP-CUSTOMER-01; inquiry-triage + Follow-Up | Draft → separate send authority → provider delivery receipt |
| Ongoing pipeline | COS-01 + Focusa Workstream; Follow-Through | One due next action until verified disposition; no parallel CRM |
| Settlement | PAY-01; finance-operations + evidence-closure | Currency-qualified settled cash from authoritative provider; unpaid installments stay open |
| Fulfillment and improvement | CST-01 / OUT-01; delivery review, evidence, Quiet Kaizen | Actual customer acceptance, then private outcome/leverage assessment |

Use the canonical routine candidate/blueprint/instance compiler and existing OpenClaw/provider schedule. The profile's discovery and qualification stages are commercial compositions, **not falsely classified as new v1 routine families or already compiled executable routines**. Before adding new dedicated prospecting-family templates, follow the existing additive vNext routine contract, fixtures and consumer migration guidance.

## Minimal pilot and measured exit criteria

1. **Read-only:** Reconcile source scope, owner/contact permissions, history, opt-outs, duplicate identities and excluded non-prospects across both CRM portals. Document sampling/pages and evidence confidence.
2. **First useful work:** Deliver a prioritized, source-linked small opportunity set; owner accepts one real prospect and appropriate offer. Have Wirebot produce a specific, verifiable personalized outreach draft.
3. **Authorized effect:** If the owner grants the exact send channel and policy, perform one bounded send via the owning provider and verify provider receipt; otherwise the trial ends successfully at a reviewed draft, not an invented send.
4. **Repeatability:** Prove new response handling, deduplication, no duplicate touches after retries, stale/denied grant, wrong portal/tenant, opt-out, missed schedule, and pause/revoke. Do not let a single good run masquerade as steady unattended operation.
5. **Commercial outcome:** Observe replies → qualified opportunities → accepted terms → actual currency/settlement → delivery acceptance. Report **contract value, invoices, installments due and cash actually settled separately**. Unanswered/dormant prospects retain accurate terminal or next-check state.
6. **Portability proof:** Bind the same commercial profile to a separately controlled non-HubSpot professional-services fixture ([example](../../tests/fixtures/operator-commercial-work-binding.services.valid.json)); no relationship records, grants or owner context cross customers.

Success is a truthful, repeatable path to verified revenue and owner capacity, not the number of messages sent. Cross-client runtime claims require consumer evidence; the portable contract alone does not close SAG-10/SAG-18.

## Next execution owner

The authorized server agent should inspect actual Wirebot/Core/Focusa runtime state, existing OpenClaw schedules and current CRM permissions; then write the *private* owner binding and create **only an accepted first routine instance**, rather than importing a new framework or activating this repository's sample data. Keep current state/desired state and exact blocking refs in the existing SOVOS server-agent handoff, without overwriting product-specific authority.
