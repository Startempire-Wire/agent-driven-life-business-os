#!/usr/bin/env python3
"""Non-destructive regression: existing substrate --output must yield valid private v5 JSON."""
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "substrate-bootstrap.sh"

def invoke(*args):
    # Executes discovery only (never --apply or --install). Missing components
    # normally produce exit 1; a healthy host may exit 0.
    return subprocess.run(
        ["/bin/bash", str(SCRIPT), *map(str, args)],
        text=True, capture_output=True, check=False, timeout=70,
        env={**os.environ, "UIAI_ENGINE_URL": "http://127.0.0.1:1",
             "OPENCLAW_GATEWAY_URL": "http://127.0.0.1:1"},
    )

def check():
    with tempfile.TemporaryDirectory(prefix="wirebot-audit-regression-") as directory:
        target = Path(directory) / "substrate.json"
        first = invoke("--check", "--json", "--output", target)
        assert first.returncode in (0, 1, 3), (first.returncode, first.stderr)
        assert target.is_file(), "--output silently omitted the report"
        record = json.loads(target.read_text(encoding="utf-8"))
        assert json.loads(first.stdout) == record, "disk report differs from stdout"
        assert record["schema"] == "agent-os-substrate-check.v5"
        assert isinstance(record["components"], list)
        assert isinstance(record["install_plan"], list)
        if os.name != "nt":
            assert stat.S_IMODE(target.stat().st_mode) == 0o600, "report is not owner-private"
        again = invoke("--check", "--json", "--output", target)
        assert again.returncode in (0, 1, 3), (again.returncode, again.stderr)
        assert json.loads(target.read_text(encoding="utf-8"))["schema"] == record["schema"]
        unrelated = Path(directory) / "customer-notes.json"
        unrelated.write_text('{"owner_data":"PRESERVE"}', encoding="utf-8")
        refused = invoke("--check", "--json", "--output", unrelated)
        assert refused.returncode == 69
        assert unrelated.read_text(encoding="utf-8") == '{"owner_data":"PRESERVE"}'
        link = Path(directory) / "link.json"
        link.symlink_to(unrelated)
        refused_link = invoke("--check", "--json", "--output", link)
        assert refused_link.returncode == 69
        assert link.is_symlink() and unrelated.read_text(encoding="utf-8") == '{"owner_data":"PRESERVE"}'
        no_mode = invoke("--output", Path(directory) / "should-not-exist.json")
        assert no_mode.returncode == 64
        assert not (Path(directory) / "should-not-exist.json").exists()
    print("substrate-bootstrap-report: PASS")

if __name__ == "__main__":
    check()
