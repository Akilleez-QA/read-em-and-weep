"""Exact checks for the original-cover D3 reducer control."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import sympy as sp

_PATH = Path(__file__).resolve().parents[1] / "original_cover_control.py"
_SPEC = importlib.util.spec_from_file_location("original_cover_control", _PATH)
control = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(control)

# Supplied-list multiplicities. These lock the recorded input boundary.
# They are not a proof that the geometric label lists are complete.
D2_SOURCE = {
    -11: 23, -10: 20, -9: 40, -8: 34, -7: 51, -6: 42, -5: 41,
    -4: 31, -3: 22, -2: 15, -1: 9, 0: 5, 1: 2, 2: 1,
}
D2_TARGET = {
    -11: 32, -10: 26, -9: 52, -8: 40, -7: 60, -6: 43, -5: 47,
    -4: 32, -3: 25, -2: 16, -1: 9, 0: 5, 1: 2, 2: 1,
}
D3_SOURCE = {
    -12: 26, -11: 23, -10: 46, -9: 40, -8: 60, -7: 51, -6: 51,
    -5: 41, -4: 31, -3: 22, -2: 15, -1: 9, 0: 5, 1: 2, 2: 1,
}
D3_TARGET = {
    -12: 38, -11: 32, -10: 64, -9: 52, -8: 78, -7: 60, -6: 66,
    -5: 47, -4: 39, -3: 25, -2: 16, -1: 9, 0: 5, 1: 2, 2: 1,
}


class OriginalCoverControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = control.run_control()

    def test_rebuilt_d3_is_invertible_and_matches_certificate(self):
        result = self.result
        self.assertEqual(result["shape"], [9, 9])
        self.assertEqual(result["determinant"], "1")
        self.assertTrue(result["matches_certificate"])
        self.assertTrue(result["entries_in_Q"])
        self.assertEqual(len(result["source_columns"]), 9)
        self.assertEqual(len(result["target_rows"]), 9)
        determinant = sp.Integer(result["determinant"])
        self.assertNotEqual(determinant, 0)
        self.assertEqual(determinant, 1)

    def test_zero_reducer_fails_the_same_check(self):
        result = self.result
        self.assertEqual(result["stub_shape"], [9, 9])
        self.assertEqual(result["stub_determinant"], "0")
        self.assertTrue(result["stub_is_zero"])
        self.assertTrue(result["stub_check_failed"])
        self.assertIn("singular", result["stub_error"])
        self.assertIn("differs from supplied entries", result["producer_stub_error"])

    def test_basis_lists_recorded_as_input_boundary(self):
        by_order = {item["order"]: item for item in self.result["census"]}
        order2 = by_order[2]
        order3 = by_order[3]
        self.assertEqual(order2["source_length"], 336)
        self.assertEqual(order2["target_length"], 390)
        self.assertEqual(order2["prescribed_character"], -2)
        self.assertEqual(order2["source_multiplicities"], D2_SOURCE)
        self.assertEqual(order2["target_multiplicities"], D2_TARGET)
        self.assertEqual(len(order2["source_columns"]), 15)
        self.assertEqual(len(order2["target_rows"]), 16)
        self.assertEqual(order3["source_length"], 423)
        self.assertEqual(order3["target_length"], 534)
        self.assertEqual(order3["prescribed_character"], -1)
        self.assertEqual(order3["source_multiplicities"], D3_SOURCE)
        self.assertEqual(order3["target_multiplicities"], D3_TARGET)
        self.assertEqual(len(order3["source_columns"]), 9)
        self.assertEqual(len(order3["target_rows"]), 9)
        for item, source, target in (
            (order2, D2_SOURCE, D2_TARGET),
            (order3, D3_SOURCE, D3_TARGET),
        ):
            self.assertEqual(sum(source.values()), item["source_length"])
            self.assertEqual(sum(target.values()), item["target_length"])
            self.assertEqual(
                source[item["prescribed_character"]], len(item["source_columns"])
            )
            self.assertEqual(
                target[item["prescribed_character"]], len(item["target_rows"])
            )


if __name__ == "__main__":
    unittest.main()
