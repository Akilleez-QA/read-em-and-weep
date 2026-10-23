#!/usr/bin/env python3
"""Universal q-adic free-word checks for the NEW normalization interface.

No actual HM data, numerical substitutions, ranks, solves or dependencies.
The cohomology block may have arbitrary rank. A final formal cyclic trace
with an extra N symbol demonstrates a nonzero trace-response polynomial;
it is not an actual n8/source evaluation. Written geometric hypotheses and
the trace-sheaf cohomology argument are not certified by this script.
"""
from time import perf_counter


class P:
    def __init__(self, terms=None):
        self.terms = {m: c for m, c in (terms or {}).items() if c}

    def __add__(self, other):
        out = self.terms.copy()
        for m, c in other.terms.items():
            out[m] = out.get(m, 0) + c
        return P(out)

    def __neg__(self):
        return P({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        out = {}
        for (n, w), c in self.terms.items():
            for (k, v), e in other.terms.items():
                m = (n + k, w + v)
                out[m] = out.get(m, 0) + c * e
        return P(out)

    def __eq__(self, other):
        return isinstance(other, P) and self.terms == other.terms

    def coeff(self, degree):
        return P({(0, w): c for (n, w), c in self.terms.items() if n == degree})

    def mod(self, degree):
        return P({(n, w): c for (n, w), c in self.terms.items() if n < degree})


zero = P()
one = P({(0, ()): 1})


def q(n):
    return P({(n, ()): 1})


def v(name):
    return P({(0, (name,)): 1})


def mat():
    return [[zero for _ in range(5)] for _ in range(5)]


def eye():
    a = mat()
    for j in range(5):
        a[j][j] = one
    return a


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def neg(a):
    return [[-x for x in r] for r in a]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), zero)
             for j in range(len(b[0]))] for i in range(len(a))]


def scale(a, c):
    return [[c * x for x in r] for r in a]


def prod(*args):
    out = args[0]
    for a in args[1:]:
        out = mul(out, a)
    return out


def entry(a):
    assert len(a) == len(a[0]) == 1
    return a[0][0]


checks = 0
negative_checks = 0


