#!/usr/bin/env python3
"""Regression coverage for the canonical SOVOS routine template and pack libraries."""

import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    template_schema = load(ROOT / "contracts/operator-routine-template.v1.schema.json")
    pack_schema = load(ROOT / "contracts/operator-routine-pack.v1.schema.json")
    tv = Draft202012Validator(template_schema)
    pv = Draft202012Validator(pack_schema)

    required_families = {
        "orientation",
        "intake_triage",
        "follow_up",
        "follow_through",
        "reconciliation",
        "delivery_review",
        "renewal_expiry",
        "finance_ops",
        "content_distribution",
        "system_health",
        "incident_response",
        "knowledge_freshness",
        "evidence_closure",
        "learning_improvement",
        "workforce_dispatch",
        "planning",
    }

    template_ids = set()
    routine_families = set()
    template_catalog = sorted((ROOT / "routine-templates").glob("*.json"))
    if len(template_catalog) < 18:
        raise AssertionError("starter routine template catalog unexpectedly incomplete")

    for template_path in template_catalog:
        item = load(template_path)
        tv.validate(item)
        template_ids.add(item["template_id"] + "@" + item["template_version"])
        routine_families.add(item["classification"]["routine_family"])

    missing_families = required_families - routine_families
    if missing_families:
        raise AssertionError(
            f"core routine families missing canonical templates: {sorted(missing_families)}"
        )

    required_pack_ids = {
        "routine-pack://life/personal-executive",
        "routine-pack://life/household-family",
        "routine-pack://life/research-creator",
        "routine-pack://life/personal-finance",
        "routine-pack://life/wellness-care",
        "routine-pack://business/professional-services",
        "routine-pack://business/software-saas",
        "routine-pack://business/content-community",
        "routine-pack://business/ecommerce-product",
        "routine-pack://business/local-field-service",
        "routine-pack://business/founder-portfolio",
    }

    pack_ids = set()
    pack_catalog = sorted((ROOT / "routine-packs").glob("*.json"))
    if len(pack_catalog) < 11:
        raise AssertionError("starter routine pack catalog unexpectedly incomplete")

    for pack_path in pack_catalog:
        pack = load(pack_path)
        pv.validate(pack)
        pack_ids.add(pack["pack_id"])
        for ref in pack["template_refs"]:
            if ref not in template_ids:
                raise AssertionError(
                    f"routine pack {pack_path.name} references missing canonical template {ref}"
                )

    missing_packs = required_pack_ids - pack_ids
    if missing_packs:
        raise AssertionError(
            f"starter routine packs missing canonical artifacts: {sorted(missing_packs)}"
        )

    print("routine library coverage: PASS")


if __name__ == "__main__":
    main()
