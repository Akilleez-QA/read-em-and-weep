#!/usr/bin/env python3
"""Universal bookkeeping only. No actual HM coefficients or rank evaluations."""
from itertools import product
from math import gcd
from functools import reduce

# Norm polarization: e*d=6 and excluded degrees1,3 leave (e,d)=(3,2),(1,6).
assert [(6//d,d) for d in (1,2,3,6) if d not in (1,3)] == [(3,2),(1,6)]
assert (3-1)*(3-1) == 4
assert (6-1)*(6-2)//2 == 10
possible_branch = sorted({12*a+20*b+30*c+60*d for a,b,c,d in product(range(3),repeat=4)
                          if 12 <= 12*a+20*b+30*c+60*d <= 24})
assert possible_branch == [12,20,24]
assert [(r-4)//2 for r in possible_branch] == [4,8,10]
assert (3-1)*(5-1) == 8 < 10
assert 10-4 == 6

# A5 quotient signature for genus4.
solutions=[(a,b,c) for a,b,c in product(range(5),repeat=3) if 15*a+20*b+24*c==63]
assert solutions == [(1,0,2)]
assert 30+12+12 == 54
# 2g-2=-120+30+4*12+4*12.
assert -120+30+48+48 == 6
# Canonical pencils M,N; ramification classes 3M+N and M+3N.
assert (2*3+1,2*1+3) == (7,5)
# 12M=7M+5N gives exact possible torsion exponent5; nontriviality is geometric.
assert ((12-7),5) == (5,5)
assert (3*2)%5 == 1

# Picard presentation rows (2,-5,0),(0,5,-5): Smith torsion order5.
entries=[2,-5,0,0,5,-5]
minors=[10,-10,25]
assert reduce(gcd, map(abs,entries)) == 1
assert reduce(gcd, map(abs,minors)) == 5
assert reduce(gcd,[30,12,12]) == 6

# All rank3 degree0 splitting types with exactly3 global sections.
splits=[]
for a in range(-4,5):
 for b in range(-4,a+1):
  c=-a-b
  if c <= b and sum(max(k+1,0) for k in (a,b,c)) == 3:
   splits.append((a,b,c))
assert sorted(splits)==[(0,0,0),(1,0,-1),(2,-1,-1)]
print('PASS: norm degree, genus possibilities, signature (2,5,5), fifth-torsion arithmetic, and three splitting types.')
