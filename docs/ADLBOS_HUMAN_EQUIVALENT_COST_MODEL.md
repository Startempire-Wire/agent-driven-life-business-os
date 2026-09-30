# ADLBOS Human-Equivalent Operating Cost Model

**Status:** CURRENT public-safe economic reference  
**As of:** 2026-09-29  
**Purpose:** provide a conservative, updateable benchmark for the human labor that may be represented by recurring Agent-Driven Life & Business OS routines.  
**Calculation authority:** [`../data/adlbos-human-equivalent-cost-model.v1.json`](../data/adlbos-human-equivalent-cost-model.v1.json). Displayed totals in this document MUST agree with that file.  
**Not a price sheet:** this document does not state or imply ADLBOS pricing, customer savings, ROI, employee replacement, or guaranteed labor reduction.

---

## 1. Why this model exists

ADLBOS can compile recurring business work into deterministic programs, scheduled OpenClaw automations, Focusa-governed workers, UIAI computer execution, human-reserved decisions, routine analytics and continuous optimization.

A useful economic question is:

> **If a business had to perform the same modeled workload with people, what amount of paid human labor would the workload represent?**

That is different from claiming:

> "ADLBOS replaces X employees."

Most small businesses would not hire a separate full-time employee for every function. They would combine duties, use existing staff, hire part-time help, use a virtual assistant, or contract specialists.

Therefore this model uses **fractional human-equivalent hours** for each recurring routine and compares those hours with:

1. a U.S. employee compensation benchmark; and
2. a freelance/virtual-assistant market benchmark.

The modeled hours are assumptions for comparison, not claims about every ADLBOS deployment.

---

## 2. Current source anchors

### U.S. employee compensation

The U.S. Bureau of Labor Statistics reported that in June 2026 full-time private-industry workers cost employers an average of:

- **$54.00/hour total compensation**
- **$36.97/hour wages and salaries**
- **$17.03/hour benefits**

Wages therefore represented approximately **68.5%** of total employer compensation for full-time private-industry workers.

For the occupational benchmarks below, this model uses:

```text
estimated loaded employer cost
=
occupation median wage
÷ 0.685
```

This is an approximation. Benefit load varies by employer, occupation, industry, geography and worker. It should be used as a planning benchmark, not payroll/accounting advice.

### Freelance / contractor market

The contractor side uses current published Upwork category bands or an explicitly named conservative proxy. As of this refresh:

- virtual assistants: **$10–$20/hour**;
- advanced U.S. VA / executive-assistant support: **$38–$50+/hour**;
- customer service representatives: **$10–$19/hour**;
- bookkeepers: **$11–$25/hour**;
- market research analysts: **$25–$70/hour**;
- project managers: **$19–$45/hour**;
- sales representatives: **$13–$40/hour**.

Where no current role-specific public band is used, the structured model names the proxy explicitly. A proxy is a workload-comparison device, not a claim that the occupations are interchangeable.

---

## 3. Role benchmark table

The occupational medians below are U.S. BLS May 2025 wage benchmarks. The loaded employer estimate applies the June 2026 full-time private-industry compensation ratio described above.

| Human role benchmark | BLS median wage | Approx. loaded employer cost/year | Approx. loaded employer cost/hour | Contractor proxy used |
|---|---:|---:|---:|---:|
| Executive secretary / executive administrative assistant | $76,590/yr | $111,810 | $53.75 | $38–$50/hr |
| Secretary / administrative assistant | $48,310/yr | $70,526 | $33.91 | $10–$20/hr |
| Customer service representative | $21.53/hr | $65,376 | $31.43 | $10–$19/hr |
| Bookkeeping/accounting/auditing clerk | $50,670/yr | $73,971 | $35.56 | $11–$25/hr |
| Market research analyst | $78,760/yr | $114,978 | $55.28 | $25–$70/hr |
| Project management specialist | $102,320/yr | $149,372 | $71.81 | $19–$45/hr |
| Human resources specialist | $75,940/yr | $110,861 | $53.30 | $38–$50/hr |
| Sales-support proxy | $68,190/yr | $99,547 | $47.86 | $13–$40/hr |
| Management/process-analysis proxy | $101,860/yr | $148,701 | $71.49 | $19–$45/hr |

