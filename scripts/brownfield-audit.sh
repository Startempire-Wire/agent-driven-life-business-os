#!/usr/bin/env bash
# Brownfield audit — one bounded system-shape report, value-free, pretty in all forms.
# v3 (GP-08/09): python-built JSON (injection-safe), strict args, combinable flags,
# HTTPS enforced except loopback, fine-grained score with per-component breakdown,
# service-shape section, and deterministic commentary throughout.
# The readiness score is substrate readiness only — never a W.I.N.S. business
# outcome. An observation is not enrollment; a fingerprint is not identity.
# Exit codes: 0 clean, 1 missing components, 3 present-but-unhealthy,
#             2 delivery failure (--post), 64 usage, 65 helper/data failure,
#             66 refused endpoint.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUB="$DIR/substrate-bootstrap.sh"
MODE_PRINT=1; MODE_JSON=0; MODE_POST=0; LABEL=""; ENDPOINT="${AUDIT_ENDPOINT:-}"; TOKEN="${AUDIT_TOKEN:-}"

while [ $# -gt 0 ]; do
  case "$1" in
    --post) MODE_POST=1; shift ;;
    --json) MODE_JSON=1; shift ;;
    --no-print) MODE_PRINT=0; shift ;;
    --label)
      if [ $# -lt 2 ] || [ -z "${2:-}" ]; then echo "--label requires a value" >&2; exit 64; fi
      LABEL="$2"; shift 2 ;;
    -h|--help)
      echo "usage: brownfield-audit.sh [--post] [--json] [--no-print] [--label NAME]"
      echo "env: AUDIT_ENDPOINT (https URL; http only for 127.0.0.1/localhost), AUDIT_TOKEN (optional bearer)"
      exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 64 ;;
  esac
done

[ -x "$SUB" ] || { echo "substrate-bootstrap.sh not found next to this script" >&2; exit 65; }

if [ "$MODE_POST" = "1" ]; then
  if [ -z "$ENDPOINT" ]; then
    echo "NOT REPORTED: no AUDIT_ENDPOINT configured (report printed locally only)" >&2
    MODE_POST=0
  elif printf '%s' "$ENDPOINT" | grep -qi '^https://'; then
    : # approved transport
  elif printf '%s' "$ENDPOINT" | grep -qi '^http://\(127\.0\.0\.1\|localhost\)'; then
    echo "WARNING: local-loopback HTTP endpoint (testing only; not durable intake)" >&2
  else
    echo "REFUSED: AUDIT_ENDPOINT must be https (or loopback http for local testing); got $ENDPOINT" >&2
    exit 66
  fi
fi

# --- one-way machine fingerprint (pseudonymous observation, not identity/enrollment) ---
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

# --- environment detection: platform facts that drive installer-UI route selection ---
# value-free: presence/kind only, no unrelated package versions, no network probes.
os_id="-"; os_version="-"
if [ -r /etc/os-release ]; then
  os_id="$(. /etc/os-release && echo "${ID:--}")"
  os_version="$(. /etc/os-release && echo "${VERSION_ID:--}")"
fi
os_arch="$(uname -m 2>/dev/null || echo '-')"

init_kind="unknown"
if command -v systemctl >/dev/null 2>&1 && systemctl is-system-running >/dev/null 2>&1; then init_kind="systemd"
elif [ -d /run/systemd/system ]; then init_kind="systemd"
elif command -v launchctl >/dev/null 2>&1; then init_kind="launchd"
elif [ -f /sbin/openrc ] || command -v rc-service >/dev/null 2>&1; then init_kind="openrc"
fi

virt_kind="-"
if command -v systemd-detect-virt >/dev/null 2>&1; then
  virt_kind="$(systemd-detect-virt 2>/dev/null || echo none)"
fi
container="no"
[ -f /.dockerenv ] && container="yes"
[ -f /proc/vz ] && container="yes" && [ "$virt_kind" = "-" ] && virt_kind="openvz"

