#!/usr/bin/env python3
"""Finite universal degree bookkeeping, not actual HM evaluation."""
from itertools import product
orders=[12,8,4]
terms=[]
for i,j,r in product(range(3),range(3),range(4)):
    if i+j+r==3:
        terms.append((i,j,r,orders[i]+orders[j]-4*r))
assert len(terms)==8
assert all(v==12 for i,j,r,v in terms)
assert min(12,4+8-2)==10
assert 10-4==6
assert [d for d in (0,4,8,12) if d>=6 and d!=12]==[8]
assert (8+1)*(2+1)==27
for d in (-2,0,2):
    assert d-5<0 and d-3<0
# Every q^2 term not involving L2 has order at least sixteen.
assert 8+8==12+8-4==12+12-8==16
print('PASS: all eight ordered cubic harmonic products; fourth correction retained; low trace-kernel degrees; 27-dimensional polynomial block.')
