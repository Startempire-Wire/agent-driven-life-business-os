# Wirebot product UI inventory and consolidation audit

- **Audit date:** 2026-09-13
- **Scope:** Focusa Desktop, Focusa Menubar, Focusa browser extension, UIAI Cockpit, UIAI evidence/FPV PWAs, Wirebot browser extension, Wirebot Desktop/mobile, W.I.N.S. screens, Veragensia, and their public sales/access doors
- **Status vocabulary:** `implemented` means source exists; `runtime-observed` means a current service/tool was observed; `released` or `customer-ready` requires separate distribution and consumer proof
- **Decision posture:** this is an inventory and options paper, not a final architecture declaration. Only explicitly operator-confirmed directions are marked confirmed; all other placements remain candidates.

## 1. Confirmed direction and open questions

### Operator-confirmed direction

- The interface previously described as the Golden Path “wrapped process” is now named **Wirebot Desktop**.
- Wirebot Direct subscription screens and the existing W.I.N.S. mobile/PWA screens should be considered for one consolidated Wirebot experience.
- The W.I.N.S. PWA should be developed into a mobile app rather than remaining only a browser-installable PWA.
- Wirebot Direct, Full AITL Setup and the personal-presence engagement use the **same Wirebot app**, not tier-specific Tauri applications.
- Full AITL Setup is the established scalable middle path; it is not a newly invented offer.
- UIAI’s complete Evidence PWA will be integrated into **UIAI Cockpit**.
- Veragensia must remain visible as a first-class product/runtime in the portfolio inventory.
- Because Veragensia’s first native reference Agent Computer targets Chromebook hardware, every ecosystem application UI should work fully and coherently on the **Veragensia Chromebook baseline**.
- Every product is **agent-operation complete by default**: all consequential UI actions and readable state have complete, versioned API and CLI routes. Computer-use automation (CUA) is the absolute last resort.

### Decisions intentionally deferred

- Whether Wirebot contains only bounded UIAI/evidence modules, embeds the complete UIAI Cockpit, or shares a modular Cockpit workspace between both products.
- Whether “Wirebot Desktop” is the product-family name or only the desktop distribution of a broader “Wirebot” application.
- Whether desktop, mobile and PWA are built from one exact frontend package or share lower-level components/contracts through separate shells.
- Which repository owns the Wirebot application source.
- Which current W.I.N.S. implementation becomes canonical.
- Whether the PWA remains a supported delivery target after native mobile release.
- The exact Direct, Full AITL, support and personal-presence prices and their activation dates.
- How much Focusa governance, UIAI operation and Veragensia control should be exposed to ordinary Wirebot customers versus professional operators.

## 2. Product and UI catalogue

### 2.1 Focusa Desktop

- **Canonical owner:** `Startempire-Wire/focusa`
- **Recovered source:** `apps/desktop/` on `origin/local/spec158-desktop-pivot-audit-2026-08-04`; absent from current `main`
- **Technology/identity:** SvelteKit + Tauri 2; package `focusa-desktop`; product `Focusa Desktop`; identifier `com.focusa.desktop`; branch source version `0.9.143`; 1440×900 resizable primary window
- **Origin:** spun out of the Spec 135 Mission Canvas series through the Spec 158 desktop pivot after the complete rich Canvas proved unsuitable as a Pi TUI-first product. Commit `1367ee5c9` introduced the real Desktop shell on 2026-08-04.
- **Purpose:** primary rich Focusa cognitive cockpit and professional workspace—Mission Canvas, generated surfaces, Work Rail, context control, global prompt/editor, Agent TUI inner surface, evidence and governed operations. Pi remains a thin agent/runtime/control surface rather than the owner of the rich desktop experience.
- **Separation proof:** commit `16c1a6e44` added a typed **Desktop-to-Menubar bridge**, explicitly treating Desktop and Menubar as cooperating applications. They are not aliases.
- **Implementation evidence:** the recovered branch contains 159 Desktop files across 139 Desktop-touching commits. Commit `9234daee0` added a canonical Spec 135 operation registry; later commit `e02b39430` described 25 live plus eight preview operations.
- **Current status:** substantial implemented branch source exists, but it is not in current `main`; the branch is 339 commits ahead and 2,032 behind current main. A dependency-free archived `npm test` attempt stopped on the first shell contract because the current source no longer contained the expected `UIAI Engine browser proof` label, proving branch/test drift. No current release, installed-runtime or supported-branch acceptance was proven. Source recovery must not be mistaken for active product release.
- **Boundary:** Focusa Desktop owns rich mission/governance presentation. It is not Focusa Menubar, Wirebot Desktop, UIAI Cockpit, W.I.N.S. or the customer’s Life and Business OS shell.

### 2.2 Focusa Menubar

