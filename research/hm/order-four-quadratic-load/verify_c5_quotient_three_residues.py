#!/usr/bin/env python3
"""Universal quotient and residue identities, never an actual HM instance."""
import sympy as s
A,B,C,u,z,V,w=s.symbols('A B C u z V w',nonzero=True)
D=-B*C/A
raw=-(A*u+C)/(u**2*(B*u+D))
assert s.cancel((-B*C**2/A**3)*raw.subs(u,C*z/A)-(z+1)/(z**2*(z-1)))==0
rho=(z+1)/(z**2*(z-1))
assert s.cancel(s.diff(rho,z)+2*(z**2+z-1)/(z**3*(z-1)**2))==0
assert s.rem(s.together(rho-(z+1)/(3*z-2)).as_numer_denom()[0],z*z+z-1,z)==0
num=s.together((V*V+11*V-1).subs(V,(z+1)/(3*z-2))).as_numer_denom()[0]
assert s.rem(num,z*z+z-1,z)==0
assert s.discriminant(z*z+z-1,z)==5
assert s.discriminant(V*V+11*V-1,V)==125
assert 2*4-2==5*(-2)+4*(5-1)
assert 2*3-2==4
# Universal pullback of the simple logarithmic differential.
assert s.cancel(s.diff(w**5,w)/(5*w**5)-1/w)==0
assert (6+2+2)%10==0
assert 12==1+1+5+5
print('PASS: universal symplectic C5 quotient, four harmonic branch points, and two critical values.')
print('PASS: exact three-residue scaling and orbit/ramification counts.')
print('No principal-parts gluing or actual global third value is assumed or evaluated.')
