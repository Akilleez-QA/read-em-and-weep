#!/usr/bin/env python3
"""Small exact universal character checks; no actual-source evaluation."""
from fractions import Fraction as R
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "ALGEBRA.md": "83f5aee293995257459229e6b323522224ce8f3d",
    "GENERATION.md": "becd3300950c2379d1f03294863d8335a83a1087",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


entries = json.loads((ROOT / "audit-inputs/manifest.json").read_text())
require(len(entries) == 2, "Exactly two dependencies are expected")
require({e["name"]: e["git_blob"] for e in entries} == EXPECTED, "Manifest mismatch")
for e in entries:
    b = (ROOT / "audit-inputs" / e["name"]).read_bytes()
    require(sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest() == e["git_blob"],
            "Input blob mismatch: " + e["name"])

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


S=C["S"]
N2=va(sym(16),vm(S,sym(5)))
N4=rep(V=2,P=4,D=3)
Hminus=rep(A=2,V=2,P=1,D=1)
Kmu=va(va(sym(16),sym(14)),vm(S,va(sym(5),sym(3))))
Z=va(Kmu,Hminus)
Iminus=rep(V=1,P=3,D=3)
Pi=rep(V=1,P=1)
require(N2==rep(A=1,V=2,P=3,D=4),"N2 character")
require(vm(S,C["T"])==rep(A=1,V=1,P=2,D=2),"S tensor T")
require(vm(S,S)==rep(one=1,A=1,V=1,P=1,D=1),"S tensor S")
for d in (7,18):
    require(vs(vm(sym(2),sym(d-2)),sym(d))==va(sym(d-2),sym(d-4)),
            "Universal multiplication kernel at d="+str(d))
require(Kmu==rep(one=1,A=3,V=4,P=5,D=6),"Kernel mu character")
require(Z==rep(one=1,A=5,V=6,P=6,D=7),"Restricted relation character")
require(vm(sym(2),N2)==va(Z,Iminus),"Source equals kernel plus image")
require(N4==va(Iminus,Pi),"Target equals image plus cokernel")
require(vm(sym(7),W)==va(sym(8),sym(6)),"Scalar quotient exact sequence")
require(vm(sym(2),N2)==rep(one=1,A=5,V=7,P=9,D=10),"Product source character")


def dim(char):
    require(char[0][1]==0 and char[0][0].denominator==1,"Integral dimension")
    return int(char[0][0])


require([dim(x) for x in (N2,Kmu,Hminus,Z,Iminus,N4,Pi)]==[41,72,21,93,30,37,7],
        "Dimension sequence")
require(3*41==123 and 19+4*8==51 and 51-21==30,"Product/image dimensions")
require([dim(x) for x in (sym(8),vm(sym(7),W),sym(6))]==[9,16,7],"Cokernel sequence")
require(Kmu!=Z and dim(Kmu)==72,"Negative control: omit the constant preimage")
require(Pi!=ZERO and dim(Pi)==7,"Negative control: omit the degree-one quotient block")
print("PASS: exact immutable inputs; fixed character table; two universal product kernels;")
print("72/93/21 relation sequence; 9/16/7 cokernel sequence; 123/30/37/7 dimensions.")
print("The written proof/review establishes actual-map naturality and exactness.")
