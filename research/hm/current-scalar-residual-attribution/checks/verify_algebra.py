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


def first_order_sign_calibration(transgression_sign=1, row_trace_sign=-1):
    """Propagate one ordinary-wedge bivector pair through the complete lift.

    The two disjoint pairs add linearly at first order. All logarithmic
    derivatives below are independent generic traceless matrices, not point
    samples. The signs are parameters only for the rejection regressions.
    """
    half, quarter = S.Rational(1, 2), S.Rational(1, 4)

    def traceless(name):
        a, b, c = S.symbols(name + '0:3')
        return S.Matrix([[a, b], [c, -a]])

    pa, pb, qa, qb = map(traceless, ['pa', 'pb', 'qa', 'qb'])
    C = half * (qa*pb-qb*pa)
    # A^E_ij and transported A^E_jk have column coefficients -P^t,-Q^t.
    ordinary_E = S.trace((-pa.T)*(-qb.T)-(-pb.T)*(-qa.T))
    def K(a, b):
        return -half * (a*b-b*a)

    delta_K = K(pa,pb)+K(qa,qb)-K(pa+qa,pb+qb)
    ra, rb, sa, sb = S.symbols('q_ij_a q_ij_b q_jk_a q_jk_b')
    ordinary_theta = quarter * (ra*sb-rb*sa)
    total_theta = -ordinary_theta
    # Recompute the supertrace coefficient from degrees, ranks, and weights.
    weighted_rank = sum(sign*rank*weight**2 for sign, rank, weight in
                        [(-1,5,-1),(1,15,1),(-1,10,3),(1,2,5)])
    ordinary_old = weighted_rank * ordinary_theta
    total_old = weighted_rank * total_theta
    pi_aw = -half * ordinary_theta
    delta_r = sa*sb-(ra+sa)*(rb+sb)+ra*rb
    gerbe = S.Rational(15,4)*ra*sb
    # This is the ordinary coefficient identity checked by the universal
    # free-trace expansion below: delta T = old square - new square.
    delta_T = transgression_sign * (ordinary_old-ordinary_E)
    delta_s = -quarter*delta_T-S.Rational(15,8)*delta_r
    delta_x = delta_s*S.eye(2)-half*delta_K
    stages = []

    def zero(value, name):
        entries = list(value) if isinstance(value, S.MatrixBase) else [value]
        if any(S.expand(entry) != 0 for entry in entries):
            raise ValueError('First-order sign calibration failed: '+name)
        stages.append(name)

    zero(weighted_rank+30, 'supertrace coefficient')
    zero(total_old+ordinary_old, 'total-to-ordinary old square')
    zero(half*total_theta-pi_aw, 'total theta to Pi_AW')
    zero(-15*pi_aw-gerbe-S.Rational(15,8)*delta_r, 'theta and gerbe correction')
    zero(S.trace(C)-row_trace_sign*half*ordinary_E, 'row-column ordinary trace')
    zero(delta_s-gerbe-quarter*ordinary_E, 'ordinary transgression to scalar')
    zero(delta_s-gerbe+half*S.trace(C), 'unchanged scalar equation')
    zero(delta_K-2*C+S.trace(C)*S.eye(2), 'rank-two delta K')
    zero(delta_x-gerbe*S.eye(2)+C, 'unchanged full first-order equation')
    return stages


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
    calibration = first_order_sign_calibration()
    rejected_signs = []
    for name, signs in [('reversed ordinary transgression', (-1,-1)),
                        ('reversed ordinary row-column trace', (1,1))]:
        try:
            first_order_sign_calibration(*signs)
        except ValueError:
            rejected_signs.append(name)
        else:
            raise ValueError('Wrong first-order sign was accepted: '+name)
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
            'firstOrderSignCalibration': calibration,
            'wrongSignVariantsRejected': rejected_signs,
            'commutativeScalarOrMatrixEntryIdentities': len(checks),
            'mixedMoyalTerms': 4, 'completeModuleExpansion': True,
            'characterSupportEnumerated': True,
            'scope': 'Universal symbolic identities; no point sampling or scalar evaluation.'}


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
