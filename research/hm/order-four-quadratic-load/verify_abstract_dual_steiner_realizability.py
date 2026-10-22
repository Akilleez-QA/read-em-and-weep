#!/usr/bin/env python3
"""Bounded character checks only: no pencil, point, coefficient, or rank evaluation."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'unrestricted-dual-splittings-and-pairs.json'
data=json.loads(SOURCE.read_text())
# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
zero=(0,)*9
unit=lambda n:tuple(int(k==n)for k in names)
def add(*xs):return tuple(map(sum,zip(*xs)))if xs else zero
def neg(x):return tuple(-v for v in x)
def dec(ch):
 out=[inner(ch,chars[n])for n in names]
 assert all(b==0 and a.denominator==1 for a,b in out)
 return tuple(int(a)for a,b in out)
# All degrees needed by the proof and the extra coefficient test are <=28.
prod={(n,k):dec([times(a,b)for a,b in zip(chars[n],symchar(k))])for n in names for k in range(29)}
def h0(X,t=0):return add(*(prod[n,e+t]for e,n in X if e+t>=0))
def h1(X,t=0):return add(*(prod[n,-e-t-2]for e,n in X if e+t<=-2))
dims={n:int(chars[n][0][0])for n in names}
def dim(ch):return sum(m*dims[n]for m,n in zip(ch,names))
def rank(X):return sum(dims[n]for e,n in X)
def degree(X):return sum(e*dims[n]for e,n in X)
def tensorW(ch):return add(*(tuple(m*v for v in prod[n,1])for m,n in zip(ch,names)))
M2=(0,0,0,1,2,3,0,4,0);M3=(0,0,3,0,0,0,3,0,6)
assert(dim(M2),dim(M3))==(41,54)
profiles=[tuple(map(tuple,X))for X in data['profiles']]
assert len(profiles)==len(set(profiles))==260
coefficients=Counter()
for X in profiles:
 assert all(-28<=e<=-1 for e,n in X)
 assert all(chars[n][1][0]==(-1)**e*dims[n]for e,n in X)
 assert(rank(X),degree(X))==(13,-54)
 assert h0(X)==h0(X,-1)==zero
 assert h1(X)==M2 and h1(X,-1)==M3
 E=tuple((-e-1,n)for e,n in X) # F^*(-1); irreducible duals are unchanged.
 assert all(e>=0 for e,n in E)
 assert(rank(E),degree(E))==(13,41)
 assert h0(E)==M3 and h1(E)==zero
 # E is globally generated; its evaluation kernel has rank41, degree-41.
 assert dim(h0(E))-rank(E)==41 and -degree(E)==-41
 # K(1) has representation R. Its exact character is H0(E)W-H0(E(1)).
 R=add(tensorW(h0(E)),neg(h0(E,1)))
 assert R==M2 and dim(R)==41 and min(R)>=0
 # Equivalently the coefficient character identity holds block by block,
 # including j=1 where the kernel contribution is zero.
 for e,n in X:
  j=-e
  assert add(tensorW(prod[n,j-1]),neg(prod[n,j]))==(prod[n,j-2]if j>=2 else zero)
 coefficients[h0(X,1)]+=1
expected={zero:37,unit('T'):8,unit('S'):15,unit('Wp'):87,
 add(unit('Wp'),unit('T')):17,add(unit('Wp'),unit('S')):32,
 add(unit('Wp'),unit('Wp')):51,
 add(unit('Wp'),unit('Wp'),unit('T')):3,
 add(unit('Wp'),unit('Wp'),unit('S')):7,
 add(unit('Wp'),unit('Wp'),unit('Wp')):3}
assert dict(coefficients)==expected
print('Input SHA-256:',hashlib.sha256(SOURCE.read_bytes()).hexdigest())
print('PASS: all 260 negative types have rank13 degree-54 and adjacent characters M2,M3.')
print('PASS: all dual-twisted bundles E have rank13 degree41, H0=M3*, H1=0.')
print('PASS: all evaluation kernels have rank41 degree-41 and coefficient character R=M2*.')
print('PASS: exact blockwise coefficient identities and ten degree-one section-character counts.')
print('Scope: abstract equivariant Steiner presentation existence only; not actual HM or A/B/Gauss realization.')
print('Bound: 261 cached products, 260 profiles with at most13 blocks each; no instances or rank experiments.')
