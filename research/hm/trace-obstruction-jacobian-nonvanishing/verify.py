#!/usr/bin/env python3
"""Bounded formal differential identity; no actual coefficient/point evaluation."""
import sympy as s
F,F1,F2,G,G1,G2,L,L1,u,t=s.symbols('F F1 F2 G G1 G2 L L1 u t')
f=(F,F1,F2);g=(G,G1,G2);l=(L,L1,0)
def mul(a,b):
    return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])
def tau(a,b,d,e):
    return s.expand(d*(d-1)*a[0]*b[2]-2*(d-1)*(e-1)*a[1]*b[1]+e*(e-1)*a[2]*b[0])
b=u*(tau(mul(f,g),mul(l,f),8,4)/s.Integer(462)-tau(mul(f,f),mul(l,g),6,6)/s.Integer(550))
coef=s.diff(b,L1)
assert s.expand(coef-u*F*(F1*G/3-F*G1/5))==0
bx=b.subs({L:1,L1:0}); by=b.subs({L:t,L1:1})
J=3*F*G1-5*F1*G
assert s.expand(t*bx-by-u*F*J/15)==0
# Euler Jacobian identity without any f,g coefficients.
assert s.expand((3*F-t*F1)*G1-F1*(5*G-t*G1)-J)==0
# Formal 2x2 determinant comparison used in the socle proof.
a,b0,c,d,X,Y=s.symbols('a b0 c d X Y')
M=s.Matrix([[a,b0],[c,d]])
v=s.Matrix([X,Y]); w=M*v
assert s.simplify(M.adjugate()*w-M.det()*v)==s.zeros(2,1)
print('PASS: harmonic Jacobian identity, normalization 1/15, Euler relation, adjugate identity.')
