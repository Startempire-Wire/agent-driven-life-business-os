#!/usr/bin/env python3
"""Regression proof for the Portfolio Business Compiler portable envelopes."""

import copy
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def invalid(validator, value, label):
    if not list(validator.iter_errors(value)):
        raise AssertionError(f"{label} unexpectedly validated")

def main():
    routine_schema = load(ROOT / "contracts/operator-routine-blueprint.v1.schema.json")
    leverage_schema = load(ROOT / "contracts/operator-leverage-snapshot.v1.schema.json")
    Draft202012Validator.check_schema(routine_schema)
    Draft202012Validator.check_schema(leverage_schema)
    rv = Draft202012Validator(routine_schema)
    lv = Draft202012Validator(leverage_schema)

    routine = load(ROOT / "tests/fixtures/operator-routine-blueprint.valid.json")
    leverage = load(ROOT / "tests/fixtures/operator-leverage-snapshot.valid.json")
    rv.validate(routine)
    lv.validate(leverage)

    # The base optimization loop must validate with no W.I.N.S. dependency.
    serialized_base = json.dumps(leverage)
    if "wins://" in serialized_base.lower() or "game_projection" in leverage:
        raise AssertionError("base leverage fixture unexpectedly depends on W.I.N.S.")

    wins_projection = copy.deepcopy(leverage)
    wins_projection["game_projection"] = {
        "season_ref": "wins://season/q3",
        "milestone_refs": ["wins://milestone/proven-routine"],
        "routine_maturity": "proven",
    }
    lv.validate(wins_projection)

    no_scope = copy.deepcopy(routine)
    no_scope["scope"]["business_refs"] = []
    no_scope["scope"]["life_domain_refs"] = []
    invalid(rv, no_scope, "routine without business/life scope")

    active_without_assignment = copy.deepcopy(routine)
    active_without_assignment["status"] = "active"
    active_without_assignment["trigger"]["schedule"]["schedule_ref"] = "openclaw://automation/weekly"
    invalid(rv, active_without_assignment, "active routine without Focusa assignment")

    active_schedule_without_schedule_ref = copy.deepcopy(routine)
    active_schedule_without_schedule_ref["status"] = "active"
    active_schedule_without_schedule_ref["supervision"]["focusa_assignment_ref"] = "focusa://assignment/1"
    invalid(rv, active_schedule_without_schedule_ref, "active scheduled routine without scheduler ref")

    # OpenClaw is the default, not the only permitted owner.
    provider_schedule = copy.deepcopy(routine)
    provider_schedule["trigger"]["schedule"]["scheduler_class"] = "provider_scheduler"
    provider_schedule["trigger"]["schedule"]["scheduler_owner_ref"] = "provider://crm/scheduler"
    rv.validate(provider_schedule)

    secret = copy.deepcopy(routine)
    secret["privacy"]["contains_secret_material"] = True
    invalid(rv, secret, "routine carrying secret material")

    no_scope2 = copy.deepcopy(leverage)
    no_scope2["scope"]["business_refs"] = []
    no_scope2["scope"]["life_domain_refs"] = []
    no_scope2["scope"]["routine_refs"] = []
    invalid(lv, no_scope2, "leverage snapshot without scope")

    no_momentum = copy.deepcopy(leverage)
    no_momentum["momentum"]["evidence_refs"] = []
    invalid(lv, no_momentum, "momentum without evidence")

    private_payload = copy.deepcopy(leverage)
    private_payload["privacy"]["contains_private_payload"] = True
    invalid(lv, private_payload, "portable leverage snapshot containing private payload")

    cost_without_currency = copy.deepcopy(leverage)
    del cost_without_currency["operational_metrics"]["currency"]
    invalid(lv, cost_without_currency, "direct cost without currency")

    doc = (ROOT / "docs/agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md").read_text(encoding="utf-8")
    for phrase in [
        "Several businesses are normal.",
        "OpenClaw's built-in Gateway automations scheduler is the default",
        "Momentum is sustained verified progress",
        "Leverage means one change increases future capacity.",
        "W.I.N.S. is an optional setup-aware progression/recognition/community projection.",
        "W.I.N.S.=off",
    ]:
        if phrase not in doc:
            raise AssertionError(f"portfolio compiler doctrine missing: {phrase}")

    print("portfolio compiler contracts: PASS")

if __name__ == "__main__":
    main()
