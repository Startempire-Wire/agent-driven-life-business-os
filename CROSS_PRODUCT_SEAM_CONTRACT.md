# Cross-Product Seam Contract

**Status:** LIVE portable integration contract  
**Architecture owner:** `CURRENT_ECOSYSTEM_ARCHITECTURE.md`  
**Purpose:** define the minimum rules that make ADLBOS cross-product references, freshness, replay and source resolution safe across Wirebot, Focusa, Focusa Workforce, UIAI, Veragensia, W.I.N.S., MeriFolio and optional federation.

This contract does **not** create a new service, registry, clock, database, event bus or authority layer.

It standardizes what product-owned adapters must preserve when information crosses a product boundary.

---

## 1. Core law

> **A reference identifies source-owned state. It does not copy that state and it does not grant authority over it.**

> **A timestamp describes time observed by a participant. It does not establish global causal order.**

Cross-product consumers resolve current state through the owning product before consequential action.

---

## 2. Portable reference law

Bare IDs are not assumed to be globally unique.

A cross-product reference MUST carry enough source context to identify the owning namespace/domain and object kind without guessing from the ID string.

Conceptual shape:

```text
OperatorRef {
  domain
  kind
  id
  owner_ref?
  environment_ref?
}
```

Products MAY encode this as a URI, typed object, generated contract or opaque string plus typed/source fields. ADLBOS does not require one transport encoding.

Required semantics:

- `domain` identifies the canonical owner or contract namespace;
- `kind` identifies the referenced object class;
- `id` is opaque to consumers unless the owning contract explicitly defines parsing;
- `owner_ref` / `environment_ref` are included where tenancy or multi-environment ambiguity exists;
- references should remain stable across UI routes, display-name changes, process restarts and body/runtime replacement unless the owning object itself changes identity;
- no consumer infers authority, entitlement, tenancy or object type from a convenient string prefix alone;
- references MUST NOT contain reusable secrets or unnecessary private data.

Examples of reference kinds include:

```text
owner
environment
partner
delegation
project
workstream
foreman
work
workpoint
agent
attention
evidence
receipt
execution
runtime
body
outcome
federation_grant
credential_use
```

Product-specific kinds remain owned by their product contracts.

### 2A. SOVOS Operator Environment seam

`operator.environment.v1` identifies the owner-specific deployment substrate. It is a portable projection, not a provisioning authority.

For a complete **dedicated full-Sovereign Operator Environment** it MUST establish:

~~~text
one Canonical Owner Principal
one dedicated persistent VPS for that owner
one owner-specific Tailscale tailnet/private mesh
at least one owner-controlled local body on that tailnet
one durable Operating Partner ref
cloud_vps | local_body | hybrid residency
single-writer/reconcile coordination
shared_runtime_allowed = false
~~~

Consumers MUST NOT infer this state from:

- a Wirebot tier label;
- a workspace being active;
- a shared LBI existing;
- Tailscale reachability alone;
- a VPS hostname alone;
- an OpenClaw process being healthy.

This v1 contract deliberately does **not** model non-full-Sovereign Startempire/operator-managed isolated containers. Managed execution must use the existing owning provider/tenant identity, isolation, grants and lifecycle authority; it is not equivalent to a dedicated VPS/mesh merely because a customer has a Wirebot identity. Do not modify the v1 schema or reuse its status label as a shortcut. A broader portable contract requires separate proven consumer demand and versioned migration.

Moving the Operating Partner between cloud/local bodies changes runtime placement, not owner identity or partner identity.

---

## 3. Reference resolution

When a consumer receives a cross-product reference:

1. validate supported namespace/kind/version;
2. preserve the original ref unchanged for correlation/audit;
3. resolve through the owning product or trusted adapter;
4. verify current owner/tenant/environment scope;
5. verify current state/revision/freshness;
6. verify current authority separately;
7. perform the requested operation only through the owning contract.

A valid reference to an existing object can still be unusable because it is:

```text
unauthorized
unentitled
revoked
expired
stale
moved/rebound
incompatible
unavailable
```

Reference validity is therefore distinct from operation authority.

---

## 4. Common actionable envelope

Actionable cross-product envelopes SHOULD carry, as applicable:

```text
schema
schema_version
producer
producer_version
source_ref
source_revision
owner_ref / tenant_ref
environment_ref
actor_ref
correlation_id
issued_at / observed_at
expires_at
idempotency_key / replay_key
payload refs + intent
```

Not every read-only projection needs every field.

Consequential mutation paths need enough information to detect stale state, incompatible contracts, duplicated requests and actor/scope mismatch.

