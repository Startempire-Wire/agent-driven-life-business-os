#!/usr/bin/env bash
# Golden Path Stage 1 — substrate bootstrap: verify, report, and (base-only) install
# the foundational toolchain as owning code. Idempotent, value-free, fail-closed.
#
# v4 (GP-08 gap closure):
#   - preflight: python3 required for report building (fail-closed exit 68)
#   - base primitives (python3, node, npm, git, curl) are first-class components
#   - install_plan: order, requires_admin, verify_cmd, depends_on per entry
#   - --apply base --yes: installs ONLY missing base primitives via the detected
#     package manager; every non-base component remains print-routes-only
#   - resource floors (disk/mem), network reachability + DNS + clock sync
#   - WSL and launchd service layers; setup_state (fresh|partial|configured)
#   - home-path redaction (paths render as ~), single-run flock, --output FILE
set -uo pipefail

MODE="check"; JSON=0; OUTPUT=""; APPLY=0; CONFIRM=0; DRYRUN=0; TOTAL=16
while [ $# -gt 0 ]; do
  case "$1" in
    --check) MODE=check; shift ;;
    --json) JSON=1; shift ;;
    --install) MODE=install; shift ;;
    --output) [ $# -ge 2 ] || { echo "--output requires a path" >&2; exit 64; }; OUTPUT="$2"; shift 2 ;;
    --apply)
      [ $# -ge 2 ] || { echo "--apply requires a scope (only 'base' is supported)" >&2; exit 64; }
      [ "$2" = "base" ] || { echo "only --apply base is supported; heavier installs stay operator-run" >&2; exit 64; }
      APPLY=1; MODE=apply; shift 2 ;;
    --yes) CONFIRM=1; shift ;;
    --dry-run) DRYRUN=1; shift ;;
    -h|--help)
      echo "usage: substrate-bootstrap.sh [--check|--install|--apply base] [--json] [--output FILE] [--yes] [--dry-run]"
      echo "  --apply base --yes        installs ONLY missing base primitives (python3, node, npm, git, curl)"
      echo "                            via the detected package manager; requires root/sudo for admin routes."
      echo "  --apply base --dry-run    prints the exact install commands that would run; executes nothing."
      echo "  All non-base components are always print-routes-only; heavier installs are operator-authorized runs."
      exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 64 ;;
  esac
done

# --- single-run lock (best-effort; advisory if flock unavailable) ---
if command -v flock >/dev/null 2>&1; then
  exec 9>/tmp/agent-os-substrate.$(id -u).lock
  flock -n 9 || { echo "another substrate run holds the lock; refusing concurrent run" >&2; exit 67; }
fi

# --- preflight: report building requires python3 (fail-closed, honest) ---
if ! command -v python3 >/dev/null 2>&1; then
  echo "PREFLIGHT FAILED: python3 is required to build the report but is not installed." >&2
  echo "Base install route: sudo dnf install -y python3 | sudo apt-get install -y python3 | brew install python3" >&2
  exit 68
fi

TIMEOUT_CMD=""
command -v timeout >/dev/null 2>&1 && TIMEOUT_CMD="timeout 15"

find_bin() {
  local name="$1" d
  command -v "$name" 2>/dev/null && return 0
  for d in /usr/local/bin /usr/bin /opt/cpanel/ea-nodejs20/bin /opt/homebrew/bin \
           /usr/local/homebrew/bin "$HOME/.local/bin" "$HOME/bin" /snap/bin; do
    [ -x "$d/$name" ] && { echo "$d/$name"; return 0; }
  done
  return 1
}

