"""Synthetic constructor-only controls for the repaired common-edge guard."""
import unittest
from inserted_program import (
    Budget, FullOwner, PrismProgram, RegularExtensionWitness, SparseOracle,
    SyntheticFibers, SyntheticQuotients, ZERO,
)


class GuardScope(unittest.TestCase):
    def make(self, a, b):
        budget = Budget()
        one = SparseOracle({ZERO: 1}, budget)
        witness = RegularExtensionWitness(
            'synthetic', 'toy', (a.standard_tag, b.standard_tag),
            (a, b), 'artificial-domain',
        )
        return PrismProgram(
            (a, b), one, SyntheticQuotients({}), SyntheticFibers(1, {}),
            one, ZERO, witness, budget,
        )

    def test_equal_physical_labels_distinct_increasing_tags_accepted(self):
        a = FullOwner(1, 'a', 2, 3, 8)
        b = FullOwner(1, 'b', 2, 3, 12)
        self.assertEqual(a.physical_key, b.physical_key)
        self.assertNotEqual(a.common_key, b.common_key)
        self.assertEqual(self.make(a, b).edge, (a, b))
        with self.assertRaisesRegex(ValueError, 'increasing source-first common edge'):
            self.make(b, a)

    def test_same_common_label_different_occurrence_rejected(self):
        a = FullOwner(1, 'a', 2, 3, 8)
        b = FullOwner(1, 'b', 2, 3, 8)
        with self.assertRaisesRegex(ValueError, 'increasing source-first common edge'):
            self.make(a, b)

    def test_auxiliary_first_order_is_used(self):
        a = FullOwner(1, 'a', 5, 15, 15)
        b = FullOwner(1, 'b', 0, 0, 0)
        self.assertEqual(self.make(a, b).edge, (a, b))
        with self.assertRaisesRegex(ValueError, 'increasing source-first common edge'):
            self.make(b, a)


if __name__ == '__main__':
    unittest.main()
