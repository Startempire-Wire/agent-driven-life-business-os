#!/usr/bin/env bash
# Bounded regression battery for the substrate/audit script pair.
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
SUB="$ROOT/scripts/substrate-bootstrap.sh"
AUD="$ROOT/scripts/brownfield-audit.sh"
DIFF="$ROOT/scripts/fleet-diff.py"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

bash -n "$SUB" "$AUD"
set +e
"$SUB" --check --json >"$tmp/sub.json"
rc=$?
set -e
case "$rc" in 0|1|3) ;; *) echo "unexpected substrate exit: $rc" >&2; exit 1 ;; esac
python3 - "$tmp/sub.json" <<'PY'
import json, sys
x=json.load(open(sys.argv[1])); assert "environment" in x; assert "mesh" in x["environment"]
PY
set +e
"$AUD" --json --no-print >"$tmp/audit.out"
rc=$?
set -e
case "$rc" in 0|1|2|3) ;; *) echo "unexpected audit exit: $rc" >&2; exit 1 ;; esac
python3 - "$tmp/audit.out" <<'PY'
import json, sys
# The audit emits one report; tolerate a non-zero readiness exit.
x=json.load(open(sys.argv[1])); assert x["schema"] == "agent-os-brownfield-audit.v5"
assert isinstance(x["readiness_score"]["score"], int)
PY
if "$SUB" --definitely-unknown >/dev/null 2>&1; then exit 1; else test $? -eq 64; fi
if "$SUB" --apply base >/dev/null 2>&1; then exit 1; else test $? -eq 64; fi
cat >"$tmp/previous.json" <<'JSON'
{"machines":[{"hostname":"local","status":"audited","report":{"readiness_score":{"score":65}}}],"fleet_score":{"score":65,"blockers":[]}}
JSON
cat >"$tmp/current.json" <<'JSON'
{"machines":[{"hostname":"local","status":"audited","report":{"readiness_score":{"score":40}}},{"hostname":"new","status":"offline"}],"fleet_score":{"score":20,"blockers":[{"machine":"local","component":"focusa","reason":"unhealthy"}]}}
JSON
python3 "$DIFF" "$tmp/previous.json" "$tmp/current.json" >"$tmp/diff.json"
python3 - "$tmp/diff.json" <<'PY'
import json, sys
x=json.load(open(sys.argv[1])); assert x["schema"] == "agent-os-fleet-diff.v1"
assert x["fleet_score"]["delta"] == -45
assert x["machines"][0]["score"]["delta"] == -25
assert len(x["blockers"]["added"]) == 1
PY
printf '%s\n' 'agent-os script regression: PASS'