pkg_managers=""
for pm in apt-get dnf yum brew winget apk zypper; do
  command -v "$pm" >/dev/null 2>&1 && pkg_managers="$pkg_managers $pm"
done
command -v npm >/dev/null 2>&1 && pkg_managers="$pkg_managers npm"
command -v cargo >/dev/null 2>&1 && pkg_managers="$pkg_managers cargo"
pkg_managers="$(printf '%s' "$pkg_managers" | sed 's/^ //')"
[ -n "$pkg_managers" ] || pkg_managers="-"

env_file="$(mktemp)"
ENV_TYPE="$os_type" ENV_ID="$os_id" ENV_VERSION="$os_version" ENV_KERNEL="$os_kernel" \
ENV_ARCH="$os_arch" ENV_INIT="$init_kind" ENV_VIRT="$virt_kind" ENV_CONTAINER="$container" \
ENV_PKGS="$pkg_managers" python3 -c '
import json,os
env={"platform":{"os":os.environ["ENV_TYPE"],"distro_id":os.environ["ENV_ID"],"distro_version":os.environ["ENV_VERSION"],"kernel":os.environ["ENV_KERNEL"],"arch":os.environ["ENV_ARCH"]},
 "init":os.environ["ENV_INIT"],
 "virtualization":os.environ["ENV_VIRT"],
 "container":os.environ["ENV_CONTAINER"]=="yes",
 "package_managers":os.environ["ENV_PKGS"].split() if os.environ["ENV_PKGS"]!="-" else [],
 "commentary":"presence/kind facts only; drives installer-UI route selection per platform (apt vs brew vs npm vs runbook)"}
print(json.dumps(env))
' > "$env_file"
env_json="$(cat "$env_file")"; rm -f "$env_file"

# --- service-shape section: known agent-OS units, active state only (value-free) ---
SERVICES=(
  "focusa-daemon" "context-core" "agent-kb-api" "wirebot-scoreboard" "openclaw-gateway"
  "wbt" "mem0-wirebot" "letta-wirebot" "letta-relay" "agent-audit" "agent-kb-refresh"
  "cloudflared-wirebot" "cloudflared-agent-audit" "wirebot-wbt"
)
svc_tmp="$(mktemp)"; trap 'rm -f "$svc_tmp"' EXIT
if command -v systemctl >/dev/null 2>&1; then
  for s in "${SERVICES[@]}"; do
    state="$(systemctl is-active "$s.service" 2>/dev/null || true)"
    case "$state" in
      active)   note="unit active; observed running (observation, not a health guarantee)" ;;
      inactive|failed) note="unit exists but is not active" ;;
      *)        state="absent"; note="no such unit on this host" ;;
    esac
    SVC_NAME="$s" SVC_STATE="$state" SVC_NOTE="$note" python3 -c '
import json,os
print(json.dumps({"service":os.environ["SVC_NAME"],"state":os.environ["SVC_STATE"],"commentary":os.environ["SVC_NOTE"]}))
' >> "$svc_tmp"
  done
fi
services_json="$(python3 -c 'import json,sys;print(json.dumps([json.loads(l) for l in sys.stdin if l.strip()]))' < "$svc_tmp")"

# --- component data from the owning checker (reused, not duplicated) ---
sub_json="$("$SUB" --check --json 2>/dev/null)"
sub_exit=$?
if [ -z "$sub_json" ]; then echo "substrate check produced no data" >&2; exit 65; fi
case "$sub_exit" in 0|1|3) ;; *) echo "substrate check failed (exit $sub_exit)" >&2; exit 65 ;; esac

