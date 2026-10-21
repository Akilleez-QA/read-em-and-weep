"""Small synthetic examples only: no HM/source numerical fixtures."""
import unittest
from dataclasses import replace
from fractions import Fraction
from q4_compression import Matrix as M, compress, inverse, rank, hstack


def add(a, b):
    if (a.rows, a.cols) != (b.rows, b.cols):
        raise ValueError('Shape mismatch')
    return M(a.rows, a.cols, tuple(tuple(x+y for x, y in zip(ar, br))
                                 for ar, br in zip(a.data, b.data)))


class ToyCompressionTests(unittest.TestCase):
    def test_rank_drop(self):
        l = M.of([[1], [0], [0]])
        v = M.of([[1], [0], [0]])
        for t, expected in [(0, 1), (1, 0), (Fraction(2, 3), 0)]:
            u = M.of([[1, 0, 0], [0, 1, 0], [0, 0, t]])
            c = compress(u, v, l)
            self.assertTrue(c.verify())
            self.assertEqual(c.dimensions['paired_cokernel'], expected)
            self.assertEqual(c.dimensions['intermediate_target'], 2)

    def test_non_split_lift_cancellation(self):
        # L3=<e1>; primary target=<e1>. Both residual maps hit e2.
        # u(e2)=e2 while v(1)=e1+e2. Their difference supplies primary e1.
        # Ignoring the cubic's off-diagonal lift would leave a cokernel.
        l = M.of([[1], [0]])
        u = M.of([[0, 0], [0, 1]])
        actual = compress(u, M.of([[1], [1]]), l)
        discarded_lift = compress(u, M.of([[0], [1]]), l)
        self.assertEqual(actual.dimensions['paired_cokernel'], 0)
        self.assertEqual(discarded_lift.dimensions['paired_cokernel'], 1)
        self.assertEqual(actual.induced, M.of([[-1]]))
        self.assertTrue(actual.verify())

    def test_representative_independence(self):
        u = M.of([[1, 2, 3], [0, 1, 4], [1, 0, 2], [2, 1, 0]])
        v = M.of([[0], [1], [0], [1]])
        l = M.of([[1], [1], [0]])
        c = compress(u, v, l)
        n, p = c.residual_source, c.target.projection
        for b in [M.of([[2, -3]]), M.of([['1/2', '2/7']])]:
            changed = add(n.section, l @ b)
            self.assertEqual(n.projection @ changed, M.identity(n.projection.rows))
            self.assertEqual(p @ u @ changed, c.induced)
        # Raw row transform on ALL [v,uL,uJ] columns, not only pivot subset.
        allcols = hstack(v, u @ l, u @ n.section)
        reduced = c.row_transform @ allcols
        self.assertEqual(reduced.row_slice(c.target.relation_basis.cols, u.rows),
                         hstack(M.zero(c.induced.rows, v.cols+l.cols), c.induced))
        self.assertEqual(c.row_transform @ c.pivot_augmented, c.reduced_pivot_block)

    def test_all_base_changes_with_commuting_certificates(self):
        u = M.of([[1, 2, 3], [0, 1, 4], [1, 0, 2], [1, 3, 7]])
        v = M.of([[1, 2], [2, 4], [1, 2], [3, 6]])
        l = M.of([[1], [1], [0]])
        a = M.of([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 2, 1], [0, 0, 0, 1]])
        b = M.of([[1, 2, 0], [0, 1, 1], [0, 0, 1]])
        e = M.of([[2, 1], [1, 1]])
        f = M.of([[3]])
        c = compress(u, v, l)
        changed = compress(a @ u @ inverse(b), a @ v @ inverse(e),
                           b @ l @ inverse(f))
        # Explicit induced isomorphisms in residual source and D coordinates.
        sn, tn = c.residual_source, changed.residual_source
        sd, td = c.target, changed.target
        fn = tn.projection @ b @ sn.section
        fd = td.projection @ a @ sd.section
        fn_inv = sn.projection @ inverse(b) @ tn.section
        fd_inv = sd.projection @ inverse(a) @ td.section
        self.assertEqual(fn @ sn.projection, tn.projection @ b)
        self.assertEqual(fd @ sd.projection, td.projection @ a)
        self.assertEqual(fd @ c.induced, changed.induced @ fn)
        self.assertEqual(fn_inv @ fn, M.identity(fn.cols))
        self.assertEqual(fn @ fn_inv, M.identity(fn.rows))
        self.assertEqual(fd_inv @ fd, M.identity(fd.cols))
        self.assertEqual(fd @ fd_inv, M.identity(fd.rows))
        # Also the full paired cokernel coordinate isomorphism.
        self.assertEqual(c.dimensions['paired_cokernel'], 1)
        old, new = c.full_cokernel, changed.full_cokernel
        iso = new.projection @ a @ old.section
        back = old.projection @ inverse(a) @ new.section
        self.assertEqual(iso @ old.projection, new.projection @ a)
        self.assertEqual(back @ iso, M.identity(iso.cols))
        self.assertEqual(iso @ back, M.identity(iso.rows))

    def test_zero_and_extreme_dimensions(self):
        for m, n, k, ell in [(0, 0, 0, 0), (0, 2, 3, 2),
                             (3, 0, 0, 0), (3, 2, 0, 0), (3, 2, 0, 2)]:
            l = M.identity(n).columns(range(ell))
            c = compress(M.zero(m, n), M.zero(m, k), l)
            self.assertTrue(c.verify())
            self.assertEqual(c.dimensions['paired_cokernel'], m)
        c = compress(M.identity(3), M.zero(3, 0), M.identity(3))
        self.assertEqual(c.induced, M.zero(0, 0))

    def test_invalid_inputs_and_tampering(self):
        with self.assertRaises(TypeError):
            M.of([[0.1]])
        with self.assertRaises(ValueError):
            compress(M.identity(2), M.zero(3, 1), M.zero(2, 0))
        with self.assertRaises(ValueError):
            compress(M.identity(2), M.zero(2, 0), M.zero(2, 1))
        c = compress(M.identity(2), M.zero(2, 0), M.zero(2, 0))
        self.assertFalse(replace(c, induced=M.zero(2, 2)).verify())


if __name__ == '__main__':
    unittest.main(verbosity=2)
