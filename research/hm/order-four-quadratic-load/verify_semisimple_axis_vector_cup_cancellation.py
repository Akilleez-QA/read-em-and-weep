#!/usr/bin/env python3
"""Universal symbolic identities for arbitrary C5 symplectic tensor lines."""
# Load only the universal symbolic setup, never an actual source instance.
from verify_divisor_quintic_two_chart_cancellation import *
r=S.symbols('r')
f1=f.subs({X:1,Y:r})
n1=n.subs({X:1,Y:r})
nh=S.cancel(S.rem(r**3*n1,f1,r))*X**2
nh=S.expand(nh.subs(r,Y/X))
h=X*Y**3
mh=S.cancel((h*S.diff(f,z)-nh*g)/f)
assert not S.denom(mh).has(X,Y)
uh=k*A/B*X**3*Y-k*X*Y**3*z
Gh=uh+2*k*z*h
vh=A/(B*c)*z**(-4)


nhy=S.expand((nh/z**6).subs(sub));mhy=S.cancel((h*S.diff(fy,v)-nhy*gy)/fy)

def Rh(p,m,n,a,Gamma,v0,t):
 return S.expand(k*a*a*(-S.Rational(2,15)*tau(p,m)+S.Rational(2,5)*p*tau(p,n)+S.Rational(1,5)*tau(p,p)*n-S.Rational(1,15)*tau(h,S.diff(p,t))+S.Rational(2,3)*p*v0)-tau(p,Gamma)/30)
R1=Rh(px,mh,nh,z,Gh,vh,z)
Ghy=S.expand((Gh/z**2-4*k/z*h).subs(sub))
R2=Rh(py,mhy,nhy,-v,Ghy,S.expand((z*z*vh).subs(sub)),v)
Z=Y**2*z**3-2*A/B*X**2*z**2
Zy=S.expand((Z/z**4).subs(sub))

P1=S.expand(tau(R1,Z));P2=S.expand(tau(R2,Zy))
alpha1=3*k*l/(10*B*c*c)
alpha2=-k*l/(2*A)
assert regular(vh+tau(px,nh),z)
assert regular(S.expand((z*z*vh).subs(sub))+tau(py,nhy),v)
assert regular(R1-alpha1*X*Y/z**6-alpha2*X*Y/z,z)
assert regular(R2,v)
assert regular(P1,z) and regular(P2,v)
# Cup a=z. Its sole pole has a global meromorphic lift regular in the y chart.
assert regular(z*R1-alpha1*X*Y/z**5,z)
assert S.expand((z**4*(alpha1*X*Y/z**5)).subs(sub))==-alpha1*X*Y*v
print('PASS: universal semisimple operator relation, canonical correction, actual Gram primitives.')
print('PASS: exact two polar coefficients and vector-class exactness after cup a=st.')
print('No parameters are assigned actual values; no actual matrix or rank is evaluated.')
