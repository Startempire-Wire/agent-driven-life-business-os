#!/usr/bin/env bash
# Portable contract regression suite.
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
python3 "$ROOT/tests/agent-operation-contract-test.py"
python3 "$ROOT/tests/agent-contract-optimization-test.py"
printf '%s\n' 'portable contract regressions: PASS'
