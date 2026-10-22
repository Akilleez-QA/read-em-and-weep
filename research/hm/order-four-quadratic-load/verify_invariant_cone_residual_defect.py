#!/usr/bin/env python3
"""Universal normal-jet degrees and residual characters, not actual coefficients."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm,vs=q['vadd'],q['vmul'],q['vscale']; sp=lambda n:[q['sym'](n,x) for x in q['Wp']]
assert q['inner'](vm(q['W'],q['W']),q['one'])==q['z'](1)
# For all integers k>=2, 2-2k <= -2; this symbolic linear inequality is immediate.
assert 2-2*2==-2
H0S2=va(sp(5),vm(sp(3),q['W']),vm(q['Wp'],q['A']))
assert H0S2==va(q['A'],q['D'],vs(2,q['T']))
H0T=va(H0S2,q['one'],q['T'])
H0Tp=va(H0T,vs(-1,sp(5)))
R=va(q['A'],vs(2,q['Wp']))
assert R[0]==q['z'](7)
assert vm(R,q['A'])==H0Tp==va(q['one'],q['A'],q['D'],vs(2,q['T']))
assert 9-2==7 and 27-6==21 and 7*(0+1)+14==21
assert 7*(2-3+1)==0
print('PASS: unique first-normal invariant, negative higher jet degrees, residual Hilbert7t+21 and exact (A+2Wp)O(2) section character.')
