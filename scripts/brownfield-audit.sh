#!/usr/bin/env bash
# Brownfield audit — one bounded system-shape report, value-free, pretty in all forms.
# v4 (GP-08/09 gap closure): environment + resources + network from the owning
# checker, service layer per init kind, setup-state detection, report identity
# chain, services folded into the score, installer-ready plan passthrough.
# The readiness score is substrate readiness only — never a W.I.N.S. business
# outcome. An observation is not enrollment; a fingerprint is not identity.
# Exit codes: 0 clean, 1 missing components, 3 present-but-unhealthy,
#             2 delivery failure (--post), 64 usage, 65 helper/data failure,
#             66 refused endpoint, 67 concurrent-run lock held.
set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUB="$DIR/substrate-bootstrap.sh"
MODE_PRINT=1; MODE_JSON=0; MODE_POST=0; LABEL=""; ENDPOINT="${AUDIT_ENDPOINT:-}"; TOKEN="${AUDIT_TOKEN:-}"; OUTPUT=""

if command -v flock >/dev/null 2>&1; then
  exec 9>/tmp/agent-os-audit.$(id -u).lock
  flock -n 9 || { echo "another audit run holds the lock; refusing concurrent run" >&2; exit 67; }
fi

while [ $# -gt 0 ]; do
  case "$1" in
    --post) MODE_POST=1; shift ;;
    --json) MODE_JSON=1; shift ;;
    --no-print) MODE_PRINT=0; shift ;;
    --output) [ $# -ge 2 ] || { echo "--output requires a path" >&2; exit 64; }; OUTPUT="$2"; shift 2 ;;
    --label)
      if [ $# -lt 2 ] || [ -z "${2:-}" ]; then echo "--label requires a value" >&2; exit 64; fi
      LABEL="$2"; shift 2 ;;
    -h|--help)
      echo "usage: brownfield-audit.sh [--post] [--json] [--no-print] [--output FILE] [--label NAME]"
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

os_name="-"; [ -r /etc/os-release ] && os_name="$(. /etc/os-release && echo "${PRETTY_NAME:--}")"
os_type="$(uname -s 2>/dev/null || echo '-')"
os_kernel="$(uname -r 2>/dev/null || echo '-')"

# --- service-shape section: state per detected init system (value-free) ---
SERVICES=(
  "focusa-daemon" "context-core" "agent-kb-api" "wirebot-scoreboard" "openclaw-gateway"
  "wbt" "mem0-wirebot" "letta-wirebot" "letta-relay" "agent-audit" "agent-kb-refresh"
  "cloudflared-wirebot" "cloudflared-agent-audit" "wirebot-wbt"
)
svc_tmp="$(mktemp)"; trap 'rm -f "$svc_tmp"' EXIT
svc_domain="none"
if [ "$(uname -s)" = "Darwin" ] && command -v launchctl >/dev/null 2>&1; then
  svc_domain="launchd"
  for s in "${SERVICES[@]}"; do
    state="absent"; note="not found in launchctl list"
    if launchctl list 2>/dev/null | grep -q "$s"; then
      state="loaded"; note="present in launchctl list (loaded label; not a health guarantee)"
    fi
    SVC_NAME="$s" SVC_STATE="$state" SVC_NOTE="$note" python3 -c '
import json,os
print(json.dumps({"service":os.environ["SVC_NAME"],"state":os.environ["SVC_STATE"],"commentary":os.environ["SVC_NOTE"]}))' >> "$svc_tmp"
  done
elif command -v systemctl >/dev/null 2>&1; then
  svc_domain="systemd"
  for s in "${SERVICES[@]}"; do
    state="$(timeout 5 systemctl is-active "$s.service" 2>/dev/null || true)"
    case "$state" in
      active)   note="unit active; observed running (observation, not a health guarantee)" ;;
      inactive|failed) note="unit exists but is not active" ;;
      *)        state="absent"; note="no such unit on this host" ;;
    esac
    SVC_NAME="$s" SVC_STATE="$state" SVC_NOTE="$note" python3 -c '