- **Canonical owner:** `Startempire-Wire/focusa`
- **Current source:** `apps/menubar/` on current `main`
- **Technology/identity:** SvelteKit + Tauri 2; package `focusa-menubar`; product `Focusa`; identifier `com.focusa.menubar`; current source version `0.9.186`; 340×480 fixed companion window
- **Purpose:** lightweight status/control companion for focus, Workpoints, Trajectory, project/runtime state, pairing, sync, proof and governed work controls
- **Current status:** substantial current-main implementation with updater configuration and tests. The earlier audit check could not run because the routed build environment lacked `svelte-kit`; this is an unverified build, not proof of a source failure.
- **Observed gaps:** current release/install acceptance, Linux tray/window adaptation, complete UI/API/CLI mapping and operation of the Desktop bridge against a reconciled Desktop source
- **Boundary:** Menubar may summarize/control Desktop and daemon state, but it does not replace the full Desktop cognitive cockpit.

### 2.3 Focusa browser extension

- **Canonical owner:** `Startempire-Wire/focusa`
- **Current definition:** `docs/174-focusa-agent-workforce-extension-concept.md`
- **Purpose:** browser-adjacent Focusa workforce/session surfaces; the human-side capture/save browser extension is named as future work
- **Current status:** concept only. The document says `Status: concept`; no Chrome manifest or implementation was found in the current Focusa tree.
- **Boundary:** do not confuse this with the implemented Focusa Pi extension, UIAI browser tools, or the Wirebot/Startempire Wire extension.
- **Gap:** implementation owner, manifest, permission model, origin isolation, release channel, store listing, and consumer proof remain absent.

### 2.4 UIAI Cockpit

- **Canonical owner:** `WPUIAI/uiai-engine`
- **Current source:** `apps/cockpit/`
- **Technology/identity:** SvelteKit + Tauri 2; package `uaiengine-cockpit`; product `UIAI Engine Cockpit`; identifier `com.wpuiai.uiaiengine.cockpit`; source version `0.1.0-dev`
- **Purpose:** first-party browser/computer operation, multimodal inspection, diagnostics, evidence, workstream controls, takeover/control leases, and operator workspace
- **Specification:** `UIAI_COCKPIT_000...` is a replacement-candidate master specification with later amendments, not a blanket claim that every designed surface is released
- **Current status:** substantial implementation exists; the inspected checkout is one commit ahead and 515 behind its remote with extensive uncommitted/untracked work, so it is not safe evidence of current upstream or installed-runtime parity. `npm run check` executed and reported nine unresolved imports/types across the current local hardening/profile work; tests did not run after the check failure.
- **Boundary:** Cockpit owns the full operator-grade UIAI and evidence workspace. Wirebot consumes bounded capabilities and evidence views; it does not absorb Cockpit.

### 2.5 UIAI FPV and Evidence PWA modules

- **Canonical owner:** UIAI Engine
- **FPV PWA:** the UIAI first-person-view PWA is documented as implemented: tokenized `/m/{token}` sessions, read-only by default, optional audited controls
- **Evidence PWA / Evidence Share:** current UIAI tools return governed Evidence Share Packet and EPWA delivery contracts. The active browser audit produced EPWA delivery envelopes, although publication was blocked without an admissible Focusa evidence scope.
- **Confirmed placement:** the complete Evidence PWA is integrated into UIAI Cockpit. Whether Wirebot also contains a bounded evidence viewer, shared Evidence PWA module or the complete Cockpit remains under comparison.
- **Wrinkle:** FPV live-session viewing and portable Evidence Share packets are distinct products/contracts and must not be collapsed into one generic “PWA.”

### 2.6 Wirebot browser extension

- **Canonical source owner observed:** `Startempire-Wire/Startempire-Wire-Network` (local checkout `startempire-wire-network-ext`)
- **Technology/identity:** Svelte extension; Manifest V3; package `startempire-wire-network-extension`; current manifest/package version `0.2.2`
- **Surfaces:** browser action popup, side panel, new-tab override, options, background worker, content scripts, network/community resources and Wirebot interactions
- **Current status:** implementation and a built `dist/manifest.json` exist. Store publication/current user installation was not proven. The local checkout is 17 commits ahead of `origin/main` with an untracked Beads daemon-error file, so it must not be treated as clean published source. Its source check could not run because `svelte-check` was unavailable; dependencies were not installed during this audit.
- **Naming wrinkle:** public manifest and repository identity say “Startempire Wire Network,” while business discussion calls it “Wirebot Extension.” Its product name, network role, and Wirebot role need one explicit decision.
- **Boundary:** browser-context, network/community and web-page interaction remain extension-specific; the extension should deep-link/share context with Wirebot Desktop/mobile rather than reproduce the complete application.

