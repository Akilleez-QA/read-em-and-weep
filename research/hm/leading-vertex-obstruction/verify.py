"""Bounded free-tag audit, not an actual-source calculation or formal proof."""
from collections import Counter

# Enumerate the cubic coefficient without commuting ordered matrix factors.
tags = Counter((i,j,r) for i in range(3) for j in range(3)
               for r in range(4) if i+j+r==3)
expected = Counter([(1,2,0),(2,1,0),(0,2,1),(2,0,1),
                    (1,1,1),(0,1,2),(1,0,2),(0,0,3)])
assert tags == expected
weights = {0:12,1:8,2:4}
assert all(weights[i]+weights[j]-4*r==12 for i,j,r in tags)
# Any higher even jet strictly raises this degree.
assert all(weights[i]+2+weights[j]-4*r>12 for i,j,r in tags)

# The change L2 -> L2+D occurs in exactly four cubic products, never D^2.
varying = {(i,j,r) for i,j,r in tags if i==2 or j==2}
assert varying == {(1,2,0),(2,1,0),(0,2,1),(2,0,1)}
assert (2,2,0) not in tags

# Weighted entry availability, trace-kernel degrees and dimensions.
def dim(degree): return max(degree+1,0)
assert [dim(-2),dim(-4),dim(0)] == [0,0,1]
assert [dim(0),dim(-2),dim(2)] == [1,0,3]
assert dim(4)+dim(2)+dim(6)==15
assert dim(4-5)+dim(4-3)==2
assert 15-2==dim(12)==13
assert dim(2)+dim(0)==4  # degree-eight square generators f^2 Sym^2 + fg
print('PASS: eight ordered cubic tags; leading-degree isolation; four retained variation tags; weighted kernel and dimension audit.')
