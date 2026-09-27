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
printf '%s\n' 'portable contract regressions: PASS'
