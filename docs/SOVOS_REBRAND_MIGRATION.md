# SOVOS Rebrand and Compatibility Migration

**Status:** ACTIVE HUMAN-FACING REBRAND — compatibility preserved; qualified naming strategy  
**Opened:** 2026-10-03  
**Current repository slug:** `Startempire-Wire/agent-driven-life-business-os`  
**Historical/current compatibility name:** Agent-Driven Life & Business OS / **ADLBOS**  
**Canonical human-facing architecture name:** **SOVOS — Sovereign Operations System**

---

## 1. Decision intent

The owner has directed that the architecture currently known as **Agent-Driven Life & Business OS (ADLBOS)** move toward the public identity:

# **SOVOS — Sovereign Operations System**

The rebrand is intended to clarify what the architecture has become:

- owner-rooted rather than model-rooted;
- human-sovereign rather than AI-sovereign;
- an operations doctrine rather than another app/runtime/database;
- capable of spanning life, businesses, workers, software, machines, evidence, outcomes and optional federation;
- portable across models, runtimes, computers, vendors and presentation identities.

The rebrand does **not** authorize a semantic architecture rewrite.

```text
ADLBOS architecture truth
        ↓ preserve
SOVOS public identity
        ↓ clarify
same owner-rooted portable doctrine
```

---

## 2. Why the migration is staged

This repository already has significant technical and documentary lineage:

- repository URLs;
- GitHub issue references;
- external links;
- historical version documents;
- compatibility-protected document paths;
- JSON schema IDs;
- structured-data schema/version strings;
- test fixtures;
- economic model filenames;
- scripts and tests;
- downstream/sibling references.

Therefore:

> **A brand rename is not permission for a repository-wide string replacement.**

The architecture already teaches that identity and implementation are different. The rename must follow the same law.

---

## 3. Current naming state

The human-facing architecture name may proceed as SOVOS now. Existing technical identifiers remain compatibility contracts:

```text
SOVOS
  canonical human-facing architecture / doctrine identity

ADLBOS
  historical and compatibility identifier

agent-driven-life-business-os
  repository slug retained

agent_os.*
adlbos.*
  existing machine identifiers retained unless separately version-migrated
```

Current prose may describe the intended transition as:

> **SOVOS — Sovereign Operations System (historically / compatibly ADLBOS)**

Do not imply that existing machine contracts have changed names merely because the public identity is changing.

---

## 4. Compatibility-protected identifiers

The following MUST NOT be renamed, moved, deleted, or silently rewritten merely for branding consistency:

### Repository

```text
Startempire-Wire/agent-driven-life-business-os
```

A future repository rename is a separate migration and should be one of the **last** steps, not the first.

### Economic source paths

```text
data/adlbos-human-equivalent-cost-model.v1.json
docs/ADLBOS_HUMAN_EQUIVALENT_COST_MODEL.md
docs/ADLBOS_PUBLIC_VALUE_FACT_SHEET.md
```

These are wired into repository integrity tests and existing references.

### Machine/schema identifiers

Existing values such as:

```text
adlbos.*
agent_os.*
existing JSON Schema $id URLs
fixture IDs
proposal IDs
contract URLs
```

remain stable unless a versioned compatibility migration proves there is value in changing them.

A human-facing brand does not require machine identifiers to match it.

### Historical/versioned documents

Dated snapshots, version-lineage documents, changelog entries, historical issue text and evidence should preserve the name that was true at the time unless a note is required to prevent present-day ambiguity.

History is not drift.

---

## 5. Migration phases

### Phase 0 — preserve intent and compatibility

**Now.**

- record SOVOS rebrand intent;
- preserve all ADLBOS architecture work;
- prohibit blind mass rename;
- identify machine/path dependencies;
- record external naming/trademark risk;
- allow SOVOS language in philosophy, design exploration and migration planning.

### Phase 1 — human-facing doctrine and qualified public identity

Proceed with:

- **SOVOS — Sovereign Operations System** as the architecture/doctrine name;
- **SOVOS Institute** as the teaching/research identity where organizational eligibility and structure support it;
- `sovos.ong` as the intended institutional domain if PIR eligibility is genuinely satisfied;
- clear association with Philoveracity where useful;
- preservation of the distinct software-product names: Wirebot, Focusa, UIAI Engine, Veragensia and others.

SOVOS is **not** a replacement product name for Wirebot, Focusa, UIAI Engine, Veragensia or another implementation. That distinction materially reduces market confusion and is part of the brand architecture.

Trademark/name review remains prudent for any proposed **bare SOVOS software product/service mark**, but it does not pause the doctrine/Institute migration.

### Phase 2 — human-facing current doctrine

Proceed with:

- README/title language;
- current architecture prose;
- Golden Path current prose;
- current build-agent docs;
- diagrams;
- public/economic copy;
- website extraction material.

Every changed current document should preserve an ADLBOS compatibility note for a defined transition period.

### Phase 3 — product surfaces

After product owners are ready:

