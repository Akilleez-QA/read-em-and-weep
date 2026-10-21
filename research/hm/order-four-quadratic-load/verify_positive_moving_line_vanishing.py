#!/usr/bin/env python3
"""Universal local square-ideal identity and order/degree bookkeeping."""
import sympy as s
f,g,alpha,beta,gamma=s.symbols('f g alpha beta gamma')
row=s.Matrix([[f,g]]); col=s.Matrix([-g,f]); phi=s.Matrix([[alpha,beta],[gamma,-alpha]])
assert s.expand((row*phi*col)[0])==beta*f*f-2*alpha*f*g-gamma*g*g
z=s.symbols('z');f3,f5,g5,b0,b2,a0,c0=s.symbols('f3 f5 g5 b0 b2 a0 c0')
F=f3*z**3+f5*z**5;G=g5*z**5
rr=s.expand((b0+b2*z*z)*F*F-2*a0*F*G-c0*G*G)
c8=rr.coeff(z,8)
assert s.expand(c8-f3*(b2*f3+2*b0*f5-2*a0*g5))==0
assert [p for p in range(7) if p%2==0 and p>=3 and 6-p>=2]==[4]
assert 2-3==-1
print('PASS: actual lower expression is a square-ideal element; only bidegree(4,2) survives; its initial term contains f3 and requires O(-1) global coefficients.')
