"""RF-R: tiny synthetic inputs only; no source/model imports or calls.

Standalone invocation bounds both normal and -O producer/independent children.
RF-R-1 was repaired; the former expected-failure regression must now pass.
"""
import os
from pathlib import Path
import resource
import subprocess
import sys
import unittest
from dataclasses import FrozenInstanceError
from fractions import Fraction as F
from field import Execution, Limits, LimitExceeded, NotLaurentPolynomial, UnsupportedInverse

Z = (0, 0, 0, 0)


def evaluate_poly(p, point):
    return sum((c * product(F(v)**n for v, n in zip(point, power))
                for power, c in p.terms), F(0))


def product(values):
    r = F(1)
    for value in values:
        r *= value
    return r


def evaluate_element(a, point):
    return {m: evaluate_poly(c.numerator, point) / evaluate_poly(c.denominator, point)
            for m, c in a.terms
            if evaluate_poly(c.numerator, point)}


def oracle_V(terms, axis):
    """Differentiate unreduced eight-variable Laurent monomials.

    Negative y powers are allowed. No kernel derivatives or basis multiplication
    are used. Reduction occurs only at the evaluation boundary below.
    """
    out = {}
    def add(power, coefficient):
        key = tuple(power)
        out[key] = out.get(key, F(0)) + coefficient
    for power, coefficient in terms.items():
        a, b = power[axis], power[axis+4]
        if a:
            q = list(power); q[axis] -= 1; q[axis+4] += 1
            add(q, coefficient*a)
        if b:
            q = list(power); q[axis+4] -= 1
            add(q, -coefficient*b/2)
            q[axis] += 2
            add(q, coefficient*b*F(3, 2))
    return {p: c for p, c in out.items() if c}


def oracle_at(terms, point):
    out = {}
    for power, c in terms.items():
        c *= product(F(x)**a for x, a in zip(point, power[:4]))
        mask = 0
        for i, b in enumerate(power[4:]):
            n, odd = divmod(b, 2)
            c *= F(point[i]**3-point[i])**n
            mask += odd * 2**i
        out[mask] = out.get(mask, F(0)) + c
    return {m: c for m, c in out.items() if c}