### 2.7 Wirebot Desktop and Wirebot Mobile

- **Product owner:** Wirebot
- **Current doctrine owner:** `Startempire-Wire/agent-driven-life-business-os`
- **Likely implementation owner:** `Startempire-Wire/wirebot-core`, because it already owns the Wirebot runtime, W.I.N.S./scoreboard frontend, tenant/session contracts and Direct productization. This is a recommendation until the source-root decision is recorded.
- **Technology direction:** one shared responsive frontend packaged by Tauri for desktop and mobile; web/PWA can remain a derived delivery target
- **Purpose:** consolidated customer application for every Wirebot plan and delivery level
- **Current status:** product direction is now established; no Wirebot Tauri package, application identifier, signing/update configuration, mobile project, or release pipeline was found
- **Critical distinction:** the Full AITL Setup delivery path already exists in the product model. The consolidated app implementation is unfinished; the service path is not newly invented.

#### Entitlement-driven experience

- **Wirebot Direct:** managed website/SaaS relationship and personal Wirebot identity without requiring Startempire Wire network membership
- **Network-enabled plans:** the same app plus authorized network/community, opportunity and distribution modules
- **Full AITL Setup:** the same app plus guided discovery, local owner moments, machine enrollment, fleet readiness, deterministic setup, Agent Operator work, remote sessions, recovery and handoff
- **Personal-presence engagement:** the same app/system plus the Canonical Owner Principal’s scarce judgment and presence; never another application
- **Sovereign/dedicated operation:** changes runtime/isolation and service agreement, not the customer app

### 2.8 W.I.N.S. screens and PWA

- **Canonical product role:** outcome and operating portal—Plan → Ship → Prove, conversation, goals, work, evidence and economics
- **Current Wirebot source:** `wirebot-core/cmd/scoreboard/ui/`, a Svelte 5/Vite frontend with Dashboard, Chat, Focus, Portfolio, Season, Talk, Feed, Score, Onboarding, Pairing, System Status and other modules
- **Mobile evidence:** responsive breakpoints and mobile-specific OAuth/pairing behavior exist in source
- **Separate source found:** the `sew-pwa` WordPress plugin is a Startempire Wire PWA foundation. It is not automatically the canonical W.I.N.S. component source.
- **Confirmed product direction:** W.I.N.S. screens become part of Wirebot Desktop/mobile. The implementation method—direct wrapping, extraction into shared modules, or a shared remote frontend—remains undecided and is weighed below.
- **Code wrinkle:** the current scoreboard `App.svelte` is large and mixes navigation, state and many product surfaces. Extraction needs explicit API/session seams before Tauri/mobile packaging.

### 2.9 Veragensia

- **Canonical owner:** `Startempire-Wire/veragensia`
- **Product identity:** Focusa Agent OS / Agent Computer substrate built from Omarchy plus Focusa, UIAI Engine, browser/extension integration and human-control boundaries
- **Purpose:** provisioned or streamable agent computer, workload enforcement, secure attention, runtime/resource identity, browser/computer execution, voice/audio UI, lifecycle and operator control reserve
- **Current status:** extensive specification and implementation source exists; the repository explicitly distinguishes its public proving ground from a completed native release. Current source checkout has uncommitted state/cache artifacts, so live/release claims require separate proof.
- **Boundary:** Veragensia is the execution environment and Agent Computer—not another Wirebot customer dashboard. Wirebot Desktop/mobile may request governed work from Veragensia and display receipts; it does not absorb the OS, UIAI Cockpit, or Veragensia’s trust controls.

## 3. Public doors and transaction surfaces

These are product entrances, not replacements for the applications:

- **`focusa.dev`:** Focusa product marketing and software licensing. Live source still contains a `$5,000` Operator Deployment offer.
- **`wirebot.chat`:** Wirebot marketing and app entry. Live WordPress content still describes “Wirebot Direct (Standalone)” at `$299/quarter` or `$999/year`.
- **`meet.focusa.dev`:** payment and scheduling flow. The verified public purchase route includes Focusa/UIAI licenses and the `$5,000` setup reservation, then promises a single-use scheduling entitlement after payment.
- **W.I.N.S. portal/mobile:** becomes a delivery target of the consolidated Wirebot frontend rather than a separately designed customer product.

No public price should imply that the unfinished consolidated app, Full AITL setup automation, Direct infrastructure or mobile binaries are currently delivered. Contract-attached invoices and first payment remain the business acceptance mechanism; the app consumes that recorded engagement and must not invent a duplicate consent ceremony.

## 4. Infrastructure model for Wirebot Direct

The current Wirebot runtime contract supports the previously intended growth model:

