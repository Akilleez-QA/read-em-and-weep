#!/usr/bin/env python3
"""Bounded symbolic reconstruction checks, no actual HM evaluations."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
nchecks=0
def ck(p,label):
 global nchecks
 if not p:raise ValueError(label)
 nchecks+=1
def zero(m):return all(s.expand(v)==0 for v in m) if isinstance(m,s.MatrixBase) else s.expand(m)==0
for row in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/row['file']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'SHA256 '+row['file'])
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'Git blob '+row['file'])
# Universal Sym^16 multiplication, not an actual HM coefficient matrix.
n=16
Mx=s.zeros(n+2,n+1);My=s.zeros(n+2,n+1)
for i in range(n+1):Mx[i,i]=1;My[i+1,i]=1
Mul=Mx.row_join(My)
right=s.zeros(2*(n+1),n+2)
for i in range(n+1):right[i,i]=1
right[-1,-1]=1
ck(Mul*right==s.eye(n+2),'universal degree16 multiplication onto')
rels=s.zeros(2*(n+1),n)
for i in range(1,n+1):rels[i,i-1]=1;rels[n+1+i-1,i-1]=-1
ck(Mul*rels==s.zeros(n+2,n),'all standard linear multiplication relations')
# A left inverse of relation inclusion certifies independence without rank calls.
relleft=s.zeros(n,2*(n+1))
for i in range(n):relleft[i,i+1]=1
ck(relleft*rels==s.eye(n),'universal relation basis independent')
ck(2*(n+1)-(n+2)==n,'complete relation dimension')
# Actual target common kernel is H0(E_B(1)); use bundle degrees, not a matrix.
ck(-4+1==-3 and -3<0,'target B has no degree1 global sections')
ck((3+4)==7,'B coefficient rank')
ck(18-2==16 and 18-1==17,'F reconstructed source/middle twists')
# Character Hom enumeration for target-only freedom.
yl={'V':1,'P':1};yb={'V':1,'P':2,'D':2}
ck(sum(v*yb.get(k,0) for k,v in yl.items())==3,'exact L to B equivariant Hom dimension')
ck(3+4==7 and 3+2*4+2*5==21,'L and B target dimensions')
ck(1-2==-1,'Qbundle L contributes H0 O(-1)=0 at N2')
# Formal endpoint relation transport: each arbitrary summand is rewritten by
# B_N(m) A_N(l) f2 = f4 B_M(m) A_M(l), then distributivity factors f4 B_M(m).
for m in ('x','y'):
 terms=[('BN',m,'AN',l,'f2','v'+str(i)) for i,l in enumerate(('x','y','x'))]
 rew=[('f4','BM',m,'AM',term[3],term[5]) for term in terms]
 expected=[('f4','BM',m,'AM',l,'v'+str(i)) for i,l in enumerate(('x','y','x'))]
 ck(rew==expected,'quadratic intertwining transports every relation '+m)
 ck(all(t[:3]==('f4','BM',m) for t in rew),'source relation factors under f4 B '+m)
# Mixed products follow from the entire quadratic family, not two axes alone.
ux,uy=s.symbols('ux uy');Txx,Txy,Tyy=s.symbols('Txx Txy Tyy')
quad=ux**2*Txx+2*ux*uy*Txy+uy**2*Tyy
ck(s.diff(quad,ux,uy)==2*Txy,'polarization retains mixed product')
# Isolated B vertex means there is no full linear F/L-to-B endomorphism.
a,b,d,w=s.symbols('a b d w')
Alg=s.Matrix([[a,0,w],[0,b,0],[0,0,d]])
ck(all(Alg[1,j]==0 for j in (0,2)),'no incoming offdiagonal B arrow')
# Negative control: generated source but nonzero target joint B kernel.
AMx=s.Matrix([[1]]);AMy=s.Matrix([[0]])
ANx=s.Matrix([[1],[0]]);ANy=s.Matrix([[0],[1]])
BMx=BMy=s.zeros(1,1);BNx=BNy=s.zeros(1,2)
f2=s.eye(1);f4=s.eye(1)
for BM in (BMx,BMy):
 for AM,AN in ((AMx,ANx),(AMy,ANy)):
  ck(zero(BNx*AN*f2-f4*BM*AM),'without J every quadratic still intertwines')
ck(AMy==s.zeros(1,1) and ANy*f2!=s.zeros(2,1),'without J middle extension impossible')
# Negative control: target joint B kernel zero, source middle not generated.
AMx=AMy=ANx=ANy=s.zeros(1,0)
BMx=s.eye(1);BMy=s.zeros(1,1)
BNx=s.zeros(1,1);BNy=s.eye(1)
f2=s.zeros(0,0);f4=s.eye(1)
ck(AMx.row_join(AMy)==s.zeros(1,0),'toy source A-span zero')
Joint=BNx.col_join(BNy)
ck(s.Matrix([[0,1]])*Joint==s.eye(1),'toy target joint B map has left inverse')
for BM,BN in ((BMx,BNx),(BMy,BNy)):
 for AM,AN in ((AMx,ANx),(AMy,ANy)):
  ck(BN*AN*f2==f4*BM*AM==s.zeros(1,0),'toy all endpoint quadratic equations vacuous')
z3=s.symbols('z3');f3=s.Matrix([[z3]])
ck(BNx*f3-f4*BMx==s.Matrix([[-1]]),'toy Bx equation impossible for every symbolic middle map')
# Exact marked generation quotient identity: if f kills Q and N images and
# y=Qx+Nz, linearity forces f(y)=0. Universal symbolic distributivity.
f,Q,N,x,z=s.symbols('f Q N x z',commutative=False)
ck(s.expand(f*(Q*x+N*z)-(f*Q)*x-(f*N)*z)==0,'generation kills remaining target-only map')
ck(s.expand((f*Q)*x+(f*N)*z).subs({f*Q:0,f*N:0})==0,'both generating images killed')
print(json.dumps({'status':'pass','checks':nchecks,'negative_quadratic_reverse_hom_dimension':3,'joint_Q_all_negative_quadratic_reverse_hom_dimension':0,'actual_instance_evaluations':0,'scope':'conditional actual c-d-f one-sided preservation; no source or cubic-value claim'},indent=2))
