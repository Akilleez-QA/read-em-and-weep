#!/usr/bin/env python3
"""Universal derivation/frame identities; no actual-source coefficients."""
import sympy as s
f,g,p,df,dg,dp,a,az,k,z,w,dw = s.symbols('f g p df dg dp a az k z w dw')
r=k*a*(df*g+f*dg-2*az*f*g)
gp=g+p*f
dgp=dg+dp*f+p*df
rp=k*a*(df*gp+f*dgp-2*az*f*gp)
quot=k*a*(g*g*(dp+2*az*p)-2*p*g*dg)-p*p*r
assert s.expand(rp*g*g-r*gp*gp-f*f*quot)==0
n=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
dn=n.diff(f)*df+n.diff(g)*dg
R=k*a*(dn-2*az*n)
assert all(s.expand(x)==0 for x in n*R+R*n)
# w is here a formal Euler-degree-eight coefficient, not the chart coordinate.
Dy=z*z*dw-4*a*z*w
ay=a/z**2
azy=az-2*a/z
ry=k*ay*(Dy-2*azy*z*z*w)
rx=k*a*(dw-2*az*w)
assert s.simplify(ry-rx)==0
# Generic change-of-frame differentiation is encoded by the universal commutator.
B=s.Matrix(2,2,s.symbols('b0:4'))
assert all(s.expand(x)==0 for x in n*(B*n-n*B)+(B*n-n*B)*n)
print('PASS: finite double-cubic source change, tangent equation, exact base covariance.')
print('PASS: scalar-frame-independent commutator tangent identity.')
print('No actual endpoint or fourth Bockstein value is asserted.')
