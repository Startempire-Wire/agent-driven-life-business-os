# Wirebot Application Family and Startempire Wire Integration Architecture

- **Status:** grounded architecture-options paper: operator-directed intent plus observed source/document evidence; implementation ownership and pricing remain open
- **Direction introduced:** 2026-09-13 during this documentation effort
- **Application family:** proposed Wirebot Web/PWA/Desktop/Mobile
- **Integration scope:** Startempire Wire community ecosystem plus Wirebot, W.I.N.S., Focusa, UIAI and Veragensia connections
- **Delivery truth:** architecture/documentation only; no canonical Wirebot Desktop source, release, installation or public application has been proven

## 1. Intent

Create one professional, high-quality Wirebot application family that gives appropriately entitled users a coherent way to participate in the Startempire Wire ecosystem, operate their Wirebot, compose an AI workforce and consume governed outcomes.

Startempire Wire currently runs substantially on WordPress. That is not a reason to reproduce WordPress pages inside a desktop window. Existing WordPress products may remain canonical domain owners and expose versioned endpoints consumed by native-quality Wirebot modules.

The application should support:

- a useful, inexpensive entry experience for community members;
- Wirebot Direct managed users;
- Full Agent-in-the-Loop (AITL) engagements;
- network/business users;
- Sovereign deployments that selectively federate with Startempire Wire;
- future clients using the same portable application contracts without inheriting private Startempire authority or data.

No public price is selected here.

## 2. Historical correction

AI Draftees and the current Startempire Wire WordPress experiences existed before a Wirebot Desktop application was considered. The operator first introduced the Wirebot Desktop/Web/Mobile family during this documentation work on 2026-09-13.

Therefore:

- old website boundaries do not prove future application boundaries;
- AI Draftees is useful domain and UX evidence, not a settled Desktop design;
- “move,” “embed,” “share,” “federate” and “retire” remain separate options;
- the new application must be designed from current outcomes, contracts and users rather than retrofitting a story that did not exist.

## 3. Evidence labels

- **Observed:** supported by the cited current repository/source/document; it is not automatically released or live.
- **Operator-directed:** explicitly stated by the operator as intended direction.
- **Candidate/open:** proposed interpretation, name, architecture or sequence requiring validation or decision.
- **Unverified:** not yet proven in source, runtime, deployed endpoint or customer-visible behavior.

## 4. Confirmed direction versus open choices

### 4.1 Operator-directed

1. Integrate the full Startempire Wire ecosystem **somehow** into the Wirebot application family.
2. Deliver a professional, coherent product—not a collection of raw admin pages or iframes.
3. Reuse suitable WordPress APIs/endpoints rather than reconstructing domain logic.
4. Use one entitlement-driven application family instead of separate plan-specific forks.
5. Support community, Direct and Sovereign/federated users with different authorized projections.
6. Consider an inexpensive Wirebot level for community members.
7. Preserve product/domain ownership and complete API/CLI/agent operation parity.

### 4.2 Candidate/open choices

- exact owning repository and framework for each Wirebot client;
- whether AI Draftees remains a separate public marketplace, becomes a Wirebot module, uses shared contracts or is retired after migration;
- exact community-tier capabilities, price, limits and support;
- which Startempire Wire screens remain public-web-first versus receive native app modules;
- identity/token issuer and account-linking flow;
- federation topology, discovery and revocation contracts;
- data residency and offline/cache policy;
- checkout and entitlement activation ownership;
- full Cockpit embedding versus governed projections/deep links;
- native desktop/mobile packaging and release infrastructure.

## 5. First-principles product rules

1. **One function, one canonical owner.** The app consumes domain operations; it does not copy business logic into every client.
2. **Module integration, not webpage accumulation.** Shared navigation/design can compose distinct products without pretending they are one backend.
3. **API first.** Public or first-party UI functionality requires a versioned domain operation with API, product CLI and agent-tool parity.
4. **No normal CUA.** Wirebot never clicks through its own websites to operate first-party features. Missing structured operations are parity defects.
5. **Entitlements select capabilities.** They do not create different application forks.
6. **Federation is explicit.** Sovereign nodes disclose only approved projections and retain local authority over private state.
7. **Community is useful at entry.** A low-cost tier must deliver a real outcome, not a crippled advertisement.
8. **Professional quality is systemic.** Identity, errors, loading, accessibility, privacy, updates, support and receipts are product features.
9. **Do not duplicate WordPress.** Retain WordPress where it is a suitable domain/CMS/commerce owner; replace only after evidence supports migration.
10. **Dispatch is not outcome.** W.I.N.S., evidence and acceptance remain distinct from activity feeds.

