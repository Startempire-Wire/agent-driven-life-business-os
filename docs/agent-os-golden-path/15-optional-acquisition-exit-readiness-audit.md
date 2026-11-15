# Optional Acquisition & Exit Readiness — Stage 5 extension

> **Status:** PROPOSED optional audit profile, not installed runtime functionality, legal advice, valuation certification, permission to contact sellers, or authorization to broker transactions.
> **Parent:** [Stage 5 Full-Surface Business Discovery Audit](./12-full-surface-business-discovery-audit-and-workforce-inference.md).
> **Architecture authority:** `../../CURRENT_ECOSYSTEM_ARCHITECTURE.md`; use existing Focusa work/evidence, Wirebot owner-facing projection, and source-system truth.

## Decision and non-goals

Stage 5 remains the default audit, with unchanged ordinary-customer completion and first-value criteria. An owner or duly authorized delegate may **opt in** to an additional `acquisition_exit_readiness` assessment for sale, succession, acquisition preparation, or owner-independent scaling. Opt-out, unknown, and inaccessible are not negative readiness scores. Do not add a compulsory onboarding gate, new task store, new authority plane, automatic brokerage outreach, or app dependency.

The same optional profile supports an owner preparing to sell and a buyer evaluating a target, but the **buyer-side diligence scope is separately authorized**. A buyer's interest does not grant access to a seller's records.

## Activation and authority

Record an owner-approved profile selection, exact business/legal entity, jurisdiction, purpose (`scale`, `succession`, `sell`, `buy`), audience, data classes, source grants, authorized reviewers, expiration, withdrawal path, and visibility policy. Keep the audit read-only by default. Record every evidence item with source owner, retrieval timestamp, document period, classification, confidence, contradiction, and disclosure restriction. Owner-only financial and employee data never flows automatically to Wirebase or a marketplace. Public/partner/buyer sharing requires separate object-scoped permission and an appropriate NDA/data-room policy.

## Optional assessment domains

| Domain | Evidence and questions | Output / potential improvement |
|---|---|---|
| Owner dependence | Which approvals, relationships, pricing decisions, and operational steps stop without the owner? Test delegated operation | Owner-dependency map; bounded delegation and SOP candidates |
| Financial quality | Three years of financial statements and tax returns when available, trailing twelve months, accounting basis, AR/AP, debt, working capital, cash conversion, recurring revenue, owner compensation, add-back support | Reconciliation and missing-document ledger; **no agent-certified EBITDA, SDE, or valuation** |
| Customer / revenue concentration | Largest customers, churn, retention, renewal rights, sales pipeline, transferability and consent | Concentration and renewal risk register |
| People / knowledge | Key-person exposure, job descriptions, training, employment and contractor agreements, retention, access control | Cross-training and documented operating procedures |
| Contracts / legal | Entity ownership, licenses, permits, insurance, litigation, liens, guarantees, assignment/change-of-control clauses, leases, supplier terms | Counsel-reviewed issue list; no automated legal conclusion |
| Technology / IP / security | Source and domain ownership, software licenses, IP assignments, vendor dependency, access, backups, data protection, incident history | Remediation workstreams and verified recovery exercises |
| Operations / scalability | Process maps, cycle time, exception rates, quality, inventory, delivery, automation coverage | Repeatable routines, measurable owner-time reduction |
| Transaction / succession | Owner objectives, timeline, successors, seller financing preferences, transition assistance, confidentiality and stakeholder constraints | Readiness checklist, handoff plan, professional referrals |

All domains can be `not_requested`, `not_applicable`, `unverified`, `evidence_partial`, `verified`, or `blocked`. Never infer willingness to sell from age, public demographic signals, or missing documents. Show freshness and coverage before any readiness aggregate. An optional readiness index is a transparent rubric with versioned weights and visible unknowns, **not** a price estimate, investment recommendation, or prediction of sale completion.

## Typical transaction stages and document mapping

