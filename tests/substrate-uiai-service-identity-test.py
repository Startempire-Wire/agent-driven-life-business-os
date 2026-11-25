#!/usr/bin/env python3
"""Golden Path audited UIAI reuse must verify the owning service, not HTTP 200."""
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "substrate-bootstrap.sh"


def probe(body, expected):
    with tempfile.TemporaryDirectory(prefix="sovos-uiai-identity-") as td:
        base = Path(td)
        bindir = base / "bin"
        bindir.mkdir()
        curl = bindir / "curl"
        # The subprocess's curl is intentionally isolated: zero real UIAI
        # access, no installs, no customer state; all other tools are host OS.
        curl.write_text('#!/bin/sh\nprintf "%s" "$SOVOS_FAKE_HEALTH"\n', encoding="utf-8")
        curl.chmod(0o755)
        env = {
            **os.environ, "PATH": str(bindir) + os.pathsep + os.environ.get("PATH", ""),
            "HOME": str(base),
            "SOVOS_FAKE_HEALTH": body,
            "UIAI_ENGINE_URL": "http://127.0.0.1:1",
            "OPENCLAW_GATEWAY_URL": "http://127.0.0.1:2",
        }
        p = subprocess.run(
            ["/bin/bash", str(SCRIPT), "--check", "--json"],
            env=env, text=True, capture_output=True, timeout=70, check=False,
        )
        assert p.returncode in (0, 1, 3), (p.returncode, p.stderr)
        report = json.loads(p.stdout)
        row = next(x for x in report["components"] if x["component"] == "uiai")
        assert row["runtime"]["state"] == expected, row
        assert row["runtime"]["healthy"] is (expected == "runtime_healthy")
        if expected == "runtime_healthy":
            assert all(p["component"] != "uiai" for p in report["install_plan"]), \
                "healthy remote UIAI must not trigger a duplicate installation"


def main():
    probe('{"status":"healthy","service":"uiai-engine","browserless":true}', "runtime_healthy")
    probe('{"status":"healthy","service":"another-app"}', "endpoint_unreachable")
    probe('{"status":"unhealthy","service":"uiai-engine"}', "endpoint_unreachable")
    probe("<html>200 OK but not a UIAI engine</html>", "endpoint_unreachable")
    print("substrate-uiai-service-identity: PASS")


if __name__ == "__main__":
    main()
