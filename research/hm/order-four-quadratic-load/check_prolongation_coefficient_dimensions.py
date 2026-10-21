#!/usr/bin/env python3
"""Universal tensor identities only; no HM coefficients or actual-rank test."""
from fractions import Fraction

def rank(rows):
    a=[list(map(Fraction,row)) for row in rows]
    r=0
    for c in range(len(a[0])):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        d=a[r][c];a[r]=[x/d for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                d=a[i][c]
                a[i]=[x-d*y for x,y in zip(a[i],a[r])]
        r+=1
    return r

for s in range(1,5):
    # Normal form a=sum_{i<s} p_i tensor v_i. Coefficients of j(a).
    rows=[]
    for i in range(4):
        for j in range(i,4):
            v=[0]*20
            if j<s: v[i*5+j]+=1
            if i<s: v[j*5+i]+=1
            rows.append(v)
    got=rank(rows)
    expected=s*(9-s)//2
    assert got==expected,(s,got,expected)
    print(f'tensor rank {s}: coefficient-span dimension {got} PASS')
print('Only universal normal-form tensors checked; no actual adjoint corank asserted.')
