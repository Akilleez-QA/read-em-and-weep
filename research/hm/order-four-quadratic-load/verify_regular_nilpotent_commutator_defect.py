#!/usr/bin/env python3
import sympy as s
f,g,p,t=s.symbols('f g p t')
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
S1=s.Matrix([[f,0],[2*g,-f]])
S2=s.Matrix([[g,-2*f],[0,-g]])
H=s.diag(1,-1); E=s.Matrix([[0,1],[0,0]]); F=E.T
zero=s.zeros(2)
assert s.trace(N*S1)==s.trace(N*S2)==0
for A,R in [(H,g*S1-f*S2),(E,-g*S2),(F,-f*S1)]:
    assert (N*A-A*N-R).applyfunc(s.expand)==zero
P=s.Matrix([[1,0],[p,1]])
for A,R in [(N,P*N*P.inv()),(S1,P*S1*P.inv()),(S2,P*(S2-p*S1)*P.inv())]:
    assert (A.subs(g,g+p*f)-R).applyfunc(s.expand)==zero
series=s.cancel((t**3+t**5-t**6-t**8-t**10+t**16)/(1-t)**2)
assert s.denom(series)==1
assert series.subs(t,1)==45
assert s.expand(series).coeff(t,4)==2
assert s.expand(series).coeff(t,8)==6
print('PASS: all commutator and generator-change identities; length45 and degrees4,8.')
print('The regular-sequence and Hilbert–Burch arguments are proved in the accompanying note.')
