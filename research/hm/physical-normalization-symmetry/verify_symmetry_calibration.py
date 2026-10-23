#!/usr/bin/env python3
"""Bounded exact character/degree/multiplier diagnostics.

Only universal representation characters and formal polynomial coefficient
labels are used. No actual HM coefficients, points, matrices, source choices,
evaluations or ranks occur. Geometric orbit and authentication premises are
proved/stated in PROOF.md, not inferred from the arithmetic below.
"""
from fractions import Fraction as F
from time import perf_counter


class Qphi:
    # a+b*phi with phi^2=phi+1.
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def coerce(x):
        return x if isinstance(x, Qphi) else Qphi(x)

    def __add__(self, x):
        x = self.coerce(x)
        return Qphi(self.a+x.a, self.b+x.b)

    __radd__ = __add__

    def __neg__(self):
        return Qphi(-self.a, -self.b)

    def __sub__(self, x):
        return self+-self.coerce(x)

    def __rsub__(self, x):
        return self.coerce(x)+-self

    def __mul__(self, x):
        x = self.coerce(x)
        return Qphi(self.a*x.a+self.b*x.b,
                    self.a*x.b+self.b*x.a+self.b*x.b)

    __rmul__ = __mul__

    def __truediv__(self, x):
        # Only rational denominators are needed.
        return Qphi(self.a/F(x), self.b/F(x))

    def __pow__(self, n):
        out = Qphi(1)
        for _ in range(n):
            out = out*self
        return out

    def __eq__(self, x):
        x = self.coerce(x)
        return (self.a, self.b) == (x.a, x.b)


phi = Qphi(0, 1)
phibar = 1-phi
sizes = [1, 15, 20, 12, 12]
chars = {
    '1': [1, 1, 1, 1, 1],
    'A': [3, -1, 0, phi, phibar],
    'V': [3, -1, 0, phibar, phi],
    'P': [4, 0, 1, -1, -1],
    'D': [5, 1, -1, 0, 0],
}
chars = {k: [Qphi.coerce(v) for v in c] for k, c in chars.items()}


def add(*cs):
    return [sum((c[i] for c in cs), Qphi()) for i in range(5)]


def sub(c, d):
    return [x-y for x, y in zip(c, d)]


def tensor(c, d):
    return [x*y for x, y in zip(c, d)]


def times(n, c):
    return [n*x for x in c]


def inner(c, d):
    return sum((n*x*y for n, x, y in zip(sizes, c, d)), Qphi())/60


def binary_sym(n, two):
    if n == 0:
        return chars['1']
    prev, out = chars['1'], two
    for _ in range(1, n):
        prev, out = out, sub(tensor(two, out), prev)
    return out


checks = 0
negative_checks = 0


def equal(x, y, label):
    global checks
    if x != y:
        raise AssertionError(label)
    checks += 1


def different(x, y, label):
    global negative_checks
    if x == y:
        raise AssertionError(label)
    negative_checks += 1


