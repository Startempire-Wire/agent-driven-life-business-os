#!/usr/bin/env python3
"""Offline source-owned SOVOS installer review tests.

The Golden Path preview is never an executable installer or entitlement source.
All cases use synthetic audit v5 rows and do not touch machines or providers.
"""
import importlib.util
from pathlib import Path

module_path = Path(__file__).resolve().parents[1] / "scripts" / "activation-blueprint.py"
spec = importlib.util.spec_from_file_location("sovos_activation_blueprint", module_path)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


def audit(*components):
    return {"schema": "agent-os-brownfield-audit.v5", "components": list(components)}


def review(evidence, expression="proto", hosting="managed_isolated"):
    preview = app.build(evidence, {"marketing_expression": expression, "hosting_profile": hosting})
    assert preview["approval_recorded_here"] is False
    return preview["installation_review"]


def check():
    # A typical first buyer has no Focusa yet. The Golden Path starts with
    # substrate / provider / Pi and acquires Focusa *after* these steps.
    fresh = review(audit(
        {"component": "pi", "present": False},
        {"component": "focusa", "present": False},
        {"component": "uiai", "present": False,
         "runtime": {"state": "endpoint_unreachable", "healthy": False}},
    ))
    assert [c["component"] for c in fresh["components"]] == [
        "pi", "focusa", "focusa_pi_extension", "uiai"]
    assert all(c["decision"] == "unknown" for c in fresh["components"])
    seq = fresh["sequence"]
    assert seq == [
        "inspect_target", "base_prerequisites", "model_provider_access", "pi",
        "focusa", "focusa_pi_extension", "uiai", "higher_expression_delta",
        "verify_first_mission"]
    assert fresh["apply_available"] is False
    assert fresh["authorization_recorded"] is False
    assert fresh["license_issued_verified"] is False
    assert fresh["runtime_ready"] is False
    assert fresh["first_mission_accepted"] is False

    # Brownfield: reuse healthy Focusa and a remote UIAI service, but do not
    # alter an independently owned OpenClaw installation for a Proto buyer.
    existing = review(audit(
        {"component": "pi", "present": True, "health": "n/a"},
        {"component": "focusa", "present": True, "health": "healthy"},
        {"component": "uiai", "present": False,
         "runtime": {"state": "runtime_healthy", "healthy": True}},
        {"component": "openclaw", "present": True, "health": "healthy"},
    ))
    actual = {row["component"]: row["decision"] for row in existing["components"]}
    assert actual == {
        "pi": "unknown", "focusa": "reuse", "focusa_pi_extension": "unknown",
        "uiai": "reuse", "openclaw": "leave_alone"}
    assert existing["network_federation"] == "future_optional_separate_authority"

    # A detected unhealthy service suggests repair, never blind replacement;
    # repeated/conflicting sensor observations must remain unknown.
    partial = review(audit(
        {"component": "focusa", "present": True, "health": "unhealthy"},
        {"component": "focusa", "present": False},
        {"component": "uiai", "present": True, "health": "unhealthy"},
    ))
    actual = {row["component"]: row["decision"] for row in partial["components"]}
    assert actual["focusa"] == "unknown"
    assert actual["uiai"] == "repair"

    # Five model-specific cumulative sets preserve lower-model rights.
    # Only the accepted dedicated hosting profile adds the private-mesh lane.
    sizes = []
    for expression in ("proto", "tempo", "crew", "chief", "sovereign"):
        result = review(audit(), expression)
        sizes.append(len(result["components"]))
        assert result["license_issued_verified"] is False
        assert result["apply_available"] is False
        assert result["first_mission_accepted"] is False
        assert result["network_federation"] == "future_optional_separate_authority"
    assert sizes == sorted(sizes) and len(set(sizes)) == 5
    full = review(audit(), "sovereign", "dedicated_vps")
    assert {"customer_vps", "private_mesh", "local_body"} <= {
        row["component"] for row in full["components"]}
    assert not {"customer_vps", "private_mesh", "local_body"} & {
        row["component"] for row in fresh["components"]}

    for invalid in ("network", "wirebot_network", "Direct", 2, [], None):
        try:
            app.expression_install_review(audit(), invalid, "managed_isolated")
        except ValueError:
            pass
        else:
            raise AssertionError("invalid Expression accepted")
    for invalid in ("network", 4, [], {}):
        try:
            app.expression_install_review(audit(), "proto", invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid hosting accepted")
    malformed = review(audit({"component": [], "present": True}))
    assert malformed["components"][0]["observed_state"] == "not_observed"
    assert all(row["proposed_only"] and not row["apply_operation_bound"]
               for row in malformed["components"])
    print("wirebot-expression-install-review: PASS")


if __name__ == "__main__":
    check()
