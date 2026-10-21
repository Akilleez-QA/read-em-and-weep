#!/usr/bin/env python3
"""Universal splitting possibilities; no HM differential or instance rank."""
from itertools import combinations_with_replacement
splittings=[a for a in combinations_with_replacement(range(1,7),5) if sum(a)==10]
assert len(splittings)==7
for a in splittings:
    defect=sum(x==1 for x in a)
    h0_second=sum(max(3-x,0) for x in a)
    assert defect<=4
    print({'negative_degrees':a,'binary_corank':defect,'binary_rank':20-defect,'h0_J_twist2':h0_second})
assert len({a for a in splittings if 1 not in a})==1
assert (2,2,2,2,2) in splittings
print('PASS: seven types; binary coefficient rank at least16; balance iff corank0')
print('No assertion about which type the actual ruling bundle has.')