- UI labels;
- documentation portals;
- onboarding;
- marketing;
- application metadata where appropriate;
- API documentation presentation labels.

No product may invent a separate authority model as part of the rename.

### Phase 4 — machine identifiers only where justified

Default: **do not rename them**.

If a machine identifier is ever migrated:

```text
old identifier
→ accepted compatibility alias / migration
→ new versioned identifier
→ consumer proof
→ deprecation window
→ only then retirement
```

Never mutate a schema meaning in place merely to change the brand word.

### Phase 5 — repository slug, optional and last

Only after:

- dependent repositories are inventoried;
- Git remotes and CI references are known;
- raw URLs and documentation links are mapped;
- redirects are tested;
- compatibility paths are preserved;
- the benefit outweighs the migration cost.

The repository slug may remain historical indefinitely without harming the public SOVOS identity.

---

## 6. External-name context and qualified-use rule

A material external conflict was discovered before the migration was made irreversible.

As of 2026-10-03:

- **Sovos Compliance, LLC** actively operates a large enterprise software company under **SOVOS**;
- it markets tax/compliance software and an **agentic AI** platform;
- a live U.S. **SOVOS** word-mark registration exists (registration no. 5,877,055; serial no. 87/564,848) covering tax/compliance computer software and related services.

This repository does not decide trademark law.

It establishes a narrower naming discipline:

> **Proceed with SOVOS as the architecture/doctrine and Institute identity; do not casually introduce a new bare `SOVOS` commercial software product in the tax/compliance/enterprise-software market without specific trademark review.**

The domain suffix `.ong` and qualified forms such as **SOVOS Institute**, **SOVOS — Sovereign Operations System**, and **SOVOS by Philoveracity** strengthen contextual distinction, but a TLD is not itself a trademark-law exemption.

The existing software products keep their own names. This repository's rebrand therefore does not require turning SOVOS into a competing tax/compliance software brand.

---

## 7. Philosophy versus technical architecture

The SOVOS name has acquired deeper philosophical resonance in the Philoveracity Relaunch work around:

- human freedom;
- owner/human sovereignty under God;
- technology as instrument;
- explicit and revocable delegation;
- coherence without erasure;
- many systems acting in harmony;
- the "One Song" metaphor.

That philosophical work is preserved in:

- `Philoveracity/Rework/relaunch/08-freedom-sovereignty-one-song.md`
- `Philoveracity/Rework/relaunch/10-book-outline-one-song.md`

Reference URL:
https://github.com/Philoveracity/Rework/tree/main/relaunch

This repository remains responsible for **technical architecture doctrine**, not for becoming a theological or philosophical authority store.

The philosophy may explain *why* owner-rooted architecture matters; the technical contracts must continue to define *how* it works.

---

## 8. Non-regression invariants

The rebrand MUST NOT alter these truths:

1. the deployment `CanonicalOwnerPrincipal` remains the architecture root;
2. delegated operation is not ownership;
3. Operating Partner identity remains distinct from model/runtime/body;
4. Focusa remains the governed-work/authority owner for its domain;
5. Focusa Workforce remains the workforce-operations surface;
6. UIAI Engine remains computer/browser execution owner;
7. Veragensia remains Agent Computer/body/runtime/placement owner;
8. source domains / owner acceptance retain accepted-outcome truth;
9. Wirebot/Perpetua retain the private feedback/leverage/Quiet Kaizen role;
10. W.I.N.S. remains optional/setup-aware where current doctrine says so;
11. federation remains explicit and never implies pooled authority;
12. activity remains distinct from Evidence, verification, settlement and accepted outcome;
13. reusable secrets do not cross ordinary seams;
14. one concern retains one canonical owner;
15. the doctrine remains portable rather than turning into another product runtime.

---

## 9. Agent instructions

When encountering either name:

```text
SOVOS
ADLBOS
Agent-Driven Life & Business OS
Sovereign Operations System
```

assume they may refer to the same architecture lineage unless context clearly identifies a historical snapshot or different concept.

Do not:

- create duplicate SOVOS copies of ADLBOS documents;
- fork contracts merely to change prefixes;
- rename compatibility-protected files;
- rewrite historical evidence;
- change schema IDs without a migration;
- rename the GitHub repository as cleanup;
- state that public trademark clearance is complete unless it has actually been completed.

Prefer:

```text
one architecture
+ one lineage
+ human-facing alias/migration metadata
+ stable machine contracts
```

---

## 10. Completion definition

The rebrand is complete only when:

- the human-facing architecture/doctrine identity is consistently SOVOS;
- any new bare commercial software use of SOVOS receives the specific clearance appropriate to that use;
- current human-facing doctrine agrees on that name;
- product surfaces adopt it coherently;
- old links/identifiers continue to work where promised;
- no architecture semantics were lost;
- no historical evidence was rewritten;
- all repository integrity/contract tests pass;
- a replacement agent can understand why ADLBOS identifiers still exist.

Until then, this is a **staged identity migration**, not a destructive rename.
