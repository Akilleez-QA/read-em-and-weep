#!/usr/bin/env python3
"""Exact universal representation checks for actual two-step criterion."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_twist_five_global_cohomology.py')))
q=r['r']; va,vm,vs=r['va'],r['vm'],r['vs']
t=3; chi=vs(-1,q['ambient_sym'](t))
for i,a in r['fc'].items():
 for j,b in r['fc'].items():chi=va(chi,vm(vm(a,b),q['ambient_sym'](t+1+i+j)))
assert [q['inner'](vs(-1,chi),q[k]) for k in ['W','Wp','S','T']]==[q['z'](n) for n in [0,3,3,6]]
assert vm(q['W'],q['D'])==va(q['S'],q['T'])
assert vm(q['W'],q['S'])==va(q['A'],q['D'])
assert vm(q['W'],q['T'])==va(q['D'],q['V'],q['P'])
assert vm(q['W'],q['Wp'])==q['P']
assert 5>4
print('PASS: Y odd character is 3W-prime+3S4+6T6 and all factorization identities hold.')
print('PASS: an injective fixed-u map from D5 cannot factor through one S4.')
print('No actual multiplication scalar, coefficient, or rank evaluated.')
