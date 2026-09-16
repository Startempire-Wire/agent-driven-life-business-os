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

## 12. Offline and cached projections

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

## 13. Federation

Cross-Operator federation follows the same reference/freshness laws plus explicit federation issuer/audience/scope/expiry/revoke semantics.

A federated ref never grants ambient access to the referenced Operator's private state.

The receiving Operator resolves only what the federation grant explicitly exposes.

---

## 14. Required negative proofs

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

## 15. Non-goals

Do not create:

- a universal ADLBOS database;
- a global object registry merely to resolve refs;
- a new central event bus;
- a new global clock service;
- a duplicate approval/entitlement/credential authority;
- a scheme that requires every product to use the same internal primary-key format.

The contract exists so independently owned products can interoperate without collapsing their boundaries.
