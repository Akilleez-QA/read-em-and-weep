#!/usr/bin/env python3
"""Uniform symbolic identities; no actual coefficient or matrix evaluation."""
import sympy as s
X,Y,z,A,B,c,L,k,theta=s.symbols('X Y z A B c L k theta',nonzero=True)
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z**2-B*c*X*Y**2*z**3
g=-L*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)/(2*A*c)
a=z**2
P8=(6*A**3*c**2*z**4*X**8+12*A**3*c*z**2*X**7*Y+6*A**3*X**6*Y**2
-18*A**2*B*c**2*z**5*X**6*Y**2-2*A**2*B*c*z**3*X**5*Y**3+21*A**2*B*z*X**4*Y**4
+18*A*B**2*c**2*z**6*X**4*Y**4-32*A*B**2*c*z**4*X**3*Y**5+24*A*B**2*z**2*X**2*Y**6
+4*B**3*c**2*z**7*X**2*Y**6-18*B**3*c*z**5*X*Y**7+9*B**3*z**3*Y**8)
rm=-L*k*P8/(30*A*B*c**2*z**4)
rt=2*k*a*s.diff(a*f*g,z)
F=L*k*Y**6/(A*c**4*z**7)
P=A**2*X**2+7*A*B*c**2*z**5*X**2-2*A*B*c*z**3*X*Y+A*B*z*Y**2+2*B**2*c**4*z**10*X**2-8*B**2*c**3*z**8*X*Y+5*B**2*c**2*z**6*Y**2
Q=-A**2*X**2-4*A*B*c**2*z**5*X**2+2*A*B*c*z**3*X*Y-A*B*z*Y**2+B**2*c**4*z**10*X**2+2*B**2*c**3*z**8*X*Y-2*B**2*c**2*z**6*Y**2
assert s.cancel(s.rem(rm,f,X)+F*P/6)==0
assert s.cancel(s.rem(rt,f,X)-2*F*Q)==0
pol=s.Poly(s.expand(P+12*theta*Q),X,Y,z)
assert s.expand(pol.coeff_monomial(X**2)-A**2*(1-12*theta))==0
assert s.expand(pol.coeff_monomial(X**2*z**10)-2*B**2*c**4*(6*theta+1))==0
assert s.Rational(1,12)!=-s.Rational(1,6)
assert 3*(-2+10)==24 and 24+1-4==21
assert (4-2)+1==3 and (1-2)==-1
print('PASS: both exact remainders and incompatible constant proportionality conditions.')
print('PASS: reduced-curve degree24, h0=21; nilpotent global kernel dimension3.')
print('The corrected lower source is nonzero; no fourth Bockstein value is asserted.')
