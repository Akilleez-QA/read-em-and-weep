"""Independent homogeneous trace, global-generator and supertrace-dual controls."""
from pathlib import Path
from itertools import product,permutations,combinations
from fractions import Fraction as Q
from collections import defaultdict
import hashlib,json,math,re,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
start=time.monotonic();H=Path(__file__).resolve().parent;R=H.parent;P=R/'hm-epsilon-projective-generator-bridge-20261016';groups={}
def ck(g,v):
 assert v,g;groups[g]=groups.get(g,0)+1
 assert time.monotonic()-start<20

def add(*ps):
 o=defaultdict(int)
 for p in ps:
  for e,c in p.items():o[e]+=c
 return{e:c for e,c in o.items()if c}
def scale(p,c):return{e:c*a for e,a in p.items()if c*a}
def mul(p,q):
 o=defaultdict(int)
 for a,c in p.items():
  for b,d in q.items():o[tuple(x+y for x,y in zip(a,b))]+=c*d
 return{e:c for e,c in o.items()if c}
one={(0,)*8:1}
def prod(ps):
 o=one
 for p in ps:o=mul(o,p)
 return o
def var(i):return{tuple(int(i==j)for j in range(8)):1}
X=[var(2*i)for i in range(4)];Y=[var(2*i+1)for i in range(4)]
def perm(p,pi):
 o={}
 for e,c in p.items():
  ee=[0]*8
  for i,j in enumerate(pi):ee[j]=e[i]
  o[tuple(ee)]=c
 return o
def eps(p):return(-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))
def br(i,j):return add(mul(X[i],Y[j]),scale(mul(X[j],Y[i]),-1))
a=mul(br(0,1),br(2,3));U=add(prod([X[0],X[1],Y[2],Y[3]]),prod([Y[0],Y[1],X[2],X[3]]));q=prod([X[2],X[2],X[3],X[3],Y[0],Y[0],Y[1],Y[1]])
vs=[add(*(prod([X[i]if i in inds else Y[i]for i in range(4)])for inds in combinations(range(4),k)))for k in range(5)]
beta=[one,vs[2],add(mul(vs[2],vs[2]),scale(mul(vs[1],vs[3]),-1),scale(mul(vs[0],vs[4]),2))]
Delta=prod([br(i,j)for i in range(4)for j in range(i+1,4)])
partition={frozenset([0,1]),frozenset([2,3])};group=[p for p in permutations(range(4))if {frozenset(p[i]for i in b)for b in partition}==partition]
for p in group:
 pi=tuple(2*p[i]+j for i in range(4)for j in range(2))
 ck('epsilon_generator_character',perm(a,pi)==scale(a,eps(p)));ck('resolvent_invariant',perm(U,pi)==U)
rev=tuple(i^1 for i in range(8))
for j in range(3):
 generator=mul(a,prod([U]*j));ck('generator_reversal',perm(generator,rev)==generator)
 for e in generator:ck('generator_multidegree',all(e[2*i]+e[2*i+1]==j+1 for i in range(4)))
 f=mul(q,generator);alt=add(*(scale(perm(f,tuple(2*p[i]+t for i in range(4)for t in range(2))),eps(p))for p in permutations(range(4))))
 expected=scale(mul(Delta,beta[j]),4);ck('eight_variable_trace_identity',alt==expected)
 for e in alt:ck('trace_multidegree',all(e[2*i]+e[2*i+1]==j+3 for i in range(4)))
 ck('beta_reversal',perm(beta[j],rev)==beta[j])
 # Every standard chart, including all infinity combinations, is a restriction of the same identity.
 for chart in product([0,1],repeat=4):
  def local(poly):
   o=defaultdict(int)
   for e,c in poly.items():o[tuple(e[2*i+(1 if chart[i]else 0)]for i in range(4))]+=c
   return{k:v for k,v in o.items()if v}
  ck('all_16_chart_trace_restrictions',local(alt)==local(expected))
# The graded-dimension equality is a degree-four polynomial identity, so five points suffice.
def choose(n):return math.comb(n,4)if n>=4 else 0
for n in range(9):
 def cycles(p):
  seen=set();c=0
  for i in range(4):
   if i in seen:continue
   c+=1;j=i
   while j not in seen:seen.add(j);j=p[j]
  return c
 inv=Q(sum((n+1)**cycles(p)for p in group),8);odd=Q(sum(eps(p)*(n+1)**cycles(p)for p in group),8)
 ck('invariant_graded_dimension',inv==choose(n+4)+choose(n+3)+choose(n+2))
 ck('epsilon_graded_dimension',odd==choose(n+3)+choose(n+2)+choose(n+1))
# Original authenticated rows; genuine degree signs, not ordinary transpose.
txt=(R/'hm-four-detector-carrier-transfer-20261015/THEOREM.md').read_text();rows={}
for name in 'hjpr':
 expr=next(line for line in txt.splitlines()if line.startswith('- L'+name+'=')).split('=',1)[1].replace('−','-')
 rows[name]={(b,int(i),int(j)):(-1 if s=='-'else 1)for s,b,i,j in re.findall(r'([+-]?)F(20|31)\[(\d+),(\d+)\]',expr)}
