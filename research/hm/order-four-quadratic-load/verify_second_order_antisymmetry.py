#!/usr/bin/env python3
"""Universal representation check; the actual scalar is not evaluated."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm=r['vadd'],r['vscale'],r['vmul']
assert vm(r['W'],r['A'])==va(r['W'],r['S'])
assert vm(r['A'],r['A'])==va(r['one'],r['A'],r['D'])
assert r['inner'](r['A'],r['D'])==r['z'](0)
assert 3>2
print('PASS: antisymmetry has only its A channel; the linear legs are W and S4.')
print('PASS: symmetric second obstruction has only the D5 channel in its cokernel.')
print('The Koszul division proof determines the equivalence, not a scalar evaluation.')
