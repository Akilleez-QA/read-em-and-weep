# Historical reproducibility source. Not executed during publication preparation.
import json,time,hashlib,resource
from pathlib import Path
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2);resource.setrlimit(resource.RLIMIT_CPU,(30,30))
P=Path(__file__).resolve().parent;R=P.parent;t=time.monotonic();checks=0
src=R/'hm-positive-twelve-detector-interface-20261016/interface.json';I=json.loads(src.read_text())
E=json.loads((R/'hm-detector-plus-first-component-20261016/positive-eight-maps.json').read_text());C=json.loads((R/'hm-plus-twist-minus1-quotient-20261016/certificate.json').read_text());D=json.loads((R/'hm-plus-twist-minus1-quotient-20261016/detectors.json').read_text())
for p,h in I['input_sha256'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h;checks+=1
assert I['coordinate_order']==['z'+str(j) for j in range(8)]+['w'+str(j) for j in range(4)];checks+=1
assert I['detector_order']==['h','j','p','r']==E['detector_order'];checks+=1
for j,cy in enumerate(I['positive_dual_cycles']):
 actual={tuple(x['basis_key']):F(x['coefficient']) for x in cy['terms']};expected={}
 if j<8:
  assert (cy['primal_twist'],cy['dual_twist'])==(-3,-2);checks+=1
  for row in E['positive_basis_ambient80'][j]:expected[tuple(row[:4]+[0]*5)]=F(row[4])
 else:
  assert (cy['primal_twist'],cy['dual_twist'])==(-4,-1);checks+=1
  for k,z in C['cycles'][j-8]:
   orb=C['positive_orbits'][1][k]
   for index,scale in [(orb['representative'],1)]+([] if orb['partner']==orb['representative'] else [(orb['partner'],orb['sign'])]):
    key=tuple(C['full_bases'][1][index]);expected[key]=expected.get(key,0)+scale*F(z)
 assert actual=={k:v for k,v in expected.items() if v};checks+=1
for j,name in enumerate(I['detector_order']):
 q=dict(D[[x['detector'] for x in D].index(name)]['coordinates'])
 assert I['detector_matrix'][j]==E['detector_matrix_4_by_8'][j]+[F(q.get(k,0)) for k in range(4)];checks+=1
M=list(map(lambda r:list(map(F,r)),I['detector_matrix']));comp=[0,1,4,5,8,9,10,11];assert I['complementary_coordinate_indices']==comp;checks+=1
# Explicit two-sided inverse, rather than a rank solve.
B=M+[[F(i==j) for j in range(12)] for i in comp]
def inverse(y):
 x=[F(0)]*12
 for j,k in enumerate(comp):x[k]=y[4+j]
 x[6]=y[0]/2+x[9];x[7]=y[1]/2;x[2]=y[2]/2;x[3]=y[3]/2+x[11]
 return x
def apply(x):return [sum(a*b for a,b in zip(r,x)) for r in B]
for j in range(12):
 e=[F(i==j) for i in range(12)]
 assert inverse(apply(e))==e;checks+=1
 assert apply(inverse(e))==e;checks+=1
assert [[M[i][j] for j in [6,7,2,3]] for i in range(4)]==[[2*F(i==j) for j in range(4)] for i in range(4)];checks+=1
out={'status':'PASS','checks':checks,'interface_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'seconds':time.monotonic()-t,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'new_elimination':False,'source_values':False}
(P/'receipt.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
