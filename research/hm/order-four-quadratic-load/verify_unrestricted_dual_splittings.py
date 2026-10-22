#!/usr/bin/env python3
"""Universal exact character and bounded integer enumeration, never map instances."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import contextlib,io,runpy,json,time,hashlib
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_negative_vertex_scalar.py'))
names=('one','W','Wp','A','V','P','S','D','T'); reps=[r[n] for n in names]
zero=(0,)*9
unit=lambda i:tuple(int(i==k) for k in range(9))
def dec(ch):
 a=[r['inner'](ch,R) for R in reps]
 assert all(y==0 and x.denominator==1 for x,y in a)
 return tuple(int(x) for x,y in a)
def add(*xs):return tuple(map(sum,zip(*xs))) if xs else zero
def neg(x):return tuple(-v for v in x)
def scale(k,x):return tuple(k*v for v in x)
def eff(x):return min(x)>=0
D=[int(R[0][0]) for R in reps]
tensors={(i,j):dec(r['vmul'](reps[i],reps[j])) for i in range(9) for j in range(9)}
def mul(x,y):return tuple(sum(x[i]*y[j]*tensors[i,j][k] for i in range(9) for j in range(9) if x[i] and y[j]) for k in range(9))
@lru_cache(None)
def sym(n):
 assert n>=0
 return unit(0) if n==0 else unit(1) if n==1 else add(mul(unit(1),sym(n-1)),neg(sym(n-2)))
@lru_cache(None)
def prod(i,n):return mul(unit(i),sym(n))
M2=(0,0,0,1,2,3,0,4,0); M3=(0,0,3,0,0,0,3,0,6)
coords3=(2,6,8);coords2=(3,4,5,7)
blocks=[]
for j in range(1,55):
 for i,R in enumerate(reps):
  if j*D[i]>54 or R[1][0]!=(-1)**j*D[i]:continue
  c3=prod(i,j-1);c2=prod(i,j-2) if j>=2 else zero
  if eff(add(M3,neg(c3))) and eff(add(M2,neg(c2))):
   v=tuple(c3[k] for k in coords3)+tuple(c2[k] for k in coords2)
   assert c3==add(*(scale(c3[k],unit(k)) for k in coords3))
   assert c2==add(*(scale(c2[k],unit(k)) for k in coords2))
   blocks.append((j,i,v))
@lru_cache(None)
def solve(i,remaining):
 if i==len(blocks):return int(not any(remaining))
 v=blocks[i][2];cap=min(x//y for x,y in zip(remaining,v) if y)
 return sum(solve(i+1,tuple(x-c*y for x,y in zip(remaining,v))) for c in range(cap+1))
def enumerate_counts(i,remaining):
 if i==len(blocks):
  if not any(remaining):yield ()
  return
 v=blocks[i][2];cap=min(x//y for x,y in zip(remaining,v) if y)
 for c in range(cap+1):
  rest=tuple(x-c*y for x,y in zip(remaining,v))
  if solve(i+1,rest):
   for tail in enumerate_counts(i+1,rest):yield (c,)+tail
start=time.monotonic()
remaining=(3,3,6,1,2,3,4)
assert len(blocks)==26
assert solve(0,remaining)==260
assert solve.cache_info().currsize<=27*4*4*7*2*3*4*5==362880
profiles=[tuple((-j,i) for (j,i,v),c in zip(blocks,co) for _ in range(c)) for co in enumerate_counts(0,remaining)]
assert len(profiles)==260 and len(set(profiles))==260
assert sum(not any(e==-1 for e,i in Q) for Q in profiles)==37
assert max(-e for Q in profiles for e,i in Q)==28
@lru_cache(None)
def h0(X,t):return add(*(prod(i,e+t) for e,i in X if e+t>=0))
@lru_cache(None)
def h1(X,t):return add(*(prod(i,-e-t-2) for e,i in X if e+t<=-2))
def degree(X):return sum(e*D[i] for e,i in X)
def nd(X):return tuple((-e-2,i) for e,i in X)
@lru_cache(None)
def hom(e,i,f,k):return f>=e and prod(k,f-e)[i]>0
def embeds(X,Y):return all(any(hom(e,i,f,k) for f,k in Y) for e,i in X)
def receives(X,Y):return all(any(hom(f,k,e,i) for f,k in Y) for e,i in X)
for Q in profiles:
 assert sum(D[i] for e,i in Q)==13 and degree(Q)==-54
 assert h1(Q,0)==M2 and h1(Q,-1)==M3
print('Blocks:',[(j,names[i]) for j,i,v in blocks],flush=True)
print('Profiles:',len(profiles),'DP states:',solve.cache_info(),'seconds',time.monotonic()-start,flush=True)
print('Degree-one coefficient characters:',dict(Counter(tuple(h0(Q,1)) for Q in profiles)),flush=True)
def convert(X):return tuple((e,names.index(n)) for e,n in X)
def compatible(A,B,Q):
 # One and the same Q must receive the quotient B and admit A into Q(-2).
 if not receives(B,Q) or not embeds(A,nd(Q)):return False
 # L has top degree <=-2, and H0(L(2)) injects into H0(B).
 if not eff(add(h0(B,1),neg(h0(Q,1)))):return False
 if not eff(add(h0(B,2),h0(B,0),neg(h0(Q,2)))):return False
 # Necessary inequalities only; this range is a declared finite filter.
 return all(eff(add(h1(Q,u),neg(h1(B,u)))) and eff(add(h1(Q,-u),neg(h0(A,u)))) for u in range(-30,31))
outputs={}
source11=json.loads((ROOT/'one-one-endpoint-necessary-pairs.json').read_text())
source12=json.loads((ROOT/'one-two-finite-quotient-pairs.json').read_text())
ids12=json.loads((ROOT/'one-two-endpoint-orbit-constraints.json').read_text())['remaining_pair_ids']
for label,source,ids in [('one_one',source11,range(len(source11))),('one_two',source12['pairs'],ids12)]:
 records=[]
 for pid in ids:
  p=source[pid];A=convert(p['A']);B=convert(p['B'])
  qs=[i for i,Q in enumerate(profiles) if compatible(A,B,Q)]
  if qs:records.append(dict(pair_id=pid,Q_ids=qs))
 outputs[label]=records
 print(label,'remaining pairs',len(records),'ids',[p['pair_id'] for p in records],flush=True)
 print(label,'defects',dict(Counter(source[p['pair_id']]['defect'] for p in records)),flush=True)
 print(label,'Q types',len(set(q for p in records for q in p['Q_ids'])),flush=True)
assert len(outputs['one_one'])==126 and len(outputs['one_two'])==10
assert Counter(source11[p['pair_id']]['defect'] for p in outputs['one_one'])=={0:60,12:51,20:2,24:13}
assert [sum(len(p['Q_ids']) for p in outputs[k]) for k in ('one_one','one_two')]==[2140,594]
out=dict(inputs={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('verify_negative_vertex_scalar.py','one-one-endpoint-necessary-pairs.json','one-two-finite-quotient-pairs.json','one-two-endpoint-orbit-constraints.json')},scope='Necessary unrestricted formal splitting and pair compatibility, not realization.',blocks=[(j,names[i],v)for j,i,v in blocks],profiles=[[(e,names[i]) for e,i in Q] for Q in profiles],compatibility=outputs)
(ROOT/'unrestricted-dual-splittings-and-pairs.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: unrestricted j>=1 classification; no Q*(1) vanishing imposed.')
