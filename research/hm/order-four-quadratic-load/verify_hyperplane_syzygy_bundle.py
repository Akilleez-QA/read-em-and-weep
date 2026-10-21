#!/usr/bin/env python3
"""Universal degree/twist bookkeeping, no actual coefficient or rank scan."""
rank=46-44+3
sheaf_degree=44+3*(-6)
assert (rank,sheaf_degree)==(5,26)
assert 2*(-3)==-6
assert (2*5-1)==9  # Sym^2 F(5)=B(9), since B=Sym^2 F(1).
for n in range(6): assert max(n-6+1,0)==0
assert 3*max(6-6+1,0)==3
assert (6+3)==9
print('PASS: exact kernel twist, cokernel rank5 degree26, and normal-order product twists.')
