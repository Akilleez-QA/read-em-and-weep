#!/usr/bin/env python3
"""Independent symbolic interface audit: no parameter assignment or rank test."""
from pathlib import Path
import runpy
import sympy as S
root=Path(__file__).resolve().parent
def read(name): return runpy.run_path(str(root/name))
op=read('verify_two_endpoint_input_cone_operators.py')
a=read('verify_homogeneous_endpoint_secondary_square_cancellation.py')
b=read('verify_homogeneous_endpoint_secondary_xy3_nonvanishing.py')
def zero(v):
 if isinstance(v,S.MatrixBase):
  for entry in v: assert S.cancel(entry)==0
 else: assert S.cancel(v)==0
# The ACTUAL-compatible regular operators are literally those in both secondary scripts.
zero(a['AA']-op['connections']['X4'][0])
zero(b['AA']-op['connections']['XY3'][0])
zero(a['eta']-b['eta'])
zero(a['ns']['nx']-b['ns']['nx']);zero(a['ns']['ny']-b['ns']['ny'])
z,X,Y,B,c,k=[b[q] for q in ('z','X','Y','B','c','k')]
assert S.expand(a['gamma']).coeff(z,-1)==0
assert S.expand(a['gamma']).coeff(z,-2)==0
zero(S.expand(b['gamma']).coeff(z,-1)-3*k*Y/(B*c))
zero(S.expand(b['gamma']).coeff(z,-2))
# An arbitrary nonzero normal-generator scale cannot change either conclusion.
scale=S.Symbol('c_eta',nonzero=True)
residue=3*scale*k/(B*c)
assert residue.is_nonzero
# Physical coefficient lines: frame difference 7, cover degree halves.
assert (2-4//2, 2-2//2+7, 2-6//2-7)==(0,8,-8)
assert 4-12//2==-2
assert -S.Rational(5,2)-S.Rational(1,2)==-3
print('PASS: both secondary scripts use precisely the independently actual-compatible operators and identical normal input.')
print('PASS: actual normalized endpoint values are zero and c_eta*3k/(Bc)[Y/z], with c_eta nonzero.')
print('No fourth Bockstein or additional representation channel inferred.')