1. **Preparation and advisor engagement:** ownership authority, engagement and fee terms, conflicts, confidentiality, business profile, operating/financial cleanup.
2. **Marketing and screening:** permission-approved teaser, buyer qualification, NDA, confidential information memorandum (CIM) where appropriate; no agent sends without approved recipient, content and channel authority.
3. **Indication / offer:** IOI or LOI as applicable, price and structure assumptions, exclusivity, financing and contingency terms; human professional review.
4. **Diligence / data room:** reconciled financials/taxes, customer/vendor contracts, employees, payroll, IP, technology, cybersecurity, litigation, permits, property, assets/liabilities, consents and material exceptions. Every request maps to source, owner, permission, reviewer and status.
5. **Definitive agreement:** asset vs equity purchase, schedules/disclosures, representations, warranties, indemnities, escrow, working capital, transition services, assignments and third-party approvals, all with licensed legal/tax review.
6. **Closing and transition:** funds/escrow confirmation from authoritative providers, transfer checklist, employee/customer communications where approved, access handoff, seller training, post-close obligations.

Document names and requirements vary by transaction, entity type, industry and jurisdiction. A real-estate brokerage license does **not** by itself prove authority for every business-brokerage activity or jurisdiction; verify license scope, applicable rules and engagement before assigning regulated work.

## Audit-to-work flywheel

`source evidence → optional readiness findings → owner-reviewed priority → operator.routine_candidate.v1 → accepted blueprint → Focusa Workstream/Foreman/CRIST → bounded Wirebot/UIAI execution → independent outcome verification → refreshed readiness evidence`.

Reuse Stage 5 routine candidates, template matching, Focusa work and Evidence/receipts, and the existing 7/30/90-day planning output. No parallel task database, evidence authority or scheduler. Each improvement records baseline, expected business effect, owner time/cost, owner-reserved decisions, source-system metric, proof standard, rollback and re-audit date. Improvements do not imply increased sale price without qualified evidence.

## Wirebot App projection (future owning-repository work)

Expose the profile as an optional action from the existing audit; show domain coverage, unknowns, contradictions, permission scopes, diligence requests, readiness trends, proposed routines, accepted Workstreams, verified outcomes and explicit export controls. Keep drafts visually separate from executed work. The app displays canonical state through owning APIs; it does not become a second source of truth. Mobile-first view and progressive disclosure should keep ordinary Stage 5 simple. App implementation belongs in `Startempire-Wire/Wirebot-App`, following its current conventions and contracts, not speculative endpoints added here.

## Wirebase boundary (future product integration)

Wirebase may index owner-consented public facts and permission-scoped derived signals, each with provenance, freshness, legal basis, sharing policy and revocation. Private audit documents and buyer/seller intent are never syndicated by default. Seller interest, readiness claims, and buyer introductions require direct authorization. Wirebot software subscriptions and partner implementation agreements remain distinct; no service-delivery obligation is imposed on the software publisher.

## Acceptance and simulation matrix

- Ordinary Stage 5 audit produces identical mandatory outputs when optional profile is off.
- Opt-in/opt-out and revocation isolate each tenant, entity, reviewer and document; no cross-client leakage.
- Missing financial documents produce `unverified` and coverage gaps, never a fabricated score.
- Contradictory accounting, bank and tax figures remain separately attributed until reconciled.
- Buyer-side access cannot be inferred from seller discovery; restricted documents are denied.
- An audit finding generates a proposed routine, not a worker, schedule or customer contact.
- Authorized simulated workflow demonstrates source → candidate → approval → Workstream → evidence → independently accepted outcome → re-audit.
- LOI, NDA, data-room disclosure, brokerage referral and external outreach remain gated and logged.
- App projection and Wirebase export simulations verify no new canonical task/evidence store and no private data release by default.
- Run existing repository integrity and Stage 5 regression checks; cross-repository implementation requires separate owner-repository PRs and runtime evidence.

## Delivery sequence

1. Accept this optional Stage 5 contract without modifying default audit behavior.
2. Implement versioned optional intake, domain/rubric and evidence fixtures using existing schema conventions after examining their owners.
3. Simulate one seller and one buyer diligence case, including negative permissions and missing evidence.
4. Wire accepted findings to existing routine compiler and Focusa work/evidence interfaces.
5. Build Wirebot App presentation against verified APIs, then permissioned Wirebase projection.
6. Prove end-to-end on a consenting pilot business; record actual outcomes, not hypothetical valuation uplift.
