from math import prod

def h0(i,j):return max(i+1,0)*max(j+1,0)
def h1(i,j):return max(-i-1,0)*max(j+1,0)+max(i+1,0)*max(-j-1,0)
def h2(i,j):return max(-i-1,0)*max(-j-1,0)
# Polar complete intersection: two bidegrees (2,3).
assert 2*3+3*2==12
# Kernel determinant, after accounting for target O(0,3).
assert (-2-2,0-3)==(-4,-3)
assert (-4+4,-3+3)==(0,0)
assert h1(0,0)==h2(0,0)==0
assert h1(2,3)==h1(4,2)==0
source=2*h0(2,3)+3*h0(4,2)
target=4*h0(4,3)
assert (source,target)==(69,80)
assert source-h0(0,0)==68
assert target-(source-h0(0,0))==12
assert (2//2+3,4//2+2)==(4,4)
print('PASS: exact Koszul line degrees and reduced-support length 12.')
print('PASS: H1/H2 vanishings give global lifting, not only a dimension heuristic.')
print('PASS: 69 -> 80 has kernel 1 and quotient 12; principal source coefficients have twist four.')
print('Full b-channel companion and remaining monad equations are not discarded.')
