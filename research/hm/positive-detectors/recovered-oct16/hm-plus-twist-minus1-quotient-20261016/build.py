# Historical reproducibility source. Not executed during publication preparation.
import json,subprocess,time,resource,hashlib
from pathlib import Path
from fractions import Fraction as F
P=Path(__file__).parent; start=time.monotonic()
source=P.parent/'hm-epsilon-projective-generator-bridge-20261016/pinned/check_hm_p4_all_twists.js'
# Literal Python translation of the inspected pinned polynomial generator.
ranks=[5,15,10,2]
def wp(i):return ((i+2)%5,(i+3)%5)
def wm(i):return ((i+1)%5,(i+4)%5)
def eps(a):
 if len(set(a))<5:return 0
 return (-1)**sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))
d=[[[] for _ in range(ranks[l])] for l in range(3)]
for a in range(5):
 for r in range(15):
  for k in range(5):
   v=eps([k,*(wp(a) if r<5 or r>=10 else wm(a)),*(wp(r) if r<5 else wm(r-5) if r<10 else wm(r-10))])
   if v:d[0][a].append((r,k,v))
def form(c,h,pq):
 p,q=pq;d[1][c].extend([(5*h+q,p,1),(5*h+p,q,-1)])
for i in range(5):
 form(i,0,wp(i));form(i+5,1,wm(i));form(i+10,0,wm(i));form(i+10,1,wp(i))
for b in range(2):
 for k in range(5):d[2][b*5+k].append((b,k,1))
# Authenticate every homogeneous linear slot against the pinned literal model.
modelpath=P.parent/'hm-factored-coefficient-action-20261014/pinned-model-input.json'
model=json.loads(modelpath.read_text())
for l,name in enumerate(('gamma','delta','ev')):
 for col in range(ranks[l]):
  actual={}
  for row,k,z in d[l][col]:actual[row,k]=actual.get((row,k),0)+z
  actual={k:v for k,v in actual.items() if v}
  expected={}
  for row in range(ranks[l+1]):
   for ex,z in model[name][row][col]:
    m=tuple(map(int,ex.split(',')));assert sum(m)<=1
    k=0 if sum(m)==0 else m.index(1)+1
    expected[row,k]=expected.get((row,k),0)+z
  assert actual==expected,(name,col,actual,expected)
incoming=[[[] for _ in range(ranks[l+1])] for l in range(3)]
for l in range(3):
 for c,ts in enumerate(d[l]):
  for r,k,z in ts:incoming[l][r].append((c,k,z))
def mon(n,k=5):
 if n<0:return []
 if k==1:return [(n,)]
 return [(a,*t) for a in range(n+1) for t in mon(n-a,k-1)]
def basis(r):return [[u,u+r,a,b,*m] for u in range(4) if u+r<4 for a in range(ranks[u+r]) for b in range(ranks[u]) for m in mon(r-1)]
data=[]
for r in (1,2,3):
 src=basis(r);rows=None
 if r<3:
  dst=basis(r+1);idx={tuple(k):i for i,k in enumerate(dst)};rows=[{} for _ in dst]
  for col,key in enumerate(src):
   u,v,a,b,*m=key
   def emit(uu,vv,aa,bb,k,z):
    mm=m.copy();mm[k]+=1;row=rows[idx[(uu,vv,aa,bb,*mm)]]
    row[col]=row.get(col,0)+z
    if not row[col]:del row[col]
   if v<3:
    for c,k,z in d[v][a]:emit(u,v+1,c,b,k,z)
   if u>0:
    for c,k,z in incoming[u-1][b]:emit(u-1,v,a,c,k,z*(-1 if r%2==0 else 1))
  rows=[list(x.items()) for x in rows]
 data.append({'basis':src,'matrix':rows})
collections=[]; peak=0
def guard():
 global peak
 n=sum(sum(len(r) for r in a) for a in collections);peak=max(peak,n)
 if n>100000:raise RuntimeError('LIVE_ENTRY_CAP')
 if time.monotonic()-start>28:raise RuntimeError('TIME_CAP')
def add(a,b,c):
 for i,v in b.items():
  z=a.get(i,F(0))+c*v
  if z:a[i]=z
  else:a.pop(i,None)
