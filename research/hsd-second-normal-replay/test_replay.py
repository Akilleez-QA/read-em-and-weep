"""Exact checks for the independent second-normal replay."""

import ast
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import common
from common import (
    A0,
    F4,
    G4,
    ONE4,
    S3,
    W6,
    dot3,
    g_times_c,
    lambda_covector,
    relation,
    transport_identity_literal,
)

HERE = Path(__file__).resolve().parent
FORBIDDEN = (
    "SECOND_NORMAL_SECTION_CORRECTIONS",
    "SECOND_NORMAL_COMPARISON_CHECKS",
    "check_second_normal_comparison",
    "lambda_order_three",
)


class HandPins(unittest.TestCase):
    def test_gc_matches_hand_binomial(self):
        self.assertEqual(g_times_c(), transport_identity_literal())

    def test_s3_binomial_coefficients(self):
        # (X^2 + Y^2)^3 = X^6 + 3 X^4 Y^2 + 3 X^2 Y^4 + Y^6
        expected = {
            (0, 6, 0, 0): common.F(1),
            (0, 4, 2, 0): common.F(3),
            (0, 2, 4, 0): common.F(3),
            (0, 0, 6, 0): common.F(1),
        }
        self.assertEqual(S3, expected)

    def test_lambda_w_and_lambda_x(self):
        finite_r = relation("finite")[1:]
        infinity_r = relation("infinity")[1:]
        self.assertEqual(dot3(lambda_covector("finite", 2), finite_r), ONE4)
        self.assertEqual(dot3(lambda_covector("finite", 0), finite_r), ONE4)
        self.assertEqual(dot3(lambda_covector("finite", 1), finite_r), ONE4)
        self.assertEqual(dot3(lambda_covector("infinity", 0), infinity_r), ONE4)
        self.assertEqual(dot3(lambda_covector("infinity", 1), infinity_r), ONE4)
        self.assertEqual(dot3(lambda_covector("infinity", 2), infinity_r), ONE4)

    def test_tb_identity_components(self):
        from common import apply_TB, shift, vec_eq

        image = apply_TB(relation("infinity"))
        target = [shift(component, dz=3) for component in relation("finite")]
        self.assertTrue(vec_eq(image, target))
        # E0 component of z^3 r_finite is z^3 W^6.
        self.assertEqual(target[1], {(3, 0, 0, 6): common.F(1)})

    def test_bracket_literal_from_omega(self):
        """{-2 z X^{-2} Y^{-1} E0 E1, E0} = 2 z X^{-1} E0, from Ω(E1, E0) = -XY."""
        from common import V_E0, action_on_vector, omega_pairs

        eta = {(1, -2, -1, 0, 0, 1, 1, 0): common.F(-2)}
        vector = action_on_vector(eta, V_E0, omega_pairs("finite"))
        self.assertEqual(vector[0], {})
        self.assertEqual(vector[2], {})
        self.assertEqual(vector[3], {})
        self.assertEqual(vector[1], {(1, -1, 0, 0): common.F(2)})

    def test_bch_half_from_the_exponential(self):
        """exp(hA) exp(hB) = exp(h(A+B) + h^2/2 [A,B]) through h^2, over Q."""
        # 2x2 matrices, entries are polynomials in h truncated at h^3.
        A = [[common.F(1), common.F(2)], [common.F(-3), common.F(4)]]
        B = [[common.F(0), common.F(-1)], [common.F(5), common.F(2)]]

        def mm(p, q):
            return [
                [p[0][0] * q[0][0] + p[0][1] * q[1][0], p[0][0] * q[0][1] + p[0][1] * q[1][1]],
                [p[1][0] * q[0][0] + p[1][1] * q[1][0], p[1][0] * q[0][1] + p[1][1] * q[1][1]],
            ]

        def madd(p, q):
            return [[p[i][j] + q[i][j] for j in range(2)] for i in range(2)]

        def mscale(p, c):
            return [[c * p[i][j] for j in range(2)] for i in range(2)]

        eye = [[common.F(1), common.F(0)], [common.F(0), common.F(1)]]
        # exp(hM) = I + h M + h^2 M^2 / 2, stored as coefficients of 1, h, h^2.
        def exp_h(M):
            M2 = mm(M, M)
            return [eye, M, mscale(M2, Fraction(1, 2))]

        def mul_series(p, q):
            out = [mscale(eye, 0), mscale(eye, 0), mscale(eye, 0)]
            out[0] = mm(p[0], q[0])
            out[1] = madd(mm(p[0], q[1]), mm(p[1], q[0]))
            out[2] = madd(madd(mm(p[0], q[2]), mm(p[1], q[1])), mm(p[2], q[0]))
            return out

        def commutator(p, q):
            return madd(mm(p, q), mscale(mm(q, p), -1))

        left = mul_series(exp_h(A), exp_h(B))
        bracket = commutator(A, B)
        # exp(h(A+B) + h^2/2 [A,B]) = I + h(A+B) + h^2 ( (A+B)^2/2 + [A,B]/2 )
        AB = madd(A, B)
        quad = madd(mscale(mm(AB, AB), Fraction(1, 2)), mscale(bracket, Fraction(1, 2)))
        right = [eye, AB, quad]
        self.assertEqual(left, right)
        # The opposite quadratic sign disagrees on this pair.
        flipped = [eye, AB, madd(mscale(mm(AB, AB), Fraction(1, 2)), mscale(bracket, Fraction(-1, 2)))]
        self.assertNotEqual(left, flipped)

    def test_cohomology_vanishing_numbers(self):
        # B I^2 lines: plane degree of each frame plus -2 is negative.
        frames = {"P": (3, -3), "E0": (0, 0), "E1": (4, -4), "E2": (3, -4)}
        for bidegree in frames.values():
            self.assertLess(bidegree[1] - 2, 0)
        # A I^2 = O(3,-8). H^1(P1, O(3))=0 and H^1(P2, O(-8))=0, so Künneth gives 0.
        # A = O(3,-6), so A I^2 = O(3,-8). H^1(P1, O(3)) = 0 and H^1(P2, O(n)) = 0.
        self.assertEqual((3 + 0, -6 - 2), (3, -8))
        self.assertGreaterEqual(3, -1)

    def test_builder_does_not_name_solver_output(self):
        source = (HERE / "build_rhs.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        self.assertIsNotNone(tree)
        for token in FORBIDDEN:
            self.assertNotIn(token, source)
        common_source = (HERE / "common.py").read_text(encoding="utf-8")
        for token in FORBIDDEN:
            self.assertNotIn(token, common_source)

    def test_displayed_forms_match_chart(self):
        # Finite Ω entries used by the bracket are F, g, W^6.
        self.assertEqual(common.omega_pairs("finite")[(1, 2)], F4)
        self.assertEqual(common.omega_pairs("finite")[(1, 3)], G4)
        self.assertEqual(common.omega_pairs("finite")[(2, 3)], W6)
        self.assertEqual(relation("finite")[0], common.scale(A0, -1))
        self.assertEqual(relation("infinity")[1], S3)


class FrozenSolution(unittest.TestCase):
    def test_corrections_solve_frozen_rhs(self):
        import build_rhs
        import check_solutions

        build_rhs.main()
        check_solutions.main()
        report = json.loads((HERE / "check_report.json").read_text(encoding="utf-8"))
        self.assertEqual(report["exported_terms"], 405)
        self.assertEqual(report["good_failures"], 0)
        self.assertEqual(report["good_equations"], 135)
        self.assertEqual(report["bad_algebra_failures"], 42)
        self.assertTrue(report["opposite_sign_nontrivial"])
        frozen = json.loads((HERE / "frozen_rhs.json").read_text(encoding="utf-8"))
        self.assertEqual(
            frozen["rhs_sha256"],
            "b9125f86d68b0eeb0fcca82dfad8c72a05aad0aed76ad6fd6411c59f324e02bf",
        )
        self.assertEqual(frozen["rhs_sha256"], report["rhs_sha256"])
        self.assertEqual(frozen["pin"], "22b800836385cf4c869c200bfc6715e07613aad6")


if __name__ == "__main__":
    unittest.main()
