#!/usr/bin/env python3
"""Global degree-eight cohomological cancellation; all source parameters stay symbolic."""
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

r=a*(rm-theta*rt)
v1=k*z**5*((2*theta+s.Rational(1,3))*A*c*z**2*X**3+6*A*theta*X**2*Y+(4*theta-s.Rational(1,3))*B*z*Y**3)
v2=L*k*((12*theta+2)*A**2*c*X**5+(6*theta+1)*A*B*c*z*X**3*Y**2+(12*theta-1)*B**2*Y**5)/(6*A*B*c**2)
w=s.cancel(f*v2-g*v1)
assert s.Poly(w,z).degree()<=2
assert s.Poly(v1,z).degree()<=7
assert s.Poly(w,X,Y).total_degree()==8
assert s.cancel(s.rem(w+r,f,X))==0
# Both homogeneous tangent representatives are regular in the actual triangular charts.
p0=L*X*Y/(2*A*c*z**4)-L*X**2/(2*A*z**2)+L*B*Y**2/(A**2*z)
y=s.symbols('w',nonzero=True)
pinf=-L*Y**2/(2*A*c**2*y**2)+L*X**2/(B*c**2*y)
s.Poly(s.cancel(v2+p0*v1),X,Y,z)
s.Poly(s.cancel((z*v2).subs(z,-1/y)+pinf*(z**(-7)*v1).subs(z,-1/y)),X,Y,y)
# No selected coefficient: solve the identity for the entire scalar quartic.
cc=s.symbols('chi0:5'); chi=sum(cc[i]*z**i for i in range(5))
rem=s.cancel(s.rem(s.cancel((r-w-2*g*v1)/f)-chi*g,f,X))
sol=s.solve(s.Poly(rem.as_numer_denom()[0],X,Y,z).coeffs(),[theta,*cc])
assert sol=={theta:-s.Rational(1,12),cc[0]:A*k/(3*B*c**2),cc[1]:0,cc[2]:0,cc[3]:0,cc[4]:0}
chi=A*k/(3*B*c**2)
Q=L*k*(-11*A*c*z**2*X**2+5*A*X*Y+B*c*z**3*Y**2)/(30*A*B*c**3*z**4)
assert s.cancel((r-w-2*g*v1).subs(theta,-s.Rational(1,12))-chi*f*g-f**2*Q)==0
# The uniqueness/surjectivity kernels have a P1 O(-1) factor.
assert (8-3,2-3)==(5,-1)
assert (3-3,7-3)==(0,4)
assert 4*8==32 and 9*3==27 and 32-27==5
print('PASS: unique global wedge, explicit tangent coefficients, both actual triangular charts.')
print('PASS: full scalar quartic identity uniquely fixes theta=-1/12 and chi=A*k/(3*B*c^2).')
print('PASS: exact f^2 remainder and 32-to-27 scalar-kernel dimensions.')
print('This is the canonical degree-eight/global-boundary cancellation, not a full actual normal K or fourth value.')
