#!/usr/bin/env python3
"""Regression proof for the Portfolio Operating Compiler portable envelopes."""

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

    no_scope = copy.deepcopy(routine)
    no_scope["scope"]["business_refs"] = []
    no_scope["scope"]["life_domain_refs"] = []
    invalid(rv, no_scope, "routine without business/life scope")

    active_without_assignment = copy.deepcopy(routine)
    active_without_assignment["status"] = "active"
    active_without_assignment["trigger"]["schedule"]["schedule_ref"] = "openclaw://schedule/weekly"
    invalid(rv, active_without_assignment, "active routine without Focusa assignment")

    active_schedule_without_schedule_ref = copy.deepcopy(routine)
    active_schedule_without_schedule_ref["status"] = "active"
    active_schedule_without_schedule_ref["supervision"]["focusa_assignment_ref"] = "focusa://assignment/1"
    invalid(rv, active_schedule_without_schedule_ref, "active scheduled routine without OpenClaw schedule ref")

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

    doc = (ROOT / "docs/agent-os-golden-path/13-portfolio-operating-compiler-leverage-and-momentum.md").read_text(encoding="utf-8")
    for phrase in [
        "Several businesses are normal.",
        "OpenClaw Automations is the default durable scheduler",
        "The game is the owner's real life/business progress.",
        "Observed → Modeled → Pilot → Proven → Automated → Compounding",
        "W.I.N.S. owns accepted-outcome and owner-facing progression semantics.",
    ]:
        if phrase not in doc:
            raise AssertionError(f"portfolio compiler doctrine missing: {phrase}")

    print("portfolio compiler contracts: PASS")

if __name__ == "__main__":
    main()
