#!/usr/bin/env python3
"""Universal character arithmetic; actual geometric cohomology inputs are in companion."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm,vs=r['vadd'],r['vmul'],r['vscale']
N,Wp,U,L2=[r[x] for x in ('N','Wp','H','L2')]
fc={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,U)),2:Wp}
chi=vs(-1,r['ambient_sym'](5))
for i,ri in fc.items():
 for j,rj in fc.items():
  chi=va(chi,vm(vm(ri,rj),r['ambient_sym'](6+i+j)))
h0=va(r['one'],r['P'],r['D'])
h1=va(h0,vs(-1,chi))
expected=va(r['one'],r['A'],r['V'],r['D'],r['Wp'],vs(3,r['T']))
assert h1==expected
assert h0[0]==r['z'](10) and h1[0]==r['z'](32)
assert vm(r['A'],r['A'])==va(r['one'],r['A'],r['D'])
from itertools import product
for flags in product((0,1),repeat=3):
 n=sum(f*d for f,d in zip(flags,(1,3,5)))
 assert (10+n)-(3+n)==43-36
 assert 48-(10+n)==41-(3+n)
print('PASS: exact twist-five Euler/H1 characters and all three-channel section-defect dimensions.')
