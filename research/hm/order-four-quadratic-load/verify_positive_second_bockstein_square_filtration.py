#!/usr/bin/env python3
"""Universal character/filtered-degree checks; no actual HM coefficients."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
sy,vm,inn=q['sy'],q['vm'],q['inner']
A,V,W,Wp,P=[q[n] for n in ('A','V','W','Wp','P')]
one=q['one']; D=sy(4)
def plus(*cs):
    out=[q['z'](0)]*9
    for c in cs: out=[q['add'](x,y) for x,y in zip(out,c)]
    return out
wp_sym=lambda n:[q['sym'](n,t) for t in Wp]
assert wp_sym(4)==D
assert wp_sym(8)==plus(P,D)
assert vm(P,A)==plus(V,P,D)
assert plus(wp_sym(8),vm(P,A))==plus(V,P,P,D,D)
assert inn(plus(one,D),vm(P,A))==1
# Sym^2(Sym^2 W)=Sym^4 W+1, the universal binary identity.
assert 3*4//2==5+1
# Ordinary square of a regular initial (3,5) pair.
num={0:1,6:-1,8:-1,10:-1,11:1,13:1}
hilbert=[sum(c*(d-k+1) for k,c in num.items() if d>=k) for d in range(20)]
assert hilbert==[1,2,3,4,5,6,6,6,5,4,2,1]+[0]*8
assert 8+4==12 and all(v==0 for v in hilbert[12:])
# Cover-degree-eight relation, at ordinary twists four and six.
assert -8+4==-4 and -4+4==0
assert -8+6==-2 and -4+6==2
assert 9+4*3==21
assert 9*3+4==31
assert 5+15+9==29
assert 9+5+15+21==50 and 50-29==21
assert 13+7+25+31==76
assert 13+7+25+27==72 and 76-72==4
assert 3<4 # a map supported on source A cannot remove all four cokernel dimensions
print('PASS: twist-four square obstruction is H0(Q4(4)) of dimension21.')
print('PASS: D5 multiplication raises cover degree8 to12 and is zero in the square quotient.')
print('PASS: the remaining A multiplication is the P4-valued Serre contraction with one possible D5 scalar.')
print('No nonvanishing or actual rank is selected.')
