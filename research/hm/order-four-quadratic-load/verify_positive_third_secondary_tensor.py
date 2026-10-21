#!/usr/bin/env python3
"""Universal polynomial bookkeeping for the secondary tensor; no HM data."""
import sympy as s
q,a,h,t=s.symbols('q a h t')
x,y,v,k,xi,zeta=s.symbols('x y v k xi zeta')
# Changing a representative of C and its q-division simultaneously.
x_new=x+q*y
v_new=v+h*y+k
assert s.expand(q*v_new-h*x_new-(q*v-h*x)-q*k)==0
assert s.expand(a*v_new-a*v-h*(a*y)-a*k)==0
# Thus qk=0 preserves the lift equation. Output changes by h(M_2)
# and a(K), both zero in P by separately proved geometric inputs.
# The actual third correction polynomial uses q xi=0, q zeta=a xi,
# and q v=a h zeta; verify its unreduced residual exactly.
residual=s.expand((q+t*a)*(h*xi-t*h*zeta+t**2*v)-t**3*a*v)
expected=h*q*xi+t*h*(a*xi-q*zeta)+t**2*(q*v-a*h*zeta)
assert s.expand(residual-expected)==0
# Degrees of the correction-free dual certificate.
deg_second=2
deg_lambda=3*deg_second
deg_eta=deg_lambda+1
deg_argument=1+1 # a times zeta_a, with h independent of a.
assert (deg_lambda,deg_eta,deg_eta+deg_argument)==(6,7,9)
# Dimensions of the actual lower cokernel, using the proved characters.
assert 41-((1+3+3+5)-1)==3+3*4+3*5==30
print('PASS: universal lift-change, representative-change, exact cubic residual,')
print('dual-certificate degrees, and lower-cokernel dimensions.')
print('Geometry (h M_2 subset q M_2 and a K subset q M_2) is an explicit input;')
print('this test evaluates no actual bundle coefficient or matrix rank.')