## 6. Candidate application architecture

```text
Wirebot Web / PWA / Desktop / Mobile
├── shared design system, navigation and entitlement renderer
├── local secure session/cache/notification adapters
├── Wirebot executive and workforce modules
├── Startempire Wire community modules
├── W.I.N.S. outcome modules
└── governed capability clients
    ├── Startempire Wire API gateway/domain adapters
    │   └── WordPress-owned REST APIs, webhooks and commerce/membership
    ├── Wirebot APIs and product-native CLI
    ├── Focusa governance, Workpoints, CRIST, evidence and receipts
    ├── UIAI browser/computer/evidence operations
    └── Veragensia Agent Computer operations
```

This is a logical boundary, not proof of a deployed gateway or settled repository.

### 6.1 Why a domain-adapter layer

WordPress plugins currently use multiple namespaces, authentication methods, schemas and release cadences. The application should not couple every view directly to plugin internals. A thin, versioned domain-adapter layer can:

- normalize identity, pagination, errors, timestamps and entitlement claims;
- preserve each plugin/product as canonical owner;
- expose stable app contracts while plugins evolve;
- avoid a second business database;
- translate federated and managed deployment routes;
- publish capability/version discovery;
- return source provenance and receipts.

The adapter is not a new owner of community, marketplace, payment, governance or execution truth.

## 7. Startempire Wire module map

The current site contains first-party plugin/source foundations for membership, network connection/parent coordination, the Wire/feed, smart listings, the Pitch, AI Draftees, Discord synchronization, PWA behavior and Wirebot provisioning. A separate Ring Leader exposes a `sewn/v1` REST namespace with content/auth/stats/provisioning responsibilities. Presence does not prove completeness or live readiness.

| Candidate app module | User outcome | Current likely domain owner/source | App treatment | Required audit |
|---|---|---|---|---|
| Community Home | see membership, relevant activity and next useful action | Startempire Wire membership/community stack | native summary/cards with deep links where suitable | identity, memberships, privacy, live routes |
| Wire Feed and Signals | discover current community/business signals | `sew-the-wire` and related signal sources | native feed contract with filters, provenance and actions | schemas, ranking, pagination, write actions |
| Opportunities and Jobs | discover, save, apply, dispatch or route opportunities | smart listings, job manager, Wire opportunities/bridges | native opportunity lifecycle module | canonical owner, application semantics, W.I.N.S. joins |
| Briefs and The Pitch | publish/consume structured business briefs and proposals | `sew-the-pitch` | native reading/composition where APIs are complete | draft/publish/approval parity and media |
| AI Draftees | browse worker profiles, reputation and availability; hire/link workers | `wire-draftees` WordPress plugin v0.1.0 | public marketplace/reputation candidate; private assignment via Workforce Composer | current live UX, API, checkout, dispatch, data and migration |
| Workforce Composer | select role hierarchy/task packs and assign bounded work | new shared contracts; likely Wirebot + Focusa governance | native app module | product owner, schemas, CRIST/authority/receipt integration |
| W.I.N.S. | view accepted outcomes, portfolio and evidence | Wirebot Scoreboard/W.I.N.S. | canonical shared Wirebot frontend modules | API extraction, tenancy, responsive/native acceptance |
| Events and Meetings | discover/coordinate relevant community events | WordPress event/community sources | native calendar/list or governed deep link | event source, RSVP operation and calendar authority |
| Discussions/Channels | communicate in approved community spaces | BuddyBoss/Discord bridges and Wirebot communications | notification/inbox/deep-link candidate | consent, channel identity, send permissions, moderation |
| Membership and Billing | understand plan, entitlement and account state | MemberPress/WooCommerce/Stripe-owned flows | secure account/entitlement module; hosted checkout where appropriate | source of truth, webhook receipts, cancellation/refunds |
| Wirebot Workspace | priorities, assistant, tasks, projects, workforce and settings | Wirebot product family | native primary workspace | canonical APIs/CLI, shared UI modules, tenancy |
| Governance and Mission | CRIST, Mission Canvas, Trajectory, Workpoints and approvals | Focusa | governed projection/deep link or bounded shared component | Desktop/Cockpit ownership and operation contracts |
| Execution and Evidence | browser/computer actions and visual proof | UIAI Cockpit/Engine | governed execution/evidence views, not copied engine | API/tool parity, EPWA delivery and review semantics |
| Agent Computer | device status, capabilities, requests and receipts | Veragensia | remote governed device module | Chromebook release/install and operation registry proof |

