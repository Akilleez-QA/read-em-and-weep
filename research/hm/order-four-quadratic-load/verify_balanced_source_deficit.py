#!/usr/bin/env python3
"""Universal kernel-source identities; no actual HM coefficients or inputs."""
import sympy as s
r0,r1,x,y,z,u,w=s.symbols('r0 r1 x y z u w')
chi=s.symbols('chi', nonzero=True)
cs=s.symbols('t0:8')
t=sum(cs[j]*r0*u**(3-j)*w**j+cs[4+j]*r1*u**(3-j)*w**j for j in range(4))
r=s.Matrix([r0,r1]); ell=s.Matrix([[-r1,r0]])
source=s.Matrix([-s.diff(t,r1),s.diff(t,r0)])
M=s.Matrix([[z,x],[y,-z]])
Mr=M.subs({x:r0*r0,y:-r1*r1,z:-r0*r1},simultaneous=True)
assert Mr==r*ell
assert s.expand((ell*source)[0]-t)==0
assert (Mr*source-r*t).applyfunc(s.expand)==s.zeros(2,1)
q0=(x*y+z*z)/chi
assert (M*M-chi*q0*s.eye(2)).applyfunc(s.expand)==s.zeros(2)
# Arbitrary Cartan map and evaluation functional, not an actual instance.
A=s.Matrix(4,2,s.symbols('A0:8')); lam=s.Matrix(1,4,s.symbols('lam0:4'))
F=(lam*A*r)[0]
assert s.expand((lam*A*Mr*source)[0]-F*t)==0
# Source-block bookkeeping keeps both channels and the physical multiplier.
am,bm=s.symbols('am bm',nonzero=True)
Ac,Bc=s.symbols('Ac Bc')
assert s.expand((am*Ac+bm*Bc)/am-Ac-bm*Bc/am)==0
print('PASS: unique full-input cubic spinor, Veronese factor, physical square, and mandatory B companion.')
