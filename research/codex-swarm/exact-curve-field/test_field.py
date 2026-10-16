"""Artificial inputs only. No source programs, JSON, model, or catalog imports."""
import unittest
from dataclasses import FrozenInstanceError
from fractions import Fraction as F
from field import (Execution, Limits, LimitExceeded, NotLaurentPolynomial,
                   UnsupportedInverse)


class ArtificialFieldTests(unittest.TestCase):
    def setUp(self):
        self.e = Execution()
        self.one = self.e.scalar(1)
        self.x = [self.e.x(i) for i in range(4)]
        self.y = [self.e.y(i) for i in range(4)]

    def test_curve_and_derivation(self):
        for i in range(4):
            x, y = self.x[i], self.y[i]
            relation = y*y - x*x*x + x
            self.assertTrue(relation.is_zero())
            self.assertTrue(relation.V(i).is_zero())
            # Non-vacuous check: differentiate both sides before subtracting.
            self.assertEqual((y*y).V(i), (x*x*x-x).V(i))
            self.assertEqual(x.V(i), y)
            self.assertEqual(y.V(i), (self.e.scalar(3)*x*x-self.one)/self.e.scalar(2))

    def test_leibniz_moving_frame(self):
        a = (self.x[0]+self.y[1]) / self.x[2]
        b = self.y[0]*self.y[2] + self.x[1]
        for i in range(4):
            self.assertEqual((a*b).V(i), a.V(i)*b+a*b.V(i))

    def test_distinct_derivations_commute(self):
        a = (self.x[0]*self.y[1] + self.y[0]*self.x[1])/self.x[2]
        for i, j in ((0, 1), (0, 2), (1, 3)):
            self.assertEqual(a.V(i).V(j), a.V(j).V(i))

    def test_artificial_nu_inverse(self):
        # Local artificial nu: deliberately not a source-specific field object.
        nu = self.e.scalar(F(7, 3))*self.x[0]*self.y[1]*self.y[3]
        self.assertEqual(nu*nu.inverse(), self.one)
        self.assertEqual(nu.inverse()*nu, self.one)
        self.assertEqual(self.x[2]/self.x[2], self.one)
        self.assertEqual(self.y[0]/self.y[0], self.one)

    def test_all_basis_products_and_inverses(self):
        for mask in range(16):
            a = self.e.element(((mask, self.e.rational(F(2, 5))),))
            self.assertEqual(a*a.inverse(), self.one)
            for other in range(16):
                b = self.e.element(((other, self.e.rational(1)),))
                expected = self.e.rational(F(2, 5))
                for i in range(4):
                    if mask & other & (1 << i):
                        expected = expected*self.e.rational(self.e.curve(i))
                self.assertEqual(a*b, self.e.element(((mask ^ other, expected),)))

    def test_mixed_jets(self):
        a = self.x[0]*self.x[1]
        self.assertEqual(a.jet([0, 1]), self.y[0]*self.y[1])
        self.assertEqual(a.jet([0, 1, 0]), self.y[0].V(0)*self.y[1])
        self.assertEqual(a.jet([0, 1, 0]), a.jet([1, 0, 0]))
        self.assertEqual(self.x[0].jet([0, 0, 0]), self.e.scalar(3)*self.x[0]*self.y[0])

    def test_quotient_derivative(self):
        r = self.x[0]/self.x[1]
        expected = self.y[0]/self.x[1]
        self.assertEqual(r.V(0), expected)
        self.assertEqual(r.V(1), -(self.x[0]*self.y[1]/(self.x[1]*self.x[1])))
        reciprocal = self.x[0].inverse()
        self.assertEqual(reciprocal.V(0), -(self.y[0]/(self.x[0]*self.x[0])))

    def test_exact_multivariate_cancel(self):
        e = self.e
        x, z = e.xpoly(0), e.xpoly(1)
        d = x+z+e.constant(1)
        q = x*x+z.scale(F(2, 3))+e.constant(-5)
        monomial = x*x*z
        r = e.rational(d*q, monomial*d)
        self.assertEqual(r.laurent_coefficient((0, -1, 0, 0)), F(1))
        self.assertEqual(r.laurent_coefficient((-2, 0, 0, 0)), F(2, 3))
        self.assertEqual(r.laurent_coefficient((-2, -1, 0, 0)), F(-5))
        self.assertEqual(r.laurent_coefficient((99, 99, 0, 0)), F(0))
        quotient, remainder = (d*q).divide(d)
        self.assertEqual(quotient, q)
        self.assertTrue(remainder.is_zero())

    def test_bad_quotient_never_support_zero(self):
        x, z = self.e.xpoly(0), self.e.xpoly(1)
        for numerator, denominator in ((self.e.constant(1), x+z), (x, x+z),
                                       (x*x+z, x+z+self.e.constant(1))):
            r = self.e.rational(numerator, denominator)
            for target in ((0, 0, 0, 0), (999, 999, 999, 999), (-999, 0, 0, 0)):
                with self.assertRaises(NotLaurentPolynomial):
                    r.laurent_coefficient(target)

    def test_zero_and_validation(self):
        z = self.e.scalar(0)
        self.assertEqual(z.laurent_coefficient((-1, 0, 0, 0)), F(0))
        self.assertTrue((self.y[0]-self.y[0]).is_zero())
        for denominator in (z, self.e.scalar(self.e.rational(0))):
            with self.assertRaises(ZeroDivisionError):
                denominator.inverse()
        with self.assertRaises(ZeroDivisionError):
            self.e.rational(1, 0)
        with self.assertRaises(UnsupportedInverse):
            (self.y[0]+self.y[1]).inverse()
        with self.assertRaises(ValueError):
            self.y[0].laurent_coefficient((0, 0, 0, 0))
        with self.assertRaises(TypeError):
            self.e.scalar(0.5)
        with self.assertRaises(ValueError):
            self.e.poly((((-1, 0, 0, 0), 1),))
        with self.assertRaises(ValueError):
            self.x[0].V(4)

    def test_immutable_and_cross_execution(self):
        p = self.e.xpoly(0)
        with self.assertRaises(FrozenInstanceError):
            p.terms = ()
        with self.assertRaises(FrozenInstanceError):
            self.x[0].terms = ()
        with self.assertRaises(FrozenInstanceError):
            self.x[0].terms[0][1].denominator = p
        with self.assertRaises(TypeError):
            self.e.counts['products'] = 0
        with self.assertRaises(ValueError):
            self.x[0]+Execution().x(0)

    def test_shared_counter(self):
        e = Execution(Limits(products=2))
        a, b = e.constant(2), e.constant(3)
        a*b
        self.assertEqual(e.counts['products'], 1)
        c = e.constant(7)
        b*c
        self.assertEqual(e.counts['products'], 2)
        with self.assertRaises(LimitExceeded):
            a*c
        with self.assertRaises(LimitExceeded):
            b.is_zero()
        with self.assertRaises(LimitExceeded):
            e.constant(0)

    def test_tiny_storage_step_and_bit_caps(self):
        for limits, value in ((Limits(storage_events=0), 1),
                              (Limits(steps=0), 1),
                              (Limits(bit_height=3), 8),
                              (Limits(bit_height=3), F(1, 8))):
            e = Execution(limits)
            with self.assertRaises(LimitExceeded):
                e.constant(value)
            with self.assertRaises(LimitExceeded):
                e.constant(0)
        e = Execution(Limits(bit_height=3))
        with self.assertRaises(LimitExceeded):
            e.poly(((((8, 0, 0, 0)), 1),))
        e = Execution(Limits(bit_height=4))
        a = e.constant(7)
        with self.assertRaises(LimitExceeded):
            a*a


if __name__ == '__main__':
    unittest.main(verbosity=2)