import json,os
print(json.dumps({"service":os.environ["SVC_NAME"],"state":os.environ["SVC_STATE"],"commentary":os.environ["SVC_NOTE"]}))' >> "$svc_tmp"
  done
else
  for s in "${SERVICES[@]}"; do
    SVC_NAME="$s" SVC_STATE="unknown" SVC_NOTE="no supported init detection on this host" python3 -c '
import json,os
print(json.dumps({"service":os.environ["SVC_NAME"],"state":os.environ["SVC_STATE"],"commentary":os.environ["SVC_NOTE"]}))' >> "$svc_tmp"
  done
fi
services_json="$(python3 -c 'import json,sys;print(json.dumps([json.loads(l) for l in sys.stdin if l.strip()]))' < "$svc_tmp")"

# --- setup-state detection: fresh vs partially configured vs configured ---
setup_state="fresh"; setup_notes=""
fcount=0
[ -d "$HOME/.focusa" ] && fcount=$((fcount+1))
[ -d "$HOME/.beads" ] && fcount=$((fcount+1))
[ -f "$HOME/AGENTS.md" ] && fcount=$((fcount+1))
[ -n "$(git config --global user.email 2>/dev/null)" ] && fcount=$((fcount+1))
case "$fcount" in
  0) setup_state="fresh"; setup_notes="no agent-OS markers found (no ~/.focusa, ~/.beads, AGENTS.md, git identity)" ;;
  1|2) setup_state="partial"; setup_notes="$fcount of 4 agent-OS markers present" ;;
  *) setup_state="configured"; setup_notes="$fcount of 4 agent-OS markers present" ;;
esac

# --- component + plan data from the owning checker (reused, not duplicated) ---
sub_json="$("$SUB" --check --json 2>/dev/null)"
sub_exit=$?
if [ -z "$sub_json" ]; then echo "substrate check produced no data" >&2; exit 65; fi
case "$sub_exit" in 0|1|3) ;; *) echo "substrate check failed (exit $sub_exit)" >&2; exit 65 ;; esac

# --- report identity chain (dedup + diffing for the future receiver) ---
cache_dir="$HOME/.cache/agent-os-audit"; mkdir -p "$cache_dir" 2>/dev/null || true
prev_id=""; prev_hash=""
if [ -r "$cache_dir/last.json" ]; then
  prev_id="$(python3 -c 'import json;print(json.load(open("'$cache_dir'/last.json")).get("report_id",""))' 2>/dev/null || true)"
  prev_hash="$(python3 -c 'import json;print(json.load(open("'$cache_dir'/last.json")).get("report_hash",""))' 2>/dev/null || true)"
fi

# --- build the full report in one python pass (no shell interpolation into JSON) ---
report="$(SUB_EXIT="$sub_exit" LABEL="$LABEL" FP="$fp" FP_DESC="$fp_desc" \
OS_NAME="$os_name" SERVICES_JSON="$services_json" SVC_DOMAIN="$svc_domain" SETUP_STATE="$setup_state" \
SETUP_NOTES="$setup_notes" PREV_ID="$prev_id" PREV_HASH="$prev_hash" \
python3 -c '
import json,os,sys,datetime,uuid
sub=json.loads(sys.stdin.read())
services=json.loads(os.environ["SERVICES_JSON"])
env=sub["environment"]
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
    if c.get("resolved_path"):
        import shutil
        if shutil.which(c["component"]) is None: offpath.append(c["component"])
total=len(sub["components"])
comp_score=round(100*points/total) if total else 0
services_active=sum(1 for s in services if s["state"]=="active")
services_known=sum(1 for s in services if s["state"]!="absent")
svc_score=round(100*services_active/services_known) if services_known else 0
score=round(0.8*comp_score+0.2*svc_score)
capped=False
if blockers and score>40: score=40; capped=True
breakdown=[{"component":c["component"],"score_points":c["score_points"],"critical":c["critical"]} for c in sub["components"]]

