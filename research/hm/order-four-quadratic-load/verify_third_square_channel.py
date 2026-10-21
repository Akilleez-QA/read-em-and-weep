#!/usr/bin/env python3
"""Exact universal character and degree checks for the third-channel filtration."""
from pathlib import Path
import runpy
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm=r['vadd'],r['vscale'],r['vmul']
h7=vm(r['P'],r['A'])
h9=va(vm(r['P'],va(r['A'],r['V'],r['P'])),vs(-1,vm(r['A'],r['A'])))
s18=[r['sym'](18,x) for x in r['W']]
assert va(h9,vs(-1,h7))==s18
assert [r['inner'](x,r['D']) for x in (h7,h9,s18)]==[r['z'](1),r['z'](2),r['z'](1)]
s6=[r['sym'](6,x) for x in r['W']]
assert s6==va(r['V'],r['P']) and r['inner'](s6,r['D'])==r['z'](0)
assert [n for n in (12,20,30,60) if n<=18]==[12]
print('PASS: third channels restrict in an exact 1-to2-to1 sequence.')
print('PASS: the sole possible degree12 common divisor would require the absent D5 in Sym6W.')
print('No actual third channel selected.')
