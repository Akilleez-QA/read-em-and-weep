"""Exact abstract numerator-jet compression; no physical source inputs."""
from itertools import combinations, product
from math import comb
import json
import sympy as s

vertices=list(product((0,1),repeat=2))
jet=list(product(range(2),repeat=2))
def full_basis(q):
    m=3*(q+1)-2
    return [(I,a) for I in combinations(range(4),q+1) for a in product(range(m+1),repeat=2)]
def small_basis(q):
    return [(I,a) for I in combinations(range(4),q+1) for a in jet]
B=[full_basis(q) for q in range(3)]
C=[small_basis(q) for q in range(3)]
def D(q):
    target={v:i for i,v in enumerate(B[q+1])}; out=s.zeros(len(B[q+1]),len(B[q]))
    for j,(I,a) in enumerate(B[q]):
        for v,(x,y) in enumerate(vertices):
            if v in I: continue
            J=tuple(sorted(I+(v,))); out[target[J,(a[0]+3*x,a[1]+3*y)],j]=(-1)**J.index(v)
    return out

def Q(q):
    out=s.zeros(len(C[q]),len(B[q])); idx={v:i for i,v in enumerate(C[q])}
    for j,(I,a) in enumerate(B[q]):
        for b in jet:
            out[idx[I,b],j]=comb(a[0],b[0])*comb(a[1],b[1]) if all(b[i]<=a[i] for i in range(2)) else 0
    return out

def multiply(p,a):
    return {tuple(a[i]+b[i] for i in range(2)):c for b,c in p.items() if all(a[i]+b[i]<2 for i in range(2))}
polys=[{a:comb(3*x,a[0])*comb(3*y,a[1]) for a in jet if a[0]<=3*x and a[1]<=3*y} for x,y in vertices]
def small_D(q):
    out=s.zeros(len(C[q+1]),len(C[q])); idx={v:i for i,v in enumerate(C[q+1])}
    for j,(I,a) in enumerate(C[q]):
        for v in range(4):
            if v in I: continue
            J=tuple(sorted(I+(v,)))
            for b,c in multiply(polys[v],a).items(): out[idx[J,b],j]+=(-1)**J.index(v)*c
    return out
# Apex 3 has d=(1+t)^3(1+u)^3, inverse=1-3t-3u+9tu.
apex=3; inverse={(0,0):1,(1,0):-3,(0,1):-3,(1,1):9}
def H(q):
    out=s.zeros(len(C[q-1]),len(C[q])); idx={v:i for i,v in enumerate(C[q-1])}
    for j,(I,a) in enumerate(C[q]):
        if apex not in I: continue
        J=tuple(v for v in I if v!=apex)
        for b,c in multiply(inverse,a).items():out[idx[J,b],j]+=(-1)**I.index(apex)*c
    return out
D0,D1=D(0),D(1); Q0,Q1,Q2=[Q(q) for q in range(3)]
A0,A1=small_D(0),small_D(1); H1,H2=H(1),H(2)
assert Q0.rank()==16
assert Q1*D0==A0*Q0 and Q2*D1==A1*Q1
assert H2*A1+A0*H1==s.eye(24)
seed=s.Matrix([((7*i)%13)-6 for i in range(16)])
ebar=A1.T*seed
assert A0.T*ebar==s.zeros(16,1)
etabar=H2.T*ebar
e=Q1.T*ebar; eta=Q2.T*etabar
assert D1.T*eta==e and D0.T*e==s.zeros(16,1)
# Exact compression has only 12 closed rows, while full closed rows have dimension134.
assert A0.rank()==12 and A1.rank()==12
assert D0.rank()==16 and D1.rank()==134
out={'full_dimensions':[len(b) for b in B], 'jet_dimensions':[len(c) for c in C],
     'jet_algebra_dimension':4, 'full_closed_covector_dimension':134,
     'jet_closed_covector_dimension':12,'exact_intertwining':True,
     'exact_contraction':True,'exact_lifted_dual_residual_zero':True,
     'physical_source_evaluated':False}
print(json.dumps(out,indent=2))
