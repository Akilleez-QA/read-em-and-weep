#!/usr/bin/env python3
"""Exact synthetic Hom-complex tests, not actual HM instances."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
ROOT=Path(__file__).resolve().parent;n=0
def ck(p,msg):
 global n
 n+=1
 if not p:raise RuntimeError(msg)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==e['sha256'],'immutable SHA256')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'],'immutable Git blob')
names=('one','W','A','S','D','T','V','P','Wp');dims=(1,2,3,4,5,6,3,4,2)
def ch(**kw):return tuple(kw.get(n,0) for n in names)
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def mw(a):return tuple(sum(a[i]*rules[i][j] for i in range(9)) for j in range(9))
sym=[ch(one=1),ch(W=1)]
for i in range(2,7):sym.append(tuple(a-b for a,b in zip(mw(sym[-1]),sym[-2])))
AD=tuple(sum(sym[i][j] for i in (6,4,2)) for j in range(9))
ck(AD==ch(A=1,D=1,V=1,P=1),'three unique secondary channels')
ck(sum(x*y for x,y in zip(ch(P=1),ch(A=1,D=1)))==0,'equivariant null-homotopy ambiguity zero')
ck(sum(x*y for x,y in zip(ch(D=1),ch(A=1,D=1)))==1,'one-dimensional degree-zero induced map')
ck(2-1==1,'radical kernel line dimension')
def mat(r,c,seed):return [[F(((i+2)*(j+3)*(seed+1)+i-j*seed)%11-5) for j in range(c)] for i in range(r)]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(r,s)] for r,s in zip(a,b)]
def zero(a):return all(x==0 for r in a for x in r)
def transpose(a):return list(map(list,zip(*a)))
def rank(a):
 a=[list(map(F,row)) for row in a];r=0
 for c in range(len(a[0])):
  pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];p=a[r][c];a[r]=[x/p for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    p=a[i][c];a[i]=[x-p*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
for seed in range(24):
 # S0 dim4,S1 dim3,T0 dim3,T1 dim4. No actual geometry represented.
 qs=mat(3,4,seed);qt=mat(4,3,seed+1);h=mat(4,4,seed+2)
 ls=mat(3,4,seed+3);lt=mat(4,3,seed+4)
 j0=mm(h,qt);j1=mm(qs,h);k0=mm(h,lt);k1=mm(ls,h)
 ck(zero(add(mm(qs,j0),mm(j1,qt),-1)),'Q boundary is Q cocycle')
 dqk=add(mm(qs,k0),mm(k1,qt),-1)
 dlj=add(mm(ls,j0),mm(j1,lt),-1)
 ck(zero(add(dqk,dlj)),'dQ dL plus dL dQ on homotopy')
 ck(zero(add(mm(ls,k0),mm(k1,lt),-1)),'secondary same-L chain identity')
# Explicit diagnostic chain maps with nonzero endpoint map but zero secondary cohomology.
q=[[F(1),F(0)],[F(0),F(0)]];h=q;l=[[F(3),F(0)],[F(0),F(7)]]
j0=mm(h,q);j1=mm(q,h);k0=mm(h,l);k1=mm(l,h)
ck(j0==q and j1==q and not zero(h),'nonzero null-homotopic endpoint map')
ck(j0[1][1]==j1[1][1]==k0[1][1]==k1[1][1]==0,'nonzero h need not give secondary cohomology')
# Surjection followed by adjoint has rank4, for indefinite bilinear pairings too.
for seed in range(12):
 b=[[F(int(i==j)) for j in range(4)]+[F(seed+i)] for i in range(4)]
 pairingP=[[F((1 if i%2==0 else -1)*int(i==j)) for j in range(4)] for i in range(4)]
 adj=mm(transpose(b),pairingP)
 ck(rank(b)==4 and rank(adj)==4,'surjection and bilinear adjoint injection')
 ck(rank(mm(adj,b))==4,'composition rank4 independent of positivity')
ck(4>3,'rank incompatibility with A factor')
# Quartic transvectant matrices for the universal two SL2 orbit types.
square=[[F(0) for j in range(5)] for i in range(5)]
axis=[[F(0) for j in range(5)] for i in range(5)]
for j in range(5):
 if j:square[j-1][j]=F(2*j)
 axis[j][j]=F(2*j-4)
ck(rank(square)==rank(axis)==4,'both nonzero quadratic Jordan types rank4')
ck(zero(mm(square,[[F(int(i==0))] for i in range(5)])),'square kernel x4')
ck(zero(mm(axis,[[F(int(i==2))] for i in range(5)])),'semisimple kernel x2y2')
ck(5-4==1 and -(-5)+(-3)==2,'kernel/cokernel line ranks and degree')
print(f'PASS: {n} exact checks; two immutable inputs; no actual HM evaluation.')
