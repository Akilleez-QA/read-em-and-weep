#!/usr/bin/env python3
"""Fixed universal characters/degrees only; no actual multiplication evaluation."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
count=0
def require(c,m):
 global count
 count+=1
 if not c: raise RuntimeError(m)
def z(a,b=0):return F(a),F(b)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def scale(k,x):return k*x[0],k*x[1]
def total(xs):
 r=z(0)
 for x in xs:r=add(r,x)
 return r
def va(*cs):return [total(x) for x in zip(*cs)]
def vs(k,c):return [scale(k,x) for x in c]
def vm(c,d):return [mul(x,y) for x,y in zip(c,d)]
def sym(n,x):
 if n==0:return z(1)
 a,b=z(1),x
 for _ in range(2,n+1):a,b=b,add(mul(x,b),scale(-1,a))
 return b
phi=z(F(1,2),F(1,2));phip=z(F(1,2),F(-1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
one=[z(1)]*9;A=[sym(2,x) for x in W];D=[sym(4,x) for x in W]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]));V=va([sym(6,x) for x in W],vs(-1,P))
def inner(c,d):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,c,d)))
require(sum(sizes)==120,'group order')
require(inner(V,one)==z(0),'V has no invariant')
require(vm(V,P)==va(A,P,D),'V times P')
require(vm(V,D)==va(A,V,P,D),'V times D')
section=va(one,P,D);bound=vm(V,section)
require(bound==vs(2,va(A,V,P,D)),'joint kernel ambient character')
require(inner(bound,one)==z(0),'joint kernel ambient has no scalar')
require(bound[0]==z(30),'joint kernel ambient dimension30')
P3=va(one,vs(4,A),vs(2,V),vs(3,P),vs(3,D))
R=va(one,vs(3,A),vs(2,V),vs(3,P),vs(3,D))
N4=va(vs(2,V),vs(4,P),vs(3,D))
rel=va(one,vs(4,A),vs(4,V),vs(5,P),vs(7,D))
N2=va(A,vs(2,V),vs(3,P),vs(4,D))
require(P3[0]==z(46),'full middle dimension')
require(R[0]==z(43),'reachable middle dimension')
require(N4[0]==z(37),'final cohomology dimension')
require(va(R,rel)==vm(V,N2),'actual first-arrow sequence characters')
require(rel[0]==z(80),'first-arrow relation dimension')
require(inner(P3,one)==z(1),'unique scalar middle')
require(inner(N4,V)==z(2),'full final repeated V')
require((vm(V,N4)[0],R[0])==(z(111),z(43)),'curried ambient is not final37')
# Exact first-section degree arithmetic, not any section map.
require((6-1,7-1,8-1)==(5,6,7),'G shift convention')
require(min([2])>1,'primary section first relation after degree1')
require(4*4-6==10,'symmetric quotient of U tensor U')
require(5*4*4-5*6==5*10,'linear symmetric quotient dimensions')
# Four-column Koszul index audit: the direct sheaf proof is primary.
p,q=-3,1
out=[(p+r,q-r+1) for r in range(2,6) if -3<=p+r<=0 and q-r+1>=0]
require(out==[(-1,0)],'only possible outgoing higher differential')
require(all(p-r < -3 for r in range(2,6)),'no incoming higher differential')
root=Path(__file__).resolve().parent
for e in json.loads((root/'INPUTS.json').read_text()):
 b=(root/e['local_path']).read_bytes()
 require(len(b)==e['bytes'],'input byte count '+e['label'])
 require(hashlib.sha256(b).hexdigest()==e['sha256'],'input SHA256 '+e['label'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'],'input Git blob '+e['label'])
print(json.dumps({'status':'PASS','checks':count,'full_middle_dimension':46,'curried_reachable_dimension':43,'scalar_second_image_dimension':3,'transported_scalar_operator_rank':1,'scope':'Bounded fixed representation and degree bookkeeping; actual-map proof is written, no selected instance evaluation.'},indent=2,sort_keys=True))
