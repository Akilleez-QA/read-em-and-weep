"""Tests for the exact-arithmetic review of the plane-completion lemma."""

import json
import sys
import unittest
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_plane_completion as chk


class TestPin(unittest.TestCase):
    def test_pinned_blobs_match_published_digests(self):
        digests = chk.pinned_digests()
        for name, digest in chk.EXPECTED_SHA256.items():
            actual, size = digests[name]
            self.assertEqual(actual, digest, name)
            if name in chk.EXPECTED_BYTES:
                self.assertEqual(size, chk.EXPECTED_BYTES[name], name)

    def test_manifest_records_the_same_two_digests(self):
        raw = chk.git_object_bytes("manifest.json")
        manifest = json.loads(raw)
        files = manifest["files"]
        for name in ("PLANE_COMPLETION_LEMMA.md", "INDEPENDENT_REVIEW.md"):
            self.assertEqual(files[name]["sha256"], chk.EXPECTED_SHA256[name])
            self.assertEqual(files[name]["bytes"], chk.EXPECTED_BYTES[name])


class TestElevenIdentities(unittest.TestCase):
    def test_eleven_residuals_are_the_zero_polynomial(self):
        residuals = chk.eleven_residuals()
        self.assertEqual(len(residuals), 11)
        for name, value in residuals.items():
            self.assertEqual(value, 0, name)

    def test_vector_sum_components_separately(self):
        for label, relation in (("finite", chk.finite_r()), ("infinity", chk.infinity_r())):
            for index, component in enumerate(chk.vector_sum_residuals(relation)):
                self.assertEqual(component, 0, (label, index))

    def test_chart_form_entries_match_the_skew_matrix(self):
        finite, infinity = chk.omega_chart_residuals()
        self.assertEqual(finite, [0, 0, 0])
        self.assertEqual(infinity, [0, 0, 0])

    def test_auxiliary_polynomials_and_transition(self):
        for name, value in chk.auxiliary_identity_residuals().items():
            self.assertEqual(value, 0, name)
        self.assertEqual(chk.transition_residuals(), [0, 0, 0, 0])

    def test_opposite_cech_sign_is_not_an_isometry(self):
        self.assertTrue(chk.flipped_pairing_is_nonzero())
        self.assertTrue(chk.sign_flip_does_not_cancel())


class TestDegreesWeightsCover(unittest.TestCase):
    def test_corrections_have_plane_degree_minus_four(self):
        degrees = chk.correction_plane_degrees()
        self.assertTrue(degrees)
        for name, degree in degrees.items():
            self.assertEqual(degree, -4, name)

    def test_bundle_arithmetic(self):
        bundles = chk.derived_bundles()
        self.assertEqual(bundles["D"], (1, 1))
        self.assertEqual(bundles["M"], (2, -4))
        self.assertEqual(bundles["M_formula"], (2, -4))
        self.assertEqual(
            bundles["filtration"],
            {"P": (2, -4), "E0": (-1, -1), "E1": (3, -5), "E2": (2, -5)},
        )
        self.assertEqual(bundles["Hom_E0_P"], (3, -3))
        self.assertEqual(bundles["Hom_E1_P"], (-1, 1))
        self.assertEqual(bundles["Hom_E2_P"], (0, 1))
        self.assertEqual(bundles["Hom_A_P"], (0, 3))

    def test_kunneth_vanishing_and_h2_complement(self):
        band, parts = chk.cohomology_p1_p2(2, -4)
        self.assertEqual(band, [0, 0, 9, 0])
        nonzero = [item for item in parts[2] if item[3] != 0]
        self.assertEqual(nonzero, [((0, 2), 3, 3, 9)])
        for bidegree in ((2, -4), (-1, -1), (3, -5), (2, -5)):
            dims, _parts = chk.cohomology_p1_p2(*bidegree)
            self.assertEqual(dims[1], 0, bidegree)
        self.assertEqual(chk.cohomology_p1_p2(3, -3)[0][0], 0)
        self.assertEqual(chk.cohomology_p1_p2(-1, 1)[0][0], 0)
        self.assertEqual(chk.cohomology_p1_p2(0, 1)[0][0], 3)
        self.assertEqual(chk.cohomology_p1_p2(0, 3)[0][0], 10)
        self.assertEqual(chk.cohomology_p1_p2(2, 0)[0][0], 3)

    def test_weights_match_targets_four_and_eight(self):
        ledger = chk.weight_ledger()
        self.assertEqual(ledger["psi_finite"], [3, 1, 1])
        self.assertEqual(ledger["psi_infinity"], [-3, 3, 1])
        self.assertEqual(ledger["d_D_finite"], 1)
        self.assertEqual(ledger["d_D_infinity"], 5)
        self.assertEqual(ledger["sums_finite"], [4, 4, 4])
        self.assertEqual(ledger["sums_infinity"], [8, 8, 8])
        self.assertEqual(ledger["form_totals_finite"], [4, 4, 4])
        self.assertEqual(ledger["form_totals_infinity"], [8, 8, 8])
        self.assertEqual(ledger["P_D_finite"], 4)
        self.assertEqual(ledger["P_D_infinity"], 8)

    def test_simultaneous_vanishing_forces_the_irrelevant_ideal(self):
        for value in chk.cover_polynomials().values():
            self.assertEqual(value, 0)

    def test_stated_overlaps_are_regular_and_swapped_terms_are_not(self):
        values = chk.overlap_values()
        self.assertEqual(values["finite_c12_on_U12"], 0)
        self.assertEqual(values["finite_c23_on_U23"], 0)
        self.assertEqual(values["finite_c31_on_U31"], 12)
        self.assertTrue(values["finite_c31_pole_on_U12"])
        self.assertTrue(values["finite_c12_pole_on_U23"])
        self.assertTrue(values["finite_c23_pole_on_U31"])
        self.assertEqual(values["infinity_c12_at_u0"], sp.Rational(1, 2))
        self.assertEqual(values["infinity_c23_at_u0"], -1)
        for name, gcd in chk.wrong_overlap_denominators().items():
            self.assertEqual(sp.degree(gcd), 0, name)


