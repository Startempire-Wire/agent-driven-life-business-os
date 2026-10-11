#!/usr/bin/env python3
"""Read-only validation of a private SOVOS commercial-work binding (no provider calls)."""
import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError, SchemaError

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def check(profile, binding):
    p_schema = load(ROOT / "contracts/operator-commercial-work.v1.schema.json")
    b_schema = load(ROOT / "contracts/operator-commercial-work-binding.v1.schema.json")
    Draft202012Validator.check_schema(p_schema)
    Draft202012Validator.check_schema(b_schema)
    Draft202012Validator(p_schema).validate(profile)
    Draft202012Validator(b_schema).validate(binding)
    expected = profile["profile_id"] + "@" + profile["profile_version"]
    if binding["profile_ref"] != expected:
        raise ValueError("binding profile ref does not match the inspected contract version")

    sources = binding["source_bindings"]
    for cls in ("primary_crm", "payment"):
        if sum(s["source_class"] == cls for s in sources) != 1:
            raise ValueError("exactly one " + cls + " source required in a business binding")
    crm = [s["source_ref"] for s in sources if s["source_class"] in ("primary_crm", "relationship_crm")]
    if len(crm) != len(set(crm)):
        raise ValueError("the same CRM may not be disguised as two different source accounts")

    # Refs are opaque but must not accidentally become credentials, emails,
    # raw records or pasted URLs with query secrets. Do not echo rejected values.
    ref_values = [binding["scope"]["owner_ref"], binding["scope"]["business_ref"],
                  binding["supervision"]["chief_of_staff_ref"]]
    for s in sources:
        ref_values.extend([s["source_ref"], *s["credential_use_refs"]])
    for x in binding["product_routes"]:
        ref_values.extend([x["offer_ref"], x["terms_policy_ref"], x["readiness_ref"]])
        if x["environment_ref"]:
            ref_values.append(x["environment_ref"])
    for x in ref_values:
        lower = x.lower()
        if "://" not in x or "@" in x or any(z in lower for z in (
                "apikey=", "api_key=", "access_token=", "bearer ", "password=",
                "refresh_token=", "sk-")):
            raise ValueError("binding contains a raw identifier or secret-like ref; use scoped opaque refs")
    if binding["status"] == "active" and binding["automation"]["state"] != "active":
        raise ValueError("active binding has no active existing scheduler projection")

    return {
        "contract_valid": True,
        "profile_ref": expected,
        "binding_status": binding["status"],
        "source_classes": sorted(set(s["source_class"] for s in sources)),
        "offer_routes": len(binding["product_routes"]),
        "provider_access_reverified": False,
        "grants_reverified": False,
        "routine_runtime_verified": False,
        "note": "Static conformance only; source access, live grants, consent, payment and customer outcomes require current owning-provider proof.",
    }

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--binding", required=True, help="Owner-private JSON file matching the versioned binding contract")
    ap.add_argument("--profile", default=str(ROOT / "commercial-work/revenue-engine.v1.json"))
    ap.add_argument("--json", action="store_true", help="Print a privacy-safe JSON summary")
    args = ap.parse_args()
    try:
        report = check(load(args.profile), load(args.binding))
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError, ValidationError, SchemaError):
        # Error text from jsonschema validation can echo private values. Avoid it.
        print("commercial work binding: INVALID (check schema, private refs, and binding revisions)", file=sys.stderr)
        return 1
    except Exception:
        print("commercial work binding: UNVERIFIED (validator error)", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, sort_keys=True, indent=2))
    else:
        print("commercial work binding: VALID STRUCTURE; provider and runtime authority UNVERIFIED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
