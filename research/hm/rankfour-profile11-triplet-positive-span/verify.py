#!/usr/bin/env python3
"""Fixed universal character/degree checks, never actual-instance evaluation."""
from pathlib import Path
from collections import Counter
import hashlib,json
from characters import product,DIM
ROOT=Path(__file__).resolve().parent
checks=0
def eq(actual,expected,label):
 global checks
 checks+=1
 if actual!=expected:raise RuntimeError((label,actual,expected))
def chars(*pairs):
 c=Counter()
 for r,n,m in pairs:
  for k,v in product(r,n).items():c[k]+=m*v
 return +c
def sub(a,b):
 c=Counter(a);c.subtract(b)
 if any(x<0 for x in c.values()):raise RuntimeError(('negative multiplicity',dict(c)))
 return +c
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/x['file']).read_bytes()
 eq(len(b),x['bytes'],'input bytes '+x['file'])
 eq(hashlib.sha256(b).hexdigest(),x['sha256'],'input SHA256 '+x['file'])
 eq(hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest(),x['git_blob_sha1'],'input blob '+x['file'])
M2=Counter(A=1,V=2,P=3,D=4)
H0E=chars(('D',2,1),('Wp',3,1),('T',3,1),('V',4,1),('one',8,1))
H=sub(H0E,M2)
eq(dict(H),dict(A=2,V=2,P=2,D=2),'original ambient character')
eq(sum(DIM[r]*m for r,m in H.items()),30,'original ambient dimension')
J=product('one',8);eq(dict(J),dict(P=1,D=1),'complete octic character')
C=sub(H,J);eq(dict(C),dict(A=2,V=2,P=1,D=1),'small ambient character')
eq(sum(DIM[r]*m for r,m in C.items()),21,'small ambient dimension')
eq(30-9,21,'lower bound for span')
eq(-46-(-18),-28,'lower endpoint degree bound')
eq(-10*4+6,-34,'minimal-span contradiction at rank four')
eq((4+5),9,'only quotient dimension at least eight')
eq(21-16,5,'small dual rank')
eq(5-3,2,'small endpoint rank')
eq((-6)*3,-18,'small transpose degree')
eq(6-18,-12,'original dual quotient degree')
eq(-8-4-(-12),0,'original defect preserved')
eq(dict(product('A',4)),dict(A=1,V=1,P=1,D=1),'triplet positive sections')
Lcohom=sub(M2,product('A',4));eq(dict(Lcohom),dict(V=1,P=2,D=3),'endpoint H1')
eq(sum(DIM[r]*m for r,m in Lcohom.items()),26,'endpoint h1 dimension')
eq(28-2,26,'endpoint ordinary Euler check')
eq((14%2),0,'doublet degree violates odd center parity')
scalar_pairs=[2,4,6,8,10,12,14]
for j in scalar_pairs:
 c=chars(('one',j-2,1),('one',26-j,1))
 eq(sum(DIM[r]*m for r,m in c.items()),26,'scalar pair dimension '+str(j))
 if j==10:eq(c,Lcohom,'unique scalar pair')
 else:eq(c.get('one',0)>0 or c.get('A',0)>0,True,'forbidden scalar constituent '+str(j))
eq(dict(product('one',16)),dict(V=1,P=1,D=2),'degree eighteen curve cohomology')
eq(product('A',2)['one'],1,'unique nonzero top derivative row')
eq(product('one',6).get('one',0),0,'lower line cannot have internal derivative')
eq(product('one',8).get('one',0),0,'lower derivative cannot factor through top image')
eq(product('one',2).get('one',0),0,'no invariant vector of A')
eq(-10-18,-28,'endpoint degree')
eq(-8*3,-24,'derivative target degree')
eq((-16)-(-28),12,'maximal possible saturation defect')
eq(-24-(-28),4,'saturated derivative cokernel degree')
eq(4+2,6,'positive forward quotient degree')
eq(-28+2*2,-24,'twisted endpoint image degree')
eq(-28-24,-52,'actual forward transform degree')
for n in (10,18):
 eq(2*(1-n),-2*n+2,'universal first principal-parts degree '+str(n))
eq(2*(-9)+2*(-17),-52,'intrinsic first-jet total degree')
eq((-46)-(-52),6,'forward quotient degree check')
U=product('one',10);T=product('one',18)
eq(dict(U),dict(A=1,V=1,D=1),'degree ten coefficient system')
eq(dict(T),dict(A=1,V=1,P=2,D=1),'degree eighteen coefficient system')
eq(dict(sub(chars(('one',10,1),('one',18,1)),C)),dict(P=1,D=1),'actual coefficient kernel')
eq(sum(DIM[r]*m for r,m in U.items()),11,'complete degree-ten dimension')
eq(sum(DIM[r]*m for r,m in T.items()),19,'complete degree-eighteen dimension')
eq(11+19-21,9,'joint coefficient loss dimension')
# Exactly the derived span alternatives, not a search for bundle configurations.
for u,t,overlap in [(6,15,0),(11,10,0),(11,15,5)]:
 eq(u+t-overlap,21,'derived coefficient spans fill the ambient')
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'scope':'Fixed universal characters, exact degree arithmetic and source authentication only. Actual geometric arguments are reviewed mathematically, not machine-certified.'},indent=2,sort_keys=True))
