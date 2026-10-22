#!/usr/bin/env python3
import sympy as s
f,g,a,b,t=s.symbols('f g a b t')
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
sigma=s.Matrix([f,g]); I=s.eye(2)
P=I+s.Matrix([[a*g,-a*f],[b*g,-b*f]])
assert s.expand(P.det()-1-a*g+b*f)==0
assert (P-I)*sigma==s.zeros(2,1)
assert s.simplify(P.subs({a:f*t,b:g*t})-I-t*N)==s.zeros(2)
assert N*N==s.zeros(2)
assert s.expand((I+t*N).det())==1
assert s.simplify((I+t*N)*N*(I-t*N)-N)==s.zeros(2)
print('PASS: regular-pair determinant-one stabilizer is I+tN; its square-zero lift fixes N exactly.')
print('Universal identities only; no actual source coefficient or rank evaluation.')
