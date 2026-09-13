# Wirebot Ecosystem Agent-Operation Parity Audit

- **Status:** first-pass source audit; not product conformance or release certification
- **Contract:** [Agent-Operation-Complete Software Contract](./07-agent-operation-complete-software-contract.md)
- **Primary acceptance machine:** qualified Veragensia Chromebook
- **Audit rule:** source presence, internal endpoints and CLI names are evidence only; operation-level parity requires accepted producer and consumer proof

## 1. Purpose

This ledger identifies which first-party UI and business-operation families already have structured foundations and which still depend on UI-only behavior, incomplete adapters or unproven parity. It does not choose whether UIAI Cockpit is embedded, module-shared, deep-linked or separate, and it does not select the final Wirebot frontend/mobile packaging.

“Full API and CLI” does not mean publishing privileged administration to the internet. The supported API may be local, private or remotely scoped. It must remain versioned, discoverable, authenticated and callable by an authorized agent without visually operating the UI.

## 2. Portfolio summary

| Surface | Human UI exists | Structured API foundation | CLI foundation | Canonical operation catalogue | First-party normal path free of CUA | Audit state |
|---|---:|---:|---:|---:|---:|---|
| Focusa daemon/core | yes, multiple consumers | strong | strong | strong but not mapped here exhaustively | yes in principle | partial parity evidence |
| Focusa Desktop | substantial recovered branch source | strong underlying daemon | strong underlying CLI | Spec 135 Desktop registry exists on branch | likely, unproven | branch/main and UI parity unresolved |
| Focusa Menubar | substantial current-main companion | strong underlying daemon | strong underlying CLI | UI mapping incomplete | likely, unproven | unmapped companion parity |
| Focusa browser extension | concept only | conceptual | conceptual | no | n/a | not implemented |
| UIAI Engine | service/tools | strong HTTP/MCP/tool surface | no supported complete CLI proven | broad tool registry | CUA is itself a product capability | partial product parity |
| UIAI Cockpit | preview/substantial local source | service bridge | no complete CLI proven | 16-card manifest, 5 cards lack contract refs | unproven | partial/unhealthy checkout |
| UIAI FPV/Evidence PWA | implemented/spec-backed surfaces | typed session/evidence routes | unverified | partial | yes for viewing | partial consumer proof |
| Wirebot `wb`/runtime | multiple UIs/services | broad service endpoints | broad CLI families | no unified operation catalogue | mixed/unproven | partial |
| W.I.N.S. | responsive Svelte UI | scoreboard handlers | overlapping `wb` commands | no screen-operation ledger | unproven | partial |
| Wirebot browser extension | MV3 source/build | REST/websocket/chrome-message foundations | no complete CLI | no | unproven | partial |
| Wirebot Desktop/mobile | not implemented | intended managed APIs | intended `wb` CLI | no app catalogue | n/a | absent |
| Veragensia | OS/Agent Computer UI | descriptors and future adapters | scripts exist; complete CLI absent | 22 semantic operations | execution adapters incomplete | descriptor-only partial |
| Public sales/setup sites | WordPress/browser UI | provider/WordPress APIs exist in parts | WP/provider CLIs exist in parts | no cross-business operation catalogue | unproven | unmapped |
| Invoice → payment → scheduling → workspace | fragmented process | provider endpoints exist | provider CLIs vary | no canonical lifecycle contract | no | major gap |
| Golden Path fleet scripts | reports/CLI output | no supported service API | yes | script schemas only | yes | CLI-only partial |

No row currently proves product-level **accepted** status under the contract.

## 3. Focusa

### 3.1 Focusa daemon/core

Observed foundations:

- a large versioned `/v1` API route set;
- broad `focusa` CLI and native `focusa_*` tool surfaces;
- explicit authority, scope, confirmation, idempotency and receipt semantics for many operations;
- machine-readable capability search/describe and generated operation bindings.

Open parity work:

