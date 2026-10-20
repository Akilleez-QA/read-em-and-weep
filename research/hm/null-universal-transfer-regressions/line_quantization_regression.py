#!/usr/bin/env python3
"""Bounded exact universal line-module tests, never actual HM data.

Ring: Q[x1^+-1,...,x4^+-1,s,t]/(s,t)^3. Composition is F after G.
Run normally or with -O. --mutant choices deliberately break one convention;
a correctly detected mutant exits 1. No assertions, dependencies, or I/O data.
"""
from fractions import Fraction as Fr
from itertools import product
import argparse
import sys

ZERO = (0,) * 6
MUTANT = 'none'
CHECKS = 0


def clean(p):
    return {k: Fr(v) for k, v in p.items() if v and k[0] + k[1] <= 2}


def term(exponents=(0, 0, 0, 0), coefficient=1, order=(0, 0)):
    return clean({tuple(order) + tuple(exponents): Fr(coefficient)})


def add(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def scale(p, c):
    return clean({k: v*c for k, v in p.items()})


def mul(p, q):
    out = {}
    for k, v in p.items():
        for l, w in q.items():
            e = tuple(a+b for a, b in zip(k, l))
            if e[0]+e[1] <= 2:
                out[e] = out.get(e, 0) + v*w
    return clean(out)


def shift_order(p, a, b):
    return clean({(k[0]+a, k[1]+b)+k[2:]: v for k, v in p.items()})


def D(p, weight, i, chart=()):
    """Chart tuple gives inverted coordinates. In infinity frame D=-d/du/2."""
    out = {}
    for k, v in p.items():
        e = list(k)
        if i in chart:
            c = -Fr(k[i+2], 2)
            e[i+2] -= 1
        else:
            effective_weight = weight
            if MUTANT == 'dropped_root' and weight != 0:
                effective_weight -= 1
            c = Fr(k[i+2]-effective_weight, 2)
            e[i+2] += 1
        if c:
            out[tuple(e)] = out.get(tuple(e), 0) + c*v
    return clean(out)


# (left derivative, right derivative, scalar, formal parameter index)
CONTRACTIONS = ((0, 1, Fr(1, 2), 0), (1, 0, Fr(-1, 2), 0),
                (2, 3, Fr(1, 2), 1), (3, 2, Fr(-1, 2), 1))


def star(p, wp, q, wq, chart=()):
    """m exp(sP+tQ) through total parameter degree two."""
    pieces = [mul(p, q)]
    for i, j, c, a in CONTRACTIONS:
        pieces.append(shift_order(scale(mul(D(p, wp, i, chart),
                                               D(q, wq, j, chart)), c),
                                  int(a == 0), int(a == 1)))
        for k, l, d, b in CONTRACTIONS:
            if MUTANT == 'missing_mixed' and a != b:
                continue
            coefficient = mul(D(D(p, wp, i, chart), wp, k, chart),
                              D(D(q, wq, j, chart), wq, l, chart))
            pieces.append(shift_order(scale(coefficient, c*d/2),
                                      int(a == 0)+int(b == 0),
                                      int(a == 1)+int(b == 1)))
    return add(*pieces)


def quant(f, source, target, z, chart=()):
    if MUTANT == 'plain_map':
        return mul(f, z)
    hom = 0 if MUTANT == 'wrong_hom' else target-source
    return star(f, hom, z, source, chart)


def frame(p, weight, chart):
    """Finite coefficient -> chart coefficient using e_inf=x^weight e_0."""
    out = {}
    for k, v in p.items():
        e = list(k)
        for i in chart:
            e[i+2] = weight-k[i+2]
        out[tuple(e)] = out.get(tuple(e), 0) + v
    return clean(out)


def equal(label, actual, expected):
    global CHECKS
    CHECKS += 1
    if actual != expected:
        if isinstance(actual, dict) and isinstance(expected, dict):
            keys = sorted(set(actual) | set(expected))
            key = next(k for k in keys if actual.get(k, 0) != expected.get(k, 0))
            witness = (key, actual.get(key, 0)-expected.get(key, 0))
        else:
            witness = 'matrix/vector differs'
        raise RuntimeError('%s; residual witness %r' % (label, witness))


def nonzero(label, p):
    equal(label, bool(p), True)


def coefficient(p, a, b):
    return {k[2:]: v for k, v in p.items() if k[:2] == (a, b)}


def mcompose(A, wa, B, wb, chart=()):
    if MUTANT == 'reversed_order':
        A, B, wa, wb = B, A, wb, wa
    return [[add(*(star(A[i][k], wa, B[k][j], wb, chart)
                    for k in range(2))) for j in range(2)] for i in range(2)]


def qapply(A, source, target, z, chart=()):
    return [add(*(quant(A[i][j], source, target, z[j], chart)
                  for j in range(2))) for i in range(2)]


def run():
    one = term()
    x = [term(tuple(int(i == j) for i in range(4))) for j in range(4)]
    # Sparse hand-chosen Laurent germs, not global sections or geometric data.
    z = add(term((-1, 2, 1, -2), Fr(2, 3)), term((2, 0, -1, 1)),
            term((0, 1, 0, -1), Fr(-3, 5), (1, 0)))
    a = add(term((1, -1, 2, 0)), term((0, 1, -1, 2), Fr(1, 3)),
            term((1, 0, 0, 1), 2, (0, 1)))
    b = add(term((0, 2, 1, -1)), term((1, 0, -2, 1), Fr(-1, 2)))
    f = add(term((2, -1, 0, 1)), term((-1, 0, 1, 2), Fr(3, 2)))
    g = add(term((0, 1, -1, 1)), term((1, -2, 2, 0), Fr(-2, 3)))
    weights = (-3, -1, 0, 1, 3, 5)
    # Closed-form oracle independent of exponential assembly.
    for n in weights:
        e = (-2, 0, 1, 3)
        p = term(e, Fr(2, 7))
        for i in range(4):
            ei = list(e); ei[i] += 1
            equal('finite D monomial n=%s i=%s' % (n, i), D(p, n, i),
                  term(ei, Fr(2, 7)*Fr(e[i]-n, 2)))
            for j in range(4):
                equal('commuting line operators', D(D(p, n, i), n, j),
                      D(D(p, n, j), n, i))
            equal('line Leibniz', D(mul(z, a), n, i),
                  add(mul(D(z, n, i), a), mul(z, D(a, 0, i))))
        equal('right unit', star(z, n, one, 0), z)
        equal('module associativity n=%s' % n,
              star(star(z, n, a, 0), n, b, 0),
              star(z, n, star(a, 0, b, 0), 0))
    oracle = star(mul(x[0], x[2]), 0, mul(x[1], x[3]), 0)
    equal('independent mixed st normalization', coefficient(oracle, 1, 1),
          {(2, 2, 2, 2): Fr(1, 64)})
    pure = star(term((2, 0, 0, 0)), 0, term((0, 2, 0, 0)), 0)
    equal('independent pure s2 normalization', coefficient(pure, 2, 0),
          {(4, 4, 0, 0): Fr(9, 32)})
    # Cases include the four specified integer weights solely as generic parameters.
    triples = ((-1, 1, 3), (1, 3, 5), (5, -1, 1), (-3, 0, 5))
    for m, n, ell in triples:
        for i in range(4):
            equal('Hom commutator source=%s target=%s' % (m, n),
                  add(D(mul(f, z), n, i), scale(mul(f, D(z, m, i)), -1)),
                  mul(D(f, n-m, i), z))
        equal('right-module linearity %s->%s' % (m, n),
              quant(f, m, n, star(z, m, a, 0)),
              star(quant(f, m, n, z), n, a, 0))
        equal('quantized composition %s->%s->%s' % (m, n, ell),
              quant(f, n, ell, quant(g, m, n, z)),
              quant(star(f, ell-n, g, n-m), m, ell, z))
        # Actual frame transition, including each mixed finite/infinity chart.
        for flags in product((False, True), repeat=4):
            chart = tuple(i for i in range(4) if flags[i])
            for i in range(4):
                equal('D frame gluing n=%s chart=%s i=%s' % (n, chart, i),
                      frame(D(z, n, i), n, chart),
                      D(frame(z, n, chart), n, i, chart))
            equal('module-action frame gluing',
                  frame(star(z, m, a, 0), m, chart),
                  star(frame(z, m, chart), m, frame(a, 0, chart), 0, chart))
            equal('quantized-map frame gluing',
                  frame(quant(f, m, n, z), n, chart),
                  quant(frame(f, n-m, chart), m, n, frame(z, m, chart), chart))
            equal('Hom-composition frame gluing',
                  frame(star(f, ell-n, g, n-m), ell-m, chart),
                  star(frame(f, ell-n, chart), ell-n,
                       frame(g, n-m, chart), n-m, chart))
    # Noncommuting 2x2 coefficient matrices, acting on column vectors.
    A = [[f, one], [x[2], add(x[0], x[3])]]
    B = [[x[1], g], [one, x[0]]]
    vector = [z, b]
    for m, n, ell in triples[:2]:
        C = mcompose(A, ell-n, B, n-m)
        equal('noncommuting matrix composition',
              qapply(A, n, ell, qapply(B, m, n, vector)),
              qapply(C, m, ell, vector))
        equal('matrix right-module linearity',
              qapply(A, m, n, [star(v, m, a, 0) for v in vector]),
              [star(v, n, a, 0) for v in qapply(A, m, n, vector)])
    # Explicit witnesses ensure degenerate cases cannot mask the controls.
    nonzero('plain multiplication genuinely differs',
            add(quant(f, -1, 1, z), scale(mul(f, z), -1)))
    nonzero('matrix coefficients genuinely noncommute',
            add(mul(A[0][0], B[0][0]), mul(A[0][1], B[1][0]),
                scale(mul(B[0][0], A[0][0]), -1),
                scale(mul(B[0][1], A[1][0]), -1)))
    print('PASS: %s exact checks; mutant=%s; optimize=%s' %
          (CHECKS, MUTANT, sys.flags.optimize))


def main():
    global MUTANT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutant', default='none', choices=(
        'none', 'plain_map', 'wrong_hom', 'dropped_root',
        'reversed_order', 'missing_mixed'))
    MUTANT = parser.parse_args().mutant
    try:
        run()
    except Exception as exc:
        print('FAIL after %s checks; mutant=%s; optimize=%s: %s' %
              (CHECKS, MUTANT, sys.flags.optimize, exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
