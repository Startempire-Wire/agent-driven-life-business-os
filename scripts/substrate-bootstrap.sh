#!/usr/bin/env bash
# Golden Path Stage 1 — substrate bootstrap: verify/report the toolchain as owning code.
# Idempotent, value-free, fail-closed. Per-component presence, version, health (exit
# status only — never secret values). Installs are NOT executed by this script:
# official routes are printed for an operator-authorized deployment run.
#
# v3 (GP-08 hardening):
#   - discovery beyond PATH via well-known locations (off-PATH installs detected)
#   - openclaw and uiai included
#   - per-check timeout when timeout(1) exists
#   - JSON via python3 escaping; pretty-printed in all forms
#   - fine-grained per-component detail: resolved path, score points, commentary
#   - exit 1 = missing; exit 3 = present-but-unhealthy; missing wins if both
set -uo pipefail

MODE="check"; JSON=0
for a in "$@"; do
  case "$a" in
    --check) MODE=check ;;
    --json) JSON=1 ;;
    --install) MODE=install ;;
    -h|--help) echo "usage: substrate-bootstrap.sh [--check|--install] [--json]"; exit 0 ;;
    *) echo "unknown arg: $a" >&2; exit 64 ;;
  esac
done

TIMEOUT_CMD=""
command -v timeout >/dev/null 2>&1 && TIMEOUT_CMD="timeout 15"

# find <name> — PATH first, then well-known locations. Locations are configuration
# metadata, not secrets; they are the diagnostic value of discovery.
find_bin() {
  local name="$1" d
  command -v "$name" 2>/dev/null && return 0
  for d in /usr/local/bin /usr/bin /opt/cpanel/ea-nodejs20/bin /opt/homebrew/bin \
           /usr/local/homebrew/bin "$HOME/.local/bin" "$HOME/bin" /snap/bin; do
    [ -x "$d/$name" ] && { echo "$d/$name"; return 0; }
  done
  return 1
}

# name|version-cmd|health-cmd (optional, exit-code only)|official route|critical|route-kind
# route-kind ∈ npm|binary|script|runbook — lets an installer UI pick its execution shape.
# health commands must not contain '|'. critical=true -> missing/unhealthy caps the
# readiness score and surfaces as a visible blocker.
COMPONENTS=(
  "git|git --version|-|official git package or git-scm.com installer|false|binary"
  "pi|pi --version|-|npm install -g @earendil-works/pi-coding-agent|true|npm"
  "focusa|focusa --version|focusa status --agent --json|focusa official upgrade channel|true|script"
  "rbw|rbw --version|-|official rbw release per vault runbook|false|binary"
  "gh|gh --version|-|official gh installer (cli.github.com)|false|binary"
  "wrangler|wrangler --version|-|npm install -g wrangler|false|npm"
  "gog|gog version|-|official gog release binary|false|binary"
  "bd|bd --version|-|official beads install|false|binary"
  "tailscale|tailscale version|tailscale status|official tailscale install script|false|script"
  "agent-kb|agent-kb version|agent-kb freshness --json|canonical KB deployment install|true|script"
  "openclaw|openclaw --version|-|official OpenClaw install per owning runbook|false|runbook"
  "uiai|uiai --version|-|official UIAI Engine install per owning runbook|false|runbook"
)

tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT
missing=0; unhealthy=0

