# Historical reproducibility source. Not executed during publication preparation.
"""Small exact global-generator and detector-dual bridge. No source values/rank solve."""
import hashlib,itertools,json,resource,time
from pathlib import Path
from collections import defaultdict
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
HERE=Path(__file__).resolve().parent; START=time.monotonic(); checks=0
def test(b):
 global checks
 assert b; checks+=1
def add(*ps):
 r=defaultdict(int)
 for p in ps:
  for e,c in p.items():r[e]+=c
 return {e:c for e,c in r.items() if c}
def sc(p,c):return {e:c*a for e,a in p.items() if c*a}
def mul(p,q):
 r=defaultdict(int)
 for a,c in p.items():
  for b,d in q.items():r[tuple(x+y for x,y in zip(a,b))]+=c*d
 return {e:c for e,c in r.items() if c}
def powp(p,n):
 r={(0,)*len(next(iter(p))):1}
 for _ in range(n):r=mul(r,p)
 return r
def var(n,i):return {tuple(int(i==j) for j in range(n)):1}
def perm(p,pi):
 r={}
 for e,c in p.items():
  a=[0]*len(e)
  for i,j in enumerate(pi):a[j]=e[i]
  r[tuple(a)]=c
 return r
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

# Homogeneous generator character and involution: eight independent Cox variables.
X=[var(8,2*i) for i in range(4)];Y=[var(8,2*i+1) for i in range(4)]
br=lambda i,j:add(mul(X[i],Y[j]),sc(mul(X[j],Y[i]),-1))
a=mul(br(0,1),br(2,3))
U=add(mul(mul(X[0],X[1]),mul(Y[2],Y[3])),mul(mul(Y[0],Y[1]),mul(X[2],X[3])))
rev=[j^1 for j in range(8)]
for f in (a,U):test(perm(f,rev)==f)
for pi,eps in [((1,0,2,3),-1),((0,1,3,2),-1),((2,3,0,1),1)]:
 pp=[2*pi[i]+j for i in range(4) for j in range(2)]
 test(perm(a,pp)==sc(a,eps));test(perm(U,pp)==U)
for j in range(3):
 for e in mul(a,powp(U,j)):
  test(all(e[2*i]+e[2*i+1]==j+1 for i in range(4)))

# Exact polynomial alternants, not sampled values; dense-chart identities homogenize.
x=[var(4,i) for i in range(4)];one={(0,)*4:1}
e=[one]
for k in range(1,5):
 e.append(add(*(powp(one,1) if not ss else __import__('functools').reduce(mul,(x[i] for i in ss),one) for ss in itertools.combinations(range(4),k))))
aa=mul(add(x[0],sc(x[1],-1)),add(x[2],sc(x[3],-1)))
uu=add(mul(x[0],x[1]),mul(x[2],x[3]));q=mul(powp(x[2],2),powp(x[3],2))
delta=one
for i in range(4):
 for j in range(i+1,4):delta=mul(delta,add(x[i],sc(x[j],-1)))
beta=[one,e[2],add(powp(e[2],2),sc(mul(e[1],e[3]),-1),sc(e[4],2))]
for j in range(3):
 f=mul(q,mul(aa,powp(uu,j)))
 alt=add(*(sc(perm(f,pi),sign(pi)) for pi in itertools.permutations(range(4))))
 test(alt==sc(mul(beta[j],delta),4))
v=[var(5,i) for i in range(5)];b5=[{(0,)*5:1},v[2],add(powp(v[2],2),sc(mul(v[1],v[3]),-1),sc(mul(v[0],v[4]),2))]
for b in b5:test(perm(b,list(reversed(range(5))))==b)

# Authenticate the exact pinned small package, without executing its rank routine.
expected={'Perfect-Complex-D8-F3.md':'3a8c3633e83466b29ea2e5739c6b486f856b91b2','certificate.json':'304d031083bb2a19fb9bc012cfd338bbe0129980','check_hm_p4_all_twists.js':'7adc1d6a733636204b1dd613870c168717be6277'}
for name,h in expected.items():
 b=(HERE/'pinned'/name).read_bytes();test(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==h)
cert=json.loads((HERE/'pinned/certificate.json').read_text())
test([c['cohomology'][2] for c in cert['p4Twists']]==[2,10,20,20])

# Only the homogeneous linear differential literals are used below.
modelpath=HERE.parent/'hm-factored-coefficient-action-20261014/pinned-model-input.json'
model=json.loads(modelpath.read_text()); ranks=[5,15,10,2]
dd=[]
for name in ['gamma','delta','ev']:
 d={}
 for i,row in enumerate(model[name]):
  for j,ls in enumerate(row):
   for ex,c in ls:
    ee=tuple(map(int,ex.split(',')));test(sum(ee)<=1)
    k=0 if sum(ee)==0 else ee.index(1)+1
    d[i,j,k]=d.get((i,j,k),0)+c
 dd.append({k:c for k,c in d.items() if c})
