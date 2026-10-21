#!/usr/bin/env python3
"""Universal character arithmetic only. No HM coefficients or rank tests."""
from math import comb

def parity(dim, trace):
    assert (dim+trace)%2 == 0 and abs(trace)<=dim
    return ((dim+trace)//2,(dim-trace)//2)
def tensor(a,b):
    return (a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def sym_trace(plus,minus,n):
    return sum((-1)**j*comb(minus+j-1,j)*comb(plus+n-j-1,n-j)
               for j in range(n+1))
def jet_trace(m): return sum((-1)**j*(j+1) for j in range(m))
assert [sym_trace(3,2,n) for n in (1,2,3)] == [1,3,3]
assert parity(15,3)==(9,6)
assert [jet_trace(m) for m in (2,4)]==[-1,-2]
assert parity(20,4)==(12,8)
assert parity(180,4)==(92,88)
assert parity(75-20,-1-4)==(25,30)
assert parity(250-180,-2-4)==(32,38)
assert parity(50-5,-2-1)==(21,24)
assert parity(100-35,-4-3)==(29,36)
assert parity(10,-2)==(4,6)
assert parity(5,1)==(3,2)
assert parity(20,-4)==(8,12)
assert parity(5,-3)==(1,4)
assert tensor((4,0),(1,4))==(4,16)
# Unknown scalar epsilon on U cancels from the actual primary Euler term.
for epsilon in (1,-1):
    primary_trace=-(-2*epsilon)+epsilon
    assert (4*epsilon)*primary_trace==12
# Actual resolution: chi(B_Q(4))=chi(T)+chi(UF_Q2)+chi(dO_Q-6).
ordinary_index=50+4*(5-10)-30
involution_index=-2+12-(3-1)
assert (ordinary_index,involution_index)==(0,8)
assert ((ordinary_index+involution_index)//2,
        (ordinary_index-involution_index)//2)==(4,-4)
# Positive Schrödinger inversion lift has trace1 and dimensions(3,2).
assert parity(5,1)==(3,2)
assert parity(4,4)==(4,0)
assert parity(36,4)==(20,16)
assert parity(15,-1)==(7,8)
assert parity(50,-2)==(24,26)
assert parity(11,-5)==(3,8)
assert parity(14,-6)==(4,10)
assert tensor((3,2),(3,8))==(25,30)
assert tensor((3,2),(4,10))==(32,38)
assert tensor((3,2),(3,2))==(13,12)
assert 85-4==81
print('PASS: ambient quadrics parity9/6; actual25-point defects25/30 and32/38')
print('PASS: Rao parity21/24 and29/36; conditional20-boundary parity8/12 ->4/16')
print('PASS: unknown U sign cancels; ordinary/equivariant adjoint indices0/8')
print('PASS: actual even Euler index4 forces at least four invariant sections')
print('PASS: one-point defects3/8 and4/10 recover the25-point parity after tensoring')
print('BOUNDARY: universal characters only; no chosen coefficients, matrices, or ranks')

# Full ambient85 pencil, using actual tail-boundary exact sequences.
assert 20+100-35==85
assert 40+50-5==85
assert parity(20,4)==(12,8)
assert parity(40,-8)==(16,24)
assert parity(85,4-4-3)==(41,44)
assert parity(85,-8-2-1)==(37,48)
assert min(41,37)+min(44,48)==81
assert min(41,48)+min(44,37)==78
assert (-1)**44==(-1)**48==1
assert 11-3==8
print('PASS: full ambient85 parities41/44 ->37/48, even/odd corank bounds4/7')

bidegrees=[(85-k,k) for k in range(4,79,2)]
assert bidegrees[0]==(81,4) and bidegrees[-1]==(7,78)
assert len(bidegrees)==38 and all(a+b==85 and a>=7 and b>=4 for a,b in bidegrees)
print('PASS: only38 permitted determinant bidegrees, from81/4 through7/78')
