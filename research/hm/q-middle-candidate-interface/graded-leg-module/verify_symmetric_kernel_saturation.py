#!/usr/bin/env python3
"""Exact universal identities only: no numerical evaluation or rank calculation.

Run: python verify_symmetric_kernel_saturation.py
Requires SymPy. The proof of module exactness is in the companion note; this
verifier checks its polynomial maps, constructive formula, symbolic subbundle
certificate, and resulting Hilbert/cohomology identities.
"""

from itertools import combinations
import sympy as sp

x, y, z = sp.symbols("x y z")
FB, FC, FD = sp.symbols("FB FC FD", nonzero=True)
coords = (x, y, z)
r = sp.Matrix(coords)
C = sp.Matrix([[0, -z, y], [z, 0, -x], [-y, x, 0]])
Q = -C


def zero(expr):
    entries = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
    assert all(sp.cancel(sp.expand(v)) == 0 for v in entries), expr


def wedge(u, v):
    return u * v.T - v * u.T


def symprod(u, v):
    return (u * v.T + v * u.T) / 2


def double_curl(M):
    return sp.Matrix(3, 3, lambda a, b: sp.expand(sum(
        sp.LeviCivita(a, k, i) * sp.LeviCivita(b, ell, j)
        * sp.diff(M[i, j], coords[k], coords[ell])
        for k in range(3) for i in range(3)
        for ell in range(3) for j in range(3))))


zero(r.T * C)
zero(C * r)
zero(wedge(C[:, 1], C[:, 2]) - x * Q)
zero(wedge(C[:, 2], C[:, 0]) - y * Q)
zero(wedge(C[:, 0], C[:, 1]) - z * Q)
print("PASS: Koszul relation and all three exterior-product identities")

# The three exact symmetric-square presentation relations.
for j in range(3):
    zero(sum((coords[i] * symprod(C[:, i], C[:, j])
              for i in range(3)), sp.zeros(3)))
w = sp.Matrix(sp.symbols("w0:3"))
zero(C * (r * w.T + w * r.T) * C.T)
print("PASS: symmetric-square chain relations and polynomial gauge kernel")

# Universal coefficient tensors, not a choice of physical source data.
# Every coefficient of an arbitrary symmetric constant/linear potential remains
# an independent symbol. No points, randomized values, or rank calls are used.
for d in (2, 3):
    monomials = (sp.Integer(1),) if d == 2 else coords
    potential = sp.zeros(3)
    for i in range(3):
        for j in range(i, 3):
            coeffs = sp.symbols(f"b{d}_{i}{j}_0:{len(monomials)}")
            value = sum(c * m for c, m in zip(coeffs, monomials))
            potential[i, j] = potential[j, i] = value
    M = C * potential * C.T
    zero(M * r)
    reconstructed_potential = double_curl(M) / (d * (d + 1))
    zero(reconstructed_potential - reconstructed_potential.T)
    zero(C * reconstructed_potential * C.T - M)
d = sp.symbols("d", integer=True, positive=True)
zero(2 + 2 * (d - 1) + d * (d - 1) - d * (d + 1))
print("PASS: double-curl reconstruction in degrees 2 and 3 with all coefficients free")
print("PASS: universal Euler contraction coefficient d(d+1)")

fcoeffs = sp.symbols("f0:6")
f = sum(a * m for a, m in zip(fcoeffs, (x*x, x*y, x*z, y*y, y*z, z*z)))
W = f * Q
recovered_f = (sp.diff(W[1, 2], x) - sp.diff(W[0, 2], y)
               + sp.diff(W[0, 1], z)) / 5
zero(recovered_f - f)
lift = (sp.diff(f, x) * wedge(C[:, 1], C[:, 2])
        + sp.diff(f, y) * wedge(C[:, 2], C[:, 0])
        + sp.diff(f, z) * wedge(C[:, 0], C[:, 1])) / 2
zero(lift - W)
print("PASS: cubic alternating-sector polynomial extraction and product lift")