res=env.get("resources",{}); net=env.get("network",{})
# feasibility gates: things that would make an install run fail regardless of plan
try:
    res_disk=int(res.get("disk_avail_mb") or -1)
    if 0<=res_disk<2048:
        blockers.append({"component":"disk","reason":"only %d MB free under home; installs may fail" % res_disk})
except (TypeError,ValueError):
    pass
if net.get("tcp443")=="failed":
    notes.append("github.com:443 unreachable — installs will fail until network is fixed")
if net.get("dns")=="failed":
    notes.append("DNS resolution failing — install sources unresolvable")
if env.get("clock_ntp")=="no":
    notes.append("clock not NTP-synchronized — TLS/certificate operations may fail")

if not blockers and missing==0 and unhealthy==0:
    verdict="Substrate complete and responsive; all scored components healthy."
elif blockers:
    verdict="Usable substrate with CRITICAL blockers; repair the listed components before governed operation."
else:
    verdict="Substrate usable; non-critical gaps noted below."
if missing: notes.append(f"{missing} component(s) absent: "+", ".join(c["component"] for c in sub["components"] if not c["present"]))
if unhealthy: notes.append(f"{unhealthy} component(s) present but unhealthy: "+", ".join(c["component"] for c in sub["components"] if c["health"]=="unhealthy"))
for o in offpath: notes.append(f"{o} is installed off PATH — shells using bare PATH lookups will miss it; add the directory to PATH or symlink")
notes.append(f"{services_active} of {len(services)} known agent-OS service units active ({services_known} present, {os.environ["SVC_DOMAIN"]}); states are observations, not health proofs")
notes.append(f"setup state: {os.environ["SETUP_STATE"]} ({os.environ["SETUP_NOTES"]})")
if capped: notes.append("score capped at 40 because a critical component is missing or unhealthy — the cap keeps blockers visible")
notes.append("readiness_score is substrate+runtime readiness only; it is not a W.I.N.S. business outcome and observations are not enrollment")

report_id=str(uuid.uuid4())
report={
 "schema":"agent-os-brownfield-audit.v4",
 "report_id":report_id,
 "generated_at":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
 "previous_report_id":os.environ["PREV_ID"] or None,
 "previous_report_hash":os.environ["PREV_HASH"] or None,
 "machine_fingerprint":os.environ["FP"],
 "fingerprint_method":"sha256("+os.environ["FP_DESC"]+")",
 "label":os.environ["LABEL"],
 "os":{"name":os.environ["OS_NAME"]},
 "environment":env,
 "audit":{"tool":"substrate-bootstrap.sh","mode":"value-free","checker_exit":int(os.environ["SUB_EXIT"])},
 "setup_state":{"state":{"fresh":"fresh","partial":"partial","configured":"configured"}[os.environ["SETUP_STATE"]],"note":os.environ["SETUP_NOTES"]},
 "components":sub["components"],
 "services":services,
 "install_plan":sub.get("install_plan",[]),
 "readiness_score":{
   "score":score,
   "scale":"0-100 substrate+runtime readiness",
   "formula":"components (80%): healthy=1.0, present+n/a=0.7, present+unhealthy=0.3, missing=0 averaged; runtime (20%): active/known service units; capped at 40 when any critical component is missing or unhealthy",
   "score_capped":capped,
   "component_score":comp_score,"service_score":svc_score,
   "services_active":services_active,"services_known":services_known,
   "components_total":total,"present":present,"missing":missing,"healthy":healthy,"unhealthy":unhealthy,
   "blockers":blockers,
   "breakdown":breakdown,
   "not":"W.I.N.S. business outcome; observations are not enrollment"},
 "commentary":{"verdict":verdict,"notes":notes}}
import hashlib
rh=hashlib.sha256(json.dumps(report,sort_keys=True).encode()).hexdigest()
report["report_hash"]="sha256:"+rh
os.makedirs(os.path.expanduser("~/.cache/agent-os-audit"),exist_ok=True)
json.dump({"report_id":report_id,"report_hash":report["report_hash"]},open(os.path.expanduser("~/.cache/agent-os-audit/last.json"),"w"))
print(json.dumps(report,indent=2))
' <<< "$sub_json")" || { echo "report build failed" >&2; exit 65; }

