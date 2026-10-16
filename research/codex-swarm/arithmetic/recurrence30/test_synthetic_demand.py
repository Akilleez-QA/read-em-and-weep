"""Tiny colored-token INTEGER metadata control, unrelated to physical polynomials."""
from math import comb, factorial
from itertools import product
import unittest
import seed30_partition_demand as contract


class Controls(unittest.TestCase):
    def test_divided_power_diagonal(self):
        # Synthetic two-color tokens; T=2,L=3. Only (0,3),(1,2) admitted.
        # Token degree is n0 + 2*(n1-T); no physical coordinate is used.
        L, T = 3, 2
        states = {(0, 0): 1}
        for i in range(2):
            nxt = {}
            for ell in range(L + 1):
                for n in (range(T) if i == 0 else range(T, L + 1)):
                    if n > ell:
                        continue
                    degree = n if i == 0 else 2 * (n - T)
                    for (previous, alpha), count in states.items():
                        if previous == ell - n:
                            key = (ell, alpha + degree)
                            nxt[key] = nxt.get(key, 0) + comb(ell, n) * count
            states = nxt
        diagonal = {alpha: count for (ell, alpha), count in states.items() if ell == L}
        direct = {}
        for a, b in product(range(T), range(T, L + 1)):
            if a + b == L:
                degree = a + 2 * (b - T)
                direct[degree] = direct.get(degree, 0) + factorial(L) // (factorial(a) * factorial(b))
        self.assertEqual(diagonal, direct)
        self.assertEqual(diagonal, {2: 1, 1: 3})

    def test_fixed_metadata_and_closed_gates(self):
        c = contract.build()
        self.assertEqual([p['s'] for p in c['partitions']], [0, 1, 2, 3, 4])
        self.assertEqual([p['L'] for p in c['partitions']], [535, 1069, 1603, 2137, 2671])
        self.assertEqual(c['partitions'][-1]['B_s_special_case'], '1')
        self.assertFalse(any(c['gates'].values()))
        self.assertEqual(len(c['prefix_kernel']['block_denominator_occurrences']), 6)
        with self.assertRaises(TypeError):
            contract.build(unsupported_field=True)


if __name__ == '__main__':
    unittest.main()