1. Begin with shared managed infrastructure/VPS capacity.
2. Give each customer a logically isolated bot identity containing tenant, user, agent, memory, tier, runtime, channel and budget bindings.
3. Route authenticated W.I.N.S./Wirebot app sessions to that identity.
4. Add capacity/nodes as usage grows.
5. Move contractually qualified Sovereign customers to dedicated managed runtimes without changing the Wirebot application.

This model is documented but a production Wirebot Direct estate was not established or proven in this audit. Product marketing must distinguish architecture intent from live capacity, provisioning and support readiness.

## 5. Consolidation boundaries

| Surface | Must remain canonical for | May appear inside Wirebot app as | Must not become |
|---|---|---|---|
| Focusa Desktop | rich Focusa Mission Canvas/cognitive cockpit and professional workspace | bounded project, goal, Workpoint, Canvas, evidence and approval views | Focusa Menubar or the Wirebot customer shell |
| Focusa Menubar | lightweight Focusa status/control companion | summarized project, Workpoint, pairing, sync and work controls | the complete rich Desktop workspace |
| Focusa browser extension | Focusa browser-adjacent workforce/capture | deep links and context handoff | a duplicate Wirebot extension |
| UIAI Cockpit | full browser/computer/evidence operator workspace | bounded evidence viewer, session status, approved controls | a copied UIAI engine inside Wirebot |
| UIAI Evidence PWA | evidence packets, verification, sharing, redaction | customer evidence inbox/viewer | a Wirebot-owned evidence authority |
| Wirebot extension | browser/network context and side-panel access | companion/deep-link to customer workspace | the complete desktop/mobile app |
| Wirebot Desktop/mobile | consolidated customer operating partner and setup/support workspace | all entitlement-selected Wirebot modules | Focusa Desktop, Cockpit or Veragensia |
| Veragensia | Agent Computer OS/execution and human-control reserve | governed machine/session status and receipts | a customer subscription UI |

## 6. Options and tradeoffs

### 6.1 UIAI Cockpit inside Wirebot

| Option | Description | Advantages | Costs/risks | Reversibility |
|---|---|---|---|---|
| A. Separate Cockpit + bounded Wirebot evidence/session views | Cockpit remains its own professional operator app; Wirebot renders only customer-safe projections and deep links | Clearest authority boundary; smallest Wirebot app; independent releases; least exposure of advanced controls | Context switching; duplicate navigation patterns; customers may miss valuable UIAI capabilities | High |
| B. Embed the complete Cockpit in Wirebot | All Cockpit screens ship inside the Wirebot application and are entitlement-gated | Most consolidated experience; strong premium demonstration; Direct/AITL users can see browser, evidence and agent activity in one place | Large application; exposes operator complexity; security and capability surface expands; Wirebot releases become coupled to Cockpit; risk of two Cockpit implementations | Low unless Cockpit is modular first |
| C. One canonical modular Cockpit workspace, consumed by both shells | UIAI owns Cockpit modules/contracts; UIAI Cockpit exposes the full workspace; Wirebot selects entitlement-safe modules from the same packages | DRY; preserves UIAI ownership; supports a genuinely consolidated Wirebot experience; each shell can have different navigation and permissions | Highest initial modularization cost; requires stable package/version/API boundaries and cross-repository release coordination | High after modularization |
| D. Remote Cockpit web surface embedded in Wirebot | Wirebot hosts a webview/route to Cockpit rather than compiling its components | Fastest proof; one deployed Cockpit implementation | Network-dependent; difficult auth/cookie/origin handling; weaker native feel; broad remote surface inside customer app; offline failure | Medium |

**Current evidence-based lean, not a decision:** evaluate C first. It allows full Cockpit capabilities to appear in Wirebot when justified without transferring UIAI’s canonical authority or creating a copied Cockpit.

Qualitative weighting for later decision: A is strongest for isolation and release independence; B is strongest for immediate one-app breadth but weakest for security/release coupling; C is strongest for long-term cohesion and DRY but slowest to establish correctly; D is fastest for a proof but weakest for native/offline quality. No numeric score is assigned until the operator chooses the relative importance of speed, breadth, isolation and maintainability.

### 6.2 W.I.N.S. PWA to desktop/mobile

| Option | Description | Advantages | Costs/risks | Reversibility |
|---|---|---|---|---|
| A. Wrap the current scoreboard UI directly | Point Tauri at the existing responsive Svelte frontend | Fastest prototype; validates customer demand and native packaging | Current shell is large/monolithic; web auth, service worker and navigation assumptions leak into native; hard to maintain | Medium |
| B. Extract canonical W.I.N.S. modules, then build web/Tauri shells | Separate screens, session, navigation, API and design-system packages; consume them from PWA, desktop and mobile shells | Strongest long-term DRY; native adapters are explicit; every target shares business/UI logic | More work before the first binary; migration must preserve current portal behavior | High |
| C. Keep W.I.N.S. remotely hosted and use a Tauri webview | Native shell loads the managed web application | Simple deployment and instant server-side updates | Mostly a packaged website; offline/degraded UX is weak; native capabilities and store policy may be harder; origin/session compromise has larger impact | Medium |