# name|version-cmd|health-cmd|official route|critical|route_kind|base|order|requires_admin|depends_on
COMPONENTS=(
  "git|git --version|-|git via package manager or git-scm.com|true|pkg|true|0|admin|"
  "curl|curl --version|-|curl via package manager|true|pkg|true|0|admin|"
  "python3|python3 --version|-|python3 via package manager|true|pkg|true|0|admin|"
  "node|node --version|-|nodejs via package manager or nodesource|true|pkg|true|0|admin|"
  "npm|npm --version|-|npm ships with nodejs|true|pkg|true|0|user|node"
  "pi|pi --version|-|npm install -g @earendil-works/pi-coding-agent|true|npm|false|1|user|npm"
  "focusa|focusa --version|focusa status --agent --json|focusa official upgrade channel|true|script|false|2|admin|"
  "rbw|rbw --version|-|official rbw release per vault runbook|false|binary|false|2|user|"
  "gh|gh --version|-|official gh installer (cli.github.com)|false|binary|false|2|user|"
  "wrangler|wrangler --version|-|npm install -g wrangler|false|npm|false|2|user|npm"
  "gog|gog version|-|official gog release binary|false|binary|false|2|user|"
  "bd|bd --version|-|official beads install|false|binary|false|2|user|"
  "tailscale|tailscale version|tailscale status|official tailscale install script|false|script|false|2|admin|"
  "agent-kb|agent-kb version|agent-kb freshness --json|canonical KB deployment install|true|script|false|2|admin|"
  "openclaw|openclaw --version|-|official OpenClaw install per owning runbook|false|runbook|false|3|admin|"
  "uiai|uiai --version|-|official UIAI Engine install per owning runbook|false|runbook|false|3|admin|"
)

# --- environment detection (value-free presence/kind facts) ---
os_type="$(uname -s 2>/dev/null || echo '-')"
os_arch="$(uname -m 2>/dev/null || echo '-')"
os_id="-"; os_version="-"; os_name="-"
if [ -r /etc/os-release ]; then
  os_id="$(. /etc/os-release && echo "${ID:--}")"
  os_version="$(. /etc/os-release && echo "${VERSION_ID:--}")"
  os_name="$(. /etc/os-release && echo "${PRETTY_NAME:--}")"
fi
os_kernel="$(uname -r 2>/dev/null || echo '-')"
is_wsl="no"; [ -r /proc/version ] && grep -qi microsoft /proc/version 2>/dev/null && is_wsl="yes"

init_kind="unknown"
if [ "$os_type" = "Darwin" ]; then init_kind="launchd"
elif command -v systemctl >/dev/null 2>&1; then init_kind="systemd"
fi
virt_kind="-"; container="no"
if command -v systemd-detect-virt >/dev/null 2>&1; then virt_kind="$(systemd-detect-virt 2>/dev/null || echo none)"; fi
[ -f /.dockerenv ] && container="yes"
[ -f /proc/vz ] && { container="yes"; [ "$virt_kind" = "-" ] && virt_kind="openvz"; }

pkg_managers=""
for pm in apt-get dnf yum brew apk zypper npm cargo; do
  command -v "$pm" >/dev/null 2>&1 && pkg_managers="$pkg_managers $pm"
done
pkg_managers="$(printf '%s' "$pkg_managers" | sed 's/^ //')"

# --- resource floors ---
disk_avail_mb="-"; [ -d "$HOME" ] && disk_avail_mb="$(df -Pm "$HOME" 2>/dev/null | awk 'NR==2{print $4}')"
mem_avail_mb="-"
if command -v free >/dev/null 2>&1; then mem_avail_mb="$(free -m 2>/dev/null | awk '/^Mem/{print $7}')"; fi

# --- network + clock (reachability facts, value-free) ---
net_dns="unknown"; net_tcp443="unknown"; clock_ntp="unknown"
NET_JSON="$(timeout 10 python3 -c '
import json,socket
r={"dns":"unknown","tcp443":"unknown"}
try:
    socket.getaddrinfo("github.com",443); r["dns"]="ok"
except Exception: r["dns"]="failed"
try:
    s=socket.create_connection(("github.com",443),timeout=5); s.close(); r["tcp443"]="ok"
