#!/usr/bin/env python3
"""Only invented scalar Laurent examples; no imports of physical source."""
from fractions import Fraction as Q
import json

ZERO=(0,0,0,0)
E1=(-3,-3,-1,-1); E2=(-2,-2,-2,-2); E3=(-1,-1,-3,-3)

def clean(p): return {a:Q(c) for a,c in p.items() if c}
def add(p,q):
    r=dict(p)
    for a,c in q.items(): r[a]=r.get(a,0)+c
    return clean(r)
def scale(p,c): return clean({a:c*v for a,v in p.items()})
def mul(p,q):
    r={}
    for a,c in p.items():
        for b,d in q.items():
            e=tuple(x+y for x,y in zip(a,b)); r[e]=r.get(e,0)+c*d
    return clean(r)
def deriv(p,i):
    r={}
    for a,c in p.items():
        b=list(a); b[i]-=1; r[tuple(b)]=c*a[i]
    return clean(r)
def ensure(ok,label):
    if not ok: raise RuntimeError(label)
def trace(p): return p.get((-1,-1,-1,-1),Q(0))
def polynomial(p): return all(min(e)>=0 for e in p)

f={E1:Q(1),E2:Q(-1),E3:Q(1)}
p={(2,2,0,0):Q(1),(1,1,1,1):Q(2),(0,0,2,2):Q(1)}
g={(2,1,-3,-3):Q(1,2),(1,0,-2,-2):Q(1),(-1,-2,0,0):Q(-1),(-2,-3,1,1):Q(-1,2)}
h=mul(p,f)
ensure(h==deriv(g,0),'invented divergence identity')
ensure(trace(h)==0,'invented trace')
ensure(f[E1]+2*f[E2]+f[E3]==0,'weighted selector')
bad=add(f,{E2:Q(1)})
hbad=mul(p,bad)
ensure(trace(hbad)==2,'negative mutation trace')
ensure(hbad!=deriv(g,0),'negative mutation must reject original certificate')
# Explicit invented polynomial certificate N/D with G=A/Qden.
D={(3,3,3,3):Q(1)}
Qden={(2,3,3,3):Q(1)}
N=mul(D,f); A=mul(Qden,g)
ensure(polynomial(N) and polynomial(A),'invented numerator polynomialness')
lhs=mul(mul(p,N),mul(Qden,Qden))
rhs=mul(D,add(mul(Qden,deriv(A,0)),scale(mul(A,deriv(Qden,0)),-1)))
ensure(lhs==rhs,'denominator certificate interface')
Nbad=mul(D,bad)
ensure(mul(mul(p,Nbad),mul(Qden,Qden))!=rhs,'mutated interface rejected')
print(json.dumps({'status':'invented exact controls passed','weighted_coefficients':[1,-1,1],
 'trace':0,'mutated_trace':2,'denominator_interface':True,
 'physical_evaluations':0,'production_imports':0,'actual_matrix_polynomial_products':0},sort_keys=True))