# Generic symmetric-presentation chain identity over independent symbols.
rel = sp.Matrix(5, 3, lambda i, a: sp.Symbol(f"t_{i}_{a}"))
pairs = list(combinations(range(3), 2))
sympairs = [(i, j) for i in range(5) for j in range(i, 5)]
pair_index = {pair: n for n, pair in enumerate(sympairs)}
d1 = sp.zeros(15, 15)
for a in range(3):
    for i in range(5):
        for j in range(5):
            d1[pair_index[tuple(sorted((i, j)))], 5*a+i] += rel[j, a]
d2 = sp.zeros(15, 3)
for c, (a, b) in enumerate(pairs):
    for i in range(5):
        d2[5*a+i, c] = rel[i, b]
        d2[5*b+i, c] = -rel[i, a]
zero(d1 * d2)
print("PASS: universal source symmetric-presentation differential squares to zero")

# The physical symbolic Laurent matrix supplied by the parent proof. All its
# markings remain indeterminates, and determinants are exact exterior cubes.
R = sp.Matrix([
    [z/FB, 0, -3*x/FD],
    [x/(6*FB), -FC*y/(2*FB*FD), 0],
    [0, -z/FC, 0],
    [-y/FB, 0, 3*z/FD],
    [0, -3*x/FC, -9*y/FD],
])
normalized = {
    (0,1,2): x*x*z,
    (0,1,3): x*y*y-y*z*z,
    (0,1,4): FB*FD*x**3+3*FC**2*y*y*z,
    (0,2,3): x*y*z-z**3,
    (0,2,4): y*z*z,
    (0,3,4): x*x*y-x*z*z,
    (1,2,3): x*z*z,
    (1,2,4): x*y*z,
    (1,3,4): FB*FD*x*x*z+3*FC**2*y**3,
    (2,3,4): y*y*z,
}
for rows, n in normalized.items():
    det = sp.factor(R[list(rows), :].det())
    ratio = sp.cancel(det/n)
    assert not set(coords).intersection(ratio.free_symbols), (rows, ratio)
    num, den = sp.fraction(ratio)
    # A Laurent unit is a nonzero rational times a parameter monomial.
    assert len(sp.Poly(num, FB, FC, FD).terms()) == 1, (rows, ratio)
    assert len(sp.Poly(den, FB, FC, FD).terms()) == 1, (rows, ratio)
    zero(det-ratio*n)
n = normalized
zero((n[(0,1,4)]-3*FC**2*n[(2,3,4)])/(FB*FD)-x**3)
zero((n[(1,3,4)]-FB*FD*n[(0,1,2)])/(3*FC**2)-y**3)
zero(n[(1,2,4)]-n[(0,2,3)]-z**3)
zero(n[(0,1,3)]+n[(0,2,4)]-x*y*y)
zero(n[(0,3,4)]+n[(1,2,3)]-x*x*y)
assert {sp.Poly(v, x,y,z).total_degree() for v in n.values()} == {3}
print("PASS: all symbolic maximal minors and the exact ideal equality I3(R)=m^3")

t = sp.symbols("t")
numerator_H = 36*t**2-18*t**3+3*t
numerator_products = 45*t**2-27*t**3+3*t**4
zero(numerator_H-numerator_products-3*t*(1-t)**3)


def dimS(degree):
    return (degree+2)*(degree+1)//2 if degree >= 0 else 0


assert 36*dimS(1)-18*dimS(0)+3*dimS(2) == 108
assert 45*dimS(1)-27*dimS(0)+3*dimS(-1) == 108
assert 15*dimS(1)-15*dimS(0)+3*dimS(-1) == 30
# On P2, H1(O(n))=0 and h2(O(n))=dim S[-n-3].
assert dimS(-(-1)-3) == 0  # cubic left term O(-1)
assert dimS(-(-2)-3) == 0  # quadratic left term O(-2)
assert 3*dimS(-(-3)-3) == 3  # linear saturation defect
print("PASS: exact Hilbert-series defect is 3t, and cubic quotient has rank 30")
print("PASS: degree-three sheaf obstruction vanishes; degree-one defect is three")
print("ALL CHECKS PASSED (symbolic identities only; no specialization or rank experiment)")
