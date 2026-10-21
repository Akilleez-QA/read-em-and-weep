#!/usr/bin/env python3
"""Universal polynomial-division identities only; no HM coefficients or rank tests."""
import sympy as s
u,v,z,S1,S2,r0,r1=s.symbols('u v z S1 S2 r0 r1')
P=z*z-S1*z+S2
ell=u+z*v
rem=s.rem(ell*(r0+z*r1),P,z)
A0=u*r0-S2*v*r1
A1=v*r0+u*r1+S1*v*r1
assert s.expand(rem-A0-z*A1)==0
assert s.expand(v*A0-u*A1+(u*u+S1*u*v+S2*v*v)*r1)==0
assert s.div(ell*(r0+z*r1),P,z)[0]==v*r1
# Generic degree7 formal polynomial, never actual bundle coefficients.
f=s.symbols('f0:8')
F=sum(f[i]*z**i for i in range(8))
r,t=s.symbols('r t')
Ps=(z-r)*(z-t)
H,R=s.div(F,Ps,z)
d=t-r
assert s.simplify(H.subs(z,r)-(F.subs(z,t)-F.subs(z,r)-d*s.diff(F,z).subs(z,r))/d**2)==0
assert s.simplify(H.subs(z,t)-(F.subs(z,r)-F.subs(z,t)+d*s.diff(F,z).subs(z,t))/d**2)==0
Hd,Rd=s.div(F,(z-t)**2,z)
assert s.simplify(Hd.subs(z,t)-s.diff(F,z,2).subs(z,t)/2)==0
assert s.simplify(s.diff(Hd,z).subs(z,t)-s.diff(F,z,3).subs(z,t)/6)==0
print('PASS: exact Cech remainders, quadratic boundary sign, divided differences, and full Hermite quotient coefficients.')
