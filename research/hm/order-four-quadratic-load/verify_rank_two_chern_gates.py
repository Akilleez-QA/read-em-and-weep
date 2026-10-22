#!/usr/bin/env python3
"""Universal necessary Hilbert/Chern arithmetic, not an actual HM rank test."""
import json

def chi(a,b,t):
    return t*t+(a+3)*t+2+(a*a+3*a)//2-b

def allowed(a,b):
    if a%2 or (b-a//2)%2:
        return False
    defect=b-(a//2)**2
    return defect>=0 and defect%2==0

# Twice maximal slope; equality excluded for irreducible multiplicities.
rows=[(6,True),(7,True),(12,False),(18,False),(8,True),(14,False),(18,False)]
maxima=[2*((10+a-int(strict))//2) for a,strict in rows]
assert maxima == [14,16,22,28,16,24,28]
report=[]
for d in range(6,29,2):
    total=55+d*d-10*d
    kernel_lower=max(d*d//4,(d*d-11*d+60)//2) if d<14 else d*d//4
    pairs=[(n,total-n) for n in range(kernel_lower,total-(d-10)**2//4+1)
           if allowed(-d,n) and allowed(d-10,total-n)]
    for n,i in pairs:
        assert n+i+(-d)*(d-10)==55
        # A quadratic integer polynomial has even values at all integers iff
        # its value and its first two forward differences at zero are even.
        for a,b in [(-d,n),(d-10,i)]:
            assert chi(a,b,0)%2==0 and (a+4)%2==0 and 2%2==0
    report.append(dict(d=d,eligible_types=[j+1 for j,m in enumerate(maxima) if d<=m],
        kernel_c2_values=[n for n,i in pairs], image_c2_values=[i for n,i in pairs]))
assert len(report)==12
print(json.dumps({'type_d_maxima':maxima,'necessary_pairs_only':report},indent=2))
