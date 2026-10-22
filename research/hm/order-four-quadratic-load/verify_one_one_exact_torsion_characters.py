#!/usr/bin/env python3
"""Exact universal torsion characters; no selected coefficients, points or maps."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
import contextlib, io, runpy, json, hashlib
ROOT=Path(__file__).parent
EXPECTED_HASHES={
    'one-one-endpoint-necessary-pairs.json':'6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb',
    'verify_negative_vertex_scalar.py':'e81f548a7e0ea4069ea293ca3b86b1110c2fd6c2906e8637d1441b35f6f14af2',
}
for name,digest in EXPECTED_HASHES.items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest, ('input changed',name)
with contextlib.redirect_stdout(io.StringIO()):
    ring=runpy.run_path(str(ROOT/'verify_negative_vertex_scalar.py'))
names=('one','W','Wp','A','V','P','S','D','T'); reps=[ring[n] for n in names]; zero=(0,)*9
assert sum(int(R[0][0])**2 for R in reps)==120
for i,R in enumerate(reps):
    for j,S in enumerate(reps):assert ring['inner'](R,S)==ring['z'](int(i==j))
def dec(ch):
    out=[ring['inner'](ch,R) for R in reps]
    assert all(y==0 and x.denominator==1 for x,y in out)
    return tuple(int(x) for x,y in out)
def add(*xs):return tuple(map(sum,zip(*xs))) if xs else zero
def neg(x):return tuple(-v for v in x)
@lru_cache(None)
def block(e,n,r):
    d=e+r
    if d==-1:return zero
    ch=dec(ring['vmul'](ring[n],[ring['sym'](d if d>=0 else -d-2,w) for w in ring['W']]))
    return ch if d>=0 else neg(ch)
def chi(X,r):return add(*(block(e,n,r) for e,n in X))
def torsion(s,k,r):return add(block(k,'one',r),neg(block(k-s,'one',r)))
def shape_char(shape,r):
    kind,ks=shape
    if kind=='zero':return zero
    if kind=='reduced12':return torsion(12,ks[0],r)
    if kind=='reduced20':return torsion(20,ks[0],r)
    if kind=='cyclic24':return torsion(24,ks[0],r)
    assert kind=='semisimple24'
    return add(*(torsion(12,k,r) for k in ks))
shapes={0:[('zero',())],12:[('reduced12',(k,)) for k in range(0,10,2)],20:[('reduced20',(k,)) for k in range(0,6,2)],24:[('cyclic24',(k,)) for k in range(0,10,2)]+[('semisimple24',ks) for ks in combinations_with_replacement(range(0,10,2),2)]}
# Check periodicity and the conormal character k-12 = k-2 mod 10.
for r in range(-32,33):
    for k in range(0,10,2):
        assert torsion(12,k,r)==torsion(12,k+10,r)
        assert torsion(24,k,r)==torsion(24,k+10,r)
        assert torsion(24,k,r)==add(torsion(12,k,r),torsion(12,(k-2)%10,r))
    for k in range(0,6,2):assert torsion(20,k,r)==torsion(20,k+6,r)
source=ROOT/'one-one-endpoint-necessary-pairs.json'; old=json.loads(source.read_text())
assert len(old)==159
assert dict(Counter(p['defect'] for p in old))=={0:80,12:61,20:5,24:13}
records=[]; rejected=[]
for i,p in enumerate(old):
    A=tuple(map(tuple,p['A'])); B=tuple(map(tuple,p['B'])); C=tuple((-e-2,n) for e,n in B)
    def delta(r):return add(chi(C,r),neg(chi(A,r)))
    for X,d in ((A,p['a']),(B,p['b'])):
        assert sum(int(ring[n][0][0]) for e,n in X)==3
        assert sum(e*int(ring[n][0][0]) for e,n in X)==d
        assert all(ring[n][1][0]==(-1)**e*ring[n][0][0] for e,n in X)
    assert p['defect']==-6-p['a']-p['b']
    matches=[s for s in shapes[p['defect']] if all(delta(r)==shape_char(s,r) for r in (0,1))]
    # Two twists suffice by the equivariant Euler recurrence; check a redundant interval.
    for s in matches:assert all(delta(r)==shape_char(s,r) for r in range(-32,33))
    item=dict(pair_id=i,**p,possible_torsion_shapes=matches)
    (records if matches else rejected).append(item)
counts=dict(sorted(Counter(p['defect'] for p in records).items()))
out=dict(scope='Necessary exact-character overlist, not realization or profile exclusion.',inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('one-one-endpoint-necessary-pairs.json','verify_negative_vertex_scalar.py')},input_count=len(old),remaining_count=len(records),remaining_by_defect=counts,remaining_ids=[p['pair_id'] for p in records],records=records,rejected_ids=[p['pair_id'] for p in rejected],rejected_by_defect=dict(sorted(Counter(p['defect'] for p in rejected).items())))
(ROOT/'one-one-exact-torsion-characters.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact torsion character filter:',len(old),'->',len(records),'by defect',counts)
print('Rejected by defect:',out['rejected_by_defect'])
print('Reduced-defect stabilizer counts:',{t:dict(Counter(p['possible_torsion_shapes'][0][1][0] for p in records if p['defect']==t)) for t in (12,20)})
print('PASS: exhaustive reduced-orbit and length-two local module alternatives; twists 0,1 plus redundant -32..32 checks.')
# Exact stabilizer restriction from character orthogonality over the cyclic group.
# z is a formal primitive root; reduction modulo its cyclotomic polynomial is exact.
import sympy as sp
z=sp.Symbol('z')
@lru_cache(None)
def restriction(n,m):
    indexes={10:(0,2,5,4,3,1,3,4,5,2),6:(0,6,7,1,7,6)}[m]
    poly=sp.Poly(sp.cyclotomic_poly(m,z),z)
    sqrt5=2*(z+z**(m-1))-1 if m==10 else None
    vals=[]
    for i in indexes:
        a,b=ring[n][i]
        assert m==10 or b==0
        vals.append(sp.Rational(a.numerator,a.denominator)+(sp.Rational(b.numerator,b.denominator)*sqrt5 if b else 0))
    out=[]
    for w in range(m):
        v=sp.rem(sum(vals[j]*z**((-w*j)%m) for j in range(m)),poly.as_expr(),z)/m
        v=sp.simplify(v); assert v.is_Integer and v>=0
        out.append(int(v))
    assert sum(out)==int(ring[n][0][0])
    return tuple(out)
def fiber(X,m):
    out=[0]*m
    for e,n in X:
        for w,v in enumerate(restriction(n,m)):out[(w+e)%m]+=v
    return out
def subtract_weights(v,ws,m):
    v=v.copy()
    for w in ws:v[w%m]-=1
    return v if min(v)>=0 else None
local_records=[]
for p in records:
    t=p['defect']; A=p['A']; C=[(-e-2,n) for e,n in p['B']]
    good=[]
    for kind,ks in p['possible_torsion_shapes']:
        if not t:good.append((kind,ks));continue
        m=6 if t==20 else 10
        source_ws=[k-(24 if kind=='cyclic24' else 20 if t==20 else 12) for k in ks]
        u=subtract_weights(fiber(A,m),source_ws,m)
        v=subtract_weights(fiber(C,m),ks,m)
        if u is not None and v is not None and u==v:good.append((kind,ks))
    if good:local_records.append(dict(p,possible_torsion_shapes=good))
out['local_fiber_remaining_count']=len(local_records)
out['local_fiber_remaining_by_defect']=dict(sorted(Counter(p['defect'] for p in local_records).items()))
out['local_fiber_records']=local_records
out['local_fiber_rejected_ids']=sorted(set(p['pair_id'] for p in records)-set(p['pair_id'] for p in local_records))
(ROOT/'one-one-exact-torsion-characters.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('Local fiber/Tor compatibility:',len(local_records),out['local_fiber_remaining_by_defect'])
print('Local fiber rejected IDs:',out['local_fiber_rejected_ids'])
print('24-defect local shapes:',[(p['pair_id'],p['possible_torsion_shapes']) for p in local_records if p['defect']==24])

assert len(records)==len(local_records)==159
assert counts=={0:80,12:61,20:5,24:13}
assert all(len(p['possible_torsion_shapes'])==(2 if p['defect']==24 else 1) for p in local_records)
assert {p['pair_id'] for p in local_records if p['defect']==24 and p['possible_torsion_shapes'][0][1]==(4,)}=={8,15,19,20}
assert {p['pair_id'] for p in local_records if p['defect']==24 and p['possible_torsion_shapes'][0][1]==(6,)}=={9,10,11,12,13,14,16,17,18}
print('PASS: all 159 pairs survive exact sheaf characters and stabilizer fiber/Tor tests; no pruning or realization claimed.')
