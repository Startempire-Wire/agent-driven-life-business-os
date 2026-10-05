#!/usr/bin/env python3
"""Regression proof for operator.environment.v1."""

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
    schema = load(ROOT / "contracts/operator-environment.v1.schema.json")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    env = load(ROOT / "tests/fixtures/operator-environment.valid.json")
    validator.validate(env)

    shared = copy.deepcopy(env)
    shared["management"]["shared_runtime_allowed"] = True
    invalid(validator, shared, "shared runtime in SOVOS Operator Environment")

    no_local = copy.deepcopy(env)
    no_local["private_mesh"]["local_body_refs"] = []
    invalid(validator, no_local, "environment without owner-controlled local body")

    wrong_mesh = copy.deepcopy(env)
    wrong_mesh["private_mesh"]["provider"] = "other"
    invalid(validator, wrong_mesh, "environment without required Tailscale mesh")

    not_dedicated = copy.deepcopy(env)
    not_dedicated["persistent_vps"]["dedicated_to_owner"] = False
    invalid(validator, not_dedicated, "environment without dedicated owner VPS")

    no_residency = copy.deepcopy(env)
    no_residency["residency"]["active_body_refs"] = []
    invalid(validator, no_residency, "environment without active partner residency")

    no_coordinator = copy.deepcopy(env)
    del no_coordinator["residency"]["runtime_coordinator_ref"]
    invalid(validator, no_coordinator, "environment without runtime coordinator")

    bad_conflict_policy = copy.deepcopy(env)
    bad_conflict_policy["residency"]["state_conflict_policy"] = "multi_writer"
    invalid(validator, bad_conflict_policy, "environment permitting split-brain state writes")

    secret = copy.deepcopy(env)
    secret["privacy"]["contains_secret_material"] = True
    invalid(validator, secret, "portable environment contract carrying secrets")

    print("operator environment contract: PASS")

if __name__ == "__main__":
    main()
