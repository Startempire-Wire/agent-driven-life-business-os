# Composable AI Workforce Catalogue and Client Assignment Matrix

- **Status:** proposed reusable workforce-design baseline grounded in current Focusa/UIAI capabilities and operator-provided duty examples; profiles do not grant authority or prove deployment
- **Applies to:** new and existing Agent-Driven Life and Business OS clients
- **Execution substrate:** Focusa-governed work plus UIAI Engine browser/computer/evidence capabilities
- **Supervisor model:** one client-scoped Chief of Staff delegates to bounded workers through Workpoints, tasks, CallGraphs or approved recurring schedules
- **Product rule:** every first-party worker-facing capability remains API/CLI complete; computer-use automation (CUA) is last resort

## 1. Purpose

This catalogue turns the evolving Focusa and UIAI capability plane into reusable **AI employee profiles**. A client audit can select from a known workforce instead of guessing what agents should exist, what they may do, how long they should live, which tools they need or how their work is accepted.

The catalogue supports:

- **flash workers:** short-lived, task-bounded instances spun up when needed;
- **campaign workers:** checkpointed workers retained across a bounded project or remediation;
- **staff roles:** durable client-specific role contracts whose execution remains episodic and governed;
- **scheduled workers:** recurring instances launched by an approved scheduler;
- **specialist benches:** defined profiles that remain dormant until prerequisites and authority exist.

A profile is a template, not an employee instance, capability grant, schedule, task or architecture authority. Assignment requires a client-scoped employment packet, CRIST disposition, exact tools, data scope, acceptance evidence and supervisor.

## 2. Source and freshness model

This document derives its capability vocabulary from:

- Focusa Agent Card and live progressive tool discovery; inspected runtime version `0.9.192`;
- Focusa Spec 135/135B Professional Workspaces and CRIST Project Genesis;
- Focusa Silent Sessions, Work Loop, Workset, CallGraph, Workpoint, Trajectory, evidence, temporal, resource, lineage and metacognition contracts;
- UIAI Engine agent card, health/discovery, browser, source, diagnostics, screenshot, Evidence Share and FPV surfaces;
- the [Agent-Operation-Complete Software Contract](./07-agent-operation-complete-software-contract.md);
- the [ecosystem API/CLI parity audit](./08-wirebot-ecosystem-agent-operation-parity-audit.md).

Tool counts are deliberately not frozen. Focusa and UIAI registries evolve; “140+ tools” describes current scale, not a permanent contract. Every worker loads the smallest live-discovered bundle required for its assignment.

## 3. CRIST for every employee

Every employee instance carries a CRIST envelope:

1. **Context** — exact client, project, workstream, current state, evidence, privacy boundary and desired outcome.
2. **Role** — profile ID, responsibilities, supervisor, allowed tools/data, exclusions, budget and escalation path.
3. **Interview** — questions needed to resolve material ambiguity; it may be full, delta-only or explicitly waived for deterministic preapproved work.
4. **Spec** — outcome, scope, dependencies, acceptance, evidence, material rollback and delivery destination.
5. **Tasks** — dependency-ordered executable work with done conditions and failure paths.

### 3.1 CRIST depth

| Depth | Use | Interview behavior |
|---|---|---|
| Full | new client, new role, ambiguous/high-consequence mission, new data or system boundary | complete bounded interview before task compilation |
| Delta | known role applied to a new client/workstream or changed conditions | ask only unanswered client-specific questions |
| Inherited | ready task under an accepted project Spec/CallGraph | inherit verified CRIST packet; interview only on drift or contradiction |
| Deterministic recurring | approved monitor/report with stable inputs and no expanded consequence | no routine human interview; validate freshness, scope and stop conditions each run |

Every profile uses CRIST “to some degree”; no profile bypasses Context, Role, Spec or Tasks. Avoiding repetitive interviews is not permission to infer missing authority.

## 4. Worker lifetime and state model

| Code | Worker form | Typical duration | State posture | Activation |
|---|---|---|---|---|
| F | Flash | one bounded task or minutes/hours | stateless or receipt-only | on-demand Silent Session, ready task or event |
| S | Session | one working session | Workpoint/checkpointed | Silent Session or supervised interactive run |
| C | Campaign | days/weeks until one accepted outcome | checkpointed project state | task frontier, event or supervised schedule |
| P | Staff profile | indefinite role contract; execution remains episodic | client-scoped durable state in canonical stores | event, schedule, queue or on-demand delegation |
| E | Emergency | incident lifetime only | append-only evidence and recovery state | authorized alert/runbook trigger |

“Stateful employee” means state is stored in approved client/project systems with provenance, retention and revocation. It never means trusting a model transcript or leaving an uncontrolled process alive indefinitely.

### 4.1 Relationship to current Wirebot memory

**Operator-directed boundary:** stateful workers should use an architecture similar to Wirebot’s current state/Core Memory model. It is **TBD whether they share Wirebot’s actual stores or records**. No profile receives ambient access to the operator’s, manager’s, another worker’s or another client’s memory.

Current source/document evidence describes a layered model:

| Current layer | Observed responsibility | Evidence/status boundary |
|---|---|---|
| Context Core | deterministic current operator state, events, guidance and controlled actions | current `wb doctor` reports service/port active; not a worker-memory store by itself |
| OpenClaw native memory | workspace Markdown plus indexed retrieval | documented current model; current host reports local unit inactive and configured remote gateway reachable |
| Wirebot Memory Bridge | turn hooks, Mem0 fact extraction, Letta sync, `MEMORY.md`, wiki tools and audit | source exists; dependency health varies and does not prove end-to-end delivery |
| Scoreboard memory review/delivery | approval/correction queue and durable jobs to Mem0, `MEMORY.md`, fact YAML, Wiki and Letta | source/docs define retry, backoff, dead-letter and trace behavior; live full-path proof remains required |
| Mem0 | semantic recall | current host reports local service inactive and port 8200 closed |
| Letta | structured/long-term state and archival | current host reports local unit inactive but configured remote port reachable; reachability is not semantic health |
| Wiki/Agent-KB | source-aware durable knowledge | distinct from episodic worker memory and from architecture authority |
| Focusa | project/work governance: Trajectory, Workpoints, tasks, evidence, receipts and continuation | distinct from general personal/business memory |

Current `wb memory` also exposes a hardcoded single-operator namespace in CLI paths. Multi-client/stateful-worker architecture is therefore not operationally settled. Wirebot Core issue #33 tracks the required architecture and isolation work.

Before general activation, compare isolated per-worker stores, client-shared memory with role-scoped projections, manager-owned context for stateless crew, project/workstream partitions and federated retrieval. Define canonical ownership, write admission, approval, correction, confidence, retention, expiry, deletion, conflict resolution, migration and cross-tenant denial. Similar architecture does not imply shared storage.

## 5. Activation modes

| Mode | Mechanism | Suitable work | Hard boundary |
|---|---|---|---|
| On-demand | `focusa_silent_sessions` start/reopen with exact session/run scope | flash specialists, reviews, research, bounded implementation | profile and session do not grant task authority |
| Ready frontier | Workpoint/task/CallGraph eligible node | dependency-ordered project work | validated graph is not execution permission by itself |
| Work Loop | Focusa Work Loop under writer/budget controls | continuous progression across ready authorized tasks | never self-renews exhausted budget |
| Background job | `focusa_bg_run` / `focusa_bg_run_many` | builds, tests, scans, terminal-blocking work | accepted dispatch is not completion |
| Event-driven | approved webhook, queue event, evidence/health signal | intake, triage, receipt handling | event payload cannot mint authority |
| Scheduled | canonical client scheduler/cron launches a typed assignment | reports, health, reconciliations, maintenance | schedule is separate from Silent Sessions and must carry scope, budget and idempotency |
| Manual supervised | Chief of Staff or operator delegates one exact packet | sensitive/high-consequence work | confirmation and external consent remain explicit |

