# Wirebot five-model cost-plus pricing reconciliation

**Recorded:** 2026-11-14. **Status:** Internal scenario, cost-model input for commercial review; **not approved retail pricing, not verified vendor invoices, not an active Stripe catalogue, not a deployment acceptance certificate.** Customer-facing website shall expose only the approved price and delivered benefits, **never this internal cost model**.

## Decisions / source authority

- Five models are **Proto → Tempo → Crew → Chief → Sovereign**, each with life and business use cases, using the model-stack license matrix; not the legacy setup-mode names or numeric runtime levels.
- **Customer pays their own AI/model provider** (BYOK). Inference tokens are **$0 in Wirebot's COGS in this scenario**, not free to the customer. Third-party SMS, messaging, search/API subscriptions are excluded unless separately contracted and paid.
- Managed isolated runtime is permitted for Proto through Chief: **no customer VPS or private Tailscale requirement by default**. Full-Sovereign SOVOS requires the contracted dedicated owner environment, including VPS/private Tailscale mesh/local body, usually with hosting paid directly by the owner under the modeled commercial premise.
- **Founder engineering/architecture effort is investment-recovery cost**, not an outside legal debt. Future engineering, maintenance, upgrades, security and support are recurring costs and must also be included.
- Historical November 12 **$79/month Proto Founding Reader introductory launch promotion (first 3 months)** with proposed $99/month regular is **a real historical launch-price proposal**, but **not approved, active, or empirically cost-justified**. It has **not been declared abandoned by the owner**; reassess rather than silently delete history.

## Cost-model assumptions (replace with invoices/records as evidence arrives)

| Assumption | Scenario value | Evidence status |
| --- | ---: | --- |
| Active paying customers across five models | 150 (Proto 50, Tempo 45, Crew 30, Chief 20, Sovereign 5) | Illustrative only |
| Relative shared-cost weight | Proto 1.0; Tempo 1.3; Crew 1.8; Chief 2.7; Sovereign 4.5 | Allocation policy assumption |
| Founder development/architecture hours | 3,500 hours | Unverified economic investment |
| Founder work opportunity value | $125/hour | Unverified economic rate |
| Founder capital/value to recover | **$437,500** | 3,500 × $125, not third-party payable |
| Founder recovery period | 48 months | Planned pricing recovery, not accounting depreciation |
| Founder recovery pool | $9,114.58/month | Model formula |
| Future engineering + maintenance | 120 hours/month × $100 = **$12,000/month** | Scenario, includes releases, patches, adaptation |
| Shared business overhead | **$8,500/month** | Scenario (security, legal, accounting, operational platforms, sales, contingency) |
| Total shared recurring + recovery cost | **$29,614.58/month** | Allocated by relative weights to 239 weighted customer units |
| Support labor | $55/hour fully loaded | Scenario |
| Onboarding labor | $80/hour fully loaded | Scenario |
| Average active customer life | 18 months | Scenario for CAC/first-setup amortization |
| U.S. card payments | 2.9% + $0.30 | Published Stripe list rate; verify merchant/account |
| Stripe Billing pay-as-you-go | Additional 0.7% | **Optional** vendor list rate; set to zero if not used by WPUIAI/EDD flow |
| Refund/dispute/bad-debt provision | 1.5% of revenue | Scenario, not empirical loss |
| Target modeled contribution margin | 30% **after** payment fees, allocated maintenance, overhead, founder recoup | Owner profit goal represented as editable scenario |
| Income tax, financed capital costs | Not modeled | Add when source data known |

