"""Bounded free-jet verification only; no actual forms, points or ranks."""
import sympy as s
F1,F2,G,G1,G2,x,x1,x2,z,u,r,r1=s.symbols('F1 F2 G G1 G2 x x1 x2 z u r r1')
R=s.Rational
# Reduction modulo the unspecified F. Product rule for fg at F=0.
fg1=F1*G
fg2=F2*G+2*F1*G1
# Degrees fg=8, x=4, f^2=6, z=6.
B_fg_x=(-42*fg1*x1+12*fg2*x)/462
B_f2_z=60*F1**2*z/550
Tdiag=u*(-16*F1*G1+20*F2*G)/112
Tupper=u*F1**2/5
psi=2*Tdiag*x+2*u*B_fg_x+Tupper*z-u*B_f2_z
# Use r=2uGx and r'=2uG'x+2uGx'-uF'z, as forced by trace.
rmod=2*u*G*x
r1mod=2*u*G1*x+2*u*G*x1-u*F1*z
assert s.expand(psi-(72*F2*rmod-32*F1*r1mod)/352)==0
# Pure second-ideal symbol, using r=Fz modulo F.
assert s.expand((-32*F1**2*z)/352-(-4*F1**2*z)/44)==0
# Upper-triangular coefficient denominator and second-ideal lower coefficient.
assert 2*(10-1)*(2-1)*(10+2-1)==198
assert R(1,5)-R(60,550)==R(1,11)
print('PASS: first-ideal identity; second-ideal symbol; denominators. No instance evaluated.')