# --- build the full report in one python pass (no shell interpolation into JSON) ---
report="$(SUB_EXIT="$sub_exit" LABEL="$LABEL" FP="$fp" FP_DESC="$fp_desc" \
OS_TYPE="$os_type" OS_KERNEL="$os_kernel" OS_NAME="$os_name" SERVICES_JSON="$services_json" ENV_JSON="$env_json" \
python3 -c '
import json,os,sys,datetime
sub=json.loads(sys.stdin.read())
services=json.loads(os.environ["SERVICES_JSON"])
env=json.loads(os.environ["ENV_JSON"])
CRITICAL={"pi","focusa","agent-kb"}
points=0.0; present=0; missing=0; healthy=0; unhealthy=0; blockers=[]; notes=[]; offpath=[]
for c in sub["components"]:
    if not c["present"]:
        missing+=1
        if c["critical"]: blockers.append({"component":c["component"],"reason":"critical component missing"})
        continue
    present+=1
    if c["health"]=="healthy": points+=1.0; healthy+=1
    elif c["health"]=="unhealthy":
        points+=0.3; unhealthy+=1
        if c["critical"]: blockers.append({"component":c["component"],"reason":"critical component unhealthy"})
    else: points+=0.7
    if c.get("resolved_path") and "/" in c["resolved_path"]:
        import shutil
        if shutil.which(c["component"]) is None: offpath.append({"component":c["component"],"resolved_path":c["resolved_path"]})
total=len(sub["components"])
score=round(100*points/total) if total else 0
capped=False
if blockers and score>40: score=40; capped=True
breakdown=[{"component":c["component"],"score_points":c["score_points"],"critical":c["critical"]} for c in sub["components"]]
services_active=sum(1 for s in services if s["state"]=="active")
services_known=sum(1 for s in services if s["state"]!="absent")

# deterministic commentary: verdict, then the specific things an operator would act on
if not blockers and missing==0 and unhealthy==0:
    verdict="Substrate complete and responsive; all scored components healthy."
elif blockers:
    verdict="Usable substrate with CRITICAL blockers; repair the listed components before governed operation."
else:
    verdict="Substrate usable; non-critical gaps noted below."
if missing: notes.append(f"{missing} component(s) absent: "+", ".join(c["component"] for c in sub["components"] if not c["present"]))
if unhealthy: notes.append(f"{unhealthy} component(s) present but unhealthy: "+", ".join(c["component"] for c in sub["components"] if c["health"]=="unhealthy"))
for o in offpath: notes.append(f"{o['component']} is installed off PATH at {o['resolved_path']} — works here, but shells/tools using bare PATH lookups will miss it")
if missing and not offpath:
    pass
notes.append(f"{services_active} of {len(services)} known agent-OS service units active ({services_known} present on host); states are observations, not health proofs")
if capped: notes.append("score capped at 40 because a critical component is missing or unhealthy — the cap keeps blockers visible")
notes.append("readiness_score is substrate readiness only; it is not a W.I.N.S. business outcome and observations are not enrollment")

report={
 "schema":"agent-os-brownfield-audit.v3",
 "generated_at":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
 "machine_fingerprint":os.environ["FP"],
 "fingerprint_method":"sha256("+os.environ["FP_DESC"]+")",
 "label":os.environ["LABEL"],
 "os":{"type":os.environ["OS_TYPE"],"kernel":os.environ["OS_KERNEL"],"name":os.environ["OS_NAME"]},
 "environment":env,
 "audit":{"tool":"substrate-bootstrap.sh","mode":"value-free","checker_exit":int(os.environ["SUB_EXIT"])},
 "components":sub["components"],
 "install_plan":sub.get("install_plan",[]),
 "services":services,
 "readiness_score":{
   "score":score,
   "scale":"0-100 substrate readiness",
   "formula":"healthy=1.0, present+n/a=0.7, present+unhealthy=0.3, missing=0; averaged over all components; capped at 40 when any critical component (pi, focusa, agent-kb) is missing or unhealthy",
   "score_capped":capped,
   "components_total":total,"present":present,"missing":missing,"healthy":healthy,"unhealthy":unhealthy,
   "blockers":blockers,
   "breakdown":breakdown,
   "not":"W.I.N.S. business outcome; observations are not enrollment"},
 "commentary":{"verdict":verdict,"notes":notes}}
