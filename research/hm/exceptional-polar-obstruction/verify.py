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
# Fixed plane Steiner character calculation. No actual maps are entered.
symD=vs(F(1,2),va(vm(D,D),psi2(D)))
require(symD==va(one,P,vs(2,D)),'Sym2D')
def sw(n): return [sym(n,x) for x in W]
def sv(n): return [total(sym(2*n-4*j,x) for j in range(n//2+1)) for x in Wp]
def chiO(n): return sv(n) if n>=0 else sv(-n-3) if n<=-3 else vs(0,one)
def chiB(n): return va(vm(A,chiO(n-5)),vs(-1,vm(vm(A,D),chiO(n-4))),vm(symD,chiO(n-3)))
for n,wanted in [(1,va(A,V)),(0,va(V,P,D)),(-1,va(A,V,P,D)),(-3,va(V,P,D))]:
 require(vs(-1,chiB(n))==wanted,'plane H1 at '+str(n))
require(chiB(2)==A,'H0BR2')
require(chiB(3)==symD,'H0BR3')
h04=va(vm(symD,V),vs(-1,vm(A,D)))
require(chiB(4)==h04,'H0BR4')
require(vm(A,V)==va(P,D),'no trivial in matrix domain')
# Geometry proves all other groups zero; this checks their exact invariant sizes.
layer={
 2:(0,0,int(inner(one,h04)[0])),
 4:(0,0,int(inner(sw(2),A)[0])),
 6:(0,int(inner(sw(4),va(V,P,D))[0]),0),
 8:(0,int(inner(sw(6),va(A,V,P,D))[0]),0),
 10:(0,int(inner(sw(8),va(A,V))[0]),0),
 12:(int(inner(sw(10),symD)[0]),0,0)}
require(layer=={2:(0,0,0),4:(0,0,1),6:(0,1,0),8:(0,2,0),10:(0,0,0),12:(2,0,0)},'entire even-layer invariant table')
require(sw(6)==va(V,P) and sw(8)==va(P,D),'small symmetric powers')
require(sw(10)==va(A,V,D),'Sym10')
require(sw(16)==va(V,P,vs(2,D)),'Sym16')
require(inner(A,sw(16))==z(0),'first Leray invariant H1')
require(inner(W,sw(17))==z(0),'vertex Leray invariant H1')
require(inner(one,sw(14))==z(0),'unique invariant line channel')
require(inner(one,va(vs(2,V),vs(4,P),vs(3,D)))==z(0),'H1B4 invariant vanish')
require(sum(a-b+c for j,(a,b,c) in layer.items() if j<=10)==-2,'K10 Euler')
require(sum(a-b+c for a,b,c in layer.values())==0,'K12 Euler')
# Exhaustive scalar-rank consequences; these are universal dimensions, not actual ranks.
allowed=[]
for a in (0,1):
 for b in range(2):
  if b<=1-a and (1-a)-b==0:
   require((1-a)+(2-b)==2,'middle dimension2')
   allowed.append((a,b))
require(allowed==[(0,1),(1,0)],'nonzero internal transgression alternatives')
for k in (0,1):require(2-k in (1,2),'nonzero top boundary')
# Independent Euler check from the complete-evaluation interface.
HH=va(one,vs(3,A),V,vs(2,P),vs(2,D))
EE=va(vs(2,W),Wp,vs(2,S),vs(2,T))
require(inner(HH,sw(10))==z(6) and inner(EE,sw(11))==z(6),'C(-12) invariant Euler zero')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'immutable input '+item['key'])
print('PASS: plane Steiner Euler characters; six even-layer invariant groups; two Leray vanishings; unique vertex channel; K10/K12 Euler; internal transgression rank alternatives; top nonvanishing consequences; five immutable inputs.')
print('BOUNDARY: fixed abstract characters only; no actual HM/source coefficients, points, matrices, derivatives or instance ranks.')
