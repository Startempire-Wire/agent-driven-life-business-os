#!/usr/bin/env bash
# Agent OS brownfield audit — value-free component audit + shaped report.
# For operator-authorized audits of brownfield client systems. Verifies presence
# of the Stage 1 substrate components (reusing substrate-bootstrap.sh — the single
# component-check implementation), adds a one-way machine fingerprint for
# uniqueness, and optionally POSTs the report to an operator-deployed endpoint.
#
# Never reads or emits: environment dumps, file contents, credentials, tokens,
# keys, cookies, IP addresses, usernames. The machine fingerprint is a one-way
# SHA-256 of the OS machine id (or platform UUID) — identifying, not secret,
# not reversible. The optional label comes only from the operator via --label.
#
# Modes:
#   (default)       audit + human/JSON print, no network
#   --post          audit + POST report to $AUDIT_ENDPOINT (optional $AUDIT_TOKEN bearer)
#   --json          print the report JSON (default prints human table + JSON)
#   --label NAME    operator-supplied deployment label (no auto-detected identity)
# Exit codes: 0 audit complete (delivery failure with --post exits 2),
#             64 usage error, 65 substrate helper missing.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUB="$DIR/substrate-bootstrap.sh"
MODE="print"; LABEL=""; ENDPOINT="${AUDIT_ENDPOINT:-}"; TOKEN="${AUDIT_TOKEN:-}"

while [ $# -gt 0 ]; do
  case "$1" in
    --post) MODE="post"; shift ;;
    --json) MODE="json"; shift ;;
    --label) LABEL="${2:-}"; shift 2 || true ;;
    -h|--help)
      echo "usage: brownfield-audit.sh [--post] [--json] [--label NAME]"
      echo "env: AUDIT_ENDPOINT (https URL), AUDIT_TOKEN (optional bearer)"
      exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 64 ;;
  esac
done

[ -x "$SUB" ] || { echo "substrate-bootstrap.sh not found next to this script" >&2; exit 65; }

# --- one-way machine fingerprint (uniqueness without secrets) ---
fp_source=""; fp_desc=""
if [ -r /etc/machine-id ]; then
  fp_source="$(tr -d '[:space:]' < /etc/machine-id)"; fp_desc="/etc/machine-id"
elif command -v ioreg >/dev/null 2>&1; then
  fp_source="$(ioreg -rd1 -c IOPlatformExpertDevice 2>/dev/null | sed -n 's/.*"IOPlatformUUID" = "\(.*\)"/\1/p' | head -n1)"
  fp_desc="IOPlatformUUID"
else
  fp_source="hostname:$(hostname 2>/dev/null)"; fp_desc="hostname-weak"
fi
[ -n "$fp_source" ] || { fp_source="unavailable"; fp_desc="unavailable"; }
fp="$(printf %s "$fp_source" | (sha256sum 2>/dev/null || shasum -a 256) | awk '{print $1}')"
fp="sha256:${fp:-unavailable}"

# --- public OS metadata only ---
os_name="-"
if [ -r /etc/os-release ]; then os_name="$(. /etc/os-release && echo "${PRETTY_NAME:--}")"; fi
os_type="$(uname -s 2>/dev/null || echo '-')"
os_kernel="$(uname -r 2>/dev/null || echo '-')"

# --- component data from the owning checker (reused, not duplicated) ---
sub_json="$("$SUB" --check --json 2>/dev/null)"
sub_human="$("$SUB" --check 2>/dev/null)"
if [ -z "$sub_json" ]; then echo "substrate check produced no data" >&2; exit 65; fi
present="$(printf '%s\n' "$sub_human" | grep -c '^ok ' || true)"
total="$(printf '%s\n' "$sub_json" | grep -o '"component"' | wc -l | tr -d ' ')"
missing=$(( total - present ))
healthy="$(printf '%s\n' "$sub_human" | grep -c 'health=healthy' || true)"
unhealthy="$(printf '%s\n' "$sub_human" | grep -c 'health=unhealthy' || true)"
now="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

report="{\"schema\":\"agent-os-brownfield-audit.v1\",\"generated_at\":\"$now\",\"machine_fingerprint\":\"$fp\",\"fingerprint_method\":\"sha256($fp_desc)\",\"label\":\"$LABEL\",\"os\":{\"type\":\"$os_type\",\"kernel\":\"$os_kernel\",\"name\":\"$os_name\"},\"audit\":{\"tool\":\"substrate-bootstrap.sh\",\"mode\":\"value-free\"},\"components\":$sub_json,\"summary\":{\"components_total\":$total,\"present\":$present,\"missing\":$missing,\"healthy\":$healthy,\"unhealthy\":$unhealthy}}"

if [ "$MODE" = "json" ]; then
  echo "$report"
else
  printf '%s\n' "$sub_human"
  echo "---- report (also printed as JSON) ----"
  echo "$report"
fi

if [ "$MODE" = "post" ]; then
  if [ -z "$ENDPOINT" ]; then
    echo "NOT REPORTED: no AUDIT_ENDPOINT configured (report printed locally only)" >&2
    exit 0
  fi
  if ! command -v curl >/dev/null 2>&1; then
    echo "DELIVERY FAILED: curl not present; report printed locally only" >&2
    exit 2
  fi
  auth_args=()
  [ -n "$TOKEN" ] && auth_args=(-H "Authorization: Bearer $TOKEN")
  code="$(curl -fsS --max-time 20 -X POST -H "Content-Type: application/json" ${TOKEN:+-H "Authorization: Bearer $TOKEN"} --data-binary "$report" -o /dev/null -w '%{http_code}' "$ENDPOINT" 2>/dev/null)" || code="curl-failed"
  if [ "$code" = "200" ] || [ "$code" = "201" ] || [ "$code" = "202" ]; then
    echo "REPORTED: endpoint accepted report (HTTP $code)"
  else
    echo "DELIVERY FAILED: endpoint returned $code (report printed locally only)" >&2
    exit 2
  fi
fi
exit 0