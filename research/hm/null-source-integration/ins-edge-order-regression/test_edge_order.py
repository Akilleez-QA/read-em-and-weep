"""Artificial-only regression; run with INS01 directory on PYTHONPATH."""
import unittest
from inserted_program import (
    Budget, FullOwner, PrismProgram, RegularExtensionWitness, SparseOracle,
    SyntheticFibers, SyntheticQuotients, WholeNumerator, ZERO,
)


class ArtificialSource:
    mode = 'synthetic'

    def degree_upper(self, owners, pair=(0, 1)):
        return ZERO

    def coefficient(self, owners, exponent, pair=(0, 1)):
        # SourceSlice supplies the source-first sorted tuple and external sign.
        return int(exponent == ZERO and
                   tuple(o.carrier for o in owners) == (2, 3, 4))


class EdgeOrderRegression(unittest.TestCase):
    def test_reversed_output_edge_must_be_rejected_or_alternated(self):
        budget = Budget()
        a = FullOwner(1, 'a', 1, 0, 8)
        b = FullOwner(1, 'b', 2, 0, 12)
        one = SparseOracle({ZERO: 1}, budget)
        zero = SparseOracle({}, budget)
        fibers = SyntheticFibers(1, {8: [(3, 0)], 12: [(4, 0)]})
        quotients = SyntheticQuotients({
            (3, 0, 8): {ZERO: 1},
            (4, 0, 12): {ZERO: 1},
        })

        def numerator(edge):
            witness = RegularExtensionWitness(
                'synthetic', 'artificial-whole-N',
                tuple(o.standard_tag for o in edge), edge,
                'artificial-constant-polynomial-domain',
            )
            prism = PrismProgram(
                edge, ArtificialSource(), quotients, fibers, one, ZERO,
                witness, budget, pair=(0, 1),
            )
            return WholeNumerator(zero, prism, one, (ZERO, ZERO))

        forward = numerator((a, b)).coefficient(ZERO)
        self.assertEqual(forward, -1)
        try:
            reverse = numerator((b, a)).coefficient(ZERO)
        except ValueError:
            return  # Explicit increasing-edge API restriction is a valid fix.
        self.assertEqual(reverse, -forward,
                         'Unsorted output accepted without alternating whole N')


if __name__ == '__main__':
    unittest.main()