raw=(R/'hm-factored-coefficient-action-20261014/pinned-model-input.json').read_bytes();ck('original_model_pin',hashlib.sha256(raw).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926');model=json.loads(raw);dd=[]
for name in ['gamma','delta','ev']:
 d={}
 for i,row in enumerate(model[name]):
  for j,terms in enumerate(row):
   for ex,c in terms:
    e=tuple(map(int,ex.split(',')));assert sum(e)<=1;d[i,j,0 if not sum(e)else 1+e.index(1)]=c
 dd.append(d)
ranks=[5,15,10,2]
def dual(row):
 return{(0,2,j,i):-c if b=='20'else c for (b,i,j),c in row.items()if b=='20'}|{(1,3,j,i):c for(b,i,j),c in row.items()if b=='31'}
def transport(E):
 def ix(level,i):return i if level==3 else 5*(i//5)+4-i%5
 signs=[-1,-1,1,1]
 return{(u,v,ix(v,i),ix(u,j)):c*signs[u]*signs[v]for(u,v,i,j),c in E.items()}
def boundary(E):
 o=defaultdict(int)
 for (u,v,i,j),c in E.items():
  if v<3:
   for (a,b,k),z in dd[v].items():
    if b==i:o[u,v+1,a,j,k]+=z*c
  if u>0:
   for(a,b,k),z in dd[u-1].items():
    if a==j:o[u-1,v,i,b,k]-=c*z
 return{k:v for k,v in o.items()if v}
# Pair with all 80 coordinate basis vectors in degree -2.
for name,row in rows.items():
 E=dual(row)
 for block,n,m in [('20',5,10),('31',15,2)]:
  for i,j in product(range(n),range(m)):
   pairing=(-1 if block=='20'else 1)*E.get((0 if block=='20'else 1,2 if block=='20'else 3,j,i),0)
   ck('all_matrix_unit_supertrace_pairings',pairing==row.get((block,i,j),0))
 ck('original_dual_cycle_closed',not boundary(E));ck('transported_dual_cycle_closed',not boundary(transport(E)))
 ck('dual_transport_involution',transport(transport(E))==E)
ck('total_pairing_sign',(-1)**(2*4)==1)
# Independently enumerate the archived ambient basis and authenticate every supplied sparse term.
def mons(d,n=5):
 if n==1:return[(d,)]
 return[(i,)+m for i in range(d+1)for m in mons(d-i,n-1)]
b5=[{(0,0,0,0,0):1},{(0,0,1,0,0):1},{(0,0,2,0,0):1,(0,1,0,1,0):-1,(1,0,0,0,1):2}]
records=json.loads((P/'detector-dual-cycles.json').read_text());ck('genuine_degrees',records['genuine_complex_degrees']==[-1,0,1,2]);ck('exact_record_count',len(records['records'])==24)
seen=set()
for rec in records['records']:
 name=rec['detector'];j=rec['dual_twist']+2;revflag=rec['transported'];ident=name,j,revflag;ck('unique_cycle_record',ident not in seen);seen.add(ident)
 basis=[(u,u+2,a,b,*m)for u in range(2)for a in range(ranks[u+2])for b in range(ranks[u])for m in mons(j)];idx={key:i for i,key in enumerate(basis)}
 ck('ambient_dimension',len(basis)==rec['ambient_dimension']==[80,400,1200][j]);ck('serre_dual_twist',rec['primal_twist']==-3-j)
 E=transport(dual(rows[name]))if revflag else dual(rows[name]);want={(*k,*m):4*c*z for k,c in E.items()for m,z in b5[j].items()};got={tuple(t['basis_key']):t['coefficient']for t in rec['terms']}
 ck('exact_sparse_cycle',got==want and len(got)==len(rec['terms']))
 for t in rec['terms']:ck('every_ambient_index',t['index']==idx[tuple(t['basis_key'])])
 ck('global_cycle_not_only_constant_specialization',not boundary(E)and all(sum(m)==j for m in b5[j]))
ck('positive_P4_coordinate_reversal',eps(tuple(reversed(range(5))))==1)
for name,gitsha in [('Perfect-Complex-D8-F3.md','3a8c3633e83466b29ea2e5739c6b486f856b91b2'),('certificate.json','304d031083bb2a19fb9bc012cfd338bbe0129980'),('check_hm_p4_all_twists.js','7adc1d6a733636204b1dd613870c168717be6277')]:
 raw=(P/'pinned'/name).read_bytes();ck('archived_package_git_pin',hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==gitsha)
report=dict(status='PASS',controls=sum(groups.values()),groups=groups,global_trace_coefficients=['4','4 v2','4(v2^2-v1 v3+2v0 v4)'],supertrace_signs=[-1,1],dual_records_verified=24,source_values_acquired=False,large_solve=False,elapsed_seconds=time.monotonic()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(H/'bridge-receipt.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
