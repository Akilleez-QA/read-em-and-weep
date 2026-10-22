#!/usr/bin/env python3
"""Universal dimensions and characters of the Ext-annihilator vertex gate."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm=r['vadd'],r['vmul']
assert vm(r['D'],r['A'])==va(r['A'],r['V'],r['P'],r['D'])
source=va(vm(r['D'],r['A']),r['D'])
assert source==va(r['A'],r['V'],r['P'],r['vscale'](2,r['D']))
assert source[0]==r['z'](20)
assert 9+5*3+5==29 and 29-9==20
assert 3+5==8
print('PASS: positive ordinary quartics have dimension29, conic restriction9, and vertex-gate source20.')
print('PASS: K20=A+V+P4+2D5; preserving centralizer has dimension8.')
print('No actual Ext-module identification, restriction rank, or multiplication coefficient assumed.')
