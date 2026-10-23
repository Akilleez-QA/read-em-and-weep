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
E=[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']]
source_tuple=[1,1,1,0,1,0,0,0]
require(sum(c.DIM[r] for e,r in E)==17,'source rank')
require(sum(e*c.DIM[r] for e,r in E)==-54,'source degree')
require(clean(chi(E,4))=={'D':2,'P':3,'V':3},'source Euler')
# Dimension/recurrence controls over every product used by this packet.
for r in c.NAMES:
 for n in range(41):
  require(sum(c.DIM[s]*m for s,m in c.product(r,n).items())==c.DIM[r]*(n+1),'product dimension')
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text())
require(len(rows)==159,'fixed historical size')
out=[]
old1142_shapes={((-8,'one'),(4,'one'),(8,'one')),((-8,'one'),(4,'one'),(10,'one'))}
for i,x in enumerate(rows):
 A,B=x['A'],x['B'];w=[]
 for u in range(-10,11):
  for label,lhs,rhs in [('H1(E(u))-H1(A(u))',h1(E,u),h1(A,u)),('H1(E(-u))-H0(B(u))',h1(E,-u),c.h0(B,u))]:
   n=negative(sub(lhs,rhs))
   if n:w.append({'condition':label,'twist':u,'negative_multiplicities':n})
 compatible=not w
 require(compatible==(source_tuple in x['compatible_E_types']),'frozen source compatibility '+str(i))
 h=sum(c.product(r,e+1)['Wp'] for e,r in A)
 env=c.h0(A,2);env.update(chi(A,4));env.subtract(chi(E,4))
 cubic=sub(c.h0(A,3),Counter(Wp=1,T=2))
 old1140=bool(negative(cubic));old1142=tuple(sorted(map(tuple,A))) in old1142_shapes
 newtest=(h==0 and bool(negative(env)))
 out.append({'index':i,'A':A,'B':B,'a':x['a'],'b':x['b'],'defect':x['defect'],
 'P_degree_bound_failed':x['a']<0,'P_cohomology_compatible':compatible,'source_failures':w,
 'Euler_doublet_Hom_dimension':h,'quartic_character':clean(env),
 'quartic_negative_multiplicities':negative(env),'quartic_filter_applicable':h==0,
 'fails_1153_criterion':newtest,'old1140_cubic_negative_multiplicities':negative(cubic),
 'old1140_excluded':old1140,'old1142_shape_excluded':old1142,
 'retained_by_all_applied_filters':compatible and x['a']>=0 and not old1140 and not old1142 and not newtest})
def ids(test):return [r['index'] for r in out if test(r)]
summary={
 'fixed_historical_records':len(rows),
 'P_cohomology_compatible_indices':ids(lambda r:r['P_cohomology_compatible']),
 'P_compatible_degree_bound_excluded_indices':ids(lambda r:r['P_cohomology_compatible'] and r['P_degree_bound_failed']),
 'P_compatible_old1140_excluded_indices':ids(lambda r:r['P_cohomology_compatible'] and r['old1140_excluded']),
 'P_compatible_old1142_excluded_indices':ids(lambda r:r['P_cohomology_compatible'] and r['old1142_shape_excluded']),
 'P_compatible_Hom_zero_indices':ids(lambda r:r['P_cohomology_compatible'] and r['quartic_filter_applicable']),
 'P_compatible_1153_negative_indices':ids(lambda r:r['P_cohomology_compatible'] and r['fails_1153_criterion']),
 'additional_P_exclusions_beyond1140_1142':ids(lambda r:r['P_cohomology_compatible'] and r['fails_1153_criterion'] and not r['old1140_excluded'] and not r['old1142_shape_excluded']),
 'retained_forced_nonzero_cubic_kernel_indices':ids(lambda r:r['retained_by_all_applied_filters'] and bool(r['quartic_negative_multiplicities'])),
 'retained_indices':ids(lambda r:r['retained_by_all_applied_filters'])}
require(len(summary['P_cohomology_compatible_indices'])==35,'35 P-compatible')
require(summary['P_compatible_Hom_zero_indices']==[42,43,53,67,76,102,130,132],'eight Hom-zero')
require(summary['P_compatible_1153_negative_indices']==[42,43,53,67,76,102],'six overlap')
require(summary['P_compatible_degree_bound_excluded_indices']==[42,43,53],'degree cuts are old overlap')
require(summary['additional_P_exclusions_beyond1140_1142']==[],'no additional cut')
require(summary['P_compatible_old1142_excluded_indices']==[],'D-only prior shapes')
result={'scope':'Fixed original159 records, P-source-conditioned necessary tests only. No current live count or all-source exclusion.',
 'source':E,'source_tuple':source_tuple,'summary':summary,'checks':checks,'character_module_controls':c.checks,'records':out}
print(json.dumps(result,indent=2,sort_keys=True))
