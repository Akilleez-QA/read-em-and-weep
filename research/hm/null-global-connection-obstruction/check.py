#!/usr/bin/env python3
"""Universal scalar arithmetic only: Q[t]/(t^5), no model imports or matrices."""
from fractions import Fraction as Q
from math import factorial
import json
from pathlib import Path
D=4
terms=((-5,-1),(15,1),(-10,3),(2,5))
f=[sum((Q(m*k**j,factorial(j)) for m,k in terms),Q(0)) for j in range(D+1)]
def mul(a,b):
    return [sum((a[k]*b[j-k] for k in range(j+1)),Q(0)) for j in range(D+1)]
end=mul(f,[(-1)**j*x for j,x in enumerate(f)])
assert f==[2,0,-15,0,Q(75,4)]
assert end==[4,0,-60,0,300]
# Total Chern class from log c = sum (-1)^(j-1)(j-1)! ch_j.
logc=[Q(0)]+[(-1)**(j-1)*factorial(j-1)*f[j] for j in range(1,D+1)]
powlog=[Q(1)]+[Q(0)]*D
c=powlog.copy()
for n in range(1,D+1):
    powlog=mul(powlog,logc)
    c=[x+y/factorial(n) for x,y in zip(c,powlog)]
assert c==[1,0,15,0,0]
assert 4*c[2]-c[1]**2==60
assert end[4]*24==7200
# Rank-two arbitrary line twist identity, coefficients in (b,a*l,l^2,a^2):
# 4(b+a*l+l^2) - (a+2*l)^2 = 4*b-a^2.
assert [4,4-4,4-4,-1]==[4,0,0,-1]
result={'ring':'Q[t]/(t^5); t represents theta in H^2',
        'signed_multiplicity_and_power':terms,
        'ch_F':[str(x) for x in f],
        'total_c_F':[str(x) for x in c],
        'ch_End_F':[str(x) for x in end],
        'discriminant_theta2':60,'theta4_integral':24,
        'HRR_End':7200,'discriminant_theta2_pairing':1440,
        'arbitrary_line_twist_discriminant_invariant':True,
        'scope':'Only universal truncated scalar polynomial arithmetic; no source matrices or actual jets.'}
p=Path(__file__).with_name('check-results.json')
p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