“Full ecosystem integration” means every domain has an intentional app relationship—native module, shared component, governed projection, deep link or explicit exclusion. It does not require moving every WordPress page into the app.

## 8. WordPress endpoint contract

A WordPress-backed module is app-ready only when its domain owner provides:

- explicit versioned namespace and operation identifiers;
- machine-readable schema/OpenAPI discovery;
- stable resource IDs and tenant/principal scope;
- renewable bearer/device/OAuth-style authentication—not browser-cookie dependence;
- least-privilege scopes and entitlement checks;
- clear public/read/write/destructive consequence classes;
- pagination, filtering, ordering and bounded payloads;
- idempotency keys for consequential retries;
- optimistic concurrency/revision handling where state can race;
- typed error codes with recovery guidance;
- rate-limit and freshness/cache metadata;
- webhooks/events for reliable change delivery;
- durable receipts for consequential mutations;
- revocation and account-unlink behavior;
- data export/deletion and retention boundaries;
- product-native CLI and agent-tool parity;
- producer, consumer, cross-version and live end-to-end proof.

The app must not parse HTML, depend on WordPress admin screens, store application passwords insecurely or treat a generic JWT as cross-tenant authority.

## 9. Identity, entitlement and federation

### 9.1 Identity layers

Keep these distinct:

- application installation/device;
- human principal;
- Startempire Wire community account;
- Wirebot tenant/workspace;
- Focusa project/workstream;
- Direct managed deployment;
- Sovereign node;
- linked third-party provider accounts.

An account link records a relationship; it does not merge authorities or private data.

### 9.2 Existing tiers and proposed offer overlays

**Observed current Wirebot tier contract:** `Free / Public`, `FreeWire`, `Wire`, `ExtraWire` and `Sovereign`; shared versus dedicated runtime and autonomy differ by tier. Current Wirebot vision also distinguishes standalone `wirebot.chat` customers from Startempire Wire network members. Full AITL and Wirebot Direct are established offer/service concepts in the Golden Path documentation, not replacements for the runtime tier contract.

| Layer | Current grounded meaning | Operator-directed/candidate application implication |
|---|---|---|
| Free / Public | shared minimal public/demo mode | public discovery only; exact modules require audit |
| FreeWire | shared per-life/business identity with low autonomy | first candidate mapping for an inexpensive community Wirebot experience |
| Wire | shared per-identity medium autonomy | richer community and workspace capabilities per entitlement |
| ExtraWire | shared per-identity high managed autonomy | broader managed/network capabilities per entitlement |
| Sovereign | dedicated managed runtime and stronger isolation | local/private operation plus explicitly approved federation projections |
| Wirebot Direct | established managed SaaS offer outside automatic Full AITL scope | may use eligible runtime tier plus linked community modules |
| Full AITL | established professional setup/delivery path | configured application/workforce/governance experience under contract |

“Community Companion” is only a possible customer-facing package name. It must first be reconciled with FreeWire/Wire rather than creating an improvised duplicate tier. Public pricing stays unchanged until capability, operating cost, support, checkout and contract language agree.

### 9.3 Federation envelope

Every cross-node request/projection should carry, as applicable:

- protocol/schema version;
- issuer node and verifiable identity;
- subject principal/organization pseudonymous reference;
- audience/target node;
- operation and exact resource scope;
- entitlement/capability reference;
- issued, effective and expiry time;
- nonce/idempotency/replay protection;
- minimum disclosed payload;
- provenance and freshness;
- evidence/receipt references;
- correction, revocation and dispute state;
- cryptographic signature/trust-chain reference.

Sovereign federation never grants the central community ambient access to private memory, credentials, files, calendars, messages, projects or agent-computer state.

## 10. Professional application experience

### 10.1 Information architecture candidate

```text
Today
Community
Opportunities
Workforce
Projects
W.I.N.S.
Evidence
Devices
Settings
```

The application renders only entitled/relevant modules. Community users should not see broken premium navigation; Sovereign users should see federation state clearly; Full AITL users should not need a different app.

### 10.2 Quality requirements

