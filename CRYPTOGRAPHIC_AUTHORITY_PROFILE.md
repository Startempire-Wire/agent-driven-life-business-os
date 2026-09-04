# Cryptographic Authority Profile

**Status:** LIVE PORTABLE CRYPTOGRAPHIC AUTHORITY CONTRACT  
**Applies with:** `OWNER_AUTHORITY_CONSTITUTION.md`

This profile defines how owner and AI authority identities are hashed and verified without confusing a durable principal with a changing software build.

## 1. Three hashes, three questions

Do not collapse identity, constitution, and runtime into one digest.

```text
principal_identity_sha256   -> WHO is this authority principal?
constitution_sha256         -> WHICH authority law/constitution is bound?
runtime_attestation_sha256  -> WHAT exact runtime is acting now?
```

A runtime update should normally change the runtime attestation, not silently create a new principal identity. A constitutional authority change should change the constitution hash and require an authority-compatible delegation update or revalidation.

## 2. Canonicalization

All machine-readable authority manifests MUST use one specified deterministic canonical serialization before hashing. The normative portable profile is **JSON Canonicalization Scheme (JCS / RFC 8785)** over UTF-8 JSON.

```text
sha256_hex = lowercase_hex(SHA-256(JCS(document)))
```

Hash input MUST exclude transport wrappers and detached signatures unless a schema explicitly states otherwise. The schema/version defines exactly which fields are signed and hashed.

## 3. Owner principal identity

The stable owner principal manifest identifies the architecture authority root.

```json
{
  "schema": "agent_os.owner_principal.v1",
  "principal_id": "owner:<stable-id>",
  "display_name": "<owner display name>",
  "authority_public_key": "<encoded public key>",
  "authority_key_algorithm": "<algorithm>",
  "created_at": "<timestamp>",
  "lineage_root_ref": "<optional external owner enrollment/attestation ref>"
}
```

Compute:

```text
owner_principal_sha256 = SHA-256(JCS(owner_principal_manifest))
owner_key_fingerprint  = fingerprint(owner authority public key)
```

The owner principal hash is intended to remain stable across ordinary repository, runtime, device, or software changes. Key rotation uses an owner-authorized rotation record linking old and new keys/principal revisions rather than silently replacing identity.

## 4. AI principal identity

A durable authority-capable AI uses a stable principal manifest separate from its changing runtime.

```json
{
  "schema": "agent_os.ai_principal.v1",
  "principal_id": "ai:<stable-id>",
  "identity_name": "<name>",
  "owner_principal_sha256": "<owner hash>",
  "authority_public_key": "<encoded public key>",
  "authority_key_algorithm": "<algorithm>",
  "created_at": "<timestamp>",
  "lineage_root_ref": "<optional lineage ref>"
}
```

Compute:

```text
ai_principal_sha256 = SHA-256(JCS(ai_principal_manifest))
ai_key_fingerprint  = fingerprint(ai authority public key)
```

The AI principal hash answers **which durable AI principal** is acting. It MUST NOT include ordinary binary hashes, model versions, tool versions, current hostnames, or mutable runtime measurements that would make identity change on every upgrade.

## 5. Constitution identity

Authority policy is separately versioned and hashed through a machine-readable constitution manifest.

```json
{
  "schema": "agent_os.authority_constitution.v1",
  "constitution_id": "<stable constitution id>",
  "constitution_version": "<version>",
  "owner_principal_sha256": "<owner hash>",
  "normative_document_refs": [
    {"ref": "OWNER_AUTHORITY_CONSTITUTION.md", "sha256": "<document digest>"},
    {"ref": "CRYPTOGRAPHIC_AUTHORITY_PROFILE.md", "sha256": "<document digest>"}
  ],
  "created_at": "<timestamp>"
}
```

Compute:

```text
constitution_sha256 = SHA-256(JCS(constitution_manifest))
```

A materially changed authority constitution produces a new constitution hash. Delegations can require one exact constitution or an explicit compatible version range/policy.

## 6. Runtime attestation

The runtime attestation describes the actual software/model/tool environment currently exercising the principal.

