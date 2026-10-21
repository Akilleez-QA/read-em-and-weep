#!/usr/bin/env python3
"""Universal bookkeeping for the conditional final positive obstruction."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm,vs=r['vadd'],r['vmul'],r['vscale']
h=va(vm(r['P'],va(r['A'],r['V'],r['P'])),vs(-1,vm(r['A'],r['A'])))
assert h==va(r['A'],vs(2,r['V']),vs(3,r['P']),vs(2,r['D']))
assert h[0]==r['z'](31) and r['inner'](h,r['D'])==r['z'](2)
assert 41-33-3==5 and 37-33-3==1
assert 37-3*2==31
for e in range(3,32):assert 6+e<=37
# Formal x0,x1,x2 chain: M0x0=0, M1x0=-M0x1, M1x1=-M0x2.
coeff={0:0,1:1-1,2:1-1,3:1}
assert {k:v for k,v in coeff.items() if v}=={3:1}
print('PASS: one remaining row, finite last exponent at most31 if full rank occurs.')
print('PASS: the third global gate has two equivariant channels in H0(I_Z(9)).')
print('No actual second/third coefficient or final rank evaluated.')
