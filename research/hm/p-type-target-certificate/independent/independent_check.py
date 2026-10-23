from pathlib import Path
import json,hashlib,sys
# Independent exact class inner products, not production McKay recurrence.
exec((Path(__file__).parent/'base.py').read_text())
from functools import lru_cache
product=lru_cache(None)(product)
PACK=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
rows=json.loads((PACK/'inputs/profile11-pairs.json').read_text())
P=[1,1,1,0,1,0,0,0]
E=[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']]
def h1(B,t):
 out=Counter()
 for e,r in B:out.update(product(r,-e-t-2))
 return out
def ge(a,b):return all(a[r]>=b[r] for r in chars)
def clean(a):return {r:a[r] for r in chars if a[r]}
need(len(rows)==159)
need(chi(E,4)==Counter(V=3,P=3,D=2))
records=[]
author=json.loads((PACK/"RESULT.json").read_text())["records"]
for i,row in enumerate(rows,1):
 A,B=row['A'],row['B']
 need((row['a']<0)==author[i-1]['P_degree_bound_failed'])
 failures=[]
 for u in range(-10,11):
  for label,a,b in [('H1(E(u))-H1(A(u))',h1(E,u),h1(A,u)),('H1(E(-u))-H0(B(u))',h1(E,-u),h0(B,u))]:
   neg={r:a[r]-b[r] for r in chars if a[r]<b[r]}
   if neg:failures.append({'condition':label,'twist':u,'negative_multiplicities':neg})
 compatible=not failures
 need(failures==author[i-1]['source_failures'])
 need(compatible==(P in row['compatible_E_types']))
 
 hom=h0(A,1)['Wp']
 envelope=h0(A,2);envelope.update(chi(A,4));envelope.subtract(chi(E,4))
 old=not ge(h0(A,3),Counter(Wp=1,T=2))
 negative={r:n for r,n in envelope.items() if n<0}
 fail=hom==0 and bool(negative)
 need(hom==author[i-1]['Euler_doublet_Hom_dimension'])
 need(clean(envelope)==author[i-1]['quartic_character'])
 need(negative==author[i-1]['quartic_negative_multiplicities'])
 need(old==author[i-1]['old1140_excluded'])
 need(fail==author[i-1]['fails_1153_criterion'])
 need((tuple(sorted(map(tuple,A))) in {((-8,'one'),(4,'one'),(8,'one')),((-8,'one'),(4,'one'),(10,'one'))})==author[i-1]['old1142_shape_excluded'])
 if not compatible:continue
 records.append(dict(row=i,A=A,B=B,defect=row['defect'],hom=hom,envelope=clean(envelope),negative=negative,prior1140=old,rejected1153=fail))
summary=dict(total_P=len(records),hom_zero=sum(r['hom']==0 for r in records),rejected1153=[r['row'] for r in records if r['rejected1153']],rejected1153_after1140=[r['row'] for r in records if r['rejected1153'] and not r['prior1140']],prior1140=[r['row'] for r in records if r['prior1140']])
forced=[r['row']-1 for r in records if not r['prior1140'] and r['negative'] and not r['rejected1153']]
need(forced==[86,87,88,89,96,109,116,134])
need(all(r['hom']==1 and r['negative']=={'V':-1} for r in records if r['row']-1 in forced))
summary['forced_nonzero_cubic_zero_based_indices']=forced
need([i for i,r in enumerate(rows) if P in r['compatible_E_types'] and r['a']<0]==[42,43,53])
need(-3*2-4*12==-54 and -4*14==-56)
need(all(rows[r['row']-1]['a']>=2 for r in records if not r['prior1140'] and not r['rejected1153']))
print(json.dumps(dict(checks=checks,summary=summary,records=records),indent=2))