Focusa Silent Sessions currently expose lifecycle controls, not a blanket cron grant. A schedule invokes an approved assignment; it does not turn a dormant profile into an always-authorized employee.

## 6. Capability bundles

Profiles below reference these bounded bundles. Exact schemas are loaded through live discovery only when needed.

### 6.1 Focusa bundles

| ID | Capability family | Representative current tools |
|---|---|---|
| F-DISC | capability discovery | `focusa_agent_card`, `focusa_tool_search`, `focusa_tool_describe`, `focusa_tool_graph`, `focusa_tool_bundle` |
| F-SCOPE | identity/bootstrap/Genesis | `focusa_project_identity`, `focusa_project_verify`, `focusa_project_bootstrap`, `focusa_project_genesis`, `focusa_daemon_routing_status` |
| F-TRAJ | direction and gap | `focusa_north_star_gate`, `focusa_trajectory_view`, `focusa_hlt_history`, `focusa_trajectory_define_goal`, `focusa_trajectory_assess`, `focusa_trajectory_propose_workpoint` |
| F-WP | bounded action/continuation | `focusa_active_object_resolve`, `focusa_workpoint_checkpoint`, `focusa_workpoint_resume`, `focusa_workpoint_link_evidence`, `focusa_session_transfer` |
| F-FOCUS | concise operating state | `focusa_intent`, `focusa_current_focus`, `focusa_next_step`, `focusa_open_question`, `focusa_recent_result`, `focusa_constraint`, `focusa_failure`, `focusa_decide` |
| F-EXEC | governed execution | `focusa_workset_projection`, `focusa_callgraph_validate`, `focusa_callgraph_observe`, `focusa_bg_run`, `focusa_bg_run_many`, `focusa_bg_status`, `focusa_fast_forward` |
| F-LOOP | continuous work control | `focusa_work_loop_writer_status`, `focusa_work_loop_status`, `focusa_work_loop_context`, `focusa_work_loop_checkpoint`, `focusa_work_loop_select_next`, `focusa_work_loop_control` |
| F-SILENT | isolated worker lifecycle | `focusa_silent_sessions` status/start/reopen/tail/send/pause/resume/interrupt/restart/kill/config/receipt/capabilities |
| F-EVID | evidence and acceptance | `focusa_evidence_capture`, `focusa_workpoint_link_evidence`, `focusa_browser_diagnostics_intake`, `focusa_project_card_outcome` |
| F-CTX | bounded context | `focusa_context_cognition`, `focusa_context_cognition_render`, `focusa_context_cognition_curate`, `focusa_context_cognition_proof`, preload build/render/verify |
| F-TIME | temporal authority | `focusa_temporal_authority`, `focusa_hlt_history` |
| F-LEARN | prediction/metacognition | `focusa_predict_record`, `focusa_predict_recent`, `focusa_predict_evaluate`, `focusa_predict_stats`, metacog capture/retrieve/reflect/adjust/evaluate |
| F-LINEAGE | checkpoints and recovery | tree head/path/snapshot/diff/restore/recent helpers, `focusa_trajectory_checkpoint`, `focusa_trajectory_resume`, `focusa_session_transfer` |
| F-RESOURCE | resource and bloat control | `focusa_resource_mode`, Bloatgaurd reports/domains/profiles/routines, `focusa_traverse` |
| F-RUNTIME | instruction/runtime integrity | runtime effective/sources/conflicts/explain/simulate, constitution/prompt previews, artifact delivery/verify, instruction-integrity and amendment operations |
| F-SEC | credentials/device/communications | `focusa_credentials_verify`, device pairing/status/list/revoke, SMS health/enrollment/scoped thread/send/OTP/checkpoint/events/revoke |
| F-COCKPIT | whole-flywheel observation | `focusa_cockpit_projection`, Workset and CallGraph projections, background-job board |
| F-DX | diagnostics/recovery | `focusa_tool_doctor`, runtime doctor, DXUX report/requirement/explain/digest, state-hygiene doctor/plan/apply |
| F-BROWSER | governed UIAI bridge | `focusa_browser_workflow_plan`, `focusa_browser_capabilities_intake`, `focusa_browser_diagnostics_intake` |
| F-DOC | docs/call-stack conformance | `focusa_call_stack_design`, `focusa_call_stack_verify`, runtime/agent artifact preview and verification |

### 6.2 UIAI bundles

| ID | Capability family | Representative current tools |
|---|---|---|
| U-DISC | browser capability discovery | `pi_uiai_agent_card`, `pi_uiai_tool_search`, `pi_uiai_tool_graph`, `uiai_health`, `uiai_status` |
| U-RESEARCH | web/source research | `uiai_search`, `uiai_source_to_markdown`, research packet build/compose |
| U-SESSION | browser lifecycle | browser open/navigate/back/forward/resize/close, FPV share |
| U-READ | semantic page reading | browser read/text/snapshot/DOM/selector resolution |
| U-ACT | semantic browser actions | browser click/fill/type/select/press/hover/scroll/wait using supported semantic selectors or refs |
| U-DIAG | diagnostics | browser diagnostics/clear, engine errors, console/network/failed-request evidence |
| U-EVID | visual/evidence delivery | browser screenshot, one-shot screenshot, Evidence Share list/inspect/verify/resolve/settings |
| U-VISUAL | responsive/visual QA | screenshots, resize, scroll, CSS injection, frame catalogue/render |
| U-EVAL | bounded page evaluation | sync/async page evaluation for diagnostics or structured extraction |
| U-AUTH | renewable verification | `uiai_2fa_code` for an approved profile; never recovery codes and never ambient credential access |
| U-CUA | last-resort computer use | visual/coordinate/keyboard operation only after API/CLI and semantic interfaces are proven insufficient |

`U-ACT` is still secondary to a first-party API/CLI. `U-CUA` is the final fallback for external/legacy software and requires a recorded structured-interface gap.

### 6.3 Verbatim Focusa evidence for worker composition

The statements below are direct quotations, not rewritten product claims. They ground the proposed compositions while preserving the source’s own status: Spec 174 is explicitly a **concept**, and tool-registry entries describe available operation surfaces rather than client deployment.

#### Workforce and CRIST documentation