class TestRadicalsAndNoGo(unittest.TestCase):
    def test_each_local_psi_has_radical_exactly_the_graph_of_a(self):
        relation = (chk.r1s, chk.r2s, chk.r3s)
        graph = chk.graph_vector()
        vertical = chk.vertical_vector()
        for index in range(3):
            psi = [0, 0, 0]
            psi[index] = chk.a_s / relation[index]
            matrix = chk.form_matrix(relation, psi, lam=1)
            self.assertEqual(sp.simplify(matrix * graph), sp.zeros(5, 1))
            self.assertNotEqual(sp.simplify(matrix * vertical), sp.zeros(5, 1))
            self.assertEqual(len(matrix.nullspace()), 1)

    def test_zero_psi_keeps_b_and_the_canonical_pairing_but_not_the_radical(self):
        relation = (chk.r1s, chk.r2s, chk.r3s)
        matrix = chk.form_matrix(relation, (0, 0, 0), lam=1)
        self.assertEqual(sp.simplify(matrix * chk.vertical_vector()), sp.zeros(5, 1))
        self.assertNotEqual(sp.simplify(matrix * chk.graph_vector()), sp.zeros(5, 1))
        self.assertEqual(len(matrix.nullspace()), 1)
        self.assertNotEqual(sp.simplify(chk.a_s), 0)

    def test_zero_pairing_puts_p_in_the_radical_and_misses_a(self):
        relation = (chk.r1s, chk.r2s, chk.r3s)
        pure_p = sp.Matrix([1, 0, 0, 0, 0])
        graph = chk.graph_vector()
        self.assertEqual(sp.Matrix.hstack(pure_p, graph).rank(), 2)
        for psi in ((0, 0, 0), (chk.a_s / chk.r1s, 0, 0), (chk.r2s, chk.r3s, chk.r1s)):
            matrix = chk.form_matrix(relation, psi, lam=0)
            self.assertEqual(matrix * pure_p, sp.zeros(5, 1))

    def test_global_hom_obstruction_is_exactly_the_cubic_monomials(self):
        data = chk.scalar_pairing_obstruction()
        self.assertEqual(data["image_rank"], 3)
        self.assertEqual(data["augmented_rank"], 4)
        self.assertTrue(data["x3_row_of_image_is_zero"])
        self.assertTrue(data["y3_row_of_image_is_zero"])
        self.assertEqual(data["x3_coefficient_of_a"], 1)
        self.assertEqual(data["y3_coefficient_of_a"], 1)

    def test_uniqueness_uses_h0(self):
        band, _parts = chk.cohomology_p1_p2(2, -4)
        self.assertEqual(chk.isometry_status(band[0], band[1]), "unique")
        self.assertEqual(chk.isometry_status(1, 0), "exists-not-unique")
        self.assertEqual(chk.isometry_status(0, 1), "not-settled-by-vanishing")


if __name__ == "__main__":
    unittest.main()
