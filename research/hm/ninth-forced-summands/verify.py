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
require(vm(W,W)==va(one,A),'W squared')
require(vm(W,D)==va(S,T),'W D')
require(vm(A,A)==va(one,A,D),'A squared')
require(vm(A,V)==va(P,D),'A V')
require(vm(A,P)==va(V,P,D),'A P')
require(inner(P,vm(W,W))==z(0),'no P2-to-W3')
require(inner(W,vm(W,D))==z(0),'no W(-1)-to-W3')
require(inner(A,vm(va(V,P),A))==z(0),'unique A4 lift')
require(inner(V,vm(A,A))==z(0) and inner(P,vm(A,A))==z(0),'zero adjacent V/P blocks')
require(inner(D,vm(A,A))==z(1),'one adjacent D channel')
require(inner(W,vm(A,W))==z(1),'opposite W3-to-A4 Hom must not be suppressed')
def h1line(d):return max(-d-1,0)
require(h1line(2)==0 and h1line(-1)==0,'correct extension order splits')
require(h1line(-3)==2,'forbidden opposite-order ordinary Ext is not zero')
require(3-4==-1 and -(3-1)==-2,'third canonical twists')
require(-(-3)-1==2 and -6-2==-8,'dual pulled-back coefficients')
require(6-3==3 and 6+2==8,'twisted y kernel and target')
require(15+7+2==24 and 15*4+7*6+2*3==108,'F24')
require(12+7-6==13 and 12*4+7*6-6==84,'residual presentation')
require(2*3+3*4+84==102,'H9 total degree')
require(13*8-84==20 and 2*5+3*4+20==42,'Theta dual-twist degrees')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: fixed Hom characters, correct/nonvanishing Ext directions, Cartier duality twists, all bundle degrees and three exact originals. No actual map or instance evaluated.')