| Source | Direct quotation | Catalogue implication |
|---|---|---|
| Focusa Spec 174 lines 10–13 | “**The extension is a window, not the runtime** — agents live in the daemon(s), keep working when the browser closes, and the extension reconnects live over the daemon SSE stream.” | Workforce Composer UI must remain a client of the runtime. |
| Focusa Spec 174 lines 20–22 | “Agents ── instantiated from ──► Roles (= Objective + Capabilities + Secret Scopes + Model Tier + Budget + Lifespan)” | A profile must include more than a title or prompt. |
| Focusa Spec 174 lines 26–29 | “Stateful Managers: persistent memory via daemon awareness substrate; delegate, review, replan; survive browser close.” / “Stateless Crew: spawned per node via focusa bg/workloop machinery; expire on completion; cost-tracked per unit of work.” | Grounding for manager/crew and durable/flash distinctions. |
| Focusa Spec 174 lines 70–71 | “Design rule: every agent action is inspectable; every human touchpoint is a consent or a direction.” | Assignments require auditability and typed human checkpoints. |
| Focusa Spec 135B lines 34–41 | “Focusa C.R.I.S.T. Context → Role → Interview → Spec → Tasks” | Every employee uses a CRIST disposition. |
| Focusa Spec 135B line 161 | “No approved role, spec, or task plan may be silently rewritten by new context.” | New evidence triggers amendment/review, not hidden profile mutation. |
| Focusa Spec 135B lines 170–176 | “Project corpus ≠ turn prompt” and “Each action receives only the relevant, scoped, permission-safe projection.” | Stateful work uses canonical stores and bounded context, not transcript memory. |
| Focusa Spec 135 lines 227–230 | “Canonical runtime Owns ProjectIdentity, exact scope, reducer state, Trajectory, Workpoints, tasks, capabilities, permissions, Evidence, Receipts, sessions, proposals, conflict resolution, recovery, and event history.” | The future UI must not create a parallel authority store. |
| Focusa Spec 135 line 258 | “Every stage MUST be implemented as real-time generated plain-language UI.” | Workforce configuration must remain understandable to non-specialists. |

#### Live Focusa tool-registry quotations

Observed through `focusa_tool_describe` on 2026-09-13:

| Tool | Direct `purpose` quotation | Used by |
|---|---|---|
| `focusa_project_genesis` | “Stage, resume, inspect, or atomically commit the verified project journey from HLT and specification through tasks, first Workpoint, coordination, and readiness receipt.” | CRIST/onboarding and project-assignment workers |
| `focusa_silent_sessions` | “Thin daemon-native Spec133 API client for exact session/run status, bounded observation, steering, controls, config, receipts, capabilities, and legacy action compatibility; process-control failures return failure_class=process_control_failed with receipt-backed recovery.” | isolated flash/session execution |
| `focusa_workpoint_checkpoint` | “Create a typed Focusa Workpoint checkpoint before compaction, resume, context overflow, model switch, or risky continuation. Use this instead of trusting raw transcript memory; Focusa becomes the canonical continuation source and returns an explicit next-step hint.” | all checkpointed/stateful workers |
| `focusa_callgraph_validate` | “validating a CallGraph definition deterministically before any create or dispatch action.” | planner/foreman/dispatcher profiles |
| `focusa_bg_run` | “Dispatch one terminal-blocking command through `focusa bg run --detach` and report success only with a durable job receipt.” | engineering, test, release and scan workers |
| `focusa_evidence_capture` | “Capture a bounded evidence ref/result and optionally link it to the active Workpoint.” | evidence and outcome profiles |
| `focusa_context_cognition_curate` | “Spec 100 Phase 3 — token-budgeted context selection. Ranks candidates by workpoint target + evidence overlap and selects the highest-scoring subset under a token budget.” | research, specification and knowledge workers |
| `focusa_temporal_authority` | “Read, commit, revise, observe, forecast, or preflight scoped temporal claims with evidence, confidence, uncertainty, freshness, and no fabricated urgency.” | scheduling, commitment and report workers |
| `focusa_metacog_retrieve` | “Best safe search tool for past learning signals relevant to the current ask. Use this before planning or reflection.” | learning and quality workers |
| `focusa_browser_workflow_plan` | “Plan a governed UIAI/WebMCP read, action, diagnostics, evidence, and cleanup sequence.” | browser, UX and acceptance workers |

#### Code-level boundary quotations

- `crates/focusa-cli/src/commands/workset.rs:18`: “Read the deterministic replay projection.”
- `crates/focusa-api/src/routes/credentials.rs:3-5`: “Secret-free by construction: the route never sees or returns secret values — only requirement verdicts, grant lifecycle states, and redacted provider descriptors.”
- `crates/focusa-core/src/credential_authority.rs:5-7`: “model/public projections carry NO account identifier and NO secret value — agents request ROLES, never vault item names or raw values unless the operator deliberately permits it.”

These implementation quotations constrain workforce composition alongside the live schemas and specifications.

### 6.4 Required per-assignment tool evidence

Before a profile can be assigned, the Workforce Composer/compiler must collect—not paraphrase—the current source language for every selected tool:

```yaml
schema_version: workforce.tool-evidence.v1
tool_name: exact-live-tool-name
registry_version: exact-observed-version
direct_purpose_quote: verbatim-registry-description
source_refs:
  - exact-doc-or-code-reference
api_routes: []
cli_commands: []
side_effect_profile: exact-live-value
scope_requirement: exact-live-value
authority_requirement: exact-live-value
verification_status: verified | blocked | unavailable
verified_at: rfc3339-time
evidence_issue_refs: []
```

The source quotation is evidence of advertised intent, not proof of correctness. Compare it with schemas, applicable Focusa specs and implementation for consequential assignments. `blocked` or `unavailable` prevents automatic activation of the affected capability; it does not license the composer to invent semantics. The full 140-plus-tool registry should be generated from progressive discovery rather than manually frozen in this document.

### 6.5 Golden Path toolchain assignment

The current `substrate-bootstrap.sh` baseline inventories 16 components. Its contract is conservative: base primitives may be installed only through explicit confirmed Base Apply; non-base components remain route-only. Presence never grants a worker authority.

| Golden Path tool | Canonical function | Eligible profiles | Typical task packs/work | Assignment boundary |
|---|---|---|---|---|
| `git` | source history and collaboration | REC-01, ENG-01, DOC-01, REL-01 | repository reconnaissance, implementation, documentation, release | exact repository/branch; no destructive history operations |
| `curl` | bounded HTTP/API diagnostics | API-01, INT-01, TST-01, HLT-01 | endpoint discovery, contract and health checks | never substitutes for auth, typed clients or browser pixel proof |
| `python3` | scripts, validators and data transformation | ENG-01, TST-01, REC-01, REL-01, TLS-01 | audits, schema tests, migrations and release checks | reviewed bounded script; no secret output or broad rewrites |
| `node` | JavaScript/TypeScript runtime | ENG-01, TST-01, EXT-01, VIS-01, REL-01 | web/extension build, test and tooling | project-pinned versions and exact package boundary |
| `npm` | Node package/build command surface | ENG-01, TST-01, EXT-01, REL-01, TLS-01 | install from approved lockfile, build and test | dependency installation requires explicit project authority |
| `pi` | reference coding-agent harness | ENG-01, REC-01, SPC-01, CGP-01 | scoped engineering and specification sessions | harness access is not project/tool authority |
| `focusa` | governance, work, evidence and continuation | all governed profiles; especially COS-01, FRM-01, DSP-01, AUT-01, EVD-01 | CRIST, Workpoints, execution, evidence, receipts and recovery | exact project/continuity/Workpoint and live tool evidence |
| `rbw` | approved vault retrieval adapter | SEC-01, CRED-01, SET-01 | exact credential-role fulfillment | exact approved field only; no vault enumeration or raw secret narration |
| `gh` | GitHub repository/issue/release interface | REC-01, ENG-01, DOC-01, REL-01, SUP-01 | issue triage, source collaboration and approved release paths | existing approved auth/repository; no repo/visibility/branch expansion |
| `wrangler` | Cloudflare developer/edge CLI | DEP-01, REL-01, INT-01, SEC-01 | approved worker/site deployment and diagnostics | exact account/zone/project grant; DNS mutation is consequential |
| `gog` | Google workspace adapter | EAA-01, TMP-01, COM-01, KB-01, ONB-01 | mail, calendar, documents and collaboration | exact account/service scopes; current missing account remains unavailable |
| `bd` | project-local Beads task ledger | FRM-01, DSP-01, ENG-01, SUP-01 | task readiness, dependencies, assignment and closure | project-local only; task provenance is not architecture authority |
| `tailscale` | approved private network/transport | HLT-01, RCV-01, VER-01, SEC-01, DEP-01 | device reachability, private service routing and recovery | transport never grants service/data authority |
| `agent-kb` | canonical source-aware knowledge retrieval | KB-01, RES-01, INV-01, DOC-01, COS-01 | policy/runbook/topology research | bootstrap → freshness → search → direct document; no raw-store hot path |
| `openclaw` | Wirebot/Chief-of-Staff runtime | COS-01, DSP-01, SET-01, CST-01, VER-01 | assistant runtime, channels, skills and delegated work | client identity, tier, channel, skill and memory scope required |
| `uiai` | UIAI Engine CLI/runtime entry | BRW-01, UXA-01, VIS-01, ACC-01, RES-01, EVD-UI-01 | browser research/action, diagnostics and visual evidence | UIAI-first workflow; API/CLI first-party routes precede browser/CUA |

