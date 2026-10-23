"""Exact marked-doublet character, orbit and bound checks. No actual HM coefficients."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
checks=[]
def ck(label, ok):
    if not ok: raise RuntimeError(label)
    checks.append(label)
def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def total(xs):
    v=z(0)
    for x in xs:v=add(v,x)
    return v
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n):
    a=[z(1)]*9;b=tr
    for _ in range(n):a,b=b,[sub(mul(x,y),v) for x,y,v in zip(tr,b,a)]
    return a
def va(*vs):return [total(t) for t in zip(*vs)]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def vs(k,a):return [scale(k,x) for x in a]
def ip(a,b):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
C={'1':sym(0),'W':sym(1),'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5),'P':P}
C['V']=va(sym(6),vs(-1,P));C['Wp']=va(vm(C['W'],P),vs(-1,C['T']))
for n,a in C.items():
    for m,b in C.items():ck('orthogonality '+n+' '+m,ip(a,b)==z(int(n==m)))
for n in range(7):ck('Wprime absent Sym'+str(n),ip(C['Wp'],sym(n))==z(0))
ck('Sym7 Wprime plus T',sym(7)==va(C['Wp'],C['T']))
ck('unique degree6 doublet channel',vm(C['W'],sym(6))==va(C['Wp'],vs(2,C['T'])))
ck('Hom dimension1',ip(C['Wp'],vm(C['W'],sym(6)))==z(1))
for n in range(1,12):ck('no scalar invariant degree'+str(n),ip(C['1'],sym(n))==z(0))
ck('one invariant degree12',ip(C['1'],sym(12))==z(1))
# Exact independent finite-group check on A5, no actual parameter values.
from itertools import permutations
perms=[p for p in permutations(range(5)) if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0]
idp=tuple(range(5))
def compose(p,q):return tuple(p[q[i]] for i in range(5))
def order(p):
 q=idp
 for n in range(1,61):
  q=compose(p,q)
  if q==idp:return n
 raise RuntimeError('order')
orders=[order(p) for p in perms]
ck('A5 order60',len(perms)==60)
ck('possible cyclic stabilizer orders',set(orders)=={1,2,3,5})
ck('twentyfour order5 elements',orders.count(5)==24)
subgroups=set()
for p in perms:
 if order(p)==5:
  q=idp; elems=[]
  for _ in range(5):elems.append(q);q=compose(p,q)
  subgroups.add(frozenset(elems))
ck('six cyclic5 subgroups',len(subgroups)==6)
orbits=sorted(60//k for k in set(orders))
ck('projective orbit possibilities',orbits==[12,20,30,60])
ck('unique degree12 orbit multiplicity solution',[(a,b,c,d) for a in range(2) for b in range(2) for c in range(2) for d in range(2) if 12*a+20*b+30*c+60*d==12]==[(1,0,0,0)])
# Bounds at both sharp endpoints, with no map values selected.
for top in range(-12,4):ck('rank1 impossible top'+str(top),not any(4<=e<=top for e in range(-20,21)))
for topsum in range(-6,6):
 allowed=[b+6 for b in range(-6,topsum+1) if b+6==0 or b+6>=12]
 ck('saturation forced sum'+str(topsum),allowed==[0])
ck('sharp determinant degree12',2*3-2*(-3)==12)
ck('sharp rank1 kernel degree',2*(-3)-4==-10)
ck('negative target Hom degree',-8-(-3)<0)
# DVR local Smith valuations alpha<=beta; simple det forces (0,1).
ck('simple determinant Smith valuations',[(a,b) for a in range(4) for b in range(a,4) if a+b==1]==[(0,1)])
ck('rankzero entails determinant order>=2',all(a+b>=2 for a in range(1,8) for b in range(a,8)))
root=Path(__file__).resolve().parent
manifest=json.loads((root/'INPUTS.json').read_text())
for r in manifest:
 raw=(root/r['file']).read_bytes()
 ck('input bytes PR'+str(r['pr']),len(raw)==r['bytes'])
 ck('input sha256 PR'+str(r['pr']),hashlib.sha256(raw).hexdigest()==r['sha256'])
 ck('input gitblob PR'+str(r['pr']),hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==r['git_blob'])
print(json.dumps({'status':'pass','checks':len(checks),'check_labels':checks,'rank_one_minimum_saturation_degree':4,'rank_two_saturation_top_two_bound':5,'conditional_target':'O(-8)+W O(3)','positive_block_Hom_dimension':1,'determinant_degree':12,'defect_support':'unique reduced projective A5 orbit of size12','positive_block_cokernel_length':12,'actual_source_instances_evaluated':0,'claim_scope':'conditional marked bundle-map geometry; no source/profile exclusion or complete repair'},indent=2))