---

## 5. Version compatibility

Rules:

- unsupported consequential schema/major versions fail closed;
- additive-field compatibility is explicit per contract, not assumed globally;
- consumers must preserve unknown opaque refs they are allowed to relay even when they cannot interpret the referenced object's private schema;
- producers should not repurpose an existing field with incompatible semantics;
- contract migration must not silently widen authority or tenancy.

Version negotiation is a compatibility concern, not an entitlement or authority grant.

---

## 6. Time and causal-order law

Distributed ADLBOS systems may run on browsers, Chromebooks, VPSs, Agent Computers, containers and third-party services with imperfect clock agreement.

Therefore:

```text
wall-clock timestamp != causal order
wall-clock timestamp != authority proof
```

Use product-owned monotonic/causal mechanisms where available:

```text
revision
sequence
event cursor / epoch
generation
lease version
ETag/version token
idempotency record
```

Wall-clock values remain useful for:

```text
human presentation
freshness hints
expiry windows
support/audit context
```

but a consumer MUST NOT decide which conflicting mutation is newer solely by comparing clocks from independent systems.

---

## 7. Expiry and clock skew

Time-bounded grants, handoffs, attention actions and credential-use requests SHOULD declare their source/issuer time basis and expiration semantics.

Consumers must tolerate a bounded configured clock-skew window where the owning security/product contract permits it.

Rules:

- issuer/owner remains authoritative for grant expiry where possible;
- when local clock confidence is insufficient for a consequential decision, revalidate with the source rather than guessing;
- already-expired state fails closed for new consequential action;
- a stale cached item may remain visible with degraded status;
- reconnect triggers source revalidation before mutation from cached approval/grant/entitlement/execution state.

Do not create a new global time service merely to satisfy this contract.

---

## 8. Replay and ambiguous completion

A retryable consequential operation SHOULD carry product-owned idempotency/replay semantics.

When a network/tool failure leaves outcome unknown:

```text
reconcile current source state
→ inspect request/idempotency receipt if supported
→ retry only when owning semantics prove safe
```

Never blindly replay a consequential mutation because the caller did not receive a response.

Event replay reconstructs projections; it does not replay mutations.

---

## 9. Attention state

For `operator.attention.v1`:

```text
presenter seen/acknowledged/hidden/snoozed
!=
source approved/denied/resolved/cancelled/expired
```

A surface may keep local presentation acknowledgement.

The source domain owns resolution.

Before consequential action from an attention item, resolve the current source revision/state.

`operator.attention_policy.v1` is the owner-scoped portable delivery/reply policy referenced by routine `attention_policy_ref` values. It may define notification classes, approved channel refs/fallbacks, quiet hours, coalescing, reply posture/consequence ceiling, lock-screen privacy and lifecycle revision. It grants no source resolution, channel credential, execution permission or transport entitlement.

Delivery-channel state remains presentation state:

```text
notification published / delivered / read / cleared / deleted
!=
source resolved / desired outcome verified
```

A channel adapter such as ntfy may carry a stable correlation/sequence ID so one owner-visible notification evolves with one meaningful thread. That transport identifier MUST NOT replace the source attention/follow-through reference.

Inbound owner responses from a channel are attributed inputs, not ambient commands. Route them through the verified Operating Partner/owner session, preserve correlation/provenance, and revalidate authority before consequential execution.

---

## 10. Credential-use references

`operator.credential_use_ref.v1` is a specialized opaque reference/use request.

It may identify:

```text
credential_ref
provider/account ref
requesting actor/work ref
requested operation/scope
consequence/approval policy ref
validity/expiry
correlation
```

The credential authority resolves or denies it at execution time.

The reference MUST NOT expose the reusable secret itself.

Possession of the reference is not authorization to use the credential.

---

## 11. Correlation versus ownership

`operator.correlation.v1` joins a causal story without becoming an object owner.

A correlation may connect:

```text
owner
partner/delegated human
assignment
Workstream / work
worker/session/runtime
UIAI execution
Evidence
Receipt/settlement
accepted outcome
```

Each object remains owned by its source product.

Correlation IDs should be stable through retries/recovery where the logical request is the same, while product-owned idempotency keys may have stricter operation-specific rules.

---

## 12. Routine candidate, pack, template, blueprint, instance and leverage seams

`operator.routine_candidate.v1` is the source-backed audit inference that explains why a routine is being proposed, which evidence class supports it, what burden/outcome it addresses, which templates match, what human boundary applies, and what authority/reliability gaps remain. It is not a schedule, assignment or authority grant.