Additional installed tools—including `wb`, WordPress/WP-CLI adapters, Guardian, container engines, platform CLIs, databases, media tools and customer business systems—must enter the same inventory before assignment. The Golden Path audit emits the actual per-machine set; the catalogue must never infer availability from this baseline.

Each inventory row must record component/version, source/manager, install stage, owning product, health, platform, API/CLI operations, consequence class, credentials, data scopes, eligible/prohibited profiles, task packs, upgrade/rollback and evidence receipts. New tools remain unassigned until this mapping is complete.

## 7. Master workforce profile grid

In compact bundle cells, a prefix applies across slash-separated names until a comma; for example, `F-DISC/SCOPE/TRAJ, U-READ/EVID` means `F-DISC`, `F-SCOPE`, `F-TRAJ`, `U-READ` and `U-EVID`.

### 7.1 Executive, coordination and governance

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| COS-01 | Client Chief of Staff | synthesize client state, prioritize, delegate, observe receipts, escalate exceptions | F-DISC/SCOPE/TRAJ/WP/COCKPIT/CTX/TIME/EVID | Full then Delta | P/stateful | event, queue, supervised | conditional |
| EAA-01 | Executive Administrative Assistant | coordinate communications, schedules, meetings, documents, reports, follow-up and approved administrative task packs | F-CTX/TIME/SEC/EVID/WP, U-RESEARCH | Full then Delta | P/stateful | event, queue, scheduled | yes |
| FRM-01 | Project Foreman | manage one project from accepted trajectory through Workpoints and evidence | F-SCOPE/TRAJ/WP/EXEC/LOOP/EVID | Full or Inherited | P/checkpointed | ready frontier, Work Loop | conditional |
| DSP-01 | Workforce Dispatcher | match ready work to approved employee profiles and available execution lanes | F-COCKPIT/EXEC/SILENT/LOOP | Inherited | P/stateful roster | event/queue | yes |
| CRI-01 | CRIST Interviewer | gather missing Context/Role/Interview facts and produce bounded handoff | F-SCOPE/TRAJ/CTX/WP | Full/Delta | F/stateless | on-demand | no |
| SPC-01 | Specification Compiler | turn accepted intent into outcome, scope, dependencies, acceptance and rollback | F-CTX/TRAJ/DOC/WP | Full/Delta | S/checkpointed | on-demand | no |
| CGP-01 | CallGraph Planner | decompose approved work into dependency/evidence/failure graph | F-DOC/EXEC/WP/TRAJ | Inherited | F/stateless | on-demand | no |
| AUT-01 | Authority and Scope Steward | verify principal, project, grants, consequence class and scope before action | F-SCOPE/RUNTIME/SEC/WP | Delta | P/stateful policy refs | event/preflight | yes |
| ENT-01 | Entitlement and Consent Clerk | reconcile contract/payment/entitlement/consent state without duplicating approval | F-SEC/EVID/TIME/WP | Delta | P/stateful ledger refs | event/supervised | yes |
| TMP-01 | Temporal Coordinator | maintain verified commitments, windows, forecasts and stale-state handling | F-TIME/TRAJ/EVID | Delta/Deterministic | P/stateful | event/scheduled | yes |
| BGT-01 | Budget and Capacity Steward | observe turns/time/resources and prevent silent budget renewal | F-LOOP/RESOURCE/COCKPIT/TIME | Deterministic | P/stateful metrics | scheduled/event | yes |

### 7.2 Discovery, research and knowledge

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| RES-01 | Web Research Analyst | answer evidence-backed questions from public sources | U-DISC/RESEARCH/READ, F-CTX/EVID | Delta | F/stateless | on-demand | no |
| SRC-01 | Source Conversion Librarian | convert approved URLs/documents into bounded Markdown/evidence records | U-RESEARCH, F-EVID/CTX | Deterministic | F/receipt-only | event/batch | yes |
| CMP-01 | Competitive Intelligence Analyst | compare competitors, capabilities, pricing claims and market evidence | U-RESEARCH/READ/EVID, F-CTX/TIME | Full/Delta | C/checkpointed | campaign/scheduled | conditional |
| KB-01 | Knowledge Curator | deduplicate, classify, refresh and route canonical client knowledge | F-CTX/EVID/LEARN/TIME | Delta/Deterministic | P/stateful | event/scheduled | yes |
| OPP-01 | Opportunity Scout | identify bounded opportunities and submit evidence-backed candidates | U-RESEARCH/READ, F-LEARN/TIME/EVID | Delta/Deterministic | P/stateful candidates | scheduled | yes |
| INV-01 | Existing-System Inventory Auditor | catalogue software, accounts, workflows, ownership, health and unknowns | F-SCOPE/CTX/EVID, U-READ/DIAG | Full/Delta | C/checkpointed | audit campaign | conditional |
| FRESH-01 | Freshness and Drift Auditor | compare current runtime/source/docs against prior accepted state | F-TIME/EVID/DX/LINeAGE/CTX | Deterministic | F/receipt-only | scheduled/event | yes |
| DOC-01 | Documentation Steward | reconcile behavior, API/CLI contracts, runbooks and references | F-DOC/CTX/EVID, U-RESEARCH | Inherited | C/checkpointed | ready task/scheduled review | conditional |

### 7.3 Product, UX and browser quality

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| PRD-01 | Product Surface Auditor | inventory product UIs, source owners, dependencies, status and overlap | F-CTX/EVID/DOC, U-READ/VISUAL | Full/Delta | C/checkpointed | audit campaign | no |
| UXA-01 | UX Journey Auditor | verify complete customer/operator journeys and identify friction | U-SESSION/READ/ACT/DIAG/EVID, F-BROWSER/EVID | Delta | S/checkpointed | on-demand | conditional |
| A11Y-01 | Accessibility Specialist | inspect semantic trees, keyboard flow, labels, focus and contrast evidence | U-READ/ACT/VISUAL/DIAG, F-EVID | Delta | F/stateless | on-demand/batch | yes |
| VIS-01 | Visual QA Specialist | verify rendered pixels, responsive layouts and regression evidence | U-SESSION/VISUAL/EVID/DIAG, F-EVID | Inherited | F/receipt-only | build/event | yes |
| BRW-01 | Structured Browser Operator | perform browser-only workflows using semantic refs after API/CLI discovery | F-BROWSER/SEC/EVID, U-DISC/SESSION/READ/ACT/DIAG | Delta | S/checkpointed | on-demand | no |
| CUA-01 | Legacy CUA Specialist | operate an external legacy UI only when structured routes are unavailable | F-BROWSER/SEC/EVID/WP, U-SESSION/DIAG/EVID/CUA | Full/Delta | F/receipt-only | manual supervised | no |
| EVD-UI-01 | Evidence Share Reviewer | inspect, verify and resolve screenshots/EPWA/FPV packets | U-EVID/READ, F-EVID | Inherited | F/stateless | event/queue | yes |
| EXT-01 | Browser Extension QA Specialist | verify install, permissions, message contracts, origins and revocation | U-SESSION/READ/ACT/DIAG/EVID, F-SEC | Delta | C/checkpointed | release candidate | conditional |
| CHR-01 | Veragensia Chromebook UX Tester | prove all portfolio UIs on qualified hardware with resource and pixel evidence | U-VISUAL/EVID/DIAG, F-RESOURCE/EVID/EXEC | Full/Inherited | C/checkpointed | release campaign | no |

