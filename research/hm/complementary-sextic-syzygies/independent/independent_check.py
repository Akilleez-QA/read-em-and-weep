#!/usr/bin/env python3
"""Independent exact class-character and formal apolar controls; no HM instance."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
checks=0
def need(v,label):
 global checks
 checks+=1
 if not v: raise RuntimeError(label)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def mul(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def sub(a,b):return add(a,scale(-1,b))
z=lambda a,b=0:(F(a),F(b))
tr=[z(2),z(-2),z(F(1,2),F(1,2)),z(F(-1,2),F(-1,2)),z(F(1,2),F(-1,2)),z(F(-1,2),F(1,2)),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n,t):
 if n<0:return z(0)
 a,b=z(1),t
 if n==0:return a
 for j in range(2,n+1):a,b=b,sub(mul(t,b),a)
 return b
P=[z(v) for v in [4,4,-1,-1,-1,-1,1,1,0]]
V=[sub(sym(6,t),p) for t,p in zip(tr,P)]
T=[sym(5,t) for t in tr]
Wp=[sub(mul(p,t),tt) for p,t,tt in zip(P,tr,T)]
for i,t in enumerate(tr):
 need(mul(P[i],t)==sym(7,t),'linear multiplier character')
 need(sub(mul(P[i],sym(2,t)),sym(8,t))==V[i],'kernel character V')
 need(mul(V[i],t)==T[i],'complementary V channel')
 need(add(Wp[i],T[i])==sym(7,t),'target irreducibles')
for d in range(1,61):
 for t,p,v in zip(tr,P,V):
  need(sub(mul(p,sym(d,t)),sym(d+6,t))==mul(v,sym(d-2,t)),'all multiplier exact character')
 need(4*(d+1)-(d+7)==3*(d-1),'kernel dimension')
for a in range(1,7):
 for b in range(a,7):
  for c in range(b,7):
   if a+b+c!=6:continue
   need(sum(max(2-x,0) for x in (a,b,c))<=3,'linear-kernel dimension bound')
   if a>=2:need((a,b,c)==(2,2,2),'balanced kernel forced')
hilbert=[]
for n in range(60):
 h=n+1-4*max(n-5,0)+3*max(n-7,0)
 need(h>=0,'Hilbert nonnegative');hilbert.append(h)
need(hilbert[:7]==[1,2,3,4,5,6,3] and not any(hilbert[7:]),'Hilbert vector')
need(sum(hilbert)==24,'finite quotient length')
pairings=0
for d in range(1,27):
 n=d+6;k=d-1
 for a in range(k+1):
  for b in range(7):
   coefficient=F(0)
   for j in range(8):
    h=n-a-b-j
    if 0<=h<=d:coefficient+=F((-1)**(a+j)*comb(7,j)*comb(d,h),comb(n,a+j))
   need(coefficient==0,'formal apolar identity');pairings+=1
 need((k+1)+7==n+1,'apolar dimensions')
 need(n+1-4==n-3,'rank4 sharp model')
 if d>=2:
  need(-1>-d and n+4-6==n-2,'nonzero high sharp model')
 else:need(not any(-1<e<0 for e in range(-6,7)),'d1 high block empty')
 need((-1)**d==(-1)**n,'center parity')
 for r in range(15):
  for q in range(18):
   codim=n+1+q-(r+4)
   need((r<=q)==(codim>=n-3),'rank bound')
   if r:need((r<q)==(codim>=n-2),'strict saturated rank bound')
sources={'pr1147.md':('2ea61681c18105cbba37e7135fc968aa9052e14eff71d963e8c374f55f041122','9bf944c40951a06378c48b743157ed0c1710aead'),'pr1148.md':('18ad6a68fdc672e505d2c9e607152dbe7e6a6d42c20898acbafbd807aaf78fd5','f8ff9012ce5cef32b6a4bb26e8baa7c37d395a72'),'character-reference.py':('5b3b1d415f26ca467670afeb73357cbb0e9c125a6b1acd25155b6d85eef4e4f1','0660296ed3874b59a14b1afc75da1d031c6d63a9')}
for name,(sha,blob) in sources.items():
 data=(ROOT/'originals'/name).read_bytes()
 need(hashlib.sha256(data).hexdigest()==sha,'fresh original hash')
 need(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==blob,'fresh original blob')
print(json.dumps({'checks':checks,'formal_apolar_pairings':pairings,'character_multiplier_degrees':[1,60],'actual_instance_evaluated':False,'new_actual_exclusion_claimed':False},indent=2,sort_keys=True))
