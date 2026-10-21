#!/usr/bin/env python3
"""Universal representation/Hilbert checks. No HM instance inputs or matrices."""
import json
from fractions import Fraction
from math import comb

# A5 classes: identity, double transposition, 3-cycle, and two 5-cycle classes.
sizes=[1,15,20,12,12]
chi=[4,0,1,-1,-1]
chi_square=[4,4,1,-1,-1]
chi_cube=[4,0,4,-1,-1]
sym3=[Fraction(a**3+3*a*b+2*c,6) for a,b,c in zip(chi,chi_square,chi_cube)]
inv=sum(s*t for s,t in zip(sizes,sym3))/60
assert sym3==[20,0,2,0,0] and inv==1
# Every invariant effective degree <=18 divisor is a sum of these orbit sizes.
orbits=[12,20,30,60]
reachable={0}
for n in range(1,19):
    if any(n-o in reachable for o in orbits): reachable.add(n)
assert 18 not in reachable
# Unique cubic + 4-regularity gives the coordinate Hilbert function.
def hilbert(n):
    return 0 if n<0 else [1,4,10][n] if n<3 else 6*n+1
numerator=[sum((-1)**j*comb(4,j)*hilbert(n-j) for j in range(5)) for n in range(11)]
assert numerator==[1,0,0,-1,-6,9,-3,0,0,0,0]
assert 35-hilbert(4)-4==6
assert 27-36+4==-5
print(json.dumps({
    'standard_A5_symmetric_cube_character': list(map(int,sym3)),
    'invariant_cubic_dimension': int(inv),
    'possible_invariant_effective_degrees_le18':sorted(reachable),
    'coordinate_Hilbert_function_degrees_0_to_7':[hilbert(n) for n in range(8)],
    'coordinate_Hilbert_numerator':numerator[:7],
    'minimal_ideal_resolution':{'generators':{'degree3':1,'degree4':6},'first_syzygies':{'degree5':9},'second_syzygies':{'degree6':3}},
    'actual_HM_coefficients_or_rank_evaluations':False
},indent=2))
