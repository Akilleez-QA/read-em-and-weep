#!/usr/bin/env python3
"""Universal synthetic HPL regressions over Q; no physical/source data or I/O.

Run: python transfer_regression.py (also python -O transfer_regression.py).
Negative controls: --mutant plus-series | naive-projection | omit-HR.
The checks deliberately do not use Python assert, so optimization cannot erase them.
All matrices are represented as column maps on named, bigraded basis vectors.
"""
from fractions import Fraction as F
import argparse
import sys


class RegressionFailure(Exception):
    pass


CHECKS = 0


def check(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RegressionFailure(label)


def vec(**entries):
    return {k: F(v) for k, v in entries.items() if v}


def add(*vectors):
    out = {}
    for v in vectors:
        for k, a in v.items():
            out[k] = out.get(k, F(0)) + a
    return {k: a for k, a in out.items() if a}


def scale(a, v):
    return {k: F(a) * b for k, b in v.items() if a * b}


def basis(k):
    return {k: F(1)}


def linear(columns):
    return lambda v: add(*(scale(a, columns.get(k, {})) for k, a in v.items()))


class Example:
    def __init__(self, height, unit=False):
        self.height = height
        # x_j has total degree one; y_j has total degree two.
        self.grades = {f'x{j}': (height-j, 1-height+j)
                       for j in range(height+1)}
        self.grades.update({f'y{j}': (height-j+1, 1-height+j)
                            for j in range(1, height+2)})
        # A lower-row arrow, a following separate arrow, and a retained class.
        self.grades.update(v=(0, 1), w=(0, 2), s=(0, 2), t=(0, 3), c=(0, 2))
        # Contractible square with NONZERO anticommuting composites.
        self.grades.update(a=(0, 0), b=(1, 0), e=(0, 1), f=(1, 1))
        weights = [F(2, 3), F(-3, 5), F(5, 7), F(7, 11), F(11, 13)]
        self.weights = [F(1)] * (height+1) if unit else weights[:height+1]
        dc = {f'x{j}': basis(f'y{j}') for j in range(1, height+1)}
        dc.update(a=basis('b'), e=basis('f'))
        hc = {f'y{j}': basis(f'x{j}') for j in range(1, height+1)}
        hc.update(b=basis('a'), f=basis('e'))
        tc = {f'x{j}': scale(self.weights[j], basis(f'y{j+1}'))
              for j in range(height+1)}
        tc.update(v=scale(F(3, 2), basis('w')), s=scale(F(-2, 3), basis('t')),
                  a=basis('e'), b=scale(-1, basis('f')))
        self.delta, self.h, self.pert = linear(dc), linear(hc), linear(tc)
        self.K = ['x0', f'y{height+1}', 'v', 'w', 's', 't', 'c']
        self.i = linear({k: basis(k) for k in self.K})
        self.p = self.i
        self.D = lambda v: add(self.delta(v), self.pert(v))

    def inverse(self, op, v, sign=-1):
        # Exactly bounded by the Cech height. Also check termination instead
        # of silently relying on this bound; square components have height 1.
        term, result = v, {}
        for j in range(max(self.height, 1)+1):
            result = add(result, scale(sign**j, term))
            term = op(term)
        check(not term, 'finite series terminates')
        return result

    def I(self, v, sign=-1):
        return self.inverse(lambda z: self.h(self.pert(z)), self.i(v), sign)

    def P(self, v, sign=-1):
        return self.p(self.inverse(lambda z: self.pert(self.h(z)), v, sign))

    def H(self, v, sign=-1):
        return self.h(self.inverse(lambda z: self.pert(self.h(z)), v, sign))

    def dK(self, v, sign=-1):
        return self.p(self.pert(self.I(v, sign)))


def test_example(ex):
    for name, op, shift in [('delta', ex.delta, (1, 0)), ('Delta', ex.pert, (0, 1)),
                            ('h', ex.h, (-1, 0))]:
        for k, grade in ex.grades.items():
            for target in op(basis(k)):
                check(ex.grades[target] == tuple(a+b for a, b in zip(grade, shift)),
                      f'{name} has stated bidegree on {k}')
    for k in ex.grades:
        v = basis(k)
        check(not ex.delta(ex.delta(v)), 'delta squared')
        check(not ex.pert(ex.pert(v)), 'Delta squared')
        check(not add(ex.delta(ex.pert(v)), ex.pert(ex.delta(v))), 'anticommutation')
        check(not ex.D(ex.D(v)), 'D squared')
        check(add(ex.delta(ex.h(v)), ex.h(ex.delta(v))) == add(v, scale(-1, ex.i(ex.p(v)))),
              'unperturbed SDR homotopy')
        check(not ex.h(ex.h(v)), 'h squared')
        check(not ex.p(ex.h(v)), 'p h')
        check(ex.P(ex.D(v)) == ex.dK(ex.P(v)), 'P chain map')
        check(add(ex.D(ex.H(v)), ex.H(ex.D(v))) == add(v, scale(-1, ex.I(ex.P(v)))),
              'perturbed SDR homotopy')
        check(not ex.H(ex.H(v)), 'H squared')
        check(not ex.P(ex.H(v)), 'P H')
    for k in ex.K:
        v = basis(k)
        check(ex.p(ex.i(v)) == v, 'p i identity')
        check(not ex.h(ex.i(v)), 'h i')
        check(ex.D(ex.I(v)) == ex.I(ex.dK(v)), 'I chain map')
        check(ex.P(ex.I(v)) == v, 'P I identity')
        check(not ex.dK(ex.dK(v)), 'dK squared')
        check(not ex.H(ex.I(v)), 'H I')
    check(ex.delta(ex.pert(basis('a'))) == basis('f'), 'nonzero square composite +f')
    check(ex.pert(ex.delta(basis('a'))) == scale(-1, basis('f')), 'nonzero square composite -f')
    check(ex.dK(basis('v')) == scale(F(3, 2), basis('w')), 'nonzero lower differential')
    check(ex.dK(basis('s')) == scale(F(-2, 3), basis('t')), 'nonzero outgoing differential')
    check(ex.P(basis('c')) == basis('c'), 'retained nonexact class')
    check(all('c' not in ex.dK(basis(k)) for k in ex.K), 'class c not in boundary image')
    product = F(1)
    for a in ex.weights:
        product *= a
    expected = scale((-1)**ex.height * product, basis(f'y{ex.height+1}'))
    check(ex.dK(basis('x0')) == expected and bool(expected), 'nonzero staircase with alternating sign')
    return expected


def main(mutant=None):
    for height in range(1, 5):
        expected = test_example(Example(height))
        print(f'PASS height {height}: d_{height+1}(x0) = {expected}')
    ex = Example(4, unit=True)
    test_example(ex)
    x, R, terminal = basis('x0'), basis('y1'), basis('y5')
    check(ex.I(x) == vec(x0=1, x1=-1, x2=1, x3=-1, x4=1), 'five explicit lift coefficients')
    term = x
    for j in range(5):
        projected = ex.p(ex.pert(term))
        check(projected == (terminal if j == 4 else {}), f'exactly four h needed, term {j}')
        term = ex.h(ex.pert(term))
    check(not term, 'fifth h vanishes')
    check(not ex.D(R), 'upper source closed')
    check(not ex.p(R), 'naive source projection zero')
    check(ex.P(R) == terminal, 'full source projection nonzero')
    # Independently inspect every staircase degree of a mixed full source.
    full = vec(y1=2, y2=3, y3=5, y4=7, y5=11, c=13)
    check(ex.P(full) == vec(y5=8, c=13), 'full projection 2-3+5-7+11 plus retained class')
    check(ex.p(full) == vec(y5=11, c=13), 'naive projection differs on mixed source')
    u = x
    check(ex.dK(u) == ex.P(R), 'primitive finite equation')
    b = scale(-1, add(ex.I(u), ex.H(R)))
    check(b == scale(-1, x), 'primitive cancellation gives -x0')
    check(ex.D(b) == scale(-1, R), 'Db=-R including HR')
    dropped = scale(-1, ex.I(u))
    check(ex.D(dropped) == scale(-1, terminal), 'omitted HR has wrong derivative -y5')
    check(add(ex.D(dropped), R) == vec(y1=1, y5=-1), 'omitted HR nonzero residual')
    # Negative controls are genuine violated checks, not success on an exception.
    if mutant == 'plus-series':
        odd = Example(1, unit=True)
        check(odd.D(odd.I(x, sign=1)) == odd.I(odd.dK(x, sign=1), sign=1),
              'MUTANT plus-series violates DI=I dK')
    elif mutant == 'naive-projection':
        check(ex.p(R) == ex.P(R), 'MUTANT naive-projection loses upper contribution')
    elif mutant == 'omit-HR':
        check(ex.D(dropped) == scale(-1, R), 'MUTANT omit-HR fails Db=-R')
    print(f'PASS {CHECKS} exact checks; universal synthetic data only')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutant', choices=['plus-series', 'naive-projection', 'omit-HR'])
    args = parser.parse_args()
    try:
        main(args.mutant)
    except RegressionFailure as exc:
        print(f'FAIL after {CHECKS} checks: {exc}', file=sys.stderr)
        sys.exit(1)
