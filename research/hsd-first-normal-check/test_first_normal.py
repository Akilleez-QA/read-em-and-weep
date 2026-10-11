"""Exact tests for the §5.1 recheck. Run from the repository root:

    python3 -m unittest research/hsd-first-normal-check/test_first_normal.py -v
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp

import check_first_normal as cf


class IdealTests(unittest.TestCase):
    def test_numerator_outside_and_degree_three_rank(self):
        report = cf.check_numerator_and_sequence()
        self.assertTrue(report["outside"])
        self.assertNotEqual(sp.expand(report["remainder"]), 0)
        variables = [cf.X, cf.Y, cf.W]
        g1 = cf.S - cf.W**2
        # The normal-form remainder witnesses nonmembership for this monomial order.
        self.assertEqual(
            cf._membership_remainder(cf.a - report["remainder"], [cf.w, g1, cf.F], variables),
            0,
        )
        self.assertEqual(report["rank"], 6)
        self.assertEqual(report["rank_with_a"], 7)
        self.assertEqual(report["columns"], 6)
        self.assertEqual(report["monomials"], 10)

    def test_generators_are_a_regular_sequence(self):
        variables = [cf.X, cf.Y, cf.W]
        g1 = cf.S - cf.W**2
        ok, step, extras = cf.is_regular_sequence([cf.w, g1, cf.F], variables)
        self.assertTrue(ok)
        self.assertIsNone(step)
        self.assertEqual(extras, [])

    def test_colon_detector_sees_a_zerodivisor(self):
        # (XY) : (X) contains Y, so the detector must not report a regular step.
        extras = cf.colon_extras([cf.X * cf.Y], cf.X, [cf.X, cf.Y])
        self.assertTrue(extras)
        ok, step, _extras = cf.is_regular_sequence([cf.X**2, cf.X], [cf.X])
        self.assertFalse(ok)
        self.assertEqual(step, 1)


class CechTests(unittest.TestCase):
    def test_class_lives_on_the_triple_overlap(self):
        report = cf.check_cech_and_chart()
        self.assertTrue(all(report["coprime"].values()))
        self.assertEqual(report["numerator_plane_degrees"], [3])
        self.assertEqual(report["denominator_plane_degrees"], [10])
        numerator = cf.z * cf.a
        denominator = sp.expand(cf.w * (-cf.g) * cf.F)
        self.assertEqual(cf.plane_degrees(numerator), {3})
        self.assertEqual(cf.plane_degrees(denominator), {10})

    def test_regular_at_the_explicit_chart_and_colon(self):
        variables = [cf.X, cf.Y, cf.W]
        g1 = cf.S - cf.W**2
        signed = [cf.w, sp.expand(-g1), cf.F]
        ok, step, extras = cf.is_regular_sequence(signed, variables)
        self.assertTrue(ok, (step, extras))
        product = sp.expand(cf.w * (-g1) * cf.F)
        squared = [sp.expand(factor**2) for factor in signed]
        colon = cf.colon_generators(squared, product, variables)
        self.assertTrue(cf.contained(colon, signed, variables))
        self.assertTrue(cf.contained(signed, colon, variables))
        # Numerator survives the first map of the direct limit.
        self.assertNotEqual(
            cf._membership_remainder(sp.expand(cf.a * product), squared, variables),
            0,
        )
        report = cf.check_cech_and_chart()
        self.assertTrue(report["regular_with_z"])
        self.assertFalse(report["a_killed_in_first_limit_step"])
        self.assertEqual(report["leading_pure_powers"], {"X": 2, "Y": 3, "W": 6})
        self.assertTrue(report["colon_equals_ideal"])
        self.assertTrue(report["regular_at_z1"])


class InjectivityTests(unittest.TestCase):
    def test_flag_and_kunneth(self):
        report = cf.check_injectivity()
        self.assertTrue(all(report["flag"].values()))
        self.assertEqual(report["AI"], (3, -7))
        expected = {
            "P": (3, -4),
            "E0": (0, -1),
            "E1": (4, -5),
            "E2": (3, -5),
        }
        for line in report["lines"]:
            self.assertEqual(line["bidegree"], expected[line["summand"]])
            self.assertEqual(line["h1"], 0)
            self.assertEqual(cf.h1_dimension(*line["bidegree"]), 0)
        # The same formula is nonzero on a line that should contribute, so the zero
        # results are not a constant function.
        self.assertGreater(cf.h1_dimension(-3, 0), 0)
        base = cf.transition_matrix()
        self.assertEqual(sp.expand(base[1, 2] - cf.z * cf.C), 0)


class DegreeTests(unittest.TestCase):
    def test_bidegree_matches_O_3_minus_7(self):
        report = cf.check_bidegree()
        self.assertEqual(report["plane_degree"], 3 - 6 - 2 - 2)
        self.assertEqual(report["plane_degree"], -7)
        self.assertEqual(report["AI"], (3, -7))
        self.assertEqual(report["HomDA_tensor_DI"], (3, -7))
        self.assertEqual(report["visible_z_exponent"], 1)
        self.assertEqual(report["A_frame_base_degree"], 3)
        self.assertEqual(report["L_base"], 4)
        self.assertNotEqual(report["visible_z_exponent"], report["AI"][0])


class TauTests(unittest.TestCase):
    def test_rederived_identity_includes_value_line(self):
        report = cf.check_tau()
        self.assertTrue(report["identity"])
        self.assertTrue(report["value_line_slot_is_z"])
        for entry in report["pq_entries"]:
            self.assertEqual(sp.expand(sp.together(entry - cf.z**4)), 0)
        derived = report["derived"]
        for chart in range(3):
            residual = cf.form_residual(
                derived["tau"][chart],
                derived["omega_finite"][chart],
                derived["omega_infinity"][chart],
            )
            self.assertEqual(residual, sp.zeros(4))
        # Infinity pairing on the perturbed chart is g/z, the value transported by z^4.
        omega = derived["omega_infinity"][1]
        self.assertEqual(sp.simplify(omega[1, 2] - cf.g / cf.z), 0)
        self.assertEqual(sp.simplify(omega[0, 3] - 1), 0)

    def test_e_leg_scaling_breaks_and_is_not_a_pairing_rescaling(self):
        report = cf.check_tau()
        self.assertTrue(report["break_matches_prediction"])
        self.assertTrue(report["break_entry_nonzero"])
        self.assertEqual(sp.expand(report["break_entry"] - cf.z**3 * cf.g), 0)
        self.assertEqual(sp.expand(report["break_pq_defect"]), 0)

    def test_shear_does_not_break_and_pd_rescaling_is_excluded(self):
        report = cf.check_tau()
        self.assertTrue(report["shear_still_holds"])
        self.assertNotEqual(sp.expand(report["pd_pairing_defect"]), 0)
        # The excluded P–D rescaling moves the pairing by 1, in the units of Ω(P, q).
        self.assertEqual(sp.expand(report["pd_pairing_defect"] - 1), 0)


class VerdictTests(unittest.TestCase):
    def test_all_five_pass(self):
        report = cf.verdicts()
        self.assertEqual(report["pin"], cf.PIN)
        self.assertEqual(
            report["verdicts"],
            {"1": "pass", "2": "pass", "3": "pass", "4": "pass", "5": "pass"},
        )
        self.assertFalse(report["check2"]["kernel_risk"])
        self.assertTrue(report["check3"]["proved"])


if __name__ == "__main__":
    unittest.main()
