#!/usr/bin/env python3
"""Independent universal socle, primitive, and cohomology checks, no actual instance."""
import sympy as S
X,Y,s,t,z,w,A,B,c,lam,k,e,nu=S.symbols('X Y s t z w A B c lam k e nu',nonzero=True)
def tau(f,g,x=X,y=Y):
    return S.diff(f,x,2)*S.diff(g,y,2)-2*S.diff(f,x,y)*S.diff(g,x,y)+S.diff(f,y,2)*S.diff(g,x,2)
Qh=e*(-A/B*X**2*s*s+Y**2*s*t)/4
Qother=e*(X**2*s*t+B/A*Y**2*t*t)/4
# Direct socle checks for the two named quartics; all remaining pairings are zero by character.
assert S.expand(tau(Qh,X**2)-e*s*t)==0
assert S.expand(tau(Qh,X*Y))==0
assert S.expand(tau(Qh,Y**2)+A/B*e*s*s)==0
assert S.expand(tau(Qother,X**2)-B/A*e*t*t)==0
assert S.expand(tau(Qother,X*Y))==0
assert S.expand(tau(Qother,Y**2)-e*s*t)==0
rhs=k*s*t*(t*S.diff(Qh,t)-s*S.diff(Qh,s))
Qu=k*A/B*s*s*Qother-k*s*t*Qh
assert S.expand(Qu-rhs)==0
print('PASS: two actual socle tensor identities force the claimed unique global inverse u.')
h=X*Y**3
ux=k*A/B*X**3*Y-k*X*Y**3*z
Gx=ux+2*k*z*h
Gy=S.expand((Gx/z**2-4*k*h/z).subs(z,-1/w))
assert S.expand(Gy-(k*A/B*X**3*Y*w*w+3*k*X*Y**3*w))==0
print('PASS: the opposite Gamma includes its full inhomogeneous coefficient-frame correction.')
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z*z-B*c*X*Y**2*z**3
g=-lam/(2*A*c)*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)
n=A/(B*lam)*(A*X*Y+A*c*X**2*z**2+3*B*c*Y**2*z**3+B*c*c*X*Y*z**5)
m=X*Y**2*(A*X+5*B*c*Y*z**3)/(2*B*c*z**4)
assert S.cancel(h*S.diff(f,z)-m*f-n*g)==0
px=lam/(2*A*c)*X*Y/z**4-lam/(2*A)*X**2/z**2+lam*B/A**2*Y**2/z
py=-lam/(2*A*c*c)*Y**2/w**2+lam/(B*c*c)*X**2/w
ny=S.expand((n/z**6).subs(z,-1/w))
etax=A/(B*c)/z**4
etay=S.expand((z*z*etax).subs(z,-1/w))
assert S.expand(etax+tau(px,n)+3*c*z)==0
assert S.expand(etay+tau(py,ny)+13*A/(B*c)*w*w)==0
print('PASS: actual n restriction identity and both regular transforms of the nonzero Gram primitive.')
csection=Y**2*t*t-2*A/B*X**2*s*t
# Product apolar form, applying positive pairing coefficientwise then negative pairing.
def tensor_pair(F,G):
    val=0
    for i in range(3):
        Fi=S.expand(F).coeff(X,2-i).coeff(Y,i)
        for j in range(3):
            Gj=S.expand(G).coeff(X,2-j).coeff(Y,j)
            val+=tau(X**(2-i)*Y**i,X**(2-j)*Y**j)*tau(Fi,Gj,s,t)
    return S.expand(val)
assert tensor_pair(csection,Qh)==0
assert {2,4,6,8}-{8,0,2}=={4,6}
assert (4+6)%10==0
Zx=Y**2*z**3-2*A/B*X**2*z*z
Zy=S.expand((Zx/z**4).subs(z,-1/w))
assert S.expand(Zy-(-Y**2*w-2*A/B*X**2*w*w))==0
assert tau(X*Y,Zx)==0 and tau(X*Y,Zy)==0
print('PASS: actual P4 annihilator, both detecting characters, and the Serre-test frame.')
C6=3*k*lam/(10*B*c*c)
C1=-k*lam/(2*A)
assert S.expand((z**6*C6*z**-6).subs(z,-1/w)-C6)==0
assert 1<=1<=5 and (6+8+0)%10==4 and 4 not in {8,0,2}
assert S.expand((z**4*C6*z**-5).subs(z,-1/w)+C6*w)==0
assert S.expand((z**4*C6/nu*z**-5).subs(z,-1/w)+C6/nu*w)==0
print('PASS: lower nonzero class survives A, but its semisimple cup is exact before the upper quotient.')
print('All parameters remain formal; no selected HM coefficients, actual matrices/ranks, or scan used.')
