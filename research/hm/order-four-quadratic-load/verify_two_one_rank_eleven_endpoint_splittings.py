#!/usr/bin/env python3
"""Bounded universal rank-eleven endpoint characters; no actual map evaluations."""
import hashlib
from pathlib import Path
import runpy,contextlib,io,json,itertools
R=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):r=runpy.run_path(str(R/'verify_adjacent_rank_three_gauss.py'))
for k in ('reps','va','vs','vm','sym','dimension','effective','zero','U'):globals()[k]=r[k]
def hc(B,t=0):
 out=[zero]
 for e,n in B:
  d=e+t
  if d>=0:out.append(vm(reps[n],sym(d)))
  elif d<=-2:out.append(vs(-1,vm(reps[n],sym(-d-2))))
 return va(*out)
def h0(B,t=0):return hc([(e,n) for e,n in B if e+t>=0],t)
def line(d,k,t):return va(hc([(k,'one')],t),vs(-1,hc([(k-d,'one')],t)))
def opts(s):
 if s==0:return [()]
 if s in (12,20,30):return [((s,k),) for k in range(0,{12:10,20:6,30:4}[s],2)]
 if s==24:return [((24,k),) for k in range(0,10,2)]+[((12,k),(12,l)) for k in range(0,10,2) for l in range(k,10,2)]
 if s==32:return [((12,k),(20,l)) for k in range(0,10,2) for l in range(0,6,2)]
def tc(o,t):return va(zero,*[line(d,k,t) for d,k in o])
chiE4=va(vm(r['M3'],sym(3)),vs(-1,vm(va(vs(2,reps['V']),vs(4,reps['P']),vs(3,reps['D'])),sym(4))))
pairs=json.loads((R/'two-one-primal-interior-quotient-summary.json').read_text())['pairs']
from functools import lru_cache
names=list(reps)
def vec(v):
 values=tuple(r['multiplicity'](v,reps[n]) for n in names)
 assert all(x==int(x) for x in values)
 return tuple(map(int,values))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
