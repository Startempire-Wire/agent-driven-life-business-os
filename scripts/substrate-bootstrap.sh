#!/usr/bin/env bash
# Golden Path Stage 1 — substrate bootstrap: verify/report the toolchain as owning code.
# Idempotent, value-free, fail-closed. Per-component presence, version, health (exit
# status only — never secret values). Installs are NOT executed by this script:
# official routes are printed for an operator-authorized deployment run. No invented
# commands; this script reuses official CLIs and adds only the Stage 1 embedded check.
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

# name|version-cmd|health-cmd (optional, exit-code only)|official route
# NOTE: health commands must not contain '|' — pipe-using checks are dispatched below.
COMPONENTS=(
  "git|git --version|-|official git package or git-scm.com installer"
  "pi|pi --version|-|npm install -g @earendil-works/pi-coding-agent"
  "focusa|focusa --version 2>/dev/null|focusa status --agent --json|focusa official upgrade channel"
  "rbw|rbw --version|-|official rbw release per vault runbook"
  "gh|gh --version|-|official gh installer (cli.github.com)"
  "wrangler|wrangler --version|-|npm install -g wrangler"
  "gog|gog version|-|official gog release binary"
  "bd|bd --version|-|official beads install"
  "tailscale|tailscale version|tailscale status|official tailscale install script"
  "agent-kb|agent-kb version 2>/dev/null|-|canonical KB deployment install"
)

out="["; first=1; missing=0
for c in "${COMPONENTS[@]}"; do
  IFS='|' read -r name vcmd hcmd route <<< "$c"
  if command -v "$name" >/dev/null 2>&1; then
    ver=$($vcmd 2>/dev/null | head -n1); [ -n "$ver" ] || ver="-"
    health="n/a"
    if [ "$name" = "agent-kb" ]; then
      # freshness CLI exits non-zero on unknown freshness even when status is ok;
      # health must parse status, not the raw exit code.
      if agent-kb freshness --json 2>/dev/null | grep -q '"status": *"ok"'; then
        health="healthy"
      else
        health="unhealthy"
      fi
    elif [ "$hcmd" != "-" ]; then
      if $hcmd >/dev/null 2>&1; then health="healthy"; else health="unhealthy"; fi
    fi
    st="ok"
  else
    ver="-"; health="n/a"; st="missing"; missing=$((missing+1))
  fi
  if [ "$MODE" = "install" ] && [ "$st" = "missing" ]; then
    echo "INSTALL ROUTE (not executed; requires operator-authorized deployment run): $name -> $route"
  fi
  if [ "$JSON" = "1" ]; then
    [ $first -eq 0 ] && out="$out,"
    if [ "$st" = "ok" ]; then p=true; else p=false; fi
    out="$out{\"component\":\"$name\",\"present\":$p,\"version\":\"$ver\",\"health\":\"$health\",\"route\":\"$route\"}"
    first=0
  else
    printf "%-8s %-10s %-26s health=%-9s route=%s\n" "$st" "$name" "$ver" "$health" "$route"
  fi
done
if [ "$JSON" = "1" ]; then echo "$out]"; fi
if [ "$missing" -gt 0 ]; then exit 1; fi
exit 0