except Exception: r["tcp443"]="failed"
print(json.dumps(r))' 2>/dev/null || echo '{}')"
net_dns="$(printf '%s' "$NET_JSON" | python3 -c 'import json,sys;print(json.load(sys.stdin).get("dns","unknown"))' 2>/dev/null || echo unknown)"
net_tcp443="$(printf '%s' "$NET_JSON" | python3 -c 'import json,sys;print(json.load(sys.stdin).get("tcp443","unknown"))' 2>/dev/null || echo unknown)"
if command -v timedatectl >/dev/null 2>&1; then
  if timedatectl show -p NTPSynchronized 2>/dev/null | grep -q yes; then clock_ntp="yes"; else clock_ntp="no"; fi
fi

# --- component checks ---
tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT
missing=0; unhealthy=0; missing_base=0; idx=0
# progress: "working..." meter to stderr so stdout stays parseable in every mode
progress() { printf '\rworking... [%d/%d] %s        ' "$1" "$TOTAL" "$2" >&2; }

for c in "${COMPONENTS[@]}"; do
  IFS='|' read -r name vcmd hcmd route critical kind base order priv deps <<< "$c"
  idx=$((idx+1)); progress "$idx" "$name"
  bin_path=""; ver="-"; health="n/a"; st="missing"; vargs=""
  bin_path="$(find_bin "$name" 2>/dev/null || true)"
  if [ -n "$bin_path" ]; then
    vargs="${vcmd#"$name" }"
    ver="$($TIMEOUT_CMD "$bin_path" $vargs 2>/dev/null | head -n1)"
    [ -n "$ver" ] || ver="-"
    health="n/a"
    if [ "$name" = "agent-kb" ]; then
      if $TIMEOUT_CMD agent-kb freshness --json 2>/dev/null | grep -q '"status": *"ok"'; then health="healthy"; else health="unhealthy"; fi
    elif [ "$hcmd" != "-" ]; then
      if $TIMEOUT_CMD $hcmd >/dev/null 2>&1; then health="healthy"; else health="unhealthy"; fi
    fi
    st="ok"; [ "$health" = "unhealthy" ] && unhealthy=$((unhealthy+1))
  else
    bin_path=""; ver="-"; health="n/a"; st="missing"; missing=$((missing+1))
    [ "$base" = "true" ] && missing_base=$((missing_base+1))
  fi
  if [ "$MODE" = "install" ] && [ "$st" = "missing" ]; then
    echo "INSTALL ROUTE (not executed; requires operator-authorized deployment run): $name -> $route"
  fi
  COMP_NAME="$name" COMP_PRESENT="$st" COMP_VERSION="$ver" COMP_HEALTH="$health" \
  COMP_ROUTE="$route" COMP_CRITICAL="$critical" COMP_KIND="$kind" COMP_BASE="$base" \
  COMP_ORDER="$order" COMP_PRIV="$priv" COMP_DEPS="$deps" COMP_PATH="$bin_path" \
  COMP_VARGS="$vargs" \
  python3 -c '
import json,os
present=os.environ["COMP_PRESENT"]!="missing";health=os.environ["COMP_HEALTH"]
critical=os.environ["COMP_CRITICAL"]=="true";base=os.environ["COMP_BASE"]=="true"
path=os.environ["COMP_PATH"];deps=[d for d in os.environ["COMP_DEPS"].split(",") if d]
if not present: pts=0.0
elif health=="healthy": pts=1.0
elif health=="unhealthy": pts=0.3
else: pts=0.7
if not present:
    note=("not found on PATH or well-known locations"
          + (" — BASE PRIMITIVE: install first, other components depend on it" if base else ""))
elif health=="healthy": note="present and responding to its health probe"
elif health=="unhealthy":
    note="present but health probe failed; binary runs, service not answering" + (" — CRITICAL" if critical else "")
else: note="present; no health probe defined (n/a, not assumed healthy)"
# redact home directories in displayed paths
if path:
    import re
    path=re.sub(r"^/home/[^/]+", "~", path); path=re.sub(r"^/Users/[^/]+", "~", path)