rows={'h':{('31',0,1):1,('20',2,6):-1,('20',3,9):-1},'j':{('31',1,1):1,('20',3,7):-1,('20',4,5):-1},'p':{('31',5,0):1,('20',1,3):1,('20',4,2):1},'r':{('31',6,0):1,('20',0,3):1,('20',2,4):1}}
idx=[[4-i for i in range(5)],[5*b+4-i for b in range(3) for i in range(5)],[5*b+4-i for b in range(2) for i in range(5)],[0,1]]
sg=[-1,-1,1,1]
def dual(row):
 # Genuine L degrees -1,0,1,2: Str(F E)=-tr(F20 E02)+tr(F31 E13).
 return {(0 if block=='20' else 1,2 if block=='20' else 3,j,i):(-c if block=='20' else c) for (block,i,j),c in row.items()}
def transport(E):return {(u,v,idx[v][a],idx[u][b]):c*sg[u]*sg[v] for (u,v,a,b),c in E.items()}
def boundary2(E):
 r=defaultdict(int)
 for (u,v,a,b),c in E.items():
  if v<3:
   for (i,j,k),z in dd[v].items():
    if j==a:r[u,v+1,i,b,k]+=c*z
  if u>0:
   for (i,j,k),z in dd[u-1].items():
    if i==b:r[u-1,v,a,j,k]-=c*z
 return {k:c for k,c in r.items() if c}
outrows={}
for name,row in rows.items():
 E=dual(row);test(not boundary2(E));test(not boundary2(transport(E)));test(transport(transport(E))==E)
 for (block,i,j),c in row.items():
  u=0 if block=='20' else 1;vv=u+2
  test((-1)**(u-1)*E[u,vv,j,i]==c)
 outrows[name]={'dual_cycle':[[*k,c] for k,c in E.items()],'transported_dual_cycle':[[*k,c] for k,c in transport(E).items()]}

# Sparse ambient coordinates in the exact archived basis(r=2,t=j-2).
# These are cycle representatives, not quotient-coordinate claims.
def monomials(degree,n=5):
 if n==1:return [(degree,)]
 return [(a,)+b for a in range(degree+1) for b in monomials(degree-a,n-1)]
cycle_records=[]
for j in range(3):
 basis=[(u,u+2,a,b,*m) for u in range(2) for a in range(ranks[u+2]) for b in range(ranks[u]) for m in monomials(j)]
 index={b:i for i,b in enumerate(basis)}
 test(len(basis)==[80,400,1200][j])
 for name,row in rows.items():
  for reversed_ in [False,True]:
   E=transport(dual(row)) if reversed_ else dual(row)
   terms=[{'index':index[(*k,*m)],'basis_key':list((*k,*m)),'coefficient':4*c*z} for k,c in E.items() for m,z in b5[j].items()]
   test(len({r['index'] for r in terms})==len(terms))
   cycle_records.append({'detector':name,'transported':reversed_,'primal_twist':-3-j,'dual_twist':j-2,'ambient_dimension':len(basis),'terms':sorted(terms,key=lambda x:x['index'])})
(HERE/'detector-dual-cycles.json').write_text(json.dumps({'scope':'Exact sparse global-cycle coordinates in the archived ambient basis; not quotient coordinates','genuine_complex_degrees':[-1,0,1,2],'basis_key':['source_index','target_index','row','column','v0','v1','v2','v3','v4'],'records':cycle_records},indent=2)+'\n')

# Tiny derivative-cycle representation, independent of any large matrix rank computation.
for ell,d in enumerate(dd):
 for (i,j,k),c in d.items():
  test(dd[ell].get((idx[ell+1][i],idx[ell][j],4-k),0)==sg[ell]*sg[ell+1]*c)
for ell in range(2):
 product=defaultdict(int)
 for (i,j,k),c in dd[ell].items():
  for (a,b,l),z in dd[ell+1].items():
   if b==i:product[a,j,tuple(sorted((k,l)))]+=c*z
 test(not any(product.values()))
# Derivative cycle D_k has ev coefficient1 at each block's column k; it has unique pivots.
for k in range(5):
 for l in range(5):test(dd[2].get((0,k,l),0)==int(k==l))

out={'status':'PASS','checks':checks,'seconds':time.monotonic()-START,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'source_values':False,'rank_rerun':False,'global_generator_degrees':[1,2,3],'epsilon_twists':[-3,-4,-5],'dimensions':[20,10,2],'detector_factor':4,'beta':[[[list(e),c] for e,c in b.items()] for b in b5],'dual_cycles':outrows,'derivative_kernel_dimension_from_archived_certificate':5,'derivative_kernel_involution_trace':1,'pinned_git_blobs':expected,'model_sha256':hashlib.sha256(modelpath.read_bytes()).hexdigest()}
(HERE/'receipt.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('dual_cycles','beta')},indent=2))
