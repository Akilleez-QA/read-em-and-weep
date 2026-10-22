#!/usr/bin/env python3
"""Universal characters and quadratic root algebra, no actual HM evaluations."""
import runpy
from pathlib import Path
from sympy import Matrix, symbols, expand
r=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
expected=[
 [3,2,2,1,0,0,0], [3,2,2,1,0,0,0], [3,2,2,1,0,0,0],
 [3,2,2,1,1,1,1], [3,2,2,1,1,0,0], [3,2,2,1,1,0,0],
 [3,2,2,1,1,1,1]]
orders=[]
for row,want in zip(r['rows'],expected):
 dims=[r['couplings'](row,k) for k in range(2,9)]
 assert dims==want
 dims.append(0) # k=9 has negative second-factor degree.
 orders.append([k for k in range(2,9) if dims[k-2]>dims[k-1]])
assert orders==[[2,4,5],[2,4,5],[2,4,5],[2,4,8],[2,4,6],[2,4,6],[2,4,8]]
eps=symbols('epsilon')
Z=Matrix([[0,eps],[1,0]])
for e in range(7):
 M=Z**e
 assert expand(M.det()-(-eps)**e)==0
 m=e//2
 target=eps**m*(Matrix.eye(2) if e%2==0 else Z)
 assert M==target
 # Unit entry after dividing epsilon^m; determinant valuation e.
 assert any(expand(v/eps**m) in (1,-1) for v in M if v!=0)
 print('root power',e,'elementary exponents',m,e-m)
print('PASS: exact possible raw diagonal orders by type:',orders)
print('PASS: Delta torsion multiplicity is raw order minus two.')
print('No actual HM coefficients, ranks, or scalar values were evaluated.')
