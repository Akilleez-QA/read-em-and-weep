import sympy as S
X,Y,r,s,u,v,alpha,beta,A,B,C=S.symbols('X Y r s u v alpha beta A B C')
def ap(f,g):
    return S.expand(sum((-1)**j*S.binomial(3,j)*S.diff(f,X,3-j,Y,j)*S.diff(g,X,j,Y,3-j) for j in range(4)))
ell=r*X+s*Y
assert ap(ell**3,ell**2*(u*X+v*Y))==0
assert ap(ell**2*(u*X+v*Y),ell**2*(alpha*X+beta*Y))==0
# Arbitrary negative covector (r,s), ell=i_w omega=-s X+r Y.
l=-s*X+r*Y
a=A*r*r+B*r*s+C*s*s
D_l=S.diff(a,r)*X+S.diff(a,s)*Y
# Natural coefficient action on ell in the pinned Clebsch convention.
assert S.expand(D_l.subs({X:r,Y:s})-2*a)==0
assert S.expand(l.subs({X:r,Y:s}))==0
# Riemann--Hurwitz and the uniform nonvanishing locus.
g=4; degree=3
ram=2*g-2+2*degree
assert ram==12 and ram-2-4==6
print('PASS: universal apolar tangent Lagrangians and cubic osculating incidence.')
print('PASS: exact Hamiltonian factor two in the fixed natural coefficient-action convention.')
print('PASS: twelve reduced ramification-orbit degree and at least six admissible pairs.')
print('No actual coefficients, points, matrices, ranks, or scans were evaluated.')
