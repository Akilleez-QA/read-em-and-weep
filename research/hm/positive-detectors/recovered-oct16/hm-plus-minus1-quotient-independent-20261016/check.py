# Historical reproducibility source. Not executed during publication preparation.
import json,time,resource,hashlib
from pathlib import Path
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2);resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t=time.monotonic();P=Path(__file__).resolve().parent;root=P.parent;D=root/'hm-plus-twist-minus1-quotient-20261016';C=json.loads((D/'certificate.json').read_text());checks=0
ranks=[5,15,10,2];sg=[-1,-1,1,1]
def dec(x):return {int(i):F(v) for i,v in x}
def add(out,v,c=1):
 for i,a in v.items():
  out[i]=out.get(i,0)+c*a
  if not out[i]:del out[i]
def app(cols,v):
 o={}
 for i,c in v.items():add(o,cols[i],c)
 return o
M=json.loads((root/'hm-factored-coefficient-action-20261014/pinned-model-input.json').read_text())
d=[]
for name,n in zip(['gamma','delta','ev'],ranks):
 cols=[[] for _ in range(n)]
 for i,row in enumerate(M[name]):
  for j,terms in enumerate(row):
   for ex,c in terms:
    e=tuple(map(int,ex.split(',')));assert sum(e) in (0,1)
    k=0 if sum(e)==0 else e.index(1)+1
    cols[j].append((i,k,c))
 d.append(cols)
def mons(n,k=5):
 if k==1:return [(n,)]
 return [(a,*z) for a in range(n+1) for z in mons(n-a,k-1)]
def rev(key):
 u,v,a,b,*e=key
 ix=lambda l,i:i if l==3 else 5*(i//5)+4-i%5
 return (u,v,ix(v,a),ix(u,b),*e[::-1]),sg[u]*sg[v]
bases=[];inc=[]
for r in (1,2,3):
 basis=[(u,u+r,a,b,*e) for u in range(4-r) for a in range(ranks[u+r]) for b in range(ranks[u]) for e in mons(r-1)]
 assert [list(x) for x in basis]==C['full_bases'][r-1];checks+=1;bases.append(basis)
 idx={x:i for i,x in enumerate(basis)};visited=set();orbits=[];I=[]
 for i,key in enumerate(basis):
  if i in visited:continue
  key2,s=rev(key);j=idx[key2];visited.update([i,j])
  if i==j and s<0:continue
  v={i:F(1)}
  if i!=j:v[j]=F(s)
  I.append(v);orbits.append(dict(representative=i,partner=j,sign=s))
 assert orbits==C['positive_orbits'][r-1];checks+=1;inc.append(I)
assert list(map(len,inc))==[123,196,72];checks+=1
projected=[]
for r in (1,2):
 dstidx={x:i for i,x in enumerate(bases[r])};full=[]
 for u,v,a,b,*e in bases[r-1]:
  col={}
  def emit(uu,vv,aa,bb,k,c):
   ee=e.copy();ee[k]+=1;add(col,{dstidx[(uu,vv,aa,bb,*ee)]:c})
  if v<3:
   for aa,k,c in d[v][a]:emit(u,v+1,aa,b,k,c)
  if u>0:
   for bb,terms in enumerate(d[u-1]):
    for rr,k,c in terms:
     if rr==b:emit(u-1,v,a,bb,k,c*(1 if r%2 else -1))
  full.append(col)
 cols=[]
 for v in inc[r-1]:
  y=app(full,v);small={j:y[min(vec)] for j,vec in enumerate(inc[r]) if y.get(min(vec))}
  assert app(inc[r],small)==y;checks+=1;cols.append(small)
 saved=list(map(dec,C['A_columns' if r==1 else 'B_columns']))
 assert cols==saved;checks+=1;projected.append(cols)
A,B=projected
K,V,VL,Q,R,H=[list(map(dec,C[k])) for k in ['kernel_basis','image_basis','image_lifts','cycles','coordinate_map_columns','boundary_lift_map_columns']]
assert all(not app(B,v) for v in A+K+Q);checks+=len(A+K+Q)
# Exact signed permutation minor proves B surjective without elimination.
free=[max(v) for v in K];piv=sorted(set(range(196))-set(free));assert len(set(free))==124 and len(piv)==72
assert all(len(B[j])==1 and abs(next(iter(B[j].values())))==1 for j in piv)
assert len({next(iter(B[j])) for j in piv})==72;checks+=3
assert all({j:v[j] for j in free if j in v}=={free[i]:F(1)} for i,v in enumerate(K));checks+=124
old=[]
for v,l in zip(V,VL):
 assert app(A,l)==v and all(not v.get(j) for j in old);old.append(min(v));assert v[min(v)]==1;checks+=1
assert len(set(old))==120;checks+=1
for v in K:
 y=app(A,app(H,v));add(y,app(Q,app(R,v)));assert y==v;checks+=1
for i,v in enumerate(Q):assert app(R,v)=={i:F(1)};checks+=1
for v in A:assert not app(R,v);checks+=1
# Reconstruct each detector's positive projection from the prior signed complete dual cycles.
records=json.loads((root/'hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json').read_text())['records'];saved=json.loads((D/'detectors.json').read_text());actual=[];idx={x:i for i,x in enumerate(bases[1])}
for rec in records:
 if rec['dual_twist']!=-1:continue
 full={}
 for term in rec['terms']:
  key=tuple(term['basis_key']);j=term['index'];assert bases[1][j]==key
  key2,s=rev(key);add(full,{j:F(term['coefficient'],2)});add(full,{idx[key2]:s*F(term['coefficient'],2)})
 small={j:full[min(v)] for j,v in enumerate(inc[1]) if full.get(min(v))};q=app(R,small);h=app(H,small)
 sv=next(x for x in saved if x['detector']==rec['detector'] and x['transported']==rec['transported'])
 assert small==dec(sv['positive_projected_cycle']) and q==dec(sv['coordinates']) and h==dec(sv['boundary_lift']);checks+=1
 y=app(A,h);add(y,app(Q,q));assert y==small;checks+=1
 actual.append([rec['detector'],rec['transported'],[[i,str(x)] for i,x in q.items()]])
out=dict(status='PASS',checks=checks,detectors=actual,certificate_sha256=hashlib.sha256((D/'certificate.json').read_bytes()).hexdigest(),seconds=time.monotonic()-t,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,rank_elimination=False,source_values=False)
(P/'receipt.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
