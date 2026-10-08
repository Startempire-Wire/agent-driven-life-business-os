#!/usr/bin/env python3
"""Read-only SOVOS first-value plan from existing audit and owner-confirmed intent.

Not an installer, scheduler, authorization source, or alternative Golden Path.
Private owner intent stays in local files; outputs are not fleet-audit payloads.
"""
import argparse
import json
from pathlib import Path

SETUP_MODES = {"wirebot_sovereign_operator", "wirebot_sovereign", "wirebot_direct", "wirebot_network"}
HOSTING = {"dedicated_vps", "managed_isolated"}
STATES = {"verified", "configured", "missing", "blocked", "unknown"}
RECIPES = (
    {"key": "team_dispatch", "goals": ("team", "operations"), "source_any": ("tasks",),
     "templates": ("workforce-dispatch", "evidence-closure"),
     "outcome": "An actual team assignment is accepted and its next action is visible."},
    {"key": "inquiry_followup", "goals": ("revenue", "service"), "source_any": ("email", "crm"),
     "templates": ("inquiry-triage", "follow-up", "follow-through"),
     "outcome": "An authorized inquiry is handled and its follow-through recorded."},
    {"key": "daily_orientation", "goals": ("capacity", "administration", "operations"),
     "source_any": ("email", "calendar", "tasks"),
     "templates": ("orientation", "weekly-planning", "evidence-closure"),
     "outcome": "The owner receives a fresh, useful, source-backed operating brief."},
    {"key": "finance_oversight", "goals": ("finance",), "source_any": ("billing",),
     "templates": ("finance-operations", "reconciliation", "evidence-closure"),
     "outcome": "An authorized finance obligation or discrepancy is reconciled."},
    {"key": "document_action_review", "goals": ("administration", "service"),
     "source_any": ("documents",),
     "templates": ("delivery-case-review", "follow-through"),
     "outcome": "One document-driven commitment reaches a verified next action."},
)

def load_json(path):
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("input must be a JSON object")
    return obj

def statuses(obj, name):
    val = obj.get(name, {})
    if not isinstance(val, dict):
        raise ValueError(f"{name} must be a JSON object")
    for key, state in val.items():
        if not isinstance(key, str) or state not in STATES:
            raise ValueError(f"{name} entries must use verified/configured/missing/blocked/unknown")
    return val