def rev(k):
 u,v,a,b,*m=k
 def ix(l,i):return i if l==3 else 5*(i//5)+4-i%5
 sign=[-1,-1,1,1][u]*[-1,-1,1,1][v]
 return [u,v,ix(v,a),ix(u,b),*m[::-1]],sign
orbits=[]; inclusions=[]; selectors=[]
for D in data:
 basis=D['basis']; idx={tuple(k):i for i,k in enumerate(basis)}; seen=set(); inc=[]; sel={}; orb=[]
 for i,k in enumerate(basis):
  if i in seen:continue
  kr,sgn=rev(k);j=idx[tuple(kr)];seen|={i,j}
  if i==j and sgn==-1:continue
  v={i:F(1)}
  if j!=i:v[j]=F(sgn)
  sel[i]=len(inc);inc.append(v);orb.append({'representative':i,'partner':j,'sign':sgn})
 inclusions.append(inc);selectors.append(sel);orbits.append(orb)
assert list(map(len,inclusions))==[123,196,72]
cols=[]
for l in range(2):
 rows=[dict(r) for r in data[l]['matrix']]; fullcols=[{} for _ in data[l]['basis']]
 for i,r in enumerate(rows):
  for j,v in r.items():fullcols[j][i]=F(v)
 out=[]
 for v in inclusions[l]:
  w={}
  for j,c in v.items():add(w,fullcols[j],c)
  small={selectors[l+1][i]:c for i,c in w.items() if i in selectors[l+1]}
  back={}
  for j,c in small.items():add(back,inclusions[l+1][j],c)
  assert back==w
  out.append(small)
 cols.append(out)
A,B=cols;collections.extend([A,B]);guard()
def apply(cols,v):
 out={}
 for i,c in v.items():add(out,cols[i],c)
 return out
assert all(not apply(B,c) for c in A)
# RREF of B: 72 rows, 196 columns. Kernel is formed before quotient elimination.
rows=[{} for _ in range(72)]
for j,c in enumerate(B):
 for i,v in c.items():rows[i][j]=v
collections.append(rows);piv=[];rr=0
for j in range(196):
 p=next((i for i in range(rr,72) if rows[i].get(j)),None)
 if p is None:continue
 rows[p],rows[rr]=rows[rr],rows[p];q=rows[rr][j];rows[rr]={k:v/q for k,v in rows[rr].items()}
 for i in range(72):
  if i!=rr and rows[i].get(j):add(rows[i],rows[rr],-rows[i][j])
 piv.append(j);rr+=1;guard()
assert rr==72
K=[]
for j in range(196):
 if j in piv:continue
 v={j:F(1)}
 for i,p in enumerate(piv):
  if rows[i].get(j):v[p]=-rows[i][j]
 assert not apply(B,v);K.append(v)
collections.append(K);guard()
# Incremental normalized basis, each vector carries its lift in original A columns
# and four quotient representatives. Equal value provenance is never used here.
V=[];L=[];Q=[];piv2=[];cycles=[]
collections.extend([V,L,Q,cycles])
def reduce(v):
 w=dict(v);l={};q={}
 for p,b,bl,bq in zip(piv2,V,L,Q):
  c=w.get(p)
  if c:add(w,b,-c);add(l,bl,c);add(q,bq,c)
 return w,l,q
for j,c in enumerate(A):
 w,l,q=reduce(c)
 if not w:continue
 p=min(w);z=w[p]; lift={j:F(1)};add(lift,l,-1)
 piv2.append(p);V.append({i:v/z for i,v in w.items()});L.append({i:v/z for i,v in lift.items()});Q.append({});guard()
assert len(V)==120
for k in K:
 w,l,q=reduce(k)
 if not w:continue
 n=len(cycles);cycles.append(dict(k));p=min(w);z=w[p]
 lift={i:-v/z for i,v in l.items()};qc={n:1/z}
 for i,v in q.items():qc[i]=qc.get(i,0)-v/z
 piv2.append(p);V.append({i:v/z for i,v in w.items()});L.append(lift);Q.append(qc);guard()
assert len(cycles)==4 and len(V)==124
# Check every tracked identity exactly against the original projected maps.
for v,l,q in zip(V,L,Q):
 w=apply(A,l);add(w,apply(cycles,q),1);assert w==v
# Complete ambient reduction maps. Identity is asserted on all 124 kernel generators.
red=[];lifts=[]
for j in range(196):
 w,l,q=reduce({j:F(1)});red.append(q);lifts.append(l)
collections.extend([red,lifts]);guard()
for k in K:
 q=apply(red,k);l=apply(lifts,k);w=apply(A,l);add(w,apply(cycles,q),1);assert w==k
for i,c in enumerate(cycles):assert apply(red,c)=={i:F(1)}
assert all(not apply(red,a) for a in A)
def enc(v):return [[i,str(x)] for i,x in sorted(v.items())]
detectors=[]
records=json.loads((P.parent/'hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json').read_text())['records']
idx={tuple(k):i for i,k in enumerate(data[1]['basis'])}
for rec in records:
 if rec['dual_twist']!=-1:continue
 full={}
 for term in rec['terms']:
  key=term['basis_key'];assert data[1]['basis'][term['index']]==key
  j=term['index'];c=F(term['coefficient'],2)
  full[j]=full.get(j,0)+c
  key2,sgn=rev(key);jj=idx[tuple(key2)];full[jj]=full.get(jj,0)+sgn*c
 full={i:v for i,v in full.items() if v}
 small={selectors[1][i]:c for i,c in full.items() if i in selectors[1]}
 assert not apply(B,small)
 coord=apply(red,small);lift=apply(lifts,small)
 back=apply(A,lift);add(back,apply(cycles,coord),1);assert back==small
 detectors.append({'detector':rec['detector'],'transported':rec['transported'],'positive_projected_cycle':enc(small),'coordinates':enc(coord),'boundary_lift':enc(lift)})
(P/'detectors.json').write_text(json.dumps(detectors,indent=2)+'\n')
out={'twist':-1,'basis_order':'pinned u,v,target-row,source-column,ascending monomial exponent lexicographic','positive_basis':'representative e_i + sign e_partner; fixed positive e_i','full_bases':[d['basis'] for d in data],'positive_orbits':orbits,'A_columns':list(map(enc,A)),'B_columns':list(map(enc,B)),'cycles':list(map(enc,cycles)),'coordinate_map_columns':list(map(enc,red)),'boundary_lift_map_columns':list(map(enc,lifts)),'kernel_basis':list(map(enc,K)),'image_basis':list(map(enc,V[:120])),'image_lifts':list(map(enc,L[:120]))}
(P/'certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
receipt={'status':'PASS','dimensions':[123,196,72],'ranks':[120,72],'cohomology':[3,4,0],'quotient_cycles':4,'checks':'full signed reversal inclusion; BA=0; Bcycles=0; image lift identities; identity=Alift+cycle*coordinate on kernel basis; coordinate(cycles)=I; coordinate(A)=0','max_live_rational_entries':peak,'seconds':time.monotonic()-start,'maxrss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'generator_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Exact positive twist−1 symbolic quotient only; no source values.'}
(P/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