**Current evidence-based lean, not a decision:** B is the durable product path; A can be a disposable prototype only if it does not become the second canonical implementation.

### 6.3 Evidence PWA placement in Wirebot

| Option | Description | Advantages | Costs/risks |
|---|---|---|---|
| Viewer only | Wirebot lists and verifies customer evidence packets; authoring and administration stay in Cockpit | Simple customer story; narrow permissions | Advanced evidence workflows require Cockpit |
| Shared EPWA module | UIAI publishes the canonical Evidence PWA viewer as a reusable module consumed by Cockpit and Wirebot | Same proof experience everywhere; no renderer fork | Requires stable module/version contract and release coordination |
| Full Cockpit | Evidence arrives as part of a complete embedded Cockpit | Maximum capability | Inherits all full-Cockpit coupling and security costs |

The confirmed requirement is complete Evidence PWA integration in Cockpit. Its additional Wirebot placement remains open.

### 6.4 Wirebot application source ownership

| Option | Advantages | Costs/risks |
|---|---|---|
| `wirebot-core/apps/wirebot` | Co-locates runtime, W.I.N.S. UI, tenant/session contracts and app; easiest initial extraction | Repository is already broad; release boundaries must be tightened |
| New dedicated Wirebot app repository | Clean product/release ownership and smaller checkout | Immediate cross-repository package/version complexity; risks duplicating W.I.N.S. during extraction |
| ADLBOS repository | Close to Golden Path doctrine | Wrong concern owner: a portable doctrine/process repository would become product source |

### 6.5 Native mobile strategy

| Option | Advantages | Costs/risks |
|---|---|---|
| Tauri 2 desktop + iOS/Android from shared frontend | One Rust/web stack and product family | Native plugin maturity, store policies, background behavior and platform QA remain real work |
| PWA plus desktop Tauri only | Lowest immediate cost and preserves instant mobile delivery | Does not satisfy the confirmed native-mobile direction |
| Separate native mobile framework consuming shared contracts | Best platform-specific UX where needed | Highest engineering/release duplication; risks divergence from desktop/W.I.N.S. |

### 6.6 Veragensia Chromebook portfolio baseline

This baseline exists **because of Veragensia**. Its first native reference Agent Computer is Chromebook hardware, so that machine must be capable of presenting and operating the full ecosystem: Focusa Desktop, UIAI Cockpit and Evidence PWA, the Focusa and Wirebot browser extensions, Wirebot Desktop/mobile-compatible screens, W.I.N.S., and Veragensia’s own controls.

Two test lanes must remain distinct:

1. **Primary ecosystem lane — Veragensia on Chromebook hardware:** firmware/OS conversion has produced the supported Veragensia/Omarchy Linux Agent Computer. Linux/Tauri, browser/PWA and extension routes can participate in one integrated desktop.
2. **Secondary customer-access lane — stock ChromeOS:** unconverted consumer or managed Chromebooks use Chrome/PWA, Android and permitted Crostini routes. Success here does not prove the Veragensia-native system, and Veragensia-native success does not prove managed ChromeOS compatibility.

“Every app UI works fully on the Veragensia Chromebook” is the primary acceptance target, while the packaging route remains product-specific. Four routes are available and may be combined:

| Route | Advantages | Costs/risks | Best candidate uses |
|---|---|---|---|
| Responsive web/PWA | Native ChromeOS fit; instant updates; touch/mouse/keyboard; lowest installation friction | Browser storage/background limits; weaker filesystem, secure storage and OS integration; managed service required | Wirebot/W.I.N.S., UIAI Evidence/FPV views, read-focused Focusa surfaces |
| Android application on ChromeOS | Native store/update path; mobile and Chromebook reuse; better notifications/secure storage than PWA | Chromebook Android compatibility varies; window/keyboard behavior needs explicit QA; not every enterprise Chromebook enables Play Store | Wirebot Mobile, customer evidence and communication surfaces |
| Linux/Tauri through Crostini | Desktop code reuse and broad native capabilities on supported x86_64/ARM Linux environments | Linux enablement is user/admin friction; not universal on managed devices; packaging, display integration and updates need proof | Focusa Desktop and UIAI Cockpit professional/operator use |
| Veragensia-native Chromebook | Deepest Agent Computer integration, secure attention and governed execution | Firmware/device compatibility, destructive installation and hardware qualification; intentionally specialized rather than a general customer prerequisite | Veragensia reference Agent Computer |

#### Per-surface Chromebook audit

