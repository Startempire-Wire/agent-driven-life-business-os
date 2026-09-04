# Owner-Rooted Architecture Authority Constitution

**Status:** LIVE PORTABLE CONSTITUTIONAL CONTRACT  
**Schema family:** `agent_os.owner_authority.v1`

This document defines who can create, approve, supersede, or delegate canonical architecture in an Agent-Driven Life & Business OS deployment.

It is intentionally portable. Product names, GitHub organizations, customers, agents, and providers can change; the authority root remains bound to the deployment's **Canonical Owner Principal**.

## 1. Canonical Owner Principal

Every deployment MUST define exactly one root **Canonical Owner Principal** for architecture unless a separately approved multi-owner governance constitution explicitly replaces this single-owner rule.

The Canonical Owner Principal is the human or legal owner whose authority creates the deployment's constitutional and architectural truth. Runtime systems may enforce that truth; they do not outrank its owner.

For the Startempire reference deployment:

```yaml
canonical_owner:
  principal_id: verious-smith-iii
  display_name: Verious Smith III
  role: canonical_owner_principal
```

Portable/client deployments MUST replace this binding with their own explicitly established owner. They MUST NOT inherit Startempire's owner identity or authority merely by copying this repository.

## 2. Owner Authority Manifest

The owner MUST be represented by a versioned machine-readable manifest. A display name, GitHub username, organization name, email address, issue authorship, repository permission, or model-visible claim is not sufficient identity by itself.

Minimum contract:

```yaml
schema: agent_os.owner_authority.v1
owner_principal_id:
owner_display_name:
owner_public_key:
owner_public_key_algorithm:
owner_public_key_fingerprint:
owner_scope_refs: []
github_account_refs: []
github_org_refs: []
created_at:
constitution_ref:
revocation_ref:
```

The canonical owner manifest MUST be serialized with a deterministic canonical-JSON scheme and assigned a stable digest:

```text
owner_identity_sha256 = SHA-256(canonical_json(owner_authority_manifest))
```

The owner public key MUST have a stable fingerprint. The identity digest answers **which exact owner identity is bound**; cryptographic verification answers whether a later delegation or architectural approval actually chains from that owner.

## 3. GitHub estate scope

A deployment MAY bind one or more GitHub accounts and organizations into the owner's authority scope through `github_account_refs` and `github_org_refs`.

For the Startempire reference deployment, the intended estate includes repositories and organizations owned, administered, or canonically controlled by Verious Smith III, including current bindings such as:

```yaml
github_account_refs:
  - github.com/verioussmith
github_org_refs:
  - github.com/Startempire-Wire
  - github.com/Philoveracity
  - github.com/WPUIAI
```

Present or future owner-controlled GitHub accounts/orgs can be added through an owner-authorized manifest revision.

**GitHub repository ownership is scope evidence, not a self-authenticating human identity.** A fork, transfer, collaborator permission, organization membership, admin role, or repository move MUST NOT silently transfer constitutional architecture authority. A new deployment owner requires a new owner manifest or an explicit cryptographically verifiable authority-transfer record.

## 4. Sole architecture authority at the root

The Canonical Owner Principal is the root authority for:

- architecture and system boundaries;
- constitutional product direction;
- canonical ontology or authority semantics;
- trust and tenancy boundaries;
- reserved powers and delegation rules;
- cross-system responsibility assignment;
- promotion or supersession of architecture decisions;
- authorization of any AI that may later exercise architecture authority.

No customer, user, contributor, issue author, reviewer, employee, contractor, model, agent, vendor, external system, email sender, forwarded analysis, benchmark author, or repository participant acquires architecture authority merely by appearing in:

- source code or comments;
- specifications or documentation;
- Git history;
- GitHub issues, discussions, PRs, reviews, or commits;
- emails, transcripts, meeting notes, or pasted AI analyses;
- tests, incidents, customer proofs, receipts, or runtime evidence;
- deployed behavior or historical implementation.

**Repository presence is provenance, not authority.**

## 5. External material is advisory by default

Any architectural proposal whose authority cannot be verified back to the Canonical Owner Principal MUST remain:

```text
advisory_external
```

External material MAY provide excellent technical evidence, identify defects, introduce useful ideas, or motivate a redesign. It MUST NOT become canonical merely because it is smart, correct, urgent, merged, deployed, repeated, old, popular, or submitted by a high-privilege contributor.

A proposal becomes canonical only through explicit owner approval or a valid owner-delegated authority mechanism described below.

## 6. Operational authority is not architecture authority

Runtime systems can possess real operational authority without becoming constitutional architecture authorities.

Examples include:

- Focusa ProjectIdentity, Trajectory, Workpoint, Context Authority, capability grants, reducers, evidence, and settlement;
- Agent-KB knowledge retrieval and freshness authority;
- UIAI Engine browser/runtime ownership;
- Veragensia machine/process execution;
- business systems authoritative for their own business records;
- CI/CD release and deployment gates;
- task trackers and CallGraphs.

