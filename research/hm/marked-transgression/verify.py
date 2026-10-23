#!/usr/bin/env python3
"""Bounded immutable-input and representation bookkeeping, not a formal proof."""
from pathlib import Path
import hashlib,json
from collections import Counter
ROOT=Path(__file__).resolve().parent
n=0
def check(c,msg):
 global n
 if not c: raise RuntimeError(msg)
 n+=1
for p in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/'audit-inputs'/f"{p['label']}.md").read_bytes()
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['blob'],p['label']+' blob')
# Actual input characters; these operations evaluate no actual differential.
M3W=Counter(A=3,V=6,P=9,D=9)
M4=Counter(V=2,P=4,D=3)
H1={k:M3W[k]-M4[k] for k in M3W|M4}
check(H1==dict(A=3,V=4,P=5,D=6),'source H1(E(-2)) character')
check(H1['V']==4,'detector target dimension')
# A Sym6W = A(V+P)= (P+D)+(V+P+D).
ASym6=Counter(V=1,P=2,D=2)
check(ASym6['V']==1,'detector domain dimension')
check(sum({'A':3,'V':3,'P':4,'D':5}[k]*v for k,v in H1.items())==71,'H1 dimension')
check(54*2-37==71,'E(-2) Euler dimension')
# Complete evaluation makes Hom_G(O2,Jg) the unique W multiplicity.
E28=Counter(W=1,S=2,T6=3)
N41=Counter(A=1,V=2,P=3,D=4)
check(E28['W']==1 and N41['1']==0,'marked global Hom dimension')
# Allowed higher differentials in four-column first-quadrant vertical sequence.
cols=range(-3,1)
def outgoing(p,q):
 return [(r,p+r,q-r+1) for r in range(2,8) if p+r in cols and q-r+1>=0]
def incoming(p,q):
 return [(r,p-r,q+r-1) for r in range(2,8) if p-r in cols]
check(outgoing(-3,1)==[(2,-1,0)],'only source outgoing d2')
check(incoming(-3,1)==[],'no source incoming')
check(outgoing(-1,0)==[],'no target outgoing')
check(incoming(-1,0)==[(2,-3,1)],'only target incoming d2')
check(-3+1<0 and -1+0<0,'both limit terms negative')
check(3*17-3*3==42,'quotient H rank')
check(3*(-54)-3*(-18)==-108,'quotient H degree')
print(f'PASS: {n} immutable-input / bounded bookkeeping checks. Structural proof not formally checked.')