### 7.4 Engineering, API/CLI and release

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| REC-01 | Repository Reconnaissance Engineer | identify exact repository, owner, worktree, instructions and existing implementation | F-SCOPE/CTX/LINEAGE/DISC | Delta | F/stateless | on-demand | no |
| ENG-01 | Bounded Implementation Engineer | implement one accepted dependency slice and verify it | F-WP/EXEC/EVID/LINeAGE/DOC | Inherited | S/checkpointed | ready task/Silent Session | no |
| TST-01 | Test Engineer | design/run producer, consumer, integration and regression checks | F-EXEC/EVID/DOC | Inherited | F/receipt-only | ready task/build event | yes |
| PAR-01 | API/CLI Parity Engineer | map UI actions to canonical operations and prove API/CLI/UI/agent parity | F-DISC/DOC/EVID/EXEC, U-READ | Full/Inherited | C/checkpointed | audit/ready task | conditional |
| INT-01 | Integration Contract Engineer | version cross-product identity, capability, evidence and revocation adapters | F-DOC/SCOPE/EVID/RUNTIME | Full/Inherited | C/checkpointed | ready task | no |
| REL-01 | Release Engineer | execute only the canonical release chain and collect terminal receipts | F-EXEC/WP/EVID/TIME | Inherited | S/checkpointed | authorized release | no |
| DEP-01 | Deployment Engineer | install/configure approved release on exact destination | F-EXEC/SCOPE/EVID/SEC | Full/Inherited | S/checkpointed | authorized delivery | no |
| ACC-01 | Consumer Acceptance Tester | verify installed behavior on exact customer/operator surface | F-EVID/WP, U-SESSION/READ/ACT/DIAG/EVID | Inherited | F/receipt-only | post-deploy | no |
| API-01 | Operation Catalogue Curator | maintain product-owned operations and federated discovery projection | F-DISC/DOC/RUNTIME/EVID | Full/Inherited | P/stateful registry | ready task/scheduled audit | conditional |
| WPA-01 | WordPress Domain Adapter Engineer | expose existing WordPress-owned business functions through versioned app-ready operations | F-DOC/SCOPE/EVID, U-DIAG | Full/Inherited | C/checkpointed | ready task | no |
| FED-01 | Federation Contract Engineer | design and verify minimum cross-node identity, capability, projection and revocation contracts | F-DOC/SEC/EVID/RUNTIME | Full | C/checkpointed | ready task | no |

### 7.5 Infrastructure, security and recovery

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| HLT-01 | Runtime Health Monitor | observe health/readiness, classify drift and create bounded alerts | F-DX/COCKPIT/TIME/EVID | Deterministic | P/stateful metrics | scheduled/event | yes |
| INC-01 | Incident Triage Responder | preserve evidence, bound impact, diagnose and route approved recovery | F-DX/EVID/LINEAGE/SCOPE/SEC | Full/Delta | E/checkpointed | alert/manual | conditional |
| RCV-01 | Recovery Engineer | execute approved retry/repair/rollback and prove restored acceptance | F-DX/EXEC/LINeAGE/EVID | Inherited | E/checkpointed | incident frontier | no |
| SEC-01 | Security and Authentication Steward | verify renewable auth, least capability, revocation and sensitive boundaries | F-SEC/RUNTIME/EVID | Full/Delta | P/stateful policy refs | preflight/event | yes |
| CRED-01 | Credential Grant Verifier | return secret-free grant satisfaction before provider seams | F-SEC | Deterministic | F/stateless | preflight | no |
| DEV-01 | Device Pairing Specialist | pair/list/revoke devices with exact scope and receipts | F-SEC/EVID | Delta | F/receipt-only | on-demand | no |
| SMS-01 | Scoped Communications/OTP Broker | health, exact thread/send or renewable OTP injection under separate grants | F-SEC/EVID | Full/Delta | F/receipt-only | event/manual | no |
| RESRC-01 | Resource Performance Steward | monitor memory/token/bloat pressure and apply approved resource posture | F-RESOURCE/DX/EVID | Deterministic | P/stateful metrics | scheduled/event | yes |
| BCK-01 | Checkpoint and Continuity Steward | checkpoint, resume, transfer and verify continuation state | F-WP/LINEAGE/EVID | Inherited | P/stateful refs | event/threshold | yes |
| TLS-01 | Golden Path Toolchain Steward | inventory, verify, map, upgrade and revoke installed tools without granting ambient use | F-DISC/SCOPE/EVID/DX | Full/Delta | P/stateful inventory | onboarding/event/scheduled | yes |
| VER-01 | Veragensia Agent Computer Steward | manage qualified device capabilities, operation registry and governed execution handoffs | F-SCOPE/SEC/EVID/RESOURCE/BROWSER | Full | P/stateful device refs | event/supervised | conditional |

### 7.6 Customer lifecycle and business operations

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| DSC-01 | Client Discovery Analyst | inventory desired outcomes, systems, constraints and candidate workforce | F-SCOPE/CTX/TRAJ, U-RESEARCH | Full | C/checkpointed | onboarding | no |
| GPA-01 | Golden Path Audit Specialist | run safe brownfield/fresh audit and convert gaps into assignment candidates | F-SCOPE/EVID/EXEC/CTX | Full/Delta | C/checkpointed | onboarding/review | conditional |
| ONB-01 | Client Onboarding Coordinator | sequence contract, access, audit, setup, verification and handoff | F-SCOPE/TRAJ/WP/EVID/TIME | Full | C/stateful workflow | event/queue | conditional |
| ROS-01 | Client Roster Designer | select required staff, flash bench, schedules and exclusions from verified gaps | F-CTX/TRAJ/DOC/EVID | Delta | C/checkpointed | post-audit | no |
| SET-01 | Full AITL Setup Specialist | execute accepted remote setup scope and collect acceptance evidence | F-SCOPE/WP/EXEC/EVID/SEC | Full/Inherited | C/checkpointed | paid entitlement | no |
| CST-01 | Customer Success Monitor | observe outcomes, exceptions, adoption and unresolved support needs | F-COCKPIT/TIME/EVID/LEARN | Delta/Deterministic | P/stateful | scheduled/event | yes |
| OFF-01 | Offer and Pricing Readiness Analyst | reconcile offer scope, implementation, checkout, contract and claims before changes | F-CTX/EVID/TIME, U-RESEARCH/READ | Full/Delta | C/checkpointed | campaign | no |
| PAY-01 | Invoice/Payment/Scheduling Clerk | observe accepted contract/payment and manage typed scheduling/workspace handoff | F-SEC/TIME/EVID/WP | Full/Inherited | P/stateful ledger refs | event | conditional |
| COM-01 | Client Communications Coordinator | prepare/send approved scoped updates and retain delivery receipts | F-SEC/EVID/TIME | Delta | P/stateful preferences | event/scheduled | yes |
| SUP-01 | Support Triage Specialist | classify client reports, reproduce, route owning specialist and track acceptance | F-DX/CTX/EVID/WP | Delta | P/stateful cases | event/queue | yes |

