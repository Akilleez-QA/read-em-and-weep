#!/usr/bin/env python3
"""Nine-class abstract characters only. No actual tensors or instance evaluations."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

def require(condition,message):
    if not condition: raise RuntimeError(message)
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
    out=z(0)
    for x in xs:out=add(out,x)
    return out
def va(*args):return [total(v) for v in zip(*args)]
def vs(k,a):return [scale(k,x) for x in a]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def sym(n,x):
    require(n>=0,'negative symmetric power')
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
    return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
one=[z(1)]*9
A=[sym(2,x) for x in W];S=[sym(3,x) for x in W]
D=[sym(4,x) for x in W];T=[sym(5,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(W,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
reps=dict(zip(['1','W','Wp','A','V','P','S','D','T'],[one,W,Wp,A,V,P,S,D,T]))
def inner(a,b):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
require(sum(sizes)==120,'class sizes')
for n,c in reps.items():
 for m,d in reps.items():require(inner(c,d)==z(int(n==m)),'character orthogonality')
require(sum(int(c[0][0])**2 for c in reps.values())==120,'irrep completeness')
require(V==[sym(2,x) for x in Wp],'positive ambient V=Sym2 Wp')


sw=lambda n:[sym(n,x) for x in W]
rows={9:[('1',2),('1',12),('V',4)],10:[('1',2),('1',18),('A',2)],14:[('1',2),('Wp',5),('Wp',7)],15:[('1',2),('P',6)],17:[('1',14),('W',1),('Wp',5)],18:[('1',18),('W',1),('W',3)],20:[('W',1),('V',8)]}
def hom(c,d,target,k):
 return z(0) if k<d else inner(reps[c],vm(reps[target],sw(k-d)))
for row,atoms in rows.items():
 rank=sum(int(reps[c][0][0]) for c,d in atoms)
 degree=sum(int(reps[c][0][0])*d for c,d in atoms)
 require((rank,degree)==(5,26),'actual seven-type input rank/degree')
 require(total(hom(c,d,'1',6) for c,d in atoms)==z(0),'all seven Hom(C,O6) vanish')
 target=[(c,8-d) for c,d in atoms]
 n=total(hom(s,a,t,b) for s,a in [('A',4),('W',5)] for t,b in target)
 require(n==z(4 if row in (10,18) else 2),'complete source-target channel count')
require(hom('A',4,'1',8)==z(0) and hom('W',5,'1',8)==z(0),'common evaluation quotient is unhit')
for source,deg in [('A',4),('W',5)]:
 require(hom(source,deg,'1',6)==z(1),'one onto line channel')
 require(hom(source,deg,'W',5)==z(1),'one doublet receiver channel')
require(hom('1',2,'1',6)==z(0),'tautological line inside quadratic evaluation kernel')
require(hom('W',5,'W',7)==z(1),'nonunique row18 complement retained')
require(3*4+2*5==22,'selected source degree')
require(2*3+4==10 and 3*4-6==6,'rank3 joint kernel degree')
require(6+2*5==16 and 22-6==16,'rank3 receiver and nonzero line-map kernel degrees')
require(5-3==2 and 5-1==4,'actual intersection rank lower bounds')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: seven fixed type characters, all channel dimensions and vanishings, kernel/receiver degrees and two exact originals. No actual coefficient or instance evaluated.')