```json
{
  "schema": "agent_os.runtime_attestation.v1",
  "principal_sha256": "<AI principal hash>",
  "constitution_sha256": "<constitution hash>",
  "source_commit": "<git commit or null>",
  "release_ref": "<release ref or null>",
  "binary_sha256": [],
  "container_image_digests": [],
  "model_identity_refs": [],
  "tool_registry_sha256": "<digest or null>",
  "policy_bundle_sha256": "<digest or null>",
  "host_attestation_ref": "<optional TPM/TEE/host attestation ref>",
  "measured_at": "<timestamp>",
  "attestor_key_fingerprint": "<fingerprint>"
}
```

Compute:

```text
runtime_attestation_sha256 = SHA-256(JCS(runtime_attestation))
```

The attestation MUST be signed by an authorized attestor or the AI principal according to owner policy. A runtime update creates a new attestation while preserving the durable principal identity.

## 7. Delegation binds identity and acceptable runtime

A canonical architecture delegation binds the owner root to the durable AI principal and also states which constitution/runtime posture is acceptable.

```json
{
  "schema": "agent_os.architecture_delegation.v2",
  "issuer_owner_principal_sha256": "<owner hash>",
  "issuer_owner_key_fingerprint": "<owner key fingerprint>",
  "subject_ai_principal_sha256": "<AI hash>",
  "subject_ai_key_fingerprint": "<AI key fingerprint>",
  "required_constitution_sha256": "<constitution hash>",
  "runtime_attestation_policy_ref": "<policy ref>",
  "authority_scope_refs": [],
  "allowed_decision_classes": [],
  "forbidden_decision_classes": [],
  "may_delegate": false,
  "not_before": "<timestamp>",
  "expires_at": "<timestamp>",
  "revocation_ref": "<ref>",
  "nonce": "<unique nonce>",
  "signature_algorithm": "<algorithm>",
  "signature": "<detached/encoded signature>"
}
```

Authority verification MUST confirm all of the following:

1. owner principal hash and owner key fingerprint are trusted;
2. owner signature is valid over the canonical delegation payload;
3. AI principal hash and AI key fingerprint match the acting principal;
4. AI proves possession of the bound private key;
5. required constitution hash is active/compatible;
6. current runtime attestation satisfies the referenced runtime policy;
7. requested repository/project/decision class is within delegated scope;
8. `not_before` / `expires_at` are valid;
9. delegation and involved keys are not revoked;
10. nonce/replay policy passes;
11. downstream delegation is denied unless `may_delegate=true` and the child scope is strictly equal or narrower.

Failure of any check returns **non-authoritative / advisory-only**.

## 8. Startempire Wirebot binding

For the Startempire reference deployment:

```text
owner principal: Verious Smith III
AI principal candidate: Wirebot
```

No active Wirebot architecture-authority hash is declared by this document. A real `wirebot_principal_sha256` MUST NOT be minted until the canonical Wirebot principal manifest and authority public key exist and are explicitly owner-approved.

When created:

```text
wirebot_principal_sha256 = SHA-256(JCS(wirebot_ai_principal_manifest))
```

Then any architecture delegation from Verious Smith III binds that exact principal hash, its key fingerprint, the constitution hash, and a runtime-attestation policy.

A Linux account named `wirebot`, repository named `wirebot-*`, process, host, model, API token, or source commit has zero authority by naming coincidence.

## 9. Rotation, upgrade, and compromise

- **Software/model/tool upgrade:** new runtime attestation; principal normally unchanged.
- **Constitution change:** new constitution hash; revalidate or replace delegations as policy requires.
- **AI authority-key rotation:** signed rotation chain or new AI principal revision; old key revoked.
- **Owner authority-key rotation:** owner-authorized root rotation ceremony/record; all dependent trust must re-anchor deliberately.
- **Principal compromise:** revoke principal/key and all dependent delegations immediately; a replacement principal receives a new identity hash unless an owner-approved recovery/rotation protocol proves continuity.
- **Repository transfer/fork:** does not change principal identity or authority automatically.

## 10. Non-negotiable invariant

```text
Identity is stable principal identity, not mutable runtime state.
Constitution and runtime are hashed separately.
Hashing identifies objects; signatures and trust roots authorize them.
A matching name or hash without the full owner-rooted verification chain is not architecture authority.
```
