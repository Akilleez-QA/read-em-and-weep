"""Invented finite-group additive cochains, unrelated to physical source data."""
from fractions import Fraction as F
from itertools import product
G=range(4)
count=0
for mask in G:
    action=lambda g: (-1)**((g&mask).bit_count())
    for values in product(range(-2,3),repeat=3):
        f={0:F(0),**{g:F(values[g-1]) for g in [1,2,3]}}
        a=lambda g,h: action(g)*f[h]-f[g^h]+f[g]
        b={g:sum((a(g,h) for h in G),F(0))/4 for g in G}
        for g,h,k in product(G,repeat=3):
            assert action(g)*a(h,k)-a(g^h,k)+a(g,h^k)-a(g,h)==0
        for g,h in product(G,repeat=2):
            assert action(g)*b[h]-b[g^h]+b[g]==a(g,h)
        count+=1
print(f'PASS: {count} synthetic normalized cocycles; averaging coboundary identity')
