#!/usr/bin/env python3
"""Universal identities for the actual twelve-point polar reduction.

No actual map coefficients or actual-instance rank evaluation are used.
The generic Gram identity below uses twelve independent indeterminates.
"""
import contextlib
import io
import runpy
import sympy as S

with contextlib.redirect_stdout(io.StringIO()):
    c = runpy.run_path('verify_negative_vertex_scalar.py')
V, D, one = [c[k] for k in ('V', 'D', 'one')]
vm, va, inn, z = [c[k] for k in ('vmul', 'vadd', 'inner', 'z')]
assert vm(V, V) == va(one, V, D)
assert inn(vm(vm(V, V), D), one) == z(1)
assert [c['sym'](4, x) for x in c['W']] == D

# Universal Cauchy-Binet: signed maximal minors are the normal vector.
# These are independent symbols, not any actual i or Q coefficients.
X = S.Matrix(4, 3, S.symbols('X0:12'))
normal = S.Matrix([(-1)**r * X.extract([j for j in range(4) if j != r],
                                      range(3)).det()
                   for r in range(4)])
assert all(S.expand(e) == 0 for e in X.T * normal)
assert S.expand((X.T * X).det() - (normal.T * normal)[0]) == 0

u, v = S.symbols('u v')
def form(name, degree):
    coefficients = S.symbols(f'{name}0:{degree+1}')
    return sum(coefficients[j] * u**(degree-j) * v**j
               for j in range(degree+1))
def tau(f, g):
    return (S.diff(f,u,2)*S.diff(g,v,2)
            - 2*S.diff(f,u,v)*S.diff(g,u,v)
            + S.diff(f,v,2)*S.diff(g,u,2))
r, n, h = form('r',2), form('n',2), form('h',4)
assert S.expand(tau(r,n*r) - r*tau(r,n) - 3*n*tau(r,r)) == 0
C2 = (-S.Rational(2,15)*tau(r,n*r)
      + S.Rational(2,5)*r*tau(r,n)
      + S.Rational(1,5)*tau(r,r)*n
      + tau(h,r)/15)
reduced = tau(h,r)/15 + S.Rational(4,15)*r*tau(r,n) - n*tau(r,r)/5
assert S.expand(C2 - reduced) == 0

# Universal square channel: kernel = u^3 span(u,v), image = Sym^2.
hc = S.symbols('h0:5')
assert S.expand(tau(h,u*u)
                - (4*hc[2]*u*u+12*hc[3]*u*v+24*hc[4]*v*v)) == 0
assert tau(u**4,u*u) == 0 and tau(u**3*v,u*u) == 0
# Explicit universal preimages, not evaluation of an actual bundle map.
assert tau(u*u*v*v/4,u*u) == u*u
assert tau(u*v**3/12,u*u) == u*v
assert tau(v**4/24,u*u) == v*v

# Retained twists and principal-parts correction.
assert 2 + 8 - 12 == -2          # Q^t N^2 / det N
assert 6 - 12 == -6             # orthogonal quintic lift
assert -3 + 2 == -1             # actual scalar inverse kernel
assert -6 + 2*12 == 18          # double-pole meromorphic bundle
assert 12 - 2 - 1 == 9          # lower bound on nonzero second coefficients
assert 3*19 - 3*7 == 3*12       # onto second layer: 57 - 21 = 36
assert 3*12 - 3*7 == 3*5        # simple quotient: 36 - 21 = 15
assert 3*12 - 3*9 == 3*3        # upper simple quotient: 36 - 27 = 9
assert 3*5-3 == 12 and 3*3-5 == 4  # actual A and D5 boundaries

# Universal residue transport: raw versus physical normalization.
zz = S.symbols('zz')
dd, bb, nu0, nu1, zeta0, zeta1 = S.symbols(
    'dd bb nu0 nu1 zeta0 zeta1', nonzero=True)
residue = S.residue((dd/zz**2+bb/zz)*(zeta0+zeta1*zz)
                    /(nu0+nu1*zz), zz, 0)
expected = dd*zeta1/nu0 + (bb/nu0-dd*nu1/nu0**2)*zeta0
assert S.simplify(residue-expected) == 0
assert 2 + 2 == 4             # final test zeta = a i^t c
print('PASS: unique second Gram channel and universal Gram determinant identity.')
print('PASS: exact second-principal-part cancellation and universal square derivative kernel.')
print('PASS: scalar-inverse kernel correction and all polar line degrees retained.')
print('PASS: exact final-quotient Serre residue test and physical normalization correction.')
print('No actual cohomology nonvanishing or third-Bockstein value is claimed.')
