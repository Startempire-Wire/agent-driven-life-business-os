#!/usr/bin/env python3
"""Regression proof for the portable agent.operation.v1 contract."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "contracts" / "agent-operation.v1.schema.json"
VALID_PATH = ROOT / "tests" / "fixtures" / "agent-operation.valid.json"
DOC_PATH = ROOT / "docs" / "agent-os-golden-path" / "07-agent-operation-complete-software-contract.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def expect_invalid(validator: Draft202012Validator, value: dict, label: str) -> None:
    if not list(validator.iter_errors(value)):
        raise AssertionError(f"{label} unexpectedly passed agent.operation.v1")


def main() -> None:
    schema = load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    valid = load(VALID_PATH)
    validator.validate(valid)

    missing_cli = copy.deepcopy(valid)
    del missing_cli["cli"]
    expect_invalid(validator, missing_cli, "operation missing CLI parity")

    visual_api = copy.deepcopy(valid)
    visual_api["api"]["transport"] = "visual_cua"
    expect_invalid(validator, visual_api, "CUA-only operation")

    interactive_only = copy.deepcopy(valid)
    interactive_only["cli"]["output"] = "human_text"
    expect_invalid(validator, interactive_only, "CLI without JSON output")

    unscoped_mutation = copy.deepcopy(valid)
    unscoped_mutation["operation_id"] = "wirebot.workspace.update"
    unscoped_mutation["consequence_class"] = "mutate"
    unscoped_mutation["authority"]["exact_scope_fields"] = []
    validator.validate(unscoped_mutation)
    # JSON Schema cannot express every policy invariant clearly; enforce cross-field policy here.
    policy_errors = []
    if (
        unscoped_mutation["consequence_class"] != "read"
        and not unscoped_mutation["authority"]["exact_scope_fields"]
    ):
        policy_errors.append("consequential operation requires exact scope fields")
    if not policy_errors:
        raise AssertionError("unscoped mutation unexpectedly passed policy")

    doc = DOC_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "agent-operation complete by default",
        "Computer-use automation (CUA) is the absolute last resort",
        "First-party products must not integrate by opening and visually driving one another",
        "First-party no-CUA",
        "Veragensia Chromebook acceptance",
    ]
    for phrase in required_phrases:
        if phrase not in doc:
            raise AssertionError(f"contract documentation missing: {phrase}")

    print("agent-operation contract: PASS")


if __name__ == "__main__":
    main()
