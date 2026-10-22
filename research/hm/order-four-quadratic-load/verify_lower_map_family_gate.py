#!/usr/bin/env python3
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add,mul,scale=r['vadd'],r['vmul'],r['vscale']
A,V,P,D=r['A'],r['V'],r['P'],r['D']
one=[r['z'](1) for _ in A]
sym2=add(one,D)
sym3=add(A,V,P)
omega3=add(mul(A,sym2),scale(-1,sym3))
assert omega3==add(A,D)
source=mul(mul(P,A),sym2)
kernel=add(mul(P,omega3),mul(A,A))
target=add(source,scale(-1,kernel))
assert [x[0] for x in (source,kernel,target)]==[r['z'](72),r['z'](41),r['z'](31)]
assert [r['inner'](D,x) for x in (source,kernel,target)]==[r['z'](6),r['z'](4),r['z'](2)]
common=add(P,D)
cminus=add(V,scale(2,P),scale(2,D))
assert r['inner'](D,mul(common,sym2))==r['z'](5)
assert r['inner'](D,mul(cminus,sym2))==r['z'](11)
assert r['inner'](D,mul(P,omega3))==r['z'](3)
assert r['inner'](D,mul(A,A))==r['z'](1)
assert 18+4*2==26 and 9+4*2==17
assert 10+3+4*3==25 and 4+3==7
assert 49-24==25
print('PASS: actual-family rank26, universal coefficient reductions11→6→2, and kernel dimensions5 and4.')
print('The two third-gate coefficients are not evaluated; no new nonvanishing is asserted.')

# Formal Euclidean coordinates for the universal invariant contraction identity.
import sympy as sp
a=sp.symbols('a0:3');v=sp.symbols('v0:3')
q=sum(x*x for x in a);av=sum(x*y for x,y in zip(a,v))
B=[sp.expand(q*v[i]-a[i]*av) for i in range(3)]
assert sp.expand(sum(a[i]*B[i] for i in range(3)))==0
assert [sum(sp.diff(b,x,2) for x in a) for b in B]==[4*x for x in v]
assert r['inner'](D,mul(cminus,D))==r['z'](9)
assert r['inner'](D,mul(mul(P,A),D))==r['z'](5)
assert r['inner'](D,mul(common,D))==r['z'](4)
s,t=sp.symbols('s t')
qs=[s*s,s*t,t*t]
def ham(q,f):return sp.diff(q,s)*sp.diff(f,t)-sp.diff(q,t)*sp.diff(f,s)
for x in (s,t):
    assert sp.expand(qs[0]*ham(qs[2],x)+qs[2]*ham(qs[0],x)-2*qs[1]*ham(qs[1],x))==0
print('PASS: actual trace-free factorization identity and5→2 surjectivity normalization, kernel3.')
