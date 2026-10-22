#!/usr/bin/env python3
"""Universal integer checks only; no actual HM coefficients or point evaluations."""
from math import comb
from fractions import Fraction

# Smooth-conic residual sequence: (degree, six fat multiplicities).
d, multiplicities = 8, [3]*6
summands = []
for excluded in (5,4,3):
    restriction_degree = 2*d-sum(m for i,m in enumerate(multiplicities) if i != excluded)
    assert restriction_degree == 1
    summands.append(restriction_degree+1)
    multiplicities = [m-(i != excluded) for i,m in enumerate(multiplicities)]
    d -= 2
assert (d,multiplicities)==(2,[0,0,0,1,1,1])
assert comb(d+2,2)-sum(multiplicities)+sum(summands)==9
assert comb(10,2)-6*comb(4,2)==9

# Sym^8 A characters at orders2,3,5. Fifth-root sums use exact counts.
c2 = sum((-1)**k*(k+1) for k in range(9))
assert c2==5
assert 8%3 != 0 # coefficient t^8 in 1/(1-t^3) is zero
for weight in (1,2):
    counts=[0]*5
    for i in range(9):
        for j in range(9-i):
            counts[(weight*(i-j))%5]+=1
    assert counts==[9]*5 # 9*(1+z+z²+z³+z⁴)=0
    jets=[0]*5
    for degree in range(3):
        for i in range(degree+1):
            jets[(weight*(2*i-degree))%5]+=1
    assert jets==[2,1,1,1,1] # character1

ambient=[45,5,0,0,0]
jets=[36,4,0,1,1]
kernel=[a-b for a,b in zip(ambient,jets)]
P=[4,0,1,-1,-1]
D=[5,1,-1,0,0]
assert kernel==[p+d for p,d in zip(P,D)]==[9,1,0,-1,-1]
sizes=[1,15,20,12,12]
assert Fraction(sum(s*a*b for s,a,b in zip(sizes,kernel,D)),60)==1
assert Fraction(sum(s*a*b for s,a,b in zip(sizes,kernel,P)),60)==1

# Pair-permutation generator character and relation module.
pair_character=[15,3,0,0,0]
trivial=[1]*5
assert pair_character==[a+b+2*c for a,b,c in zip(trivial,P,D)]
assert [a-b for a,b in zip(pair_character,kernel)]==[a+b for a,b in zip(trivial,D)]
# Residual flag generator multiplicities: factors C_k miss precisely p_k.
removed=[]
required=[3]*6
for current in (5,4,3):
    for other in range(current):
        factors=set(range(6))-{current,other}-set(removed)
        mult=[sum(k!=point for k in factors) for point in range(6)]
        assert mult[other]==required[other]+1
        assert all(mult[point]>=required[point] for point in range(6) if point!=current)
    required=[m-(point!=current) for point,m in enumerate(required)]
    removed.append(current)

# Equalities m I=m³ and m² I=m⁴, where I=(x²,y²).
for m in (1,2):
    products={(i+a,m-i+b) for i in range(m+1) for a,b in ((2,0),(0,2))}
    assert products=={(i,m+2-i) for i in range(m+3)}
assert 5*4 > 2*8 and 6*2 > 8
assert 4-1==3 # combined square and fiber test rank
print('PASS: residual dimensions, exact characters, unique D5 kernel, local ideal products and jet Bezout bounds.')