emit() {
  if [ -n "$OUTPUT" ]; then printf '%s\n' "$report" > "$OUTPUT"; fi
}
emit

if [ "$MODE_JSON" = "1" ]; then
  printf '%s\n' "$report"
fi
if [ "$MODE_PRINT" = "1" ]; then
  printf '%s' "$report" | python3 -c '
import json,sys
r=json.load(sys.stdin)
rs=r["readiness_score"]
print("=" * 62)
print("AGENT-OS BROWNFIELD AUDIT — " + r["generated_at"])
print("report: " + r["report_id"] + ("" if not r["previous_report_id"] else "  (prev: " + r["previous_report_id"] + ")"))
print(("label: " + r["label"]) if r["label"] else "label: (none)")
print("host: " + r["os"]["name"] + " | fingerprint " + r["machine_fingerprint"][:20] + "… (pseudonymous, not identity)")
print("setup state: " + r["setup_state"]["state"] + " — " + r["setup_state"]["note"])
print("=" * 62)
print()
print("READINESS SCORE: %d/100  (substrate+runtime — not a W.I.N.S. outcome)" % rs["score"])
print("  component score %d/100 | service score %d/100 (0.8×comp + 0.2×svc)" % (rs["component_score"], rs["service_score"]))
if rs["score_capped"]: print("  score capped at 40: a critical component is missing or unhealthy")
print("  components: %d total | %d present | %d missing | %d healthy | %d unhealthy" % (rs["components_total"], rs["present"], rs["missing"], rs["healthy"], rs["unhealthy"]))
if rs["blockers"]:
    print("  BLOCKERS:")
    for b in rs["blockers"]: print("    - %s: %s" % (b["component"], b["reason"]))
print()
e=r["environment"]; p=e["platform"]
print("ENVIRONMENT")
print("  platform: %s (%s %s) %s | virt %s | wsl %s" % (p["os"], p["distro_id"], p["distro_version"], p["arch"], e["virtualization"], "yes" if e.get("wsl") else "no"))
print("  init: %s | container: %s" % (e["init"], "yes" if e["container"] else "no"))
print("  package managers: %s" % (", ".join(e["package_managers"]) if e["package_managers"] else "none detected"))
print("  resources: disk %s MB free | mem %s MB available" % (e["resources"]["disk_avail_mb"], e["resources"]["mem_avail_mb"]))
print("  network: dns %s | tcp443 %s | clock ntp %s" % (e["network"]["dns"], e["network"]["tcp443"], e["clock_ntp"]))
print()
print("COMPONENTS")
for c in r["components"]:
    st = "missing" if not c["present"] else "ok"
    tag = " [base]" if c["base"] else (" [critical]" if c["critical"] else "")
    print("  %-8s %-10s%-13s health=%-9s points=%.1f" % (st, c["component"], tag, c["health"], c["score_points"]))
    print("      version: %s | %s" % (c["version"], c["commentary"]))
    if c["resolved_path"]: print("      found:   " + c["resolved_path"])
    print("      route(%s, order %d, admin=%s): %s" % (c["route_kind"], c["order"], "yes" if c["requires_admin"] else "no", c["route"]))
print()
plan=r["install_plan"]
if plan:
    print("INSTALL PLAN (operator-authorized execution only; base-only apply supported)")
    for e2 in plan:
        print("  [%d] %-10s (%s, admin=%s%s) %s" % (e2["order"], e2["component"], e2["route_kind"], "yes" if e2["requires_admin"] else "no", ", after "+",".join(e2["depends_on"]) if e2["depends_on"] else "", e2["route"]))
        print("      verify after install: %s" % e2["verify_cmd"])
else:
    print("INSTALL PLAN: nothing missing")
print()
print("SERVICES (observed state)")
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
case "$sub_exit" in
  1) exit 1 ;;
  3) exit 3 ;;
esac
exit 0