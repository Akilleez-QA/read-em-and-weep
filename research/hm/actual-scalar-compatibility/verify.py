#!/usr/bin/env python3
"""Bounded formal scalar identities only; no actual source evaluation."""
import sympy as S
q,r,z,kappa=S.symbols('q r z kappa', nonzero=True)
c0,c1,c2,h,b=S.symbols('c0 c1 c2 h b')
alpha=c0+c1*z+c2*z*z
a=r*r*alpha
u=r*r*(c0+c1*(z-kappa*q/r**2)+c2*(z-kappa*q/r**2)**2)
assert S.expand(u-a+kappa*q*S.diff(alpha,z)).coeff(q,0)==0
assert S.expand(u-a+kappa*q*S.diff(alpha,z)).coeff(q,1)==0
F=S.expand((a*h-q*b)*u)
assert S.expand(F.coeff(q,0)-a*a*h)==0
assert S.expand(F.coeff(q,1)+a*b+kappa*a*h*S.diff(alpha,z))==0
# h has positive binary weight four; a,b and the negative derivative have weight zero.
eps=S.symbols('eps')
F1=-a*b-kappa*a*(eps**4*h)*S.diff(alpha,z)
assert F1.coeff(eps,0)==-a*b
K0,d,aa,bb=S.symbols('K0 d aa bb')
s0=-aa*bb
assert S.expand(K0+aa*s0*d-(K0-aa**2*bb*d))==0
print('PASS: free quadratic Taylor coherence modulo q².')
print('PASS: exact F0/F1 expansion with retained connection term.')
print('PASS: positive degree zero is -ab, not the degree-four connection term.')
print('PASS: canonical-source substitution in the immutable slope law.')
