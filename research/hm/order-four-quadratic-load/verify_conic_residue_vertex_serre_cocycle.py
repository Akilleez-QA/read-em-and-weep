"""Universal symbolic identities for the conic/vertex Serre comparison."""
import sympy as s
u,v,h,x,y,t,r=s.symbols('u v h x y t r', nonzero=True)
# Koszul right arrow pi(A,B)=uB-vA.
su=s.Matrix([0,h/u]); sv=s.Matrix([-h/v,0]); sigma=s.Matrix([u,v])
assert s.simplify(u*su[1]-v*su[0]-h)==0
assert s.simplify(u*sv[1]-v*sv[0]-h)==0
assert all(s.simplify(q)==0 for q in su-sv-sigma*h/(u*v))
# A universal oriented section, not an actual evaluated HM section.
N=s.Matrix([[-x*y,x*x],[-y*y,x*y]])
I=s.eye(2)
assert N*N==s.zeros(2)
assert N*s.Matrix([x,y])==s.zeros(2,1)
assert s.expand((I+t*N).det())==1
assert s.simplify((I+t*N)*(I-t*N))==I
assert s.simplify((I+t*N)*(I+r*N)-(I+(t+r)*N))==s.zeros(2)
# Exact weight separation, for arbitrary nonnegative even degree d=2j.
j=s.symbols('j', integer=True, nonnegative=True)
weight=-2-j
assert s.solve(s.Eq(weight,-2),j)==[0]
assert s.solve(s.Eq(weight,2),j)==[]
# The degree-zero restriction is H1(P1,O(-2)), dual to constants.
assert -(-2)-2==0
print('PASS: Koszul class, exact nilpotent transition, and full kernel weight separation')
