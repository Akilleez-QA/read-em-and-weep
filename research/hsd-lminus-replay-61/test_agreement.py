"""Supplied-data comparison against the pinned package outputs.

Runs after the selector freeze. It does not import the package replay.
"""

from __future__ import annotations

import io
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

from compare_supplied import compare
from selector import PIN


REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_MEMBER = "research/hm/second-scalar-all81"
WANTED = (
    "quotients.json",
    "expected.json",
    "duplicate-binding.json",
)


class SuppliedAgreement(unittest.TestCase):
    def test_no_mismatches_against_pinned_outputs(self):
        archive = subprocess.check_output(
            ["git", "archive", PIN, PACKAGE_MEMBER],
            cwd=REPO_ROOT,
        )
        with tempfile.TemporaryDirectory() as directory:
            with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
                for name in WANTED:
                    bundle.extract(PACKAGE_MEMBER + "/" + name, directory, filter="data")
            result = compare(Path(directory) / PACKAGE_MEMBER)
        self.assertEqual(result["mismatches"], [])
        self.assertEqual(result["statistics"]["computed_targets"], 65)
        self.assertEqual(result["statistics"]["empty_boundary_targets"], 16)
        self.assertEqual(result["statistics"]["requests"], 648)
        self.assertEqual(result["equal_array_pairs"], 12)
        self.assertEqual(result["documented_mapped_rows"], 1086)


if __name__ == "__main__":
    unittest.main()
