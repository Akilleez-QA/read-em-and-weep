#!/usr/bin/env python3
"""Generic symbolic binary forms only, never actual HM coefficients."""
import sympy as s
a,b=s.symbols('a b')
fcoef=s.symbols('f0:4');gcoef=s.symbols('g0:6');pcoef=s.symbols('p0:3')
f=sum(fcoef[i]*a**(3-i)*b**i for i in range(4))
g=sum(gcoef[i]*a**(5-i)*b**i for i in range(6))
p=sum(pcoef[i]*a**(2-i)*b**i for i in range(3))
def jac(x,y): return s.diff(x,a)*s.diff(y,b)-s.diff(x,b)*s.diff(y,a)
def hes(x): return s.hessian(x,(a,b))
def mix(U,V): return U[0,0]*V[1,1]+U[1,1]*V[0,0]-2*U[0,1]*V[0,1]
HF,HG,HP=hes(f),hes(g),hes(p)
j=jac(f,p)/15
F,H=s.diff(f,a)/3,s.diff(f,b)/3
G,K=s.diff(g,a)/5,s.diff(g,b)/5
J1,J2=s.diff(j,a)/3,s.diff(j,b)/3
kappa=H*J1-F*J2
Rlower=2*(K*J1-G*J2)+2*p*kappa+j*j
t=mix(HF,HG)/240;ss=-HF.det()/36;r=HG.det()/400
HGnew=hes(g+p*f)
tnew=mix(HF,HGnew)/240;rnew=HGnew.det()/400
L=mix(HF,HP)/144
assert s.expand(mix(HF,HGnew)-mix(HF,HG)-4*p*HF.det()-f*mix(HF,HP))==0
assert s.expand(jac(f,jac(f,p))-s.Rational(3,2)*(f*mix(HF,HP)-p*HF.det()))==0
assert s.expand(kappa+tnew-t+p*ss+f*L)==0
assert s.expand(Rlower+rnew-r-2*p*t+p*p*ss+2*(g+p*f)*L)==0
print('PASS: exact generic quintic-generator correction is -L [[f,0],[2(g+pf),-f]].')
print('All coefficients are universal independent indeterminates; no actual HM instance or rank.')
# Track the canonical harmonic lift instead of silently fixing a quotient representative.
x,y,z=s.symbols('x y z')
def even2(poly):
    P=s.Poly(s.expand(poly),a,b)
    return sum(P.coeff_monomial(a**(2-i)*b**i)*[x,y,z][i] for i in range(3))
def even4(poly):
    P=s.Poly(s.expand(poly),a,b)
    bas=[x*x,x*y,(x*z+2*y*y)/3,y*z,z*z]
    return sum(P.coeff_monomial(a**(4-i)*b**i)*bas[i] for i in range(5))
fv=s.Matrix([even2(F),even2(H)])
jv=s.Matrix([even2(J1),even2(J2)])
gv=s.Matrix([even4(G),even4(K)])
gnew=s.Matrix([even4(s.diff(g+p*f,a)/5),even4(s.diff(g+p*f,b)/5)])
p0=even2(p)
delta=s.Matrix([-y*jv[0]-z*jv[1],x*jv[0]+y*jv[1]])
E=(gnew-gv-p0*fv-delta).applyfunc(lambda v:s.cancel(v/(x*z-y*y)))
assert all(not el.has(x,y,z) for el in E)
e=s.expand(a*E[0]+b*E[1])
# Report the exact relative constant without selecting any form coefficients.
ratio=s.cancel(e/L)
print('Canonical harmonic even-lift correction has e/L =',ratio)
assert ratio==-8
assert s.Rational(1,144)*9==s.Rational(1,16)
import runpy
from pathlib import Path
rr=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
assert rr['inner'](rr['Wp'],rr['S'])==rr['z'](0)
assert rr['inner'](rr['one'],rr['vmul'](rr['Wp'],rr['S']))==rr['z'](0)
print('PASS: the invariant Wprime O(-5) residue cohomology is zero.')