### Important interpretation

The loaded annual amounts above show what a **full-time** role costs at the benchmark wage. They MUST NOT be added together to claim ADLBOS "replaces" all of those people.

The routine matrix below uses only the modeled fraction of each role's time.

---

## 4. Representative recurring-routine matrix

This reference scenario models **50 human hours per week** distributed across common owner-support and business-operations work.

It is deliberately mixed: some work resembles executive assistance, some customer support, bookkeeping, sales operations, research, project coordination, workforce administration or process improvement.

| Representative routine | Human benchmark | Modeled human time | Employee-equivalent annual cost | Freelance/contractor annual range |
|---|---|---:|---:|---:|
| Daily inbox triage + owner summary | Executive assistant | 5.0 hr/wk | $13,976 | $9,880–$13,000 |
| Calendar coordination + reminders | Executive assistant | 3.0 hr/wk | $8,386 | $5,928–$7,800 |
| Meeting prep, notes + follow-up tracking | Executive assistant | 3.0 hr/wk | $8,386 | $5,928–$7,800 |
| Document/record organization | Administrative assistant | 2.0 hr/wk | $3,526 | $1,040–$2,080 |
| CRM hygiene + lead routing/follow-up preparation | Sales support | 4.0 hr/wk | $9,955 | $2,704–$8,320 |
| Weekly pipeline review + management report | Sales support | 2.0 hr/wk | $4,977 | $1,352–$4,160 |
| Customer inquiry triage + response preparation | Customer service | 5.0 hr/wk | $8,172 | $2,600–$4,940 |
| Invoice/AP/AR follow-up + bookkeeping preparation | Bookkeeping | 4.0 hr/wk | $7,397 | $2,288–$5,200 |
| Expense/reconciliation review | Bookkeeping | 2.0 hr/wk | $3,699 | $1,144–$2,600 |
| Market/competitor research brief | Market research | 3.0 hr/wk | $8,623 | $3,900–$10,920 |
| KPI compilation + management brief | Management/process analyst | 2.0 hr/wk | $7,435 | $1,976–$4,680 |
| Project/workstream status + blocker coordination | Project management | 4.0 hr/wk | $14,937 | $3,952–$9,360 |
| Vendor/renewal/deadline watch | Executive assistant | 1.5 hr/wk | $4,193 | $2,964–$3,900 |
| Hiring/workforce coordination + follow-up | HR / advanced-support proxy | 2.0 hr/wk | $5,543 | $3,952–$5,200 |
| Routine analytics + process-optimization review | Management/process analyst | 2.0 hr/wk | $7,435 | $1,976–$4,680 |
| Cross-business portfolio brief + priority synthesis | Project management | 2.0 hr/wk | $7,469 | $1,976–$4,680 |
| System/exception monitoring + escalation | Administrative assistant | 2.0 hr/wk | $3,526 | $1,040–$2,080 |
| Business-corpus delta audit + routine extraction | Management/process analyst | 1.5 hr/wk | $5,576 | $1,482–$3,510 |
| **Modeled total** | mixed functions | **50.0 hr/wk** | **$133,212/yr** | **$56,082–$104,910/yr** |

The structured JSON is the calculation authority; displayed values are rounded from it.

---

## 5. Direct example: scheduled daily email review

Suppose a business owner wants one reliable daily routine:

```text
every business day
→ inspect authorized inbox
→ separate urgent / actionable / informational mail
→ summarize important threads
→ identify commitments and follow-up
→ deliver one owner brief
→ escalate only what actually needs the owner
```