row={"component":os.environ["COMP_NAME"],"present":present,"version":os.environ["COMP_VERSION"],
 "health":health,"route":os.environ["COMP_ROUTE"],"critical":critical,"base":base,
 "route_kind":os.environ["COMP_KIND"],"order":int(os.environ["COMP_ORDER"]),
 "requires_admin":os.environ["COMP_PRIV"]=="admin","depends_on":deps,
 "verify_cmd":(os.environ["COMP_NAME"]+" "+os.environ["COMP_VARGS"]).strip(),
 "resolved_path":path or None,"score_points":pts,"commentary":note}
print(json.dumps(row))
' >> "$tmp"
done

rows_json="$(python3 -c 'import json,sys;print(json.dumps([json.loads(l) for l in sys.stdin if l.strip()]))' < "$tmp")"
printf '\rworking... [16/16] done                    \n' >&2

# --- base-primitive apply (operator-authorized; base only) ---
# --- base-primitive apply (operator-authorized; base only; --dry-run shows commands) ---
apply_result="not-requested"
if [ "$MODE" = "apply" ]; then
  if [ "$CONFIRM" != "1" ] && [ "$DRYRUN" != "1" ]; then
    echo "REFUSED: --apply base requires --yes (execute) or --dry-run (preview)" >&2
    exit 64
  fi
  if [ "$missing_base" = "0" ]; then
    if [ "$DRYRUN" = "1" ]; then
      apply_result="dry-run: all base primitives present; nothing to install"
      echo "DRY-RUN: $apply_result"
    else
      apply_result="all base primitives present; nothing to install"
      echo "APPLY: $apply_result"
    fi
  else
    applied=""; failed=""
    pkg=""
    case "$os_id" in
      almalinux|rhel|centos|rocky|fedora) command -v dnf >/dev/null 2>&1 && pkg="dnf install -y" ;;
      ubuntu|debian) command -v apt-get >/dev/null 2>&1 && pkg="apt-get install -y" ;;
      darwin) command -v brew >/dev/null 2>&1 && pkg="brew install" ;;
    esac
    if [ -z "$pkg" ]; then
      echo "APPLY FAILED: no supported package manager detected for $os_id (dnf/apt-get/brew)" >&2
      apply_result="failed: no supported package manager"
    elif [ "$DRYRUN" = "1" ]; then
      echo "DRY-RUN: no packages will be installed; the following commands WOULD run on an operator-authorized execution:"
      for c in "${COMPONENTS[@]}"; do
        IFS='|' read -r name vcmd hcmd route critical kind base order priv deps <<< "$c"
        [ "$base" = "true" ] || continue
        find_bin "$name" >/dev/null 2>&1 && continue
        case "$name" in
          npm) find_bin node >/dev/null 2>&1 || continue ;;  # node's install provides npm; listed once under node
          node) target="nodejs" ;;
          python3) target="python3" ;;
          git) target="git" ;;
          curl) target="curl" ;;
        esac
        admin="user-local"; [ "$priv" = "admin" ] && admin="requires root/sudo"
        echo "  DRY-RUN: $pkg $target   # $name ($admin)"
      done
      apply_result="dry-run: commands printed; nothing executed"
    else
      echo "APPLY: installing missing base primitives via '$pkg' (admin routes need root/sudo)"
      for c in "${COMPONENTS[@]}"; do
        IFS='|' read -r name vcmd hcmd route critical kind base order priv deps <<< "$c"
        [ "$base" = "true" ] || continue
        find_bin "$name" >/dev/null 2>&1 && continue
        # npm depends on node; nodejs package provides both — listed/installed once under node
        case "$name" in
          npm) continue ;;  # node's install provides npm; node entry covers it when node is missing
          node) target="nodejs" ;;
          python3) target="python3" ;;
          git) target="git" ;;
          curl) target="curl" ;;
        esac
        if $pkg "$target" >/dev/null 2>&1; then
          applied="$applied $name"
        else
          failed="$failed $name"
        fi
      done
      apply_result="applied:${applied:- none}; failed:${failed:- none}"
      echo "APPLY RESULT:$apply_result"
    fi
  fi