`operator.routine_pack.v1` is a composable suggestion bundle for a life/business operating shape. It points to owner-neutral templates and MUST remain explicitly non-identitarian: a pack helps the compiler ask which routine families are worth checking, not which routines a person or business must run.



`operator.routine_template.v1` is an owner-neutral reusable pattern. It carries generic fit signals, trigger preferences, step skeleton, human boundaries, reliability defaults, measurement defaults and bindable parameters. It MUST NOT carry customer private payload, active credentials, grants, exact schedules or canonical work state.

`operator.routine_blueprint.v1` is the owner-specific portable compilation/reference envelope for one discovered or proposed routine. It may carry owner/portfolio/business/life-domain refs, purpose and desired-outcome refs, source/provenance refs, triggers, step classes, role/assignment/Workstream refs, authority/budget/credential-use refs, execution placement, reliability/overlap/retry/missed-run/revoke refs and measurement-plan refs.

It is not the canonical schedule, task graph, roster, Evidence or outcome store.

`operator.routine_instance.v1` is the compiled binding of one accepted blueprint revision. It may bind template lineage, exact owner/domain scope, trigger/scheduler refs, Focusa assignment, typed operation/decision/prompt contract refs, authority/credential-use refs, reliability semantics and acceptance refs. It MUST NOT become the canonical scheduler, work store, credential store or Evidence ledger.

A template update MUST NOT silently mutate an active routine instance. Material changes require a new instance revision or governed update.

`operator.leverage_snapshot.v1` is a source-qualified projection used to connect operational evidence to owner-facing progress. It may carry scope/time window, routine refs, source metric/Evidence/receipt refs, accepted-outcome refs, capacity/time buyback, reliability/recovery, cost/attention trend, cross-routine/business reuse, risk reduction, opportunity unlocked, momentum signal, confidence/attribution limits and season/milestone refs.

No universal numeric score is required. `operator.leverage_snapshot.v1` is part of the **base private ADLBOS feedback loop** and does not require W.I.N.S.

Source domains retain their outcome truth and telemetry. Wirebot/Perpetua may synthesize the cross-domain private leverage/momentum projection from source-qualified refs. W.I.N.S., when enabled for the current setup, may consume that projection and add its own season/score/recognition/community semantics.

A leverage snapshot MUST NOT count agent/tool activity as an accepted outcome, double-count one shared gain across several businesses without disclosed attribution, treat estimates as proven fact, grant authority/scheduling/autonomy, or hide regressions behind an aggregate score.

Scheduled routine activation uses OpenClaw's persistent Automations scheduler by default in the current architecture, while product-native/provider/native deterministic schedulers remain valid when explicitly stronger. The schedule binds an exact routine-instance revision rather than reinterpreting the latest template/blueprint at run time. Focusa remains the governed-work/authority owner and is revalidated before consequential execution.

---

### 12.1 Agent-first progression, Buyback, and evolutionary inspection seam — target contract

This is an **additive target** over the existing source-qualified operator.leverage_snapshot.v1, not an in-place redefinition, new authority, backend, event bus, score ledger or mandatory W.I.N.S. dependency. The base snapshot schema and its existing consumers remain compatible. Any necessary new numeric Buyback/retrospective fields require a separately versioned schema or a backwards-compatible existing projection; do not slip an undocumented field into the current v1 as if consumers have adopted it.

Proposed **logical capabilities** (operation names, not claims of installed HTTP paths, CLI commands or activated grants):

| Capability | Read/write and owning boundary | Required effect |
|---|---|---|
| operator.progression.read | Wirebot/Perpetua private source-qualified read projection | Current owner-goal gap, accepted outcome, momentum, leverage/capacity and incomplete coverage |
| operator.buyback.inspect | Wirebot read synthesis over owner/source routine analytics | Gross/estimated/realized/net/protected/reinvested time or money, recurrence, cost, confidence and overlap |
| operator.progression.lineage | Read, with current source resolution and redaction | Goal → work/routine → effect → receiver verification → memory-eligible learning → leverage and next candidate |
| operator.evolution.inspect | Read Focusa-governed and Core component evidence | Baseline/variant, hypothesis, protocol, held-out results, current gate, costs, regression/rollback; no architecture change power |
| operator.feedback.propose | Governed candidate through existing owner correction/approval path | Owner correction, objection, reflection or accept/reject; no silent direct memory promotion, grant or outcome settlement |

