# Historical reproducibility source. Not executed during publication preparation.
"""Fixed v0 multiplication via saved quotient maps; no elimination/source values."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,)*2)
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
start=time.monotonic()
modelpath=ROOT/'hm-factored-coefficient-action-20261014/pinned-model-input.json'
certpath=ROOT/'hm-plus-twist-minus1-quotient-20261016/certificate.json'
model=json.loads(modelpath.read_text())
cert=json.loads(certpath.read_text())
gamma={}
for i,row in enumerate(model['gamma']):
 for a,terms in enumerate(row):
  for exponent,c in terms:
   ex=tuple(map(int,exponent.split(',')))
   if sum(ex)>1: raise ValueError('Not authenticated linear gamma')
   k=0 if not sum(ex) else ex.index(1)+1
   gamma[i,a,k]=gamma.get((i,a,k),0)+c
del model
basis=cert['full_bases'][1]
if len(basis)!=400: raise ValueError('Wrong degree2 twist-minus1 basis')
index={tuple(x):i for i,x in enumerate(basis)}
orbits=cert['positive_orbits'][1]
if len(orbits)!=196: raise ValueError('Wrong positive space')
projector={}
for j,o in enumerate(orbits):
 i,p,s=o['representative'],o['partner'],o['sign']
 if i==p:
  if s!=1: raise ValueError('Negative fixed vector retained')
  projector[i]=(j,F(1))
 else:
  projector[i]=(j,F(1,2));projector[p]=(j,F(s,2))
Q=[{int(i):F(c) for i,c in col} for col in cert['coordinate_map_columns']]
if len(Q)!=196 or any(len(c)>4 for c in Q):raise ValueError('Coordinate map cap')
projector_operations=0;coefficient_products=0
columns=[]
for r in range(30):
 b,i=divmod(r,15)
 E={(1,3,b,i):1}
 for a in range(5):
  for k in range(5):
   c=gamma.get((i,a,k),0)
   if c:E[0,2,5*b+k,a]=c
 if len(E)>26:raise ValueError('Input support cap')
 col=[F(0) for _ in range(4)]
 for key,c in E.items():
  ambient=index[(*key,1,0,0,0,0)]
  if ambient not in projector:continue
  j,p=projector[ambient]
  projector_operations+=1
  if projector_operations>780:raise ValueError('Projection operation cap')
  value=p*c
  for h,q in Q[j].items():
   coefficient_products+=1
   if coefficient_products>3120:raise ValueError('Product cap')
   col[h]+=value*q
 columns.append(col)
receipt={'scope':'Saved positive quotient projection of v0 times all30 K30 graph cycles',
 'operation_caps':{'projector':780,'coordinate_products':3120},
 'operations':{'projector':projector_operations,'coordinate_products':coefficient_products},
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [modelpath,certpath]},
 'columns':[[str(c) for c in col] for col in columns],
 'seconds':time.monotonic()-start,'rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'elimination':False,'source_values':False}
(HERE/'v0-map.json').write_text(json.dumps(receipt,indent=2)+'\n')
for r,col in enumerate(columns):
 if any(col):print(r,[str(c) for c in col])
print('Operations:',receipt['operations'])