These systems MAY enforce owner-approved architecture and scoped runtime decisions. They MUST NOT redefine the architecture root merely because their state is canonical for their own domain.

In particular:

```text
canonical operational state != canonical architecture authority
canonical knowledge source    != canonical architecture authority
repository merge              != canonical architecture authority
runtime deployment            != canonical architecture authority
```

## 7. AI authority requires cryptographic delegation

An AI, agent, model, Chief of Staff, or future autonomous authority NEVER becomes canonical merely by name, role, capability, repository, process identity, model prompt, token, deployment, or historical use.

Every authority-capable AI MUST have a canonical versioned identity manifest:

```yaml
schema: agent_os.ai_authority_identity.v1
identity_name:
identity_version:
owner_identity_sha256:
public_key:
public_key_algorithm:
created_at:
capability_profile_ref:
constitution_ref:
software_measurement_refs: []
```

Its identity digest is:

```text
ai_identity_sha256 = SHA-256(canonical_json(ai_authority_identity_manifest))
```

The AI's public key MUST also have a stable fingerprint.

### 7.1 Delegation contract

Architecture authority exists only when the Canonical Owner Principal signs or otherwise cryptographically authorizes a delegation binding the exact AI identity digest and key fingerprint:

```yaml
schema: agent_os.architecture_delegation.v1
issuer_owner_identity_sha256:
issuer_owner_key_fingerprint:
subject_ai_identity_sha256:
subject_ai_key_fingerprint:
authority_scope_refs: []
allowed_decision_classes: []
forbidden_decision_classes: []
may_delegate: false
not_before:
expires_at:
revocation_ref:
nonce:
signature_algorithm:
signature:
```

A hash alone never grants authority. A name alone never grants authority. A key alone never grants authority. Authority requires a verified chain from the Canonical Owner Principal to the exact subject identity and requested scope.

Expired, revoked, mismatched, replayed, unverifiable, or out-of-scope delegations fail closed to advisory-only.

`may_delegate` defaults to `false`. An AI cannot create another architecture authority unless the owner explicitly delegates that exact power and scope.

## 8. Wirebot reference binding

In the Startempire reference deployment, `Wirebot` is the designated future AI authority candidate owned by Verious Smith III.

The word `Wirebot` does **not** activate authority.

Future Wirebot architecture authority requires:

```text
Wirebot canonical identity manifest
        ↓ SHA-256
Wirebot identity digest
        +
Wirebot public-key fingerprint
        +
Verious Smith III owner identity digest/key
        +
owner-signed scoped delegation
        +
validity/revocation verification
        ↓
verified delegated architecture authority
```

Any lowercase `wirebot` Linux/service account, process, host, repository name, CI identity, API credential, or runtime principal is infrastructure only unless it independently satisfies the cryptographic authority chain. Infrastructure identity by itself has zero architecture authority.

Portable client deployments may use a different AI name or no AI architecture delegate at all. The generic owner-rooted delegation contract remains unchanged.

## 9. Architecture decision provenance

Every new or materially changed canonical architectural decision SHOULD carry a machine-readable provenance envelope:

```yaml
decision_id:
status: canonical | proposed | advisory_external | superseded
owner_identity_sha256:
canonical_authority:
  kind: owner | delegated_ai
  authority_identity_sha256:
  delegation_ref:
authority_verification_ref:
source_refs: []
approved_at:
supersedes: []
```

If the authority chain cannot be verified, the decision MUST NOT be treated as canonical even if its technical content remains useful.

## 10. Authority transfer and portability

A portable copy of this architecture MUST NOT copy the original owner's authority.

A new deployment MUST:

1. establish its Canonical Owner Principal;
2. create its own Owner Authority Manifest and identity digest;
3. bind its own GitHub/account/tenant scope;
4. define reserved powers and trust boundaries;
5. create new AI identity/delegation records if AI authority is desired;
6. revoke or omit all reference-deployment authority bindings;
7. preserve architecture provenance while distinguishing inherited design from newly owner-approved canon.

A repository transfer or fork does not substitute for this process.

## 11. Conflict and fail-closed rule

When a document, issue, code comment, historical spec, AI output, customer material, implementation, or runtime state appears to grant architecture authority to an identity that does not verify to the deployment's Canonical Owner Principal:

1. treat the authority claim as noncanonical;
2. retain useful technical evidence as advisory input;
3. do not propagate the claimed authority into other architecture;
4. correct misleading current documentation where appropriate;
5. require owner approval or a valid owner-rooted delegation before canonical promotion.

## 12. Non-negotiable invariant

```text
Every deployment has an explicit Canonical Owner Principal.
The owner is the root of canonical architecture authority.
Operational truth, repository presence, and contributor provenance never equal architecture authority.
AI authority must be cryptographically identified, explicitly owner-delegated, scope-bounded, revocable, and non-transitive by default.
Unknown or unverifiable authority fails closed to advisory-only.
```