If a human executive assistant spent **1 hour per business day** on that routine, the modeled workload is:

```text
5 hours/week × 52 weeks = 260 hours/year
```

Using the benchmarks above:

| Human fulfillment model | Approximate annual labor cost |
|---|---:|
| U.S. executive-assistant employee-equivalent | **$13,976/year** |
| Advanced VA / executive-assistant contractor proxy | **$9,880–$13,000/year** |

That is the labor represented by the modeled routine. It is **not** a statement that an automated routine is equivalent in judgment, relationship quality, exception handling or legal responsibility to an experienced human executive assistant.

---

## 6. What the 50-hour reference scenario means

Fifty hours/week is approximately:

```text
2,600 human hours/year
1.25 conventional 40-hour FTEs
```

But the comparison is more useful than a simple FTE count because the work spans several specialties.

### Human-equivalent reference

For this representative workload:

- **loaded U.S. employee-equivalent:** about **$133,000/year**
- **freelance/contractor equivalent:** about **$56,082–$104,910/year**

These are labor-equivalent reference values, not ADLBOS pricing and not promised savings.

### Useful full-role context

A single full-time U.S. executive assistant at the BLS median wage is approximately **$111,800/year loaded** under this model.

A single general secretary/administrative assistant is approximately **$70,500/year loaded**.

This helps explain why even a portfolio of small recurring routines can become economically material without pretending that the business would have hired a dedicated employee for every routine.

---

## 7. What ADLBOS adds that a raw labor comparison does not measure

The purpose of ADLBOS is not merely to perform labor more cheaply.

Its architecture can also create system-level value that a simple hourly comparison cannot price reliably:

- deterministic execution of stable steps;
- 24/7 persistent scheduling on the private execution substrate;
- source-linked Evidence and receipts;
- repeatable recovery/retry semantics;
- owner attention reduction;
- cross-business reuse of proven capabilities;
- routine analytics;
- before/after measurement;
- leverage/momentum inference;
- Quiet Kaizen keep/improve/retire loop;
- progressive movement from manual → modeled → pilot → proven → automated → compounding;
- consistent policy/authority enforcement;
- lower dependence on one person's undocumented memory;
- ability to route only genuinely human-reserved decisions to the owner.

These are reasons to measure ADLBOS by **outcomes, reliability, attention and leverage**, not by pretending every automated action equals an employee hour.

---

## 8. Public-safe claims

The following statements are appropriate for future website extraction if the model date and sources remain current:

> **A representative portfolio of recurring business-support routines can easily add up to roughly 50 hours of human work per week.**

> **Using current U.S. compensation data, the modeled 50-hour/week mix in this reference represents about $133,000 per year of loaded employee-equivalent labor.**

> **Using current published freelance/contractor category bands and named proxies for the same modeled workload produces a rough market range of about $56,082–$104,910 per year.**

> **One routine as simple as a one-hour-per-business-day executive inbox review represents roughly $10,000–$14,000 per year of human labor at current executive-assistant/advanced-VA benchmarks.**

Always accompany those claims with language such as:

> These are modeled human-equivalent labor benchmarks, not claims that software replaces employees or guarantees savings. Actual work, rates, outcomes and appropriate human involvement vary by business.

---

## 9. Claims that should NOT be published

Do not publish:

- "ADLBOS replaces 9 employees."
- "ADLBOS saves every customer $133,000 per year."
- "One AI worker equals one human employee."
- the sum of every full-time occupational salary as if every customer would otherwise hire all roles;
- estimated owner time saved as verified savings unless the deployment actually measures it;
- revenue uplift without authoritative before/after evidence;
- a fabricated ADLBOS MSRP derived from these labor numbers.

The economic comparison should remain falsifiable and conservative.

---

## 10. Pricing / value guidance

This document intentionally does **not** define ADLBOS retail pricing.

For internal positioning, use three separate numbers:

