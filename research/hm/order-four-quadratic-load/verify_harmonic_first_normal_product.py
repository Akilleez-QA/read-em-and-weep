#!/usr/bin/env python3
"""Universal monomial identities only; no HM/source coefficients."""
import sympy as s
from functools import lru_cache
x,y,z,u,v=s.symbols('x y z u v')
q=x*z-y*y
lap=lambda p:s.diff(p,x,z)-s.diff(p,y,2)/4
@lru_cache(None)
def lift_monomial(i,j):
    m=(i+j)//2; b=i%2
    P=x**((i-b)//2)*y**b*z**((j-b)//2)
    out=P; c=s.Integer(1); derivative=P
    for r in range(1,m//2+1):
        derivative=lap(derivative)
        c=-c/(r*(s.Rational(2*m+1,2)-r))
        out+=c*q**r*derivative
    out=s.expand(out)
    assert s.expand(lap(out))==0
    assert s.expand(out.subs({x:u*u,y:u*v,z:v*v})-u**i*v**j)==0
    return out

def lift(p):
    return s.expand(sum(c*lift_monomial(i,j) for (i,j),c in s.Poly(p,u,v).terms()))
def trans(p,r):
    return s.diff(p,u,2)*s.diff(r,v,2)-2*s.diff(p,u,v)*s.diff(r,u,v)+s.diff(p,v,2)*s.diff(r,u,2)
def B(p,r,m,n):
    return s.expand(trans(p,r)/(2*(2*m-1)*(2*n-1)*(2*m+2*n-1)))
count=0
for m in range(4):
 for n in range(4):
  for i in range(2*m+1):
   for j in range(2*n+1):
    p=u**i*v**(2*m-i); r=u**j*v**(2*n-j)
    difference=s.expand(lift(p)*lift(r)-lift(p*r)-q*lift(B(p,r,m,n)))
    assert s.reduced(difference,[q*q],x,y,z)[1]==0
    count+=1
f,g,K12,K21=s.symbols('f g K12 K21')
assert s.rem(s.rem(K12*g*g+K21*f*f,f*f,f),g*g,g)==0
print(f'PASS: {count} universal harmonic product basis identities modulo q^2; diagonal gauge terms vanish modulo (f^2,g^2).')
print('No actual HM coefficients, actual-instance matrix, or rank evaluation used.')
