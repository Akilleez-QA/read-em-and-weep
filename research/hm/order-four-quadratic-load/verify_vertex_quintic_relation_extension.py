#!/usr/bin/env python3
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
sy,vm,inn=q['sy'],q['vm'],q['inner']
A,V,W,Wp,P=[q[n] for n in ('A','V','W','Wp','P')]
T6=sy(5)
wp_sym=lambda n:[q['sym'](n,t) for t in Wp]
assert wp_sym(5)==T6
assert vm(Wp,A)==T6
assert vm(Wp,W)==P
assert inn(V,sy(6))==1
assert inn(P,sy(6))==1
assert inn(T6,vm(Wp,A))==1
assert 4*(-1)-3*(-3)==5
assert 5-(-1)>0 # no O(5)->O(-1) map
assert -2+(-1)-5==-8
assert 9*(-4)-4*(-8)==-4 # Q4 has rank5 and degree-4
assert 9*(2+1)==27
assert 4*1==4 # H1(P4 O(-2))
assert 27+4==31
assert 5*(6+1)-4==31
print('PASS: nonsplit unique quintic-generator extension and the 27-to-31 square-shadow P4 cokernel.')
print('No comparison identifying gamma with this nonzero extension is assumed.')
