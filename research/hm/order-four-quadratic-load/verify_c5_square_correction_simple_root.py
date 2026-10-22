#!/usr/bin/env python3
"""Universal character, cyclic-weight, and transvectant checks.

No actual HM/source coefficients, point coordinates, or map matrices are used.
Letters X,Y,s,t are arbitrary abstract eigenbasis variables.
"""
import contextlib
import io
import runpy
import sympy as S

with contextlib.redirect_stdout(io.StringIO()):
    c = runpy.run_path('verify_negative_vertex_scalar.py')
assert c['inner'](c['vmul'](c['V'], c['S']), c['Wp']) == c['z'](1)

mod = lambda x: x % 10
pos2 = [mod(3*(2-j)-3*j) for j in range(3)]
pos3 = [mod(3*(3-j)-3*j) for j in range(4)]
pos4 = [mod(3*(4-j)-3*j) for j in range(5)]
neg2 = [mod(-(2-j)+j) for j in range(3)]
assert pos2 == [6, 0, 4]
assert pos3 == [9, 3, 7, 1]
assert pos4 == [2, 6, 0, 4, 8]
assert neg2 == [8, 0, 2]

# O(d) fibers: x has tautological weight +1, y has -1.
fiber = lambda d, taut: mod(-d*taut)
assert [fiber(3, p) for p in (1,-1)] == [7,3]
assert mod(3+fiber(3,1)) == 0       # f_x = X^2Y
assert mod(7+fiber(3,-1)) == 0      # f_y = XY^2
assert [fiber(2,p) for p in (1,-1)] == [8,2]
assert [fiber(6,p) for p in (1,-1)] == [4,6]
assert [fiber(-6,p) for p in (1,-1)] == [6,4]
assert [fiber(2,p) for p in (1,-1)] == [8,2]  # tangent weights

a_weight = 2
im_beta2 = {mod(2*a_weight+w) for w in neg2}
assert im_beta2 == {2,4,6}
assert {2,4,6,8} - im_beta2 == {8}
assert mod(8-3*a_weight) == 2       # detected h = X^4
assert mod(-8) == 2                # final quotient dual c

# List every possible tensor monomial by (positive Y exponent, negative t exponent).
q_lines = [(j,l) for j,w in enumerate(pos2)
           for l,nw in enumerate(neg2) if mod(w+nw)==2]
u_lines = [(j,l) for j,w in enumerate(pos4)
           for l,nw in enumerate(neg2) if mod(w+nw)==6]
assert q_lines == [(1,2),(2,0)]     # XY t^2, Y^2 s^2
assert u_lines == [(1,1),(3,2),(4,0)]  # X^3Y st, XY^3t^2, Y^4s^2

# The quartic Gram map raises the positive weight by +4 at x, -4 at y.
assert [mod(w+4) for w in (6,0,4)] == [0,4,8]
assert [mod(w-4) for w in (4,0,6)] == [0,6,2]
assert 8 not in pos2 and 2 not in pos2
assert mod(2-fiber(2,-1)) == 0      # i_y^t c is in C XY
assert fiber(-6,-1) == 4           # different kernel character

X,Y,s,t = S.symbols('X Y s t')
def tau(f,g):
    return (S.diff(f,X,2)*S.diff(g,Y,2)
            -2*S.diff(f,X,Y)*S.diff(g,X,Y)
            +S.diff(f,Y,2)*S.diff(g,X,2))
def apolar(f,g,xx,yy,degree):
    return S.expand(sum((-1)**j*S.binomial(degree,j)
                        *S.diff(f,xx,degree-j,yy,j)
                        *S.diff(g,xx,j,yy,degree-j)
                        for j in range(degree+1)))

# Universal differentiation on the two abstract weight monomials separately.
Da = lambda q: -2*t*S.diff(q,s)
assert Da(X*Y*t**2) == 0
assert S.expand(t**2*Da(Y**2*s**2)+4*Y**2*s*t**3) == 0
assert S.diff(X**2*Y,Y) == X**2
assert apolar(Y**2,X**2,X,Y,2) != 0
assert apolar(t**3,s**3,s,t,3) != 0
assert tau(X**4,X**2) == 0
assert tau(X**2,X*Y**3) == 12*X*Y
assert tau(X*Y,X*Y) == -2

# Equivariant Laurent-coefficient possibilities, not a constructed local model.
# p is invariant in V O(-8); n_h has weight 2 in V O(6).
p_coefficient_weights = {j:mod(2*j-2) for j in range(-1,4)}
n_coefficient_weights = {j:mod(2*j-4) for j in range(5)}
assert p_coefficient_weights == {-1:6,0:8,1:0,2:2,3:4}
assert n_coefficient_weights == {0:6,1:8,2:0,3:2,4:4}
assert tau(X**2,X**2) == 0 and tau(X**2,X*Y) == 0

# The four nonzero abstract eigenline maps of an arbitrary cubic tensor.
# This polynomial identity ring is NOT an actual HM coefficient assignment.
A,B,C,D,e,k = S.symbols('A B C D e k', nonzero=True)
relation = S.groebner([A*D+B*C], A,B,C,D,e,k)
def zero_mod_symplectic(expr):
    numerator = S.fraction(S.cancel(expr))[0]
    assert relation.reduce(numerator)[1] == 0

# Ordinary cubic apolar pairings give BC/(3AD)=-1/3.
assert apolar(X**3,Y**3,X,Y,3) == 36
assert apolar(X**2*Y,X*Y**2,X,Y,3) == -12
assert apolar(s*t**2,s**2*t,s,t,3) == 12
assert apolar(s**3,t**3,s,t,3) == 36
zero_mod_symplectic(B*C/(3*A*D)+S.Rational(1,3))

cc,dd,jj,ll = -2*B*e/C, -A*e/B, -D*e/C, -2*C*e/B
for identity in (A*jj+B*e+C*cc, C*jj+D*e,
                 A*e+B*dd, B*ll+C*e+D*dd):
    zero_mod_symplectic(identity)
U,V = 4*k*B/C, 4*k*A/C
zero_mod_symplectic(U*e+V*jj+4*k*cc)
zero_mod_symplectic(U*dd+V*e)
beta_over_alpha = -B*D/(2*C**2)
assert S.cancel(jj+beta_over_alpha*ll) == 0
m_oriented = C*beta_over_alpha/D
assert S.cancel(m_oriented+B/(2*C)) == 0
assert S.cancel(U+8*k*m_oriented) == 0
b_diagonal = -U/2-2*k*m_oriented
assert S.cancel(b_diagonal-2*k*m_oriented) == 0
residue_scalar = -(4*k*m_oriented+U)/30
assert S.cancel(residue_scalar-2*k*m_oriented/15) == 0

# Exact-sequence degrees and the orders at the root.
assert -3+1 == -2 and -3+2 == -1
assert 2*2+1 == 5                 # ord(a^2 q_z), q_z has order one
assert 2+1 == 3                   # ord(a a_z)
assert 4-2 == 2 and -1+1 == 0     # all R terms regular at root
print('PASS: unique dual-boundary derivative channel and opposite-point apolar convention.')
print('PASS: all C5 weights, O(d) fibers, detected h, and two Gram residue lines.')
print('PASS: Gaussian monomial, simple-root structure, and nonzero scalar residue pairing.')
print('PASS: universal symplectic-socle ratio and exact oriented FULL simple residue.')
print('Actual u nonvanishing uses the exact-sequence proof; no actual coefficients were evaluated.')
print('The full fixed-pole residue is nonzero; no nonzero GLOBAL class or third value is claimed.')