for c in "${COMPONENTS[@]}"; do
  IFS='|' read -r name vcmd hcmd route critical kind <<< "$c"
  bin_path="$(find_bin "$name" 2>/dev/null || true)"
  if [ -n "$bin_path" ]; then
    # run "<resolved binary> <version args without the bare name>"
    vargs="${vcmd#"$name" }"
    ver="$($TIMEOUT_CMD "$bin_path" $vargs 2>/dev/null | head -n1)"
    [ -n "$ver" ] || ver="-"
    health="n/a"
    if [ "$name" = "agent-kb" ]; then
      # freshness CLI exits non-zero on unknown freshness even when status is ok;
      # health must parse status, not the raw exit code.
      if $TIMEOUT_CMD agent-kb freshness --json 2>/dev/null | grep -q '"status": *"ok"'; then
        health="healthy"
      else
        health="unhealthy"
      fi
    elif [ "$hcmd" != "-" ]; then
      if $TIMEOUT_CMD $hcmd >/dev/null 2>&1; then health="healthy"; else health="unhealthy"; fi
    fi
    st="ok"
    [ "$health" = "unhealthy" ] && unhealthy=$((unhealthy+1))
  else
    bin_path=""; ver="-"; health="n/a"; st="missing"; missing=$((missing+1))
  fi
  if [ "$MODE" = "install" ] && [ "$st" = "missing" ]; then
    echo "INSTALL ROUTE (not executed; requires operator-authorized deployment run): $name -> $route"
  fi
  COMPONENT_NAME="$name" COMPONENT_PRESENT="$st" COMPONENT_VERSION="$ver" \
  COMPONENT_HEALTH="$health" COMPONENT_ROUTE="$route" COMPONENT_CRITICAL="$critical" \
  COMPONENT_PATH="$bin_path" COMPONENT_KIND="$kind" \
  python3 -c '
import json,os
present=os.environ["COMPONENT_PRESENT"]!="missing";health=os.environ["COMPONENT_HEALTH"]
critical=os.environ["COMPONENT_CRITICAL"]=="true";path=os.environ["COMPONENT_PATH"]
# deterministic score contribution: healthy=1.0, present+n/a=0.7, unhealthy=0.3, missing=0
if not present: pts=0.0
elif health=="healthy": pts=1.0
elif health=="unhealthy": pts=0.3
else: pts=0.7
# deterministic commentary: state + why it matters, no speculation
if not present:
    note=("not found on PATH or well-known locations; official install route is available"
          + (" — CRITICAL for governed operation" if critical else " — optional until used"))
elif health=="healthy":
    note="present and responding to its health probe"
elif health=="unhealthy":
    note=("present but its health probe failed; the binary runs but the service is not answering"
          + (" — CRITICAL: governs work/evidence, repair before relying on it" if critical else ""))
else:
    note="present; this release defines no health probe, so health is not assessed (n/a, not assumed healthy)"
row={"component":os.environ["COMPONENT_NAME"],"present":present,"version":os.environ["COMPONENT_VERSION"],
 "health":health,"route":os.environ["COMPONENT_ROUTE"],"critical":critical,
 "route_kind":os.environ["COMPONENT_KIND"],
 "resolved_path":path or None,"score_points":pts,"commentary":note}
print(json.dumps(row))
' >> "$tmp"
done

rows_json="$(python3 -c 'import json,sys;print(json.dumps([json.loads(l) for l in sys.stdin if l.strip()]))' < "$tmp")"

if [ "$JSON" = "1" ]; then
  python3 -c 'import json,sys
rows=json.loads(sys.argv[1])
plan=[{"component":r["component"],"route":r["route"],"route_kind":r["route_kind"],"critical":r["critical"]} for r in rows if not r["present"]]
print(json.dumps({"schema":"agent-os-substrate-check.v3","components":rows,"install_plan":plan,"install_policy":"plans are rendered for an operator-authorized run; this script never executes installs"},indent=2))' "$rows_json"
else
  python3 -c '
import json,sys
rows=json.loads(sys.argv[1])
for r in rows:
    st = "missing" if not r["present"] else "ok"
    print("# %s" % r["commentary"])
    print("%-8s %-10s %-26s health=%-9s points=%.1f%s" % (st, r["component"], r["version"], r["health"], r["score_points"], ("  found: "+r["resolved_path"]) if r["resolved_path"] else ""))
' "$rows_json"
fi
if [ "$missing" -gt 0 ]; then exit 1; fi
if [ "$unhealthy" -gt 0 ]; then exit 3; fi
exit 0
