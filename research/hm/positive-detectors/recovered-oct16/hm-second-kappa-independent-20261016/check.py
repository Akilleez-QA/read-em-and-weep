# Historical reproducibility source. Not executed during publication preparation.
#!/usr/bin/env python3
"""Four saved-map witnesses plus tiny Cox trace identities; no elimination."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations, combinations
import hashlib,json,resource,time

ROOT=Path(__file__).resolve().parent.parent
HERE=Path(__file__).resolve().parent
start=time.monotonic(); checks=0; products=0
def ok(x):
 global checks
 assert x
 checks+=1
def cp(a,b):
 global products
 if products>=3900: raise RuntimeError('Universal coefficient-product cap')
 products+=1
 return a*b
def plus(a,b):
 c=dict(a)
 for m,v in b.items():
  c[m]=c.get(m,F(0))+v
  if not c[m]: del c[m]
 return c
def times(a,b):
 c={}
 for m,x in a.items():
  for n,y in b.items():
   k=tuple(i+j for i,j in zip(m,n))
   c[k]=c.get(k,F(0))+cp(x,y)
 return {m:c for m,c in c.items() if c}
def scaled(a,s): return {m:cp(c,s) for m,c in a.items() if c}
def mon(xs):
 e=[0]*8
 for i in xs:e[i]+=1
 return {tuple(e):F(1)}
def permute(a,p):
 c={}
 for m,v in a.items():
  n=[0]*8
  for i in range(4):n[2*p[i]]=m[2*i];n[2*p[i]+1]=m[2*i+1]
  c[tuple(n)]=v
 return c
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def alt(a):
 c={}
 for p in permutations(range(4)):c=plus(c,scaled(permute(a,p),sign(p)))
 return c
def bracket(i,j):return plus(mon([2*i,2*j+1]),scaled(mon([2*j,2*i+1]),-1))
one=mon([])
v=[]
for d in range(5):
 p={}
 for S in combinations(range(4),d):p=plus(p,mon([2*i+(0 if i in S else 1) for i in range(4)]))
 v.append(p)
a=times(bracket(0,1),bracket(2,3))
U=plus(mon([0,2,5,7]),mon([1,3,4,6]))
qprime=mon([0,1,3,3,4,5,7,7])
Delta=one
for i,j in combinations(range(4),2):Delta=times(Delta,bracket(i,j))
H=[p for p in permutations(range(4)) if {frozenset((p[0],p[1])),frozenset((p[2],p[3]))}=={frozenset((0,1)),frozenset((2,3))}]
ok(len(H)==8)
average={}
for p in H:average=plus(average,permute(qprime,p))
average=scaled(average,F(1,8))
rhs=scaled(times(v[0],plus(v[2],scaled(U,-1))),F(1,4))
ok(average==rhs)
Upow=one
for j in range(3):
 lhs=alt(times(qprime,times(a,Upow)))
 target=scaled(times(v[0],Delta),-2) if j==1 else {}
 ok(lhs==target)
 Upow=times(Upow,U)
ok(tuple(-e-1 for e in (1,0,1,0))==(-2,-1,-2,-1))

modelpath=ROOT/'hm-factored-coefficient-action-20261014/pinned-model-input.json'
certpath=ROOT/'hm-plus-twist-minus1-quotient-20261016/certificate.json'
producerpath=ROOT/'hm-two-position-positive-completeness-20261016/v0-map.json'
model=json.loads(modelpath.read_text()); cert=json.loads(certpath.read_text()); saved=json.loads(producerpath.read_text())
ok(hashlib.sha256(modelpath.read_bytes()).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926')
ok(hashlib.sha256(certpath.read_bytes()).hexdigest()=='616006681d2952a3d895e2bf369d2c5813a9091c38a490b9bd936c2299e5de3c')
gamma={}
for i,row in enumerate(model['gamma']):
 for a,terms in enumerate(row):
  for exp,c in terms:
   m=tuple(map(int,exp.split(',')))
   ok(len(m)==4 and min(m)>=0 and sum(m)<=1)
   k=0 if sum(m)==0 else m.index(1)+1
   gamma[i,a,k]=gamma.get((i,a,k),0)+F(c)
def graph(r):
 c,i=divmod(r,15); E={(1,3,c,i):F(1)}
 for a in range(5):
  for k in range(5):
   if gamma.get((i,a,k)):E[0,2,5*c+k,a]=gamma[i,a,k]
 return E
basis=[tuple(k) for k in cert['full_bases'][1]]; index={k:i for i,k in enumerate(basis)}
orbits=cert['positive_orbits'][1]; Q=cert['coordinate_map_columns']
ok(len(basis)==400 and len(orbits)==196 and len(Q)==196)
ok(all(len(c)<=4 for c in Q))
ok(30*26==780 and 4*780==3120 and 780+3120==3900)
ambient_to_positive={}
for j,o in enumerate(orbits):
 for i in {o['representative'],o['partner']}: ambient_to_positive[i]=j
static_projector=0; static_Q=0
for r in range(30):
 E=graph(r); ok(len(E)<=26)
 for key in E:
  ambient=index[key+(1,0,0,0,0)]
  if ambient in ambient_to_positive:
   static_projector+=1
   static_Q+=len(Q[ambient_to_positive[ambient]])
ok((static_projector,static_Q)==(80,14))
ok(saved['operations']=={'projector':80,'coordinate_products':14})

def reversal(k):
 u,w,a,b,*m=k
 # Genuine chain signs on both degree+2 blocks are negative.
 if (u,w)==(0,2):a=5*(a//5)+4-a%5;b=4-b
 elif (u,w)==(1,3):b=5*(b//5)+4-b%5
 else:raise AssertionError(k)
 return (u,w,a,b,*reversed(m))
expected={9:[F(1,2),0,0,0],4:[0,F(-1,2),0,0],5:[0,0,F(1),0],12:[0,0,0,F(1,2)]}
columns={}
for r,want in expected.items():
 # Independent route: form full (v0E + rho(v0E))/2, rather than
 # distributing an ambient coefficient directly into an orbit map.
 full={}
 for k,c in graph(r).items():
  key=k+(1,0,0,0,0)
  full=plus(full,{key:cp(c,F(1,2))})
  full=plus(full,{reversal(key):cp(c,F(-1,2))})
 coordinates={j:full.get(basis[o['representative']],F(0)) for j,o in enumerate(orbits)}
 coordinates={j:c for j,c in coordinates.items() if c}
 rebuilt={}
 for j,c in coordinates.items():
  o=orbits[j]
  rebuilt=plus(rebuilt,{basis[o['representative']]:c})
  if o['representative']!=o['partner']:rebuilt=plus(rebuilt,{basis[o['partner']]:cp(c,o['sign'])})
 ok(rebuilt==full)
 outgoing={}; image=[F(0)]*4
 for j,c in coordinates.items():
  for i,t in cert['B_columns'][j]:outgoing=plus(outgoing,{int(i):cp(c,F(t))})
  for i,t in Q[j]:image[int(i)]+=cp(c,F(t))
 ok(not outgoing)
 ok(image==want)
 ok([F(x) for x in saved['columns'][r]]==image)
 columns[str(r)]=[str(x) for x in image]
ok(products<=3900)
receipt={'status':'PASS','checks':checks,'fixed_universal_coefficient_products':products,
 'product_cap':3900,'producer_count_metadata_verified':{'projector':static_projector,'coordinate_products':static_Q},
 'four_verified_Q_columns':columns,'position':[-2,-1,-2,-1],
 'trace_triple':['0','-2*v0','0'],'resulting_four_rows':['-w0','w1','-2*w2','-w3'],
 'seconds':time.monotonic()-start,'rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'rank_elimination':False,'source_values':False,'all81_positions_processed':False,
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [modelpath,certpath,producerpath]}}
(HERE/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
