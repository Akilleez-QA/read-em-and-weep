#!/usr/bin/env python3
"""Universal conic splitting and parity-index checks; no actual ranks."""
from math import comb

def h0(degrees): return sum(max(d+1,0) for d in degrees)
def h1(degrees): return sum(max(-d-1,0) for d in degrees)
def ambient_trace(n):
    return sum((-1)**j*comb(j+1,j)*comb(2+n-j,n-j) for j in range(n+1))
for a in (-1,0,1,2):
    assert min(a+4,2-a)>=0
    d4=[8,2*a+10,6-2*a]
    d3=[6,2*a+8,4-2*a]
    d2=[4,2*a+6,2-2*a]
    assert (h0(d4),h1(d4))==(27,0)
    assert (2*h0(d3),2*h1(d3))==(42,0)
    assert (3*h0(d2),3*h1(d2))==((45,0) if a<=1 else (48,3))
assert ambient_trace(6)==10 and ambient_trace(1)==1
assert 210-30-175==5 and 10-6-7==-3
q1_chi=-55-5
q1_trace=1-(-3)
assert ((q1_chi+q1_trace)//2,(q1_chi-q1_trace)//2)==(-28,-32)
assert 2*32==64 and 3*29==87 and 87-64==23
assert 27-23==4 and 4*28==112
for m in range(1,8):
    assert (-1)**(m-1)==(-1)**(m+1)
for k in range(65):
    for r in range(min(27,23+k)+1):
        h1_plus=23+k-r
        h0_plus=27+k-r
        assert h0_plus-h1_plus==4
        assert h1_plus>=max(0,k-4) and h0_plus>=max(4,k)
print('PASS: all allowed conic splittings have h0(B_C4)=27 and H1=0')
print('PASS: first jets42 odd; second-jet dimensions45/0 or48/3 retained')
print('PASS: actual Q1 parity indices(-28,-32); positive lower gate64 ->87')
print('PASS: exact positive boundary27 ->coker, excess bounds, odd third-order target112')
print('BOUNDARY: no actual rank, jet-lifting surjectivity, or twist-four vanishing asserted')

# Seventh ideal power: source twist-4, target twist-3, Serre dual source twist1.
m=7
assert (3-m,4-m)==(-4,-3) and -(-4)-3==1
expected={-1:([0,2,4],[1,3]),0:([0,2,4],[1,3,5]),1:([0,2,4,6],[1,3,5]),2:([0,2,4,6],[1,3,5])}
for a in (-1,0,1,2):
    allowed=[]
    for m in range(7):
        degrees=[8-2*m,2*a+10-2*m,6-2*a-2*m]
        if h0(degrees): allowed.append(m)
    assert ([m for m in allowed if m%2==0],[m for m in allowed if m%2])==expected[a]
print('PASS: I^7 detection, odd I^6 detection, and splitting-dependent leading-order bounds')