| Surface | Candidate Chromebook route | Current evidence | Gap to “fully working” |
|---|---|---|---|
| Focusa Desktop | Linux/Tauri inside Veragensia; optional responsive projection for stock ChromeOS | recovered `apps/desktop` branch source is a full-window Tauri cognitive cockpit | current-main reconciliation, Linux package/install, secure storage, release and complete device parity are unproven |
| Focusa Menubar | Linux/Tauri tray/companion inside Veragensia | current-main macOS-shaped Tauri companion exists | Linux tray/window adaptation, Desktop bridge, package/install and full device parity are unproven |
| Focusa browser extension | Chrome Manifest V3 | concept document only | no manifest, implementation, permission audit, store/release or Chromebook proof |
| UIAI Cockpit | Linux/Tauri inside Veragensia plus browser/PWA access where appropriate | Tauri source and extensive specifications exist | no proven Veragensia Chromebook package; current local source check fails; input, windowing, capture, evidence and control behavior need device proof |
| UIAI Evidence/FPV PWA | Chrome PWA | FPV is documented implemented and runtime EPWA envelopes were observed | installability, offline/readback, touch layout and admissible customer-scope publication need Chromebook proof |
| Wirebot browser extension | Chrome Manifest V3 | v0.2.2 manifest/build source exists | store/current-install proof, source reconciliation and real Chromebook browser testing absent |
| Wirebot/W.I.N.S. | Linux/Tauri or shared web frontend inside Veragensia; PWA/Android for stock ChromeOS | responsive Svelte screens and PWA assumptions exist | canonical source extraction, auth, native adapters, Veragensia integration, install/update and full device acceptance absent |
| Veragensia | native Chromebook/Omarchy on qualified hardware | Docs 186–189 specify Chromebook-first v0.1 and a Dell CC11260 reference path | explicitly proposed/not released; firmware, hardware, installer and full work-cycle evidence remain open |

#### Proposed Veragensia Chromebook acceptance contract—not yet adopted

On the qualified Veragensia Chromebook, prove the integrated portfolio: boot/login; Focusa Desktop launch and daemon pairing; UIAI Cockpit launch, browser/computer control and Evidence PWA use; installation and operation of both browser extensions; Wirebot/W.I.N.S. customer workspace; governed handoff to Veragensia execution; shared identity/scope resolution without ambient authority; keyboard, touch and pointer use; file handoff; notifications; camera/microphone where applicable; secure credential storage; offline/degraded behavior; update/rollback; deep links; evidence readback; and sign-out/revocation with zero residue. Measure cold start, idle/active memory, CPU pressure and concurrent-app behavior against the qualified hardware profile. Pixel inspection and real-device consumer testing are required.

A separate stock-ChromeOS matrix then proves customer-access routes through PWA, Android, Chrome extension or permitted Crostini. The primary ecosystem goal is **complete integrated operation on the Veragensia Agent Computer**, not an unsupported claim that macOS/Windows bundles execute directly on ChromeOS.

### 6.7 Agent-operation-complete baseline

The normative, testable requirements live in the [Agent-Operation-Complete Software Contract](./07-agent-operation-complete-software-contract.md). This is a default product requirement, not an optional accessibility layer. A first-party feature is incomplete when a human can operate it only through pixels, pointer gestures or private UI logic.

For every consequential UI action and readable state, the canonical feature owner provides:

- one versioned operation contract and stable operation identifier;
- strict machine-readable input/output schemas;
- authenticated, scoped API and documented CLI routes;
- the same authority, entitlement, confirmation and consequence classification across UI, API and CLI;
- idempotency/replay behavior for mutations;
- durable evidence/receipt references;
- bounded errors, diagnostics and recovery guidance;
- capability discovery, version negotiation and deprecation policy;
- producer, API-consumer, CLI-consumer and UI-parity tests;
- headless operation without visually controlling the UI.

The UI, API and CLI are adapters over the same owning service/operation. They do not maintain parallel business logic, state stores or permission rules. Layout may remain presentation-specific, but underlying state, selections, commands, exports, approvals and outcomes remain agent-readable and agent-operable.

#### Automation fallback ladder

1. **Canonical structured operation:** typed application operation, API, CLI, MCP/ACP binding or stable application protocol.
2. **Structured platform interface:** D-Bus, accessibility object model, DOM/WebMCP or another semantic interface only when no canonical operation exists.
3. **CUA absolute last resort:** visual recognition, pointer coordinates and keyboard emulation only when no structured route exists and the exact action is authorized.

CUA is never the normal integration among Focusa, UIAI, Wirebot, W.I.N.S. or Veragensia. Every first-party CUA fallback creates a named API/CLI parity defect, records why no structured operation was available, captures evidence and has bounded retry/stop behavior. UIAI can execute CUA safely; its availability does not make CUA the preferred route.

