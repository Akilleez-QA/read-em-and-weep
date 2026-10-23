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
# W trace separates the nine classes; g-square has trace trace(g)^2-2.
square=[W.index(sub(mul(x,x),z(2))) for x in W]
require(square==[0,0,5,5,3,3,7,7,1],'exact square-class map')
def psi2(c):return [c[i] for i in square]
H=va(V,W)
L2=vs(F(1,2),va(vm(H,H),vs(-1,psi2(H))))
require(L2==va(V,vm(V,W),one),'exterior square H')
N=va(A,Wp)
# Sym^n(V+W), with V=Sym2 Wp; this Euler calculation uses degrees 5 through 11.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}

chi6=va(*[vs(F(1,2),vm(vm(ci,cj),sn(i+j+7))) for i,ci in c.items() for j,cj in c.items()],
        *[vs(F(1,2),vm(psi2(ci),sn(2*i+7))) for i,ci in c.items()])
positive=va(vs(4,A),vs(3,V),vs(5,P),vs(5,D))
negative=va(vs(2,W),vs(2,Wp),vs(3,S),vs(4,T))
require(chi6==va(positive,negative),'global degree-six Euler')
sv=lambda n:[total(sym(2*n-4*j,xp) for j in range(n//2+1)) for xp in Wp]
symD=vs(F(1,2),va(vm(D,D),psi2(D)))
wedgeA=vs(F(1,2),va(vm(A,A),vs(-1,psi2(A))))
plane=va(vm(symD,sv(3)),vs(-1,vm(vm(D,A),sv(2))),vm(wedgeA,V))
require(plane==va(positive,V),'actual plane section character')
require(positive[0]==z(66) and plane[0]==z(69),'section dimensions')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/'audit-inputs'/item['local']).read_bytes()
 require(len(b)==item['bytes'],'input length')
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
catalog=json.loads((root/'audit-inputs/CATALOG.json').read_text())
frontier=json.loads((root/'audit-inputs/FRONTIER.json').read_text())
actual=(root/'audit-inputs/ACTUAL.md').read_bytes()
require(catalog['upstream_input_sha256']['ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md']==hashlib.sha256(actual).hexdigest(),'same actual E provenance')
pairs=[tuple(p) for record in frontier['records'] for p in record['remaining_source_pairs']]
require(sorted(pairs)==[(10,129),(10,157),(13,21),(14,148)],'fixed necessary-pair interface')
expected={10:[[-2,'P'],[-2,'D'],[-2,'D'],[-8,'one'],[-9,'W']],13:[[-2,'P'],[-2,'D'],[-3,'T'],[-9,'W']],14:[[-2,'P'],[-2,'D'],[-4,'V'],[-4,'P'],[-8,'one']]}
reps['one']=one
for eid,blocks in expected.items():
 actual_blocks=next(x['blocks'] for x in catalog['E_catalog'] if x['id']==eid)
 require(actual_blocks==blocks,'three fixed E types, no search for additional cases')
 require(sum(int(reps[n][0][0]) for d,n in blocks)==17,'E rank')
 require(sum(d*int(reps[n][0][0]) for d,n in blocks)==-54,'E degree')
 h0=va(*[reps[n] for d,n in blocks if d==-2])
 h1=va(*[vm(reps[n],[sym(-d-4,x) for x in W]) for d,n in blocks if d<=-4])
 require(h0==va(P,vs(2 if eid==10 else 1,D)),'restriction kernel character')
 require(h1==va(h0,V),'restriction cokernel character')
 require(int(positive[0][0]-h0[0][0])==(52 if eid==10 else 57),'conditional restriction rank')
 require(int(plane[0][0]-h1[0][0])==(52 if eid==10 else 57),'same image dimension')
print('PASS: exact five inputs and same-E provenance; fixed Euler/plane sections; three conditional restriction kernels/cokernels.')
print('No actual coefficient/parameter evaluation, no candidate realization, and no terminal branch selection.')