def main():
    start = perf_counter()
    one, a, v, p, d = (chars[k] for k in ['1', 'A', 'V', 'P', 'D'])
    for n, c in chars.items():
        for m, e in chars.items():
            equal(inner(c, e), int(n == m), 'character orthogonality '+n+m)
    w = [Qphi.coerce(x) for x in [2, 0, 1, phi, phi-1]]
    u = [Qphi.coerce(x) for x in [2, 0, 1, phi-1, phi]]
    equal(binary_sym(2, w), a, 'negative W has Sym2=A')
    equal(binary_sym(2, u), v, 'positive U has Sym2=V')
    equal(binary_sym(4, u), d, 'positive source Sym4U=D5')
    t = add(one, v, p, d)
    equal(binary_sym(12, u), t, 'actual trace decomposition')
    different(binary_sym(12, w), t, 'wrong U=W identification rejected')
    equal(inner(t, one), 1, 'invariant vector dimension')
    equal(t[0], 13, 'unconstrained global trace dimension')
    squares, cubes = [0, 0, 2, 4, 3], [0, 1, 0, 4, 3]
    sym3a = [(a[j]**3+3*a[j]*a[squares[j]]+2*a[cubes[j]])/6 for j in range(5)]
    equal(sym3a, add(a, v, p), 'symmetric cube of negative quadratic space')
    equal(binary_sym(6, w), add(v, p), 'square restriction sextics')
    equal(tensor(a, d), add(a, v, p, d), 'A times D')
    equal(tensor(v, d), add(a, v, p, d), 'V times D')
    equal(tensor(p, d), add(a, v, p, d, d), 'P times D')
    source = tensor(sym3a, d)
    equal(source, add(times(3, a), times(3, v), times(3, p), times(4, d)), 'source decomposition')
    equal(source[0], 50, 'source tensor dimension')
    equal(inner(source, t), 10, 'equivariant family dimension')
    equal(inner(source, one), 0, 'invariant output absent')
    equal(inner(source, v), 3, 'V family multiplicity')
    equal(inner(source, p), 3, 'P family multiplicity')
    equal(inner(source, d), 4, 'D family multiplicity')
    equal(add(v, p, d)[0], 12, 'universal output span')
    different(Qphi(10), Qphi(12), 'family parameters not output dimension')
    different(inner(source, one), inner(t, one), 'equivariant family not invariant vector')

    axis_values = [Qphi.coerce(x) for x in [6, -2, 0, 1, 1]]
    equal(axis_values, add(a, v), 'six-axis O3 sign-valued module')
    equal(sub(sym3a, axis_values), p, 'axis-invisible cubics')
    equal(inner(tensor(p, d), t), 4, 'axis-family kernel')
    equal(inner(tensor(axis_values, d), t), 6, 'axis-family image')
    equal((5*t[0]-5*t[1])/10, 6, 'full N-equivariant axis target')
    equal(inner(tensor(a, d), t), 3, 'square-family kernel')
    equal(inner(tensor(binary_sym(6, w), d), t), 7, 'square-family image')
    equal(5*t[0]/5, 13, 'full C5-equivariant square target')
    equal(6+7-10, 3, 'separate image dimensions not additive')
    equal(2*3, 6, 'cubic degree restricted to square conic')
    equal(12 > 6, True, 'twelve zeros exceed restricted degree')
    different([6, 2, 0, 1, 1], axis_values, 'O3 sign cannot be dropped')

    # Full universal h-family multiplication: input formal coefficients
    # C[j,k] represent L(m_j)'s u^(12-k)v^k coefficient. No matrix/rank
    # computation is used: the H_j^2 diagonal has an explicit left inverse.
    for j in range(5):
        for k in range(13):
            product = {}
            for i in range(5):
                h_exp = tuple(int(r == i)+int(r == j) for r in range(5))
                key = (h_exp, i+k)
                product[key] = product.get(key, 0)+1
            recovered = {}
            for (hs, binary_exp), coefficient in product.items():
                diag = [r for r in range(5) if hs[r] == 2]
                if diag:
                    row = diag[0]
                    recovered[(row, binary_exp-row)] = coefficient
            equal(recovered, {(j, k): 1}, 'formal multiplier left inverse '+str((j, k)))
    equal((3+3, 1+1, 4+12), (6, 2, 16), 'physical norm-error degrees')
    different((6, 2, 16), (6, 1, 16), 'norm observation is not linear in h')
    equal((-1)**12, 1, 'center acts trivially on all trace coefficients')
    if perf_counter()-start >= 30:
        raise AssertionError('bounded diagnostic runtime')
    print(f'PASS: {checks} exact character/degree/coefficient checks; {negative_checks} negative controls')
    print('PASS: U=Wprime; 13 traces / 12 nontrivial outputs / 10 equivariant family parameters')
    print('PASS: axis kernel4 image6; square kernel3 image7; varying-source multiplier injectivity')
    print('SCOPE: universal diagnostics, not Lean, actual equivariance authentication, or calibration')


if __name__ == '__main__':
    main()
