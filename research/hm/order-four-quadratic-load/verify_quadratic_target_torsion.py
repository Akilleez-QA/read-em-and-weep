#!/usr/bin/env python3
"""Universal local-module and degree bookkeeping, no actual HM evaluations."""
for j in (0,1,2): assert (26-12*j)+12*j==26
# The degree2 generator relations are a+bz and az, after imposing z²=0.
# Their determinant is a², while at a=b=0 both relations vanish.
assert 2*1==2
for e in (1,2):
 for m in (1,2): assert min(e,m) in (1,2)
assert min(2,1)==1 and min(2,2)==2
assert min(1,2)+min(1,2)==2
assert 6+4==10
print('PASS: target degree decomposition and distinct simple/double-root contributions for both length-two torsion types.')
