#!/usr/bin/env python3
"""Universal double-root jet identities; no actual boundary values selected."""
import sympy as s
h,u0,u1=s.symbols('h u0 u1')
b=s.symbols('b0:4')
poly=sum(b[i]*h**i/s.factorial(i) for i in range(4))*(u0+h*u1)
quot=s.expand((poly-poly.subs(h,0)-h*s.diff(poly,h).subs(h,0))/h**2)
J0=quot.subs(h,0)
J1=s.diff(quot,h).subs(h,0)
assert s.expand(J0-b[2]*u0/2-b[1]*u1)==0
assert s.expand(J1-b[3]*u0/6-b[2]*u1/2)==0
# Linear boundary symbols, with delta(b1)=0 and delta'(b1)=-delta(b2).
c,d,e=s.symbols('c d e')
reduced=-c*u0
nilpotent=-(d/6+e/2)*u0+c*u1
assert s.diff(reduced,u1)==0 and s.diff(reduced,u0)==-c
assert s.diff(nilpotent,u1)==c
# Scalar projection on any target coordinate with c != 0 has determinant -c^2.
M=s.Matrix([[s.diff(reduced,u0),s.diff(reduced,u1)],
            [s.diff(nilpotent,u0),s.diff(nilpotent,u1)]])
assert s.expand(M.det()+c*c)==0
# Pure embedding c(h)=(ell+h*v)^2*(u0+h*u1) includes derivative correction.
ell,v=s.symbols('ell v')
source=(ell+h*v)**2*(u0+h*u1)
assert s.diff(source,h).subs(h,0)==ell**2*u1+2*ell*v*u0
print('PASS: exact Hermite quotient, varying-boundary columns, and pure-source derivative correction.')
print('Conditional only: no actual leading boundary c is evaluated or declared nonzero.')
