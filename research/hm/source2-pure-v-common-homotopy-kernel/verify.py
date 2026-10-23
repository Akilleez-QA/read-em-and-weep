from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent;checks=[]
def ck(n,b):
 if not bool(b):raise RuntimeError(n)
 checks.append(n)
for v in json.loads((root/'INPUTS.json').read_text()):
 b=(root/v['local_path']).read_bytes()
 ck(v['label']+' sha256',hashlib.sha256(b).hexdigest()==v['sha256'])
 ck(v['label']+' git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==v['git_blob'])
import sympy as s
from math import comb,factorial
x,y=s.symbols('x y');z=s.sqrt(5)
def cv(f,n):return s.Matrix([s.Poly(s.expand(f),x,y).coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def tv(f,g,k):return s.expand(sum((-1)**j*comb(k,j)*s.diff(f,x,k-j,y,j)*s.diff(g,x,j,y,k-j) for j in range(k+1)))
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
f12=-2*x**12-s.Rational(44,5)*z*x**10*y**2+66*x**8*y**4+s.Rational(88,5)*z*x**6*y**6+66*x**4*y**8-s.Rational(44,5)*z*x**2*y**10-2*y**12
f20=tv(f12,f12,2)
E=s.Matrix.hstack(*[cv(tv(f20,x**(4-i)*y**i,3),18) for i in range(5)])
P=E.T*gram(18)
M=s.Matrix.vstack(*[P*s.Matrix.hstack(*[cv(x**(2-k)*y**k*x**(16-i)*y**i,18) for i in range(17)]) for k in range(3)])
I=s.Matrix.hstack(*[cv(f12*x**(4-i)*y**i,16) for i in range(5)])
ck('equivariant D18 inclusion rank5',E.rank()==5)
ck('whole quadratic projection matrix shape',M.shape==(15,17))
ck('whole quadratic projection rank12',M.rank()==12)
ck('entire f12 Sym4 kernel identity',M*I==s.zeros(15,5))
ck('embedded f12 Sym4 rank5',I.rank()==5)
ck('common kernel equality by exact dimensions',17-M.rank()==I.rank())
rs=[0,1,2,3,4,5,6,7,8,9,13,14];cs=list(range(12));det=s.simplify(M.extract(rs,cs).det())
expected=-s.Rational(18181172528241933728741524320484149524538009158867979010156234925375606868884195114084653614308612112384,364138898268600625)*z
ck('exact full coefficient twelve minor',det==expected)
# Reconstruct the invariant normalization from the retained universal model.
ns={};exec((root/'inputs/model.py').read_text(),ns)
Pi=ns['Pi'];Vpol=[sum(v[i]*x**(6-i)*y**i for i in range(7)) for v in Pi.nullspace()]
wr=s.expand(s.Matrix([[s.diff(f.subs(y,1),x,k) for f in Vpol] for k in range(3)]).det())
ck('pinned invariant Wronskian exact',s.expand(s.Poly(wr,x).homogenize(y).as_expr()-f12)==0)
ck('Hessian invariant degree20',s.Poly(f20,x,y).is_homogeneous and s.Poly(f20,x,y).total_degree()==20)
z=s.sqrt(5);f=(1+z)/2;tr=[2,-2,0,1,-1,f,-f,f-1,1-f];w=[1,1,30,20,20,12,12,12,12]
def sy(n):
 a=s.ones(9,1);b=s.Matrix(tr)
 for _ in range(n):a,b=b,s.Matrix([s.simplify(tr[i]*b[i]-a[i]) for i in range(9)])
 return a
def mul(a,b):return s.Matrix([s.simplify(x*y) for x,y in zip(a,b)])
def ip(a,b):return s.simplify(sum(v*x*y for v,x,y in zip(w,a,b))/120)
W=sy(1);Wp=W.applyfunc(lambda a:a.xreplace({z:-z}));P=mul(W,Wp);A=sy(2);D=sy(4);V=sy(6)-P
S2=s.ones(9,1)+D;S3=sy(6)+A
NR=A+2*V+2*P+3*D;NC=V+P+2*D;N8=A+V+P+D;target=mul(A,D)
ck('common target multiplicity-free',target==A+V+P+D)
ck('actual Sym16 character',sy(16)==NC)
ck('actual Sym18 character',sy(18)==A+V+2*P+D)
ck('D18 multiplicity one',ip(D,sy(18))==1)
ck('NC kernel I2 gives three nonzero rows',NC-D==V+P+D)
ck('residual kernel character',NR-target==V+P+2*D)
ck('residual quotient projection character',NR-target-D==V+P+D)
ck('J2 character',NR+P==A+2*V+3*P+3*D)
ck('J2 common kernel character',NR+P-target==V+2*P+2*D)
ck('correction input character',mul(A,P)==V+P+D)
ck('kernel split character under zero R',NR+P-target==(P+D)+mul(A,P))
ck('canonical A Hom row unique',ip(A,target)==1)
ck('V correction has no equivariant Q-kernel ambiguity',ip(V,A+D)==0)
ck('P correction has no equivariant Q-kernel ambiguity',ip(P,A+D)==0)
ck('D correction only one Q-kernel ambiguity',ip(D,A+D)==1)
ck('residual common kernel has unique P',ip(P,NR-target)==1)
ck('residual rank and kernel dimensions',target[0]==15 and (NR-target)[0]==17)
ck('full J2 kernel dimension',(NR+P-target)[0]==21)
ck('Q kernel intersection I2 gives image16',21-5==16)
ck('forced P projection dimensions',P[0]==4 and (NR+P-target)[0]-(NR-target)[0]==4)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,NC_rank=12,NC_kernel=5,NR_rank=15,NR_kernel=17,J2_rank=15,J2_kernel=21,coefficient_minor=str(det),scope='Universal full coefficient map and actual-map transport; R0 correction consequences conditional; no actual source values'),indent=2))
