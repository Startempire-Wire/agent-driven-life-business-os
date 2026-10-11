#!/usr/bin/env python3
"""SOVOS commercial work contract: reusable lifecycle and isolated private-binding guards."""
import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))
def fail_if_valid(validator, value, label):
    if not list(validator.iter_errors(value)):
        raise AssertionError(label + " unexpectedly validated")

def main():
    schema = load("contracts/operator-commercial-work.v1.schema.json")
    binding_schema = load("contracts/operator-commercial-work-binding.v1.schema.json")
    Draft202012Validator.check_schema(schema)
    Draft202012Validator.check_schema(binding_schema)
    validator = Draft202012Validator(schema)
    bv = Draft202012Validator(binding_schema)
    profile = load("commercial-work/revenue-engine.v1.json")
    pack = load("routine-packs/business-revenue-engine.json")
    wirebot = load("tests/fixtures/operator-commercial-work-binding.wirebot.valid.json")
    services = load("tests/fixtures/operator-commercial-work-binding.services.valid.json")
    validator.validate(profile)
    bv.validate(wirebot)
    bv.validate(services)

    routine_template_schema = Draft202012Validator(load("contracts/operator-routine-template.v1.schema.json"))
    pack_schema = Draft202012Validator(load("contracts/operator-routine-pack.v1.schema.json"))
    pack_schema.validate(pack)
    available = set()
    for path in sorted((ROOT / "routine-templates").glob("*.json")):
        tpl = json.loads(path.read_text(encoding="utf-8"))
        routine_template_schema.validate(tpl)  # v1 remains unchanged
        available.add(tpl["template_id"] + "@" + tpl["template_version"])
    for ref in pack["template_refs"] + profile["routine_template_refs"]:
        if ref not in available:
            raise AssertionError("missing canonical routine template " + ref)
    if set(pack["template_refs"]) != set(profile["routine_template_refs"]):
        raise AssertionError("revenue pack and commercial profile template refs diverged")
    if profile["routine_pack_ref"] != pack["pack_id"] + "@" + pack["pack_version"]:
        raise AssertionError("profile does not reference canonical pack version")

    workforce_doc = (ROOT / "docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md").read_text(encoding="utf-8")
    catalog_roles = [profile["workforce"]["chief_of_staff_role_ref"], *profile["workforce"]["specialist_role_refs"]]
    pack_refs = set(profile["workforce"]["task_pack_refs"])
    for stage in profile["stages"]:
        pack_refs.update(stage["task_pack_refs"])
        if not set(stage["routine_template_refs"]) <= available:
            raise AssertionError("stage points to unknown routine")
        if not set(stage["task_pack_refs"]) <= set(profile["workforce"]["task_pack_refs"]):
            raise AssertionError("stage task pack missing from profile workforce set")
    for code in catalog_roles + sorted(pack_refs):
        if "| " + code + " |" not in workforce_doc:
            raise AssertionError("workforce catalogue role/task-pack not found: " + code)

    stages = [item["stage_key"] for item in profile["stages"]]
    expected = [
        "discover", "qualify", "admit_to_crm", "prepare_outreach", "engage",
        "triage_reply", "advance_opportunity", "prepare_offer", "accept_commitment",
        "reconcile_settled_cash", "verify_customer_value", "retain_expand_refer"
    ]
    if stages != expected or len(stages) != len(set(stages)):
        raise AssertionError("commercial causal stage order drifted")

    # This is two owners/CRMs and two industry shapes, with independent scopes.
    if wirebot["scope"]["owner_ref"] == services["scope"]["owner_ref"]:
        raise AssertionError("customer scopes were merged")
    if wirebot["profile_ref"] != services["profile_ref"]:
        raise AssertionError("not actually using one portable profile")
    if len([x for x in wirebot["source_bindings"] if x["source_class"] == "relationship_crm"]) != 1:
        raise AssertionError("Wirebot relationship-CRM source missing")
    if "hubspot" in json.dumps(profile).lower() or "hubspot" in json.dumps(pack).lower():
        raise AssertionError("provider-specific CRM leaked into portable contract")
    if any(x["access_state"] != "unverified" for x in wirebot["source_bindings"]):
        raise AssertionError("ChatGPT account access was silently promoted to Wirebot authorization")

    # Negative proofs: portable law cannot assert authority or payment settlement.
    incorrect = copy.deepcopy(profile)
    incorrect["authority_law"]["outbound_requires_scoped_grant"] = False
    fail_if_valid(validator, incorrect, "outbound without grant")
    incorrect = copy.deepcopy(profile)
    incorrect["outcome_law"]["crm_closed_won_is_settled_cash"] = True
    fail_if_valid(validator, incorrect, "CRM stage masquerades as cash")
    incorrect = copy.deepcopy(profile)
    incorrect["source_truth"]["cross_portal_merging_default"] = True
    fail_if_valid(validator, incorrect, "cross portal merging")
    incorrect = copy.deepcopy(profile)
    incorrect["privacy"]["contains_private_payload"] = True
    fail_if_valid(validator, incorrect, "portable private payload")
    incorrect = copy.deepcopy(profile)
    incorrect["stages"][0]["stage_key"] = "unbounded_bulk_send"
    fail_if_valid(validator, incorrect, "unknown stage")

    invalid_binding = copy.deepcopy(wirebot)
    invalid_binding["password"] = "prohibited"
    fail_if_valid(bv, invalid_binding, "embedded credential payload")
    invalid_binding = copy.deepcopy(wirebot)
    invalid_binding["status"] = "active"
    fail_if_valid(bv, invalid_binding, "activated without assignment, runtime, grants, evidence")

    # Even after unrelated active prerequisites are bound, a dedicated
    # sovereign installation still requires a real environment reference.
    active = copy.deepcopy(wirebot)
    active["status"] = "active"
    active["supervision"]["focusa_assignment_ref"] = "focusa://example/assignment"
    active["supervision"]["focusa_workstream_ref"] = "focusa://example/workstream"
    active["automation"].update(state="active", routine_instance_refs=["routine://example/1"],
                                scheduler_binding_refs=["openclaw://example/job"])
    active["verification"]["first_value_evidence_ref"] = "evidence://example/verified"
    active["governance"]["crm_write_grant_refs"] = ["grant://example/crm"]
    for source in active["source_bindings"]:
        if source["source_class"] == "primary_crm":
            source["access_state"] = "write_verified"
        if source["source_class"] == "payment":
            source["access_state"] = "read_verified"
    fail_if_valid(bv, active, "full sovereign active without operator environment")
    active["product_routes"][0]["environment_ref"] = "operator-environment://example/owner"
    bv.validate(active)

    # The deployer-facing CLI checks private customer binding conformance
    # without printing the binding's potentially sensitive source data.
    import subprocess
    import sys
    for fixture in ("operator-commercial-work-binding.wirebot.valid.json",
                    "operator-commercial-work-binding.services.valid.json"):
        out = subprocess.run([sys.executable, str(ROOT / "scripts/validate-commercial-work.py"),
                              "--binding", str(ROOT / "tests/fixtures" / fixture), "--json"],
                             capture_output=True, text=True, check=False)
        if out.returncode != 0:
            raise AssertionError("valid commercial binding CLI verification failed")
        result = json.loads(out.stdout)
        if result["grants_reverified"] or result["routine_runtime_verified"]:
            raise AssertionError("static validator claimed runtime proof")

    # A validated profile and a candidate binding are NOT proof that production
    # routing, app connector, outreach or Generalized Routine Compiler is live.
    print("commercial work contracts: PASS")

if __name__ == "__main__":
    main()
