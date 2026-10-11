"""Exact checks for the blind k=4,5,6 bases and connecting maps.

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
import generate_higher as higher


FROZEN = ROOT / "frozen" / "higher_certificate.json"


def determinant(rows):
    return higher.square_determinant([[Fraction(entry) for entry in row] for row in rows])


class HigherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = higher.certificate_payload()
        cls.orders = cls.payload["orders"]

    def test_generator_does_not_name_shipped_labels(self):
        source = (ROOT / "generate_higher.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        forbidden = (
            "order_4.json",
            "order_5.json",
            "order_6.json",
            "D4_source_basis",
            "D5_source_basis",
            "D6_source_basis",
            "D4_target_basis",
            "raw_W5_labels",
            "raw_W6_labels",
        )
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                for word in forbidden:
                    self.assertNotIn(word, node.value)

    def test_e02_weights_come_from_cech_monomials(self):
        order4 = self.orders["4"]["E0^2_H3_weights"]
        self.assertEqual(order4["dimension"], 0)
        self.assertEqual(order4["weights"], [])
        order5 = self.orders["5"]["E0^2_H3_weights"]
        self.assertEqual(order5["dimension"], 3)
        self.assertEqual(order5["groups"][0]["actual"], [-1, -1, -1])
        self.assertEqual(sorted(order5["weights"]), [-8, -6, -4])
        order6 = self.orders["6"]["E0^2_H3_weights"]
        self.assertEqual(order6["dimension"], 9)
        by_actual = {tuple(group["actual"]): sorted(group["weights"]) for group in order6["groups"]}
        self.assertEqual(by_actual[(-1, -1, -2)], [-8, -6, -4])
        self.assertEqual(by_actual[(-1, -2, -1)], [-9, -7, -5])
        self.assertEqual(by_actual[(-2, -1, -1)], [-9, -7, -5])
        for k, order in self.orders.items():
            required = int(k) - 4
            characters = order["E0^2_H3_weights"]["characters"]
            self.assertTrue(all(character <= -4 for character in characters))
            self.assertNotIn(required, characters)

    def test_required_slices_include_e1_terms(self):
        expected = {
            "4": {"U": {"AE1": 4, "AE2": 1}, "W": {"E1^2": 4, "E1E2": 1}},
            "5": {"U": {"AE1": 2}, "W": {"E1^2": 2}},
            "6": {"U": {"AE1": 1}, "W": {"E1^2": 1}},
        }
        for k, order in self.orders.items():
            for kind, table in (("U", "filtration_U"), ("W", "filtration_W")):
                counts = {
                    line["name"]: len(line["required_H2"])
                    for line in order[table]
                    if line["required_H2"]
                }
                self.assertEqual(counts, expected[k][kind])
                self.assertNotIn("E0^2", counts)
            self.assertEqual(len(order["required_U"]), sum(expected[k]["U"].values()))
            self.assertEqual(len(order["required_W"]), sum(expected[k]["W"].values()))

    def test_connecting_ranks_and_dimension_identity(self):
        full = {
            "4": {"U": 520, "W_split": 701, "rank": 0, "W": 701, "kernel": 10, "H3": 0},
            "5": {"U": 627, "W_split": 891, "rank": 3, "W": 888, "kernel": 12, "H3": 3},
            "6": {"U": 744, "W_split": 1104, "rank": 9, "W": 1095, "kernel": 12, "H3": 9},
        }
        for k, order in self.orders.items():
            dims = order["cohomology_dimensions"]
            self.assertEqual(dims["dimension_U"], full[k]["U"])
            self.assertEqual(dims["dimension_W_split"], full[k]["W_split"])
            self.assertEqual(dims["dimension_W"], full[k]["W"])
            self.assertEqual(dims["dimension_W"], dims["dimension_W_split"] - dims["inner_connecting_rank"])
            inner = next(item for item in order["extensions"] if item["name"].startswith("E0^2"))
            delta = inner["all_characters"]["delta_H2_Q_to_H3_S"]
            h1_map = inner["all_characters"]["H1_Q_to_H2_S"]
            self.assertEqual(delta["rank"], full[k]["rank"])
            self.assertEqual(delta["kernel_dimension"], full[k]["kernel"])
            self.assertEqual(delta["cokernel_dimension"], 0)
            self.assertEqual(delta["shape"][0], full[k]["H3"])
            self.assertEqual(h1_map["rank"], 0)
            self.assertEqual(h1_map["shape"][1], 0)
            self.assertEqual(
                inner["all_characters"]["H2_E_dimension"],
                h1_map["cokernel_dimension"] + delta["kernel_dimension"],
            )
            required = inner["required_character"]["delta_H2_Q_to_H3_S"]
            self.assertEqual(required["shape"], [0, 0])
            self.assertEqual(required["rank"], 0)
            if k != "4":
                self.assertTrue(any(block["rank"] > 0 for block in delta["by_character"]))
                self.assertTrue(all(block["character"] <= -4 for block in delta["by_character"]))
            for extension in order["extensions"]:
                for scope in ("all_characters", "required_character"):
                    block = extension[scope]
                    self.assertEqual(
                        block["H2_E_dimension"],
                        block["H1_Q_to_H2_S"]["cokernel_dimension"]
                        + block["delta_H2_Q_to_H3_S"]["kernel_dimension"],
                    )
            outer = next(item for item in order["extensions"] if item["name"].startswith("span"))
            self.assertEqual(outer["sub_H3_dimension"], 0)
            self.assertEqual(outer["all_characters"]["delta_H2_Q_to_H3_S"]["rank"], 0)
            images = outer["required_character"]["image_in_full_H3_E0^2"]["columns"]
            self.assertTrue(images)
            self.assertTrue(all(column["image_in_H3_E0^2"] == [] for column in images))

    def test_alpha_blocks_are_invertible_over_q(self):
        expected = {"4": "1", "5": "1", "6": "1"}
        for k, order in self.orders.items():
            self.assertEqual(order["alpha_determinant"], expected[k])
            self.assertEqual(order["alpha_rank"], len(order["alpha_matrix"]))
            self.assertNotEqual(determinant(order["alpha_matrix"]), 0)
            self.assertEqual(str(determinant(order["alpha_matrix"])), order["alpha_determinant"])

    def test_weight_cutoff_uses_generated_maximum(self):
        self.assertEqual(self.payload["generated_max_character"], {"U": 2, "W": 2})
        for order in self.orders.values():
            for table in ("filtration_U", "filtration_W"):
                for line in order[table]:
                    characters = [row[-1] for row in line["H2_monomials"]]
                    if characters:
                        self.assertLessEqual(max(characters), 2)
                        self.assertEqual(max(characters), line["H2_character_bound"])
        for row in self.payload["weight_cutoff_checks"]:
            self.assertGreaterEqual(row["k"], 7)
            self.assertTrue(row["exceeds_generated_max"])
            self.assertGreater(row["required_character"], 2)

    def test_reducer_matches_the_k23_coordinate_projection(self):
        for k in (2, 3):
            for kind in ("U", "W"):
                for vector in bases.build_basis(kind, k):
                    old = bases.reduced_coordinates(kind, k, vector["_finite"])
                    new = higher.reduced_coordinates(kind, k, vector["_finite"])
                    self.assertEqual(new, old)

    def test_perturbed_map_and_basis_fail(self):
        original = self.orders["5"]["alpha_matrix"]
        self.assertEqual(determinant(original), 1)
        perturbed = [row[:] for row in original]
        perturbed[0][0] = "0"
        self.assertEqual(determinant(perturbed), 0)
        zero = [["0", "0"], ["0", "0"]]
        self.assertEqual(determinant(zero), 0)
        self.assertNotEqual(determinant(perturbed), determinant(original))

        finite, _infinity = bases.representative("W", (2, 2), 4, (0, 0, 9), 6)
        key = bases.coordinate_key("W", (2, 2), (4, -1, -1, -10))
        self.assertEqual(higher.reduced_coordinates("W", 6, finite), {key: Fraction(1)})
        broken = {slot: dict(poly) for slot, poly in finite.items()}
        broken[(1, 1)][(2, -1, -1, -2)] = Fraction(0)
        with self.assertRaises(ValueError):
            higher.reduced_coordinates("W", 6, broken)

        columns = []
        duals, rows, cols, _sparse = higher.delta_inner_columns(5)
        self.assertEqual(higher.matrix_rank(list(map(list, zip(*cols)))), 3)
        dropped = [column[:] for column in cols]
        dropped[0] = [Fraction(0) for _ in rows]
        self.assertLess(higher.matrix_rank(list(map(list, zip(*dropped)))), 3)
        self.assertEqual(len(duals), 15)

    def test_frozen_certificate_matches_regeneration_and_hash(self):
        self.assertTrue(FROZEN.is_file(), "frozen certificate is missing")
        digest = higher.verify_certificate(FROZEN)
        stored = json.loads(FROZEN.read_text(encoding="utf-8"))
        self.assertEqual(digest, stored["content_sha256"])
        self.assertEqual(higher.body_of(stored), self.payload)


if __name__ == "__main__":
    unittest.main()
