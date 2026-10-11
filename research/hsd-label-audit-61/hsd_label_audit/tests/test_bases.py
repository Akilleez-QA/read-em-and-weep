"""Exact checks for the blind k=2,3 cohomology bases.

These tests do not read shipped label lists, stored maps, or pivot sets.
"""
import ast
import json
import unittest
from fractions import Fraction
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import generate_bases as bases


FROZEN = ROOT / "frozen" / "basis_certificate.json"


class BasisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = bases.certificate_payload()
        cls.orders = cls.payload["orders"]

    def test_generator_does_not_name_shipped_labels(self):
        source = (ROOT / "generate_bases.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        forbidden = (
            "order_1.json",
            "order_2.json",
            "order_3.json",
            "D2_source_basis",
            "D3_source_basis",
            "D2_target_basis",
            "D3_target_basis",
        )
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                for word in forbidden:
                    self.assertNotIn(word, node.value)

    def test_transition_and_homotopy_lemmas(self):
        bases.assert_relation_transition()
        self.assertGreater(bases.assert_plane_homotopy(), 0)
        self.assertTrue(self.payload["relation_transition_identity"])

    def test_line_dimensions_sum_to_enumeration(self):
        for k, order in self.orders.items():
            self.assertEqual(sum(row["dimension"] for row in order["lines_U"]), order["dimension_U"])
            self.assertEqual(sum(row["dimension"] for row in order["lines_W"]), order["dimension_W"])
            self.assertEqual(sum(order["characters_U"].values()), order["dimension_U"])
            self.assertEqual(sum(order["characters_W"].values()), order["dimension_W"])
            self.assertEqual(order["glue_and_coordinate_checks"], order["dimension_U"] + order["dimension_W"])
            self.assertEqual(order["alpha_image_lands_in_W_basis"], order["dimension_U"])

    def test_labels_are_unique_and_integral(self):
        for order in self.orders.values():
            for kind in ("U", "W"):
                keys = []
                for vector in order[kind]:
                    slot = tuple(vector["slot"]) if isinstance(vector["slot"], list) else (vector["slot"],)
                    keys.append((slot, vector["e"], tuple(vector["dual"])))
                    self.assertEqual(vector["actual"], [-n - 1 for n in vector["dual"]])
                    self.assertEqual(sum(vector["dual"]), -sum(vector["actual"]) - 3)
                    for term in vector["forced"]:
                        self.assertEqual(Fraction(term["coefficient"]).denominator, 1)
                        self.assertGreaterEqual(term["e"], 0)
                self.assertEqual(len(keys), len(set(keys)))

    def test_square_normalization_omits_global_e0e1(self):
        for order in self.orders.values():
            for vector in order["W"]:
                if vector["slot"] != [2, 2]:
                    continue
                for term in vector["forced"]:
                    self.assertEqual(term["slot"], [1, 2])
                    self.assertGreaterEqual(term["e"], 1)

    def test_pure_lines_have_no_forced_component(self):
        for k, order in self.orders.items():
            pure_u = {0, 3}
            pure_w = {(0, 0), (0, 3), (1, 2), (3, 3)}
            for vector in order["U"]:
                if vector["slot"] in pure_u:
                    self.assertEqual(vector["forced"], [])
            for vector in order["W"]:
                if tuple(vector["slot"]) in pure_w:
                    self.assertEqual(vector["forced"], [])
            self.assertIn(k, ("2", "3"))

    def test_hand_checked_e1_square_monomial(self):
        # k=2, E1^2, z^2 X^{-1} Y^{-1} W^{-6}. Only the W^4 term of C survives,
        # with the square multiplicity 2, at z^1 in E0 E1.
        finite, infinity = bases.representative("W", (2, 2), 2, (0, 0, 5), 2)
        self.assertEqual(finite[(2, 2)], {(2, -1, -1, -6): Fraction(1)})
        self.assertEqual(finite[(1, 2)], {(1, -1, -1, -2): Fraction(2)})
        self.assertTrue(all(exp[0] <= 0 for poly in infinity.values() for exp in poly))
        coords = bases.reduced_coordinates("W", 2, finite)
        self.assertEqual(coords, {(2, 2, 2, 0, 0, 5): Fraction(1)})

    def test_hand_checked_ae1_monomial(self):
        # k=2, AE1, z^1 X^{-1} Y^{-1} W^{-8}. The surviving forced term is
        # z^0 X^{-1} Y^{-1} W^{-4} in AE0, coefficient 1.
        finite, infinity = bases.representative("U", 2, 1, (0, 0, 7), 2)
        self.assertEqual(finite[2], {(1, -1, -1, -8): Fraction(1)})
        self.assertEqual(finite[1], {(0, -1, -1, -4): Fraction(1)})
        self.assertTrue(all(exp[0] <= 0 for poly in infinity.values() for exp in poly))
        coords = bases.reduced_coordinates("U", 2, finite)
        self.assertEqual(coords, {(2, 1, 0, 0, 7): Fraction(1)})

    def test_sample_alpha_image_is_nonzero(self):
        finite, _infinity = bases.representative("U", 0, 0, (0, 0, 6), 2)
        image = bases.alpha_image(2, finite)
        self.assertTrue(image)
        self.assertTrue(all(value.denominator == 1 for value in image.values()))

    def test_frozen_certificate_matches_regeneration_and_hash(self):
        self.assertTrue(FROZEN.is_file(), "frozen certificate is missing")
        digest = bases.verify_certificate(FROZEN)
        stored = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(digest, stored["content_sha256"])
        self.assertEqual(bases.body_of(stored), self.payload)


if __name__ == "__main__":
    unittest.main()