### 7.7 Evidence, outcomes and learning

| ID | Employee profile | Primary outcome/task set | Bundles | CRIST | Life/state | Activation | Cron |
|---|---|---|---|---|---|---|---|
| EVD-01 | Evidence Clerk | capture bounded proof handles and link them to exact work | F-EVID/WP | Inherited | F/receipt-only | event/queue | yes |
| OUT-01 | Outcome Evaluator | compare accepted result with prediction/spec and settle truthfully | F-EVID/LEARN/TRAJ | Inherited | F/receipt-only | completion event | yes |
| PRDCT-01 | Prediction Analyst | record bounded forecasts and evaluate calibration after outcomes | F-LEARN/TIME/EVID | Delta/Deterministic | P/stateful metrics | event/scheduled | yes |
| META-01 | Metacognition Coach | retrieve lessons, reflect on failures and propose measurable adjustments | F-LEARN/EVID/CTX | Delta | P/stateful signals | scheduled/milestone | yes |
| QLT-01 | Completion/False-Green Auditor | verify source/release/install/UI/browser distinctions and remaining work | F-EVID/DX/COCKPIT/WP | Inherited | F/stateless | completion gate | yes |
| RCP-01 | Receipt Reconciliation Clerk | reconcile dispatch, completion, duplicate and partial-failure receipts | F-EVID/EXEC/COCKPIT | Deterministic | P/stateful ledger refs | event/scheduled | yes |

## 8. Generic task-pack library

A role describes responsibility; a **task pack** describes repeatable work. Clients compose an employee from one role plus only the task packs they actually need. Customer-specific names, accounts, vendors and procedures live in a private assignment overlay, not the portable catalogue.

### 8.1 OCDD administrative lens

The example Executive Administrative Assistant duties can be organized using **OCDD**:

- **Optimization:** reduce waste, waiting, duplication and avoidable human handling;
- **Communication:** prepare, route, send and follow up through approved channels;
- **Documentation:** capture source, decisions, minutes, files, reports and receipts;
- **Decentralization:** delegate work to the canonical owner while preserving coordination and accountability.

OCDD is a useful tag/lens for administrative task packs. It does not replace CRIST, product ownership or authority.

### 8.2 Task-pack grid

| ID | Generic task pack | Typical inputs | Required output/acceptance | Default profiles | Activation | Consequence notes |
|---|---|---|---|---|---|---|
| TP-CONTENT-01 | Newsletter production | approved content, audience, template, assets, schedule | reviewed issue, delivery preview, approved send and receipt | EAA-01, DOC-01, COM-01 | campaign/scheduled | publication/send requires approval and channel grant |
| TP-SOCIAL-01 | Social channel publishing | approved content calendar, assets, platform policy | scheduled/published posts and delivery evidence | EAA-01, COM-01 | scheduled/event | no autonomous engagement manipulation or policy-violating growth automation |
| TP-SOCIAL-02 | Social monitoring and response triage | scoped channels, keywords, response policy | categorized signals, drafts and escalations | CST-01, COM-01, OPP-01 | scheduled/event | drafts are not sends; sensitive responses escalate |
| TP-EDITORIAL-01 | Editorial and transcription quality | draft article, transcript, book or presentation | corrections, factual/source gaps, graphic-example requests and acceptance checklist | DOC-01, QLT-01 | on-demand | author/editor owns final publication |
| TP-HIRING-01 | Workforce systems onboarding | accepted hire record, role, systems, access policy | scoped account invitations, checklist and receipts | ONB-01, AUT-01 | event | account creation/access mutation requires exact authorization |
| TP-PROJECT-01 | Project tracker administration | approved projects/tasks, role roster, priorities | categorized tasks, owners, dependencies and current status | EAA-01, FRM-01, DSP-01 | event/scheduled | tracker never becomes architecture authority |
| TP-FOLLOWUP-01 | Team follow-up coordination | assignments, due windows, escalation policy | reminders, responses, blockers and escalation record | EAA-01, COM-01 | scheduled/event | avoid surveillance and fabricated urgency |
| TP-RESEARCH-01 | Product and process research | question, constraints, source policy | evidence-backed options and recommendation | RES-01, CMP-01 | on-demand/campaign | research is advisory until authorized |
| TP-OPPORTUNITY-01 | Local/market opportunity scouting | geography, business goals, exclusions | ranked opportunities with source/freshness | OPP-01 | scheduled | no outreach without separate authority |
| TP-CUSTOMER-01 | Customer information response | verified inquiry, approved knowledge, channel | accurate draft/send, provenance and delivery receipt | EAA-01, COM-01, SUP-01 | event | customer send and promises are external commitments |
| TP-MEETING-01 | Meeting preparation | attendees, objectives, prior actions, data sources | agenda, pre-read, reports and open decisions | EAA-01, TMP-01 | event/scheduled | private scope and minimum disclosure |
| TP-MEETING-02 | Meeting minutes and follow-through | authorized recording/notes, attendance, decisions | minutes, decisions, tasks, owners and follow-up | EAA-01, EVD-01, FRM-01 | event | recording/transcription requires consent and retention policy |
| TP-REPORT-01 | Recurring operating report | approved analytics, traffic, staff, finance, marketing and time sources | sourced report, anomalies and action candidates | EAA-01, CST-01, HLT-01 | scheduled | unavailable data remains unknown; financial claims require authoritative source |
| TP-INBOX-01 | Inbox triage | scoped mailbox, classification/retention rules | categorized inbox, drafts, escalations and audit | EAA-01, SUP-01 | scheduled/event | default quarantine/label, not permanent deletion; separate send grant |
| TP-CALENDAR-01 | Calendar administration | approved calendars, preferences, commitments | created/updated events, conflict checks and receipts | EAA-01, TMP-01 | event/scheduled | external invitations and cancellations require policy/confirmation |
| TP-EVENT-01 | Event and speaking opportunity coordination | event criteria, geography, availability, materials | candidate list, outreach drafts, schedule options | EAA-01, OPP-01, COM-01 | campaign | outreach and booking are external commitments |
| TP-AUTOMATION-01 | Autoresponder and lead-flow administration | approved copy, segments, trigger rules | configured preview/test, activation receipt and rollback | EAA-01, INT-01, TST-01 | campaign | activation changes customer communications |
| TP-FILES-01 | Document and file stewardship | scoped repository, taxonomy, retention rules | organized index, moves/copies with receipts, unresolved duplicates | KB-01, EAA-01 | on-demand/scheduled | no deletion of unknown files; preserve ownership and provenance |
| TP-CRM-01 | CRM/contact data stewardship | authorized records, field schema, source rules | validated updates, duplicates and provenance report | EAA-01, KB-01 | event/scheduled | personal data minimization and exact tenant scope |
| TP-TRAVEL-01 | Travel research and booking | preferences, dates, budget, identity/loyalty refs | compared options; confirmed booking only after approval | EAA-01, RES-01 | on-demand | purchase/booking is high-consequence external commitment |
| TP-PROCURE-01 | Approved purchasing and gifts | recipient/purpose, budget, vendor policy | options; approved order and receipt | EAA-01 | on-demand | payment, address and purchase require explicit confirmation |
| TP-PRESENT-01 | Presentation production | audience, message, evidence, brand assets | reviewed deck, source manifest and export | DOC-01, VIS-01, EAA-01 | campaign | claims and third-party media require verification/rights |
| TP-ANALYTICS-01 | Basic business reporting | authorized sales, delivery, task and marketing data | reconciled dashboard/report and anomalies | EAA-01, CST-01, OUT-01 | scheduled | source freshness and calculation definition must remain visible |
| TP-TOOLS-01 | Golden Path toolchain onboarding/lifecycle | approved machine profile, actual inventory, platform, owner and install authority | installed-or-routed component, version/health proof, profile assignments, rollback/revoke record | TLS-01, SET-01, SEC-01, TST-01 | onboarding/event | install only through approved owner route; presence and login never grant use |
| TP-ADAPTER-01 | Client business-system adapter onboarding | approved system, tenant, operations, data and credential-role requirements | versioned adapter mapping, least-capability grant, tests and revocation path | INT-01, API-01, TLS-01, SEC-01 | campaign | customer system remains canonical owner; no screen scraping for first-party integrations |

