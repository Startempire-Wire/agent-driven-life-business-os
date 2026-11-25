#!/usr/bin/env python3
"""Source-owned Stage 1 cold-start and Greenfield bootstrap regression checks.

All executable probes use a PATH with no Python, package manager, or product
installer. They cannot install or modify any customer machine.
"""
from pathlib import Path
import os
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
BOOTSTRAP = ROOT / "scripts" / "substrate-bootstrap.sh"
GOLDEN_PATH = ROOT / "docs" / "agent-os-golden-path" / "02-agent-os-golden-path-ordered-tasks.md"

def probe(*args):
    with tempfile.TemporaryDirectory(prefix="wirebot-bootstrap-cold-start-") as empty_path:
        env = dict(os.environ, PATH=empty_path)
        return subprocess.run(
            ["/bin/bash", str(BOOTSTRAP), *args],
            env=env, text=True, capture_output=True, check=False, timeout=12,
        )

def main():
    stage = GOLDEN_PATH.read_text(encoding="utf-8").split(
        "# Stage 1 — Workstation substrate and secure agent capability", 1
    )[1].split("# Stage 2", 1)[0]
    ordered = (
        "1. Audit OS/platform",
        "2. Install only missing approved base prerequisites",
        "3. Establish the selected model/provider access",
        "4. Establish Pi/reference build-agent access",
        "5. Install/pair Focusa",
        "6. Install/pair UIAI",
    )
    positions = [stage.index(s) for s in ordered]
    assert positions == sorted(positions), "Canonical Stage 1 sequence changed"
    check = probe("--check", "--json")
    assert check.returncode == 68
    assert "Python is missing" in check.stderr
    preview = probe("--apply", "base", "--dry-run")
    assert preview.returncode == 0, (preview.returncode, preview.stderr)
    assert "python3 is missing" in preview.stdout
    assert "no changes made" in preview.stdout
    no_permission = probe("--apply", "base")
    assert no_permission.returncode == 64
    assert "requires --yes or --dry-run" in no_permission.stderr
    # No executable install path is reachable with an empty PATH, and no
    # automatic sudo escalation is attempted with a missing bootstrap manager.
    apply = probe("--apply", "base", "--yes")
    assert apply.returncode == 68
    assert "no supported Python bootstrap manager" in apply.stderr
    for p in (check, preview, no_permission, apply):
        assert "Focusa installation completed" not in p.stdout + p.stderr
    shell_syntax = subprocess.run(
        ["/bin/bash", "-n", str(BOOTSTRAP)],
        capture_output=True, text=True, check=False, timeout=12,
    )
    assert shell_syntax.returncode == 0, shell_syntax.stderr
    print("substrate-bootstrap-python-order: PASS")

if __name__ == "__main__":
    main()