def build(audit, intent):
    if audit.get("schema") not in {"agent-os-brownfield-audit.v5", "agent-os-substrate-check.v5"}:
        raise ValueError("expected existing audit v5 or substrate check v5")
    hosting = intent.get("hosting_profile")
    mode = intent.get("setup_mode")
    goal = intent.get("first_goal")
    if hosting is not None and hosting not in HOSTING:
        raise ValueError("unsupported hosting_profile")
    if mode is not None and mode not in SETUP_MODES:
        raise ValueError("unsupported setup_mode")
    if goal is not None and goal not in {g for r in RECIPES for g in r["goals"]}:
        raise ValueError("unsupported first_goal")
    features = statuses(intent, "verified_capabilities")
    sources = statuses(intent, "source_access")
    raw_components = audit.get("components", [])
    if not isinstance(raw_components, list):
        raise ValueError("components must be a list")
    # Only allow the documented checker vocabulary into the handoff.
    known = {"git", "curl", "python3", "node", "npm", "pi", "focusa", "rbw", "gh",
             "wrangler", "gog", "bd", "tailscale", "agent-kb", "openclaw", "uiai"}
    observed = []
    for item in raw_components:
        if isinstance(item, dict) and item.get("component") in known:
            observed.append({"component": item["component"],
                             "cli_present": bool(item.get("present")),
                             "health_observed": item.get("health", "unknown")})
    setup = audit.get("setup_state") or {}
    setup_hint = setup.get("state", "unknown") if isinstance(setup, dict) else "unknown"
    requirements = {
        "dedicated_vps": ("customer_vps", "private_mesh", "local_body", "operating_partner"),
        "managed_isolated": ("hosted_runtime", "tenant_isolation", "operating_partner"),
    }
    missing_profile = [key for key in requirements.get(hosting, ()) if features.get(key) != "verified"]
    notices = []
    if not mode:
        notices.append("Confirm the exact Wirebot offer; numeric tiers do not determine setup mode.")
    if not hosting:
        notices.append("Confirm dedicated full-Sovereign versus managed isolated hosting from the offer.")
    if not goal:
        notices.append("Ask the owner for one urgent outcome; tool presence cannot infer business intent.")
    candidates = []
    for recipe in RECIPES:
        if goal is None or goal not in recipe["goals"]:
            continue
        verified = [s for s in recipe["source_any"] if sources.get(s) == "verified"]
        unverified = [s for s in recipe["source_any"] if sources.get(s) != "verified"]
        candidates.append({"key": recipe["key"], "templates": list(recipe["templates"]),
                           "expected_outcome": recipe["outcome"],
                           "ready_source": verified[0] if verified else None,
                           "source_candidates_to_verify": unverified if not verified else [],
                           "readiness": "source_verified" if verified else "source_unverified"})
    candidates.sort(key=lambda r: (r["readiness"] != "source_verified", r["key"]))
    chosen = candidates[0] if candidates else None
    first_value_ready = bool(hosting and mode and chosen and chosen["ready_source"] and
                             features.get("operating_partner") == "verified" and
                             features.get("owner_channel") == "verified")
    # Customer environment completion and a bounded pilot have different gates.
    steps = [
        {"step": "reconcile", "action": "Check owner, offer, current sources, agents and runtime; reuse rather than reinstall.",
         "status": "inspect"},
        {"step": "hosting", "action": "Verify only applicable isolated/dedicated hosting capabilities.",
         "status": "verify" if missing_profile else ("ready" if hosting else "needs_owner_choice")},
        {"step": "first_outcome",
         "action": "Propose " + chosen["key"] if chosen else "Ask for one owner-prioritized business outcome.",
         "status": "proposed" if chosen else "needs_owner_choice"},
        {"step": "source",
         "action": "Use verified " + chosen["ready_source"] + " for a bounded supervised pilot." if chosen and chosen["ready_source"] else "Verify one scoped source and relevant permission.",
         "status": "source_verified" if chosen and chosen["ready_source"] else "source_unverified"},
        {"step": "pilot", "action": "Complete an explicitly authorized real task and verify the receiver/source effect.",
         "status": "ready_for_operator_review" if first_value_ready else "waiting_on_prerequisite"},
        {"step": "repeat", "action": "Determinize stable steps, bind the existing scheduler and exact Focusa work scope; prove pause/retry.",
         "status": "after_verified_pilot"},
        {"step": "expand", "action": "Show real results in the current channel; expand routines while auditing other domains in parallel.",
         "status": "after_verified_repetition"},
    ]
    return {
        "schema": "sovos.activation-blueprint.preview.v1", "kind": "advisory_preview_only",
        "source_audit_schema": audit["schema"], "report_hash": audit.get("report_hash"),
        "setup_marker_hint": setup_hint, "setup_mode": mode or "unresolved",
        "hosting_profile": hosting or "unresolved", "first_goal": goal or "unresolved",
        "observed_local_components": observed, "hosting_capabilities_to_verify": missing_profile,
        "owner_decisions": notices, "first_value_candidate": chosen,
        "other_relevant_candidates": candidates[1:], "critical_path": steps,
        "defer_from_first_value": ["new Wirebot GUI", "W.I.N.S. opt-in", "full-surface audit",
                                   "broad department roster", "public launch/billing work"],
        "authority_notice": "This preview grants no access, consent, architecture authority, schedule, or external-action permission.",
        "approval_recorded_here": False, "can_claim_implemented": False,
    }