### 8.3 Genericization map from specific duty lists

| Specific source pattern | Portable catalogue representation | Private client overlay |
|---|---|---|
| named person supplies copy/images or sends | content owner, designer, publication coordinator | actual people, approvals and handoff order |
| named project/chat/file/social vendor | project tracker, team chat, file store or social scheduler adapter | tenant, workspace, account and provider configuration |
| named email address or calendar | inbox/calendar administration | exact mailbox/calendar grant and preferences |
| “follow/like/grow” automation | social monitoring and approved engagement policy | platform rules and allowed actions; prohibited by default when unclear |
| delete junk/newsletters | inbox classification and retention | quarantine, unsubscribe and deletion policy |
| customer replies/thank-yous | customer information response | approved templates, promise limits and send authority |
| reports for weekly meeting | recurring operating report + meeting preparation | exact sources, metrics, cadence and audience |
| hotel, flight or gift purchase | travel/procurement task pack | budget, traveler/recipient, payment and explicit confirmation |
| task assignment/check-ins | project tracker administration + follow-up coordination | team roles, escalation windows and systems |

## 9. Client assignment matrix

After the Golden Path audit, classify every profile for that client:

| Assignment state | Meaning |
|---|---|
| Required staff | recurring role directly tied to a verified ongoing outcome |
| Scheduled worker | stable recurring task with approved inputs, timing, budget and stop conditions |
| On-demand bench | approved profile available for delegation when a matching task becomes ready |
| Pilot candidate | useful hypothesis requiring one bounded evidence-producing trial |
| Conditional | valuable only after named integration, data, authority or product gap closes |
| Blocked | required but currently prevented by one exact hard gate |
| Excluded | unnecessary, duplicative, prohibited or outside client scope |
| Unknown | audit evidence is insufficient; do not guess |

### 9.1 Selection dimensions

Score fit qualitatively before assignment:

1. client outcome advanced;
2. verified work frequency and volume;
3. task repeatability and stability;
4. API/CLI and data readiness;
5. consequence/privacy class;
6. human judgment and relationship sensitivity;
7. evidence and acceptance measurability;
8. state/retention requirements;
9. schedule/event reliability;
10. economics and attention saved;
11. overlap with existing human/system owner;
12. Chromebook/Veragensia compatibility where applicable.

A high automation score does not override consent, authority or human-reserved work.

### 9.2 Default assignment algorithm

1. Read verified audit gaps, active goals, systems, task history and owner constraints.
2. Group repeated work by outcome and canonical owner.
3. Match groups to existing profiles before proposing a new role.
4. Choose the shortest lifetime and least state needed.
5. Choose the smallest capability bundle and data scope.
6. Run Full or Delta CRIST for unresolved client-specific facts.
7. Pilot with one flash/session worker where risk or value remains uncertain.
8. Measure accepted outcome, reliability, cost, attention saved and escalation quality.
9. Promote to campaign/staff/scheduled status only after repeatable proof.
10. Remove or merge roles that duplicate work or fail to create value.

## 10. Client Workforce Roster Manifest

Each client receives a private, versioned manifest. Example shape:

```yaml
schema_version: client.workforce-roster.v1
client_ref: canonical-private-client-ref
revision: 1
chief_of_staff_profile: COS-01
roles:
  - profile_id: GPA-01
    assignment: scheduled_worker
    supervisor_profile_id: COS-01
    lifetime: staff_profile
    execution_instances: episodic
    state_posture: client_scoped_canonical
    activation:
      modes: [scheduled, on_demand]
      schedule_ref: private-approved-schedule-ref
      event_refs: []
    task_set_refs: [client-golden-path-audit]
    capability_bundle_ids: [F-SCOPE, F-EVID, F-EXEC, F-CTX]
    authority_grant_refs: [private-grant-ref]
    data_scope_refs: [private-data-scope-ref]
    crist_packet_ref: private-crist-ref
    acceptance_refs: [private-acceptance-ref]
    budget_ref: private-budget-ref
    escalation_ref: private-escalation-ref
    status: conditional
    blocker_refs: [missing-client-receiver]
```

The shared catalogue contains no client secrets or personal data. The private roster references canonical client-scoped records.

## 11. Scheduling policy

A role is cron-eligible only when:

- inputs and scope are deterministic;
- the client has approved the cadence and resource budget;
- duplicate runs are idempotent or safely reconciled;
- credentials are renewable and available through approved grants;
- failures produce visible typed alerts;
- no recurring external commitment occurs without required confirmation;
- state retention and evidence policies are explicit;
- missed-run, overlap, retry, pause and revoke behavior are defined.

Use event-driven activation instead of polling where reliable events exist. Use scheduled observation plus exception escalation rather than continuous agent processes. Permanent staff profiles should usually wake episodically.

## 12. Chief-of-Staff supervision contract

The Chief of Staff:

1. maintains the client roster and current outcome priorities;
2. delegates only matching ready work under exact authority;
3. selects flash, campaign, scheduled or staff execution posture;
4. supplies the minimum CRIST/context packet;
5. observes progress and receipts without micromanaging implementation;
6. pauses/revokes workers on drift, budget exhaustion or correction;
7. routes consequential decisions to the owner;
8. measures outcomes and promotes/removes profiles based on evidence;
9. prevents two employees from silently owning the same canonical concern;
10. never converts broad awareness into broad execution authority.

Workers report to the Chief of Staff operationally. Canonical product owners, client consent, Focusa authority and human reserved powers still govern their actions.

## 13. New profile admission

Create a new employee profile only when:

- repeated verified work does not fit an existing profile;
- the outcome and canonical owner are distinct;
- required capability bundles and exclusions are known;
- CRIST, acceptance, evidence, escalation and revoke paths are defined;
- a pilot demonstrates value;
- duplication review passes.

Prefer extending task sets under a stable role over producing dozens of renamed near-duplicate employees.

## 14. Future Workforce Composer and AI Draftees relook

The Startempire Wire **AI Draftees** product is the closest existing UX precedent, but it is not a current-ready blueprint. The inspected plugin at `/home/startempirewire/public_html/wp-content/plugins/wire-draftees` has a clean `main` at `cad3e12` and real browse, profile, hire, My Draftees, dispatch, department, W.I.N.S., admin, event and cron foundations. Its principal product document still reports **DRAFT v1 — 2026-02-12**. Current public deployment, transaction, API/CLI parity, client readiness and browser acceptance were not proven in this audit.

