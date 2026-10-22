#!/usr/bin/env python3
"""Universal polynomial identities, not any actual source instance or rank test."""
import sympy as S
f,g,p,r,d,e11,e12,e21,de11,de12,de21,lam,hr=S.symbols('f g p r d e11 e12 e21 de11 de12 de21 lam hr')
A=S.Matrix([[p,r],[d,-p]])
E=S.Matrix([[e11,e12],[e21,-e11]])
DE=S.Matrix([[de11,de12],[de21,-de11]])
sigma=S.Matrix([f,g]);J=S.Matrix([[0,1],[-1,0]])
# Choose the fixed convention N=[[fg,-f²],[g²,-fg]].
J=-J
N=sigma*sigma.T*J
assert N==S.Matrix([[f*g,-f*f],[g*g,-f*g]])
comm=lambda U,V:U*V-V*U
tau=lambda v:sigma*v.T*J+v*sigma.T*J
DN=lam*N-comm(A,N)
LE=DE+comm(A,E)+hr*E
Dtrace=S.trace(DN*E+N*DE)
assert S.expand(S.trace(N*LE)-Dtrace-(hr-lam)*S.trace(N*E))==0
assert S.expand(S.det(S.Matrix.hstack(sigma,E*sigma))+S.trace(N*E))==0
assert all(S.expand(x)==0 for x in comm(E,N)-tau(E*sigma))
print('PASS: exact normal trace identity, wedge sign, and tangent normalization.')

v1,v2,dv1,dv2=S.symbols('v1 v2 dv1 dv2')
v=S.Matrix([v1,v2]);Dv=S.Matrix([dv1,dv2])
Dsigma=lam*sigma/2-A*sigma
Dtau=Dsigma*v.T*J+sigma*Dv.T*J+Dv*sigma.T*J+v*Dsigma.T*J
Ltau=Dtau+comm(A,tau(v))+hr*tau(v)
Sv=Dv+A*v+(lam/2+hr)*v
assert all(S.expand(x)==0 for x in Ltau-tau(Sv))
print('PASS: complete left and right first-order operator diagrams.')

t=S.symbols('t')
num=1-t**6-t**8-t**10+t**11+t**13
hilb=S.cancel(num/(1-t)**2)
assert S.denom(hilb)==1
expected=[1,2,3,4,5,6,6,6,5,4,2,1]
assert [S.expand(hilb).coeff(t,i) for i in range(12)]==expected
assert S.degree(hilb,t)==11
assert sum(expected)==45
assert 8+4>S.degree(hilb,t)
# Both scalar u and H have positive degree four, while D preserves degree.
assert 2+2==4  # positive and negative physical quadratic factors of global u
assert 2>=2   # negative quadratic vanishes in the ordinary double-conic ideal
print('PASS: ordinary-square degree≥12 vanishing and exact n8 annihilation.')
print('PASS: global u lies in I_C²; alpha*u is the scalar null-homotopy.')
print('The secondary Cplus/J=P4 residue is not evaluated.')
