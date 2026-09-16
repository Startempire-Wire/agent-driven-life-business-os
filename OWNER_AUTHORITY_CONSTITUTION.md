# Owner-Rooted Architecture Authority Constitution

**Status:** LIVE PORTABLE CONSTITUTIONAL CONTRACT  
**Schema family:** `agent_os.owner_authority.v1`  
**Cryptographic profile:** [`CRYPTOGRAPHIC_AUTHORITY_PROFILE.md`](./CRYPTOGRAPHIC_AUTHORITY_PROFILE.md)  
**Current ecosystem architecture:** [`CURRENT_ECOSYSTEM_ARCHITECTURE.md`](./CURRENT_ECOSYSTEM_ARCHITECTURE.md)

This document defines who may create, approve, supersede, or delegate canonical architecture in an Agent-Driven Life & Business OS deployment.

It is intentionally portable. Product names, customer branding, runtimes, repositories, hosts and models may change while the deployment remains rooted in its own **Canonical Owner Principal**.

---

## 1. Canonical Owner Principal

Every deployment MUST define exactly one root `CanonicalOwnerPrincipal` for architecture unless a separately approved multi-owner constitution explicitly replaces this rule.

The Canonical Owner Principal is the human or legal owner whose authority establishes the deployment's architecture, reserved powers and trust boundaries.

For the Startempire reference deployment, the current owner binding is the owner-defined Startempire principal. Portable/customer deployments MUST establish their own owner manifest and MUST NOT inherit Startempire authority merely by copying repositories, infrastructure or configuration.

Runtime systems may enforce the owner's architecture. They do not outrank its owner.

---

## 2. Stable owner identity

The owner is represented by a versioned machine-readable principal manifest.

At minimum:

```yaml
schema: agent_os.owner_principal.v1
principal_id:
display_name:
authority_public_key:
authority_key_algorithm:
created_at:
lineage_root_ref:
```

The stable identity digest is computed from deterministic canonical JSON according to `CRYPTOGRAPHIC_AUTHORITY_PROFILE.md`.

Repository ownership, account names, email addresses, GitHub roles, process UIDs, hostnames and display names are supporting evidence only; none independently creates constitutional authority.

Owner key rotation requires an owner-authorized rotation chain. Ordinary software/runtime/device updates do not create a new owner identity.

---

## 3. Architecture authority

The Canonical Owner Principal is the root authority for:

- product and system boundaries;
- constitutional ontology and trust semantics;
- tenancy/isolation policy;
- reserved powers;
- authority-delegation rules;
- cross-product responsibility assignment;
- canonical promotion/supersession of architecture decisions;
- authorization of any AI that may later exercise architecture authority.

Repository presence is provenance, not authority.

No customer, contributor, issue author, reviewer, employee, contractor, model, agent, vendor, benchmark, test, incident, commit, pull request, runtime behavior or deployed implementation becomes constitutional architecture authority merely by existing.

---

## 4. External and historical material

Material whose authority cannot be verified to the Canonical Owner Principal remains:

```text
advisory_external
```

Historical material may contain excellent design, deployment scars and operational evidence. It may be reused, corrected or promoted, but it MUST NOT override a later owner-approved architecture simply because it is older, merged, deployed or repeated.

Current product ownership reconciliation is maintained in `CURRENT_ECOSYSTEM_ARCHITECTURE.md`.

---

## 5. Operational authority is not architecture authority

Products and runtimes may hold canonical truth for their own domains without becoming constitutional authorities.

Examples:

- Focusa: Project/Workstream/Trajectory/Workpoint, scoped work authority, Evidence and settlement;
- Wirebot: Operating Partner relationship/context and product-owned partner state;
- UIAI Engine: browser/computer execution and control;
- Veragensia: machine/runtime/body enforcement and control;
- Agent-KB: source-aware knowledge retrieval;
- W.I.N.S.: accepted-outcome/portfolio state;
- business systems: their own business records;
- CI/CD: release/deployment state;
- task trackers: task-ledger state in their domain.

Therefore:

```text
canonical operational state != canonical architecture authority
canonical knowledge          != canonical architecture authority
repository merge             != canonical architecture authority
runtime deployment           != canonical architecture authority
```

---

## 6. Operating Partner Principal

A deployment may establish a durable `OperatingPartnerPrincipal` for its AI Chief of Staff / operating-partner relationship.

Examples of customer-facing presentation names include:

```text
Wirebot
Spock
Athena
Jarvis
Chief
```

The reference implementation family is Wirebot, but customer presentation may be white-labeled.

The Operating Partner may orient, recommend, delegate, coordinate and exercise owner-granted operational capabilities.