1. Export one normalized operation catalogue conforming to `agent.operation.v1`, or define an explicit compatible projection.
2. Prove each relevant CLI command and native tool resolves to the same operation ID and output semantics.
3. Separate operations that have only tool/API exposure from those that also satisfy complete CLI parity.
4. Record supported-version negotiation and cross-version results.

### 3.2 Focusa Desktop

Focusa Desktop is the rich primary workspace recovered at `apps/desktop/` on `origin/local/spec158-desktop-pivot-audit-2026-08-04`, not the Menubar app. The Spec 135/158 pivot moved the complete Mission Canvas out of a Pi TUI-first implementation while retaining Pi as a thin control/runtime surface.

Observed evidence:

- commit `1367ee5c9` introduced the real Desktop shell;
- Tauri product `Focusa Desktop`, identifier `com.focusa.desktop`, branch version `0.9.143`;
- Mission Canvas, generated-surface renderer, Work Rail/contributions, global prompt editor, Context Control, Agent TUI inner surface and offline projection support;
- commit `9234daee0` added the typed Spec 135 operation registry;
- commit `16c1a6e44` added an explicit Desktop-to-Menubar bridge;
- 159 files and 139 Desktop-touching commits exist on the recovered branch.

Gaps:

- the Desktop tree is absent from current `main`;
- the recovered branch is 339 commits ahead and 2,032 behind current main;
- daemon/API evolution, operation IDs and package dependencies need reconciliation without replaying stale behavior;
- no current release, installed-runtime, signing/update or Veragensia acceptance was proven;
- the archived dependency-free test suite currently stops on its first shell-contract assertion: expected `UIAI Engine browser proof` text is absent from the source under test;
- complete Desktop control/state → canonical API → supported CLI parity remains unproven.

### 3.3 Focusa Menubar

Observed current-main UI families in `apps/menubar`:

- Focus bubble;
- Mission Canvas summary/control;
- Trajectory;
- Workpoint;
- Proof;
- Work Loop;
- Focus Gate;
- Sync;
- Device Pairing;
- Settings.

Current source identifies package `focusa-menubar`, Tauri identifier `com.focusa.menubar`, version `0.9.186` and a 340×480 fixed companion panel. Its client has bounded request helpers, bearer-token handling, scope headers, write detection and normalized tool results.

Gaps:

- no generated ledger mapping every Menubar control/read state to an operation ID;
- local saved-connection/settings actions are not reconciled with supported CLI operations;
- notification, tray/window, startup and update actions need Linux/Veragensia operation contracts;
- current build validation was unavailable in the routed environment because `svelte-kit` was absent;
- the historical Desktop bridge has not been proven against current main and the recovered Desktop branch;
- macOS-shaped Menubar assumptions need explicit Veragensia Linux adaptation.

### 3.4 Focusa browser extension

Only a concept document was found. No Chrome manifest, executable source, supported API, CLI, operation catalogue, store package or Chromebook proof was found.

Required baseline before implementation acceptance:

- operation catalogue for page/project context, evidence capture, task/Workpoint handoff and user-visible status;
- API and CLI equivalents for every extension action;
- explicit browser permissions, origin isolation, mutation confirmation and revocation;
- Chrome/Veragensia installation and cross-version tests.

## 4. UIAI

### 4.1 UIAI Engine

Observed structured foundations:

- HTTP routes for browser sessions, semantic selectors, actions, diagnostics, evidence and source conversion;
- MCP/native tool discovery and calls;
- an engine executable entry, which is not evidence of a complete product CLI;
- accessibility/DOM operations that precede coordinate CUA;
- diagnostics-first and evidence-delivery contracts.

UIAI is also the governed provider of CUA for applications that genuinely lack structured interfaces. That capability must remain distinct from first-party product integration.

Gaps:

