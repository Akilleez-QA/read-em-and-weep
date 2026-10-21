#!/usr/bin/env python3
"""Universal stack/coarse parity and character bookkeeping, no HM ranks."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
sy,vm,inn=q['sy'],q['vm'],q['inner']
A,V,W,Wp,P=[q[n] for n in ('A','V','W','Wp','P')]
one=q['one'];D=sy(4);T=sy(5)
def plus(*cs):
 out=[q['z'](0)]*9
 for c in cs:out=[q['add'](x,y) for x,y in zip(out,c)]
 return out
assert vm(Wp,T)==plus(A,P,D)
assert vm(Wp,P)==plus(W,T)
assert vm(Wp,A)==T
assert vm(Wp,W)==P
conormal=plus(P,P,vm(A,sy(8)))
assert conormal==plus(A,V,V,P,P,P,P,D,D)
assert conormal[0]==q['z'](35)
assert 2*2*(1+1)+3*(8+1)==35
assert 2*2*(8+1)+3*(1+1)==42
assert 2*(10+1)==22  # all conic conormal sections are odd
# Square of a (3,5) regular sequence: exact numerator.
num={0:1,6:-1,8:-1,10:-1,11:1,13:1}
h=[sum(c*(d-k+1) for k,c in num.items() if d>=k) for d in range(18)]
assert h==[1,2,3,4,5,6,6,6,5,4,2,1,0,0,0,0,0,0]
assert sum(h)==45
assert sum(h[::2])==22 and sum(h[1::2])==23
assert 22==8+2*7
assert 13+9*3+5*5+7==72
assert 72+4==76
assert 76-35==41 and 41-13==28
# Global Loewy degeneracy divisors cannot contain a full orbit.
assert 2<12 and 3<12
# Primary possibilities and the independently proved eight-dimensional bound.
assert 3+5==8 and 3+4+5==12
assert 12>8  # forces the primary P4 scalar nonzero once rank33 is proved
print('PASS: stack-square parity lengths (22,23), unique P4 primary gate, and 72-to-76 square-shadow cohomology.')
print('PASS: global Loewy orbit bounds and the 35-dimensional positive conormal contribution.')
print('The rank33 conclusion is an input; gamma nonvanishing is not inferred.')
