#!/usr/bin/env python3
"""Repository-level anti-drift checks for ADLBOS documentation and data."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def assert_contains(rel, phrase):
    if phrase not in read(rel):
        raise AssertionError(f"{rel} missing required text: {phrase!r}")

def check_relative_markdown_links():
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    failures = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in pattern.findall(text):
            target = raw.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append((path.relative_to(ROOT), raw, "escapes repository"))
                continue
            if not resolved.exists():
                failures.append((path.relative_to(ROOT), raw, "missing"))
    if failures:
        detail = "\n".join(f"  {src}: {target} ({why})" for src, target, why in failures)
        raise AssertionError("broken relative Markdown links:\n" + detail)

def check_economics():
    model = json.loads(read("data/adlbos-human-equivalent-cost-model.v1.json"))
    if model["as_of"] != "2026-09-29":
        raise AssertionError("economic model refresh date drifted")
    roles = {r["role"]: r for r in model["role_benchmarks"]}
    low = high = 0
    employee_exact = 0.0
    hours = 0.0
    wage_share = model["methodology"]["bls_full_time_private_wage_share_of_total_compensation"]
    hours_per_fte = model["methodology"]["hours_per_fte_year"]
    for routine in model["representative_routines"]:
        role = roles[routine["role"]]
        annual_hours = routine["hours_per_week"] * model["methodology"]["weeks_per_year"]
        expected_low = round(annual_hours * role["contractor_hourly_low"])
        expected_high = round(annual_hours * role["contractor_hourly_high"])
        wage_hourly = role.get("median_wage_hourly")
        if wage_hourly is None:
            wage_hourly = role["median_wage_annual"] / hours_per_fte
        expected_employee = round(annual_hours * wage_hourly / wage_share)
        if routine["contractor_annual_low"] != expected_low:
            raise AssertionError(f"contractor low drift: {routine['routine']}")
        if routine["contractor_annual_high"] != expected_high:
            raise AssertionError(f"contractor high drift: {routine['routine']}")
        if routine["employee_equivalent_annual"] != expected_employee:
            raise AssertionError(f"employee-equivalent drift: {routine['routine']}")
        low += expected_low
        high += expected_high
        employee_exact += annual_hours * wage_hourly / wage_share
        hours += routine["hours_per_week"]
    total = model["representative_total"]
    if total["contractor_annual_low"] != low or total["contractor_annual_high"] != high:
        raise AssertionError("representative contractor total drift")
    employee = round(employee_exact)
    if total["employee_equivalent_annual"] != employee:
        raise AssertionError("representative employee total drift")
    if abs(total["hours_per_week"] - hours) > 1e-9:
        raise AssertionError("representative weekly-hour total drift")
    canonical = read("docs/ADLBOS_HUMAN_EQUIVALENT_COST_MODEL.md")
    fact = read("docs/ADLBOS_PUBLIC_VALUE_FACT_SHEET.md")
    for value in (f"${low:,}", f"${high:,}", f"${total['employee_equivalent_annual']:,}"):
        if value not in canonical:
            raise AssertionError(f"canonical economics prose missing derived value {value}")
        if value not in fact:
            raise AssertionError(f"public fact sheet missing derived value {value}")

def main():
    assert_contains("AGENT_OS_GOLDEN_PATH.md", "Golden Path target:** `0.2.4-candidate`")
    assert_contains("docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md", "targeting `0.2.4-candidate`")
    assert_contains("docs/agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md", "0.2.4-candidate")
    memory = read("PORTABLE_MEMORY_REFERENCE_PROFILE.md")
    if "**Status:** LIVE" in memory:
        raise AssertionError("portable memory must not be labeled LIVE while incubating")
    if "**Status:** INCUBATING" not in memory:
        raise AssertionError("portable memory maturity is not explicit")
    for rel in (
        "docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md",
        "docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md",
    ):
        if not (ROOT / rel).is_file():
            raise AssertionError(f"compatibility-protected path missing: {rel}")
    current_files = (
        "README.md",
        "AGENTS.md",
        "CURRENT_ECOSYSTEM_ARCHITECTURE.md",
        "AGENT_OS_GOLDEN_PATH.md",
        "docs/agent-os-golden-path/02-agent-os-golden-path-ordered-tasks.md",
        "docs/agent-os-golden-path/09-composable-ai-workforce-catalogue-and-client-assignment-matrix.md",
        "docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md",
        "docs/agent-os-golden-path/13-portfolio-business-compiler-routine-analytics-and-leverage-progression.md",
        "docs/agent-os-golden-path/SERVER_AGENT_HANDOFF.md",
        "PORTABLE_MEMORY_REFERENCE_PROFILE.md",
    )
    forbidden = (
        "W.I.N.S. accepted outcomes",
        "W.I.N.S. owns accepted-outcome",
        "W.I.N.S. records accepted outcomes",
        "accepted-outcome / correction / economics defect -> W.I.N.S.",
        "Evidence → settlement → W.I.N.S.",
        "Performance/W.I.N.S.: accepted outcomes",
    )
    for rel in current_files:
        text = read(rel)
        for phrase in forbidden:
            if phrase in text:
                raise AssertionError(f"{rel} restores forbidden current ownership phrase: {phrase}")
    assert_contains("CURRENT_ECOSYSTEM_ARCHITECTURE.md", "W.I.N.S.-off is a complete valid operating state")
    assert_contains("docs/economics/01-human-equivalent-cost-and-leverage-benchmark.md", "SUPERSEDED compatibility path")
    assert_contains("docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md", "source-domain accepted life/business outcome")
    assert_contains("docs/agent-os-golden-path/10-wirebot-application-family-startempire-wire-integration-architecture.md", "optional W.I.N.S. progression / recognition / community projection")
    assert_contains("PORTABLE_MEMORY_REFERENCE_PROFILE.md", "owning source business/life domain + owner acceptance")
    model = json.loads(read("data/adlbos-human-equivalent-cost-model.v1.json"))
    if "https://www.bls.gov/ooh/sales/insurance-sales-agents.htm" not in model["sources"]:
        raise AssertionError("sales-services benchmark is missing direct BLS source provenance")
    assert_contains("docs/REPOSITORY_INTEGRITY.md", "Compatibility-protected paths")
    check_relative_markdown_links()
    check_economics()
    print("repository integrity: PASS")

if __name__ == "__main__":
    main()
