# Historical reproducibility source. Not executed during publication preparation.
"""Exact 30-coordinate graph quotient and four detector plus projections only."""
import json,hashlib,time,resource
from pathlib import Path
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
HERE=Path(__file__).resolve().parent;P=HERE.parent;start=time.monotonic();checks=0
def test(x):
 global checks
 assert x;checks+=1
def plus(a,b):
 out=dict(a)
 for k,c in b.items():out[k]=out.get(k,0)+c
 return {k:c for k,c in out.items() if c}
def scale(a,c):return {k:c*v for k,v in a.items() if c*v}
def I(a):return {(k//5)*5+4-k%5:-v for k,v in a.items()}
def quotient(a):
 out={}
 for k,c in a.items():
  target=k;sign=1
  if 20<=k<25:target=k-10;sign=-1
  if 25<=k<30:target=k-25;sign=-1
  out[target]=out.get(target,0)+sign*c
 return {k:c for k,c in out.items() if c}
gamma={}
modelpath=P/'hm-factored-coefficient-action-20261014/pinned-model-input.json'
model=json.loads(modelpath.read_text())
for b,row in enumerate(model['gamma']):
 for a,terms in enumerate(row):
  for ex,c in terms:
   ee=tuple(map(int,ex.split(',')));test(sum(ee)<=1)
   k=0 if sum(ee)==0 else ee.index(1)+1
   gamma[b,a,k]=gamma.get((b,a,k),0)+c
def graph(h):
 E={(1,3,r//15,r%15):c for r,c in h.items()}
 for a in range(5):
  for k in range(5):
   for c in range(2):
    z=sum(h.get(15*c+b,0)*gamma.get((b,a,k),0) for b in range(15))
    if z:E[0,2,5*c+k,a]=z
 return E
def residual(E):
 return {(c,a,k):E.get((0,2,5*c+k,a),0)-sum(E.get((1,3,c,b),0)*gamma.get((b,a,k),0) for b in range(15)) for c in range(2) for a in range(5) for k in range(5)}
for r in range(30):test(not any(residual(graph({r:1})).values()))

# Published d5 columns in the free-variable K basis. Their graph lifts are fixed by gamma.
B=[{a:1,25+a:1} if b==0 else {10+a:1,20+a:1} for a in range(5) for b in range(2)]
for j,b in enumerate(B):
 test(not quotient(b));test(not any(residual(graph(b)).values()))
 test(I(b)==scale(B[2*(4-j//2)+j%2],-1))
for k in range(30):
 a={k:1};test(quotient(I(a))==I(quotient(a)));test(I(I(a))==a)
 # Exact quotient splitting certificate: a - inclusion(quotient(a)) is one known column or0.
 remainder=plus(a,scale(quotient(a),-1))
 test(not remainder or remainder in B)
free=sorted(set(range(30))-set.union(*(set(b) for b in B)))
test(free==list(range(5,10))+list(range(15,20)))

bridgepath=P/'hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json'
records=json.loads(bridgepath.read_text())['records'];result=[]
for name,pivot in [('h',15),('j',16),('p',5),('r',6)]:
 raw=next(r for r in records if r['detector']==name and r['dual_twist']==-2 and not r['transported'])
 E={tuple(z['basis_key'][:4]):z['coefficient'] for z in raw['terms']}
 test(all(not any(z['basis_key'][4:]) for z in raw['terms']))
 h={15*a+b:c for (u,v,a,b),c in E.items() if (u,v)==(1,3)}
 test(h=={pivot:4});test(E==graph(h))
 transformed=next(r for r in records if r['detector']==name and r['dual_twist']==-2 and r['transported'])
 Ep={tuple(z['basis_key'][:4]):z['coefficient'] for z in transformed['terms']}
 test(Ep==graph(I(h)))
 hp=scale(plus(h,I(h)),Fraction(1,2));test(all(c.denominator==1 for c in hp.values()));hp={k:int(c) for k,c in hp.items()}
 test(quotient(hp)==hp);test(I(hp)==hp)
 result.append({'detector':name,'K30':h,'inversion_K30':I(h),'plus_quotient20':hp})
minor=[[r['plus_quotient20'].get(k,0) for r in result] for k in [15,16,5,6]]
test(minor==[[2*int(i==j) for j in range(4)] for i in range(4)])
test(all(all(k not in b for k in [15,16,5,6]) for b in B))
# Entire quotient involution is four -J5 blocks; no large-matrix computation.
trace=sum(I({k:1}).get(k,0) for k in range(20));test(trace==-4)

# Explicit positive quotient basis, projection and its Serre-dual coordinate functionals.
P8=[{5*b+s:1,5*b+4-s:-1} for b in range(4) for s in range(2)]
def positive_coordinates(h):
 q=quotient(h)
 return [Fraction(q.get(5*b+s,0)-q.get(5*b+4-s,0),2) for b in range(4) for s in range(2)]
def section(c):
 out={}
 for a,p in zip(c,P8):out=plus(out,scale(p,a))
 return out
for i,p in enumerate(P8):
 test(I(p)==p);test(quotient(p)==p)
 test(positive_coordinates(p)==[int(i==j) for j in range(8)])
 test(graph(p)==graph(I(p)))
for k in range(30):
 h={k:1};c=positive_coordinates(h)
 test(section(c)==quotient(scale(plus(h,I(h)),Fraction(1,2))))
 test(positive_coordinates(h)==positive_coordinates(I(h)))
for b in B:test(positive_coordinates(b)==[0]*8)
dual_rows=[]
for i in range(8):
 rr={k:positive_coordinates({k:1})[i] for k in range(30)}
 dual_rows.append({k:c for k,c in rr.items() if c})
positive_detector_rows=[]
for r in result:
 c=positive_coordinates(r['K30']);test(all(z.denominator==1 for z in c))
 positive_detector_rows.append([int(z) for z in c])
test(positive_detector_rows==[[0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,2],[0,0,2,0,0,0,0,0],[0,0,0,2,0,0,0,0]])
maps={'scope':'Exact positive twist-minus2 quotient and dual linear coordinates; primal cochain lifts are not supplied','basis_order':[[b,s] for b in range(4) for s in range(2)],'K30_order':'15*c+b for E13[c,b]','positive_basis_K30':P8,'positive_basis_ambient80':[[[*k,c] for k,c in sorted(graph(p).items())] for p in P8],'reduction_dual_rows':[[[k,c.numerator,c.denominator] for k,c in row.items()] for row in dual_rows],'quotient20_reduction':[[[k,int(quotient({k:1}).get(i,0))] for k in range(30) if quotient({k:1}).get(i,0)] for i in range(20)],'detector_order':['h','j','p','r'],'detector_matrix_4_by_8':positive_detector_rows,'duality':'Rows reduction_dual_rows annihilate d5 and minus eigenspace and pair delta with the8positive basis cycles. Serre duality identifies them with the primal twist-minus3 plus basis.'}
(HERE/'positive-eight-maps.json').write_text(json.dumps(maps,indent=2)+'\n')
out={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_values':False,'rank_rerun':False,'K30_graph_formula':'E02[5*c+k,a]=sum_b E13[c,b]*gamma[b,a,k]','K30_order':'r=15*c+b for E13[c,b]','d5_columns':B,'quotient_retained_rows':list(range(20)),'quotient_relations':{'20..24':'e_(20+a)=-e_(10+a)','25..29':'e_(25+a)=-e_a'},'detectors':result,'minor_rows':[15,16,5,6],'minor':minor,'minor_determinant':16,'plus_column_rank':4,'twist_minus2_quotient_dimension':20,'involution_trace':trace,'eigenspaces':{'+':8,'-':12},'input_sha256':{str(p.relative_to(P)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [bridgepath,modelpath,P/'hm-seed-gauge-scope-independent-20261016/PR76-NOTE.md']}}
(HERE/'receipt.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['d5_columns','input_sha256','detectors']},indent=2))
