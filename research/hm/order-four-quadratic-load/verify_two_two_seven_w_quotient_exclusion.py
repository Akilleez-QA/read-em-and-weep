"""Exact cohomology obstruction, with no actual maps or rank tests."""
from pathlib import Path
import contextlib,io,runpy
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):r=runpy.run_path(str(ROOT/'verify_equivariant_splitting_gauss_persistence.py'))
va,vs,vm,sym=[r[k] for k in ('va','vs','vm','sym')]
assert vm(r['W'],sym(3))==va(r['A'],r['D'])
for coeff,R2,blocks in r['profiles']:
 h1=va(vs(0,r['one']),*[vm(R,sym(j-4)) for j,R in blocks if j>=4])
 assert r['inner'](h1,r['A'])==r['z'](0)
assert -(-7+2)-2==3
print('PASS: H1((W O(-7)+O(16))(2))=A3+D5, but H1(E(2)) has no A3 in all28 actual formal types.')
print('Exact quotient cohomology excludes this A, and hence its listed zero-defect pair; no full profile exclusion.')
