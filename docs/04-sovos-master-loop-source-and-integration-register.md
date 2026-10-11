# SOVOS Master Loop — Source Coverage, Integration Seams and Completeness

**Status:** INCUBATING — source-backed draft register; not a task queue, runtime registry or approval.<br>
**Draft revision:** 0.2.0, 2026-10-11 — primary IIT principles and receiving-memory-agent integration handoff.<br>
**Parent:** [Master Loop](02-sovos-master-loop-draft.md).
**Behavioral annex:** [alarms and simulations](03-sovos-master-loop-alarm-and-simulation-design.md).

## 1. Evidence discipline

The operator requested grounding in the ecosystem's documentation, repositories and specifications before any coding. This register makes that ambition inspectable rather than pretending every repository or spec has already been read.

Evidence levels are separate: indexed; content-reviewed; source-implemented; installed/configured; reachable; authorized for exact operation; consumer-verified; outcome-accepted. A document's LIVE/CURRENT label describes its contractual role, not runtime proof. Dated proof remains dated unless revalidated. An incomplete read is not a whole-corpus audit.

Current activity: bounded local source/document review plus preservation of earlier session findings. Revision 0.2.0 additionally reviews primary IIT sources and current memory review/delivery/recall code to define proposed reciprocal integration; the operator authorizes documentation publication to the existing repository. No private CRM/mailbox data was ingested; no service or running demo was modified. Remote source/runtime revalidation was unavailable during this revision and remains a coverage gap. Existing sibling changes were preserved.

### 1.1 Working-tree provenance

| Repository/path | Observed local baseline | Review boundary |
|---|---|---|
| SOVOS `/root/agent-driven-life-business-os` | `695738c42745720c563c2956fea586e49bc38fa4`, clean before this draft; existing origin `Startempire-Wire/agent-driven-life-business-os` | Portable doctrine/contracts/catalogs; only new draft docs and index navigation changed |
| Focusa `/home/wirebot/focusa` | `16f2eeef0`; local identity/task artifacts modified | Selected product specs and implementation slices; no edits or fresh whole-product proof |
| Wirebot Core `/home/wirebot/wirebot-core` | `84eee29`; extensive staged/unstaged concurrent work | Current file contents may exceed HEAD; memory/native transition and other staged work are not certified deployed |
| Wirebot App `/home/wirebot/Wirebot-App` | `631a544`; local task artifacts modified, AGENTS untracked | Product process/specs plus selected pure TypeScript projections; runtime wiring unverified |
| Veragensia `/home/wirebot/veragensia` | `847eaee` | Profile/owning-spec inventory and cross-product boundaries; no hardware/actuation acceptance |
| UIAI `/home/wirebot/uiai-lab` | Directory contains demo/workforce material and is not itself a Git root | Not identified as authoritative UIAI Engine checkout; no product-source ownership inferred |

These are local observations, not a statement that every remote branch/runtime matches. Short hashes are provenance aids only. Private runtime configuration and secrets are deliberately excluded from public draft content.

## 2. Source ledger — reviewed foundation

### 2.1 SOVOS controlling and supporting sources

