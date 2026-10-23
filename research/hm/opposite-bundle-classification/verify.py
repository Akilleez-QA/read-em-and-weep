#!/usr/bin/env python3
"""Bounded abstract binary-icosahedral bundle enumeration; no actual instance evaluations."""
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

names=list(reps)
def dec(c):
 vals=[inner(c,reps[n]) for n in names]
 require(all(y==0 and x.denominator==1 for x,y in vals),"integral real multiplicities")
 return tuple(int(x) for x,y in vals)
H=dec(va(one,vs(3,A),V,vs(2,P),vs(2,D)))
E=dec(va(vs(2,W),Wp,vs(2,S),vs(2,T)))
atoms=[]
for name,c in reps.items():
 r=int(c[0][0]); parity=int(c[1][0]/c[0][0])
 if r>5:continue
 for d in range(26//r+1):
  if parity!=(-1)**d:continue
  h=dec(vm(c,[sym(d,x) for x in W]))
  e=dec(vm(c,[sym(d-1,x) for x in W])) if d else (0,)*9
  if any(x>y for x,y in zip(h,H)) or any(x>y for x,y in zip(e,E)):continue
  ext=inner(c,[sym(d-12,x) for x in W])[0] if d>=12 else 0
  atoms.append((name,d,r,h,e,int(ext)))
sol=[];nodes=0
def rec(i,r,d,h,e,chosen):
 global nodes
 nodes+=1
 if r==0:
  if d==0 and not any(h) and not any(e):sol.append(chosen)
  return
 for j in range(i,len(atoms)):
  a=atoms[j];n,k,s,hh,ee,ex=a
  if s>r or s*k>d:continue
  h2=tuple(x-y for x,y in zip(h,hh));e2=tuple(x-y for x,y in zip(e,ee))
  if min(h2)<0 or min(e2)<0:continue
  rec(j,r-s,d-s*k,h2,e2,chosen+[j])
rec(0,5,26,H,E,[])
print('ATOMS',len(atoms),'NODES',nodes,'SOLUTIONS',len(sol))
for ss in sol:print([(atoms[i][0],atoms[i][1]) for i in ss], 'Ext',sum(atoms[i][5] for i in ss))
expected=[
 [('1',0),('1',2),('1',2),('1',4),('1',18)],
 [('1',0),('1',2),('1',2),('Wp',11)],
 [('1',0),('1',2),('1',14),('Wp',5)],
 [('1',0),('1',2),('1',18),('W',3)],
 [('1',0),('1',2),('1',22),('Wp',1)],
 [('1',0),('1',2),('V',8)],
 [('1',2),('1',4),('1',18),('W',1)],
 [('1',2),('1',10),('1',12),('Wp',1)],
 [('1',2),('1',12),('V',4)],
 [('1',2),('1',18),('A',2)],
 [('1',2),('1',24),('A',0)],
 [('1',2),('W',1),('Wp',11)],
 [('1',2),('W',11),('Wp',1)],
 [('1',2),('Wp',5),('Wp',7)],
 [('1',2),('P',6)],
 [('1',12),('1',14),('A',0)],
 [('1',14),('W',1),('Wp',5)],
 [('1',18),('W',1),('W',3)],
 [('1',22),('W',1),('Wp',1)],
 [('W',1),('V',8)],
 [('W',13),('A',0)]]
actual=[[(atoms[i][0],atoms[i][1]) for i in ss] for ss in sol]
require(actual==expected,'complete literal21-list')
require((len(atoms),nodes,len(sol))==(45,646,21),'bounded state counts')
require([j+1 for j,ss in enumerate(sol) if sum(atoms[i][5] for i in ss)]==[8,9,11,16,21],'exact five exceptional rows')
require([int(inner(one,[sym(d,x) for x in W])[0]) for d in range(0,15,2)]==[1,0,0,0,0,0,1,0],'invariant dimensions through14')
require([sym(7,x) for x in W]==va(Wp,T),'degree7 covariant')
# Universal extension character identities: their geometry is proved separately.
for source,middle,quotient in [
 (one,vm(W,W),[sym(2,x) for x in W]),
 (one,vm(A,[sym(2,x) for x in W]),vm(W,[sym(3,x) for x in W])),
 (one,vm(Wp,[sym(7,x) for x in W]),[sym(14,x) for x in W])]:
 # After twisting down by the kernel degree, chi(O)=1 and higher cohomology vanishes.
 require(middle==va(source,quotient),'nonzero extension Euler character')
# A target-only near-miss demonstrates why E must also be checked.
near_h=va([sym(12,x) for x in W],vm(A,[sym(4,x) for x in W]),A)
near_e=va([sym(11,x) for x in W],vm(A,[sym(3,x) for x in W]),W)
require(dec(near_h)==H and dec(near_e)!=E,'source character excludes target-only near-miss')
print('PASS: full21-list; exact five Ext1 rows; structural invariant bound; degree7 covariant; three extension Euler identities; target-only negative control.')
print('BOUNDARY: abstract fixed group characters only; no actual HM/source instance evaluation.')
root=Path(__file__).resolve().parent
for entry in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/('PR'+str(entry['pr'])+'.md')).read_bytes()
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==entry['blob'],'immutable input '+str(entry['pr']))
print('PASS: three immutable dependency Git-blob identities.')
