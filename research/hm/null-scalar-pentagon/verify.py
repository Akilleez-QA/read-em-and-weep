#!/usr/bin/env python3
"""Bounded formal identities only. Standard library; no model or physical data."""
from fractions import Fraction as F
from itertools import combinations, product

pairs=list(combinations(range(1,5),2))
n=len(pairs)
x={p:tuple(int(k==i) for k in range(n)) for i,p in enumerate(pairs)}
def lin(*terms):
    return tuple(sum(c*v[k] for c,v in terms) for k in range(n))
def b(i,j,k):
    return x[j,k] if i==0 else lin((1,x[j,k]),(-1,x[i,k]),(1,x[i,j]))
wedges=list(combinations(range(n),2))
def bracket(a,c):
    return tuple(a[i]*c[j]-a[j]*c[i] for i,j in wedges)
def wlin(*terms):
    return tuple(sum(c*v[k] for c,v in terms) for k in range(len(wedges)))
def C(i,j,k,l):
    return wlin((F(1,2),bracket(b(i,j,k),b(i,k,l))),(-F(1,2),bracket(b(j,k,l),b(i,j,l))))
verts=tuple(range(5))
dC=wlin(*[((-1)**i,C(*(verts[:i]+verts[i+1:]))) for i in range(5)])
expected=bracket(b(0,1,2),b(2,3,4))
assert dC==expected
assert wlin((1,dC),(-1,expected))==(0,)*len(wedges)
# Formal exponential coefficients cancel whenever a+d=e+f.
# Verify cubic identity in the polynomial ring Q[a,d,e], with f=a+d-e.
def padd(a,b):
    out=a.copy()
    for k,v in b.items(): out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
def pmul(a,b):
    out={}
    for i,u in a.items():
        for j,v in b.items():
            k=tuple(x+y for x,y in zip(i,j));out[k]=out.get(k,0)+u*v
    return {k:v for k,v in out.items() if v}
def scale(c,a): return {k:c*v for k,v in a.items() if c*v}
def cube(a): return pmul(pmul(a,a),a)
a={(1,0,0):F(1)};d={(0,1,0):F(1)};e={(0,0,1):F(1)}
f=padd(padd(a,d),scale(-1,e))
assert cube(padd(a,d))==cube(padd(e,f))
# XOR deck characters: every bivector/input/input combination stays P or Q.
P,Q=0b0011,0b1100
weights={r^s^t for r,s,t in product((P,Q),repeat=3)}
assert weights=={P,Q} and P^Q not in weights
assert {0^P,0^Q}=={P,Q}
print('PASS: free-bracket delta C = {b012,b234}; hence delta Psi = 0.')
print('PASS: ordinary cubic exponential terms cancel under delta b = 0.')
print('PASS: scalar weights of Psi lie in P/Q, excluding full-sign P xor Q.')
print('Scope: symbolic scalar identities only; no geometric/model evaluation or extension existence claim.')
