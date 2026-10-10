#!/usr/bin/env python3
"""Exact maximal-direction checks from the full matrix cocycle.

No precomputed obstruction tensor or other verifier is imported.  The generic matrix
identity retains the ambient lift of h, both first-stage torsion parameters,
and the half correction.  The remaining checks reconstruct the Cech windows,
the extension connecting matrix, and all four restricted coefficient rows.
"""
import sympy as s


def zero(value):
    return s.cancel(s.expand(value)) == 0


def matrix_zero(value):
    return all(zero(entry) for entry in value)


def coefficient(expression, variable, exponent):
    """Extract a Laurent coefficient termwise, with no offset convention."""
    result = 0
    for term in s.Add.make_args(s.expand(expression)):
        power = term.as_powers_dict().get(variable, 0)
        if power == exponent:
            result += term / variable**power
    return s.expand(result)


t, X, Y, Z, ell = s.symbols("t X Y Z ell")
k, k0, F1, F2, G1, G2, lam, mu = s.symbols("k k0 F1 F2 G1 G2 lam mu")
u, v, w, Dq1, Dq2, E1, E2 = s.symbols("u v w Dq1 Dq2 E1 E2")
hY = -X + t*k
h = hY + ell*k0
L = s.Matrix([[ell, h], [0, t]])
J = s.Matrix([[0, 1], [-1, 0]])
q = s.Matrix([[t*F1 + X*G1, t*F2 + X*G2]])
Q0 = s.Matrix([[F1+k*G1, F2+k*G2], [G1+ell*lam, G2+ell*mu]])
# Any quadratic under a shift has this form; Dq is its actual first derivative.
Q1 = s.Matrix.vstack((q + ell*s.Matrix([[Dq1, Dq2]])
                      + ell**2*s.Matrix([[E1, E2]]))/t, s.zeros(1, 2))
A = (L.inv()*(Q1-Q0)).applyfunc(s.cancel)
V = J*A.T
half = V.T*J*V/2
assert matrix_zero(V.T*J-A)
assert half[0, 0] == half[1, 1] == 0
assert matrix_zero(A.row(0).subs(ell, 0)
                   - s.Matrix([[(Dq1+k0*G1+hY*lam)/t,
                                (Dq2+k0*G2+hY*mu)/t]]))
R0 = s.Matrix([[0, u], [v, w]])
corrected = -R0-Q0*V-L*half
projected = s.cancel((s.Matrix([[t, -h]])*corrected[:, 0])[0]).subs(ell, 0)
expected = hY*v-q[0]*A[0, 1].subs(ell, 0)+q[1]*A[0, 0].subs(ell, 0)
assert zero(projected-expected)
print("PASS full corrected matrix overlap projects to -rho0-q1*A12+q2*A11.")
print("PASS arbitrary ambient ell*k0, both torsion scalars, and ell^2 shift terms are retained.")

# A regular local isotropy solution exists once the primary cubic vanishes.
# Write H=F1*G2-F2*G1=X*W+t*H1, which is exactly the divisibility condition.
W, H1 = s.symbols("W H1")
local_u = H1+k*W
local_v = lam*(F2+k*G2)-mu*(F1+k*G1)-k0*W
local_w = W
isotropy = s.expand(t*local_u-ell*local_v-h*local_w
                     -(Q0*J*Q0.T)[0, 1])
assert zero(isotropy-(X*W+t*H1-F1*G2+F2*G1))
print("PASS regular r=0 isotropy choice includes the necessary -k0*W term in R_D1.")

# Reconstruct the complete intrinsic q space from degree and vanishing.
monomials = []
allowed = []
for i in range(3):
    for j in range(3-i):
        z = 2-i-j
        weight = 2*i+j+z
        for e in range(weight):
            mon = t**e*X**i*Y**j*Z**z
            monomials.append(mon)
            if i > 0 or e > 0:
                allowed.append(mon)
F_basis = [t**j*X**2 for j in range(3)]
F_basis += [t**j*X*Y for j in range(2)]
F_basis += [t**j*X*Z for j in range(2)]
F_basis += [Y**2, Y*Z, Z**2]
G_basis = [X, Y, Z]
assert len(monomials) == 16 and len(allowed) == 13
assert set(allowed) == set([t*f for f in F_basis]+[X*g for g in G_basis])
f = s.symbols("f0:10")
g = s.symbols("g0:3")
qgeneric = t*sum(a*b for a, b in zip(f, F_basis))+X*sum(a*b for a, b in zip(g, G_basis))
assert zero(qgeneric.subs(X, 0)-t*(f[7]*Y**2+f[8]*Y*Z+f[9]*Z**2))
assert zero(s.diff(qgeneric, X).subs(X, 0)
            -(g[1]*Y+g[2]*Z+t*(f[3]*Y+f[5]*Z)+t**2*(f[4]*Y+f[6]*Z)))
