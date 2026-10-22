#!/usr/bin/env python3
"""Bounded abstract representation arithmetic, no actual-family data."""
from itertools import product

# Coordinates: A,V,P,D. All arrays are character multiplicities.
v4=((0,1,1,1),(0,1,1,1),(1,1,1,1),(2,1,1,1))
c2=((1,2),(1,2),(2,2),(3,2))
c3=((1,1,1),(1,1,1),(2,1,1),(1,2,2))
d10=((0,1,1,0),(0,1,0,1),(0,0,1,1),(1,0,1,1))
# D10 coordinates: trivial, epsilon, E1, E2.
c5=((1,1,0,0,1),(1,0,1,1,0),(0,1,1,1,1),(1,1,1,1,1))
def total(m, table):
    return tuple(sum(m[i]*table[i][j] for i in range(4)) for j in range(len(table[0])))
def dominates(a,b): return all(x>=y for x,y in zip(a,b))
def passes(m):
    return dominates(total(m,v4),(1,2,2,2)) and dominates(total(m,d10),(0,1,1,1))
all_m=list(product(range(2),range(3),range(3),range(3)))
assert len(all_m)==54
passing=[m for m in all_m if passes(m)]
minimal=[m for m in passing if not any(n!=m and dominates(m,n) for n in passing)]
expected={(1,0,1,0),(0,1,1,0),(1,0,0,1),(0,1,0,1)}
assert set(minimal)==expected
assert all(dominates(total(m,c2),(3,3)) and dominates(total(m,c3),(1,2,2)) and dominates(total(m,c5),(1,1,1,1,1)) for m in passing)
assert all(passes(m)==any(dominates(m,n) for n in expected) for m in all_m)
dim=lambda m:sum(a*b for a,b in zip(m,(3,3,4,5)))
assert min(map(dim,passing))==7
assert {m for m in passing if dim(m)==7}=={(1,0,1,0),(0,1,1,0)}
assert not passes((1,2,0,0))
assert not passes((0,0,2,2))
assert all(passes(m)==(m[0]+m[1]>=1 and m[2]+m[3]>=1) for m in all_m)
print('PASS: 54 abstract multiplicity tuples; four minimal supports; dimension >=7.')
print('Passing necessary tests:',len(passing))
print('Minimal supports:',sorted(minimal))