| Source | Review use | Remaining boundary |
|---|---|---|
| [Owner Constitution](../OWNER_AUTHORITY_CONSTITUTION.md), [AGENTS](../AGENTS.md) | Owner-rooted authority, requested activity, correction, scoped operations | Draft preservation is not implementation/deployment permission |
| [Cryptographic Authority](../CRYPTOGRAPHIC_AUTHORITY_PROFILE.md) | Identity/constitution/runtime hashes, canonical serialization, exact signed delegation and revocation reviewed | A model/process name is not authority; no new principal/key/delegation created |
| [Repository Integrity](REPOSITORY_INTEGRITY.md), [docs router](README.md) | Status vocabulary, protected paths, one canonical concern | This synthesis remains INCUBATING and does not replace current doctrine |
| [Current Ecosystem Architecture](../CURRENT_ECOSYSTEM_ARCHITECTURE.md) | Full-source review during the session; current key boundaries re-read | Product implementations and installed bindings require independent proof |
| [Information Infrastructure](../SOVOS_INFORMATION_INFRASTRUCTURE.md) | Full re-read: identity, typed meaning, provenance, distributed owners | No central fabric service or universal ontology inferred |
| [Human Freedom](../SOVOS_HUMAN_FREEDOM_OPERATING_DOCTRINE.md), [Driverless Business](../SOVOS_DRIVERLESS_BUSINESS_DOCTRINE.md) | Full re-read: human placement and mapped delegated operation | Maturity prose is not a demonstrated driverless domain |
| [Freedom & Leverage](../SOVOS_FREEDOM_AND_LEVERAGE_OPERATING_MODEL.md) | Full re-read: three frontiers, economic/financial/life spines, Perpetua | No universal score, automatic spending or replacement purpose |
| [Mathematical Intelligence](../SOVOS_MATHEMATICAL_INTELLIGENCE_AND_COMPOSABLE_EXPERIENCE.md) | Full re-read: four registries, engine families, human-meaning contract | Staged architecture; algorithms/catalog do not prove running alarms |
| [Routine Compiler](../SOVOS_ROUTINE_COMPILER_AND_TEMPLATE_LIBRARY.md) | Full re-read: five objects, determinization, trigger/reliability/promotion | Generalized compiler/runtime still partial |
| [Cross-Product Seams](../CROSS_PRODUCT_SEAM_CONTRACT.md) | Full re-read: refs, revision/freshness, replay, attention versus resolution | No new global clock/event bus/store |
| [Owner Channels](../SOVOS_OWNER_NOTIFICATION_AND_RESPONSE_CHANNEL.md) | Full re-read: SMS-first where viable, ntfy limits, replies, privacy | Deployment-specific routes and consumer proof required |
| [Portable Memory](../PORTABLE_MEMORY_REFERENCE_PROFILE.md) | Full re-read: incubating lifecycle, tiers, causal eval, ownership gaps | Small-corpus substrate; transcript ownership and production parity unsettled |
| [Agent Computer](../AGENT_COMPUTER_REFERENCE_PROFILE.md), [Ambient Operator](../AMBIENT_OPERATOR_REFERENCE_PROFILE.md) | Purpose/roles/enforcement/conversation sections reviewed | Remaining detailed owning-spec conformance must be audited; not ambient surveillance consent |
| [Contract Optimization](../AGENT_CONTRACT_OPTIMIZATION_PROFILE.md) | Core law, ownership, classes and provenance sections reviewed | Remaining evaluation/migration details pending before any policy changes |
| [Golden Path](../AGENT_OS_GOLDEN_PATH.md) | Current spine/owner/hosting/authority sections reviewed | Detailed deployment sequence remains its existing owner; not forked here |
| [Workforce Catalogue 09](agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md) | CRIST, worker lifetimes, human VAs, existing managers and memory boundaries reviewed | Remaining profile-by-profile applicability and live capability proofs pending |
| [Discovery 12](agent-os-golden-path/12-full-surface-business-discovery-audit-and-workforce-inference.md) | Full re-read: authorized source coverage, evidence classes, existing work | No actual all-account/device discovery performed by this draft |
| [Portfolio Compiler 13](agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md) | Full re-read: private loop, setup modes, analytics, optional W.I.N.S. | Not a deployed general compiler |
| [Runtime Closure 14](agent-os-golden-path/14-routine-compiler-runtime-closure-plan.md) | Full re-read: inquiry slice, exact instance/grant/trigger/evidence chain | Existing plan is referenced, not newly decomposed or activated |
| [Seam/Autonomy Audit 11](agent-os-golden-path/11-agent-os-golden-path-seamless-autonomy-gap-audit.md) | Full re-read: identity/workforce/delegation/work-lifecycle/attention/correlation, credentials, memory, control, compatibility, optional federation and closure | Listed joins remain gaps unless separately proven; existing execution-order examples are not activated |
| [Templates](../routine-templates/README.md), [packs](../routine-packs/README.md) | Current catalogs enumerated/re-read; canonical versus compatibility paths | Individual JSON policy/step fit must be reviewed for each chosen binding |
| [Commercial pilot](commercial-work/WIREBOT_HUBSPOT_PILOT.md) | Read-only source boundary, private binding and existing-profile reuse | ChatGPT CRM access is not Wirebot runtime access; no contact/account facts copied |

### 2.2 Machine-readable contract seams

No schemas were changed. Existing strict v1 contracts should be reused where adequate; unsupported additions require explicit evolution, fixtures and old/new consumer proof.

| Existing artifact | Intended reuse / inspection disposition |
|---|---|
| `contracts/operator-routine-instance.v1.schema.json` | Full review: compiled step input/output refs, operation/decision/prompt/attention refs, consequence/idempotency; supervision, grants, trigger owner, reliability, acceptance, lifecycle/privacy |
| `contracts/operator-attention-policy.v1.schema.json` | Full review: notification classes, channel routing, quiet hours, coalescing, consequence ceiling, source revalidation, lock-screen policy |
| `contracts/operator-routine-template.v1.schema.json` | Previously reviewed; recheck exact enums and bindable parameters before draft contract evolution |
| `contracts/operator-routine-candidate.v1.schema.json` | Identified canonical inference envelope; detailed alarm/candidate mapping pending |
| `contracts/operator-routine-blueprint.v1.schema.json` | Identified owner-specific preview; exact obligation/cell additions pending |
| `contracts/operator-routine-pack.v1.schema.json` | Canonical catalog composition; not identity/activation |
| `contracts/operator-leverage-snapshot.v1.schema.json` | Base private outcome/capacity projection; inspect exact fields before richer economic/life extensions |
| Specified families `operator.attention.v1`, `operator.correlation.v1` | Source-bearing presentation/correlation are specified in current doctrine/audit, but corresponding JSON Schema files are NOT present in this checkout's `contracts/`; materialization and exact case mapping remain gaps |
| Specified closure and opaque credential-use seams | Conceptual cross-product boundaries, not existing `operator-closure` or `operator-credential-use-ref` JSON Schema files in this checkout; exact product contracts/binding remain to be verified |
| `contracts/operator-environment.v1.schema.json` | Dedicated full-Sovereign semantics; cannot relabel managed containers |
| `contracts/operator-commercial-work.v1.schema.json`, `contracts/operator-commercial-work-binding.v1.schema.json`, `commercial-work/revenue-engine.v1.json` | Existing commercial composition/private binding; no added prospecting v1 enums by implication |

