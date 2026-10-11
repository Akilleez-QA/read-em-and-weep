"""Comparison of the frozen k=4,5,6 bases with the shipped D4, D5 and D6 maps."""
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import compare_higher as compare
import generate_higher as higher
from compare_labels import entry_difference

REPO = ROOT.parents[2]
FREEZE = "d154dabe2d6e00dfd0932ecfdc3e980fe9346886"


class HigherComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = json.loads(compare.FROZEN.read_text(encoding="utf-8"))
        cls.report = compare.summarize(cls.document)

    def test_freeze_commit_is_unchanged(self):
        self.assertEqual(self.report["freeze_commit"], FREEZE)
        shown = subprocess.check_output(
            [
                "git",
                "show",
                f"{FREEZE}:research/hsd-label-audit-61/hsd_label_audit/frozen/higher_certificate.json",
            ],
            cwd=REPO,
            text=True,
        )
        self.assertEqual(json.loads(shown)["content_sha256"], self.report["content_sha256"])
        self.assertEqual(
            self.report["content_sha256"],
            "203311373309eded58fa5e30ee8a9ba1aeb8ff5050f3556abe0a2370685bf7cc",
        )

    def test_identity_bases_and_exact_matrices(self):
        self.assertFalse(self.report["mismatch"])
        self.assertTrue(self.report["weight_cutoff_uses_generated_maximum"])
        self.assertEqual(self.report["generated_max_character"], {"U": 2, "W": 2})
        by_map = {item["map"]: item for item in self.report["orders"]}
        expected = {
            "D4": {
                "shape": [701, 520],
                "raw_target": 701,
                "nnz": 1962,
                "pivots": 0,
                "character": 0,
                "connecting": False,
            },
            "D5": {
                "shape": [888, 627],
                "raw_target": 891,
                "nnz": 2484,
                "pivots": 30,
                "character": 1,
                "connecting": True,
            },
            "D6": {
                "shape": [1095, 744],
                "raw_target": 1104,
                "nnz": 3046,
                "pivots": 90,
                "character": 2,
                "connecting": True,
            },
        }
        for name, spec in expected.items():
            item = by_map[name]
            self.assertEqual(item["shipped_shape"], spec["shape"])
            self.assertEqual(item["frozen_dimension_U"], spec["shape"][1])
            self.assertEqual(item["frozen_dimension_W"], spec["shape"][0])
            self.assertTrue(item["source_change_of_basis"]["ordered_equal"])
            self.assertEqual(item["source_change_of_basis"]["determinant_over_Q"], "1")
            self.assertEqual(item["source_change_of_basis"]["size"], spec["shape"][1])
            self.assertTrue(item["target_change_of_basis"]["ordered_equal"])
            self.assertEqual(item["target_change_of_basis"]["determinant_over_Q"], "1")
            self.assertEqual(item["target_change_of_basis"]["size"], spec["raw_target"])
            self.assertEqual(item["kernel_free_rows"], spec["shape"][0])
            self.assertTrue(item["kernel_free_is_ordered_complement_of_pivots"])
            self.assertTrue(item["full_matrix"]["equal"])
            self.assertEqual(item["full_nonzero_rebuilt"], spec["nnz"])
            self.assertEqual(item["full_nonzero_shipped"], spec["nnz"])
            self.assertEqual(item["full_matrix"]["only_rebuilt"], [])
            self.assertEqual(item["full_matrix"]["only_shipped"], [])
            self.assertEqual(item["full_matrix"]["value_disagreements"], [])
            self.assertEqual(item["pivot_coordinates_in_raw_image"], spec["pivots"])
            self.assertEqual(item["alpha_columns_outside_C_kernel"], 0)
            self.assertEqual(item["required_character"], spec["character"])
            self.assertTrue(item["required_block_matches_frozen_alpha"])
            self.assertEqual(item["required_block_determinant_over_Q"], "1")
            connecting = item["connecting_change_of_basis"]
            self.assertEqual(connecting["compared"], spec["connecting"])
            if spec["connecting"]:
                self.assertTrue(connecting["matches_C_on_E0E1"])
                self.assertEqual(connecting["mismatches"], [])
                self.assertEqual(connecting["determinant_over_Q"], "-1")
                size = connecting["H3_rows"]
                minus = [[Fraction(change) for change in row] for row in connecting["change_of_basis"]]
                self.assertEqual(minus, [[-Fraction(i == j) for j in range(size)] for i in range(size)])

    def test_perturbed_map_and_repeated_basis_fail(self):
        block = [
            [Fraction(entry) for entry in row]
            for row in self.document["orders"]["5"]["alpha_matrix"]
        ]
        self.assertEqual(higher.square_determinant(block), Fraction(1))
        shipped = {
            (row, column): value
            for row, values in enumerate(block)
            for column, value in enumerate(values)
            if value
        }
        perturbed_rows = [row[:] for row in block]
        perturbed_rows[0][0] = Fraction(0)
        perturbed = {
            (row, column): value
            for row, values in enumerate(perturbed_rows)
            for column, value in enumerate(values)
            if value
        }
        difference = entry_difference(perturbed, shipped)
        self.assertFalse(difference["equal"])
        self.assertEqual(higher.square_determinant(perturbed_rows), Fraction(0))
        repeated = [row[:] for row in block]
        for row in repeated:
            row[1] = row[0]
        self.assertEqual(higher.square_determinant(repeated), Fraction(0))
        # A transposition stays invertible. The control above is a repeated column.
        swapped = [row[:] for row in block]
        swapped[0][0], swapped[0][1] = swapped[0][1], swapped[0][0]
        swapped[1][0], swapped[1][1] = swapped[1][1], swapped[1][0]
        self.assertEqual(higher.square_determinant(swapped), Fraction(-1))


if __name__ == "__main__":
    unittest.main()
