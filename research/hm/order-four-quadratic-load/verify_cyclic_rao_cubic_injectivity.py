#!/usr/bin/env python3
"""Universal character checks supporting the geometric cubic Rao argument."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm=r['vadd'],r['vscale'],r['vmul']
c=va(r['ambient_sym'](3),vs(-1,r['ambient_sym'](1)))
expected=va(r['A'],vs(2,r['P']),r['D'],vs(2,r['S']),r['T'])
assert c==expected and c[0]==r['z'](30)
assert r['inner'](c,r['one'])==r['z'](0)
assert vm(r['W'],r['D'])==va(r['S'],r['T'])
assert vm(r['W'],r['A'])==va(r['W'],r['S'])
assert va(r['S'],vm(r['W'],r['D']))==va(vs(2,r['S']),r['T'])
print('PASS: cubic quotient has dimension30 and no invariant line.')
print('PASS: the two negative-linear polynomial sectors yield two S4 copies and one T6.')
print('Actual injectivity follows from the conic restriction bound in the proof, not this character check alone.')