#### Current API/CLI parity audit

| Surface | Existing structured foundation | Current gap |
|---|---|---|
| Focusa Desktop | recovered source includes a Spec 135 operation registry over Focusa daemon operations | branch/main reconciliation and complete Desktop UI-action → API → CLI parity remain unproven |
| Focusa Menubar | current app consumes extensive Focusa daemon API and tool operations | no complete Menubar UI-action → API → CLI parity ledger or reconciled Desktop bridge proof |
| Focusa browser extension | concept references Focusa operations | no implementation, API/CLI surface or parity tests |
| UIAI Cockpit | UIAI HTTP/MCP/tool APIs and an engine executable entry exist | no supported complete UIAI CLI was proven; full Cockpit parity is unproven and the current checkout check fails |
| UIAI Evidence/FPV | current UIAI tools and web routes expose typed session/evidence operations | CLI parity and complete Cockpit/Wirebot consumer proof remain open |
| Wirebot extension | WordPress REST, websocket and extension APIs exist in parts | no complete operation registry or CLI parity |
| Wirebot/W.I.N.S. | scoreboard HTTP handlers and broad `wb` CLI families exist | screen-level operation schemas and parity coverage incomplete |
| Wirebot Desktop/mobile | intended to consume managed services | no app or consolidated operation/parity contract exists |
| Veragensia | Agent App Resolver and semantic operation registry prefer structured operations | full installed-app API/CLI inventory and reference-Chromebook parity proof incomplete |

### 6.8 Portfolio integration posture

For each outside UI, choose independently between deep link, shared contract/module, bounded embedded view, or full embedding. “One customer experience” does not require one executable containing every professional tool. Focusa Desktop, UIAI Cockpit, extensions and Veragensia keep their own canonical responsibilities unless an explicit later decision changes a boundary.

## 7. Gap and wrinkle register

### P0 — decisions required before implementation

1. **Source ownership:** record whether `wirebot-core` owns `apps/wirebot` and shared W.I.N.S. packages. ADLBOS should retain doctrine, not become application source.
2. **Product naming:** decide whether the public family is “Wirebot,” with Desktop/Mobile/Web as delivery targets. Avoid making “Desktop” the product name when the same frontend ships mobile.
3. **W.I.N.S. owner:** designate one canonical W.I.N.S. component source. Do not fork scoreboard Svelte screens and the WordPress PWA.
4. **Plan/entitlement schema:** Direct, network-enabled, Full AITL, personal-presence and Sovereign capabilities need one versioned manifest consumed by every shell.
5. **Direct runtime authority:** identify the initial managed VPS/runtime, tenant provisioning owner, capacity thresholds, backup/recovery, observability and scale-out path.
6. **Pricing activation:** reconcile `$299/$999`, `$5,000`, Full AITL pricing, `$250,000` personal-presence terms and the `$450,000/year` support floor without advertising unimplemented delivery.

### P0 — safety and commercial integration

7. **Engagement binding:** invoice contract version, first-payment acceptance, customer/project identity, purchased scope and scheduling entitlement must bind to the app workspace.
8. **Device/session scope:** local devices, remote Agent Computers and support sessions require scoped, revocable grants and receipts; discovery is not enrollment.
9. **Secret handling:** owner moments remain local and go directly to the owning vault/provider. Wirebot UI must not proxy or log raw secrets.
10. **Evidence authority:** UIAI remains canonical for evidence packet construction, integrity, redaction and resolution; Wirebot stores references and customer-facing projections.
11. **Tenant isolation:** W.I.N.S., Wirebot runtime, Focusa scope, UIAI sessions and Veragensia workloads must share exact customer/project identifiers without sharing ambient context.

### P1 — frontend consolidation

12. **Large W.I.N.S. shell:** split navigation, session, API and screen modules before packaging; avoid a second implementation.
13. **Shared design system:** define customer-facing tokens/components independently from Focusa/Cockpit operator UI, while reusing stable primitives where contracts allow.
14. **Native adapter layer:** replace/bridge service worker, install prompt, web push, background sync, Web Share, OAuth redirect, cookies/session storage and filesystem behavior for Tauri desktop/mobile.
15. **Responsive information architecture:** desktop, phone and tablet need the same objects but different navigation density; do not force desktop chrome onto mobile.
16. **Offline/degraded posture:** distinguish cached view, queued local action, unavailable managed service and revoked entitlement.
17. **Extension/app handoff:** define signed/deep-linked context transfer from Wirebot extension to the app without ambient page or cookie access.
18. **Cockpit/evidence handoff:** define packet resolver and session links rather than embedding broad UIAI operator privileges.

### P1 — distribution and operations