- shared design tokens, typography, icons, component states and motion;
- keyboard and screen-reader accessibility plus touch-sized mobile targets;
- deterministic loading, empty, offline, stale, unauthorized and failure states;
- responsive behavior across Chromebook, desktop, tablet and phone;
- secure local token/key storage and explicit sign-out/device revoke;
- deep links and notification routing to exact objects;
- optimistic UI only where server reconciliation is unambiguous;
- privacy-preserving diagnostics and support export;
- update/signing/release/rollback infrastructure for native clients;
- no unexplained product IDs, task IDs or governance jargon in customer UI;
- consistent source/freshness/authority indicators where decisions depend on them;
- browser pixel proof on every supported web target and real-device proof for packaged clients.

## 11. AI Draftees and Workforce Composer

Preserve potentially reusable AI Draftees domain objects:

- employee profile;
- department;
- role/title;
- skills/integrations;
- availability;
- hire/assignment relationship;
- dispatch;
- track record and W.I.N.S.;
- message/dispute lifecycle.

Do not assume the old price cards, WordPress templates, subscription semantics or profile layout survive. The future Workforce Composer additionally requires:

- role hierarchy and generic task packs;
- CRIST profile and client-specific interview disposition;
- capability/tool bundle;
- temporary/permanent and stateless/stateful posture;
- on-demand/event/scheduled activation;
- Workpoint/task/CallGraph linkage;
- authority, data, budget and supervisor refs;
- evidence, receipts, escalation and revocation;
- private client roster separated from public marketplace identity.

See the [Composable AI Workforce Catalogue and Client Assignment Matrix](./09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md).

## 12. Agent-operation completeness

Every consequential app control maps to one canonical product-owned operation. Do not invent route names in this architecture paper. Compile the exact operation catalogue from current owners and identify gaps for:

- community feed, membership and account state;
- opportunity, job and application lifecycles;
- brief/proposal draft, review and publication;
- AI Draftee discovery, hire, dispatch, messaging and dispute state;
- workforce roster, assignment, dispatch and schedule state;
- W.I.N.S. portfolio, outcome and evidence state;
- federation link, capability, projection and revocation state;
- entitlement and device state.

**Observed starting points, not completeness claims:** AI Draftees registers a `wire-draftees/v1` namespace; the Ring Leader source registers `sewn/v1`; Wirebot provides the `wb` CLI and Go service surfaces; Focusa and UIAI publish machine-readable capability discovery. Exact route/method/auth coverage still requires the integrated inventory in Phase 0.

## 13. Integrated product relook

Audit each product as part of one portfolio while preserving separate ownership:

| Product/surface | Decide | Prove |
|---|---|---|
| Startempire Wire website | public/community/commerce pages that remain web-first | current routes, accessibility, APIs, checkout and membership |
| AI Draftees | marketplace, module, shared-contract or retirement path | live behavior, data, APIs, hire/dispatch and W.I.N.S. |
| Wirebot Web/PWA/Desktop/Mobile | shell, modules, shared UI and package strategy | source owner, design system, operations and release paths |
| W.I.N.S. | canonical reusable customer modules | tenancy, APIs, outcomes and responsive/native behavior |
| Focusa Desktop/Menubar/extension | governance/cognitive cockpit boundaries | branch integration, installed runtime and operation parity |
| UIAI Cockpit/Evidence PWA | execution/evidence ownership and projections | build health, EPWA delivery, review and acceptance |
| Veragensia | Agent Computer/device integration | Chromebook release/install, capability registry and receipts |
| Network Ring Leader/connectors | gateway/federation responsibilities | endpoint inventory, auth, rate limits, trust and deployment |
| Sales/setup surfaces | offer/checkout/consent/activation joins | IDs, contract, payment, provisioning and customer acceptance |

The relook must distinguish **source exists**, **API works**, **app-integrated**, **released**, **installed/configured** and **customer-visible/accepted**.

## 14. Delivery sequence

### Phase 0 — evidence and ownership

1. Inventory live routes, repositories, WordPress plugins, data owners, APIs, auth, events, entitlements and deployments.
2. Perform current browser/pixel reviews of every user-facing product.
3. Reconcile duplicate concepts and name one canonical owner per concern.
4. Decide the AI Draftees/Workforce Composer relationship and application owner.

### Phase 1 — contracts and design system

1. Compile versioned shared identity, entitlement, module, task-pack, workforce, dispatch, evidence and federation contracts.
2. Produce API/CLI parity manifests for each domain.
3. Establish one accessible shared Wirebot design system and navigation model.
4. Define app telemetry, privacy, error and support contracts.

### Phase 2 — Community Companion vertical slice

