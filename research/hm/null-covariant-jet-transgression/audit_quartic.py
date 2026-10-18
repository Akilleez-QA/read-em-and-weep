#!/usr/bin/env python3
"""Independent addendum consistency and mutation controls; universal coefficients only."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import runpy,json
root=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):
    q=runpy.run_path(str(root/'check_quartic.py'))
    main=runpy.run_path(str(root/'check.py'))
vec,br,add,sub,sc,d,F=[q[k] for k in ('vec','br','add','sub','sc','d','F')]
checks=[]
def eq(n,a,b):
    if a!=b: raise RuntimeError('FAIL: '+n)
    checks.append(n)
def neq(n,a,b):
    if a==b: raise RuntimeError('MUTATION SURVIVED: '+n)
    checks.append(n)
eq('curvature identical to full four-entry transgression',q['C4'],main['C4'])
x,y,z=vec('a'),vec('b'),vec('c')
anti=add(br(x,br(y,z)),br(y,br(x,z)))
eq('independent symmetric double-adjoint trace identity',anti,add(sc(4*d(x,y),z),sc(-2*d(x,z),y),sc(-2*d(y,z),x)))
neq('curvature omission rejected',q['W'],q['Q4'])
neq('curvature sign reversal rejected',q['W'],sub(q['Q4'],q['C4']))
for name in ('Q4','C4','W'):
    for coord in q[name]:
        for monomial in coord:
            if len(monomial)!=4 or sorted(v[1] for v in monomial)!=list('1234') or any(v[0] not in 'LU' for v in monomial):
                raise RuntimeError('Invalid multilinear sector premise: '+name)
    checks.append('four distinct current slots validated: '+name)
# Exhaustive coefficient projection must reconstruct the entire polynomial.
from itertools import product
for name in ('Q4','C4','W'):
    eq('exhaustive sixteen-sector reconstruction: '+name,q[name],add(*(q['sector'](q[name],''.join(word)) for word in product('LU',repeat=4))))
print(json.dumps({'status':'PASS','checks':checks,'scope':'Independent formula/mutation controls with shared scalar algebra; no physical current values.'},indent=2))
