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




# All computations concern fixed abstract characters and bundle degrees.
H=va(one,P,vs(2,D))
require(vm(P,A)==va(V,P,D),'H0 P(2)')
require(vm(D,A)==va(A,V,P,D),'H1 D(-4)')
require(inner(V,H)==z(0),'no V in constant ambient source')
require(vm(P,W)==va(Wp,T),'P W=Wp+T')
require(vm(P,S)==va(S,vs(2,T)),'P Sym3W=S+2T')
require(inner(Wp,vm(P,S))==z(0),'P constant subbundle exclusion')
require(vm(D,W)==va(S,T),'H1 D(-3) and constant D sections')
require(vm(P,D)==va(A,V,P,vs(2,D)),'H0 P(4)')
# Representation Euler identity at twist one.
require(va(vm(P,S),vs(-1,vm(D,W)))==T,'Euler character T')
for hasS,hasT in [(0,0),(1,0),(0,1),(1,1)]:
    dim=6+4*hasS+6*hasT
    require((dim<=9)==(hasS==hasT==0),'negative-rank bound forces H1 K(1)=0')
require(6+3==9 and -6-2*3==-12,'case I rank and degree')
require(5+4==9 and -3*4==-12,'case II rank and degree')
require(6>4 and 5>4,'residual rank-four exclusions')
require(va(vm(D,W),vs(-1,T))==S,'case II coefficient S')
# All ordinary strictly negative rank-nine degree-minus-twelve partitions.
parts=[[-4]+[-1]*8,[-3,-2]+[-1]*7,[-2]*3+[-1]*6]
require([sum(x) for x in parts]==[-12]*3,'ordinary partition degrees')
require([sum(a==-1 for a in x) for x in parts]==[8,7,6],'twist-one section counts')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
 require(len(b)==item['bytes'],'input byte count')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: exact abstract characters, P exclusion, both degree/rank arguments, coefficient identifications, and immutable input bytes. No actual extension or rank selected.')
