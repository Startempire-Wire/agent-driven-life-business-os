# Agent-Operation-Complete Software Contract

- **Status:** operator-confirmed product baseline; implementation conformance remains evidence-dependent
- **Applies to:** all first-party Wirebot ecosystem applications, services, extensions and user interfaces
- **Reference deployment:** Wirebot, W.I.N.S., Focusa, UIAI Engine/Cockpit, Veragensia and their customer/operator surfaces
- **Primary hardware acceptance:** the qualified Veragensia Chromebook
- **Architecture choices not settled here:** Cockpit embedding, Wirebot frontend source owner, mobile packaging and portfolio shell boundaries

## 1. Product rule

Every first-party product is **agent-operation complete by default**.

A human-visible feature is not complete until an authorized agent can discover, inspect and operate the same underlying capability headlessly through both a versioned API and a noninteractive CLI. The UI, API and CLI are adapters over one canonical operation owner. They do not implement separate business logic, state, permissions or outcome semantics.

**Computer-use automation (CUA) is the absolute last resort.** UIAI may provide governed browser/computer hands, but its existence never makes visual clicking the preferred interface between first-party systems.

## 2. Scope

The contract covers:

- every consequential button, form submission, command, approval, export and state transition;
- every state, status, list, record, warning, receipt and result shown by a UI;
- setup, pairing, authentication, entitlement, configuration, update, rollback, sign-out and revocation;
- local, remote, offline/degraded and recovery paths;
- web/PWA, desktop, mobile, browser-extension and Agent Computer surfaces.

Pure presentation choices such as spacing, animation and decorative styling do not require standalone domain operations. Their inputs, preferences, accessibility state and rendered-evidence capture remain machine-readable where they affect behavior or acceptance.

## 3. One canonical operation

Every capability has one owning operation contract. API, CLI, UI controls, agent tools, MCP/ACP bindings and automation adapters reference that operation; they do not redefine it.

The normative structural schema is [`contracts/agent-operation.v1.schema.json`](../../contracts/agent-operation.v1.schema.json). Cross-field policy and runtime behavior still require the conformance tests below.

Minimum descriptor:

```yaml
schema_version: agent.operation.v1
operation_id: stable.owner.action
owner: canonical-product-or-service
summary: bounded human description
consequence_class: read | mutate | destructive | external_commitment
authority:
  required_capabilities: []
  exact_scope_fields: []
  confirmation: none | required | high_consequence
input_schema_ref: contract-or-schema-ref
output_schema_ref: contract-or-schema-ref
idempotency: none | optional | required
receipt: none | result | durable
errors: typed-error-catalog-ref
recovery: bounded-recovery-ref
api:
  transport: http | local_socket | rpc | application_protocol
  method: GET | POST | PUT | PATCH | DELETE | invoke
  route: stable-route
cli:
  argv_prefix: [stable, noninteractive, command]
  input: flags | stdin_json | flags_or_stdin_json
  output: json
discovery:
  catalog: machine-readable-catalog-ref
  introduced_in: semantic-version
  deprecated_in: null
```

The exact schema owner may vary by product, but equivalent semantics may not be omitted.

## 4. API completeness

A complete API surface provides:

1. machine-readable discovery and versioning;
2. strict request/response schemas;
3. explicit identity, tenancy, project/workstream and resource scope;
4. least-capability authentication and authorization;
5. entitlement and consequence classification;
6. confirmation requirements that cannot be bypassed by changing adapter;
7. idempotency and replay handling for mutations;
8. typed errors with retryability and recovery guidance;
9. durable evidence/receipt references for consequential operations;
10. pagination, bounds and cancellation for long or large work;
11. health/readiness distinct from successful business outcomes;
12. deprecation and compatibility policy;
13. producer, consumer and cross-version tests.

An undocumented internal endpoint, database access, websocket event or UI backend call is not automatically a supported product API.

## 5. CLI completeness

A complete CLI is a first-class API consumer, not a screen scraper or parallel implementation. It provides:

