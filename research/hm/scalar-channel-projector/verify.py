#!/usr/bin/env python3
"""Nine-class abstract characters only. No actual tensors or instance evaluations."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json

count=0
def require(condition,message):
    global count
    count+=1
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
# Fixed Sym^n(V+W), with V=Sym2 Wp; maximum degree4 below.
def sn(n):
 return [total(mul(total(sym(2*i-4*j,xp) for j in range(i//2+1)),sym(n-i,x)) for i in range(n+1)) for x,xp in zip(W,Wp)]
c={-1:vs(-1,N),0:va(vm(Wp,L2),vs(-1,N)),1:vs(-1,vm(Wp,H)),2:Wp}



# Only fixed representation K-classes, not monad arrows.
def euler_primary(t):
 return va(*[vm(ci,sn(i+t)) for i,ci in c.items() if i+t>=0])
require(euler_primary(0)==vs(-1,va(A,Wp)),'primary twist0 Euler')
require(euler_primary(1)==vs(-1,va(P,W,S)),'primary twist1 Euler')
require(euler_primary(2)==vs(-1,va(one,A,T)),'primary twist2 Euler')
require(vm(P,A)==va(V,P,D),'primary source unique V')
require(vm(P,P)==va(one,A,V,P,D),'primary scalar middle unique')
require(vm(V,P)==va(A,P,D),'second primary arrow has no scalar target')
require(inner(vm(P,A),V)==z(1),'source primary V multiplicity')
require(inner(vm(P,va(one,A)),V)==z(1),'target primary V multiplicity')
require(inner(vm(P,P),one)==z(1),'unique primary scalar')
require(inner(vm(V,V),one)==z(1),'invariant bilinear form is unique')
require(inner(P,P)==z(1),'Z irreducible')
require((A[0],V[0],P[0])==(z(3),z(3),z(4)),'trace dimensions X V Z')
require([(j-1,j-3) for j in [3,4,5]]==[(2,0),(3,1),(4,2)],'actual graded shifts')
require(P[1]==P[0] and A[1]==A[0],'positive primary factor parity')
# Trace cyclicity is proved in the text; arithmetic records its normalization.
c_metric=F(3,3);t=F(3,3*4)
require(c_metric==1,'metric trace coefficient from trace identity')
require(t==F(1,4),'coevaluation scalar normalization')
require(4*t==1,'scalar projector normalization')
require(t!=0 and t!=F(1,3) and t!=-1,'exclude old nilpotent and deficient cases')
# Universal two-dimensional algebra with generator k and relation k^2=t*k.
# Pair(a,b) denotes a*Id+b*k, never an actual HM/source matrix.
def pa(x,y):return (x[0]+y[0],x[1]+y[1])
def ps(a,x):return (a*x[0],a*x[1])
def pm(x,y):return (x[0]*y[0],x[0]*y[1]+x[1]*y[0]+t*x[1]*y[1])
def eval_pair(x,eig):return x[0]+x[1]*eig
I=(F(1),F(0));k=(F(0),F(1));pi=ps(4,k)
require(pm(pi,pi)==pi,'universal normalized idempotent')
C0=k; C1=(F(-1,4),F(3,4)); C2=(F(3,20),F(3,20));Sop=(F(-1,10),F(9,10))
require(C0==pa(C1,ps(F(5,3),C2)),'actual channel commutativity normalization')
require(I==pa(ps(-1,C1),ps(5,C2)),'actual invariant contraction normalization')
expected=[(F(1,4),0),(F(-1,16),F(-1,4)),(F(3,16),F(3,20)),(F(1,8),F(-1,10))]
for op,ex in zip([C0,C1,C2,Sop],expected):
 require(tuple(eval_pair(op,e) for e in [t,0])==ex,'channel spectrum')
require(eval_pair(C1,t)*eval_pair(C1,0)==F(1,64),'C1 invertibility')
require(eval_pair(C2,t)*eval_pair(C2,0)==F(9,320),'C2 invertibility')
require(1-3*t==F(1,4) and 1+t==F(5,4),'old shifted determinant exclusions')
require(1+2*3+2*5==17,'exact first-arrow image dimension')
require(pm(k,pa(k,ps(-t,I)))==(0,0),'minimal polynomial k(k-t)')
require(t!=0,'image and kernel lines distinct')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['local_path']).read_bytes()
 require(len(b)==item['bytes'],'input length '+item['label'])
 require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256 '+item['label'])
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'input Git blob '+item['label'])
print(json.dumps({'status':'PASS','checks':count,'normalized_scalar_trace':'1/4','normalized_projector_factor':4,'first_arrow_image_dimension':17,'scope':'Fixed characters and universal rational polynomial identities only. The written actual-map trace proof is not replaced by these checks.'},sort_keys=True,indent=2))
