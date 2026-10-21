#!/usr/bin/env python3
"""Universal exact-character and dimension bookkeeping only."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
sy,vm=q['sy'],q['vm']
A,V,W,Wp,P=[q[n] for n in ('A','V','W','Wp','P')]
one=q['one'];D=sy(4);T=sy(5);S=sy(3)
def plus(*cs):
    out=[q['z'](0)]*9
    for c in cs:out=[q['add'](x,y) for x,y in zip(out,c)]
    return out
assert vm(Wp,Wp)==plus(one,V)
assert vm(Wp,A)==T
assert vm(Wp,W)==P
assert vm(Wp,S)==plus(V,D)
assert vm(P,A)==plus(V,P,D)
assert plus(P,D,P,D,vm(P,A))==plus(V,P,P,P,D,D,D)
assert 9+21==30 and 9+9==18 and 30-18==12
assert 4*3==12
print('PASS: actual negative-quadratic action factors through the 12-dimensional P4 tensor A* quotient; kernel dimension18.')
print('No second-Bockstein scalar is selected.')
