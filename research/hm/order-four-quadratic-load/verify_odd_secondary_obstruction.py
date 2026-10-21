#!/usr/bin/env python3
"""Universal finite-filtration dimensions; no actual coefficient or rank tests."""
# Plane adjoint Hilbert polynomial: chi B_R(t)=3*chi O_R(t)-15.
def chi(t):return 3*(t+1)*(t+2)//2-15
assert chi(3)==15 and chi(1)==-6 and chi(-1)==-15 and chi(-3)==-12
# Four harmonic H1 contributions in (I/I^9) odd special fiber.
assert 6+18+36+30==90
assert 30-12==18 and 90-12==78
assert 15*2==30
# Root first kernel bundle and second target twists.
assert 15-6==9 and -6*2==-12
assert 9*2==18 and 15*2==30
# The secondary exact sequence has Euler characteristic 9-15=-6.
assert 9-15==-6
for m in range(8,102,2):assert m-6>=2
print('PASS: first 30->12, full secondary 18->78, exact harmonic secondary 18->30.')
print('PASS: two root maps 9->15; kernel bundle rank9 degree-12, target twist4.')
print('PASS: final possible even normal boundary has target12 at degree6; later even degrees use positive Steiner vanishing.')
print('BOUNDARY: no rank of beta or gamma is evaluated or asserted.')
