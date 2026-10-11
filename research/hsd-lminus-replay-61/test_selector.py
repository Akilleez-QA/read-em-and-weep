"""Structural checks and precommitted negative controls.

These tests do not read replay.py and do not read expected.json.
Package inputs are taken from the pinned tree.
"""

from __future__ import annotations

import io
import subprocess
import tarfile
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

from selector import (
    PIN,
    SIGMA,
    apply_sigma_tuple,
    all_orientations,
    bindings_distinct,
    boundary_partition,
    certified_kernel_weights,
    covariance_failures,
    documented_duplicate_pairs,
    equal_array_pairs,
    evaluate,
    iter_boundary,
    kernel_weights_binomial,
    kernel_weights_inverse_power,
    load_quotients,
    monomials,
    permutation_sign,
    perturb_numerator,
    request_orientation_failures,
    sensitivity,
    summary,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_MEMBER = "research/hm/second-scalar-all81"


def extract_pinned_package():
    archive = subprocess.check_output(
        ["git", "archive", PIN, PACKAGE_MEMBER],
        cwd=REPO_ROOT,
    )
    directory = tempfile.TemporaryDirectory()
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        member = bundle.getmember(PACKAGE_MEMBER + "/quotients.json")
        bundle.extract(member, directory.name, filter="data")
    return directory, Path(directory.name) / PACKAGE_MEMBER


class SelectorAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmpdir, package = extract_pinned_package()
        cls.package = package
        cls.quotients = load_quotients(package)
        cls.weights = certified_kernel_weights()
        cls.audit = evaluate(cls.quotients, cls.weights)
        cls.stats = summary(cls.audit)

    @classmethod
    def tearDownClass(cls):
        cls._tmpdir.cleanup()

    def test_kernel_expansions_agree_and_invert(self):
        self.assertEqual(kernel_weights_binomial(), kernel_weights_inverse_power())
        self.assertEqual(self.weights[(0, 0)], 1)
        self.assertEqual(len(self.weights), 9 * 23)

    def test_partition_comes_from_the_empty_boundary(self):
        nonempty, empty = boundary_partition(self.quotients, self.weights)
        self.assertEqual(len(nonempty) + len(empty), 81)
        self.assertEqual(len(nonempty), 65)
        self.assertEqual(len(empty), 16)
        for index, target in monomials():
            leading_hits = [roles for roles in all_orientations() if target[roles[0]] == 2]
            if index in empty:
                self.assertEqual(leading_hits, [])
                self.assertTrue(all(entry <= 1 for entry in target))
            else:
                self.assertGreater(len(leading_hits), 0)
        computed_empty = [
            item["index"] for item in self.audit["coordinates"] if item["empty_boundary"]
        ]
        self.assertEqual(computed_empty, empty)
        for item in self.audit["coordinates"]:
            if item["empty_boundary"]:
                self.assertEqual(item["value"], 0)
                self.assertEqual(item["request_count"], 0)

    def test_request_orientations(self):
        failures = request_orientation_failures(self.audit["requests"])
        self.assertEqual(failures, [])
        self.assertEqual(len(self.audit["requests"]), 648)
        self.assertEqual(self.stats["selected_rows"], 114048)
        self.assertEqual(self.stats["distinct_physical"], 32472)
        self.assertEqual(self.stats["nonzero_rows"], 10504)
        self.assertEqual(self.stats["distinct_nonzero_physical"], 3152)
        self.assertEqual(self.stats["nonzero_signed_requests"], 552)
        self.assertEqual(self.stats["physical_coefficient_conflicts"], 0)
        self.assertTrue(self.stats["all_coordinates_zero"])
        self.assertEqual(len(self.quotients), 24)
        self.assertEqual(permutation_sign((0, 1, 2, 3)), 1)
        self.assertEqual(permutation_sign((1, 3, 0, 2)), -1)
        self.assertEqual(permutation_sign((2, 3, 0, 1)), 1)
        self.assertEqual(tuple(SIGMA), (2, 3, 0, 1))

    def test_physical_binding_of_equal_arrays(self):
        pairs = equal_array_pairs(self.quotients)
        self.assertEqual(len(pairs), 12)
        for left, right in documented_duplicate_pairs():
            self.assertIn((left, right), pairs)
            self.assertTrue(bindings_distinct(self.quotients[left], self.quotients[right]))
            self.assertEqual(
                self.quotients[left].array_sha256,
                self.quotients[right].array_sha256,
            )
        failures, compared = covariance_failures(self.quotients, self.weights, pairs)
        self.assertEqual(failures, [])
        self.assertGreater(compared, 0)
        fixed = (2, 2, 2, 0)
        documented_rows = 0
        for left, _right in documented_duplicate_pairs():
            documented_rows += sum(
                1 for _ in iter_boundary(fixed, self.quotients[left], self.weights)
            )
        self.assertEqual(documented_rows, 1086)
        # Stated binding values for m=(2,2,2,0) and its image m=(2,0,2,2).
        # The third column is the partner at the unchanged target, which the
        # same-target identity incorrectly identifies with the first column.
        stated = {
            ((0, 1, 2, 3), (2, 3, 0, 1)): (Fraction(8655, 16), Fraction(131, 2)),
            ((0, 1, 3, 2), (2, 3, 1, 0)): (Fraction(-2817, 16), Fraction(-169, 2)),
            ((0, 2, 1, 3), (2, 0, 3, 1)): (Fraction(18831, 8), Fraction(42869, 16)),
            ((0, 2, 3, 1), (2, 0, 1, 3)): (Fraction(-21601, 8), Fraction(-41517, 16)),
            ((0, 3, 1, 2), (2, 1, 3, 0)): (Fraction(1457, 8), Fraction(21869, 16)),
            ((0, 3, 2, 1), (2, 1, 0, 3)): (Fraction(-803, 4), Fraction(-22917, 16)),
        }
        image = apply_sigma_tuple(fixed)
        for (left, right), (at_source, at_same_target) in stated.items():
            source = sum(
                (row.signed for *_, row in iter_boundary(fixed, self.quotients[left], self.weights)),
                Fraction(0),
            )
            partner_image = sum(
                (row.signed for *_, row in iter_boundary(image, self.quotients[right], self.weights)),
                Fraction(0),
            )
            partner_fixed = sum(
                (row.signed for *_, row in iter_boundary(fixed, self.quotients[right], self.weights)),
                Fraction(0),
            )
            self.assertEqual(source, at_source)
            self.assertEqual(partner_image, at_source)
            self.assertEqual(partner_fixed, at_same_target)

    def test_same_target_binding_identity_must_fail(self):
        """Precommitted failure.

        Equal role-relative arrays do not give equal signed selections at the
        unchanged target. For orientations 0123 and 2301 at m=(2,2,2,0), the
        check `signed contributions agree` must fail.
        """
        target = (2, 2, 2, 0)
        weights = self.weights
        left = self.quotients[(0, 1, 2, 3)]
        right = self.quotients[(2, 3, 0, 1)]
        self.assertEqual(
            tuple(sorted(left.coefficients.items())),
            tuple(sorted(right.coefficients.items())),
        )
        left_sum = sum(
            (row.signed for *_, row in iter_boundary(target, left, weights)),
            0,
        )
        right_sum = sum(
            (row.signed for *_, row in iter_boundary(target, right, weights)),
            0,
        )

        def signed_contributions_agree(first, second):
            return first == second

        self.assertFalse(signed_contributions_agree(left_sum, right_sum))
        image = apply_sigma_tuple(target)
        image_sum = sum(
            (row.signed for *_, row in iter_boundary(image, right, weights)),
            0,
        )
        self.assertEqual(left_sum, image_sum)
        self.assertNotEqual(image, target)

    def test_nonzero_sensitivity_perturbation_must_fail_equality(self):
        """Precommitted failure.

        Orientation 0123 at the unique target with d=8, L=22 and w=41 is
        m=(2,2,2,0). The corner slot (r, ell) = (8, 22) reads
        [T^0 z^0] G^(-70) = 1, and the permutation sign is +1.
        Adding 1 to that numerator must change coordinate 2 by exactly 1/64.
        Equality of the unperturbed and perturbed coordinate values must fail.

        Slots with kernel weight 0, and slots no target selects, are rejected
        as controls because they lie in the detector kernel.
        """
        roles = (0, 1, 2, 3)
        slot = (8, 41, 22)
        hits = []
        for index, target in monomials():
            for *_, row in iter_boundary(target, self.quotients[roles], self.weights):
                if (row.r, row.w, row.ell) == slot:
                    hits.append((index, row.sign, row.weight))
        self.assertEqual(hits, [(2, 1, 1)])
        predicted = sensitivity(sign=1, weight=1, numerator_delta=1)
        self.assertEqual(predicted, Fraction(1, 64))
        perturbed = perturb_numerator(self.quotients, roles, slot, 1)
        perturbed_audit = evaluate(perturbed, self.weights)
        original = self.audit["coordinates"][2]["value"]
        changed = perturbed_audit["coordinates"][2]["value"]

        def coordinate_values_agree(before, after):
            return before == after

        self.assertFalse(coordinate_values_agree(original, changed))
        self.assertEqual(changed - original, predicted)
        for index, item in enumerate(self.audit["coordinates"]):
            if index == 2:
                continue
            self.assertEqual(item["value"], perturbed_audit["coordinates"][index]["value"])

    def test_nonselected_numerator_edit_is_in_the_kernel(self):
        """Not a negative control: an unselected slot must not be used as one."""
        roles = (0, 1, 2, 3)
        slot = (4, 27, 22)
        self.assertIn(slot, self.quotients[roles].coefficients)
        hits = [
            row
            for request_target in (target for _, target in monomials())
            for *_, row in iter_boundary(request_target, self.quotients[roles], self.weights)
            if (row.r, row.w, row.ell) == slot
        ]
        self.assertEqual(hits, [])
        perturbed = evaluate(
            perturb_numerator(self.quotients, roles, slot, 1),
            self.weights,
        )
        for before, after in zip(self.audit["coordinates"], perturbed["coordinates"]):
            self.assertEqual(before["value"], after["value"])


if __name__ == "__main__":
    unittest.main()
