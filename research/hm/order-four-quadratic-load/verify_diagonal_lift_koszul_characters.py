#!/usr/bin/env python3
"""Universal Euler character verification; no actual multiplication evaluated."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_twist_five_global_cohomology.py')))
q=r['r']; va,vm,vs=r['va'],r['vm'],r['vs']
chi=vs(-1,q['ambient_sym'](4))
for i,ri in r['fc'].items():
    for j,rj in r['fc'].items():
        chi=va(chi,vm(vm(ri,rj),q['ambient_sym'](5+i+j)))
h1=vs(-1,chi)
expected=va(vs(2,q['V']),vs(4,q['P']),vs(3,q['D']),vs(3,q['W']),q['Wp'],vs(4,q['S']),vs(4,q['T']))
assert h1==expected
assert q['inner'](q['S'],h1)==q['z'](4)
assert q['inner'](q['D'],r['h1'])==q['z'](1)
assert q['inner'](q['D'],r['h0'])==q['z'](1)
print('PASS: invariant ordinary-product line dimension1; actual Koszul ambient character gate4-to1.')
print('No value or rank of that actual four-to-one map is computed.')
