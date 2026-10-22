"""Bounded necessary characters for (1,2); no Q* splitting enumeration or map instances."""
from pathlib import Path
from itertools import combinations_with_replacement
from functools import lru_cache
from collections import Counter
import runpy,contextlib,io,json,hashlib
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_equivariant_splitting_gauss_persistence.py'))
names=tuple(r['reps']); reps=r['reps']; inner=r['inner']
def decomp(ch):
 out=tuple(inner(ch,reps[n]) for n in names)
 assert all(b==0 and a.denominator==1 for a,b in out)
 return tuple(int(a) for a,b in out)
zero=(0,)*len(names)
def add(*xs):return tuple(map(sum,zip(*xs))) if xs else zero
def neg(x):return tuple(-a for a in x)
def eff(x):return min(x)>=0
@lru_cache(None)
def prod(n,d):return decomp(r['vm'](reps[n],r['sym'](d)))
@lru_cache(None)
def hc(B,t=0,euler=False):
 return add(*(prod(n,e+t) if e+t>=0 else neg(prod(n,-e-t-2)) if euler and e+t<=-2 else zero for e,n in B))
def h1(B,t=0):return add(hc(B,t),neg(hc(B,t,True)))
def dim(n):return int(reps[n][0][0])
def degree(B):return sum(e*dim(n) for e,n in B)
def ordinary(B):return sorted(e for e,n in B for _ in range(dim(n)))
def nd(B):return tuple(sorted((-e-2,n) for e,n in B))
def shapes(lo,hi):
 lines=[(e,'one') for e in range(lo,hi+1) if e%2==0]
 yield from combinations_with_replacement(lines,3)
 for e in range(lo,hi+1):
  if e%2:
   for n in ('W','Wp'):
    for L in lines:yield tuple(sorted(((e,n),L)))
  else:
   for n in ('A','V'):yield ((e,n),)
@lru_cache(None)
def hom(e,n,f,m):
 if f<e:return False
 return prod(m,f-e)[names.index(n)]>0
# Every source block must have a nonzero restriction; every target block a projection.
def embeds(B,C):return all(any(hom(e,n,f,m) for f,m in C) for e,n in B)
def receives(B,C):return all(any(hom(f,m,e,n) for f,m in C) for e,n in B)
U=decomp(r['chiE3']); E2=decomp(r['chiE2'])
Q2=decomp(r['va'](r['vm'](r['M3'],r['W']),r['vs'](-1,r['vm'](r['M2'],r['A']))))
AA=[B for B in shapes(-10,26) if -8<=degree(B)<=6 and eff(add(hc(B,3,True),hc(B,1),neg(U))) and eff(add(hc(B,2,True),neg(E2)))]
def chiQ(t):
 def line(d):return r['sym'](d) if d>=0 else r['vs'](-1,r['sym'](-d-2)) if d<=-2 else r['vs'](0,r['one'])
 return decomp(r['va'](r['vm'](r['M3'],line(t-1)),r['vs'](-1,r['vm'](r['M2'],line(t)))))
BB0=[B for B in shapes(-28,8) if -12<=degree(B)<=2 and eff(add(hc(B,0,True),hc(B,2,True),neg(Q2)))]
BB=[B for B in BB0 if all(eff(add(neg(chiQ(t)),neg(h1(B,t)))) for t in range(-2,1))]
Es=[]
for co,R2,blocks in r['profiles']:
 E=tuple(sorted((-j,n) for j,R in blocks for n,mul in zip(names,decomp(R)) for _ in range(mul)))
 assert len(ordinary(E))==17 and degree(E)==-54 and min(ordinary(E))>=-10
 Es.append((co,E))
assert len(Es)==28
pairs=[]
for A in AA:
 eligible=[(co,E) for co,E in Es if receives(A,E) and eff(add(hc(A,2),neg(hc(E,2))))
 and eff(add(hc(A,3),hc(A,1),neg(hc(E,3))))
 and all(eff(add(h1(E,t),neg(h1(A,t)))) for t in range(-2,9))]
 if not eligible:continue
 for B in BB:
  t=-6-degree(A)-degree(B)
  if t not in (0,12):continue
  if t==0 and A!=nd(B):continue
  if any(x>y for x,y in zip(ordinary(A),ordinary(nd(B)))):continue
  if not embeds(A,nd(B)) or not embeds(B,nd(A)):continue
  co=[co for co,E in eligible if embeds(B,nd(E))]
  if co:pairs.append(dict(A=A,B=B,defect=t,E_types=co))
# Isolate the twelve-defect certificate using only the preliminary filters.
twelve=[]
for A in AA:
 for B in BB0:
  if -6-degree(A)-degree(B)!=12:continue
  if any(x>y for x,y in zip(ordinary(A),ordinary(nd(B)))):continue
  if not embeds(A,nd(B)) or not embeds(B,nd(A)):continue
  if any(receives(A,E) and eff(add(hc(A,2),neg(hc(E,2)))) and embeds(B,nd(E)) for co,E in Es):
   twelve.append((A,B))
assert len(twelve)==5
assert all(any(n=='one' and e in (-14,-26) for e,n in B) for A,B in twelve)
assert neg(chiQ(0))==decomp(r['M2'])
assert prod('one',12)[names.index('one')]==1
assert prod('one',24)[names.index('one')]==1
assert neg(chiQ(0))[names.index('one')]==0
assert all(h1(B,0)[names.index('one')]>=1 for A,B in twelve)
assert len(AA)==154 and len(BB0)==228 and len(BB)==91
assert len(pairs)==25 and Counter(p['defect'] for p in pairs)=={0:25}
assert sum(len(p['E_types']) for p in pairs)==155
assert len({tuple(co) for p in pairs for co in p['E_types']})==25
print('Preliminary quotient shapes:',len(AA),len(BB))
print('Surviving pairs:',len(pairs),'defects:',dict(Counter(p['defect'] for p in pairs)))
print('Surviving E types:',len({tuple(co) for p in pairs for co in p['E_types']}))
catalog=[co for co,E in Es]
output=dict(scope='Necessary formal candidates only; no realizability or rank-three exclusion.',
 inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('verify_negative_vertex_scalar.py','verify_equivariant_splitting_gauss_persistence.py','ONE-TWO-ASYMMETRIC-QUOTIENT-DEGREE-AND-DEFECT-BOUNDS.md')},
 preliminary_shapes=dict(A=len(AA),B_before_quotient_h1=len(BB0),B_after_quotient_h1=len(BB)),
 pair_count=len(pairs),record_count=155,E_catalog=catalog,
 pairs=[dict(A=p['A'],B=p['B'],defect=p['defect'],E_ids=[catalog.index(co) for co in p['E_types']]) for p in pairs],
 excluded_twelve_pairs=[dict(A=A,B=B,H1_B_trivial_multiplicity=h1(B,0)[0]) for A,B in twelve])
(ROOT/'one-two-finite-quotient-pairs.json').write_text(json.dumps(output,indent=2)+'\n')
print('PASS: all five preliminary twelve-defect pairs violate H1(B) <= M2 in the trivial character.')
print('PASS: 25 necessary isomorphism pairs, 155 pair/E records, 25 E types; no Q* splitting assumption.')
