#!/usr/bin/env python3
"""Run both exact checks and compare the deterministic reference transcript."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = ("verify_central.py", "verify_maximal.py")
chunks = []
env = dict(os.environ)
env.pop("PYTHONOPTIMIZE", None)
for script in SCRIPTS:
    result = subprocess.run(
        [sys.executable, str(ROOT / script)], cwd=ROOT, env=env,
        text=True, capture_output=True, check=True,
    )
    if result.stderr:
        raise RuntimeError(f"Unexpected stderr from {script}: {result.stderr}")
    chunks.append(f"=== {script} ===\n{result.stdout}")
actual = "\n".join(chunks)
expected = (ROOT / "verification.txt").read_text(encoding="utf-8")
if actual != expected:
    sys.stdout.write(actual)
    raise SystemExit("FAIL: exact checks completed, but output differs from verification.txt")
sys.stdout.write(actual)
print("PASS: both exact checkers match the reference transcript")
