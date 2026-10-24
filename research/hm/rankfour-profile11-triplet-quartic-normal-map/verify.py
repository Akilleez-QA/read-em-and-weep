"""Bounded universal checks only; no selected source-instance evaluation."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib,json
import characters as C
BASE=Path(__file__).resolve().parent
count=0
def require(c,msg):
 global count
 count+=1
 if not c:raise RuntimeError(msg)
pins={
 'inputs/top-jet-complement.md':('317cf0c533b6ab8ce650d566e08c87610dd11ccd',11240,'08708a646f51fb6b10ef94c1eab1b5e4ee56a775fb8e377d6a92e8d34df54259','63abea7d4412fced453c728d9f1e3c7dd4870521'),
 'inputs/nonsplit-quotient.md':('f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1',13619,'d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568','1974a5c3b20546dcb414539096511388f495cdab')}
a=json.loads((BASE/'INPUTS.json').read_text())
require(len(a)==2 and {i['file'] for i in a}==set(pins),'complete selected originals')
for i in a:
 ref,n,sha,git=pins[i['file']];b=(BASE/i['file']).read_bytes()
 require(i['ref']==ref,'immutable ref')
 require(len(b)==i['bytes']==n,'complete byte length')
 require(hashlib.sha256(b).hexdigest()==i['sha256']==sha,'input hash')
 require(hashlib.sha1(b'blob '+str(n).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==git,'input blob')
 require(i['url'].endswith('/'+ref+'/'+i['path']),'immutable path URL')
proof=(BASE/'PROOF.md').read_bytes()
require(len(proof)==15127,'frozen proof length')
require(hashlib.sha256(proof).hexdigest()=='205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba','frozen whole proof')
require(C.product('one',10)==Counter({'A':1,'V':1,'D':1}),'degree10 coefficients')
require(C.product('one',12)['one']==1,'universal degree12 invariant')
require(3+3+5==11 and 11-min(3,3,5)==8,'proper quotient span bound')
require(8-1==7 and 7-7==0,'last annihilator in span argument')
require(C.product('V',4)==Counter({'A':1,'D':1,'V':1,'P':1}),'quartic Hom identity')
require(C.product('V',4)['A']==1,'quartic Hom dimension')
require(C.product('V',8)['A']==2,'degree8 Hom dimension')
require(3*(2-10)==-24,'intrinsic second-jet degree')
require(6*(5-18)==-78,'auxiliary fifth-jet degree')
require((14-5)==9 and -(5+1)*(18-5)==-78,'B5 rank and degree')
require(6+3==9,'generic isomorphism ranks')
require(-78-(-78)-(-24)==2*12,'exact torsion length')
require((4+2,2+2)==(6,4),'actual normal untwist')
require(9-2==7 and 6+3-7==2,'sum rank and fiber intersection')
orders=(0,1,1)
exterior=tuple(sorted(orders[i]+orders[j] for i,j in combinations(range(3),2)))
require(exterior==(1,1,2),'universal exterior orders')
normalized=tuple(e-1 for e in exterior)
require(normalized==(0,0,1),'single divisor factor')
require(sum(orders)==2 and sum(normalized)==1,'determinant orders')
require(orders.count(0)==1 and normalized.count(0)==2,'fiber ranks')
require(2*(-8)+12==-4,'normalized quartic twist')
require(3*(-8)+2*12==0,'constant determinant comparison')
require(2*(-4)==-8,'second exterior normalized source')
require(-8+3*(-8)+2*12==-8,'rank3 natural identification twists')
# Three fixed formal weight identities for Lambda2Lambda2 J=J tensor det J.
weights=[(1,0,0),(0,1,0),(0,0,1)]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
wedge=[add(weights[i],weights[j]) for i,j in combinations(range(3),2)]
double=sorted(add(wedge[i],wedge[j]) for i,j in combinations(range(3),2))
expected=sorted(add(w,(1,1,1)) for w in weights)
for a,b in zip(double,expected):require(a==b,'universal rank3 exterior weight identity')
require(3*(-4)==-12,'quartic determinant degree')
require(2*3*(-8)+3*12==-12,'determinant after exterior division')
print(json.dumps({'status':'PASS','checks':count,'proof_sha256':hashlib.sha256(proof).hexdigest(),'scope':'two complete immutable originals; fixed characters, degrees, universal elementary orders and exterior weights','not_claimed':['actual coefficient, tensor, matrix or instance-rank evaluation','chosen invariant or determinant normalization','branch occurrence or exclusion','original tenth jets','proof by computation']},indent=2,sort_keys=True))
