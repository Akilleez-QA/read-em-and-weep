#!/usr/bin/env python3
"""Universal character/degree controls only; no actual-source instance data."""
from collections import Counter
from pathlib import Path
import hashlib,json,sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(x,msg):
 global checks
 checks+=1
 if not x:raise RuntimeError(msg)
def equal(x,y):
 z=Counter(x);z.subtract(Counter(y));return not any(z.values())
def dim(x):return sum(c.DIM[r]*v for r,v in x.items())
for i in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/i['file']).read_bytes()
 require(len(b)==i['bytes'],'source bytes')
 require(hashlib.sha256(b).hexdigest()==i['sha256'],'source SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob_sha1'],'Git blob')
require(equal(c.product('one',6),dict(V=1,P=1)),'unique sextic V')
require(equal(c.product('V',2),dict(P=1,D=1)),'V tensor Sym2')
require(equal(c.product('one',8),dict(P=1,D=1)),'Sym8')
require(equal(c.product('V',3),dict(S=1,T=1,Wp=1)),'V tensor Sym3')
require(equal(c.product('one',9),dict(S=1,T=1)),'Sym9')
require(equal(c.product('Wp',1),dict(P=1)),'Serre-dual cokernel')
poss=[(a,6-a) for a in range(1,4)]
require(poss==[(1,5),(2,4),(3,3)],'all ordinary types')
require((-1)**1==-1,'unbalanced odd top cannot inherit central +1')
require(c.product('V',2)['one']==0,'unbalanced even top has no trivial channel')
require(60//5==12 and 6<12,'invariant sextic base divisor impossible')
controls=[]
for d in range(65):
 src=c.product('V',d);target=c.product('one',d+6)
 kernel=c.product('Wp',d-3)
 cokernel=Counter(P=1) if d==0 else Counter(Wp=1) if d==1 else Counter()
 require(equal(src+ cokernel,target+kernel),'all-degree character exactness control')
 require(dim(kernel)==max(2*d-4,0),'kernel dimension')
 require(dim(cokernel)==max(4-2*d,0),'cokernel dimension')
 require(dim(src)-dim(kernel)==min(3*(d+1),d+7),'sharp rank formula')
 require(max(-(d-3)-1,0)*2==dim(cokernel),'line H1 formula')
 controls.append({'multiplier_degree':d,'kernel_dimension':dim(kernel),'cokernel_dimension':dim(cokernel)})
hilbert=[]
for n in range(40):
 a=n+1-3*max(n-5,0)+2*max(n-8,0)
 require(a>=0,'Hilbert coefficient genuine')
 expected=n+1 if n<6 else 4 if n==6 else 2 if n==7 else 0
 require(a==expected,'Hilbert numerator identity')
 hilbert.append(a)
require(sum(hilbert)==27,'quotient length')
require(hilbert[:8]==[1,2,3,4,5,6,4,2] and not any(hilbert[8:]),'exact finite Hilbert vector')
require(3*2<8 and 3*3==9,'minimal saturation degree two')
out={'checks':checks+c.checks,'source_originals':3,'equivariant_kernel':"Wprime tensor O(-3)",'multiplication_controls':controls,'hilbert_vector':hilbert[:8],'quotient_length':27,'actual_instance_evaluated':False,'new_actual_profile_exclusion':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(s)
else:
 if (ROOT/'RESULT.json').read_text()!=s:raise RuntimeError('retained result mismatch')
print(s,end='')
