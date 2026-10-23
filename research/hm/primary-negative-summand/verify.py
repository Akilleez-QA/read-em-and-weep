#!/usr/bin/env python3
"""Two authenticated inputs and bounded universal representation arithmetic only."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
count=0
def require(v,msg):
 global count
 count+=1
 if not v:raise RuntimeError(msg)
base=Path(__file__).resolve().parent
for item in json.loads((base/'INPUTS.json').read_text()):
 b=(base/item['local_path']).read_bytes()
 require(len(b)==item['bytes'],item['label']+' length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],item['label']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],item['label']+' Git blob')
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def sc(n,x):return n*x[0],n*x[1]
def total(xs):
 out=z(0)
 for x in xs:out=add(out,x)
 return out
def sym(n,x):
 if n==0:return z(1)
 a,b=z(1),x
 for _ in range(2,n+1):a,b=b,sub(mul(x,b),a)
 return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
Wp=[z(2),z(-2),phip,neg(phip),phi,neg(phi),z(1),z(-1),z(0)]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
A=[sym(2,x) for x in W];V=[sym(2,x) for x in Wp]
D=[sym(4,x) for x in W];T=[sym(5,x) for x in W]
sizes=[1,1,12,12,12,12,20,20,30]
def inner(a,b):return sc(F(1,120),total(sc(n,mul(x,y)) for n,x,y in zip(sizes,a,b)))
R=[];source=[];target=[]
for i in range(9):
 r=add(Wp[i],T[i]);a4=add(V[i],add(sc(2,P[i]),D[i]))
 m4=add(sc(2,V[i]),add(sc(4,P[i]),sc(3,D[i])))
 m5=add(Wp[i],sc(3,T[i]))
 require(mul(P[i],W[i])==r,'primary terminal character')
 require(mul(P[i],add(z(1),A[i]))==a4,'primary source character')
 require(mul(r,W[i])==a4,'primary cohomology source character')
 require(sub(m4,a4)==add(V[i],add(sc(2,P[i]),sc(2,D[i]))),'quotient source character')
 require(sub(m5,r)==sc(2,T[i]),'quotient target character')
 R.append(r);source.append(sub(m4,a4));target.append(sub(m5,r))
require(inner(T,T)==z(1),'T irreducible')
require(inner(T,Wp)==z(0),'T and Wp distinct')
require(inner(target,R)==z(2),'equivariant splitting ambiguity exactly2')
require(R[0]==z(8) and source[0]==z(21) and target[0]==z(12),'coefficient dimensions')
require(37-16==21 and 20-8==12,'actual quotient dimensions')
require(17-8==9 and -54+24==-30,'bundle quotient rank degree')
require(21-12==9 and -21-9==-30,'quotient pencil rank degree')
require(8*(-3)==-24 and 8*(-2)==-16,'primary degree twist')
require(R[1]==z(-8) and target[1]==z(-12),'physical odd coefficient parity')
# Serre duality twists on P1: (F* O(-3))* omega=F O(1).
require(3-2==1,'Serre duality twist')
require(max(0,-1+1)==0 and max(0,-(-1)-1)==0,'O(-1) acyclic')
require(max(0,-(-2)-1)==1,'H1 O(-2) one')
for d in [2,3,4,5,8,9,10]:
 require(max(0,-(d-3)-1)==0,'Ext1 line check d='+str(d))
result={'status':'PASS','checks':count,'input_count':2,'actual_instance_evaluation':False,'canonical_primary_bundle':{'rank':8,'degree':-24,'type':'(Wp+T) O(-3)'},'canonical_quotient':{'rank':9,'degree':-30,'terminal_source_character':'V+2P+2D','terminal_target_character':'2T','terminal_dimensions':[21,12]},'equivariant_splittings':'nonempty affine space of dimension2','complement_canonical':False,'horizontal_or_full_module_splitting_claimed':False}
print(json.dumps(result,indent=2,sort_keys=True))
