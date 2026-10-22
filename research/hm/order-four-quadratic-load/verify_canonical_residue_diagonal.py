#!/usr/bin/env python3
"""Universal operator identity, not an actual HM instance."""
import sympy as S
x,y=S.symbols('x y'); a,az,k,u0=S.symbols('a az k u0')
def form(name,d):
    cs=S.symbols(f'{name}0:{d+1}')
    return sum(cs[i]*x**i*y**(d-i) for i in range(d+1))
def tau(f,g):
    return S.diff(f,x,2)*S.diff(g,y,2)-2*S.diff(f,x,y)*S.diff(g,x,y)+S.diff(f,y,2)*S.diff(g,x,2)
p,pz,n=form('p',2),form('z',2),form('n',2)
# mh is SOURCE m_h,i; target m_h,j=mh-p*n is NOT substituted.
h,mh,u=form('h',4),form('m_source',4),form('u',4)
H=k*a*h
m=2*k*a*a*mh+S.Rational(3,2)*k*a*az*h
Lam=2*k*a*az*h-u
b=Lam/2-m; c=-2*k*a*a*n; Dp=2*a*pz+az*p
K11=tau(p,c)/6
K21=-tau(p,b)/15+tau(p*p,c)/30+tau(p,p)*c/6+tau(H,Dp)/30
U=2*tau(p,mh)/15-tau(p*p,n)/15-tau(p,p)*n/3+tau(h,pz)/15
assert S.expand(K11+k*a*a*tau(p,n)/3)==0
assert S.expand(K21-k*a*a*U-tau(p,u+2*k*a*az*h)/30)==0
wf,wp=S.symbols('wf wp'); wg=wf+wp
assert S.expand(-(wf+wg)+2*wf+wp)==0
kap,H0,uu=S.symbols('kap H0 uu'); gamma=-uu/2
assert S.expand(2*gamma+4*kap*H0-(-uu+4*kap*H0))==0
print('PASS: exact canonical-residue diagonal, harmonic cochain, and frame-weight cancellation.')
print('The scalar-extension correction remains; no actual third value is asserted.')
