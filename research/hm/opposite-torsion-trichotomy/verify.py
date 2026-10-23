#!/usr/bin/env python3
"""Fixed abstract character arithmetic only; no HM instances or rank scans."""
from itertools import combinations_with_replacement, product

def require(test, label):
    if not test:
        raise RuntimeError(label)

# Coordinates 1,A,V,P,D; abstract C5 restriction weights.
weights=[{0},{0,1,4},{0,2,3},{1,2,3,4},{0,1,2,3,4}]
ind=[tuple(int(a in w) for w in weights) for a in range(5)]
require(ind[1]==ind[4] and ind[2]==ind[3], 'inverse induction characters')
H=(1,3,1,2,2)
I=ind[:3]
expected={(0,1):(0,1,0,1,0),(1,1):(1,1,1,0,0),(1,2):(1,2,0,0,0)}
allowed={}
for i,j in combinations_with_replacement(range(3),2):
    F=tuple(h-a-b for h,a,b in zip(H,I[i],I[j]))
    if min(F)>=0: allowed[i,j]=F
require(allowed==expected,'exact maximal-torsion character patterns')
require(all((b-a)%5 not in (1,4) for a in (1,4) for b in (1,4)), 'cyclic cotangent exclusion')
require([m for m in range(4) if 26-12*m>=0]==[0,1,2], 'orbit length budget')
for m in (0,1,2):
    require((31-12*m)-(26-12*m)==5,'rank preserved')
    require(12*m+(26-12*m)==26,'degree preserved')
dims=(1,3,3,4,5)
reps={d:[v for v in product(range(d+1),repeat=5) if sum(x*y for x,y in zip(v,dims))==d] for d in (3,4)}
A=(0,1,0,0,0); WW=(1,1,0,0,0); WWp=(0,0,0,1,0)
add=lambda u,v:tuple(x+y for x,y in zip(u,v))
patterns=[]
for key,ff in expected.items():
    candidates=[]
    for v in reps[4]:
        if add(A,v)==ff: candidates.append(('O2',v))
    for name,hh in [('W O1',WW),('Wp O1',WWp)]:
        for v in reps[3]:
            if add(hh,v)==ff: candidates.append((name,v))
    require(len(candidates)==2,'exactly two quotient bundles per character')
    patterns.append((key,candidates))
print('PASS: torsion lengths 0/12/24, three maximal characters, six degree-two bundles, cyclic middle-pattern exclusion.')
for row in patterns: print(row)
print('BOUNDARY: no actual coefficients, points, matrices, derivatives, ranks, source instances or large computation.')
