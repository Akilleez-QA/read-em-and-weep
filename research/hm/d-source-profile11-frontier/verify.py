"""Filter a fixed authenticated historical list; never generate candidates."""
from pathlib import Path
import json, hashlib
from collections import Counter
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok: raise RuntimeError(msg)
def clean(x):return dict(sorted((r,n) for r,n in x.items() if n))
def sub(a,b):
 z=Counter(a);z.subtract(b);return z
def negative(x):return {r:n for r,n in sorted(x.items()) if n<0}
def h1(blocks,u):
 z=Counter()
 for e,r in blocks:z.update(c.product(r,-e-u-2))
 return z
def chi(blocks,u):return sub(c.h0(blocks,u),h1(blocks,u))
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['file']).read_bytes()
 require(len(b)==item['bytes'],item['file']+' bytes')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],item['file']+' sha256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob_sha1'],item['file']+' git blob')
E=[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']]
source_tuple=[1,1,1,0,0,1,0,0]
require(sum(c.DIM[r] for e,r in E)==17,'source rank')
require(sum(e*c.DIM[r] for e,r in E)==-54,'source degree')
require(clean(chi(E,4))=={'D':2,'P':3,'V':3},'source Euler')
for r in c.NAMES:
 for n in range(41):
  require(sum(c.DIM[s]*m for s,m in c.product(r,n).items())==c.DIM[r]*(n+1),'product dimension')
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text())
require(len(rows)==159,'fixed historical size')
def shape(A):return tuple(sorted(map(tuple,A)))
known={shape([[-8,'one'],[4,'one'],[6,'one']]):'1135',shape([[-8,'one'],[5,'W']]):'1135',shape([[-8,'one'],[4,'one'],[8,'one']]):'1142',shape([[-8,'one'],[4,'one'],[10,'one']]):'1142',shape([[-8,'one'],[2,'one'],[16,'one']]):'1145'}
out=[]
for i,x in enumerate(rows):
 A,B=x['A'],x['B'];w=[]
 for u in range(-10,11):
  for label,lhs,rhs in [('H1(E(u))-H1(A(u))',h1(E,u),h1(A,u)),('H1(E(-u))-H0(B(u))',h1(E,-u),c.h0(B,u))]:
   n=negative(sub(lhs,rhs))
   if n:w.append({'condition':label,'twist':u,'negative_multiplicities':n})
 compatible=not w
 require(compatible==(source_tuple in x['compatible_E_types']),'independent compatibility agrees '+str(i))
 require(sum(c.DIM[r] for e,r in A)==sum(c.DIM[r] for e,r in B)==3,'ranks')
 require(sum(e*c.DIM[r] for e,r in A)==x['a'],'A degree')
 require(sum(e*c.DIM[r] for e,r in B)==x['b'],'B degree')
 require(-6-x['a']-x['b']==x['defect'],'defect')
 cubic=sub(c.h0(A,3),Counter(Wp=1,T=2))
 lam=sorted([e for e,r in B for _ in range(c.DIM[r])],reverse=True)
 caps=[h*lam[0]-h*(h+1)+(10-h)*lam[1]-(10-h)*(11-h) for h in range(5,11)]
 degree=-54-x['b'];prior=known.get(shape(A))
 stage=('incompatible_D' if not compatible else 'cubic_1140' if negative(cubic) else 'dual_capacity' if degree>max(caps) else 'shape_'+prior if prior else 'remaining')
 out.append(dict(index=i,A=A,B=B,a=x['a'],b=x['b'],defect=x['defect'],D_compatible=compatible,source_failures=w,cubic_character=clean(cubic),cubic_negative=negative(cubic),B_ordinary_degrees=lam,dual_kernel_degree=degree,capacities=caps,capacity_max=max(caps),capacity_optimizers=[[h,10-h] for h in range(5,11) if caps[h-5]==max(caps)],capacity_excess=degree-max(caps),known_shape_exclusion=prior,partition=stage))
summary={s:[r['index'] for r in out if r['partition']==s] for s in ['incompatible_D','cubic_1140','dual_capacity','shape_1135','shape_1142','shape_1145','remaining']}
require(sum(map(len,summary.values()))==159,'complete disjoint partition')
require([len(summary[s]) for s in summary]==[57,32,62,2,2,1,3],'partition sizes')
require(summary['shape_1135']==[94,95],'1135 residual rows')
require(summary['shape_1142']==[100,106],'1142 residual rows')
require(summary['shape_1145']==[127],'1145 residual row')
require(summary['remaining']==[32,50,52],'exact residual rows')
expected={32:([[-8,'one'],[2,'one'],[4,'one']],[[-18,'one'],[-4,'one'],[6,'one']],12),50:([[-8,'one'],[2,'one'],[4,'one']],[[-6,'one'],[-4,'one'],[6,'one']],0),52:([[3,'W'],[-8,'one']],[[-5,'W'],[6,'one']],0)}
for i,(A,B,d) in expected.items():
 require(shape(rows[i]['A'])==shape(A) and shape(rows[i]['B'])==shape(B) and rows[i]['defect']==d,'residual identity '+str(i))
print(json.dumps(dict(scope='Necessary D-source maximal-profile(1,1) frontier only; no realization or full profile closure.',source=E,source_tuple=source_tuple,checks=checks,character_module_controls=c.checks,summary=summary,records=out),indent=2,sort_keys=True))