- no supported complete `uiai` CLI was discoverable in the current audit shell;
- no audited one-to-one API/CLI/tool operation projection for the complete route registry;
- browser actions need explicit classification between canonical structured web operations, semantic automation and coordinate/pixel CUA;
- not every evidence/publication action has proven CLI parity;
- full cross-version and Chromebook acceptance are not established here.

### 4.2 UIAI Cockpit

The Phase 0 card manifest contains 16 card declarations. Five inspected cards have `contract_ref: null`; the remainder reference Focusa tools. This is useful honesty, but it is direct evidence that complete contract coverage is unfinished.

Observed families include:

- UIAI health and browser diagnostics;
- Focusa Project Identity and Project Card;
- Workpoint and Trajectory;
- tool doctor and recovery guidance;
- Work Loop;
- device pairing;
- evidence linkage;
- UIAI session/evidence controls.

Gaps:

1. Replace every `contract_ref: null` for an in-scope feature with a canonical operation or explicitly exclude it.
2. Map every card action/state to API, CLI and agent-tool consumers.
3. Preserve UIAI versus Focusa authority ownership instead of wrapping Focusa operations as Cockpit-owned logic.
4. Resolve current local source-check errors before claiming build health.
5. Prove Linux/Tauri operation, secure storage and update behavior on Veragensia.

Embedding Cockpit in Wirebot would not close these gaps. The embedded UI must still invoke structured operations rather than becoming a visual automation target.

### 4.3 UIAI FPV and Evidence PWA

Observed:

- tokenized FPV sessions are documented;
- evidence/publication envelopes and current tools exist;
- read-only default behavior is specified;
- current runtime returned bounded evidence-delivery metadata.

Gaps:

- complete CLI parity for session creation, inspection, sharing, verification, revocation and cleanup;
- admissible customer-scope publication/readback proof;
- offline/degraded and stock-ChromeOS PWA acceptance;
- Wirebot and Cockpit consumer tests against the same evidence operations.

## 5. Wirebot

### 5.1 `wb` and service plane

Observed:

- broad CLI families for status, health, businesses, context, communication, Focusa, queue, provision, plugins, vision, memory/wiki, trust, lifecycle and other domains;
- scoreboard, WBT and Context Core service handlers;
- machine-readable output support for some current commands.

Gaps:

- no single canonical operation catalogue joining CLI families to service routes and UI consumers;
- installed `wb` help, source command families and public product vocabulary require an explicit parity/freshness audit;
- machine-readable output, stable exit classes, exact scope and idempotency are not proven for every command;
- lifecycle commands need operation-level consequence/confirmation mapping.

### 5.2 W.I.N.S. UI

Observed responsive modules include customer workspace, flow, portfolio, season, talk/chat, discovery, integrations, audit, canonical mappings/rollups and navigation/settings surfaces. Scoreboard handlers and a small frontend API helper exist.

Gaps:

1. Inventory every control and read model—not only page names.
2. Assign each to a canonical Wirebot, Focusa, UIAI or external-provider owner.
3. Add stable operation IDs and strict schemas.
4. Prove equivalent `wb` commands and API results.
5. Remove UI-owned business transitions.
6. Prove headless complete workflows before desktop/mobile wrapping.

Moving the screens into a shared frontend before this mapping could preserve or amplify hidden coupling.

### 5.3 Wirebot browser extension

Observed:

- Manifest V3 source and a built manifest;
- Chrome message, local-storage, network membership, WordPress REST and websocket integration foundations;
- current branding still overlaps Startempire Wire Network.

Gaps:

- no canonical operation registry;
- no complete CLI route for extension-visible actions/state;
- browser message types are not proven as stable product operations;
- permissions, authentication, tenant/project scope and revocation need a single contract;
- source/store/current-install parity and Chromebook proof are absent.

### 5.4 Wirebot Desktop/mobile

No canonical application source, Tauri project, mobile package, signing pipeline or release proof exists. The API/CLI contract must precede packaging so the future app does not become the first or only owner of product behavior.

Required first slice:

