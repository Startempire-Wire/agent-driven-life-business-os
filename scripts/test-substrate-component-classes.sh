#!/usr/bin/env bash
# Tests for issue #10: substrate bootstrap separates CLI presence from
# runtime/adapter/endpoint classification.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT="$SCRIPT_DIR/substrate-bootstrap.sh"
tmpout=$(mktemp); stub=$(mktemp -d)
trap 'rm -rf "$tmpout" "$stub" "$srvlog" "$srvpid"' EXIT
srvlog=$(mktemp); srvpid=

pass=0; fail=0
ck() { if [ "$2" = "1" ]; then pass=$((pass+1)); echo "PASS: $1"; else fail=$((fail+1)); echo "FAIL: $1"; fi; }

jrun() { python3 -c "$1" "$tmpout"; }


# 1) Service-only runtime: healthy uiai endpoint, NO uiai CLI on PATH
python3 -c '
import http.server, threading, sys
class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        b=b"{\"status\":\"healthy\",\"service\":\"uiai-engine\",\"stub\":true}"
        self.send_response(200); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
    def log_message(self,*a): pass
srv=http.server.HTTPServer(("127.0.0.1",17456),H)
threading.Thread(target=srv.serve_forever,daemon=True).start()
import signal; signal.pause()
' > "$srvlog" 2>&1 &
srvpid=$!
sleep 1

# service-only: healthy endpoint, NO product CLI on the host (openclaw has no
# CLI here; uiai does, so it exercises the CLI+runtime-both-present case)
OPENCLAW_GATEWAY_URL=http://127.0.0.1:17456 bash "$SCRIPT" --json > "$tmpout" 2>/dev/null || true
[ "$(grep -c 'agent-os-substrate-check.v5' "$tmpout")" -gt 0 ] && ck "service-only: JSON schema is v5" "1" || ck "service-only: JSON schema is v5" "0"
oc_row=$(jrun "import json,sys; d=json.load(open(sys.argv[1])); print(json.dumps([r for r in d['components'] if r['component']=='openclaw'][0]))" )
echo "$oc_row" | python3 -c '
import json,sys
r=json.loads(sys.stdin.read())
assert r["present"] is False, r
assert r["runtime"]["state"]=="runtime_healthy", r
assert r["runtime"]["healthy"] is True, r
assert "do not auto-install" in r["remediation_owner"], r
' && ck "service-only: healthy runtime observed, CLI parity owned, no auto-install" "1"
plan_has_oc=$(jrun "import json,sys; d=json.load(open(sys.argv[1])); print(json.dumps([p for p in d['install_plan'] if p['component']=='openclaw']))" | { grep -c 'openclaw' || true; })
[ "$plan_has_oc" = "0" ] && ck "service-only: healthy remote excluded from install_plan" "1" || ck "service-only: healthy remote excluded from install_plan" "0"
uiai_row0=$(jrun "import json,sys; d=json.load(open(sys.argv[1])); print(json.dumps([r for r in d['components'] if r['component']=='uiai'][0]))" )
echo "$uiai_row0" | python3 -c '
import json,sys
r=json.loads(sys.stdin.read())
assert r["present"] is True and r["runtime"]["healthy"] is True, r
assert r["remediation_owner"]=="none", r
' && ck "cli+runtime both present: remediation none, runtime still observed" "1"

# 2) all absent: dead endpoint -> endpoint_unreachable, install plan retains route
kill $srvpid 2>/dev/null || true; wait "$srvpid" 2>/dev/null || true
for _ in 1 2 3 4 5 6 7 8 9 10; do
  curl -sS --max-time 1 http://127.0.0.1:17456/health >/dev/null 2>&1 || break
  sleep 1
done
UIAI_ENGINE_URL=http://127.0.0.1:17456 bash "$SCRIPT" --json > "$tmpout" 2>/dev/null || true
uiai_row2=$(jrun "import json,sys; d=json.load(open(sys.argv[1])); print(json.dumps([r for r in d['components'] if r['component']=='uiai'][0]))")
echo "$uiai_row2" | python3 -c '
import json,sys
r=json.loads(sys.stdin.read())
assert r["runtime"]["state"]=="endpoint_unreachable", r
assert r["remediation_owner"].startswith("runtime/service owner"), r
' && ck "all-absent: unreachable endpoint classified, remediation points to runtime owner" "1"

# 3) CLI-only: stub CLI present (fake on PATH), no runtime
mkdir -p "$stub/bin"
printf '#!/bin/sh\ncase "$1" in --version|version) echo "uiai 9.9-stub";; *) exit 0;; esac\n' > "$stub/bin/uiai"
chmod +x "$stub/bin/uiai"
PATH="$stub/bin:$PATH" UIAI_ENGINE_URL=http://127.0.0.1:17456 bash "$SCRIPT" --json > "$tmpout" 2>/dev/null || true
uiai_row3=$(jrun "import json,sys; d=json.load(open(sys.argv[1])); print(json.dumps([r for r in d['components'] if r['component']=='uiai'][0]))")
echo "$uiai_row3" | python3 -c '
import json,sys
r=json.loads(sys.stdin.read())
assert r["present"] is True, r
assert r["health"]=="n/a", r
assert r["runtime"]["state"]=="endpoint_unreachable", r
' && ck "cli-only: CLI present, runtime unreachable — states separated" "1"

# 4) --apply base behavior unchanged: no uiai/openclaw routes executed by apply
apply_out=$(PATH="$stub/bin:$PATH" bash "$SCRIPT" --apply base --dry-run 2>&1 || true)
if grep -E 'INSTALL ROUTE.*(uiai|openclaw)' <<<"$apply_out"; then ck "apply base: never touches runtime-product installs" "0"; else ck "apply base: never touches runtime-product installs" "1"; fi

echo "-----"
echo "pass=$pass fail=$fail"
[ "$fail" = "0" ]