- one stable command for every supported operation;
- noninteractive execution without prompts when all required explicit inputs are supplied;
- `--json` or equivalent machine-readable output for success and failure;
- stable exit-status classes;
- stdin/file support for structured or sensitive inputs where command arguments would be unsafe;
- explicit target/scope flags rather than ambient inference for consequential work;
- confirmation controls that preserve the API consequence policy;
- idempotency-key support where the operation requires it;
- bounded timeouts, cancellation and progress/receipt handles;
- discoverable help generated from or tested against the canonical operation contract.

Human-friendly output may be added, but it never replaces the machine-readable contract.

## 6. UI completeness

Every actionable first-party UI control maps to its operation identifier. Every displayed domain state names or derives from a supported read operation.

The UI may orchestrate several operations as a declared workflow, but must expose:

- constituent operation IDs and order;
- partial-failure and retry behavior;
- current authority/entitlement state;
- pending versus accepted outcome;
- receipt/evidence references;
- rollback or compensating action where supported.

A hidden UI-only endpoint, local-only permission bypass or client-side state transition fails parity.

## 7. Agent tool completeness

Agent-facing tools are generated from or validated against the same operation catalogue. Tool discovery returns bounded metadata before full schemas are loaded. Tool calls preserve exact scope, authority, confirmation, idempotency, error and receipt semantics.

Agent tools do not obtain broader authority than API, CLI or UI users. Natural-language intent never substitutes for the operation’s typed scope or grant.

## 8. Automation fallback ladder

Use the narrowest available interface in this order:

1. **Canonical structured operation:** direct application operation, domain API, CLI, MCP/ACP tool or stable protocol.
2. **Structured platform interface:** D-Bus, accessibility object model, DOM/WebMCP or another semantic interface when the application lacks a canonical operation.
3. **CUA last resort:** visual recognition, pointer coordinates and keyboard emulation only after structured discovery proves no sufficient route.

First-party products must not integrate by opening and visually driving one another. Wirebot invokes UIAI, Focusa, W.I.N.S. and Veragensia operations; it does not click their interfaces. Embedding a UI does not change this rule.

### 8.1 Conditions for CUA

CUA is permitted only when:

- no supported structured interface can satisfy the operation;
- the exact application, session, target and action are scoped;
- normal authentication, consent, authority and consequence gates pass;
- pre-action state and expected outcome are observed;
- retries are bounded and possible effects are reconciled before replay;
- diagnostics and evidence are captured;
- credentials are handled through an approved broker and are not exposed to model-visible pixels or logs;
- the fallback records a named `structured_interface_gap` for first-party software.

Coordinate/pixel automation follows semantic accessibility/DOM automation; it does not precede it.

## 9. Parity proof

An operation is complete only when the same test vector passes through all applicable adapters:

| Proof | Required result |
|---|---|
| Contract | versioned descriptor and schemas validate |
| Service producer | owning service performs the operation and returns typed output |
| API consumer | supported client invokes it with exact scope and receives the canonical result |
| CLI consumer | noninteractive CLI invokes it and emits equivalent machine-readable result |
| UI consumer | control invokes the same operation and renders pending/success/failure honestly |
| Agent consumer | tool discovery and invocation preserve schemas, authority and receipts |
| Cross-version | supported client/server versions negotiate or fail explicitly |
| Recovery | retry, cancellation, rollback/compensation and duplicate behavior match contract |
| Evidence | consequential effects have durable references and consumer-visible acceptance |
| First-party no-CUA | normal successful path contains no visual UI automation |

“Equivalent” means the same operation identity, accepted inputs, authority decision, durable effect, error class and receipt—not merely similar text.

## 10. Conformance reporting

Audit status is reported without diluting the completion claim:

- **unmapped:** UI/state exists without an operation inventory;
- **contracted:** canonical operation and schemas exist;
- **API-complete:** supported API passes producer/consumer proof;
- **CLI-complete:** CLI parity passes;
- **UI-parity:** UI consumes the same operation;
- **agent-parity:** agent discovery/invocation passes;
- **accepted:** all applicable proofs, recovery and consumer acceptance pass.

