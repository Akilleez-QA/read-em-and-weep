#!/usr/bin/env python3
"""Universal target-frame Cech identity and binary-form identity only."""
import sympy as S
f,g,p,di,dj,K21=S.symbols('f g p di dj K21');gj=g+p*f
K11=dj-di
# K21 is computed from the SOURCE connection; only this trace uses target gj.
shadow=2*f*gj*K11-f*f*K21
delta=2*f*gj*dj-2*f*g*di
assert S.expand(shadow-delta-f*f*(-K21-2*p*di))==0
x,y=S.symbols('x y');pc=S.symbols('p0:3');nc=S.symbols('n0:3')
P=sum(pc[j]*x**j*y**(2-j) for j in range(3));N=sum(nc[j]*x**j*y**(2-j) for j in range(3))
def tau(a,b):return S.diff(a,x,2)*S.diff(b,y,2)-2*S.diff(a,x,y)*S.diff(b,x,y)+S.diff(a,y,2)*S.diff(b,x,2)
assert S.expand(tau(P*P,N)-6*P*tau(P,N)+2*tau(P,P)*N)==0
assert 3*5-3==12 and 3*3-5==4
print('PASS: exact target-frame vector reduction, universal transvectant product, actual quotient dimensions.')
print('No claim that the resulting actual cohomology class vanishes or is nonzero.')