Each operation MUST have equivalent meaning across authenticated API, CLI, agent tool/skill, Core/W.I.N.S. projection and Wirebot App. It may be offered through different approved transports; UI access is never a prerequisite. The owning product registers the exact operation, supported version, typed argument/error shapes and capability/entitlement before consumers advertise it. SOVOS does not assign fake endpoints or unverified command names. W.I.N.S. public/community reads are separate **disclosure projections**, not the private operations above.

Minimum qualified read envelope (logical fields, NOT an implemented schema): schema/version; owner/tenant/workspace and subject/scope refs; source owner/type/revision/time; observed-at and effective window; permissions and privacy class; coverage/completeness/freshness; accepted outcome and independent receiver refs; routine/work/effect correlations; leverage_snapshot_ref; measured-vs-estimated-vs-owner-reported distinctions; attribution/contrary evidence; uncertainty/confidence; evaluation protocol/baseline; current disposition/next permitted action. Large or private bodies remain with owning sources and are fetched only via current least-privilege resolution. Sources disagreeing or unavailable stay disputed/unknown, never zero or green.

**Buyback semantic distinctions:** Gross avoided work is not net capacity; reported or forecast time saved is not realized time; one-time savings never recur by default; monthly, weekly and annual windows require time-zone-aware normalization and validity periods; recurring savings expire or are revalidated when a routine fails, is retired, or the baseline changes. Net Buyback subtracts monitoring, human oversight, exception recovery, tool/compute, maintenance and new dependencies in commensurate units. Do not double-count a shared improvement across businesses, routines, workers, or overlapping time intervals. Protecting and choosing not to spend recovered capacity is a legitimate positive outcome. Score bonuses are optional W.I.N.S. presentation policy, never a causal or financial benefit claim.

**Three evidence planes:** (1) verified external reality / accepted source outcome; (2) observed operational behavior / execution and resource cost; (3) owner-controlled private reflection and preference. Keep them separately typed and private; no happiness score, personality inference as permission, automatic behavioral penalty as value truth, or disclosure of reflection into W.I.N.S. public standing.

**Agent-first negative conformance:** W.I.N.S. disabled / no browser / app unavailable still returns the identical private outcome/Buyback semantics by API/CLI/agent tool; foreign tenant, expired or revoked owner, missing source, partial pagination, stale source version, off-line cache, duplicate event, uncertain provider result, delayed correction, unsupported contract, inconsistent metric units and disallowed disclosure all fail with truthful scoped disposition. W.I.N.S. enablement never confers Network or federation rights. Operator feedback does not by itself approve an architectural change, authorize a financial effect or settle a source outcome. Prove API↔CLI↔agent↔App↔W.I.N.S. consumer parity against the **same** qualified refs, plus a second tenant/second business and a W.I.N.S.-off fixture.

Canonical homes: Freedom & Leverage §11A for value semantics; Master Loop 08 §11 for the Observer; Core W.I.N.S. docs02/17 for restoration, community/public projections and legacy migrations; Wirebot App docs13/20 for the primary integrated UI. Current legacy /v1/scoreboard and /v1/buyback APIs must not be represented as already satisfying this seam.

---

## 13. Offline and cached projections

A cache is explicitly a projection.

Every cached consequential projection needs enough metadata to render one of:

```text
fresh
stale
unknown
unavailable
incompatible
```

Offline UX may continue read-only orientation where safe.

Mutation from stale cached authority/attention/entitlement/grant state requires source revalidation.

No UI should convert "last known allowed" into "currently authorized" merely because the source is unreachable.

---

## 14. Federation

Cross-Operator federation follows the same reference/freshness laws plus explicit federation issuer/audience/scope/expiry/revoke semantics.

A federated ref never grants ambient access to the referenced Operator's private state.

The receiving Operator resolves only what the federation grant explicitly exposes.

---

## 15. Required negative proofs

Implementations consuming these seams should prove, where applicable:

```text
same bare ID from two environments does not collide
unknown consequential schema version fails closed
stale cached approval cannot mutate source state
clock disagreement does not reorder source revisions
expired grant/reference use is denied or revalidated
ambiguous mutation is reconciled before retry
presenter acknowledgement does not resolve source action
credential-use ref leaks no reusable credential
reference possession alone grants no authority
```

---

## 16. Non-goals

Do not create:

- a universal ADLBOS database;
- a global object registry merely to resolve refs;
- a new central event bus;
- a new global clock service;
- a duplicate approval/entitlement/credential authority;
- a scheme that requires every product to use the same internal primary-key format.

The contract exists so independently owned products can interoperate without collapsing their boundaries.