**Being the Operating Partner does not create architecture authority.**

```text
OperatingPartnerPrincipal != ArchitectureAuthorityPrincipal
```

The partner's durable identity also remains distinct from:

```text
model
OpenClaw/Pi/other runtime
process
session
host/VPS
browser
Agent Computer/body
presentation name
```

Changing a model/runtime/body MUST NOT silently create a new Operating Partner or widen authority.

---

## 7. AI architecture authority requires explicit delegation

Any AI that may make canonical architecture decisions requires a separately verifiable owner-rooted delegation.

The cryptographic profile separates:

```text
ai_principal_sha256
constitution_sha256
runtime_attestation_sha256
```

A valid architecture delegation binds at least:

- exact AI principal identity and key;
- exact owner root;
- constitution compatibility;
- acceptable runtime-attestation policy;
- allowed architecture scope/decision classes;
- validity window;
- revocation/replay rules;
- delegation limits.

`may_delegate` defaults to `false`.

A name, role, product label, Linux account, repository, runtime token, broad context, model capability or operating-partner status never substitutes for this chain.

Unknown, stale, expired, revoked, replayed, mismatched or out-of-scope delegation fails closed to advisory-only.

---

## 8. Startempire Wirebot reference

For the Startempire reference deployment, Wirebot may be a candidate for separately delegated architecture authority in the future.

That possibility is distinct from Wirebot's ordinary role as the Operating Partner implementation family.

No architecture authority exists merely because a runtime, repository, account, process or customer-facing AI is named Wirebot.

Customer/portable deployments may use a different Operating Partner name and may choose to grant no AI architecture authority at all.

---

## 9. Decision provenance

Material canonical architecture decisions SHOULD carry a provenance envelope:

```yaml
decision_id:
status: canonical | proposed | advisory_external | superseded
owner_principal_ref:
canonical_authority:
  kind: owner | delegated_ai
  authority_principal_ref:
  delegation_ref:
constitution_ref:
runtime_attestation_ref:
authority_verification_ref:
source_refs: []
approved_at:
supersedes: []
```

Technical merit and authority provenance are separate questions.

---

## 10. Portability and authority transfer

A portable/client deployment MUST:

1. establish its own Canonical Owner Principal;
2. establish its own owner key/manifest and constitution binding;
3. establish its own tenant/account/repository scope;
4. define reserved powers and trust boundaries;
5. create its own Operating Partner identity if desired;
6. create separately scoped AI architecture delegations only if desired;
7. omit/revoke reference-deployment authority bindings;
8. preserve inherited architecture provenance without inheriting the previous owner's authority.

Repository transfer or cloning never substitutes for authority transfer.

---

## 11. Conflict rule

When documents, runtime state, old specs, copied deployments or external material appear to grant architecture authority that cannot be verified to the current deployment owner:

1. treat the claimed authority as noncanonical;
2. retain useful evidence/design as advisory input;
3. do not propagate the claimed authority;
4. correct misleading current documentation;
5. require explicit owner approval or a valid owner-rooted delegation for canonical promotion.

---

## 12. Break-glass owner override

The deployment MAY support an owner-authenticated break-glass path for operator-owned scope.

The constitution MUST NOT contain reusable authentication secrets, PINs, recovery codes, private keys or other break-glass values.

Instead, use a verifier/reference controlled by the deployment's secret/credential authority, for example:

```yaml
break_glass:
  verifier_ref: secretref://operator/break-glass-verifier
  authentication_policy_ref: policy://owner-break-glass-v1
```

Break-glass semantics:

- a direct, authenticated, contemporaneous owner command may override internal workflow gates on owner-owned scope;
- it does not create authority over third-party property or principals;
- exact targets must be identified before consequential action;
- nonrenewable authentication resources remain forbidden for automation;
- architecture delegation cannot be self-issued through break glass;
- the action produces a durable receipt without recording authentication material;
- break glass bypasses a gate for the owner's specific act; it does not silently repair or permanently disable the gate.

Any authentication material previously committed to repository history MUST be treated as exposed and rotated through its owning credential system. Deleting it from the current file does not erase Git history.

---

## 13. Non-negotiable invariant

```text
Every deployment has an explicit Canonical Owner Principal.
The owner is the root of constitutional architecture authority.
Operating Partner authority and architecture authority are separate.
Operational/domain truth does not equal architecture authority.
Stable principal identity, constitution and runtime attestation remain separate objects.
AI architecture authority is explicitly owner-delegated, scope-bounded, revocable and non-transitive by default.
Unknown authority fails closed.
Reusable authentication secrets do not live in architecture documents.
```
