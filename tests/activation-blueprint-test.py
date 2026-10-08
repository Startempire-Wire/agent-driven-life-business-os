#!/usr/bin/env python3
"""Offline checks for read-only SOVOS activation preview, no network/provider calls."""
import importlib.util
from pathlib import Path

path = Path(__file__).parents[1] / "scripts" / "activation-blueprint.py"
spec = importlib.util.spec_from_file_location("activation_blueprint", path)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

AUDIT = {"schema": "agent-os-brownfield-audit.v5",
         "report_hash": "sha256:test",
         "setup_state": {"state": "agent-OS markers present"},
         "machine_fingerprint": "should-not-leak",
         "components": [{"component": "openclaw", "present": True, "health": "healthy",
                         "resolved_path": "/private/path"}]}

def check():
    managed = {"setup_mode": "wirebot_direct", "hosting_profile": "managed_isolated",
               "first_goal": "revenue",
               "verified_capabilities": {"hosted_runtime": "verified",
                                         "tenant_isolation": "verified",
                                         "operating_partner": "verified", "owner_channel": "verified"},
               "source_access": {"email": "verified"}}
    one = app.build(AUDIT, managed)
    assert one["hosting_capabilities_to_verify"] == []
    assert one["first_value_candidate"]["key"] == "inquiry_followup"
    assert one["critical_path"][4]["status"] == "ready_for_operator_review"
    assert "should-not-leak" not in app.markdown(one)
    assert "/private/path" not in app.markdown(one)
    assert one["approval_recorded_here"] is False

    dedicated = {"setup_mode": "wirebot_sovereign_operator", "hosting_profile": "dedicated_vps",
                 "first_goal": "team", "verified_capabilities": {
                     "operating_partner": "verified", "owner_channel": "verified"},
                 "source_access": {"tasks": "verified"}}
    two = app.build(AUDIT, dedicated)
    assert two["first_value_candidate"]["key"] == "team_dispatch"
    assert set(two["hosting_capabilities_to_verify"]) == {"customer_vps", "private_mesh", "local_body"}
    assert two["critical_path"][4]["status"] == "ready_for_operator_review"
    assert app.build(AUDIT, {})["first_value_candidate"] is None
    not_verified = dict(managed, source_access={"email": "configured"})
    assert app.build(AUDIT, not_verified)["critical_path"][4]["status"] == "waiting_on_prerequisite"
    for invalid in ({"hosting_profile": "shared_without_isolation"}, {"source_access": {"email": "yes"}}):
        try:
            app.build(AUDIT, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid intent must fail")
    print("activation-blueprint: PASS")

if __name__ == "__main__":
    check()
