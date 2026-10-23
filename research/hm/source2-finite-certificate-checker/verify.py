#!/usr/bin/env python3
"""Reproduce only the package's universal/synthetic structural tests."""
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest

import check_certificate as c
from test_certificate import CertificateTests, fixture


def main():
    root = Path(__file__).resolve().parent
    expected_fixture = fixture()
    saved_fixture = c.load_bytes((root / "synthetic-example.json").read_bytes())
    if saved_fixture != expected_fixture:
        raise RuntimeError("retained synthetic fixture differs from formula")
    capture = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(CertificateTests)
    names = [test.id().split(".")[-1] for test in suite]
    result = unittest.TextTestRunner(stream=capture).run(suite)
    if not result.wasSuccessful():
        raise RuntimeError(capture.getvalue())
    command = [sys.executable] + (["-O"] if not __debug__ else [])
    command += [str(root / "check_certificate.py"), str(root / "synthetic-example.json"),
                "--expected-data-sha256", expected_fixture["binding"]["data_sha256"]]
    proc = subprocess.run(command, capture_output=True, text=True, timeout=20, check=True)
    cli_result = json.loads(proc.stdout)
    expected_result = c.check(expected_fixture, expected_fixture["binding"]["data_sha256"])
    if cli_result != expected_result:
        raise RuntimeError("CLI and direct API reports differ")
    report = {
        "status": "PASS",
        "unit_tests": result.testsRun,
        "tests": names,
        "synthetic_fixture_regeneration": "PASS",
        "synthetic_cli_expected_digest_check": "PASS",
        "synthetic_result": cli_result,
        "scope": "Universal/synthetic exact checks only; no actual HM certificate supplied or evaluated.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
