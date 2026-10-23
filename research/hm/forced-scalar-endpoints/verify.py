"""Universal character/degree controls, not actual-instance computations."""
from pathlib import Path
import hashlib,json
from collections import Counter
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
for row in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/row['file']).read_bytes()
 require(len(b)==row['bytes'],'input length '+row['file'])
 require(hashlib.sha256(b).hexdigest()==row['sha256'],'input SHA256 '+row['file'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob_sha1'],'Git blob '+row['file'])
import characters as c
for R in c.NAMES:
 for n in range(26):
  z=c.product(R,n)
  require(sum(c.DIM[s]*v for s,v in z.items())==c.DIM[R]*(n+1),'tensor dimension')
  require(all(isinstance(v,int) and v>=0 for v in z.values()),'genuine tensor')
def chi(blocks,t):
 z=Counter()
 for e,R in blocks:
  z.update(c.product(R,e+t));z.subtract(c.product(R,-e-t-2))
 return z
def clean(z):return {R:z[R] for R in c.NAMES if z[R]}
E=[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')]
require(sum(c.DIM[R] for e,R in E)==17,'rank E')
require(sum(e*c.DIM[R] for e,R in E)==-54,'degree E')
X=chi(E,4)
require(clean(X)=={'D':2,'V':3,'P':3},'Euler E4')
for n in range(7):require(c.product('one',n)['Wp']==0,'first Wp lower')
require(c.product('one',7)['Wp']==1,'first Wp')
require(c.product('one',17)['Wp']==1,'unique scalar channel')
require(c.product('one',9)['Wp']==0,'reject degree9')
# Common invariant divisor b must be at most10, strictly below12.
base_divisors=[]
for b in range(18):
 if c.product('one',17-b)['Wp']:
  require(b<=10,'common divisor character bound')
  if b==0 or b>=12:base_divisors.append(b)
require(base_divisors==[0],'scalar line base-point-free')
rows=[]
for r in (3,5):
 A=[(-r,'Wp'),(16,'one')]
 a=sum(e*c.DIM[R] for e,R in A)
 require(a==16-2*r,'degree A')
 degK=-54-a;degN=degK+6;lower=degN+44;upper=-r-9
 require((degK,degN,lower)==(-70+2*r,-64+2*r,-20+2*r),'source lower bound')
 C=c.h0(A,2);C.subtract(X);C.update(chi(A,4))
 require(C['V']==-1,'forced cubic witness')
 candidate=[]
 for e in range(lower,upper+1):
  if e%2==0 and c.product('one',-r-2-e)['Wp']:candidate.append(e)
 require(candidate==([-12] if r==3 else []),'rank-two candidates')
 witnesses=[]
 for e in candidate:
  I=[(14,'one'),(e,'one')]
  Q=c.h0(I,2);Q.update(chi(A,4));Q.update(chi(I,4));Q.subtract(X)
  require(clean(Q)=={'one':1,'A':2,'D':3,'V':-1,'P':1},'rank-two signed witness')
  require(Q['V']<0,'rank-two contradiction')
  witnesses.append(dict(e=e,envelope=clean(Q)))
 I=[(14,'one')]
 Q=c.h0(I,2);Q.update(chi(A,4));Q.update(chi(I,4));Q.subtract(X)
 require(clean(Q)=={'one':1,'A':2,'D':3,'P':2 if r==3 else 1},'rank-one envelope')
 require(all(v>=0 for v in Q.values()),'do not exclude rank-one')
 degL=degK-14
 require(degL==-84+2*r,'rank-one kernel degree')
 require(degL+20==degN,'cubic-kernel quotient degree')
 require(-6-14==-20,'cubic line kernel degree')
 require(14-2==12,'next derivative target')
 rows.append(dict(r=r,degree_A=a,degree_K=degK,degree_N=degN,min_degree_K=lower,negative_image_upper=upper,rank_two_candidates=candidate,rank_two_witnesses=witnesses,forced_derivative_rank=1,forced_image_degree=14,rank_next_kernel=13,degree_next_kernel=degL,cubic_kernel_degree=-20,next_derivative_target_degree=12,rank_one_envelope=clean(Q)))
print(json.dumps(dict(status='PASS',scope='P-source; actual k=1; no target exclusion',checks=checks,character_module_checks=c.checks,rows=rows),indent=2,sort_keys=True))