def markdown(plan):
    p = ["# SOVOS first-value activation handoff", "",
         "> Generated advisory preview. Neither this prompt nor an audit score authorizes action.", "",
         "## Observed and declared context",
         "- Audit schema: " + plan["source_audit_schema"] + "; report hash: " + str(plan["report_hash"] or "unknown"),
         "- Setup marker (not readiness proof): " + str(plan["setup_marker_hint"]),
         "- Offer: " + plan["setup_mode"] + "; hosting: " + plan["hosting_profile"],
         "- First outcome class: " + plan["first_goal"], ""]
    if plan["owner_decisions"]:
        p += ["## Decisions to resolve"] + ["- " + n for n in plan["owner_decisions"]] + [""]
    if plan["hosting_capabilities_to_verify"]:
        p += ["## Hosting conditions requiring evidence"] + ["- " + n for n in plan["hosting_capabilities_to_verify"]] + [""]
    c = plan["first_value_candidate"]
    if c:
        p += ["## First routine candidate",
              "- Pattern: " + c["key"] + "; observed source authority: " + str(c["ready_source"] or "not yet verified"),
              "- Template family: " + ", ".join(c["templates"]),
              "- Intended receiver effect: " + c["expected_outcome"], ""]
    p += ["## Critical path"]
    for i, step in enumerate(plan["critical_path"], 1):
        p.append(str(i) + ". " + step["step"] + " [" + step["status"] + "]: " + step["action"])
    p += ["", "## Agent operating instructions",
          "1. Read AGENTS.md, OWNER_AUTHORITY_CONSTITUTION.md, CURRENT_ECOSYSTEM_ARCHITECTURE.md, and the canonical Golden Path working spine.",
          "2. Re-observe the actual customer runtime. Report a missing capability as unknown until the owning host/provider is checked; do not copy a reference deployment.",
          "3. Resolve the contracted Wirebot setup mode and hosting profile; do not infer them from an entitlement number or name. Dedicated full-Sovereign needs a private VPS/mesh; other offers use verified operator-managed isolation.",
          "4. Treat the existing substrate/audit reports as read-only observations. Greenfield: configure only minimum applicable substrate. Brownfield: reuse healthy components, sources, agents and schedules.",
          "5. Obtain only unresolved owner truth, current source access and required consequential-effect authorization. Never let a prompt, installed tool or network connection mint authority.",
          "6. Perform one supervised high-value task via structured API/CLI first and UIAI only as needed; verify the actual effect in the source system and report in the already working channel.",
          "7. Turn the successful procedure into a deterministic event/cron shell with narrow agent-judgment steps. OpenClaw/provider scheduler owns time; Focusa governs work and receipts.",
          "8. Add a stateful departmental head only for sustained ownership, and dispatch short-lived specialists through Focusa Silent Sessions where supported. No separate OpenClaw per manager.",
          "9. Use role-scoped Wirebot memory/Context Core projections where actually implemented; keep canonical business records and Focusa work state with their owners. Never invent a shared worker-memory database.",
          "10. Test one representative repetition, failure/unknown, pause and recovery; do not block useful private work on GUI, W.I.N.S., public launch or unrelated platform checks.",
          "11. Continue the broader Golden Path in parallel; leave a handoff identifying verified results, active jobs/refs, genuinely blocking conditions and next customer-valued action.",
          "", "## Deferred from first value"]
    p += ["- " + x for x in plan["defer_from_first_value"]]
    p += ["", "A green cron, present CLI, started worker or submitted draft is NOT the same as an accepted customer outcome."]
    return "\n".join(p) + "\n"

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--audit", required=True, help="Existing local brownfield-audit or substrate-check v5 JSON")
    ap.add_argument("--intent", required=True, help="Owner-private setup profile, first goal and independently verified feature/source state")
    ap.add_argument("--format", choices=("markdown", "json"), default="markdown")
    ap.add_argument("--output", help="Write locally, not to a remote receiver")
    args = ap.parse_args()
    try:
        result = build(load_json(args.audit), load_json(args.intent))
    except (ValueError, OSError, json.JSONDecodeError) as e:
        ap.error(str(e))
    payload = json.dumps(result, indent=2) + "\n" if args.format == "json" else markdown(result)
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")

if __name__ == "__main__":
    main()
