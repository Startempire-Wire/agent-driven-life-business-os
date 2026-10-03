# Repository Integrity Contract

**Status:** CURRENT repository navigation and anti-drift contract  
**Effective:** 2026-09-29  
**Scope:** this repository only; product repositories remain authoritative for their own implementation/domain behavior.

This file exists to make the repository legible to a replacement human or agent without creating a new architecture authority.

## 1. Authority and reading order

Read current truth in this order:

1. `OWNER_AUTHORITY_CONSTITUTION.md` — who may establish/supersede architecture.
2. `CURRENT_ECOSYSTEM_ARCHITECTURE.md` — current cross-product ownership and topology.
3. `AGENTS.md` — portable build/operations behavior.
4. `AGENT_OS_GOLDEN_PATH.md` — current deployment/operations doctrine and version target.
5. `docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md` — field-tested current working spine.
6. owning product repository/spec — implementation truth for the component being changed.

Supporting LIVE contracts control their declared concern. A version snapshot, changelog entry, issue, audit, compatibility path, or Git history entry never outranks current architecture merely because it is more detailed.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| **LIVE** | normative portable contract currently in force for its declared concern |
| **CURRENT** | present architecture, doctrine, working spine, audit, or derived reference |
| **INCUBATING** | operationally useful reference under active refinement; not settled normative authority |
| **DATED SNAPSHOT** | preserved audit/observation evidence from a named date; never current runtime or implementation truth without re-verification |
| **candidate** | proposed/versioned change awaiting the gates stated by its owning process |
| **SUPERSEDED** | retained for compatibility or history; must point to current replacement |
| **historical / lineage** | evidence of prior decisions; not present-tense authority |

Do not label the same artifact both LIVE and incubating.

## 3. Current Golden Path

The current target is `0.2.4-candidate`. Files `0.2.1.md` through `0.2.4.md` are version lineage. The current editable working spine remains `docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md`. Do not create another parallel Golden Path process document.

## 4. Compatibility-protected paths

These paths have known internal or sibling-repository consumers and MUST NOT be renamed, moved, or deleted without a consumer migration plus compatibility plan:

- `docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md`
- `docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md`

A tidier folder is not sufficient reason to break provenance, Focusa receipts, task records, or evidence URLs.

## 5. Economic source of truth

```text
data/adlbos-human-equivalent-cost-model.v1.json
  ↓ calculation authority
docs/ADLBOS_HUMAN_EQUIVALENT_COST_MODEL.md
  ↓ explanation
docs/ADLBOS_PUBLIC_VALUE_FACT_SHEET.md
  ↓ public-copy / website extraction
```

`docs/economics/01-human-equivalent-cost-and-leverage-benchmark.md` is a preserved compatibility path only. Do not maintain parallel totals by hand.

## 6. Outcome and W.I.N.S. invariant

```text
execution
→ Focusa Evidence
→ verification / settlement
→ source-domain accepted outcome
→ base private operator.leverage_snapshot.v1
→ Wirebot/Perpetua feedback + Quiet Kaizen
→ optional W.I.N.S. progression/recognition/community projection
```

W.I.N.S. is not required for the private base loop and does not become the owner of source-domain outcome truth.

## 7. Documentation versus implementation truth

Keep distinct: `specified`, `implemented`, `configured`, `reachable`, `healthy`, `authorized`, `verified`, and `customer-proven`. Open issues may represent real implementation gaps even when the desired contract is already documented.

## 8. Change rule

A repository-wide architecture/docs change is incomplete until:

1. current authority/status/version references agree;
2. compatibility-protected paths are preserved or migrated deliberately;
3. relative Markdown links resolve;
4. structured economic totals recompute exactly;
5. current W.I.N.S./outcome ownership invariants hold;
6. existing contract/schema tests pass;
7. `tests/repository-integrity-test.py` passes;
8. stale issue language touched by the change is reconciled;
9. the resulting diff is reviewed for accidental semantic deletion.

Run `bash tests/run-contract-tests.sh`. A clean prose diff without these checks is not a completed integrity sweep.

## 9. SOVOS / ADLBOS naming migration integrity

The owner has directed the human-facing architecture/doctrine rebrand from **Agent-Driven Life & Business OS (ADLBOS)** to **SOVOS — Sovereign Operations System**.

The migration is staged under [`SOVOS_REBRAND_MIGRATION.md`](./SOVOS_REBRAND_MIGRATION.md).

During compatibility migration:

- `ADLBOS` remains a valid historical/compatibility identifier;
- the repository slug `Startempire-Wire/agent-driven-life-business-os` remains protected;
- `data/adlbos-human-equivalent-cost-model.v1.json`, `docs/ADLBOS_HUMAN_EQUIVALENT_COST_MODEL.md` and `docs/ADLBOS_PUBLIC_VALUE_FACT_SHEET.md` remain protected paths;
- existing `adlbos.*`, `agent_os.*`, JSON Schema IDs, contract URLs, fixture/proposal IDs and evidence references are not renamed for cosmetic consistency;
- historical/versioned prose retains historical naming;
- SOVOS may be used now as the human-facing architecture/doctrine name and as a qualified Institute identity;
- existing software products retain their own distinct names;
- a new bare commercial software product/service branded only `SOVOS` should receive use-specific trademark review before launch.

A rename that breaks lineage, consumers, evidence, schema identity or repository tests is an integrity regression.
