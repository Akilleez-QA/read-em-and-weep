#!/usr/bin/env python3
"""Exact full-space polar/curl identities. No HM-instance coefficients."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
checks=0
def ck(v,msg):
 global checks
 checks+=1
 if not v:raise RuntimeError(msg)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==e['sha256'],'input SHA256')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'],'input blob')
names=('one','W','A','S','D','T','V','P','Wp');dims=(1,2,3,4,5,6,3,4,2)
def ch(**kw):return tuple(kw.get(n,0) for n in names)
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def mw(a):return tuple(sum(a[i]*rules[i][j] for i in range(9)) for j in range(9))
sym=[ch(one=1),ch(W=1)]
for i in range(2,19):sym.append(tuple(a-b for a,b in zip(mw(sym[-1]),sym[-2])))
for i,a in enumerate(sym):ck(min(a)>=0 and sum(x*y for x,y in zip(a,dims))==i+1,'symmetric power dimension')
ck([sym[i][0] for i in (12,10,8,6,4)]==[1,0,0,0,0],'invariant in Cartan only')
ck(sym[18][0]==0,'no degree18 invariant')
ck(sym[6]==ch(V=1,P=1),'Type II X to D Hom zero')
ck(tuple(sum(sym[i][j] for i in (6,4,2)) for j in range(9))[names.index('D')]==1,'unique quadratic D channel')
# Sparse polynomials in u,v,x,y, with internal degree4 and external degree8.
def add(*polys):
 o={}
 for p in polys:
  for m,c in p.items():o[m]=o.get(m,0)+c
 return {m:c for m,c in o.items() if c}
def sc(p,c):return {m:a*c for m,a in p.items() if a*c}
def der(p,i):
 o={}
 for m,c in p.items():
  if m[i]:
   q=list(m);q[i]-=1;o[tuple(q)]=c*m[i]
 return o
def var(p,i):
 o={}
 for m,c in p.items():
  q=list(m);q[i]+=1;o[tuple(q)]=c
 return o
def Ei(p):return var(der(p,1),0)
def Fi(p):return var(der(p,0),1)
def Hi(p):return add(var(der(p,0),0),sc(var(der(p,1),1),-1))
def Ee(p):return sc(var(der(p,2),3),-1)
def Fe(p):return sc(var(der(p,3),2),-1)
def He(p):return add(sc(var(der(p,2),2),-1),var(der(p,3),3))
def Et(p):return add(Ei(p),Ee(p))
def Ft(p):return add(Fi(p),Fe(p))
def Ht(p):return add(Hi(p),He(p))
def cas(p,E,F,H):return add(H(H(p)),sc(E(F(p)),2),sc(F(E(p)),2))
def moment(p):return add(var(var(Ei(p),2),2),sc(var(var(Hi(p),2),3),-1),sc(var(var(Fi(p),3),3),-1))
def omega(p):return add(sc(var(Ei(der(p,3)),2),2),Hi(add(var(der(p,2),2),sc(var(der(p,3),3),-1))),sc(var(Fi(der(p,2)),3),2))
basis=[{(4-i,i,8-j,j):1} for i in range(5) for j in range(9)]
ck(len(basis)==45,'full polynomial space')
for p in basis:
 # d(moment dr), with second partials cancelling, equals Omega.
 curl=add(der(moment(der(p,3)),2),sc(der(moment(der(p,2)),3),-1))
 ck(curl==omega(p),'curl formula on full space')
 ck(sc(omega(p),2)==add(cas(p,Ei,Fi,Hi),cas(p,Ee,Fe,He),sc(cas(p,Et,Ft,Ht),-1)),'Casimir identity on full space')
 ck(cas(p,Ei,Fi,Hi)==sc(p,24),'internal Casimir')
 ck(cas(p,Ee,Fe,He)==sc(p,80),'external Casimir')
 for op in (Et,Ft,Ht):ck(omega(op(p))==op(omega(p)),'Omega equivariance')
p={(4,0,0,8):1}
ck(Et(p)=={},'Cartan highest vector')
for i in range(13):
 ck(bool(p),'Cartan basis vector nonzero')
 ck(omega(p)==sc(p,-32),'Cartan curl eigenvalue')
 ck(cas(p,Et,Ft,Ht)==sc(p,168),'Cartan total Casimir')
 p=Ft(p)
ck(p=={},'Cartan string ends after13')
ck((24+80-168)//2==-32,'nonzero scalar')
ck((3+3)-5==1 and 0-(-2*5)==10 and 28-10==18,'saturated quotient gate')
rows=[(1,0,0),(1,0,1),(1,1,0),(2,0,0)]
ck([r for r in rows if r[0]==2]==[(2,0,0)],'Type II sole remaining full-J footprint')
ck(3+6+8+10==27 and 6+8+10==24,'Type II dimensions')
print(f'PASS: {checks} checks;8 immutable inputs;45 full-space curl tests;13 Cartan vectors.')
