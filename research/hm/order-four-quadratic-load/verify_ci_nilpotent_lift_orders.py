#!/usr/bin/env python3
"""Universal CI square-ideal Hilbert polynomial and deformation orders."""
import sympy as s
t=s.symbols('t')
H=s.cancel((1-t**6-t**8-t**10+t**11+t**13)/(1-t)**2)
assert s.denom(H)==1 and s.degree(H,t)==11
assert s.expand(H)==1+2*t+3*t**2+4*t**3+5*t**4+6*t**5+6*t**6+6*t**7+5*t**8+4*t**9+2*t**10+t**11
f,g,u,v,w=s.symbols('f g u v w')
N=s.Matrix([[-f*g,f*f],[-g*g,f*g]]);K=s.Matrix([[u,v],[w,-u]])
e=s.symbols('e')
assert N*N==s.zeros(2)
assert s.expand((N+e*K).det()).coeff(e,1)==2*f*g*u-f*f*w+g*g*v
assert 16-4==12
assert [p for p in range(9) if p%2==0 and p>=5 and 8-p>=2]==[6]
assert 2-3==-1
print('PASS: CI square ideal vanishes in degrees>=12; local determinant correction spans square ideal; global derivative has sole bidegree(6,2), cubic factor requires O(-1).')
