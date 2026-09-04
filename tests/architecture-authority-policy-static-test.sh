#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
POLICY="$ROOT_DIR/OWNER_AUTHORITY_CONSTITUTION.md"
AGENTS="$ROOT_DIR/AGENTS.md"
README="$ROOT_DIR/README.md"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "PASS: $*"; }

for file in "$POLICY" "$AGENTS" "$README"; do
  [[ -f "$file" ]] || fail "missing required authority document: $file"
done

grep -Fq 'Canonical Owner Principal' "$POLICY" \
  || fail "Canonical Owner Principal contract missing"
grep -Fq 'owner_identity_sha256 = SHA-256(canonical_json(owner_authority_manifest))' "$POLICY" \
  || fail "owner identity SHA-256 contract missing"
grep -Fq 'ai_identity_sha256 = SHA-256(canonical_json(ai_authority_identity_manifest))' "$POLICY" \
  || fail "AI identity SHA-256 contract missing"
grep -Fq 'may_delegate: false' "$POLICY" \
  || fail "non-transitive AI delegation default missing"
grep -Fq 'Repository presence is provenance, not authority.' "$POLICY" \
  || fail "provenance-versus-authority invariant missing"
grep -Fq 'GitHub repository ownership is scope evidence, not a self-authenticating human identity.' "$POLICY" \
  || fail "GitHub ownership identity boundary missing"
grep -Fq 'Verious Smith III' "$POLICY" \
  || fail "Startempire owner reference binding missing"
pass "portable owner authority constitution is structurally complete"

grep -Fq '**Contract version:** 3.0.0' "$AGENTS" \
  || fail "AGENTS contract major version not advanced"
grep -Fq 'ARCHITECTURE AUTHORITY HARD STOP' "$AGENTS" \
  || fail "AGENTS architecture hard stop missing"
grep -Fq 'OWNER_AUTHORITY_CONSTITUTION.md' "$AGENTS" \
  || fail "AGENTS does not bind to owner authority constitution"
grep -Fq 'canonical runtime/domain truth ≠ canonical architecture authority' "$AGENTS" \
  || fail "runtime-versus-architecture distinction missing"
grep -Fq 'issue/PR/commit authorship ≠ architecture authority' "$AGENTS" \
  || fail "repository provenance boundary missing"
pass "primary agent contract enforces owner-rooted architecture authority"

grep -Fq 'Architecture authority constitution' "$README" \
  || fail "README does not surface architecture authority constitution"
grep -Fq 'provenance/evidence, not architecture authority' "$README" \
  || fail "README provenance boundary missing"
grep -Fq 'Verious Smith III (Sir V3)' "$README" \
  || fail "README Startempire owner binding missing"
pass "human-facing architecture guide matches authority contract"

# Prevent future edits from turning operational authority back into the architecture root.
if grep -Eqi '(^|[[:space:]])(Focusa|Agent-KB|UIAI Engine|Veragensia)[[:space:]]+(is|as)[[:space:]]+(the[[:space:]]+)?(root|final|sole)[[:space:]]+(canonical[[:space:]]+)?architecture[[:space:]]+authority' "$AGENTS" "$README"; then
  fail "operational subsystem is incorrectly described as root architecture authority"
fi
pass "operational subsystems remain subordinate to owner-rooted architecture"

echo "owner-rooted architecture authority static test: PASS"
