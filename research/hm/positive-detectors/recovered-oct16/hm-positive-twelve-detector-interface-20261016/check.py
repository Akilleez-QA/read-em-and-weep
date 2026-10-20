# Historical reproducibility source. Not executed during publication preparation.
"""Combine exact positive8/positive4 certificates; no new elimination or source values."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
P=Path(__file__).resolve().parent;R=P.parent;t=time.monotonic();checks=0
def test(x):
 global checks
 assert x;checks+=1
def read(folder,name):return json.loads((R/folder/name).read_text())
eight=read('hm-detector-plus-first-component-20261016','positive-eight-maps.json')
four=read('hm-plus-twist-minus1-quotient-20261016','certificate.json')
detectors=read('hm-plus-twist-minus1-quotient-20261016','detectors.json')
def decode(v):return {i:F(c) for i,c in v}
def add(a,b,c=1):
 r=dict(a)
 for k,v in b.items():r[k]=r.get(k,F(0))+c*v
 return {k:v for k,v in r.items() if v}
def apply(cols,v):
 r={}
 for i,c in v.items():r=add(r,cols[i],c)
 return r
A=list(map(decode,four['A_columns']));B=list(map(decode,four['B_columns']))
C=list(map(decode,four['cycles']));red=list(map(decode,four['coordinate_map_columns']))
for i,c in enumerate(C):test(not apply(B,c));test(apply(red,c)=={i:F(1)})
matrix=[]
for i,name in enumerate(eight['detector_order']):
 matched=[r for r in detectors if r['detector']==name]
 test(len(matched)==2)
 for d in matched:
  v=decode(d['positive_projected_cycle']);q=decode(d['coordinates']);lift=decode(d['boundary_lift'])
  test(not apply(B,v));test(apply(red,v)==q);test(add(apply(A,lift),apply(C,q))==v)
 test(decode(matched[0]['coordinates'])==decode(matched[1]['coordinates']))
 q=decode(matched[0]['coordinates']);row=eight['detector_matrix_4_by_8'][i]+[int(q.get(j,0)) for j in range(4)]
 test(all(q.get(j,F(0)).denominator==1 for j in range(4)));matrix.append(row)
expected=[[0,0,0,0,0,0,2,0,0,-2,0,0],[0,0,0,0,0,0,0,2,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0,0,-2]]
test(matrix==expected)
test([[r[j] for j in [6,7,2,3]] for r in matrix]==[[2*int(i==j) for j in range(4)] for i in range(4)])

# Twelve global dual-cycle representatives in the original homogeneous End basis.
cycles=[]
for i,cy in enumerate(eight['positive_basis_ambient80']):
 terms=[{'basis_key':entry[:4]+[0]*5,'coefficient':str(entry[4])} for entry in cy]
 cycles.append({'coordinate':'z'+str(i),'primal_twist':-3,'dual_twist':-2,'terms':terms})
for i,c in enumerate(C):
 full={}
 for j,z in c.items():
  orb=four['positive_orbits'][1][j];rep=orb['representative'];partner=orb['partner'];sg=orb['sign']
  full[rep]=full.get(rep,F(0))+z
  if partner!=rep:full[partner]=full.get(partner,F(0))+sg*z
 terms=[{'basis_key':four['full_bases'][1][j],'coefficient':str(z)} for j,z in sorted(full.items()) if z]
 cycles.append({'coordinate':'w'+str(i),'primal_twist':-4,'dual_twist':-1,'terms':terms})
for c in cycles:
 for term in c['terms']:
  u,v,a,b,*m=term['basis_key'];test(v-u==2);test(sum(m)==c['dual_twist']+2)

# Four detector coordinates plus eight transparent complementary coordinates form an exact chart.
complement=[0,1,4,5,8,9,10,11]
for i in range(12):
 x=[F(int(i==j)) for j in range(12)]
 d=[sum(F(a)*b for a,b in zip(r,x)) for r in matrix]
 reconstructed=[F(0)]*12
 for j in complement:reconstructed[j]=x[j]
 reconstructed[2]=d[2]/2;reconstructed[3]=d[3]/2+x[11]
 reconstructed[6]=d[0]/2+x[9];reconstructed[7]=d[1]/2
 test(reconstructed==x)
paths=[R/'hm-detector-plus-first-component-20261016/positive-eight-maps.json',R/'hm-plus-twist-minus1-quotient-20261016/certificate.json',R/'hm-plus-twist-minus1-quotient-20261016/detectors.json',R/'hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json']
out={'scope':'Exact invariant target/detector coordinate interface; actual coordinate values remain unacquired','coordinate_order':['z'+str(i) for i in range(8)]+['w'+str(i) for i in range(4)],'coordinate_definition':'Each primal coordinate is the canonical Serre pairing with its listed global dual-cycle representative, after the specified epsilon generator splitting.','detector_order':['h','j','p','r'],'detector_matrix':matrix,'positive_dual_cycles':cycles,'rank_certificate':{'columns':[6,7,2,3],'minor_determinant':16},'complementary_coordinate_indices':complement,'input_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},'premises':['Authenticated epsilon global generator and detector bridge','Exact positive twist-minus2 quotient','Exact positive twist-minus1 quotient','Twist-minus5 has no positive cohomology','Class under evaluation is inversion invariant']}
(P/'interface.json').write_text(json.dumps(out,indent=2)+'\n')
rec={'status':'PASS','checks':checks,'seconds':time.monotonic()-t,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_values':False,'new_rank_solve':False,'coordinates':12,'detector_rank':4,'review_status':'Component certificates independently reviewed; integration products checked here'}
(P/'receipt.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec,indent=2))
