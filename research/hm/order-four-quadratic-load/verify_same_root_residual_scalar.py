#!/usr/bin/env python3
"""Differentiate universal symmetric tensors; no HM coefficients."""
from sympy import symbols,Matrix,diff,expand
z=symbols('z')
# Basis x^4,x^3y,x^2y^2,x y^3,y^4 of Sym^4 W.
# ell(z)^3*x, ell(z)^3*y and ell(z)^4.
f=Matrix([1,3*z,3*z*z,z**3,0])
g=Matrix([0,1,3*z,3*z*z,z**3])
h=Matrix([1,4*z,6*z*z,4*z**3,z**4])
def symprod(a,b): return (a*b.T+b*a.T)/2
ap=diff(symprod(f,g),z).subs(z,0)
bp2=diff(symprod(h,h),z,2).subs(z,0)
e=[Matrix.eye(5)[:,i] for i in range(5)]
S=symprod(e[1],e[1])
T=symprod(e[0],e[2])
assert ap==3*S+3*T
assert bp2==32*S+24*T
assert ap-bp2/8 == -S
print('PASS: same-root residual block equals b-second-derivative/8 modulo an actual square.')
print('No projection discarded a low component; no actual HM values evaluated.')
