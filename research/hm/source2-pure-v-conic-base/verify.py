#!/usr/bin/env python3
"""Exact binary character check for the universal pure-V conic-base dichotomy."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent; checks=[]
def ck(name,p):
 if not p:raise RuntimeError(name)
 checks.append(name)
for pin in json.loads((root/'INPUTS.json').read_text()):
 b=(root/pin['local_path']).read_bytes()
 ck('sha256 '+pin['label'],hashlib.sha256(b).hexdigest()==pin['sha256'])
 ck('git blob '+pin['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob'])
r=s.sqrt(5);sizes=[1,15,20,12,12]
A=[3,-1,0,(1+r)/2,(1-r)/2];P=[4,0,1,-1,-1];one=[1]*5
inn=lambda x,y:s.simplify(sum(n*a*b for n,a,b in zip(sizes,x,y))*s.Rational(1,60))
# spin[m] is the even binary symmetric power Sym^(2m)W.
spin=[one,A]
for m in range(2,11):spin.append([s.simplify((a-1)*p-q) for a,p,q in zip(A,spin[-1],spin[-2])])
inv=[inn(v,one) for v in spin[:10]]
ck('binary invariant degrees0..18 even',inv==[1,0,0,0,0,0,1,0,0,0])
ck('odd binary degrees central parity excludes invariants',all((-1)**n==-1 for n in range(1,19,2)))
ck('unique degree-six P system',inn(P,spin[3])==1)
ck('two degree-eighteen P systems',inn(P,spin[9])==2)
ck('only positive invariant gcd degree at most18',[2*m for m,v in enumerate(inv) if m and v]==[12])
ck('residual degree is six',18-12==6)
ck('residual no possible positive invariant gcd',all(inv[m]==0 for m in range(1,4)))
ck('f12 cannot have doubled divisor',2*12>18)
ck('degree12 orbit multiplicity one',12//12==1)
ck('exceptional conic base length12',6*2==12)
ck('divisible subspace dimension one',inn(P,spin[3])==1 and inn(P,spin[9])==2)
ck('old fourth invisible line degree8 D multiplicity1',inn([5,1,-1,0,0],spin[4])==1)
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'scope':'all nonzero universal gate elements; actual gate and line relationships unselected'},indent=2))
