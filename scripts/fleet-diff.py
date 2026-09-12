#!/usr/bin/env python3
"""Compare two agent-os-fleet-audit JSON reports without contacting machines."""
import argparse
import datetime
import json


def machine_index(report):
    return {m.get("hostname", "-"): m for m in report.get("machines", [])}


def score(machine):
    return ((machine.get("report") or {}).get("readiness_score") or {}).get("score")


def blocker_keys(report):
    return {
        (b.get("machine", ""), b.get("component", ""), b.get("reason", ""))
        for b in (report.get("fleet_score") or {}).get("blockers", [])
    }


def compare(previous, current):
    old, new = machine_index(previous), machine_index(current)
    machines = []
    for hostname, machine in new.items():
        prior = old.get(hostname)
        if prior is None:
            machines.append({"hostname": hostname, "change": "new", "status": machine.get("status")})
            continue
        change = {}
        if prior.get("status") != machine.get("status"):
            change["status"] = {"from": prior.get("status"), "to": machine.get("status")}
        if score(prior) != score(machine) and score(machine) is not None:
            change["score"] = {"from": score(prior), "to": score(machine), "delta": score(machine) - (score(prior) or 0)}
        if change:
            machines.append({"hostname": hostname, "change": "changed", **change})
    for hostname, machine in old.items():
        if hostname not in new:
            machines.append({"hostname": hostname, "change": "missing", "was": machine.get("status")})

    old_score = (previous.get("fleet_score") or {}).get("score")
    new_score = (current.get("fleet_score") or {}).get("score")
    old_blockers, new_blockers = blocker_keys(previous), blocker_keys(current)
    return {
        "schema": "agent-os-fleet-diff.v1",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fleet_score": {
            "from": old_score,
            "to": new_score,
            "delta": new_score - old_score if old_score is not None and new_score is not None else None,
        },
        "machines": machines,
        "blockers": {
            "added": [list(item) for item in sorted(new_blockers - old_blockers)],
            "resolved": [list(item) for item in sorted(old_blockers - new_blockers)],
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous", type=argparse.FileType("r"))
    parser.add_argument("current", type=argparse.FileType("r"))
    args = parser.parse_args()
    print(json.dumps(compare(json.load(args.previous), json.load(args.current)), indent=2))


if __name__ == "__main__":
    main()