19. **Application identity:** package IDs, signing identities, update keys/channels and ownership do not yet exist for Wirebot desktop/mobile.
20. **Platform matrix:** macOS, Windows, Linux, iOS and Android build/sign/store requirements need explicit acceptance. “Tauri supports mobile” is not consumer proof.
21. **Release pipeline:** reproducible builds, SBOM/provenance, notarization/store review, updater rollback and supported-version policy are undefined.
22. **Installation/setup:** payment-to-download, first login, engagement binding, machine enrollment, readiness, recovery and uninstall/preserved-data flows need one tested chain.
23. **Support channel:** customer-visible session start/end, role, duration, revocation and receipt need implementation—not merely policy text.
24. **Direct capacity:** no load model, tenant density, model-cost budget, autoscaling trigger or dedicated-runtime migration proof exists.

### P2 — current inventory drift

25. **Focusa naming/status:** source is still called Menubar Preview while portfolio doctrine calls it Focusa Desktop.
26. **Focusa extension status:** defined only as a concept; no implemented Chrome extension was found.
27. **UIAI checkout drift:** inspected local UIAI source is far behind remote with substantial local work; establish a clean authoritative checkout before implementation review.
28. **Wirebot extension drift:** local source is ahead of remote and publication is unverified; reconcile before treating it as the customer extension.
29. **Veragensia release truth:** public proving-ground/source existence must not be presented as a finished native Agent Computer release.
30. **Audit scripts:** current Golden Path scripts detect substrate/runtime components, not the complete product UI installation set. Add UI detection only after package IDs and release contracts exist.
31. **Veragensia Chromebook integration profile:** Veragensia has Chromebook-first specifications, but no release profile currently installs, launches and proves the complete Focusa/UIAI/Wirebot/extension UI portfolio together.
32. **Two Chromebook lanes:** stock ChromeOS and Veragensia/Omarchy on Chromebook hardware have different security, packaging and administration models; neither currently proves the other.
33. **Reference-hardware capacity:** concurrent Focusa Desktop, UIAI Cockpit, Wirebot and browser/extension operation has no measured CPU/memory/startup baseline on the qualified Chromebook.
34. **Operation registry completeness:** no cross-product catalogue proves that every first-party UI action and readable state maps to canonical API and CLI operations.
35. **Parity test matrix:** UI/API/CLI producer and consumer tests are incomplete across the portfolio.
36. **CUA dependency ledger:** first-party workflows do not yet consistently classify CUA fallback as a defect requiring a structured replacement.

## 8. Candidate sequence after the open decisions

1. Record the product family, source owner, W.I.N.S. owner, entitlement schema and agent-operation-complete contract.
2. Inventory every UI action against its canonical API and CLI operation; file explicit parity/CUA gaps before consolidating screens.
3. Establish a clean `wirebot-core` implementation worktree and extract W.I.N.S. screens behind typed session/API interfaces.
4. Build one responsive Wirebot web shell from those canonical modules.
5. Package and prove desktop targets with Tauri.
6. Add native adapters and package the same frontend for iOS/Android; preserve the PWA as a derived web target.
7. Implement Direct provisioning on the initial managed runtime/VPS with tenant isolation and capacity evidence.
8. Implement engagement/payment/scheduling binding and Full AITL setup modules.
9. Integrate the UIAI customer evidence viewer while completing the full Evidence PWA integration in Cockpit.
10. Select and prove the supported Chromebook route for each UI against the shared acceptance contract.
11. Integrate Veragensia remote Agent Computer status, governed actions and receipts.
12. Prove every accepted workflow headlessly through API and CLI before permitting CUA fallback.
13. Run one paid pilot end to end before activating revised Full AITL/Direct pricing or claiming customer readiness.

## 9. Audit evidence and limits

- Inspected local source and current documents in ADLBOS, Focusa, Wirebot Core, UIAI Engine, Veragensia, Startempire Wire Network extension and the Startempire Wire PWA plugin.
- Inspected Git remotes, package/application identifiers, manifests and current worktree states.
- Inspected public Focusa/Wirebot purchase and homepage copy in the preceding sales audit.
- UIAI tools demonstrated current EPWA delivery envelopes, but evidence publication was blocked by missing admissible Focusa scope.
- Bounded validation jobs were attempted without installing dependencies: UIAI Cockpit `npm run check` returned nine current local type/import errors; Focusa Desktop and Wirebot Extension checks could not start because their routed environments lacked `svelte-kit`/`svelte-check`. These are explicit audit gaps, not release verdicts.
- A separately named external “Genesis Docs” source was not found in the local repository inventory, and the Google document CLI has no configured account. Its details remain operator-stated until that source is supplied or indexed.
- Existing source, manifests and plans do not prove app-store publication, installed customer usage, production Direct infrastructure or completed cross-platform release.
