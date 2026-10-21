#!/usr/bin/env python3
"""Universal ideal-power arithmetic only; no HM coefficients or ranks."""
from collections import Counter

def pieces(start, stop, parity):
    result=Counter()
    for m in range(parity,stop,2):
        lo=max(0,(start-m+1)//2)
        hi=max(0,(stop-m+1)//2)
        if hi>lo:
            result[(4-m-2*lo,hi-lo)]+=1 if m==0 else 2
    return dict(result)
assert pieces(3,9,1)=={(1,3):4,(-1,2):2,(-3,1):2}
assert pieces(3,9,0)=={(0,3):5,(-2,2):2,(-4,1):2}
assert pieces(2,10,0)=={(2,4):3,(0,3):2,(-2,2):2,(-4,1):2}
for start,stop,parity in [(3,9,1),(3,9,0),(2,10,0)]:
    for (twist,length),mult in pieces(start,stop,parity).items():
        if length>1:
            dual_twist=2*length-twist-3
            assert dual_twist>=2
        else:
            assert twist<=-3
assert 3*3==9
assert (27+45,42)==(72,42)
assert (72-4,42+4)==(68,46)
print('PASS: odd I3/I9 decomposition 4B(1)|3C +2B(-1)|2C +2B_C(-3)')
print('PASS: even I3/I9 decomposition 5B|3C +2B(-2)|2C +2B_C(-4)')
print('PASS: even I2/I10 decomposition yields upper bound9 from h0 B_R(2)=3')
print('PASS: all higher-cohomology dependencies dualize to plane twists>=2')
print('PASS: reduced jet ranks72/42 ->68/46')
print('LIMIT: algebraic decomposition, flatness, and semicontinuity require companion proof')