1. Link a community identity through renewable secure auth.
2. Show entitlement and selected community feed/opportunity/profile data through versioned APIs.
3. Provide one genuinely useful bounded Wirebot assistant outcome.
4. Verify web/PWA/Chromebook behavior and receipts.
5. Measure operating cost and value before selecting price.

### Phase 3 — workforce and W.I.N.S.

1. Implement role/task-pack catalogue and private roster contracts.
2. Add Workforce Composer and supervised dispatch.
3. Link accepted results to W.I.N.S. and evidence.
4. Pilot with one existing client before broad availability.

### Phase 4 — Direct and Full AITL

1. Add managed private workspaces, integrations, onboarding and support boundaries.
2. Bind invoice/payment/consent to exact workspace scope.
3. Prove entitlement changes, downgrade, cancellation, export and revocation.

### Phase 5 — Sovereign federation

1. Implement signed node identity, capability discovery, minimum projections and revocation.
2. Prove no ambient private-data access or authority crossover.
3. Test network outages, stale data, replay, disputes and version skew.

### Phase 6 — packaged clients

1. Package Desktop/mobile only after shared web contracts and modules are stable.
2. Establish signing, secure storage, updates, rollback, crash/support and store/release proof.
3. Verify real Chromebook/desktop/mobile targets.

## 15. Acceptance criteria

The architecture is implementation-ready when:

- each Startempire Wire domain has a named owner and intentional app relationship;
- current WordPress and non-WordPress operations are inventoried live;
- duplicate/obsolete UI paths have migration or retention decisions;
- identity, entitlement and federation threat models pass review;
- a shared application/module contract and design system are approved;
- API/CLI/agent parity exists for the first vertical slice;
- Community, Direct, Full AITL and Sovereign acceptance suites are distinct;
- pricing claims map to implemented, supportable entitlements;
- source, release, installation, configuration and browser/device proof are tracked separately.

## 16. Source/evidence map

### Prior product and architecture documentation

- `README.md` and `AGENT_OS_GOLDEN_PATH.md` in this repository;
- `docs/agent-os-golden-path/06-wirebot-product-ui-options-inventory-and-consolidation-audit.md`;
- `docs/agent-os-golden-path/07-agent-operation-complete-software-contract.md`;
- `docs/agent-os-golden-path/08-wirebot-ecosystem-agent-operation-parity-audit.md`;
- `docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md`;
- Wirebot Core `docs/VISION.md`, `PRODUCTIZATION_ROUTE.md`, `TIER_RUNTIME_CONTRACT.md`, `TRUST_MODES.md`, `SOVEREIGN_WHITE_LABEL_DEPLOYMENT.md`, `CAPABILITIES.md` and `UNIFIED_ECOSYSTEM_ADMIN_UI_SPEC_2026-03-03.md`;
- Startempire Wire extension `README.md` and `docs/bigpicture.mdx`;
- AI Draftees `docs/WIRE-DRAFTEES.md`, `DISCOVERY-MAP.md`, `HIRE-FLOW-SPEC.md`, current templates and plugin source;
- Focusa Specs 135, 135B and 174;
- UIAI Cockpit/evidence specifications already cited by the UI inventory;
- Veragensia Chromebook and semantic-operation specifications already cited by the UI inventory.

### Current source observations used here

- AI Draftees repository: clean `main` at inspected commit `cad3e12`; plugin header version `0.1.0`; product document still marked Draft v1; live/customer readiness unverified.
- Ring Leader source: `sewn/v1` REST controller plus separate authentication implementation; completeness and production suitability unverified.
- Startempire Wire plugin directory: multiple first-party WordPress products register REST routes; endpoint-by-endpoint conformance is unfinished.
- ADLBOS: no canonical Wirebot Desktop source, package, release or installed application was proven.

Operator statements in this session are the authority for the newly directed app-family integration, the desired professional quality, potential WordPress endpoint reuse, community affordability and Direct/Sovereign federation intent. They do not prove implementation.

## 17. Not done if

- the “Desktop app” is an iframe or browser wrapper around WordPress;
- first-party workflows require CUA;
- a copied app database competes with WordPress or another canonical owner;
- community and Sovereign identities are implicitly merged;
- federation exposes private tenant context by default;
- a cheap tier is priced before its cost/value/support envelope is known;
- AI Draftees is copied or deleted without current evidence and migration proof;
- passing source tests are presented as a released customer product;
- the app looks unified while authority, errors, support and data boundaries remain fragmented.
