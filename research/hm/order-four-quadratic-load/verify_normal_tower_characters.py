#!/usr/bin/env python3
"""Universal exact character arithmetic, no actual coefficients or ranks."""
import runpy
from pathlib import Path
r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm,vs=r['vadd'],r['vmul'],r['vscale']
H,N,Wp,L2=[r[k] for k in ('H','N','Wp','L2')]
fc={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}
def chi_b(t):
    out=vs(-1,r['ambient_sym'](t))
    for i,x in fc.items():
        for j,y in fc.items():out=va(out,vm(vm(x,y),r['ambient_sym'](t+1+i+j)))
    return out
def decomp(x):return {n:r['inner'](r[n],x)[0] for n in ('one','A','V','P','D','W','Wp','S','T')}
h0={1:vs(0,r['one']),3:vs(0,r['one']),5:va(r['one'],r['P'],r['D'])}
expected={1:[0,1,2,2,2,1,0,2,3],3:[1,4,2,3,3,0,3,3,6],5:[1,1,1,0,1,0,1,0,3]}
for t in (1,3,5):
    ch=va(h0[t],vs(-1,chi_b(t)))
    d=decomp(ch)
    assert list(d.values())==expected[t]
    print('H1 B(%d):'%t,d)
# Primary twist-three representation, using H0(F(3))=P and higher support.
chi_f3=va(*(vm(c,r['ambient_sym'](3+i)) for i,c in fc.items()))
f3=va(r['P'],vs(-1,chi_f3))
print('H1 F(3):',decomp(f3))
assert f3==r['W']
primary3=vm(r['P'],r['M1']);primary5=vm(r['P'],f3)
assert r['inner'](r['one'],primary3)==r['z'](1)
assert r['inner'](r['one'],primary5)==r['z'](0)
print('PASS: primary twist-three adjoint image has exactly one invariant;')
print('primary twist-five adjoint image has none. Naturality forces q0 on invariants zero.')
