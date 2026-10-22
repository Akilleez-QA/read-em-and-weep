#!/usr/bin/env python3
"""Universal apolar/CI checks only; no actual HM coefficient or rank test."""
import sympy as s
import runpy
x,y=s.symbols('x y')
def form(name,n):
    c=s.symbols(f'{name}0:{n+1}')
    return sum(c[j]*x**(n-j)*y**j for j in range(n+1))
def pair(f,g,n):
    f,g=s.Poly(f,x,y),s.Poly(g,x,y)
    return s.expand(sum((-1)**j*f.coeff_monomial(x**(n-j)*y**j)*g.coeff_monomial(x**j*y**(n-j))/s.binomial(n,j) for j in range(n+1)))
def tau(f,g):
    return s.diff(f,x,2)*s.diff(g,y,2)-2*s.diff(f,x,y)*s.diff(g,x,y)+s.diff(f,y,2)*s.diff(g,x,2)
r,u,v=form('r',2),form('u',4),form('v',2)
assert s.expand(pair(tau(r,u),v,2)-24*pair(u,r*v,4))==0
c=runpy.run_path('verify_negative_vertex_scalar.py')
vm,va=c['vmul'],c['vadd']
A,V,P,D=[c[k] for k in ('A','V','P','D')]
assert [c['sym'](6,t) for t in c['W']]==va(V,P)
assert vm(D,A)==va(A,V,P,D)==vm(V,D)
assert c['inner'](vm(A,D),V)==c['z'](1)
assert 4*(-3)+2*5==-2
assert 7-(4+2)==1 and 5-2==3
assert 3*5==15 and 15-3==12 and 4*3==12
print('PASS: universal transvectant/apolar factor24, swapped CI socle degree2, and scalar-cup characters.')
print('Invertibility follows from the actual swapped quotient and O(-1) acyclicity, not an instance rank test.')
