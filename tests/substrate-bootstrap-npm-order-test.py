#!/usr/bin/env python3
"""Guard documented Stage 1 npm installation on apt/dnf vs Homebrew.

Static source-contract checks only; no package manager or customer host is run.
"""
from pathlib import Path

source = (Path(__file__).resolve().parent.parent / "scripts" / "substrate-bootstrap.sh").read_text()
dry = source.split('elif [ "$DRYRUN" = "1" ]; then', 1)[-1].split('else\n      echo "APPLY: installing', 1)[0]
apply = source.split('echo "APPLY: installing missing base primitives', 1)[1].split('apply_result="applied:', 1)[0]

assert 'npm) continue ;;' not in source, "Missing npm cannot be silently skipped"
assert 'target="npm"' in dry and 'target="npm"' in apply, "Missing Linux npm must be installable"
assert 'if [ "$os_id" = "darwin" ]; then target="node"; else target="nodejs"; fi' in source
assert 'APPLY FAILED: npm is missing' in apply, "macOS missing npm needs explicit failure"
assert '&& find_bin "$name" >/dev/null 2>&1' in apply, "Package return code alone is not a usable binary"
assert 'failed="$failed $name"' in apply
assert 'base_prerequisites' not in apply, "No downstream product components belong in the base installer"
assert '"focusa|' in source and '"uiai|' in source
print("substrate-bootstrap-npm-order: PASS")