The `contracts/` directory inventory was checked during this revision. Distinguish its materialized files above from specified-only families; neither naming nor file existence proves field compatibility. Shared contracts may carry refs, not customer-specific source bodies or reusable secrets.

### 2.3 Product/spec evidence

Paths below are exact inspected or session-carried references, not cross-repository relative Markdown links.

| Product/source | Grounding and evidence level |
|---|---|
| Focusa `docs/05-intuition-engine.md` | Full re-read; asynchronous, zero-blocking signals only; cannot decide/act/write memory/mutate focus |
| Focusa `crates/focusa-core/src/intuition/signals.rs` | Source inspected: existing `create_signal` uses origin/kind/frame/summary/payload ref/tags; not a full cross-domain alarm contract |
| Focusa `docs/97-focusa-reflex-primitives-spec.md` | Full re-read: typed trigger/context/reflex/evidence/escalation; current registry exposes advisory metadata |
| Focusa `crates/focusa-api/src/routes/reflex.rs` | Selected code inspected: registry-backed read summaries mark `advisory_only: true`; discovery is not activation |
| Focusa `docs/current/FOCUSA_BRAIN_BODY_ANALOGY_GAP_MAP.md` | Organism map/table reviewed; dated 2026-05-26; long corpus index not re-audited as current exhaustive inventory |
| Focusa `docs/UNIFIED_ORGANISM_SPEC.md` | Relevant authority/data/promotion/degraded/integration/retention/JARVIS sections reviewed; older April snapshot conflicts recorded below |
| Focusa `docs/78-bounded-secondary-cognition-and-persistent-autonomy.md` | Status/authority/closed-loop sections re-read; normative target with explicit partial/docs-only limits |
| Focusa `docs/100-context-cognition-spec.md`, `docs/61-domain-general-cognition-core.md` | Earlier session review: bounded/advisory context and generic cognition; not document-ingestion proof |
| Focusa `docs/137-focusa-temporal-authority-deadlines-urgency-grounded-forecasting-spec.md` | Status, ownership, goals and temporal laws re-read; normative draft, not all implemented |
| Focusa `docs/138-focusa-prediction-outcome-calibration-metacognitive-learning-transfer-and-epistemic-governance-spec.md` | Status, maximal primitives, ownership and scope re-read; no full-lineage implementation claim |
| Focusa `docs/167-governed-procedure-compiler-design.md` | Full re-read: design-only typed effects/steps/handoffs; crosswalk required, not a shipped procedure engine |
| Focusa `docs/current/CALLGRAPH_IMPLEMENTATION_STATE_2026-08-16.md` | Full re-read: dated landed/remaining ledger; not current executor/settlement proof |
| Focusa `docs/135b-crist-project-genesis-context-role-interview-spec-tasks.md` | Status, CRIST sequence, iterative state machine and corpus-versus-prompt sections re-read; draft requires approved Spec before Tasks and does not silently rewrite accepted artifacts |
| Focusa `docs/135f-domain-general-ontology-core-semantic-graph-domain-packs-and-reactive-context-spec.md` | Status, foundations/partial implementation and candidate-to-canonical graph/projection sections re-read; domain packs do not create independent runtimes or grant authority |
| Focusa specs 149, 153/181–184, 156, 174/175 | Document inventory or prior-session basis; exact sections/contracts/call-sites and current conformance still pending |
| Focusa `apps/focusa-awareness/{README.md,index.ts,openclaw.plugin.json}` | Earlier session source/installed divergence evidence; current remote parity not reverified |
| Wirebot Core `docs/specs/PROACTIVE_KERNEL_v3.md` | Relevant historical quality/continuity/sensor/anti-duplication portions re-read; not a runtime prompt or current architecture authority |
| Wirebot Core `docs/MEMORY_DELIVERY_JOBS.md` | Full re-read on 2026-10-11; current concurrent native source work, V1 production, disabled native writes, incomplete cutover/single-writer qualification |
| Wirebot Core `cmd/scoreboard/memory_review_commit.go` | Full inspected local source: `commitApprovedMemory` transaction commits review and allowed sink jobs together; acknowledgement is not provider delivery |
| Wirebot Core `cmd/scoreboard/letta_memory_delivery.go` | Full inspected local source: `deliverNativeLettaMemory` reconciles committed source-qualified content, returns bound provider receipt; not a separate reasoning loop |
| Wirebot Core `cmd/scoreboard/letta_approved_recall.go` | Full inspected local source: current approval, payload hash, exact native/provider binding and committed content checked before disclosure; lexical bounded operator-only recall, not generalized workforce memory |
| Wirebot Core `plugins/wirebot-sensors/index.ts` | Selected local source inspected; synchronous poll functions and prompt hooks coexist with timers; do not generalize historical OVH repair to this checkout |
| Wirebot Core memory/Context Core/integration/operations docs and bridge/native code | Earlier session sources; exact deployed wiring and role-scoped disclosure need new proof |
| Wirebot App `docs/04-wirebot-app-system-map.md` | Current foundation/availability/Google/Flow Mesh/campaign/Perpetua sections re-read; remaining IA/source conformance pending |
| Wirebot App `docs/05-wirebot-app-core-process-contracts.md` | Full process content reviewed, including P1–P11: discovery, correction, routines/research, UI parity, optional participation and commerce |
| Wirebot App `docs/07-wirebot-perpetua-demo-pivot-spec.md`, `docs/10-wirebot-body-independent-partner-continuity-addendum.md` | Full re-read; public demo distinct, one persistent relationship across bodies |
| Wirebot App `src/lib/contracts/perpetua.ts` | Selected pure projection helpers reviewed; active capabilities, routine history/research controls are not backend enforcement or compiler proof |
| Wirebot App `src/lib/ui/trusted-catalog.json` | Exact artifact located; upstream owner and component/version/action conformance need verification |
| Veragensia docs 193/194/195/199/201 | Exact paths inventoried and portable profile reviewed; machine-enforcement/control/transfer/ambient acceptance not re-proven |
| JARVIS archived original | Earlier full-session review carried forward; seven-domain intent preserved, live claims rejected without new proof |

