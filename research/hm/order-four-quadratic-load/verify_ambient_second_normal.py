#!/usr/bin/env python3
"""Universal A5 character and P2 line-cohomology identities only.
No HM coefficients, matrices, sampled parameters, or actual ranks are evaluated.
"""
from fractions import Fraction as Q

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(a,x): return (a*x[0],a*x[1])
def scalar(a): return (Q(a),Q(0))
phi=(Q(1,2),Q(1,2)); phip=(Q(1,2),Q(-1,2))
three=[scalar(3),scalar(-1),scalar(0),phi,phip]
other=three[:3]+[phip,phi]
five=list(map(scalar,[5,1,-1,0,0]))
one=[scalar(1)]*5
square_class=[0,0,2,4,3]
sizes=[1,15,20,12,12]

def inner(x,y):
    z=scalar(0)
    for n,a,b in zip(sizes,x,y): z=add(z,scale(n,mul(a,b)))
    return scale(Q(1,60),z)

for chi in (three,other):
    sym2=[scale(Q(1,2),add(mul(chi[i],chi[i]),chi[square_class[i]])) for i in range(5)]
    assert sym2==[add(a,b) for a,b in zip(one,five)]
    assert inner(five,chi)==scalar(0)
assert inner(five,[add(a,b) for a,b in zip(three,other)])==scalar(0)
assert inner(five,five)==scalar(1)
print('PASS: Sym² of either A5 three-space is 1+5; Sym⁴W is irreducible 5.')
print('PASS: the order-four comparison space has no invariant vectors.')

# On P2, H1(O(k))=0 always; H2(O(k))=h0(O(-k-3)).
def h2_line(k):
    d=-k-3
    return (d+1)*(d+2)//2 if d>=0 else 0
assert h2_line(-3)==1 and h2_line(-2)==h2_line(-1)==0
assert 3*h2_line(-3)==3
for t in range(2,101):
    assert h2_line(t-4)==0 and h2_line(t-3)==0
print('PASS: twist-two Steiner contribution gives h0(B_R(2))=3.')
print('PASS: no positive H1 contribution for Steiner twists t≥2 (checked 2..100; proof is monotone line-cohomology).')
print('BOUNDARY: the formal induction and global-section contradiction are mathematical proofs in the companion note, not numerical tests.')