vzero=(0,)*len(names)
@lru_cache(None)
def endpoint(X,Z,H):
 # X=H1(M3), Z=chi(M4), H=H0(A).
 cap=sum(x*dimension(reps[n]) for x,n in zip(X,names))
 blocks=[]
 for j in range(1,cap+1):
  for n,R0 in reps.items():
   dim=dimension(R0)
   if dim*j>cap or R0[1][0]!=(-1)**j*R0[0][0]:continue
   c=vec(vm(R0,sym(j-1)));d=vec(vm(R0,sym(j-2))) if j>=2 else vzero
   if all(a<=b for a,b in zip(c,X)):blocks.append((j,n,dim,c,d))
 @lru_cache(None)
 def solve(i,x,z,rank):
  if i==len(blocks):
   if any(x) or min(z)<0 or any(a>b for a,b in zip(z,H)):return ()
   if sum(a*dimension(reps[n]) for a,n in zip(z,names))!=rank:return ()
   if any(a and reps[n][1][0]!=reps[n][0][0] for a,n in zip(z,names)):return ()
   return (tuple((-4,n) for a,n in zip(z,names) for _ in range(a)),)
  j,n,dim,c,d=blocks[i]
  lim=min([rank//dim]+[a//b for a,b in zip(x,c) if b])
  out=[]
  for m in range(lim+1):
   for rest in solve(i+1,tuple(a-m*b for a,b in zip(x,c)),tuple(a+m*b for a,b in zip(z,d)),rank-m*dim):
    out.append(tuple([(-4-j,n)]*m)+rest)
  return tuple(out)
 return solve(0,X,Z,11)

SOURCE_HASH='33c37ec7fe996888465d7950ebab02100c73177fceb85e9fde5434edcbbd575c'
assert hashlib.sha256((R/'two-one-primal-interior-quotient-summary.json').read_bytes()).hexdigest()==SOURCE_HASH
assert len(pairs)==13 and sum(p['records'] for p in pairs)==877
assert all(r['hom'](reps[a],reps[b])==int(a==b) for a in names for b in names)
expected=[[],[0],[0,12,20,24],[0],[0],[0,12,20,24],[0],[0],[0,12],[0,12,20,24,32],[0,12,20,24],[0],[0]]
results=[]
es={3:U,4:chiE4}
for q in range(4,9):es[q+1]=va(vm(reps['W'],es[q]),vs(-1,es[q-1]))
for q in range(3,-2,-1):es[q-1]=va(vm(reps['W'],es[q]),vs(-1,es[q+1]))
for i,p in enumerate(pairs):
 A=p['A']; X=va(hc(A,3),hc(A,1),vs(-1,U));Z=va(chiE4,vs(-1,hc(A,4)),vs(-1,hc(A,2)))
 survivors=[]
 for s in p['second_primal_defects']:
  for o in opts(s):
   assert sum(d for d,k in o)==s
   assert dimension(tc(o,3))==s
   assert dimension(va(X,vs(-1,tc(o,3))))==4+2*p['a']-s
   x=vec(va(X,vs(-1,tc(o,3))));z=vec(va(Z,tc(o,4)))
   if min(x)<0:continue
   ms=endpoint(x,z,vec(h0(A)))
   for M in ms:
    assert sum(dimension(reps[n]) for e,n in M)==11
    assert max(e for e,n in M)<=-4
    assert sum(e*dimension(reps[n]) for e,n in M)==-48-2*p['a']+s
    assert vec(vs(-1,hc(M,3)))==x and vec(hc(M,4))==z
    assert effective(va(h0(A),vs(-1,h0(M,4))))
    assert all(reps[n][1][0]==(-1)**e*reps[n][0][0] for e,n in M)
    # Two consecutive Euler characters determine all twists by the Euler sequence.
    for t in range(-2,9):
     # Recur from the two known E characters rather than assuming an E split.
     assert hc(M,t)==va(es[t],vs(-1,hc(A,t)),vs(-1,hc(A,t-2)),tc(o,t))
   if ms:survivors.append(dict(s=s,torsion=o,endpoint_count=len(ms),endpoints=ms))
 defects=sorted({x['s'] for x in survivors})
 assert defects==expected[i],(i,defects)
 results.append(dict(source_pair_index=i,A=A,B=p['B'],a=p['a'],original_defect=p['original_defect'],retained_second_defects=defects,source_records=p['records'],alternatives=survivors))
 print(i,defects,'endpoint witnesses',sum(x['endpoint_count'] for x in survivors))
# Transparent certificates for the two whole-defect exclusions.
x=vec(vs(2,reps['S']))
low=[]
for j in range(1,9):
 for n,R0 in reps.items():
  if R0[1][0]==(-1)**j*R0[0][0] and all(a<=b for a,b in zip(vec(vm(R0,sym(j-1))),x)):
   low.append((-4-j,n))
assert low==[(-5,'S'),(-8,'one')]
A=pairs[0]['A']
assert va(hc(A,3),hc(A,1),vs(-1,U))==vs(2,reps['S'])
assert va(chiE4,vs(-1,hc(A,4)),vs(-1,hc(A,2)))==va(vs(-2,reps['A']),vs(2,reps['V']),vs(2,reps['P']),vs(-1,reps['D']))
x=vec(reps['Wp'])
low=[]
for j in range(1,3):
 for n,R0 in reps.items():
  if R0[1][0]==(-1)**j*R0[0][0] and all(a<=b for a,b in zip(vec(vm(R0,sym(j-1))),x)):
   low.append((-4-j,n))
assert low==[(-5,'Wp')]
A=pairs[9]['A']
for k,z in ((0,va(vs(-1,reps['A']),reps['V'],reps['P'],reps['D'])),(2,va(vs(-1,reps['one']),vs(2,reps['V']),reps['P']))):
 assert va(hc(A,3),hc(A,1),vs(-1,U),vs(-1,line(30,k,3)))==reps['Wp']
 assert va(chiE4,vs(-1,hc(A,4)),vs(-1,hc(A,2)),line(30,k,4))==z
assert len([p for p in results if p['retained_second_defects']])==12
assert results[9]['alternatives'][-1]['torsion']==((12,4),(20,2))
assert results[9]['alternatives'][-1]['endpoints']==(((-4,'V'),(-4,'P'),(-4,'P')),)
out=dict(scope='Necessary endpoint splittings only; no global or actual realization assertion.',source_sha256=SOURCE_HASH,
 remaining_pair_count=12,remaining_source_records=sum(p['source_records'] for p in results if p['retained_second_defects']),
 dependencies={f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ('verify_adjacent_rank_three_gauss.py','verify_exceptional_cubic_gauss_corner.py','verify_equivariant_splitting_gauss_persistence.py','verify_negative_vertex_scalar.py')},pairs=results)
(R/'two-one-rank-eleven-endpoint-splittings.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 13 -> 12 necessary pairs; s=30 excluded; s=32 retained; two additional branches have s=0.')
print('Remaining source records:',out['remaining_source_records'])
