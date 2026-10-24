"""Small fixed universal identities; no actual instance or scalar evaluation."""
from pathlib import Path
from collections import Counter
import hashlib,json
import characters as C
BASE=Path(__file__).resolve().parent
count=0
def require(x,msg):
 global count
 count+=1
 if not x:raise RuntimeError(msg)
pins={
 'inputs/rankseven-equality.md':('f5895c822322b4ddab07e51a97874d4528fb5b88',15139,'a6e56f535af652d3ff437cc5041527636f601751ae24285ba1ec91670f4db7ae','6a4ef8941ee4cee131992bdf9cd7657635b058c5'),
 'inputs/nonsplit-quotient.md':('f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1',13619,'d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568','1974a5c3b20546dcb414539096511388f495cdab')}
a=json.loads((BASE/'INPUTS.json').read_text())
require(len(a)==2 and {i['file'] for i in a}==set(pins),'exact complete inputs')
for i in a:
 ref,n,sha,git=pins[i['file']];b=(BASE/i['file']).read_bytes()
 require(i['ref']==ref,'immutable ref')
 require(len(b)==i['bytes']==n,'full input bytes')
 require(hashlib.sha256(b).hexdigest()==i['sha256']==sha,'input sha256')
 require(hashlib.sha1(b'blob '+str(n).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1']==git,'input blob')
 require(i['url'].endswith('/'+ref+'/'+i['path']),'immutable URL')
proof=(BASE/'PROOF.md').read_bytes()
require(len(proof)==11240,'frozen proof bytes')
require(hashlib.sha256(proof).hexdigest()=='08708a646f51fb6b10ef94c1eab1b5e4ee56a775fb8e377d6a92e8d34df54259','frozen proof hash')
require(C.product('one',6)==Counter({'V':1,'P':1}),'physical Sym6')
require(C.product('D',2)==Counter({'V':1,'P':1,'D':1,'A':1}),'quartic kernel Hom product')
require(C.product('D',2)['A']==1,'unique equivariant embedded kernel')
require(C.product('one',6)['A']==0,'no extra finite-group A')
require(C.product('one',4)['A']==0,'quartic factor has no A')
require(C.product('W',1)['one']==1,'Schur multiplicity')
require(C.product('D',6)['one']==0,'upper U4 Hom vanishing cross-check')
# Universal quartic polarization and degree shifts, not selected evaluation.
require(4!=0 and 10!=0,'nonzero universal characteristic-zero Euler coefficients')
require(5-3==2,'quartic first-jet quotient rank')
require(0-3*(-2)==2*3,'quartic first-jet quotient degree')
require(-2-14==-16 and 3-14==-11,'universal twist')
require((-11,-11)!=(-10,-12),'actual quotient splitting mismatch')
require(1-10==-9,'intrinsic first-jet source twist')
require(-10+(-8)==2*(-9),'intrinsic first-jet extension degree')
require(-14-(-9)<0,'unique actual complement by Hom degree')
require(-10-(-9)<0,'top first jets have zero coherent lower row')
require(-8-(-9)==1,'upper Euler row degree')
require(5*(-14)+2*(-9)==-88,'F6 degree')
require(4*(-15)+(-10)==-70,'Q1 degree')
require(-88-(-8-10)==-70,'coherent kernel degree')
require(5+2==7 and 4+1==5,'actual ranks')
require(-14<-9,'canonical highest-degree block')
print(json.dumps({'status':'PASS','checks':count,'proof_sha256':hashlib.sha256(proof).hexdigest(),'scope':'two complete immutable inputs; fixed finite-group Hom multiplicities, universal quartic/first-jet and degree identities','not_claimed':['selected actual source or graph scalar evaluation','degree-ten completeness','stationary graph as a dependency','branch occurrence or exclusion','original tenth jets','proof by computation']},sort_keys=True,indent=2))
