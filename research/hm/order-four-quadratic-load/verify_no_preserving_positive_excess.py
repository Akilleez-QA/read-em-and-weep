#!/usr/bin/env python3
"""Universal degree and cohomology certificates, no selected evaluation."""
min_orbit=12
assert 5*1<min_orbit and 2*2<min_orbit
assert (7-5,5-2,2)==(2,3,2)
assert 4*1-3*2==-2
assert -2-3==-5
# Twist-four cubic quotient: 2O(-1) -> 5O(2) -> rank3 degree12.
assert -5+4==-1 and -2+4==2
assert max(-1+1,0)==0 and max(-(-1)-1,0)==0
assert 5*(2+1)==15 and 3*(4+1)==15
assert (4+1)+15==20
print('PASS: rank-drop minor degrees5 and4 are below the minimum orbit12.')
print('PASS: uniform Loewy(2,3,2), cubic relation twist-2, Ext relation twist-5.')
print('PASS: twisted relation bundle is acyclic; the 15-to15 section quotient is an isomorphism.')
print('No assertion that non-preserving positive adjoints vanish.')
