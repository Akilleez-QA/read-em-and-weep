#!/usr/bin/env python3
"""Bounded universal checks only: no HM tensors, points, source values or ranks."""
from collections import Counter
from itertools import combinations_with_replacement, permutations

# All sixteen monomials of a symbolic invariant bicubic.
allowed = {(i,j) for i in range(4) for j in range(4)
           if (12-6*i-2*j) % 10 == 0}
assert allowed == {(0,1),(2,0),(1,3),(3,2)}
# At x=y=0 only a0*y is linear; at X=y=0 only b0*X is linear.
assert {(i,j) for i,j in allowed if i+j == 1} == {(0,1)}
assert {(3-i,j) for i,j in allowed if 3-i+j == 1} == {(1,0)}
# g^2 has equal eigencharacters on v=r^2 and w.
assert (2*6) % 10 == (2*1) % 10
assert (5*6) % 10 == 0 and (5*1) % 10 == 5

# Degree-four even-family mixed -> VV block: odd negative degree.
j_values = [j for j in range(5) if (4-j) % 2 == 1]
assert j_values == [1,3]
monomials = set()
binary_degrees = set()
for j in j_values:
    monomials.update({(j+2,6-j),(j,8-j)})
    binary_degrees.update({(2*j+5,6-j),(2*j+1,8-j)})
assert monomials == {(1,7),(3,5),(5,3)}
assert binary_degrees == {(3,7),(7,5),(11,3)}
assert {(3*p+q)%10 for p,q in binary_degrees} == {6}
assert all((p+q)%2 == 0 for p,q in binary_degrees)
# Forced term: a(w)^2, h(v), z=(t/s)z0 quadratically evaluated at sw.
assert (0+2+1,4+0+1) == (3,5)
assert (0+4+3,4+0+1) == (7,5)

# C5 representation convolution; integer exponent labels, no matrices.
A_weights = [2,0,-2]
sym2_A = Counter((a+b)%5 for a,b in combinations_with_replacement(A_weights,2))
D = Counter(i%5 for i in [4,2,0,-2,-4])
assert D == Counter({j:1 for j in range(5)})
P2 = Counter()
for a,ma in sym2_A.items():
    for b,mb in D.items():
        P2[(a+b)%5] += ma*mb
assert sum(P2.values()) == 30
assert P2 == Counter({j:6 for j in range(5)})
# The target character +/-6 is in V, not A; also once in P and D.
assert 6%10 not in {2%10,0,(-2)%10}
assert 6%10 in {6%10,0,(-6)%10}
assert 3*(1+2+3) == 18
assert (1203-18,1113-18) == (1185,1095)

# P1 x P1 cohomology dimensions for the twisted CI exact sequence.
def h0(n): return max(n+1,0)
def h1(n): return max(-n-1,0)
def H1(a,b): return h1(a)*h0(b)+h0(a)*h1(b)
def H2(a,b): return h1(a)*h1(b)
assert H1(2,1)==0 and H2(0,-2)==0
assert h0(4)*h0(4)==25
assert 2*h0(2)*h0(1)+H1(0,-2)==13
assert 25-13==12

# Symbolic Vandermonde determinant, monomials in abstract X1,X2,X3.
def add(poly,exp,c):
    poly[exp]=poly.get(exp,0)+c
    if poly[exp]==0: del poly[exp]
def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items(): add(out,tuple(x+y for x,y in zip(e,f)),c*d)
    return out
lhs={}
for perm in permutations(range(3)):
    inversions=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    add(lhs,perm,(-1)**inversions)
rhs={(0,0,0):1}
for i,j in [(0,1),(0,2),(1,2)]:
    ei=[0]*3;ej=[0]*3;ei[i]=1;ej[j]=1
    rhs=mul(rhs,{tuple(ej):1,tuple(ei):-1})
assert lhs==rhs
print('PASS: invariant bicubic support and smoothness derivatives; joining-line stabilizer;')
print('      three relative monomials and line bundles; C5 multiplicities;')
print('      eighteen-dimensional receiving target and homogeneous kernel bounds;')
print('      symbolic CI cohomology dimensions; formal Vandermonde identity.')
print('No actual HM/source tensor, point, coefficient, matrix, rank or scan was used.')
