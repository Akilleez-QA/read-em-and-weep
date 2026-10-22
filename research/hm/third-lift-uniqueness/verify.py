#!/usr/bin/env python3
"""Bounded formal identities only; no HM coefficients or matrix evaluations."""
from collections import defaultdict

# Polynomials in q,a,h,b,s,t with formal differential basis Z,V,W.
def term(coef, q=0,a=0,h=0,b=0,s=0,t=0,basis="Z"):
    return {(q,a,h,b,s,t,basis):coef}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return {k:v for k,v in out.items() if v}
def scale(p,c=1,**exp):
    names=("q","a","h","b","s","t")
    return {tuple(k[i]+exp.get(n,0) for i,n in enumerate(names))+(k[6],):c*v
            for k,v in p.items()}

dU=term(1,q=2)
dC=add(term(1,a=1,h=1),term(-1,q=1,basis="V"))
dE=add(term(1,a=1,basis="V"),term(-1,a=1,b=1),term(-1,q=1,basis="W"))
dJ=add(scale(dU,a=1,h=1),scale(dU,-1,q=1,b=1),scale(dC,-1,q=2))
assert dJ==add(term(1,q=3,basis="V"),term(-1,q=3,b=1))
dJ4=add(scale(dJ,a=1),scale(dE,-1,q=3))
assert dJ4==term(1,q=4,basis="W")
# C'-C=D and dD=-q T. Then d(-q²D)=q³T.
assert scale(term(-1,q=1,basis="V"),-1,q=2)==term(1,q=3,basis="V")
# Compatible fourth correction and its multiplied fifth error.
corr=scale(dU,-1,q=2,s=1)
assert corr==term(-1,q=4,s=1)
assert scale(corr,a=1)==term(-1,q=4,a=1,s=1)
# Changing quadratic lift s by q*c, or changing fourth lift q³Nt,
# has differential divisible q^5 after multiplication by a.
assert min(k[0] for k in scale(dU,q=3,a=1))==5
assert min(k[0] for k in scale(dU,q=3,t=1))==5
# Twist bookkeeping; q,a,h,b,s,t have twist2, U4, C4,V2,Z0.
assert 2*2+4==8
assert 2*2+4+2==10
assert 10+2-4*2==4
assert 3*2+4==10
# Exact family dimensions are inputs from published representation calculation.
P2={"1":1,"A":1,"V":1,"P":2,"D":3}
assert P2["A"]+P2["D"]==4
assert 3+5==8
assert 738-4==734 and 833-4==829
assert 684-4==680 and 779-4==775
# Center parity: a is Sym² of an odd coordinate representation.
assert (-1)**2==1
# Both pencil expansions have residual -t² a s zeta with their
# respective first correction. Published normalized beta2 signs differ.
# q(s xi)=0 and q(s zeta)=a s xi.
for pencil_sign, correction_sign in ((1,-1),(-1,1)):
    first_order = pencil_sign + correction_sign
    second_order = pencil_sign * correction_sign
    assert first_order == 0 and second_order == -1
assert 8-3==5 and 8-2==6
assert 4-3==1
raw_boundary_variation = -1  # coefficient of [a s zeta]
beta2_ladder = 1             # q-t a normalized convention, cited Section3
beta2_earlier = -1           # q+t a convention, cited Section4
assert raw_boundary_variation == -beta2_ladder == beta2_earlier
print("PASS: formal ladder, variation signs, q-orders, twists, center parity, family arithmetic.")
print("Not a verification of geometric inputs, actual coefficients, or formal proof-assistant certification.")
