"""Universal character obstruction for the actual degree-zero quotient.

No selected HM coefficients or actual multiplication matrix/rank are used.
The actual target character is a proved source input; this checks its
comparison with the universal tensor-product source, not that source proof.
"""
from pathlib import Path
import runpy

helper = Path(__file__).resolve().parent.parent / 'generic-beta-fibers' / 'verify_negative_vertex_scalar.py'
r = runpy.run_path(str(helper))
source = r['vmul'](r['vmul'](r['A'],r['V']),r['T'])
target = r['vadd'](r['vscale'](3,r['Wp']),r['vscale'](3,r['S']),r['vscale'](6,r['T']))
expected_source = r['vadd'](r['vscale'](2,r['W']),r['vscale'](2,r['Wp']),
                            r['vscale'](4,r['S']),r['vscale'](5,r['T']))
assert source == expected_source
assert source[0] == target[0] == r['z'](54)
forced_kernel = r['vadd'](r['vscale'](2,r['W']),r['S'])
forced_cokernel = r['vadd'](r['Wp'],r['T'])
assert forced_kernel[0] == forced_cokernel[0] == r['z'](8)
assert r['vadd'](source,r['vscale'](-1,target)) == r['vadd'](
    forced_kernel,r['vscale'](-1,forced_cokernel))
for name,mult in [('W',2),('Wp',2),('S',4),('T',5)]:
    assert r['inner'](r[name],source) == r['z'](mult)
print('PASS: A tensor V tensor Sym5W = 2W + 2Wprime + 4Sym3W + 5Sym5W.')
print('PASS: target 3Wprime + 3Sym3W + 6Sym5W forces kernel 2W+Sym3W and cokernel Wprime+Sym5W.')
print('PASS: both forced dimensions are eight; the degree-zero quotient cannot be trivial.')