- shared operation client generated from the Wirebot catalogue;
- read-only W.I.N.S. workspace shell;
- matching `wb` commands;
- one mutation with exact scope, idempotency and durable receipt;
- headless and UI parity tests;
- Veragensia Chromebook proof without CUA.

## 6. Veragensia

Observed:

- `config/system-operations.json` validates successfully;
- 22 descriptors cover all nine expected operation families;
- categories include workspace, window, app, audio, Bluetooth, capture, clipboard, display, notification, power, text and agent behavior;
- descriptors identify operation IDs, parameters, preconditions, risk and opaque execution-template references;
- the validator explicitly states that descriptors advertise behavior, do not execute and do not grant authority.

This is the clearest existing starting point for the cross-portfolio operation model, but it is not complete execution.

Gaps:

1. Project or extend descriptors into the shared operation contract without creating a second authority model.
2. Complete the execution-adapter tranche referenced by the Veragensia specifications.
3. Provide supported local API and noninteractive CLI routes for all accepted operations.
4. Bind Focusa authority and UIAI evidence without making either product a Veragensia implementation detail.
5. Install and operate all portfolio UIs on the qualified Chromebook.
6. Measure concurrent resource use and prove complete headless workflows.
7. Reserve semantic/CUA fallbacks for external software without supported operations.

## 7. Public sales and setup surfaces

The public sites are also software interfaces and fall under the baseline when they perform consequential work.

### 7.1 Focusa.dev and wirebot.chat

Marketing content reads may remain public web projections, but plan selection, account creation, entitlement inspection, support state and purchase initiation need canonical operations with API and CLI parity for authorized agents. WordPress page or theme code is not the product operation owner.

### 7.2 meet.focusa.dev purchase/scheduling

Observed purchase routes and offer identifiers prove a browser entry, not a complete lifecycle. Required operations include:

- inspect active offer and versioned scope;
- create/retrieve invoice-contract packet;
- observe first-payment acceptance;
- issue and inspect single-use scheduling entitlement;
- schedule/reschedule/cancel within policy;
- bind the accepted engagement to one customer workspace;
- revoke/expire and reconcile duplicate or failed delivery;
- read durable consent/payment/scheduling/workspace receipts.

Each requires a supported API and CLI consumer. Agents must not complete this first-party lifecycle by clicking the public purchase UI.

### 7.3 Pricing updates

Public price/content mutation remains blocked until offers, contract scope, operational readiness, checkout identifiers and activation strategy are operator-set and reconciled. Agent-operation completeness enables safe updates; it does not authorize them.

## 8. Golden Path scripts

The current substrate, audit, sweep and fleet-diff tools are structured CLI plumbing with JSON schemas/results. They do not yet have a supported service API or customer UI mapping.

Options to evaluate later:

- wrap stable read-only reports in a private Wirebot API owned by the Golden Path service;
- keep mutation local/CLI-only but expose a governed dispatch API with exact target, hash, idempotency and receipt;
- consume report schemas in Wirebot/W.I.N.S. without copying audit logic into the frontend.

No option is selected here.

## 9. Operation-catalogue and CLI ownership options

Agent-operation completeness does not by itself decide where the catalogues or CLI commands live. Current source evidence shows Focusa already owns a generated Focusa Agent Operation Registry, while Veragensia owns its semantic native-system operation registry. The options must preserve those real domain boundaries.

### 9.1 Catalogue topology

