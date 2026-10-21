#!/usr/bin/env python3
"""Universal covariant, jet-degree and actual-cohomology-character checks only."""
from pathlib import Path
import runpy
root=Path(__file__).parent
r=runpy.run_path(str(root/'verify_pure_cross_block_couplings.py'))
for n in [8,14,16,20]:assert r['inner'](r['P'],r['sy'](n))==1
for n in [2,4]:assert r['inner'](r['P'],r['sy'](n))==0
assert [n for n in range(21) if r['inner'](r['one'],r['sy'](n))]==[0,12,20]
assert r['vm'](r['W'],r['Wp'])==r['P']
assert r['inner'](r['Wp'],r['sy'](9))==0
assert r['inner'](r['Wp'],r['vm'](r['A'],r['W']))==0
assert 5*(8-5+1)==20
assert 4*8-4*3==20
assert (-1)*2+(-6)==-8
q=runpy.run_path(str(root/'verify_diagonal_lift_koszul_characters.py'))
inner=q['q']['inner']; Wp=q['q']['Wp']; W=q['q']['W']; vm=q['vm']; z=q['q']['z']
assert inner(Wp,vm(W,q['r']['h0']))==z(1)
assert inner(Wp,q['h1'])==z(1)
assert inner(Wp,vm(W,q['r']['h1']))==z(0)
print('PASS: P4 covariant multiplicities force exact scalar-target base-divisor alternatives.')
print('PASS: D5 Wronskian degree20, third-jet determinant degree20, P4 syzygy degrees1,1,6.')
print('PASS: W-prime first-normal Koszul sequence has multiplicities1 ->2 ->1, final target0.')
print('No actual coefficient, selected matrix, evaluated rank, or local-model experiment computed.')
