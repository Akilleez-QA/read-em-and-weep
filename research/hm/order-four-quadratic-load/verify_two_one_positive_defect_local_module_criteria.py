#!/usr/bin/env python3
"""Complete local top and kernel-fiber test for positive second defects."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from collections import Counter
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad', 'two-one-rank-eleven-endpoint-splittings.json': '4704e794183cb1a2b0bf5069e3baedafeedc9ae186c40dea2917766100d23a16', 'two-one-second-defect-twenty-four-image-exclusion.json': '33ee4b7a878cf002257ff63189e57984af5240518747d03bc5fc0057b42e37ef'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
data={f:json.loads((ROOT/f).read_text())for f in PINNED}
front=data['rank-three-quotient-frontier-144.json']
pairs=data['two-one-rank-eleven-endpoint-splittings.json']['pairs']
prior={c['id']for c in data['two-one-second-defect-twenty-four-image-exclusion.json']['cases']}
assert chars['Wp'][2]==phip and chars['Wp'][6]==z(1) and chars['Wp'][8]==z(0)
# Determinant one and these traces give the restrictions at orders10,6,4.
restr={10:{'one':(0,), 'W':(1,9), 'Wp':(3,7)},6:{'one':(0,), 'W':(1,5), 'Wp':(1,5)},4:{'one':(0,), 'W':(1,3), 'Wp':(1,3)}}
results=[]
for p in pairs:
 if not any(a['s']for a in p['alternatives']):continue
 row=next(c for c in front['cases']if c['profile']=='21' and c['source_index']==p['source_pair_index'])
 assert row['A']==p['A'] and row['status']=='not_excluded'
 for ai,alt in enumerate(p['alternatives']):
  if alt['s']==0:continue
  local=[];valid=True
  for d,m in ((12,10),(20,6),(30,4)):
   source=Counter((e-2+w)%m for e,n in p['A']for w in restr[m][n])
   summands=[(k,2 if size==24 else 1)for size,k in alt['torsion']if (12 if size==24 else size)==d]
   top=Counter(k%m for k,length in summands)
   ok=all(source[k]>=count for k,count in top.items());valid &= ok
   # Exact Tor1 sequence: each generator k is replaced by k-length*d.
   kernel=source.copy();kernel.subtract(top)
   kernel.update((k-length*d)%m for k,length in summands)
   assert sum(kernel.values())==3
   local.append(dict(orbit=d,stabilizer=m,source=sorted(source.elements()),top=sorted(top.elements()),passes=ok,kernel_fiber=sorted(kernel.elements())if ok else None))
  results.append(dict(id=row['id'],source_pair_index=p['source_pair_index'],alternative_id=ai,s=alt['s'],torsion=alt['torsion'],locally_possible=bool(valid),already_excluded_by_s24=(row['id']in prior and alt['s']==24),local=local))
summary=dict(original_positive_alternatives=len(results),previously_excluded=sum(x['already_excluded_by_s24']for x in results),locally_possible=sum(x['locally_possible']for x in results),newly_excluded=sum(not x['locally_possible'] and not x['already_excluded_by_s24']for x in results),new_whole_defect_branches=0,new_quotient_exclusions=0)
assert summary==dict(original_positive_alternatives=34,previously_excluded=4,locally_possible=19,newly_excluded=11,new_whole_defect_branches=0,new_quotient_exclusions=0)
# Confirm every defect other than the already excluded two s24 branches retains an alternative.
for p in pairs:
 for defect in p['retained_second_defects']:
  if not defect:continue
  branches=[x for x in results if x['source_pair_index']==p['source_pair_index'] and x['s']==defect]
  assert any(x['locally_possible']for x in branches) or all(x['already_excluded_by_s24']for x in branches)
out=dict(scope='Exact local module surjection criterion and forced kernel fibers; no global realization claim.',source_hashes=PINNED,summary=summary,alternatives=results)
(ROOT/'two-one-positive-defect-local-module-criteria.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS:',summary)