| Option | Description | Advantages | Costs/risks | Dependencies |
|---|---|---|---|---|
| A. Product-owned catalogues + federated projection | Focusa, UIAI, Wirebot and Veragensia own their operations; Wirebot/Agent Computer exposes a read-only joined discovery view | strongest canonical ownership; independent release/versioning; avoids one god registry; fits existing evidence | federation, conflict and version negotiation are real work; agents may need several endpoints | shared descriptor projection, namespace rules, discovery joins, compatibility tests |
| B. Focusa owns the global catalogue | move all operations into Focusa’s generated registry | mature authority/tool machinery; one agent discovery surface | makes product capabilities depend on Focusa release/availability; risks confusing work governance with domain ownership | explicit owner delegation, external-provider lifecycle and outage design |
| C. Veragensia owns the global catalogue | treat Agent Computer registry as universal software registry | natural installed-device discovery; strong local capability fit | remote/cloud/business operations do not belong to device OS; other platforms become awkward | remote operation model, server authority and non-Veragensia support |
| D. UIAI owns the global catalogue | expose everything through UIAI tools | powerful execution/tool discovery and evidence | confuses execution adapter with domain owner; encourages CUA/tool mediation where direct APIs exist | authority transfer and non-browser domain coverage |
| E. ADLBOS owns one central catalogue | portable contract repository becomes operational registry | cross-portfolio visibility and portability | creates a new runtime authority and duplicates live products; highest drift risk | full lifecycle service, release process and ownership migration |

**Evidence-based lean, not a decision:** evaluate A first. Product-owned canonical catalogues plus a federated, value-free discovery projection match current ownership and minimize authority collapse. The shared `agent.operation.v1` schema should remain a portability/conformance projection, not a new runtime owner.

### 9.2 CLI topology

| Option | Description | Advantages | Costs/risks |
|---|---|---|---|
| A. Product-native complete CLIs only | `focusa`, `uiai`, `wb` and `veragens` each expose their own full operations | clear ownership and independent support | agents must discover several clients; cross-product workflows need orchestration |
| B. Native CLIs + `wb` delegating façade | every owner retains a complete CLI; `wb` offers selected joined workflows by invoking canonical APIs/contracts | one convenient operator entry without sacrificing owner parity | façade can drift or hide errors unless generated/tested; must not shell-scrape text |
| C. One generated universal CLI | generate commands from the federated catalogue | maximal consistency and machine discoverability | namespace/UX complexity; lowest-common-denominator pressure; central generator becomes critical dependency |

**Evidence-based lean, not a decision:** B is the most compatible with the current ecosystem if `wb` remains a consumer/delegator rather than a second implementation. Product-native CLI completeness remains mandatory under every option; an umbrella CLI cannot compensate for a missing owning CLI.

### 9.3 API access topology

Direct product APIs, an authenticated local Agent Computer gateway and a Wirebot remote orchestration gateway can coexist. A gateway must preserve the underlying operation ID, owner, scope, authority verdict, typed error and receipt. Proxying does not transfer canonical ownership and must not silently widen capability.

No catalogue, CLI or gateway option changes the rule that CUA is last resort.

## 10. Cross-product priority gaps

### P0 — contract ownership

1. Select the canonical catalogue owner/projection for each product without creating a new central runtime authority.
2. Map every first-party consequential UI control and read state.
3. Resolve duplicate operations across Wirebot, Focusa, UIAI and Veragensia by ownership, not renaming.
4. Specify the invoice/payment/scheduling/workspace lifecycle.

### P0 — first integrated acceptance

5. Select one bounded W.I.N.S. read operation and one receipt-producing mutation.
6. Implement or reconcile complete API and CLI adapters.
7. Bind a UI control and an agent tool to the same operation.
8. Prove the workflow headlessly with no CUA.
9. Run it on the qualified Veragensia Chromebook.

### P1 — portfolio completion

10. Export product-level operation catalogues.
11. Add parity and cross-version test matrices.
12. Reconcile browser-extension message contracts.
13. Complete Cockpit card contract refs.
14. Add sales/setup lifecycle operations.
15. Record and retire first-party `structured_interface_gap` entries.

## 11. Acceptance rule

A surface remains incomplete until all in-scope operations reach **accepted** under the Agent-Operation-Complete Software Contract. A beautiful UI, a large route count, a CLI help listing, an operation descriptor, a passing producer test or successful CUA demonstration is not enough by itself.