def require(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def different(a, b, label):
    global negative_checks
    if a == b:
        raise AssertionError(label)
    negative_checks += 1


def equal(a, b, label):
    require(a == b, label)


d = mat()
d[1][0] = one
d[4][3] = one
i0 = [[zero], [zero], [one], [zero], [zero]]
p0 = [[zero, zero, one, zero, zero]]
h0 = mat()
h0[0][1] = one
h0[3][4] = one


def differential(a):
    return sub(mul(d, a), mul(a, d))


def contraction(tag):
    # Formal, q-varying splittings with EXACT common cohomology frame g=1.
    x = v(tag + 'x0') + q(1) * v(tag + 'x1')
    y = v(tag + 'y0') + q(1) * v(tag + 'y1')
    z = v(tag + 'z0') + q(1) * v(tag + 'z1')
    s = eye()
    si = eye()
    s[1][2], s[1][3], s[2][3] = x, y, z
    si[1][2], si[1][3], si[2][3] = -x, x * z - y, -z
    equal(mul(s, si), eye(), tag + ' exact formal inverse')
    equal(mul(si, s), eye(), tag + ' reverse inverse')
    equal(mul(d, s), mul(s, d), tag + ' chain automorphism')
    inc, pr, hom = mul(s, i0), mul(p0, si), prod(s, h0, si)
    equal(mul(pr, inc), [[one]], tag + ' retraction')
    equal(add(mul(d, hom), mul(hom, d)), sub(eye(), mul(inc, pr)), tag + ' contraction')
    equal(mul(pr, d), [[zero] * 5], tag + ' closed projection')
    equal(mul(d, inc), [[zero] for _ in range(5)], tag + ' closed inclusion')
    return inc, pr, hom


def cochain(tag):
    out = mat()
    for i, j in [(0, 0), (4, 4)] + [(i, j) for i in range(1, 4) for j in range(1, 4)]:
        out[i][j] = v(f'{tag}{i}{j}_0') + q(1) * v(f'{tag}{i}{j}_1')
    return out


def cyclic_tau(a):
    # Formal trace(N*a), cyclic equivalence only. Constant a is suppressed,
    # recording tr(N)=0. No trace identity of any selected matrix is used.
    out = {}
    for (n, w), c in a.terms.items():
        if not w:
            continue
        nw = ('N',) + w
        key = (n, min(nw[k:] + nw[:k] for k in range(len(nw))))
        out[key] = out.get(key, 0) + c
    return P(out)


def main():
    start = perf_counter()
    contractions = [contraction(tag) for tag in ('A', 'B', 'C')]
    E, F = cochain('E'), cochain('F')
    # A freely specified closed part plus an order-four nonclosed tail.
    closed = mat()
    for j in range(4):
        closed[2][2] = closed[2][2] + q(j) * v('Jclosed' + str(j))
    equal(differential(closed), mat(), 'closed reference')
    J = add(closed, scale(F, q(4)))
    W = differential(F)
    T = differential(E)
    S = add(T, scale(W, q(1)))
    X = add(J, scale(E, q(3)))
    equal(differential(X), scale(S, q(3)), 'test fixture lower source equation')
    equal(T, sub(S, scale(W, q(1))), 'corrected source retained')

    def projection(c, e):
        return entry(prod(c[1], e, c[0]))

    def comparison(ca, cb, t):
        return entry(prod(cb[1], add(mul(t, cb[2]), mul(ca[2], t)), ca[0]))

    for ia, ca in enumerate(contractions):
        for ib, cb in enumerate(contractions):
            label = str(ia) + str(ib)
            equal(prod(cb[1], ca[0]), [[one]], 'same ambient frame ' + label)
            eta = comparison(ca, cb, T).coeff(0)
            equal(eta, comparison(ca, cb, S).coeff(0), 'cone corrected-source equality ' + label)
            y_a, y_b = projection(ca, X).coeff(3), projection(cb, X).coeff(3)
            ell_a, ell_b = projection(ca, E).coeff(0), projection(cb, E).coeff(0)
            equal(y_b - y_a, eta, 'lower third-jet change = cone response ' + label)
            equal(ell_b - ell_a, eta, 'row change = same cone response ' + label)
            equal(y_b - ell_b, y_a - ell_a, 'paired invariance ' + label)
            hybrid, paired = y_a - ell_b, y_a - ell_a
            equal(hybrid - paired, -eta, 'mixed error sign ' + label)
            equal(hybrid + eta, paired, 'counterterm repairs mixed error ' + label)
            equal(comparison(ca, cb, scale(S, q(3))), q(3) * comparison(ca, cb, S),
                  'q tensor compatibility ' + label)
            equal((projection(cb, J) - projection(ca, J)).mod(4), zero,
                  'lower data unchanged in common frame ' + label)
            equal(cyclic_tau(hybrid - paired), -cyclic_tau(eta), 'scalar response error ' + label)
            if ia != ib:
                different(cyclic_tau(eta), zero, 'unpaired normalizations must not be silently identified ' + label)
                different(hybrid - eta, paired, 'wrong compensation sign rejected ' + label)

    ca, cb = contractions[:2]
    eta = comparison(ca, cb, T).coeff(0)
    y_a, y_b = projection(ca, X).coeff(3), projection(cb, X).coeff(3)
    ell_a, ell_b = projection(ca, E).coeff(0), projection(cb, E).coeff(0)
    # Independent row normalization with the old lower jet is the bug.
    different(y_a - ell_b, y_a - ell_a, 'row-only substitution changes scalar')
    different(y_b - ell_a, y_a - ell_a, 'lower-only substitution changes scalar')
    # No incorrect claim of equality before restriction to Q.
    different(comparison(ca, cb, S), comparison(ca, cb, T), 'qW disappears only after restriction')
    # q^3, not q^2: this shift would read the wrong lower coefficient.
    different((q(2) * comparison(ca, cb, S)).coeff(3), eta, 'wrong normal order rejected')
    # Cone data suffice for eta, but not for the full ambient comparison.
    equal(comparison(ca, cb, T).coeff(0), eta, 'only zeroth normal jet needed')
    if perf_counter() - start >= 30:
        raise AssertionError('bounded diagnostic runtime')
    print(f'PASS: {checks} exact q-adic free-word identities; {negative_checks} negative mutation tests')
    print('PASS: paired and mixed source-response normalization, source-only cone counterterm, qW restriction boundary')
    print('SCOPE: universal diagnostics only; written proof not Lean; no actual HM response or source value')


if __name__ == '__main__':
    main()
