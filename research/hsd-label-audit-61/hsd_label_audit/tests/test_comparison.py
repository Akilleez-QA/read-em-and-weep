"""Comparison of the frozen bases with the shipped D2 and D3 maps."""
import json
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import compare_labels as compare

REPO = ROOT.parents[2]
FREEZE = "a628b449f9c48bb08a227d55cc65c729fb890d7b"


class ComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        document = json.loads(compare.FROZEN.read_text(encoding="utf-8"))
        cls.report = compare.summarize(document)

    def test_freeze_commit_is_unchanged(self):
        self.assertEqual(self.report["freeze_commit"], FREEZE)
        shown = subprocess.check_output(
            ["git", "show", f"{FREEZE}:research/hsd-label-audit-61/hsd_label_audit/frozen/basis_certificate.json"],
            cwd=REPO,
            text=True,
        )
        self.assertEqual(json.loads(shown)["content_sha256"], self.report["content_sha256"])

    def test_identity_bijection_and_exact_matrices(self):
        self.assertFalse(self.report["mismatch"])
        by_map = {item["map"]: item for item in self.report["orders"]}
        d2, d3 = by_map["D2"], by_map["D3"]
        self.assertEqual(d2["shipped_shape"], [390, 336])
        self.assertEqual(d3["shipped_shape"], [534, 423])
        self.assertEqual([d2["slice_source_columns"], d2["slice_target_rows"]], [15, 16])
        self.assertEqual([d3["slice_source_columns"], d3["slice_target_rows"]], [9, 9])
        self.assertEqual(d2["slice_rank_over_Q"], 15)
        self.assertEqual(d3["slice_determinant_over_Q"], "1")
        for item in (d2, d3):
            self.assertTrue(item["ordered_source_identity"])
            self.assertTrue(item["ordered_target_identity"])
            self.assertTrue(item["full_matrix"]["equal"])
            self.assertTrue(item["slice_matrix"]["equal"])
            self.assertEqual(item["full_matrix"]["only_rebuilt"], [])
            self.assertEqual(item["full_matrix"]["only_shipped"], [])
            self.assertEqual(item["full_matrix"]["value_disagreements"], [])

    def test_a_single_disagreement_is_isolated(self):
        rebuilt = {(0, 1): Fraction(1), (2, 3): Fraction(1, 2)}
        shipped = {(0, 1): Fraction(1), (2, 3): Fraction(1, 3), (4, 5): Fraction(-2)}
        difference = compare.entry_difference(rebuilt, shipped)
        self.assertFalse(difference["equal"])
        self.assertEqual(
            difference["value_disagreements"],
            [{"row": 2, "column": 3, "rebuilt": "1/2", "shipped": "1/3"}],
        )
        self.assertEqual(difference["only_shipped"], [{"row": 4, "column": 5, "shipped": "-2"}])
        self.assertEqual(difference["only_rebuilt"], [])


if __name__ == "__main__":
    unittest.main()
