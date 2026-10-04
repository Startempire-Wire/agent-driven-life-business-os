#!/usr/bin/env python3
"""Regression proof for operator.attention_policy.v1."""

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
    schema = load(ROOT / "contracts/operator-attention-policy.v1.schema.json")
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    policy = load(ROOT / "tests/fixtures/operator-attention-policy.valid.json")
    validator.validate(policy)

    secret = copy.deepcopy(policy)
    secret["privacy"]["contains_secret_material"] = True
    invalid(validator, secret, "attention policy carrying secret material")

    private_payload = copy.deepcopy(policy)
    private_payload["privacy"]["contains_private_payload"] = True
    invalid(validator, private_payload, "attention policy carrying private payload")

    no_channels = copy.deepcopy(policy)
    no_channels["delivery"]["channel_refs"] = []
    invalid(validator, no_channels, "attention policy without delivery channel")

    reply_without_revalidation = copy.deepcopy(policy)
    reply_without_revalidation["replies"]["source_revalidation_required"] = False
    invalid(validator, reply_without_revalidation, "reply policy without source revalidation")

    disabled_reply = copy.deepcopy(policy)
    disabled_reply["replies"]["allowed"] = False
    disabled_reply["replies"]["free_text_allowed"] = True
    invalid(validator, disabled_reply, "disabled reply policy that still accepts free text")

    bad_quiet_hours = copy.deepcopy(policy)
    bad_quiet_hours["quiet_hours"]["start_local"] = None
    invalid(validator, bad_quiet_hours, "enabled quiet-hours policy without start time")

    print("attention policy contract: PASS")


if __name__ == "__main__":
    main()