```text
1. modeled human-equivalent workload value
2. actual measured customer value after deployment
3. actual ADLBOS commercial price
```

Never substitute one for another.

A future website may compare a published ADLBOS offer price against this model only after that offer price is separately approved and current.

---

## 11. Refresh procedure

Review at least annually, and sooner if a cited source materially changes.

Refresh in this order:

1. BLS occupational median wages.
2. BLS Employer Costs for Employee Compensation wage/benefit ratio.
3. Upwork contractor rate guides.
4. Optional secondary marketplace references such as Fiverr.
5. Routine-hour assumptions only when real ADLBOS deployments provide stronger measured data.

When real deployments exist, keep the public reference scenario and add **measured case studies separately**. Never silently replace modeled assumptions with anecdotal customer results.

---

## 12. Sources

Authoritative/statistical:

1. U.S. Bureau of Labor Statistics — Employer Costs for Employee Compensation, June 2026  
   https://www.bls.gov/news.release/ecec.htm

2. U.S. Bureau of Labor Statistics — Secretaries and Administrative Assistants, May 2025 wages  
   https://www.bls.gov/ooh/office-and-administrative-support/secretaries-and-administrative-assistants.htm

3. U.S. Bureau of Labor Statistics — Customer Service Representatives, May 2025 wages  
   https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm

4. U.S. Bureau of Labor Statistics — Bookkeeping, Accounting, and Auditing Clerks, May 2025 wages  
   https://www.bls.gov/ooh/office-and-administrative-support/bookkeeping-accounting-and-auditing-clerks.htm

5. U.S. Bureau of Labor Statistics — Market Research Analysts, May 2025 wages  
   https://www.bls.gov/ooh/business-and-financial/market-research-analysts.htm

6. U.S. Bureau of Labor Statistics — Project Management Specialists, May 2025 wages  
   https://www.bls.gov/ooh/business-and-financial/project-management-specialists.htm

7. U.S. Bureau of Labor Statistics — Human Resources Specialists, May 2025 wages  
   https://www.bls.gov/ooh/business-and-financial/human-resources-specialists.htm

8. U.S. Bureau of Labor Statistics — Business and Financial Occupations / Management Analysts, May 2025 wages  
   https://www.bls.gov/ooh/business-and-financial/

9. U.S. Bureau of Labor Statistics — Sales Representatives, Services benchmark, May 2025  
   https://www.bls.gov/ooh/sales/advertising-sales-agents.htm

Freelance-market references:

10. Upwork — Virtual Assistant hourly-rate guidance  
    https://www.upwork.com/hire/virtual-assistants/cost/

11. Upwork — U.S. Virtual Assistant guidance (advanced / executive-assistant support context)  
    https://www.upwork.com/hire/virtual-assistants/us/

12. Upwork — Customer Service Representative hourly-rate guidance  
    https://www.upwork.com/hire/customer-service-representatives/cost/

13. Upwork — Bookkeeper hourly-rate guidance  
    https://www.upwork.com/hire/bookkeepers/cost/

14. Upwork — Market Research Analyst hourly-rate guidance  
    https://www.upwork.com/hire/market-researchers/cost/

15. Upwork — Project Manager hourly-rate guidance  
    https://www.upwork.com/hire/project-managers/cost/

16. Upwork — Sales Representative hourly-rate guidance  
    https://www.upwork.com/hire/sales-representatives/cost/

---

## 13. Formula reference

```text
annual human hours
= modeled hours/week × 52

occupation wage/hour
= annual median wage ÷ 2,080
  (where BLS source is annual)

loaded employee/hour
= occupation wage/hour ÷ 0.685

annual employee-equivalent routine cost
= annual human hours × loaded employee/hour

annual contractor-equivalent routine cost
= annual human hours × contractor hourly band
```

The 0.685 divisor comes from BLS June 2026 full-time private-industry wages representing 68.5% of total employer compensation.
