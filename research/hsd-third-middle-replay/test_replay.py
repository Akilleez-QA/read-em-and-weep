#!/usr/bin/env python3
"""Exact tests for the independent third-middle replay."""

import ast
import json
import unittest
from fractions import Fraction
from pathlib import Path

import replay

Q = Fraction
HERE = Path(__file__).resolve().parent


class ArithmeticTests(unittest.TestCase):
    def test_bracket_matches_hand_expansion(self):
        # p = f1^2, q = f2^2. Then [p, q] = 4 XY f1 f2 on the finite chart.
        p = {(1, 1): replay.mono()}
        q = {(2, 2): replay.mono()}
        got = replay.bracket_quad(p, q, 0)
        self.assertEqual(got, {(1, 2): replay.scale_poly(replay.F, 4)})
        self.assertEqual(replay.bracket_quad(q, p, 0), {(1, 2): replay.scale_poly(replay.F, -4)})
        self.assertEqual(replay.bracket_quad(p, p, 0), {})

    def test_bracket_off_diagonal_hand_expansion(self):
        # p = f1 f2, q = f1 f3.
        p = {(1, 2): replay.mono()}
        q = {(1, 3): replay.mono()}
        got = replay.bracket_quad(p, q, 0)
        expected = {
            (1, 1): replay.W6,
            (1, 2): replay.G,
            (1, 3): replay.neg_poly(replay.F),
        }
        self.assertEqual(got, expected)

    def test_nested_vanishes_on_a_square(self):
        family = {(0, 0, 0, 0, 0): {(1, 1): replay.mono()}}
        self.assertEqual(replay.nested_family(family, family, 0), {})

    def test_published_plane_coefficient(self):
        nested = {(0, 0, 0, 0, 0): {(1, 1): replay.mono()}}
        raw = replay.plane_rhs({}, nested)
        self.assertEqual(raw[(0, 0, 0, 0, 0)][(1, 1)][(0, 0, 0, 0)], Q(-1, 12))

    def test_transport_of_frame_squares(self):
        self.assertEqual(replay.transport_quad({(0, 0): replay.mono()}), {(0, 0): replay.mono(z=2)})
        self.assertEqual(replay.transport_quad({(3, 3): replay.mono()}), {(3, 3): replay.mono(z=2)})
        self.assertEqual(replay.transport_quad({(1, 1): replay.mono()}), {(1, 1): replay.mono(z=-4)})
        self.assertEqual(replay.transport_quad({(0, 1): replay.mono()}), {(0, 1): replay.mono(z=-1)})

    def test_c_ech_signs(self):
        edge = {(1, 1): replay.mono()}
        self.assertEqual(replay.delta_triple({(0, 1): edge}), edge)
        self.assertEqual(replay.delta_triple({(0, 2): edge}), replay.scale_quad(edge, -1))
        self.assertEqual(replay.delta_triple({(1, 2): edge}), edge)
        self.assertEqual(replay.delta_edge({(0,): edge, (1,): {}}, 0, 1), replay.scale_quad(edge, -1))
        self.assertEqual(replay.delta_edge({(1,): edge}, 0, 1), edge)

    def test_relation_multiple_has_zero_remainder(self):
        # Quadratic alpha * f1, finite chart. Diagonal f1^2 carries W^6.
        quad = {
            (1, 1): replay.W6,
            (0, 1): replay.RF[0],
            (1, 2): replay.RF[2],
            (1, 3): replay.RF[3],
        }
        self.assertEqual(replay.quotient_remainder(quad, replay.RF), {})

    def test_planted_e0_square_is_its_own_remainder(self):
        planted = {replay.E0_SLOT: replay.mono(X=-1, Y=-1, W=1)}
        self.assertEqual(replay.quotient_remainder(planted, replay.RF), planted)

    def test_remainder_is_linear(self):
        left = {(0, 0): replay.mono(z=1, X=2)}
        right = {(1, 2): replay.mono(Y=3, W=-1)}
        together = replay.add_quad(left, right)
        got = replay.quotient_remainder(together, replay.RF)
        expected = replay.scale_remainder(
            replay.quotient_remainder(left, replay.RF),
            1,
        )
        other = replay.quotient_remainder(right, replay.RF)
        for slot in set(expected) | set(other):
            self.assertEqual(
                got.get(slot, {}),
                replay.add_poly(expected.get(slot, {}), other.get(slot, {})),
            )

    def test_float_coefficients_are_rejected(self):
        with self.assertRaises(ValueError):
            replay.rat(0.5)
        with self.assertRaises(ValueError):
            replay.rat("1.5")


class SourceBoundaryTests(unittest.TestCase):
    def test_no_forbidden_imports(self):
        tree = ast.parse((HERE / "replay.py").read_text())
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported.append(node.module or "")
        forbidden = {
            "pinned_contraction",
            "tensor_slot_support",
            "verify_third_middle",
            "construct_third_middle",
            "first_order_support",
            "section_action_support",
        }
        self.assertTrue(forbidden.isdisjoint(set(imported)))

    def test_rhs_and_sign_identification_precede_cochain_read(self):
        source = (HERE / "replay.py").read_text()
        body = source[source.index("def run"):]
        build_at = body.index("build_cubic_rhs(")
        identify_at = body.index("identify_visible_bch_sign(")
        read_at = body.index("read_cochain_bytes(")
        self.assertLess(build_at, read_at)
        self.assertLess(identify_at, read_at)


class ReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = replay.run(write_path=None)

    def test_receipt_matches_committed_result(self):
        committed = json.loads((HERE / "RECEIPT.json").read_text())
        self.assertEqual(self.receipt, committed)

    def test_all_forty_equations_and_controls(self):
        receipt = self.receipt
        self.assertTrue(receipt["all_passed"])
        self.assertEqual(receipt["equations_passed"], 40)
        self.assertEqual(receipt["equations_failed"], 0)
        self.assertEqual(len(receipt["equations"]), 40)
        for row in receipt["equations"]:
            self.assertEqual(row["result"], "pass")
            for key in receipt["component_checks_per_equation"]:
                self.assertEqual(row[key], "pass")
        self.assertEqual(receipt["lambda_slice_passed"], 5)
        self.assertEqual(receipt["graded_w_terms"], 13547)
        self.assertEqual(receipt["w_support"]["result"], "pass")
        self.assertEqual(receipt["w_support"]["nonzero_count"], 28)
        self.assertEqual(receipt["w_support"]["zero_count"], 12)
        sensitive = receipt["controls"]["known_sensitive_origin_finite01"]
        self.assertEqual(sensitive["result"], "pass")
        self.assertEqual(sensitive["quotient_remainder"], [{
            "slot": [1, 1],
            "frame": "E0^2",
            "exponent_zXYW": [0, -1, -1, 1],
            "coefficient": "1",
        }])
        signed = receipt["controls"]["wrong_sign_bch"]
        self.assertEqual(signed["result"], "pass")
        self.assertTrue(signed["identified_remainder_nonzero"])
        self.assertEqual(signed["wrong_sign_equation"], "fail")
        self.assertTrue(signed["wrong_sign_remainder_equals_twice_identified"])
        self.assertFalse(signed["blanket_input_flip_used"])
        self.assertFalse(receipt["primitive_gauge_regenerated"])
        self.assertFalse(receipt["primitive_equality_required"])


if __name__ == "__main__":
    unittest.main()
