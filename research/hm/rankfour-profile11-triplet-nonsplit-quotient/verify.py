"""Bounded fixed identities only. This checker does not replace the proof."""
import hashlib,json
from pathlib import Path
from collections import Counter
from math import factorial
import characters as C
BASE=Path(__file__).resolve().parent
CHECKS=0
def require(c,msg):
 global CHECKS
 CHECKS+=1
 if not c: raise RuntimeError(msg)
def signed(*terms):
 out=Counter()
 for factor,value in terms:
  for k,v in value.items():out[k]+=factor*v
 return {k:v for k,v in out.items() if v}
def s(n):return C.product('one',n)
def one(r):return Counter({r:1})
PINS={
 'inputs/ranksix-common-kernel.md':('95137a91303d46fd945f5a2d0fed330f0e32df8c',9703,'06e1795f1390e8451dbf4e98e10a8011b3e97ce733ec6b1cbbd5af90b4694111','5661a972f1eccce29a49ea4b1af305c693a380b2'),
 'inputs/mixed-jet-pairing.md':('84b418e22f03b5718409bdeb23ae353ecc4eb681',14593,'3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b','91e0c23867113c0a7d5b032098c8e365b356859d')}
a=json.loads((BASE/'INPUTS.json').read_text())
require(len(a)==2,'exact direct input count')
require({i['file'] for i in a}==set(PINS),'exact selected inputs')
for i in a:
 ref,n,sha,git=PINS[i['file']];b=(BASE/i['file']).read_bytes()
 require(i['ref']==ref,'immutable ref')
 require(len(b)==i['bytes']==n,'complete input length')
 require(hashlib.sha256(b).hexdigest()==i['sha256']==sha,'input sha256')
 require(hashlib.sha1(b'blob '+str(n).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==git,'input git blob')
 require(i['url'].endswith('/'+ref+'/'+i['path']),'immutable path URL')
proof=(BASE/'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest()=='d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568','frozen whole proof')
# Fixed character identities, not selected instances.
V=Counter({'A':1,'V':1,'D':1,'P':1})
require(s(6)==Counter({'V':1,'P':1}),'Sym6')
require(s(9)==Counter({'S':1,'T':1}),'Sym9')
require(s(12)['one']==1,'unique universal degree12 invariant')
for n in (2,6,10):require(s(n)['one']==0,'no scalar invariant degree '+str(n))
require(signed((1,V),(-1,C.product('T',13)),(1,C.product('T',11)))=={'V':1},'orthogonal Euler character')
expected={2:{'A':1},4:{'one':1,'D':1,'A':-1},6:{'one':1,'V':1,'P':1,'D':-1}}
for d in (2,4,6):
 chi=signed((1,one('one')),(1,s(d)),(-1,s(d-2)))
 require(chi==expected[d],'fixed unequal orthogonal character '+str(d))
 require(chi!={'V':1},'unequal orthogonal type excluded '+str(d))
for n in (0,1,2):require(C.product('V',n)['one']==0,'no scalar top line in alternate triple '+str(n))
require(C.product('V',3)==Counter({'S':1,'T':1,'Wp':1}),'alternate triple times Sym3')
require(signed((1,C.product('V',3)),(-1,s(9)))=={'Wp':1},'perpendicular rank2 character')
require(C.product('Wp',3)==Counter({'D':1,'V':1}),'Wp times Sym3')
require(C.product('Wp',3)['one']==0,'Ext1 splitting')
require(C.product('T',3)['one']==0,'coherent lower derivative Hom')
# Degree and universal formal norm bookkeeping.
require(15-2*6==3,'orthogonal quotient rank')
require(6*(5-18)==-78,'actual fifth jet degree')
require(7*(6-18)==-84,'actual sixth jet degree')
require(-84-(-78)==-6,'actual scalar quotient degree')
require(2*6==12<18,'first nonzero norm order')
require((-1)**6*factorial(12)!=0,'universal mixed6,6 factorial')
require(-6-(-6)==0,'rank3 total degree')
require(-3*2==-6,'balanced rank2 degree')
require(-8+2*(-3)==-14,'actual rank3 quotient degree')
require(-14-(-10)==-4,'quotient B6/G6 degree')
require(2*(-3)-(-10)==4,'degree7 extension quotient')
require(-10-4==-14,'first extension Hom degree')
require(-10-(-8)==-2,'pullback extension Hom degree')
require((-14)+12==-2,'multiplication by universal invariant')
require(-(-14)-2==12 and -(-2)-2==0,'Serre dual multiplication direction')
require(-3-(-8)==5 and 5-2==3,'Ext dual symmetric power')
require(-10-(-13)==3,'coherent lower Hom degree')
require(-8-(-10)==2,'canonical line has no internal component')
require(-8+(-10)==2*(-9),'nonsplit M degree')
print(json.dumps({'status':'PASS','checks':CHECKS,'proof_sha256':hashlib.sha256(proof).hexdigest(),'scope':'two complete immutable inputs; fixed characters, degrees, formal mixed norm and Serre-duality directions','not_claimed':['actual coefficients or instance evaluations','selected invariant normalization or graph scalar','branch occurrence or exclusion','original tenth jets','proof by computation']},sort_keys=True,indent=2))
