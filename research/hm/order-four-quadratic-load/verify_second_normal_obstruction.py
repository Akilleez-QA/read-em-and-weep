#!/usr/bin/env python3
"""Universal degree/dimension checks; no actual HM evaluation or rank scan."""
def h0(d): return max(0,d+1)
def h1(d): return max(0,-d-1)
assert 3*3*h1(-4)==27
assert 3*h0(2)==3*3*h1(-2)==9
assert 3*3*h1(4)==0
assert 3*h0(8)+3*3*h0(4)==72
assert 3*2*h0(6)==42
for m in range(3):
    assert 3*(m+3)*h1(4-2*m)==0
assert 3*4*h0(2)==36
assert 3*6*h1(-2)==18
assert 3*5*h0(0)==15
assert 3*7*h1(-4)==63
assert {0,15,*[h0(4-e) for e in range(3)]}=={0,3,4,5,15}
assert {15-k for k in {0,3,4,5,15}}=={15,12,11,10,0}
print('PASS: intrinsic xi space27; actual local twist-one gate9 ->9')
print('PASS: twist-four second-order obstruction target0; local jet parities72/42')
print('PASS: actual higher factors36 ->18 and15 ->63 have correct degrees')
print('PASS: universal top-factor kernel dimensions{0,3,4,5,15}')
print('BOUNDARY: no actual xi coefficient, rank, nonzero commutator, or global lifting asserted')
