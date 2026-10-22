#!/usr/bin/env python3
import sympy as s
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
# Invariants in Sym^2(V+W): Sym^2 V=1+D, V*W has odd center,
# and Sym^2 W=A. Quotient by the unique invariant q removes it.
assert r['inner'](r['one'],r['vadd'](r['one'],r['D']))==r['z'](1)
assert r['inner'](r['one'],r['vmul'](r['V'],r['W']))==r['z'](0)
assert r['inner'](r['one'],r['A'])==r['z'](0)
c,d,x=s.symbols('c d x',nonzero=True)
root=-c/d; midpoint=root/2
assert s.simplify(c*midpoint+d*midpoint**2)==-c**2/(4*d)
a,b,e=s.symbols('a b e')
N=s.Matrix([[a,b],[e,-a]])
assert N*N==(-N.det())*s.eye(2)
print('PASS: no invariant determinant remainder, Cayley-Hamilton, and nonliftable midpoint.')
print('Kernel flatness and the absolute cubic gate are not asserted.')
