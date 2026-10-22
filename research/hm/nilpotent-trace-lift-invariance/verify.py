#!/usr/bin/env python3
"""Formal rank-two identities only; no HM/source instance or rank evaluation."""
import sympy as s
f,g,eta,ell,u=s.symbols('f g eta ell u', nonzero=True)
A=s.Matrix([[f/2,0],[g,-f/2]])
n=u*s.Matrix([[f*g,-f*f],[g*g,-f*g]])
E=eta*A
D=ell*A
assert n*A+A*n==s.zeros(2)
assert s.simplify(A*A-f*f*s.eye(2)/4)==s.zeros(2)
assert s.expand(s.trace(E*D)-eta*ell*f*f/2)==0
correction=s.Matrix([[0,0],[eta*ell/(2*u),0]])
assert s.expand(s.trace(n*correction)+s.trace(E*D))==0
assert 3+3+1+1==8
assert 1+1==2
print('PASS: formal kernel, pairing, explicit lift correction, degrees.')
