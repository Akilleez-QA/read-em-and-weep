"""Formal Cech sign checks only; no physical source or coefficient evaluation.

One current and one formal differentiated scalar suffice by linearity.
Current l_ij is the universal additive cocycle l_j-l_i in a common frame.
Monomials below are formal labels, not physical polynomial coefficients.
"""
from collections import defaultdict
from fractions import Fraction


def add(*polys):
    out = defaultdict(Fraction)
    for p in polys:
        for key, value in p.items():
            out[key] += value
    return {k: v for k, v in out.items() if v}


def scale(a, p):
    return {k: a * v for k, v in p.items() if a * v}


def delta(cochain):
    return lambda vertices: add(*(
        scale((-1) ** i, cochain(vertices[:i] + vertices[i + 1:]))
        for i in range(len(vertices))
    ))


def scalar(vertices):
    return {tuple(vertices): Fraction(1)}


def current_times_scalar(i, j, p):
    return add(
        {(j, label): value for label, value in p.items()},
        {(i, label): -value for label, value in p.items()},
    )


def cup_operator(t, second_sign):
    """ell cup t + second_sign * t cup ell, without the common 1/2."""
    return lambda v: add(
        current_times_scalar(v[0], v[1], t(v[1:])),
        scale(second_sign, current_times_scalar(v[-2], v[-1], t(v[:-1]))),
    )


def main():
    triangle = (0, 1, 2)
    tetrahedron = (0, 1, 2, 3)
    # A on degree zero; E on delta f (degree one).
    da = delta(cup_operator(scalar, +1))(triangle)
    ed = cup_operator(delta(scalar), -1)(triangle)
    assert add(ed, da) == {}, 'E(delta f) must equal -delta A(f)'
    assert add(ed, scale(-1, da)), 'The incorrect plus sign must fail'
    # E on degree one; A on delta s (degree two).
    de = delta(cup_operator(scalar, -1))(tetrahedron)
    ad = cup_operator(delta(scalar), +1)(tetrahedron)
    assert add(de, ad) == {}, 'delta E(s) must equal -A(delta s)'
    assert add(de, scale(-1, ad)), 'The incorrect plus sign must fail'
    print('PASS: both graded cup identities; both opposite-sign controls fail.')
    print('Scope: formal signs only; no transport, regularity, or budget certificate.')


if __name__ == '__main__':
    main()