print(json.dumps(report,indent=2))
' <<< "$sub_json")" || { echo "report build failed" >&2; exit 65; }

if [ "$MODE_JSON" = "1" ]; then
  printf '%s\n' "$report"
fi
if [ "$MODE_PRINT" = "1" ]; then
  # human view is rendered FROM the same report object — one source, no drift
  printf '%s' "$report" | python3 -c '
import json,sys
r=json.load(sys.stdin)
rs=r["readiness_score"]
print("=" * 62)
print("AGENT-OS BROWNFIELD AUDIT — " + r["generated_at"])
print(("label: " + r["label"]) if r["label"] else "label: (none)")
print("host: " + r["os"]["name"] + " | kernel " + r["os"]["kernel"])
print("fingerprint: " + r["machine_fingerprint"] + " (" + r["fingerprint_method"] + "; pseudonymous, not identity)")
print("=" * 62)
print()
print("READINESS SCORE: %d/100  (substrate only — not a W.I.N.S. business outcome)" % rs["score"])
if rs["score_capped"]: print("  score capped at 40: a critical component is missing or unhealthy")
print("  components: %d total | %d present | %d missing | %d healthy | %d unhealthy" % (rs["components_total"], rs["present"], rs["missing"], rs["healthy"], rs["unhealthy"]))
if rs["blockers"]:
    print("  BLOCKERS:")
    for b in rs["blockers"]: print("    - %s: %s" % (b["component"], b["reason"]))
print()
print("COMPONENTS")
for c in r["components"]:
    st = "missing" if not c["present"] else "ok"
    crit = " [critical]" if c["critical"] else ""
    print("  %-8s %-10s%s health=%-9s points=%.1f" % (st, c["component"], crit, c["health"], c["score_points"]))
    print("      version: " + c["version"])
    if c["resolved_path"]: print("      found:   " + c["resolved_path"])
    print("      route:   " + c["route"])
    print("      note:    " + c["commentary"])
print()
print("ENVIRONMENT")
e=r["environment"]; p=e["platform"]
print("  platform: %s (%s %s) %s/%s" % (p["os"], p["distro_id"], p["distro_version"], p["arch"], e["virtualization"]))
print("  init: %s | container: %s" % (e["init"], "yes" if e["container"] else "no"))
print("  package managers: %s" % (", ".join(e["package_managers"]) if e["package_managers"] else "none detected"))
print()
print("SERVICES (systemd units, observed state)")
for s in r["services"]:
    print("  %-10s %-22s %s" % (s["state"], s["service"], s["commentary"]))
print()
print("VERDICT: " + r["commentary"]["verdict"])
for n in r["commentary"]["notes"]:
    print("  - " + n)
'
fi

if [ "$MODE_POST" = "1" ]; then
  if ! command -v curl >/dev/null 2>&1; then
    echo "DELIVERY FAILED: curl not present; report printed locally only" >&2
    exit 2
  fi
  auth_args=()
  [ -n "$TOKEN" ] && auth_args=(-H "Authorization: Bearer $TOKEN")
  code="$(curl -fsS --max-time 20 -X POST -H "Content-Type: application/json" "${auth_args[@]}" --data-binary "$report" -o /dev/null -w '%{http_code}' "$ENDPOINT" 2>/dev/null)" || code="curl-failed"
  if [ "$code" = "200" ] || [ "$code" = "201" ] || [ "$code" = "202" ]; then
    echo "REPORTED: endpoint accepted report (HTTP $code)"
  else
    echo "DELIVERY FAILED: endpoint returned $code (report printed locally only)" >&2
    exit 2
  fi
fi
# exit mirrors substrate truth: 1 missing, 3 present-but-unhealthy, 0 clean
case "$sub_exit" in
  1) exit 1 ;;
  3) exit 3 ;;
esac
exit 0