#!/usr/bin/env python3
"""Regression proof for agent.contract_change.v1 and its protected evolution policy."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "contracts" / "agent-contract-change.v1.schema.json"
VALID_PATH = ROOT / "tests" / "fixtures" / "agent-contract-change.valid.json"
PROFILE_PATH = ROOT / "AGENT_CONTRACT_OPTIMIZATION_PROFILE.md"


PROTECTED_CLASSES = {"constitutional", "safety_authority", "architecture_boundary"}
POST_TEST_STATUSES = {"regression_tested", "approved", "rolled_out", "verified"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def policy_errors(value: dict) -> list[str]:
    errors: list[str] = []

    target_class = value["target"]["evolution_class"]
    change = value["change"]
    authority = value["authority"]
    evaluation = value["evaluation"]
    status = value["status"]
    observations = value["observations"]

    independent = {o["correlation_key"] for o in observations}
    harmful_or_superseded = {
        o["correlation_key"]
        for o in observations
        if o["observation_class"] in {"harm", "superseded"}
    }

    if target_class in PROTECTED_CLASSES and authority["requirement"] == "none":
        errors.append("protected evolution class requires owner-rooted authority")

    if change["kind"] == "remove" or change["semantic_weakening"]:
        if not change.get("supersedes_ref") and len(harmful_or_superseded) < 2:
            errors.append(
                "removal/weakening requires explicit supersession or two independent harm/superseded causes"
            )
        if len(independent) < 2 and not change.get("supersedes_ref"):
            errors.append("removal/weakening cannot rely on duplicate observations of one incident")

    if status in POST_TEST_STATUSES:
        if not evaluation["holdout_case_refs"]:
            errors.append("post-test state requires held-out cases")
        if not evaluation["protected_invariant_refs"]:
            errors.append("post-test state requires protected-invariant cases")
        if evaluation["verdict"] not in {"pass", "tradeoff_approved"}:
            errors.append("post-test state requires a passing/approved evaluation verdict")

    if (
        status in {"approved", "rolled_out", "verified"}
        and authority["requirement"] != "none"
        and not authority.get("approval_ref")
    ):
        errors.append("approved/active protected change requires an approval reference")

    if status in {"rolled_out", "verified"} and not value["rollout"].get("rollback_ref"):
        errors.append("rolled-out change requires a rollback reference")

    if status == "verified" and not value["rollout"].get("post_rollout_observation_ref"):
        errors.append("verified change requires post-rollout observation")

    derived = set(evaluation["derived_case_refs"])
    holdout = set(evaluation["holdout_case_refs"])
    if derived & holdout:
        errors.append("derived cases cannot also claim independent holdout status")

    if value["privacy"]["contains_private_payload"]:
        errors.append("portable proposal must not contain private payload")
    if value["privacy"]["contains_secret_material"]:
        errors.append("portable proposal must not contain secret material")

    return errors


def expect_policy_invalid(value: dict, label: str) -> None:
    if not policy_errors(value):
        raise AssertionError(f"{label} unexpectedly passed agent-contract evolution policy")


def main() -> None:
    schema = load(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    valid = load(VALID_PATH)
    validator.validate(valid)
    if policy_errors(valid):
        raise AssertionError(f"valid fixture failed policy: {policy_errors(valid)}")

    ungrounded_remove = copy.deepcopy(valid)
    ungrounded_remove["status"] = "proposed"
    ungrounded_remove["change"]["kind"] = "remove"
    ungrounded_remove["change"]["semantic_weakening"] = True
    ungrounded_remove["observations"] = [
        {
            **ungrounded_remove["observations"][0],
            "observation_class": "non_compliance",
        }
    ]
    ungrounded_remove["evaluation"]["holdout_case_refs"] = []
    ungrounded_remove["evaluation"]["protected_invariant_refs"] = []
    ungrounded_remove["evaluation"]["verdict"] = "not_run"
    validator.validate(ungrounded_remove)
    expect_policy_invalid(ungrounded_remove, "ungrounded removal")

    duplicate_incident_remove = copy.deepcopy(ungrounded_remove)
    duplicate_incident_remove["observations"] = [
        {
            **valid["observations"][0],
            "observation_class": "harm",
            "correlation_key": "same-incident",
        },
        {
            **valid["observations"][1],
            "observation_class": "harm",
            "correlation_key": "same-incident",
        },
    ]
    expect_policy_invalid(duplicate_incident_remove, "duplicate-incident removal")

    protected_without_authority = copy.deepcopy(valid)
    protected_without_authority["target"]["evolution_class"] = "safety_authority"
    # The JSON Schema itself must reject this, before policy code.
    if not list(validator.iter_errors(protected_without_authority)):
        raise AssertionError("protected change without authority unexpectedly passed schema")

    trained_on_holdout = copy.deepcopy(valid)
    trained_on_holdout["evaluation"]["derived_case_refs"] = ["case://same"]
    trained_on_holdout["evaluation"]["holdout_case_refs"] = ["case://same"]
    expect_policy_invalid(trained_on_holdout, "derived/holdout overlap")

    untested_verified = copy.deepcopy(valid)
    untested_verified["status"] = "verified"
    untested_verified["evaluation"]["holdout_case_refs"] = []
    if not list(validator.iter_errors(untested_verified)):
        raise AssertionError("verified change without holdout unexpectedly passed schema")

    protected_approved_without_ref = copy.deepcopy(valid)
    protected_approved_without_ref["status"] = "approved"
    protected_approved_without_ref["target"]["evolution_class"] = "safety_authority"
    protected_approved_without_ref["authority"]["requirement"] = "owner"
    protected_approved_without_ref["authority"]["approval_ref"] = None
    if not list(validator.iter_errors(protected_approved_without_ref)):
        raise AssertionError("approved protected change without approval ref unexpectedly passed schema")

    rolled_out_without_rollback = copy.deepcopy(valid)
    rolled_out_without_rollback["status"] = "rolled_out"
    rolled_out_without_rollback["rollout"]["rollback_ref"] = None
    if not list(validator.iter_errors(rolled_out_without_rollback)):
        raise AssertionError("rolled-out change without rollback unexpectedly passed schema")

    verified_without_observation = copy.deepcopy(valid)
    verified_without_observation["status"] = "verified"
    verified_without_observation["rollout"]["post_rollout_observation_ref"] = None
    if not list(validator.iter_errors(verified_without_observation)):
        raise AssertionError("verified change without post-rollout observation unexpectedly passed schema")

    private_payload = copy.deepcopy(valid)
    private_payload["privacy"]["contains_private_payload"] = True
    if not list(validator.iter_errors(private_payload)):
        raise AssertionError("portable private payload unexpectedly passed schema")

    profile = PROFILE_PATH.read_text(encoding="utf-8")
    required_phrases = [
        "Operational history may propose a contract change.",
        "Corroboration is about independence, not raw session count",
        "The evidence used to propose a change is training evidence. It is not sufficient validation.",
        "Conversation is provenance/audit, not automatic memory or policy promotion.",
        "prefer semantic-preserving extraction or relocation over deletion",
    ]
    for phrase in required_phrases:
        if phrase not in profile:
            raise AssertionError(f"optimization profile missing invariant: {phrase}")

    print("agent-contract optimization: PASS")


if __name__ == "__main__":
    main()
