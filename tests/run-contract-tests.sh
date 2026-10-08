#!/usr/bin/env bash
# Portable contract regression suite.
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
PYTHON="${PYTHON:-python3}"

if ! "$PYTHON" -c 'import jsonschema' >/dev/null 2>&1; then
  printf '%s\n' "missing test dependency: jsonschema" >&2
  printf '%s\n' "install with: $PYTHON -m pip install -r $ROOT/tests/requirements.txt" >&2
  exit 2
fi

"$PYTHON" "$ROOT/tests/agent-operation-contract-test.py"
"$PYTHON" "$ROOT/tests/agent-contract-optimization-test.py"
"$PYTHON" "$ROOT/tests/portfolio-compiler-contract-test.py"
"$PYTHON" "$ROOT/tests/routine-library-coverage-test.py"
"$PYTHON" "$ROOT/tests/attention-policy-contract-test.py"
"$PYTHON" "$ROOT/tests/operator-environment-contract-test.py"
"$PYTHON" "$ROOT/tests/activation-blueprint-test.py"
"$PYTHON" "$ROOT/tests/repository-integrity-test.py"
  # Portable memory evaluation. Runs its own gates; a non-zero exit means the
  # memory substrate stopped being installable, reachable, sovereign, or
  # causally load-bearing. Deliberately last so a substrate failure is not
  # masked by a documentation failure.
  "$PYTHON" "$ROOT/scripts/sovereign-memory-eval.py"
printf '%s\n' 'portable contract regressions: PASS'
