"""Universal character and degree controls; never an actual-instance experiment."""
import hashlib,json
from pathlib import Path
from collections import Counter
import characters as ch
P=Path(__file__).resolve().parent
checks=0
def require(c,msg):
 global checks
 checks+=1
 if not c: raise RuntimeError(msg)
def clean(c): return {r:c[r] for r in ch.NAMES if c[r]}
def chi(blocks,t):
 c=ch.h0(blocks,t)
 for e,r in blocks:
  if e+t<=-2:c.subtract(ch.product(r,-e-t-2))
 return c
for m in json.loads((P/'INPUTS.json').read_text()):
 b=(P/m['file']).read_bytes()
 require(len(b)==m['bytes'],'bytes '+m['file'])
 require(hashlib.sha256(b).hexdigest()==m['sha256'],'sha256 '+m['file'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==m['git_blob_sha1'],'git blob '+m['file'])
for r in ch.NAMES:
 for n in range(15):
  c=ch.product(r,n)
  require(sum(ch.DIM[s]*k for s,k in c.items())==ch.DIM[r]*(n+1),'dimension')
  require(all(k>=0 for k in c.values()),'genuine symmetric tensor')
sources={
 'D':[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')],
 'P':[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')],
 'V':[(-2,'V'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'V')],
 'Z':[(-3,'Wp'),(-3,'T'),(-3,'T'),(-4,'V')]}
for name,src in sources.items():
 require(sum(ch.DIM[r] for e,r in src)==17,'rank '+name)
 require(sum(e*ch.DIM[r] for e,r in src)==-54,'degree '+name)
 require(clean(chi(src,4))=={'D':2,'V':3,'P':3},'Euler '+name)
expected={4:{'V':-1},10:{'one':1,'A':2,'D':1,'V':-1}}
rows=[]
for e in (4,10):
 A=[(-1,'Wp'),(e,'one')]
 env=ch.h0(A,2);env.update(chi(A,4));env.subtract(chi(sources['P'],4))
 require(clean(env)==expected[e],'signed envelope')
 require(env['V']==-1,'negative V')
 require(ch.product('one',e-2)['one']==0,'D image Hom zero')
 require(ch.product('one',e+1)['Wp']==0,'top derivative scalar Hom zero')
 require(ch.product('Wp',0)['Wp']==1,'top identity Hom one')
 require(sum(ch.DIM[r] for d,r in A)==3,'target rank')
 require(sum(d*ch.DIM[r] for d,r in A)==e-2,'target degree')
 degK=-54-(e-2);degN=degK-(-6)
 require(degN==-46-e,'kernel degree')
 require(14-2==12,'next kernel rank')
 require(degN>12*(-5),'strict degree contradiction')
 require(-5-(-4)<0,'next Hom degree negative')
 rows.append(dict(e=e,envelope=clean(env),next_kernel_rank=12,next_kernel_degree=degN,required_upper_bound=-60))
require(clean(ch.product('one',5))=={'T':1},'Sym5')
require(clean(ch.product('one',11))=={'W':1,'S':1,'T':1},'Sym11')
require(clean(ch.product('one',2))=={'A':1},'Sym2')
require(clean(ch.product('one',8))=={'D':1,'P':1},'Sym8')
# Universal arithmetic controls, not candidate or quotient generation.
for e in range(-20,41):
 require((-46-e<=-60)==(e>=14),'degree threshold equivalence')
fixed=json.loads((P/'inputs/profile11-pairs.json').read_text())
labels={str(e):[i for i,x in enumerate(fixed) if sorted(x['A'])==sorted([[-1,'Wp'],[e,'one']])] for e in (4,10)}
require(labels=={'4':[86,87,88,89,96],'10':[116]},'fixed historical labels')
print(json.dumps(dict(result='two actual quotient shapes excluded when k=1',checks=checks,character_module_checks=ch.checks,targets=rows,historical_labels_only=labels,scope='No profile closure, live-count assertion or original repair'),indent=2,sort_keys=True))