**Vendor pricing:** [Stripe card processing](https://stripe.com/pricing), [Stripe Billing](https://stripe.com/billing/pricing), [Cloudflare R2](https://developers.cloudflare.com/r2/pricing/). Individual OVH/KnownHost/Cloudflare production invoices were **not** verified for these customer allocations. Licensing/EDD bridge cost, customer taxes, legal merchant-of-record details and real chargeback profiles remain to be reconciled.

## Line-item seller costs per active customer, per month (scenario USD)

The columns below distinguish customer-specific costs from shared founder/maintenance burdens. These are **scenario estimates**, not invoiced expenses. Amounts include amortized unpaid onboarding and acquisition and assume customers fund their own inference; **no unlimited usage promise**.

| Item | Proto | Tempo | Crew | Chief | Sovereign |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tenant compute/runtime | 9 | 16 | 36 | 90 | 25 |
| Database, queue | 2 | 4 | 9 | 20 | 35 |
| Storage and backups | 3 | 5 | 10 | 25 | 30 |
| Network/CDN | 1 | 2 | 5 | 15 | 5 |
| Monitoring/logs | 2 | 4 | 10 | 18 | 40 |
| Secrets/identity/security | 2 | 4 | 7 | 15 | 30 |
| Email/alerts | 1 | 2 | 4 | 9 | 12 |
| Connector operations | 1 | 2 | 5 | 10 | 20 |
| Incidents reserve | 2 | 4 | 10 | 25 | 75 |
| Customer support (0.35/0.7/1.4/3/6 hours at $55) | 19.25 | 38.50 | 77.00 | 165.00 | 330.00 |
| Onboarding amortized (1/2/4/8/24 hours at $80 over 18 months) | 4.44 | 8.89 | 17.78 | 35.56 | 106.67 |
| CAC amortized ($90/$180/$450/$900/$1,800 over 18 months) | 5.00 | 10.00 | 25.00 | 50.00 | 100.00 |
| **Direct monthly customer cost** | **51.69** | **100.39** | **215.78** | **477.56** | **808.67** |
| Allocated founder cost-debt recovery | 38.14 | 49.58 | 68.65 | 102.97 | 171.61 |
| Allocated future engineering/maintenance | 50.21 | 65.27 | 90.38 | 135.56 | 225.94 |
| Allocated common business overhead | 35.56 | 46.23 | 64.02 | 96.03 | 160.04 |
| **All-in pre-transaction monthly cost** | **175.60** | **261.47** | **438.82** | **812.11** | **1,366.26** |

### Pricing math

For each model:

- **Direct cost** = tenant infrastructure + support labor + onboarding amortization + acquisition amortization.
- **Allocated monthly shared cost** = model weight × [$29,614.58 ÷ 239 weighted active units].
- **All-in cost** = direct + allocated founder-recovery + allocated future maintenance + allocated shared overhead.
- **Break-even posted price** = (all-in monthly cost + $0.30) ÷ (1 − 2.9% card fee − 0.7% optional Billing fee − 1.5% loss provision).
- **Price needed for 30% contribution margin** = (all-in monthly cost + $0.30) ÷ (1 − 2.9% − 0.7% − 1.5% − 30%).
- **Zero inference cost is seller-only:** customers still pay their own providers. Excluded customer-paid services must be identified in future commercial terms.

| Model | Proposed November 12 Founding Reader, first 3 months | Previously proposed regular | Scenario break-even | Scenario 30% margin floor | **Unapproved test price** |
| --- | ---: | ---: | ---: | ---: | ---: |
| Proto | $79 | $99 | $185 | $271 | **$299/mo** |
| Tempo | $199 | $249 | $276 | $403 | **$449/mo** |
| Crew | $499 | $599 | $463 | $677 | **$799/mo** |
| Chief | $1,299 | $1,499 | $856 | $1,252 | **$1,599/mo** |
| Sovereign | $3,199 | $3,499 | $1,440 | $2,106 | **$2,999/mo** |

**Interpretation:** Under *this* 150-customer scenario, $79/$99 Proto and $199/$249 Tempo cannot cover all modeled expenses; Crew's $599 is above break-even but below target; Chief and Sovereign can achieve modeled margin even at original regular proposals. **This does not establish what customers will buy or what should be approved.** The test prices are a discussion candidate, not a merchant catalogue, customer price commitment or authorization to publish a purchasable offer.

### Customer-count sensitivity: 30% margin price floors; mix/usage held fixed

| Total active customers | Proto | Tempo | Crew | Chief | Sovereign |
| --- | ---: | ---: | ---: | ---: | ---: |
| 50 | $653 | $900 | $1,364 | $2,283 | $3,824 |
| 150 | $271 | $403 | $677 | $1,252 | $2,106 |
| 300 | $176 | $279 | $505 | $994 | $1,676 |
| 500 | $137 | $230 | $436 | $891 | $1,505 |

Fixed shared costs are recovered over fewer/more active customers. The 50/150/300/500 counts are **scenarios, not revenue forecasts**.

## Offer-to-delivery contract at pricing review

| Model | Proposed contracted incremental customer value | Seller obligations to cost / verify | External costs excluded |
| --- | --- | --- | --- |
| Proto / Maker | Pi + Focusa + Pi extension + UIAI; scoped useful first task for life, business, or an asset | Compatible install/reuse, permission and license binding, support, integration, upgrades | Customer inference/model and third-party services |
| Tempo / Steward | Proto + durable packaged routines, triggers and accepted follow-through | Scheduler/queue durability, run admission, retries, notices, routine maintenance, support | Customer cron and provider-billed actions |
| Crew / Foreman | Tempo + packaged Workforce Composer, scoped Foremen/worker dispatch | Lifecycle and isolation of workers, licensed dispatch, acceptance evidence, safety/limits | Independently owned Focusa Silent Sessions rights, provider tools |
| Chief / Chief of Staff | Crew + persistent OpenClaw-led life/business coordination | Tenant isolation, continuity, recurring orchestration, exception handling, recovery | Customer model/API tokens and external SaaS |
| Sovereign / Operating Partner | Contracted full-SOVOS private owner environment and portability | Commissioning/support/update scope, mesh and identity verification, backups/recovery/exit, rights preservation | Owner's dedicated VPS/Tailscale, local body and inference where owner-contracted |

**Commercial seams not yet closed:** approved paid SKU, monthly-vs-perpetual contractual rights, onboarding price, separate Operator Setup/$5k offer, actual worker/time/storage/operations limits, support hours and response targets, provider charges, renewal/offline grace, refunds/chargebacks, WPUIAI/EDD Stripe activation and signed license, verified installers, and life-cycle entitlements. Source ownership and functional availability must be proven before making public commitments.

## Website agent handoff

Website PR should **only show model name, consumer-facing proposed price and differentiating included benefits** with visible **proposed/not-approved** status until merchant/SKU validation. Do **not** publish this cost breakdown or founder hours on wirebot.chat. Continue the existing Request Access path; do not invent live Stripe URLs, entitlements or proof. Price source must be replaceable with approved server-authoritative catalogue later. Treat the $79 Founding Reader introductory plan as a **historical proposal for review**, not approved and not unilaterally abandoned.

**Related canonical evidence:**
- [November 13 consolidated offers](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-wirebot-consolidated-offer-inventory.md)
- [November 13 model capabilities and license gates](https://github.com/Startempire-Wire/wirebot-website/blob/main/docs/website/2026-11-13-wirebot-model-stack-license-enforcement-matrix.md)
- [SOVOS Golden Path November 14 reality ledger](https://github.com/Startempire-Wire/agent-driven-life-business-os/blob/main/docs/agent-os-golden-path/15-wirebot-five-model-greenfield-brownfield-installer-gap-register.md)
- Workbook in the originating ChatGPT conversation: `wirebot_five_model_cost_profit_matrix_2026-11-14.xlsx` (not claimed to be committed into GitHub).
