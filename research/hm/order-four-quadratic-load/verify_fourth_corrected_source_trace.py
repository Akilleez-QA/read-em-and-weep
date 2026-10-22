#!/usr/bin/env python3
"""Universal symmetric tensor contraction, with all coefficients formal."""
import sympy as s
x,y,z,u,v,w,g=s.symbols('x y z u v w gamma')
a1,a2,a3=s.symbols('a1 a2 a3')
# Generic trace-free symmetric tensor, not an HM matrix instance.
# b entries are written explicitly so no actual map/rank is evaluated.
b=[x*a1+u*a2+v*a3,u*a1+y*a2+w*a3,v*a1+w*a2-(x+y)*a3]
t11,t22,t33,t12,t13,t23=s.symbols('T11 T22 T33 T12 T13 T23')
# Formal symmetric multiplication tensor T; its trace vanishes.
products=[a1*t11+a2*t12+a3*t13,a1*t12+a2*t22+a3*t23,a1*t13+a2*t23+a3*t33]
Q=g*sum(bi*pi for bi,pi in zip(b,products))
trace=sum(s.diff(Q,a,2)/2 for a in (a1,a2,a3))
expected=g*(x*t11+y*t22-(x+y)*t33+2*u*t12+2*v*t13+2*w*t23)
assert s.expand(trace-expected)==0
assert s.expand(expected.subs(t33,-t11-t22))!=0
print('PASS: Tr(b zeta)=gamma T(S_h), hence corrected-source trace is -gamma T(S_h).')
print('Actual nonzero status uses the proved nonzero correction and second symbol; no fourth value inferred.')
