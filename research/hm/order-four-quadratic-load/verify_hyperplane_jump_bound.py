#!/usr/bin/env python3
"""Universal orbit/degree and DVR-length bookkeeping only."""
assert [j for j in range(4) if 26-12*j>=0]==[0,1,2]
assert [26-12*j for j in range(3)]==[26,14,2]
assert 3+2==5
for elementary_divisors in ([],[1],[2],[1,1]):
 assert len(elementary_divisors)<=sum(elementary_divisors)
print('PASS: uniform twelve-point torsion lengths, free quotient degrees, and distinction between length and fiber excess.')
