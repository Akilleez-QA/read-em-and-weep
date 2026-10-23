"""Fixed historical P-source filter and dual endpoint-capacity certificate."""
from pathlib import Path
from collections import Counter
import json,hashlib
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
def sub(a,b):
 v=Counter(a);v.subtract(b);return v
def clean(v):return {r:n for r,n in sorted(v.items()) if n}
def neg(v):return {r:n for r,n in sorted(v.items()) if n<0}
def h1(blocks,u):
 z=Counter()
 for e,r in blocks:z.update(c.product(r,-e-u-2))
 return z
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],'bytes '+x['file'])
 require(hashlib.sha256(b).hexdigest()==x['sha256'],'sha256 '+x['file'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'blob '+x['file'])
E=[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']]
tupleP=[1,1,1,0,1,0,0,0]
require(sum(c.DIM[r] for e,r in E)==17,'rank E')
require(sum(e*c.DIM[r] for e,r in E)==-54,'degree E')
for r in c.NAMES:
 for n in range(41):require(sum(c.DIM[s]*v for s,v in c.product(r,n).items())==c.DIM[r]*(n+1),'character dimension')
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text())
require(len(rows)==159,'frozen length')
groups={'cubic1140':[],'doublet1156':[],'flag1159':[],'dual_capacity':[]}
compatible=[];records=[];rejected=[]
shape=lambda x:tuple(sorted(map(tuple,x)))
six={shape([[-1,'Wp'],[4,'one']]),shape([[-1,'Wp'],[10,'one']])}
two={shape([[-3,'Wp'],[16,'one']]),shape([[-5,'Wp'],[16,'one']])}
for i,x in enumerate(rows):
 A,B=x['A'],x['B'];fail=[]
 for u in range(-10,11):
  for label,v in [('H1E-H1A',sub(h1(E,u),h1(A,u))),('H1Edual-H0B',sub(h1(E,-u),c.h0(B,u)))]:
   if neg(v):fail.append({'twist':u,'condition':label,'negative':neg(v)})
 require((not fail)==(tupleP in x['compatible_E_types']),'original tuple '+str(i))
 if fail:rejected.append({'index':i,'witnesses':fail});continue
 compatible.append(i)
 require(sum(c.DIM[r] for e,r in A)==sum(c.DIM[r] for e,r in B)==3,'rank quotients')
 require(sum(e*c.DIM[r] for e,r in B)==x['b'],'degree B')
 require(sum(e*c.DIM[r] for e,r in A)==x['a'],'degree A')
 witness=neg(sub(c.h0(A,3),Counter(Wp=1,T=2)))
 rec={'index':i,'A':A,'B':B,'a':x['a'],'b':x['b'],'defect':x['defect']}
 if witness:group='cubic1140';rec['negative_cubic_multiplicities']=witness
 elif shape(A) in six:group='doublet1156'
 elif shape(A) in two:group='flag1159'
 else:
  group='dual_capacity'
  lam=sorted([e for e,r in B for _ in range(c.DIM[r])],reverse=True)
  require(lam[0]<=-1,'negative B')
  vals=[h*lam[0]-h*(h+1)+(10-h)*lam[1]-(10-h)*(11-h) for h in range(5,11)]
  # Independently sum the quotient-rank form of the same six bounds.
  for h,v in zip(range(5,11),vals):
   q=[int(j<=h)+int(j<=10-h) for j in range(1,h+1)]
   require(sum(q)==10 and all(1<=k<=2 for k in q),'rank partition')
   require(sum(sum(lam[:k])-2*j*k for j,k in enumerate(q,1))==v,'quotient vs height formula')
  capacity=max(vals);degree=-54-x['b']
  require(capacity<=-70,'uniform capacity')
  require(degree>capacity,'degree contradiction')
  rec.update(ordinary_B_degrees=lam,degree_L=degree,capacities_for_h1_5_through_10=vals,capacity=capacity,maximizing_heights=[[h,10-h] for h,v in zip(range(5,11),vals) if v==capacity],contradiction_gap=degree-capacity)
 groups[group].append(i);rec['exclusion']=group;records.append(rec)
expected={'cubic1140':[42,43,53,62,63,64,65,66,67,73,74,76,102,103,110,111],'doublet1156':[86,87,88,89,96,116],'flag1159':[109,134],'dual_capacity':[130,132,141,142,143,144,145,148,149,150,151]}
require(groups==expected,'exact partition')
flat=[i for g in groups.values() for i in g]
require(len(flat)==len(set(flat))==35,'disjoint35')
require(sorted(flat)==compatible,'exhaust compatible')
require(len(rejected)==124,'non-P count')
require(max(h*(-1)-h*(h+1)+(10-h)*(-1)-(10-h)*(11-h) for h in range(5,11))==-70,'uniform bound exact')
print(json.dumps({'scope':'No actual P-source maximal profile(1,1), conditional on pinned geometric necessity theorem and exclusion inputs; not global profile closure.','checks':checks,'character_module_controls':c.checks,'historical_records':159,'P_compatible_indices':compatible,'partition':groups,'records':records,'non_P_compatibility_witnesses':rejected},indent=2,sort_keys=True))
