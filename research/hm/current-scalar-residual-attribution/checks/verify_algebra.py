#!/usr/bin/env python3
"""Exact universal coefficient identities; no sampled points or geometric ranks."""
import json
import sys
from collections import defaultdict
from fractions import Fraction as Q

import sympy as S

if sys.flags.optimize:
    raise RuntimeError('Run without Python -O or -OO.')


def normal(word, trace=False):
    central = tuple(sorted(x for x in word if x.startswith('$')))
    other = tuple(x for x in word if not x.startswith('$'))
    if trace and other:
        other = min(other[i:] + other[:i] for i in range(len(other)))
    return central + other


def tidy(terms, trace=False):
    out = defaultdict(Q)
    for word, value in terms:
        out[normal(word, trace)] += value
    return {word: value for word, value in out.items() if value}


def atom(name):
    return {(name,): Q(1)}


def add(*terms):
    return tidy((word, value) for term in terms for word, value in term.items())


def scale(term, factor):
    return {word: value * factor for word, value in term.items() if value * factor}


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    return tidy((u + v, x * y) for u, x in a.items() for v, y in b.items())


def form(name):
    return (atom(name + 'a'), atom(name + 'b'))


def fadd(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def fsub(a, b):
    return tuple(sub(x, y) for x, y in zip(a, b))


def wedge(a, b):
    return sub(mul(a[0], b[1]), mul(a[1], b[0]))


def trace(a):
    return tidy(a.items(), trace=True)


def transgression(bi, bj, a):
    # Total product BA and B delta B each have the Cech/forms minus sign.
    return trace(add(scale(wedge(bi, a), -1), wedge(a, bj),
                     scale(wedge(bi, fsub(bj, bi)), -1)))


def verify():
    b0, b1, b2, a01, a12 = map(form, ['B0', 'B1', 'B2', 'A01', 'A12'])
    a02 = fadd(a01, a12)
    dt = add(transgression(b1, b2, a12),
             scale(transgression(b0, b2, a02), -1),
             transgression(b0, b1, a01))
    rhs = trace(sub(wedge(a01, a12),
                    wedge(fadd(a01, fsub(b1, b0)), fadd(a12, fsub(b2, b1)))))
    if dt != rhs:
        raise ValueError('Unsymmetrized AW transgression identity failed')
    theta, k = form('$theta'), atom('$k')
    old = tuple(scale(mul(k, t), -1) for t in theta)
    implemented = trace(scale(add(wedge(b0, b1),
                                  mul(k, wedge(theta, fadd(b0, b1)))), -1))
    if transgression(b0, b1, old) != implemented:
        raise ValueError('Local source expansion of transgression failed')
    # Cyclicity is used only on ordinary coefficient words, not by rotating
    # Alexander-Whitney cochains. The first test retains BA and AB separately.

    x, y, p, q, r, a, b, c = S.symbols('x y p q r a b c')
    checks = []

    def zero(expr, name):
        if isinstance(expr, S.MatrixBase):
            for entry in expr:
                zero(entry, name)
            return
        if S.cancel(expr) != 0:
            raise ValueError(name)
        checks.append(name)

    curve = x**3 - x
    vq = y * S.diff(y / x, x) + (3*x*x-1)/2 * S.diff(y/x, y)
    zero(vq.subs(y*y, curve) - (x + 1/x)/2, 'Vq=delta a')
    zero(S.diff(curve/x**2, x)/(2*(curve/x**2))
         - (x*x+1)/(2*x*(x*x-1)), 'refined line rf')
    zero(S.diff(1-x**-2, x)/(2*(1-x**-2)) - 1/(x*(x*x-1)),
         'old half connection')
    P, Qm = S.Matrix([[p, q], [r, -p]]), S.Matrix([[a, b], [c, -a]])
    zero(Qm*P+P*Qm-S.trace(Qm*P)*S.eye(2), 'rank-two trace identity')
    zero(Qm*P-P*Qm-(2*Qm*P-S.trace(Qm*P)*S.eye(2)), 'rank-two commutator')
    r1, r2, s1, s2 = S.symbols('r1 r2 s1 s2')
    dr = r2*s2 - (r1+r2)*(s1+s2) + r1*s1
    zero(dr + r1*s2 + s1*r2, 'pointwise product Cech correction')
    lam = S.Rational(15, 4)
    anti = S.Rational(15, 8)*(r1*s2-s1*r2)
    zero(anti-lam*r1*s2-S.Rational(15, 8)*dr, 'short gerbe conversion')

    # Exact mixed coefficient of (1/8) pi tensor pi. Derivatives on each
    # argument commute, but the two matrix factors never change order.
    pi = {(0,1): 1, (1,0): -1, (2,3): 1, (3,2): -1}
    mixed = defaultdict(Q)
    for (i,j), z in pi.items():
        for (k,l), w in pi.items():
            if len({i,j,k,l}) == 4:
                mixed[(tuple(sorted((i,k))), tuple(sorted((j,l))))] += Q(z*w, 8)
    expected = {((0,2),(1,3)): Q(1,4), ((0,3),(1,2)): Q(-1,4),
                ((1,2),(0,3)): Q(-1,4), ((1,3),(0,2)): Q(1,4)}
    if dict(mixed) != expected:
        raise ValueError('Mixed Moyal coefficient mismatch')

    # Formal expansion of the actual second-jet module equation. Words
    # preserve matrix order; mu_i and T occurrences are independent symbols.
    h = S.symbols('h')
    g1,u1,v1,g2,u2,v2,g3,u3,v3,t,b0 = S.symbols(
        'gij uij vij gjk ujk vjk gik uik vik Tg b', commutative=False)
    m_gg,m_ug,m_gu,m2,m_bg = S.symbols('mu1gg mu1ug mu1gu mu2gg mu1bg',
                                      commutative=False)
    lhs = S.expand((g2+h*u2+h*h*(v2+t))*(g1+h*u1+h*h*v1)
                   +h*m_gg+h*h*(m_ug+m_gu+m2))
    rhs2 = S.expand((1+h*b0+h*h*b0*b0/2)*(g3+h*u3+h*h*v3)+h*h*m_bg)
    coefficient = S.expand(lhs-rhs2).coeff(h, 2)
    expected_defect = v2*g1+g2*v1-v3+u2*u1+m_ug+m_gu+m2+t*g1-b0*u3-b0*b0*g3/2-m_bg
    if S.expand(coefficient-expected_defect) != 0:
        raise ValueError('Full order-two module expansion mismatch')

    # Character support is XOR, including the same-character contractions.
    full = 15
    low = [0,1,2,4,8]
    if any(a ^ b == full for a in low for b in low):
        raise ValueError('Unexpected quadratic full-sign support')
    if any(a ^ b == full for a in low for b in [3,12]):
        raise ValueError('Unexpected mixed full-sign support')
    return {'status': 'PASS', 'universalFreeTraceIdentities': 2,
            'commutativeScalarOrMatrixEntryIdentities': len(checks),
            'mixedMoyalTerms': 4, 'completeModuleExpansion': True,
            'characterSupportEnumerated': True,
            'scope': 'Universal symbolic identities; no point sampling or scalar evaluation.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