### 2.4 External research carried from this session

These primary sources ground candidate selection, not a new live benchmark. No licensed model was installed or paid inference requested for this preservation revision. Recheck exact current release, license, terms, route and hardware before binding.

| Source | Design contribution / unresolved claim |
|---|---|
| [TypeSafe API](https://docs.typesafe.ai/api), [models](https://docs.typesafe.ai/models), [confidence](https://docs.typesafe.ai/confidence) | Typed questions against bounded state; concentration is not empirical calibration; route/version/retention must be explicit |
| [Jev limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13), [fan-out](https://docs.typesafe.ai/patterns/fan-out) | Literalness, distraction, contradictory criteria and question applicability require tests; deterministic validation remains necessary |
| [Cloudflare Jev route](https://developers.cloudflare.com/ai/models/typesafe/jev/) | Different hosting/terms for the same model; not an independent competitor |
| [Decision 2.0 Kai](https://huggingface.co/vllm-sr/Decision-2.0-Kai-0.6B), [Lux](https://huggingface.co/vllm-sr/Decision-2.0-Lux-9B) | Local candidates; reported GPU latency is vendor/author evidence, not our consumer latency |
| [Laya](https://huggingface.co/convaiinnovations/laya), [Kev](https://github.com/jaredpalmer/kev) | Local alternatives; domain/language tuning and non-controlled comparisons limit general conclusions |
| [GLiClass](https://github.com/Knowledgator/GLiClass) | Narrow labeling candidate, not assumed typed-question parity |
| [Tononi & Koch 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4387509/) | Primary integration/exclusion, perturbation predictions, aggregates/feed-forward and virtual-versus-physical substrate sections inspected; no inference of conscious software |
| [IIT 3.0 primary paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003588) and [IIT 4.0 primary paper](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465) | 3.0 overview inspected; 4.0 framework/identification and selected distinction/connectivity examples inspected, including copy-cycle versus specialized lattice; mathematical implementation audit remains incomplete |
| [Tononi/Boly/Massimini/Koch 2016](https://www.nature.com/articles/nrn.2016.44) | Public abstract/authors/references only; paywalled full article not read or purchased |
| [Kleiner/Tull formalization](https://doi.org/10.3389/fams.2020.602973) | Supplementary generalized mathematical treatment, not the requested primary lineage or assumed 4.0 identity |
| [IIT simulation design](03-sovos-master-loop-alarm-and-simulation-design.md), §12 | Versioned source-to-principle-to-test crosswalk, finite-model requirements and constrained multi-objective improvement; no numerical computation or deployed Phi |

## 3. Repository coverage that remains necessary

"All repositories" must become a finite, owner-scoped source manifest. Do not scan unrelated customers, private accounts or backups to satisfy that phrase. Use the architecture router and each product's authoritative checkout/spec index; record exclusions and inaccessible regions explicitly.

| Owning area | Current coverage | Required reconciliation before completeness |
|---|---|---|
| SOVOS doctrine/contracts/library | Central current sources reviewed; tracked Markdown inventory observed | Full disposition of remaining root profiles, Golden Path 02/05–11/handoff, structured artifacts and compatibility/history |
| Focusa core/API/harness/Workforce | Selected specs and source seams reviewed | Current source/runtime version; operation-specific inputs/outputs, grants, dispatch/settlement, continuation and consumer proof |
| Wirebot Core/OpenClaw/Context Core | Current docs plus earlier installed observations | Installed plugin/runtime revisions, existing schedules/sensors, genuine automatic inbound, memory and source-auth bindings |
| Wirebot App | Process/organism/body boundaries reviewed | Remaining IA/trajectory/controls, trusted catalog provenance, registered operation bindings, headless and UI consumer proof |
| UIAI Engine | Tool surface known; authoritative checkout not established here | Resolve actual product repo/revision/docs; adapter/error/diagnostic/Evidence/cleanup contracts and installed parity |
| Veragensia | Portable boundary and spec inventory | Exact trust/workload/lease/resource/transfer interfaces and accepted hosting profiles |
| Flow Mesh | Prior repaired projector/provider evidence carried | Current owning task/provider interface, human assignee mapping, loop/deduplication and closed-task versus outcome semantics |
| Knowledge/memory: Agent-KB, Agent Wiki, Mem0, Letta | Portable/current source boundary identified | Fresh retrieval provenance, retention/transcript owner, review/delivery/recall paths, writer fencing and restore proof |
| Public Perpetua/Arena | Explicit distinction recorded | Only public-safe simulation/story needs; do not modify demo for operational convenience |
| W.I.N.S./MeriFolio/Startempire federation | Current portable optional boundaries reviewed | Relevant exact optional projections/disputes/disclosure; off-path proof and no private critical-path dependency |
| SendyKit/campaign marketing | App/source ownership distinction recorded | Only if selected: exact sender/audience/version/suppression/callback/receipt contracts; not a mailbox dependency |
| Third-party connectors/model providers | Candidate sources identified | Current terms/license/version/privacy/cost and exact permitted operations, not an assumption of available credentials |

A repo is not fully reviewed because one README or entry point was opened. A unavailable remote region remains unavailable; it must not become "nothing there" or "all audited." Historical branches and compatibility paths should be dispositioned, not blindly merged into the current plan.

## 4. Integration contract sheets required before code

Every real seam needs a sheet with: source and consumer repo/revision; owner; exact entry operation/call-site; supported input/output and error versions; source identity/tenant/domain; data minimization/retention; current authority and credential-use; causal cursor/time/revision; replay/idempotency; lease/concurrency; timeout/backpressure; unavailable behavior; receipt/evidence/outcome; correction/pause/revoke; compatibility/migration; producer/consumer/interop/live acceptance. Missing facts are explicit gaps, not implementation defaults.

| Seam | Existing anchor | Proposed connection / missing proof |
|---|---|---|
| Source → connector cell | Native provider API/event/query; current Wirebot sensors | Exact source classes, scopes, pagination/cursors and health envelopes; no universal ingestion service |
| Connector → intuition/salience | Focusa signal creation, Spec 05, Focus Gate | Scope-bearing bounded event mapping and source revision; domain coverage is not implied by frame signals |
| Expectation → due/absence | Source commitments; Focusa temporal primitives | Actual expectation persistence owner, calendar/time policy and missed-event recovery |
| Several signals → concern | Existing correlation/attention/reflex seams | Durable alarm case owner, grouping/split correction, storm control and supported operations |
| Uncertainty → fast question | Routine step `decision_policy_ref` / `prompt_contract_ref`; secondary cognition | Provider-neutral question/output mapping, route policy, validator, budgets and abstention |
| Mathematical output → Intelligence Result | Existing four-registry architecture | Actual schemas/engine adapters, applicability and evidence/calibration; no new result database |
| Result → trusted composition | Wirebot trusted catalog/A2UI strategy | Registry/binding revisions, operation registration, error states and accessibility |
| Candidate → accepted instance | Existing v1 candidate/template/blueprint/instance | Owning compiler implementation and exact accepted-revision/current-grant binding |
| Instance → trigger/run | OpenClaw/provider-native scheduler | Installed scheduler API, exact revision, lease/replay/missed-run and durable receipt |
| Work → existing human/agent | Workforce Composer, Focusa, task/CRM owner, Flow Mesh | Identity, accepted responsibility, decline/reassign, capacity and minimal context |
| Assignment → permitted effect | Focusa/executor/provider; UIAI fallback | Live dispatch admission, machine enforcement, exact effect/recovery and receipt |
| Effect → outcome | Source/receiver + Focusa Evidence | Independent acceptance policy, disputed/partial/unknown state and durable settlement |
| Outcome → follow-through | Perpetua over source-linked obligation | Durable next-check owner, momentum hypothesis/horizon and valid terminal disposition |
| Attention → mobile/voice reply | Attention policy; Wirebot/OpenClaw channel owner | Exact channel identity, privacy, retries, authenticated correlation and consequence revalidation |
| Experience → memory/learning | Existing review/delivery and Focusa epistemic owners | Reviewable source/outcome episode → accepted revision → async bound sink receipt; no raw automatic promotion |
| Memory → current concern/action | Portable memory READ/MANAGE lifecycle; native approved recall source | Exact purpose/role scope, eligible revision, freshness, budget and live-source revalidation; no generic worker access inferred |
| Memory correction/delivery → loop health/context | Review eligibility, delivery jobs/trace and existing health owner | Invalidation, visible unavailable/denied state, causal ordering and consumer retrieval proof; no new clock/ledger |
| Body change → same partner | Veragensia/Focusa continuity; App addendum | Enforced handoff/fencing, supported capability loss and receiver proof |
| Integration evaluation → revised design | Isolated synthetic model | Defined transitions/controls; no simulation result becomes production authority |

## 5. Contradictions and compatibility constraints discovered

1. **Older unified-organism ownership:** April guidance calls Flow Mesh canonical task/work graph and Letta only local continuity. Current source/provider/Focusa work boundaries and ongoing native memory redesign are more specific. Preserve intent, resolve through current owners; do not import the old matrix wholesale.
2. **Older degraded-mode bypasses:** direct execution without Focusa and local shadow queues conflict with required current governance/canonical work. Read-only/degraded orientation is not an operational bypass.
3. **Historical JARVIS certainty:** "infrastructure works," heartbeat quotas, fixed model upgrades and mandatory continuous output are intent/history, not current proof. Preserve quality, sensors and continuity without always-execute or alert-volume rules.
4. **Intuition versus action:** Spec 05 cannot decide/act; Spec 97 discovery is advisory. A real permitted reflex effect belongs to the existing action/executor contract, not intuition or registry metadata.
5. **Procedure compiler versus routine compiler:** Spec 167 typed effect/confirmation design and SOVOS routine binding must be crosswalked. No second compiler or softened financial/security confirmation rule is assumed.
6. **Optional W.I.N.S.:** older App wording about outcome ownership must be reconciled with current SOVOS source-domain truth and optional progression. Private loop acceptance cannot depend on participation or public scoring.
7. **Native memory versus deployed V1:** concurrent native source proofs do not establish production cutover, role isolation or a provider/cross-host compare-and-swap lease. Current disabled-write boundary stays intact.
8. **Sensor checkout versus installed repair:** local source contains synchronous polling/prompt-hook paths; earlier OVH timer/asynchronous repair cannot certify this checkout or the present installed body without parity evidence.
9. **App helper versus operational authority:** pure capability/routine/research helper code is a projection; it cannot enforce source grants, research shutdown or backend revision-bound approval by itself.
10. **Catalog versus complete engine:** mathematical registries and routine JSON artifacts are present design/library; no general running organism or cross-business alarm fabric is inferred.
11. **Full-Sovereign versus managed service:** dedicated VPS/mesh/body contract is not a label for any container; local Kai or tailnet access alone proves neither tenant isolation nor sovereignty.
12. **Forecast versus deadline:** hazard/response estimates inform checks; they do not alter accepted source deadlines or waive temporal ownership.

Each must be settled in its owning specification or explicitly accepted crosswalk before coding the affected seam. Recording a conflict is not resolving it.

## 6. Unresolved design register — not tasks

| Question | Current draft posture | Resolution evidence required |
|---|---|---|
| Who persists alarm case/expectation state? | Source-owned obligation plus correlated projection; exact product owner open | Owner-approved model, supported create/update/resolve/replay contracts |
| What is the minimum connector/result contract? | Reuse existing source/signal/ref/Intelligence Result seams first | Field/error/version crosswalk and old/new consumers |
| How are relevance/severity/uncertainty prioritized? | Separate dimensions, goal/context-based bands | Consequence-specific policy and held-out noisy/missed-event cases |
| Which math engines improve actual cases? | Methods are reservoir, not mandatory footprint | Defined inputs/assumptions/baseline and measured benefit |
| Where does fast judgment execute? | Async; Kai local candidate; hosted only permitted | Hardware/licensing/quality/privacy/budget plus consumer latency |
| What are calibration/abstention thresholds? | No fabricated universal numeric threshold | Shared held-out cases, error costs and approved risk policy |
| How are existing humans bound? | Reconcile incumbent responsibility before dispatch | Actual assignee identity/state/handoff/capacity interfaces |
| Which current scheduler/run owners are usable? | OpenClaw default where appropriate, native alternatives | Installed API/revision/grant/retry/revoke and completion receipt |
| Who maintains native business state? | Primary-loop maintenance and writer qualification not assumed | Current product design, stale-update denial and cross-host fencing |
| Who owns transcript truth and retention? | Explicitly unresolved in portable profile | Owner-rooted assignment, privacy classes and accepted correction/deletion rules |
| How does outcome-then-momentum close? | Separate predicates and bounded next checks | Domain/horizon/terminal dispositions with receiver proof |
| Which setup/channel combinations are supported? | Provider-neutral, explicit hosting and SMS/push limits | Deployment-specific identity, consent, outage, accessibility and cost |
| What does the IIT experiment actually calculate? | Separate small finite network, not deployed Phi | Reviewed formulation, transition model, temporal grain and reproducible method |
| What is the complete source denominator? | Relevant repo/spec inventory in progress | Each required area reviewed, excluded with rationale, superseded or unavailable with accepted design |

### 6.1 Handoff to the agent owning memory implementation

**Reading path:** [Master Loop](02-sovos-master-loop-draft.md), §11.1 → [joint memory simulation](03-sovos-master-loop-alarm-and-simulation-design.md), §10.1 → [IIT research](03-sovos-master-loop-alarm-and-simulation-design.md), §12 → [portable memory profile](../PORTABLE_MEMORY_REFERENCE_PROFILE.md), §§2–13 and ownership routing. These are revision 0.2.0 design proposals, not a memory cutover or implementation assignment. Cite the exact fetched Git revision; being pushed does not prove a running agent loaded it.

**Respect active ownership:** this revision does not edit the portable memory profile, Wirebot memory docs/code, review queue, sink jobs, native bindings or V1 runtime. The memory agent continues its existing verified assignment. Its findings can revise these same documents; this handoff does not create another memory backlog, authority or writer.

| Existing source anchor | Reuse opportunity / boundary |
|---|---|
| Portable profile WRITE/MANAGE/READ and five tiers | Existing lifecycle and bounded disclosure; no sixth “gut memory” store |
| `commitApprovedMemory` | Atomic approved revision plus allowed delivery jobs; a Master Loop episode must use the owning review path, not call an internal helper without its authorization |
| `deliverNativeLettaMemory` / `nativeMemorySourceDocument` | Revision-qualified provider document and committed replay reconciliation; do not copy whole cases, raw transcripts or another source's authority |
| `recallNativeApprovedSources` / `handleLettaApprovedRecall` | Local code bounds query to 500 characters and results to 1–10; timeout is 15 seconds; checks current approval/provider binding. Operator-only and lexical: role/tenant-generalized retrieval is NOT proven |
| Documented `GET /v1/memory/delivery/jobs` and `GET /v1/memory/trace/{memory_id}` | Candidate delivery-health evidence surfaces; exact current registration/auth/version and runtime parity must be verified before binding |
| Existing native block/state bindings | Separate primary-loop state-maintenance seam; protected IDs/read-only flags, expected revision and qualified writer generation remain mandatory |
| Focusa evidence/epistemic outcomes | Link information-set/recall revision to result and correction; acceptance remains with source/receiver, not memory |

These are inspected source/doc anchors, not declared public callable contracts. The local Wirebot Core baseline is `84eee29` plus concurrent modifications; its source-qualified native work is not certified deployed by this draft.

**Questions the memory agent should resolve in the owning design, not improvise during a Master Loop build:**

- Which supported operations accept a minimal episode/correction candidate and expose its accepted source revision? Which interface states separate review, enqueue, provider delivery, recall and use?
- How can exact tenant/principal/domain/role/purpose and token/result budgets reach the real consumer without weakening current operator-only boundaries?
- How do rejection, erasure, supersession and expired eligibility invalidate caches/context and remain denied despite old immutable provider history?
- Which writer maintains native business state after verified outcomes? How are generation fencing, expected revision, pause/revoke and ambiguous completion proven across bodies/hosts?
- How are source correction and task/case truth reconciled without memory overriding live assignments, current grants or accepted outcomes?
- Where are transcript truth/retention and permitted episode summarization assigned? What must never be copied into shared doctrine or worker context?
- What actual consumer proves the later recall influenced an appropriate response? Which held-out/null-memory and missing-feedback controls expose a decorative connection?
- What current operation/schema errors and additive or versioned extensions are required? Any proposed shared envelope remains references-only until the owning contracts approve it.

**Receiving-agent disposition:** record each seam as supported-source-only, deployed/consumer-proven, unsupported, conflicting, or proposed extension, with evidence and exact source revision. Return corrections as bounded revisions to this register; never convert the gut–brain metaphor, a memory retrieval, or a simulated Phi into new permission. Proposed callback names/fields in §11.1 are design requirements, not registrations to implement blindly.

## 7. Specification-completeness gate

The entire bounded Master Loop specification must pass this gate BEFORE task or CallGraph decomposition. No checkbox is checked by this preservation revision.

- [ ] Finite ecosystem repository/spec/contract manifest reconciled; current owners, baselines, coverage and unavailable regions recorded.
- [ ] All session requirements trace to a design section, source basis, owning component and acceptance predicate; no alarm/model/IIT narrowing.
- [ ] Every required integration sheet names exact behavior and supported interfaces or an explicitly accepted new design—not a guess.
- [ ] Signal/expectation/case/attention/work/run/outcome/momentum ownership and transitions settled without parallel authorities.
- [ ] All alarm families, absent events, correlation/split/dedupe and health/recovery paths reviewed.
- [ ] Existing routines, Standup, sensors, employees/managers/VAs and in-flight work reconciled before any new activation.
- [ ] Decision-model applicability, privacy routes, calibration/abstention, resource placement and failure behavior specified; no vendor claim substitutes for proof.
- [ ] Mathematical-engine applicability/assumptions and normalized result/composition bindings specified.
- [ ] Memory/transcript/correction/retention/writer boundaries and V1/native compatibility settled for intended use.
- [ ] Reciprocal episode/review/delivery/eligible-recall/invalidation seams mapped to memory-owner operations; joint controls prove contribution without a second store or worker-wide disclosure.
- [ ] Scope, delegated authority, credentials, human-reserved decisions, takeover, pause/revoke and cross-client denial covered.
- [ ] Three whole-loop synthetic scenarios and adverse variants have independently specified success/failure predicates.
- [ ] Virtual intact/partition/ablation model is precise; IIT version, equations, state/grain/independence, normalized partitions, software bounds and paper-vector reproduction are reviewed.
- [ ] Intelligent integration has predeclared hypotheses, held-out controls, separate `φ_s`/structure `Φ`/outcome dimensions, rejection rules and hard privacy/authority constraints.
- [ ] Outcome verification, follow-through, momentum, leverage and optional W.I.N.S./federation semantics reconciled.
- [ ] Timing, concurrency, backpressure, budgets, observability, source outage, replay and disaster recovery designed to the actual consequence.
- [ ] UI/API/CLI/voice semantics and trusted components map to the same operations; unavailable behavior is honest.
- [ ] Producer/consumer/cross-version/live proof obligations and migration/rollback described per product owner.
- [ ] All consequential contradictions resolved or explicitly excluded; exclusions preserve the agreed system intent.
- [ ] Operator review/corrections incorporated; draft revision and intended future implementation ceiling explicit.

Completeness does not mean every future feature is included or every product already implements the needed change. It means the agreed system boundary is sufficiently specified that necessary changes can be decomposed without inventing responsibilities, policy, contracts or acceptance while coding.

## 8. Preservation and verification record

This revision changes documentation only. It preserves the whole concept, adds detailed alarm/simulation behavior, enumerates existing seams and exposes missing evidence. It creates no task graph, model adapter, schema, timer, worker, provider account, service or demo change.

Changed-document relative-link, draft-status, fence-balance and whitespace checks passed; each draft companion is below 500 lines. `git diff --check` passed for tracked changes. The new documents were also read back for ownership, source-claim and scope errors; specified-only attention/correlation/closure/credential families were corrected rather than misreported as materialized JSON Schemas.

Revision 0.2.0 changed-document validation covered four files and 88 relative links, explicit incubating/version markers, fence balance, bounded size and secret-like credential patterns; it found no issues. Readback reviewed the new memory contract, source/claim distinctions and mathematical version boundaries. The portable memory profile and concurrent Wirebot memory-delivery document were not modified by this revision.

These checks are NOT the full repository/contract suite. The execution-host SSH route was reachable, but the governed regression dispatch failed and its read-only job-ledger reconciliation found no matching job; the suite therefore did not run. This is not a failed test and was not replaced with ungoverned/local heavy execution. No runtime, simulator, model or new memory evaluation is claimed. Historical no-paid-CI rehearsal remains historical; billing-denied Actions were not failed tests. Before implementation readiness, rerun applicable suites through an admitted execution route without paid CI.

Publication is documentation-only to the existing `Startempire-Wire/agent-driven-life-business-os` repository on `main`; branch/source presence is not installed runtime or proof that another agent loaded the revision. The publication commit and remote readback belong in the delivery receipt rather than a self-referential commit hash in these documents.

Next authorized activity remains source-grounded draft enrichment and reconciliation of this register—not implementation decomposition. A replacement agent should read the parent, annex and §6.1 handoff, verify current sources, preserve concurrent changes and continue resolving specification gaps within the same planning-only ceiling.
