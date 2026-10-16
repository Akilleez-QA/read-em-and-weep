"""Abstract inference regressions only; no HM source or coefficient evaluation.

These models refute invalid implications, not the actual HM obstruction.
They are not wired into an admission path and make no physical resource claim.
"""
from fractions import Fraction as Q
from itertools import combinations
import unittest


def add(*vectors):
    return tuple(sum(xs, Q(0)) for xs in zip(*vectors))


def differential_one(t):
    return (Q(t[0]), Q(t[0]), Q(0))


def differential_two(r):
    return r[0] - r[1]


def detector(r):
    # H2 = ker D2 / im D1 is one-dimensional, detected by coordinate 2.
    return r[2]


def cech_delta(cochain, vertices, output_size):
    return {face: sum(((-1) ** j) * cochain.get(face[:j] + face[j + 1:], Q(0))
                      for j in range(output_size))
            for face in combinations(vertices, output_size)}


class CompleteRepresentativeGuards(unittest.TestCase):
    """Do not drop the B(F) and E(TF) correction blocks in equation (3)."""
    def test_abstract_complex_and_detector_are_valid(self):
        for t in ((1, 0), (0, 1), (3, -2)):
            boundary = differential_one(t)
            self.assertEqual(differential_two(boundary), 0)
            self.assertEqual(detector(boundary), 0)
        # Every closed (a,a,c) differs from (0,0,c) by a boundary.
        self.assertEqual(add((7, 7, 9), differential_one((-7, 0))), (0, 0, 9))

    def test_zero_baseline_does_not_make_correction_blocks_zero(self):
        baseline = (Q(0),) * 3
        nonzero_class = (Q(0), Q(0), Q(1))
        for block in ('B(F)', 'E(TF)'):
            with self.subTest(omitted_block=block):
                blocks = {'M0': baseline, 'B(F)': baseline, 'E(TF)': baseline}
                blocks[block] = nonzero_class
                complete = add(*blocks.values())
                self.assertEqual(differential_two(complete), 0)
                self.assertEqual(detector(baseline), 0)
                self.assertEqual(detector(complete), 1)
                incomplete = add(*(value for name, value in blocks.items() if name != block))
                self.assertEqual(detector(incomplete), 0)

    def test_nonzero_baseline_can_cancel_in_complete_representative(self):
        baseline = (Q(0), Q(0), Q(1))
        correction = (Q(0), Q(0), Q(-1))
        self.assertEqual(detector(baseline), 1)
        self.assertEqual(add(baseline, correction), (0, 0, 0))

    def test_only_sum_need_be_closed(self):
        baseline = (Q(1), Q(0), Q(0))
        correction = (Q(-1), Q(0), Q(1))
        self.assertNotEqual(differential_two(baseline), 0)
        self.assertNotEqual(differential_two(correction), 0)
        complete = add(baseline, correction)
        self.assertEqual(differential_two(complete), 0)
        self.assertEqual(detector(complete), 1)


class EvidencePromotionGuards(unittest.TestCase):
    """Local support and formal values are not authenticated class values."""
    def test_local_nonzero_closed_value_can_be_exact(self):
        vertices = (0, 1, 2, 3)
        edge = {(1, 2): Q(1)}
        exact = cech_delta(edge, vertices, 3)
        self.assertEqual(exact[(0, 1, 2)], 1)
        self.assertEqual(exact[(1, 2, 3)], 1)
        self.assertEqual(cech_delta(exact, vertices, 4), {vertices: 0})
        # It is globally exact by construction, despite two nonzero local values.
        # A local coordinate is not a cohomological detector: it misses cancellation.
        self.assertEqual(exact[(1, 2, 3)] - exact[(0, 2, 3)]
                         + exact[(0, 1, 3)] - exact[(0, 1, 2)], 0)

    def test_support_overlap_does_not_certify_coefficient(self):
        # Both summands have exponent 2 in their support; sum is zero.
        summands = ({2: Q(1)}, {2: Q(-1)})
        envelope = set().union(*(set(p) for p in summands))
        self.assertIn(2, envelope)
        self.assertEqual(sum(p.get(2, 0) for p in summands), 0)

    def test_formal_nonzero_does_not_survive_unverified_specialization(self):
        # Formal coefficient t is nonzero in Q[t]; at t=0 it vanishes.
        formal = {1: Q(1)}
        self.assertTrue(formal)
        specialize = lambda t: sum(c * t ** degree for degree, c in formal.items())
        self.assertEqual(specialize(Q(0)), 0)
        self.assertEqual(specialize(Q(1)), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
