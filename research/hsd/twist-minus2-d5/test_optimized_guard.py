#!/usr/bin/env python3
"""Entry guard for the twist -2 d5 certificate under Python optimized mode.

Plain mode must exit 0 and print the certificate. Optimized mode must exit
nonzero, print the refusal, and emit no certificate JSON. Refusal at entry
does not exercise the downstream mutation or negative-control checks.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RELATIVE = Path("research") / "hsd" / "twist-minus2-d5" / "certificate.py"
REFUSAL = (
    "certificate refuses to run under -O / PYTHONOPTIMIZE "
    "because its proof checks are asserts"
)


def environment(extra: dict[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    env.pop("PYTHONOPTIMIZE", None)
    if extra:
        env.update(extra)
    return env


def invoke(
    argv: list[str], extra: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        argv,
        cwd=ROOT,
        env=environment(extra),
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> None:
    failures: list[str] = []
    plain = invoke([sys.executable, str(RELATIVE)])
    if plain.returncode != 0:
        failures.append(f"plain mode exited {plain.returncode}, expected 0")
    if not plain.stdout.startswith("{") or '"certificate"' not in plain.stdout:
        failures.append("plain mode did not print the certificate JSON")

    cases: list[tuple[str, list[str], dict[str, str] | None]] = [
        ("python3 -O", [sys.executable, "-O", str(RELATIVE)], None),
        ("python3 -OO", [sys.executable, "-OO", str(RELATIVE)], None),
        (
            "PYTHONOPTIMIZE=1",
            [sys.executable, str(RELATIVE)],
            {"PYTHONOPTIMIZE": "1"},
        ),
    ]
    for name, argv, extra in cases:
        proc = invoke(argv, extra)
        if proc.returncode == 0:
            failures.append(f"{name} exited 0, expected nonzero")
        if proc.stdout:
            failures.append(f"{name} wrote certificate stdout ({len(proc.stdout)} bytes)")
        if proc.stderr.strip() != REFUSAL:
            failures.append(f"{name} stderr was {proc.stderr!r}")

    if failures:
        for item in failures:
            print(item, file=sys.stderr)
        raise SystemExit(1)
    print(
        "plain exit 0; -O, -OO, and PYTHONOPTIMIZE=1 refuse with empty certificate stdout"
    )


if __name__ == "__main__":
    main()