class IndependentTests(unittest.TestCase):
    def test_sparse_fraction_convolution_oracle(self):
        e = Execution()
        # Explicit hand expansion, including duplicate cancellation in input.
        p = e.poly([((1,0,0,0), F(2,3)), (Z, F(-5,7)), (Z, 1), (Z, -1)])
        q = e.poly({(0,1,0,0): F(3,2), Z: F(7,5)})
        self.assertEqual(dict((p*q).terms), {
            (1,1,0,0): F(1), (1,0,0,0): F(14,15),
            (0,1,0,0): F(-15,14), Z: F(-1)})
        self.assertEqual(dict(p.partial(0).terms), {Z: F(2,3)})
        self.assertTrue((p-p).is_zero())

    def test_rational_normalization_and_nonstructural_equality(self):
        e = Execution(); x = e.xpoly(0); one = e.constant(1)
        a = e.rational(x+one, (x-one).scale(-3))
        self.assertEqual(a.denominator.terms[-1][1], F(1))
        b = e.rational((x+one)*(x+one), ((x-one)*(x+one)).scale(-3))
        self.assertNotEqual(a.numerator.terms, b.numerator.terms)
        self.assertEqual(a, b)
        self.assertTrue((a-b).is_zero())
        self.assertEqual(e.rational(e.poly(), x).denominator, one)
        self.assertEqual(e.rational(x, -2).numerator, x.scale(F(-1,2)))

    def test_full_lex_remainder_oracle(self):
        e = Execution(); x, z = e.xpoly(0), e.xpoly(1)
        # x^2+z divided by x+z: q=x-z, r=z^2+z.
        q, r = (x*x+z).divide(x+z)
        self.assertEqual(dict(q.terms), {(1,0,0,0): F(1), (0,1,0,0): F(-1)})
        self.assertEqual(dict(r.terms), {(0,2,0,0): F(1), (0,1,0,0): F(1)})
        # Leading term first goes to remainder, but division must continue.
        q, r = (x+z*z).divide(z)
        self.assertEqual(q, z); self.assertEqual(r, x)

    def test_weighted_cancellation_one_final_division(self):
        e = Execution(); x, z, w, t = [e.xpoly(i) for i in range(4)]
        d = x+z+w+t+e.constant(1)
        monomial = x*z*z*t
        # Weighted numerators 2*A-3*B=d*Q; neither term is Laurent alone.
        target = x*w.scale(F(5,7))+t.scale(-2)+e.constant(F(3,11))
        a = x*x+z+e.constant(4)
        b = (a.scale(2)-d*target).scale(F(1,3))
        for n in (a, b):
            with self.assertRaises(NotLaurentPolynomial):
                e.rational(n, monomial*d).laurent_coefficient((200,0,0,0))
        total = e.rational(a.scale(2)-b.scale(3), monomial*d)
        expected = {(0,-2,1,-1): F(5,7), (-1,-2,0,0): F(-2),
                    (-1,-2,0,-1): F(3,11), (200,0,0,0): F(0)}
        for power, coefficient in expected.items():
            self.assertEqual(total.laurent_coefficient(power), coefficient)
        for power in (Z, (200,0,0,0), (-200,0,0,0)):
            with self.assertRaises(NotLaurentPolynomial):
                e.rational(d*target+e.constant(1), monomial*d).laurent_coefficient(power)

    def test_basis_products_unreduced_power_oracle(self):
        e = Execution(); point = (2,3,5,7)
        for a in range(16):
            for b in range(16):
                power = (0,)*4 + tuple(((a >> i)&1)+((b >> i)&1) for i in range(4))
                actual = e.element({a: e.rational(F(-2,7))}) * e.element({b: e.rational(F(3,5))})
                self.assertEqual(evaluate_element(actual, point), oracle_at({power: F(-6,35)}, point))

    def test_moving_nu_and_mixed_derivatives_external_oracle(self):
        e = Execution(); x = [e.x(i) for i in range(4)]; y = [e.y(i) for i in range(4)]
        # Artificial nu has two moving y factors; its reciprocal has negative
        # unreduced y powers in the independent oracle.
        nu = e.scalar(F(4,9))*x[0]*x[2]*y[1]*y[3]
        a = nu.inverse()
        oracle = {(-1,0,-1,0,0,-1,0,-1): F(9,4)}
        for axis in (1,3):
            a = a.V(axis); oracle = oracle_V(oracle, axis)
            for point in ((2,3,5,7), (3,2,7,5)):
                self.assertEqual(evaluate_element(a, point), oracle_at(oracle, point))
        self.assertEqual(nu.inverse().jet([1,3]), nu.inverse().jet([3,1]))
        f = x[0]*y[1]+y[0]*x[1]
        self.assertEqual((f*nu).V(1), f.V(1)*nu+f*nu.V(1))

    def test_repeated_moving_frame_derivative_oracle(self):
        e = Execution(); x, y = e.x(0), e.y(0)
        actual = x*x*y
        oracle = {(2,0,0,0,1,0,0,0): F(1)}
        for _ in range(3):
            actual = actual.V(0); oracle = oracle_V(oracle, 0)
            for point in ((2,3,5,7), (3,2,7,5)):
                self.assertEqual(evaluate_element(actual, point), oracle_at(oracle, point))

    def test_nonmonomial_rational_partial_closed_formula(self):
        e = Execution(); x, z = e.xpoly(0), e.xpoly(1)
        r = e.rational(x*z+e.constant(1), x+z+e.constant(2))
        for i in (0,1):
            derivative = r.partial(i)
            for point in ((2,3,5,7), (3,2,7,5)):
                a, b = point[:2]
                slope = b if i == 0 else a
                expected = F(slope*(a+b+2)-(a*b+1), (a+b+2)**2)
                self.assertEqual(evaluate_poly(derivative.numerator, point) /
                                 evaluate_poly(derivative.denominator, point), expected)

    def test_single_basis_inverse_denominator_shapes(self):
        e = Execution(); x = [e.xpoly(i) for i in range(4)]
        coeff = e.rational((x[0]+x[1]).scale(F(7,3)), x[2]*x[3]+e.constant(2))
        for mask in (0, 1, 5, 10, 15):
            a = e.element({mask: coeff})
            self.assertEqual(a*a.inverse(), e.scalar(1))
        with self.assertRaises(UnsupportedInverse):
            (e.scalar(1)+e.y(0)).inverse()
        with self.assertRaises(ZeroDivisionError):
            e.element().inverse()
        with self.assertRaises(ValueError):
            e.y(0).laurent_coefficient((999,0,0,0))

    def test_frozen_and_shared_meter_poison(self):
        e = Execution(Limits(products=30)); p = e.constant(2); r = e.rational(3); a = e.scalar(4)
        for obj, attr, value in ((p,'terms',()), (r,'denominator',p), (a,'terms',()), (e.limits,'steps',0)):
            with self.assertRaises(FrozenInstanceError):
                setattr(obj, attr, value)
        snapshot = e.counts
        with self.assertRaises(TypeError):
            snapshot['products'] = 0
        before = snapshot['products']; p*p
        self.assertEqual(e.counts['products'], before+1)
        self.assertEqual(snapshot['products'], before)
        with self.assertRaises(LimitExceeded):
            for _ in range(31):
                p*p
        for operation in (p.is_zero, r.is_zero, a.is_zero, lambda: p == p,
                          lambda: r == r, lambda: a == a, lambda: a.jet([]),
                          lambda: e.poly(), lambda: e.rational(p,p), lambda: r.inverse()):
            with self.assertRaises(LimitExceeded):
                operation()

    def test_limits_on_arithmetic_not_just_input(self):
        for limits, build, operation in (
            (Limits(bit_height=3), lambda e: e.constant(F(1,7)), lambda a: a*a),
            (Limits(bit_height=3), lambda e: e.poly({(7,0,0,0):1}), lambda a: a*a),
            (Limits(products=0), lambda e: e.xpoly(0), lambda a: a.partial(0)),
        ):
            e = Execution(limits); a = build(e)
            with self.assertRaises(LimitExceeded):
                operation(a)
            with self.assertRaises(LimitExceeded):
                a.is_zero()
        for limits in (Limits(steps=0), Limits(storage_events=0)):
            with self.assertRaises(LimitExceeded):
                Execution(limits).constant(1)

    def test_foreign_polynomial_pair_constructor_must_reject(self):
        owner, receiver = Execution(), Execution(Limits(products=0))
        p = owner.constant(2); q = owner.constant(3)
        # BUG RF-R-1: succeeds, uses owner's meter, ignores receiver entirely.
        with self.assertRaises(ValueError):
            receiver.rational(p, q)

    def test_cross_context_arithmetic_and_other_constructors_reject(self):
        a, b = Execution(), Execution()
        p, q = a.constant(2), b.constant(3)
        with self.assertRaises(ValueError):
            p*q
        with self.assertRaises(ValueError):
            b.scalar(a.rational(1))
        with self.assertRaises(ValueError):
            b.rational(p)


def bounds():
    resource.setrlimit(resource.RLIMIT_AS, (768*1024*1024,)*2)
    resource.setrlimit(resource.RLIMIT_CPU, (59,)*2)
    resource.setrlimit(resource.RLIMIT_CORE, (0,0))


if __name__ == '__main__':
    if '--child' in sys.argv:
        sys.argv.remove('--child')
        unittest.main(verbosity=2)
    else:
        here = Path(__file__).resolve().parent
        for optimized in (False, True):
            for script, args in (('test_field.py', []), ('test_independent.py', ['--child'])):
                command = [sys.executable, '-B'] + (['-O'] if optimized else []) + [script] + args
                print('RUN', ' '.join(command), flush=True)
                try:
                    result = subprocess.run(command, cwd=here, preexec_fn=bounds,
                        env={**os.environ, 'PYTHONDONTWRITEBYTECODE':'1'}, timeout=60)
                except subprocess.TimeoutExpired:
                    sys.exit(124)
                if result.returncode:
                    sys.exit(result.returncode)
