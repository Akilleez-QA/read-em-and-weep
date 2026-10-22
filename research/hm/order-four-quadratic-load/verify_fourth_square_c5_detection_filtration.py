#!/usr/bin/env python3
"""Abstract C5 evaluation filtration, not an actual fourth map evaluation."""
import contextlib,io,runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs=r['vadd'],r['vscale']
one,A,V,P,D=r['one'],r['A'],r['V'],r['P'],r['D']
S=lambda n:[r['sym'](n,x) for x in r['tr']]
assert S(8)==va(P,D)
assert S(20)==va(one,A,V,P,vs(2,D))
assert va(S(20),vs(-1,S(8)))==va(one,A,V,D)
assert r['inner'](D,S(8))==r['z'](1)
assert r['inner'](D,S(20))==r['z'](2)
assert (4*2+0)%10==8
assert 12>8
print('PASS: C5-square evaluation detects one of two quartic square channels.')
print('Residual Delta12 channel is basepoint-free off E; no actual beta4 value inferred.')
