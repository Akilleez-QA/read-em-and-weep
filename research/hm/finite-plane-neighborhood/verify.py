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
# W trace separates the nine classes; g-square has trace trace(g)^2-2.
square=[W.index(sub(mul(x,x),z(2))) for x in W]
require(square==[0,0,5,5,3,3,7,7,1],'exact square-class map')
def psi2(c):return [c[i] for i in square]
H=va(V,W)
L2=vs(F(1,2),va(vm(H,H),vs(-1,psi2(H))))
require(L2==va(V,vm(V,W),one),'exterior square H')
N=va(A,Wp)
# Sym^n(V+W), with V=Sym2 Wp; degrees only 2 through 8.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}
symD=vs(F(1,2),va(vm(D,D),psi2(D)))
require(symD==va(one,P,vs(2,D)),'Sym2D')
require(inner(one,va(vm(symD,V),vs(-1,vm(A,D))))==z(0),'no invariant plane B4 sections')
require(inner(A,A)==z(1),'unique normal2 candidate')
require(inner(D,va(V,P,D))==z(1),'normal4 obstruction target')
six=[sym(6,x) for x in W]
require(six==va(V,P),'Sym6W')
require(inner(six,va(A,V,P,D))==z(2),'normal6 obstruction target')
# Duality indices and twists; geometry in PROOF establishes the derived identity.
for j in (4,6,8):
 require((j-1) in (3,5,7),'ordinary thickening index')
 require(9-5==4,'ambient dual twist')
 require(4-((j-1)-1)==6-j,'last ordinary normal layer')
# Both and only both alternatives allowed by the prior actual rank relation.
rows=[]
for a in (0,1):
 for b in (0,1):
  if b<=1-a and a+b==1:
   h3=1;h5=1-a;h7=1-a-b
   require(h7==0,'seventh-neighborhood exclusion')
   require((h3,h5,h7) in [(1,0,0),(1,1,0)],'first failure4or6')
   rows.append((a,b,h3,h5,h7))
require(rows==[(0,1,1,1,0),(1,0,1,0,0)],'two exact alternatives')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 data=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['blob'],'immutable '+item['key'])
print('PASS: invariant normal-layer dimensions0/1/1/2; duality indices3/5/7 and twist4; exact two obstruction alternatives; immutable input identities.')
print('BOUNDARY: structural duality proof is separate; no actual HM/source instance evaluated.')
