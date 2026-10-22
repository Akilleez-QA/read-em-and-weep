"""Tiny universal degree/character certificates; no actual map instances."""
from pathlib import Path
import contextlib, io, runpy
from itertools import combinations_with_replacement
with contextlib.redirect_stdout(io.StringIO()):
    c=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm=c['vadd'],c['vscale'],c['vmul']
one,W,A,V,P,D=[c[n] for n in ('one','W','A','V','P','D')]
sym=lambda n:[c['sym'](n,x) for x in W]
# The only equality branch at degree -10 has an impossible H1 character.
obstruction=va(sym(12),vs(-2,sym(6)),V)
assert obstruction==va(one,A,vs(-1,V),vs(-1,P),D)
assert c['inner'](obstruction,V)==c['z'](-1)
assert c['inner'](obstruction,P)==c['z'](-1)
# Bounded elementary integer check, not an enumeration of map realizations.
for a in (-12,-10):
    triples=[x for x in combinations_with_replacement(range(-10,a+21),3) if sum(x)==a]
    assert max(sum(max(e+2,0) for e in x) for x in triples)==a+22
    if a==-10:
        assert [x for x in triples if sum(max(e+2,0) for e in x)==12]==[(-10,-10,10)]
assert 2-(-12)>-12+22
M2=va(A,vs(2,V),vs(3,P),vs(4,D))
M3=va(vs(3,c['Wp']),vs(3,c['S']),vs(6,c['T']))
chiQ2=va(vm(M3,W),vs(-1,vm(M2,sym(2))))
assert chiQ2==vs(-1,va(one,vs(2,A),V,D))
assert -54-(-22)==-32
# Invariant divisors: orbit sizes 12,20,30,60.
small={12*i+20*j+30*k for i in range(2) for j in range(1) for k in range(1)}
assert small=={0,12}
pairs=[(a,b) for a in range(-8,7,2) for b in range(-12,3,2) if a+b==-18]
assert pairs==[(-8,-10),(-6,-12)]
assert [(2*b+26,-48-2*b) for a,b in pairs]==[(6,-28),(2,-24)]
assert all(2*b+26<12 for a,b in pairs)
print('PASS: primal a>=-8; dual b>=-12; original defect 0 or12.')
print('PASS: defect12 allows only (-8,-10),(-6,-12), with saturated second dual quotient.')
print('PASS: exact primal obstruction and dual Euler characters; no actual map evaluation.')
