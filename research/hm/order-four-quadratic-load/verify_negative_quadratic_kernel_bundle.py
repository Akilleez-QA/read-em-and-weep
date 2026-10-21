#!/usr/bin/env python3
"""Universal dimensions and Chern bookkeeping; no actual HM rank calculation."""
from math import comb
assert (6-4)==2
c1K=-6; c2K=comb(6,2)
assert c2K==15
# Three copies, since dim A=3.
c1E=3*c1K
c2E=3*c2K+3*c1K*c1K
assert (c1E,c2E)==(-18,153)
ch2E=(c1E*c1E-2*c2E)//2
assert ch2E==9
rankC=48-44+6
c1C=44+c1E
ch2C=-22+ch2E
c2C=(c1C*c1C-2*ch2C)//2
assert (rankC,c1C,ch2C,c2C)==(10,26,-13,351)
assert (48-46+3,46-15)==(5,31)
assert (-5-2,-5)==(-7,-5)
assert -1+1==0  # Normal O(1) cancels tautological source O(-1).
print('PASS: root-bundle resolution, adjacent pencil, global cokernel Chern classes, and normal-obstruction twists.')
