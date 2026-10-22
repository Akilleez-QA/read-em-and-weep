"""Universal identities only; no actual HM coefficients or ranks."""
import sympy as s
x,y,z,u,A,B,c,k,alpha,beta=s.symbols('x y z u A B c k alpha beta', nonzero=True)
a=c*y
b=k*z*z
q=A*y*y+B*u*u
qc=alpha*q+beta*a*a
g=b*x-a*q
lift=qc*q-beta*a*b*x
assert s.expand(lift-(alpha*q*q-beta*a*g)) == 0
assert s.expand(lift.subs(z,0)-qc*q) == 0
assert s.expand((lift-qc*q).subs(z,0)) == 0
# Universal quotient after a=0, q=0, b=0, with nonzero c,k,B:
# C[z,u]/(z²,u²), represented by four standard monomials.
G=s.groebner([z*z,u*u],z,u)
for i in range(4):
    assert G.reduce(z**i*u**(3-i))[1] == 0
assert [20-14,6+2,8-35+27,4+8,20-12,63-33,30-8,27-22] == [6,8,0,12,8,30,22,5]
print('PASS: universal trace lifts, cubic Artinian vanishing, and dimension arithmetic')