fi

if [ "$JSON" = "1" ]; then
  python3 -c '
import json,sys
rows=json.loads(sys.argv[1])
plan=[{"component":r["component"],"route":r["route"],"route_kind":r["route_kind"],
       "critical":r["critical"],"base":r["base"],"order":r["order"],
       "requires_admin":r["requires_admin"],"depends_on":r["depends_on"],
       "verify_cmd":r["verify_cmd"]} for r in rows if not r["present"]]
plan.sort(key=lambda e:(e["order"], e["component"]))
env=json.loads(sys.argv[2])
out={"schema":"agent-os-substrate-check.v4","environment":env,"components":rows,
     "install_plan":plan,
     "install_policy":"--apply base --yes installs ONLY base primitives; every other route is printed for an operator-authorized run"}
print(json.dumps(out,indent=2))' "$rows_json" \
    "$(ENV_OS="$os_type" ENV_ID="$os_id" ENV_VER="$os_version" ENV_KERNEL="$os_kernel" \
       ENV_ARCH="$os_arch" ENV_INIT="$init_kind" ENV_VIRT="$virt_kind" ENV_CONT="$container" \
       ENV_WSL="$is_wsl" ENV_PKGS="$pkg_managers" ENV_DISK="$disk_avail_mb" ENV_MEM="$mem_avail_mb" \
       ENV_DNS="$net_dns" ENV_TCP="$net_tcp443" ENV_NTP="$clock_ntp" \
       python3 -c '
import json,os
env={"platform":{"os":os.environ["ENV_OS"],"distro_id":os.environ["ENV_ID"],
 "distro_version":os.environ["ENV_VER"],"kernel":os.environ["ENV_KERNEL"],"arch":os.environ["ENV_ARCH"]},
 "init":os.environ["ENV_INIT"],"virtualization":os.environ["ENV_VIRT"],
 "container":os.environ["ENV_CONT"]=="yes","wsl":os.environ["ENV_WSL"]=="yes",
 "package_managers":os.environ["ENV_PKGS"].split() if os.environ["ENV_PKGS"] else [],
 "resources":{"disk_avail_mb":os.environ["ENV_DISK"],"mem_avail_mb":os.environ["ENV_MEM"]},
 "network":{"dns":os.environ["ENV_DNS"],"tcp443":os.environ["ENV_TCP"]},"clock_ntp":os.environ["ENV_NTP"],
 "commentary":"presence/kind facts; resources, network and clock gates drive install-plan feasibility"}
print(json.dumps(env))')"
  [ -n "$OUTPUT" ] && cp <(python3 -c 'import json,sys;rows=json.loads(sys.argv[1])' "$rows_json") "$OUTPUT" 2>/dev/null || true
else
  printf '%s\n' "$rows_json" | python3 -c '
import json,sys
for r in json.load(sys.stdin):
    st = "missing" if not r["present"] else "ok"
    tag = " [base]" if r["base"] else (" [critical]" if r["critical"] else "")
    print("# %s" % r["commentary"])
    print("%-8s %-10s%-13s health=%-9s points=%.1f" % (st, r["component"], tag, r["health"], r["score_points"]))
    print("    version: %s | route(%s, order %d, admin=%s): %s" % (r["version"], r["route_kind"], r["order"], "yes" if r["requires_admin"] else "no", r["route"]))
    if r["resolved_path"]: print("    found: %s" % r["resolved_path"])
    if r["depends_on"]: print("    depends on: %s" % ", ".join(r["depends_on"]))
'
fi

if [ "$missing" -gt 0 ]; then exit 1; fi
if [ "$unhealthy" -gt 0 ]; then exit 3; fi
exit 0
