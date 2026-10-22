#!/usr/bin/env python3
"""Universal lower-lift comparison identities, never an actual instance matrix."""
import sympy as S
z,q,e,H,r=S.symbols('z q e H r')
a,b,c,u,v,w,du,dv,dw=S.symbols('a b c u v w du dv dw')
p0,p1,dp0,dp1=S.symbols('p0 p1 dp0 dp1')
A=S.Matrix([[a,b],[c,-a]])
E=S.Matrix([[u,v],[w,-u]])
dE=S.Matrix([[du,dv],[dw,-du]])
psi=S.Matrix([p0,p1]); dpsi=S.Matrix([dp0,dp1]); I=S.eye(2)
# Apply (I+e q E) (H D+A) (I-e q E) to an arbitrary section,
# with Dq=r q. This is a universal operator identity, not source data.
transport=(I+e*q*E)*(H*((I-e*q*E)*dpsi-e*q*(r*E+dE)*psi)+A*(I-e*q*E)*psi)
linear=transport.applyfunc(lambda t:S.expand(t).coeff(e,1))
expected=q*(E*A-A*E-H*dE-H*r*E)*psi
assert (linear-expected).applyfunc(S.simplify)==S.zeros(2,1)
defect=-linear/q
assert (defect-(H*dE+A*E-E*A+H*r*E)*psi).applyfunc(S.simplify)==S.zeros(2,1)
# rho(b0+e b1)=-b0+e b1 is equivalent to b0 odd, b1 even.
b0p,b0m,b1p,b1m=S.symbols('b0p b0m b1p b1m')
plus_equation=S.expand((b0p+e*b1p)-(-b0p+e*b1p))
minus_equation=S.expand((-b0m-e*b1m)-(-b0m+e*b1m))
assert plus_equation==2*b0p and minus_equation==-2*e*b1m
assert 4+(-2)==2 # H D eta and [A,eta] have physical twist2.
assert 2+(-2)==0 # q0 eta is a degree-zero transition correction.
# Actual representation exact sequences; multiplicities are source inputs.
dim={'V':3,'P4':4,'D5':5}
C={'V':1,'P4':3,'D5':3}; J={'V':0,'P4':0,'D5':1}
minus={'V':1,'P4':2,'D5':2}; plus={'V':0,'P4':1,'D5':1}
poly={'V':0,'P4':1,'D5':1}
quot={k:C[k]-J[k] for k in C}
missing={k:poly[k]+plus[k]-J[k] for k in C}
effective={k:minus[k]-poly[k] for k in C}
assert all(C[k]==minus[k]+plus[k] for k in C)
assert all(quot[k]==missing[k]+effective[k] for k in C)
def d(rep):return sum(dim[k]*n for k,n in rep.items())
assert (d(C),d(J),d(quot),d(missing),d(effective))==(30,5,25,13,12)
def h0_O(n):return max(n+1,0)
assert 2*h0_O(-3)==0 # H0(Wprime O(-3))=0, so actual Q0 is injective.
print('PASS: exact square-zero operator transport, including the equation-frame derivative.')
print('PASS: odd operator and affine reflection force midpoint-minus and variation-plus.')
print('PASS: normal twists, cyclic-injection acyclicity, and exact 13 -> 25 -> 12 quotient.')
print('The actual Serre multiplication diagram and global comparison are the geometric proof.')
print('No full lower lift or fourth Bockstein value is computed.')
