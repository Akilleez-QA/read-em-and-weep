#!/usr/bin/env python3
"""Fixed abstract character checks only; no actual HM/source evaluation."""
from fractions import Fraction as R
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
EXPECTED={'ACTUAL.md': 'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3', 'FULL-MODULE.md': '2ba0a7eee6ef2eb5413683e85618d7902dca3970', 'ALGEBRA.md': '83f5aee293995257459229e6b323522224ce8f3d', 'NEGATIVE-SQUARE.md': 'bdcb7d5b14f7477bcd616e0e682fa5f45e250a5d'}

def require(condition,message):
    if not condition: raise RuntimeError(message)

entries=json.loads((ROOT/'audit-inputs/manifest.json').read_text())
require(len(entries)==4,'Four immutable inputs required')
require({e['name']:e['git_blob'] for e in entries}==EXPECTED,'Manifest mismatch')
for e in entries:
    data=(ROOT/'audit-inputs'/e['name']).read_bytes()
    blob=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob==e['git_blob'],'Input blob mismatch: '+e['name'])

# A pair (a,b) denotes a+b sqrt(5), with rational a,b.
def f(a=0, b=0): return (R(a), R(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def va(x,y): return tuple(add(a,b) for a,b in zip(x,y))
def vm(x,y): return tuple(mul(a,b) for a,b in zip(x,y))
def vk(k,x): return tuple(scale(k,a) for a in x)
def vs(x,y): return va(x,vk(-1,y))
ZERO=(f(),)*9
ONE=(f(1),)*9
phi=f(R(1,2),R(1,2));phip=f(R(1,2),-R(1,2))
W=(f(2),f(-2),phi,scale(-1,phi),phip,scale(-1,phip),f(1),f(-1),f(0))
SIZES=(1,1,12,12,12,12,20,20,30)


@lru_cache(None)
def sym(n):
    require(n>=0,"Negative symmetric-power index")
    if n==0:return ONE
    a,b=ONE,W
    for _ in range(2,n+1):a,b=b,vs(vm(W,b),a)
    return b


C={"one":ONE,"W":W,"A":sym(2),"S":sym(3),"D":sym(4),"T":sym(5)}
C["P"]=tuple(f(a) for a in (4,4,-1,-1,-1,-1,1,1,0))
C["V"]=vs(sym(6),C["P"])
C["Wp"]=vs(vm(C["P"],W),C["T"])


def inner(x,y):
    out=f()
    for size,a,b in zip(SIZES,x,y):out=add(out,scale(R(size,120),mul(a,b)))
    return out


for a in C:
    for b in C:require(inner(C[a],C[b])==f(int(a==b)),"Character orthogonality")


def rep(**terms):
    out=ZERO
    for name,n in terms.items():out=va(out,vk(n,C[name]))
    return out



# Orthogonality and the sum of squared dimensions certify completeness of
# this fixed nine-character list; no source parameter is involved.
dims={name:int(char[0][0]) for name,char in C.items()}
require(sum(d*d for d in dims.values())==120,'Complete dimension sum')
even=[name for name,char in C.items() if char[1]==char[0]]
require(set(even)=={'one','A','V','P','D'},'Center-even list')
# The only center-even representations of dimension three are 1^3,A,V.
possible=[]
for n1 in range(4):
    for na in range(2):
        for nv in range(2):
            if n1+3*na+3*nv==3: possible.append((n1,na,nv))
require(set(possible)=={(3,0,0),(0,1,0),(0,0,1)},'Positive three-space alternatives')
for name in ('A','V'):
    require(inner(vm(C[name],C[name]),ONE)==f(1),'Invariant bilinear form')
    require(dims[name]==3,'Odd dimension for symmetric-form proof')
# Symmetry of these invariant forms is proved in the text, not guessed
# from the tensor-square character alone.
XF=rep(V=1,P=1,D=2)
XB=rep(A=1,V=1,P=2,D=2)
YF=rep(P=1,D=1)
YB=rep(V=1,P=2,D=2)
Pi=rep(V=1,P=1)
for X in (XF,XB):
    require(inner(X,C['V'])[0]>=1 and inner(X,C['P'])[0]>=1,
            'An abstract surjection to V+P must exist')
require([int(X[0][0]) for X in (XF,XB,YF,YB,Pi)]==[17,24,9,21,7],
        'Block dimensions')
require(int(va(YF,YB)[0][0])==30 and 30+7==37,'Aggregate target split')
require(inner(Pi,C['P'])==f(1) and inner(YF,C['P'])==f(1),'Unique radical P channel')
require(inner(C['V'],C['P'])==f(0),'Distinct quotient constituents')
print('PASS: four immutable blobs; complete fixed character list; all three positive-space cases;')
print('invariant-form and abstract projection prerequisites; fixed block/radical characters.')
print('The written proof and review establish symmetry, exact compatibility criteria, and formal sharpness.')