**Historical constraint:** AI Draftees predates the Wirebot Desktop/Web/Mobile idea; the operator first introduced that application-family direction during this documentation effort on 2026-09-13. There is no proven pre-existing Wirebot Desktop product or canonical implementation. AI Draftees’ WordPress page hierarchy, checkout flow and dashboard boundaries reflect the product landscape when it was built—not a prior decision about what belongs in the newly proposed application family. Reuse domain truth and proven behavior; re-evaluate the UX and ownership from first principles.

### 14.1 Integration options

| Option | Product shape | Advantages | Costs/risks | Dependencies |
|---|---|---|---|---|
| A. Refresh AI Draftees as separate marketplace | public Startempire Wire discovery/hire/reputation product; Wirebot links to hired profiles | preserves network marketplace, public track records and existing W.I.N.S. framing | two UX/release stacks; hire semantics may not match private client assignment; stale UX must be rebuilt | current-state audit, API/CLI contracts, identity/entitlement bridge, live acceptance |
| B. Move all Draftees UX into Wirebot | Wirebot becomes both private workforce manager and public catalogue/hire UI | one application experience | collapses network marketplace into client OS; risks scope, tenancy and business-model confusion | ownership decision, migration, public discovery/SEO replacement, checkout redesign |
| C. Shared contracts, distinct public/private experiences | AI Draftees remains public marketplace/reputation; Wirebot Workforce Composer manages private roster/task assignment; both consume shared profile/task/dispatch/outcome contracts | strongest separation with reusable data and lower duplicate logic; clients can use internal profiles plus marketplace workers | contract/versioning and cross-product identity work; coordinated releases | shared schemas, APIs/CLIs, adapter tests, entitlement and receipt joins |
| D. Treat Draftees as migration source and retire it | import useful profiles/data into Wirebot, then decommission plugin | least long-term surface area | loses marketplace/network product and existing public proof model; migration/revocation risk | explicit product decision, export/migration proof, redirects and customer transition |

**Operator-confirmed direction:** the future Wirebot application family should professionally integrate the full Startempire Wire ecosystem for appropriately entitled users. WordPress REST endpoints are valid candidate adapters, and community, Direct and Sovereign/federated experiences may expose different authorized projections. Exact module ownership, federation and migration remain open.

**Evidence-based lean, not a decision:** evaluate C first. Public worker discovery/reputation and private client workforce composition are related but different jobs. Shared contracts can preserve AI Draftees value without forcing its stale WordPress UX to own the future Wirebot app. A low-cost community entry tier is a candidate, but no price or included capability is approved until economics, readiness, checkout and contract language agree.

### 14.2 Workforce Composer hierarchy

Candidate hierarchy for later application design:

```text
Client / tenant
└── Chief of Staff
    ├── Department
    │   ├── Employee profile
    │   │   ├── Task packs
    │   │   ├── capability bundles
    │   │   ├── CRIST template
    │   │   └── state/lifetime/schedule policy
    │   └── Assignment
    │       ├── project/workstream/task set
    │       ├── authority/data/budget refs
    │       └── execution instances
    └── outcomes, receipts, performance and revocation
```

Profiles are reusable templates. Assignments are client-specific employment packets. Execution instances are Silent Sessions, Work Loop lanes, scheduled runs or bounded jobs. None may be collapsed into one mutable “agent” record.

### 14.3 Candidate application surfaces

- **Browse Workforce:** filter by department, outcome, task pack, capability, state, lifetime, schedule eligibility, risk and readiness.
- **Employee Profile:** purpose, task packs, tool bundles, CRIST depth, evidence, availability, limitations and accepted performance.
- **Compose Employee:** add/remove task packs and show conflicts, missing APIs, CUA dependencies and authority impact.
- **Assign to Work:** select client/project/workstream/task set and preview exact employment packet.
- **My Workforce:** staff, scheduled workers, active flash/campaign workers, dormant bench and blocked profiles.
- **Dispatch/Work Rail:** ready/running/completed/blocked instances with receipts and escalation.
- **Schedule:** preview/commit/pause/revoke cadence, budget, overlap and missed-run policy.
- **Skills and Tools:** live-discovered Focusa/UIAI capabilities—not static marketing claims.
- **Performance/W.I.N.S.:** accepted outcomes, reliability, evidence, disputes and corrections—not vanity activity counts.
- **Authority Preview:** exact capabilities, data scopes, confirmations and external commitments before assignment.

### 14.4 API/CLI-first operation requirements

Do not invent or canonize operation names in this catalogue. Before a graphical Workforce Composer is accepted, compile exact product-owned operations from current Focusa, Wirebot and AI Draftees contracts for:

- profile and task-pack discovery/lifecycle;
- roster inspection, assignment preview, commit and revocation;
- dispatch preview, creation, observation, interruption and cancellation;
- schedule preview, activation, pause, resume and revocation;
- capability resolution and authority preflight;
- receipt, evidence and performance inspection;
- AI Draftees import/link resolution if that product remains connected.

Every accepted operation requires the API/CLI/UI/agent parity contract. Wirebot must never manage first-party employees by visually clicking the Draftees or Focusa interfaces. Exact IDs remain unresolved until the integrated operation inventory identifies the canonical owner and reuses existing operations.

### 14.5 Integrated product relook gate

Before implementation, audit together:

1. AI Draftees current source, live routes, data, checkout, dispatches, schedules and W.I.N.S. integration;
2. Wirebot/W.I.N.S. current app and future Desktop/mobile family;
3. Focusa Desktop, Menubar, Mission Canvas, Role Composer, Silent Sessions and workforce governance;
4. UIAI Cockpit, evidence and browser/computer execution surfaces;
5. Veragensia Chromebook workforce operation;
6. customer entitlement, consent, pricing, support and Sovereign boundaries;
7. product names, ownership, shared contracts and deprecation/migration choices.

The output is one portfolio architecture with distinct product responsibilities—not one giant application or a collection of stale overlapping screens.

## 15. First implementation slices

1. Validate this catalogue against current Focusa and UIAI live registries.
2. Generate the complete Golden Path per-machine tool inventory and profile/task assignment map, including every newly installed tool.
3. Settle and prove the stateful-worker memory architecture tracked in Wirebot Core issue #33; do not infer shared storage.
4. Complete the integrated AI Draftees/Wirebot/Focusa/UIAI/Veragensia product relook before selecting the Workforce Composer owner or UX.
5. Create the private `client.workforce-roster.v1`, tool-evidence and reusable task-pack schemas plus validators.
6. Map Golden Path audit findings to assignment states without automatic activation.
7. Convert existing client-specific duty lists into generic task packs plus private overlays.
8. Pilot `GPA-01` Golden Path Audit Specialist and `ROS-01` Client Roster Designer on one existing client.
9. Spin each pilot as a bounded Silent Session under one accepted task set.
10. Capture accepted outcomes, costs, escalation quality and missing capability gaps.
11. Refine profiles; then offer the roster review to existing clients.
12. Implement scheduling only after on-demand pilots are repeatably accepted.
13. Implement the graphical Workforce Composer only after API/CLI contracts and the product owner are settled.

## 16. Completion boundary

This catalogue is complete as a design asset when every profile has a unique purpose, canonical capability bundles, CRIST depth, lifetime, state posture, activation modes, scheduling eligibility, supervisor, evidence and acceptance contract—and when a client audit can produce a private roster without guessing.

It is not proof that every employee exists, is deployed, has credentials, is scheduled or is authorized for a client. Those claims require client-specific manifests and execution evidence.