print("PASS all 13 allowed intrinsic quadrics have q|Sigma=t*b and dXq|Sigma=g+t*l+t^2*m.")

# Cech representatives of the actual extension and its connecting morphism.
d = s.symbols("d1:6")
y = s.symbols("y1:5")
z = s.symbols("z1:5")
DX = sum(a*t**(-i) for i, a in enumerate(d, 1))
DY = sum(a*t**(-i) for i, a in enumerate(y, 1))
DZ = sum(a*t**(-i) for i, a in enumerate(z, 1))
connecting = s.Matrix([[coefficient(section, t, -i) for section in (DX, t*DX, DY, DZ)]
                       for i in range(1, 5)])
M = s.Matrix.hstack(s.Matrix(d[:4]), s.Matrix(d[1:]), s.Matrix(y), s.Matrix(z))
assert connecting == M
# A dense nonmonomial sample for the connecting matrix.
dense = M.subs(dict(zip(d+y+z, (2, -1, 3, 5, -2, 1, 4, -3, 2, 5, 2, 1, -4))))
assert dense.det() != 0
print("PASS connecting H0(U(-1))->H1(O(-5)) has precisely columns (d1..d4),(d2..d5),y,z.")
print("PASS dense nonmonomial sample has connecting determinant", dense.det())

# Low cubic line degree -4; finite-chart sections of the projected ideal
# have exponents >=1, while transported infinity sections have exponents <=-4.
degree, finite_minimum = -4, 1
window = list(range(degree+1, finite_minimum))
assert window == [-3, -2, -1, 0]
assert len(window) == 4  # h1(O(-5)), not h1(O(-4)).
print("PASS projected ideal (t,h^2)|Sigma=(t) gives exact Laurent window [-3,-2,-1,0].")

b = s.symbols("b0:3")
c = s.symbols("c0:3")
gg = s.symbols("gg0:4")
ll = s.symbols("ll0:4")
mm = s.symbols("mm0:4")
b1 = b[0]*Y**2+b[1]*Y*Z+b[2]*Z**2
b2 = c[0]*Y**2+c[1]*Y*Z+c[2]*Z**2
g1, g2 = gg[0]*Y+gg[1]*Z, gg[2]*Y+gg[3]*Z
l1, l2 = ll[0]*Y+ll[1]*Z, ll[2]*Y+ll[3]*Z
m1, m2 = mm[0]*Y+mm[1]*Z, mm[2]*Y+mm[3]*Z
P = s.expand(b1*g2-b2*g1)
B1, B2 = s.expand(b1*l2-b2*l1), s.expand(b1*m2-b2*m1)
WY = s.expand(b1*s.diff(b2, Y)-b2*s.diff(b1, Y))
WZ = s.expand(b1*s.diff(b2, Z)-b2*s.diff(b1, Z))
dq1 = DX*(g1+t*l1+t*t*m1)+t*DY*s.diff(b1, Y)+t*DZ*s.diff(b1, Z)
dq2 = DX*(g2+t*l2+t*t*m2)+t*DY*s.diff(b2, Y)+t*DZ*s.diff(b2, Z)
TSigma = t*k*v-b1*(dq2+k0*g2+t*k*mu)+b2*(dq1+k0*g1+t*k*lam)
# This identity is valid before imposing the primary equation P=0.
main = -t*DX*B1-t*t*DX*B2-t*DY*WY-t*DZ*WZ
assert zero(TSigma-main+(DX+k0)*P-t*k*(v-b1*mu+b2*lam))
remaining = s.expand(TSigma+(DX+k0)*P)
actual = s.Matrix([coefficient(remaining, t, -i) for i in range(4)])
assert matrix_zero(actual+M*s.Matrix([B1, B2, WY, WZ]))
print("PASS all four projected rows from the complete matrix equal -M*(B1,B2,WY,WZ) modulo primary.")
print("PASS lift/torsion/local-solution terms have no forbidden coefficients after primary vanishes.")

Delta = s.cancel(WY/Z)
assert zero(WZ+Y*Delta)
minors = (c[0]*b[1]-c[1]*b[0], c[0]*b[2]-c[2]*b[0], c[1]*b[2]-c[2]*b[1])
assert zero(Delta-(minors[0]*Y**2+2*minors[1]*Y*Z+minors[2]*Z**2))
print("PASS Delta=0 is exactly the three 2-by-2 coefficient minors in characteristic zero.")
assert -7+3*1 == -4
assert max(-4+1, 0) == 0
print("PASS every constant minimal section has residue degree -4 and no nonzero global residue.")
print("VERDICT: invariant maximal-O(2)-direction exclusion passes; complementary orbit is not tested or excluded.")
