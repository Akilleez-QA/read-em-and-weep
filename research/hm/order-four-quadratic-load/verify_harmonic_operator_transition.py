#!/usr/bin/env python3
"""Universal formal polynomial transition identity, no actual-instance data."""
import sympy as s
import runpy
c=runpy.run_path('verify_harmonic_first_normal_product.py')
x,y,z,u,v,q=[c[t] for t in ('x','y','z','u','v','q')]
L,B=c['lift'],c['B']
def form(prefix,n):
    cs=s.symbols(f'{prefix}0:{n+1}')
    return sum(cs[i]*u**i*v**(n-i) for i in range(n+1))
p,aa,H,dp,bb=[form(n,d) for n,d in [('p',2),('c',2),('H',4),('dp',2),('b',4)]]
k11=B(p,aa,1,1)
k21=-2*B(p,bb,1,2)+B(p*p,aa,2,1)+B(p,p,1,1)*aa+B(H,dp,2,1)
actual11=L(bb-p*aa)-(L(bb)-L(p)*L(aa))
actual21=L(2*p*bb-p*p*aa-H*dp)-(2*L(p)*L(bb)-L(p)**2*L(aa)-L(H)*L(dp))
for actual,predicted in ((actual11,k11),(actual21,k21)):
    difference=s.expand(actual-q*L(predicted))
    assert s.reduced(difference,[q*q],x,y,z)[1]==0
f,g,k,r=s.symbols('f g k r')
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
K=s.Matrix([[k,0],[r,-k]])
assert s.expand(s.trace(N*K)-(2*f*g*k-f*f*r))==0
assert N*N==s.zeros(2)
print('PASS: universal harmonic operator transition, including B(p,p)c, and exact trace shadow.')
print('Every polynomial coefficient is an independent formal variable; no actual HM/source instance or rank evaluated.')