Only **accepted** satisfies agent-operation complete for that capability. Product-level completion requires every in-scope capability to be accepted or explicitly excluded with an operator-approved rationale. The portable structural regression is `tests/agent-operation-contract-test.py`; each owning product adds its own producer and adapter acceptance suite.

## 11. Veragensia Chromebook acceptance

The qualified Veragensia Chromebook is the first integrated product proving ground. It must demonstrate:

1. boot and owner login;
2. machine-readable installed-capability inventory;
3. Focusa Desktop launch, pairing and complete API/CLI/UI parity;
4. UIAI Cockpit launch and structured browser/computer/evidence operations;
5. Focusa and Wirebot browser-extension discovery and supported operations;
6. Wirebot/W.I.N.S. workspace operation through UI, API and CLI;
7. governed handoff from Wirebot intent to Focusa authority to UIAI/Veragensia execution;
8. complete headless execution of the accepted workflow without CUA;
9. explicit CUA fallback proof for one external legacy application, without normalizing it;
10. receipt/evidence readback, revocation and zero-residue teardown;
11. concurrent CPU, memory, startup and pressure measurements on qualified hardware;
12. real-device pixel, keyboard, pointer and touch verification.

Stock ChromeOS compatibility remains a separate matrix for PWA, Android, Chrome-extension and permitted Crostini routes.

## 12. Current portfolio baseline

| Surface | Structured foundation observed | Completion status |
|---|---|---|
| Focusa daemon/CLI | broad API, CLI and native tool surface | partial; Desktop UI parity ledger absent |
| Focusa Desktop | Tauri preview consuming Focusa services | unmapped as a complete UI/API/CLI product |
| Focusa browser extension | concept document | unmapped/unimplemented |
| UIAI Engine | HTTP/OpenAPI, MCP/tools and engine executable entry | substantial foundation; no supported complete CLI was proven and full operation parity is not audited |
| UIAI Cockpit | Tauri/Svelte UI over UIAI services | partial; UI/API/CLI mapping and current build health incomplete |
| UIAI FPV/Evidence PWA | typed session/evidence routes and implemented runtime envelopes | partial; CLI and consumer acceptance incomplete |
| Wirebot `wb` | broad CLI families and service clients | partial; canonical operation catalogue incomplete |
| W.I.N.S. | responsive UI and scoreboard HTTP handlers | partial; screen-level API/CLI parity incomplete |
| Wirebot browser extension | Manifest V3 source plus REST/websocket integrations | partial; operation registry, CLI and release proof incomplete |
| Wirebot Desktop/mobile | intended shared application family | not implemented |
| Veragensia | agentability model, resolver and semantic-operation registry | partial; registry invocation and integrated product parity incomplete |

Source presence is not conformance. Each row requires operation-level evidence. The living first-pass inventory is the [Wirebot Ecosystem Agent-Operation Parity Audit](./08-wirebot-ecosystem-agent-operation-parity-audit.md).

## 13. Minimum implementation sequence

1. Inventory every UI control, readable state and background workflow.
2. Assign or locate the canonical owner and operation ID; delete duplicate behaviors.
3. Specify/version the operation and schema once.
4. Implement or reconcile the owning service.
5. Implement API and CLI adapters from that contract.
6. Bind UI and agent tools to the same operation.
7. Add parity, authority, error, recovery and cross-version tests.
8. Prove the accepted workflow headlessly without CUA.
9. Run real-device UI and Veragensia Chromebook acceptance.
10. Record and replace any remaining first-party CUA fallback.

This sequence does not authorize unrelated product architecture, release, installation or public pricing changes.

## 14. Product decision boundary

This contract remains valid whether UIAI Cockpit is separate, embedded, module-shared or deep-linked; whether W.I.N.S. is extracted into a new shell or wrapped in place; and whether mobile uses Tauri, Capacitor or another approved route. Those choices affect packaging and ownership. They do not relax API/CLI completeness or permit first-party CUA as integration.
