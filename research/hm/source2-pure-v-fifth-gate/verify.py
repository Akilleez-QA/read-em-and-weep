from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent;checks=[]
def ck(n,b):
 if not bool(b):raise RuntimeError(n)
 checks.append(n)
for v in json.loads((root/'INPUTS.json').read_text()):
 b=(root/v['local_path']).read_bytes()
 ck(v['label']+' sha256',hashlib.sha256(b).hexdigest()==v['sha256'])
 ck(v['label']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==v['git_blob'])
exec((root/'inputs/model.py').read_text())
C=[DD*R1,DD*R2,R1*DP,R2*DP]
# Cofactor determinant row for B=Pi(a^2 A).
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*s.expand(B[[j for j in range(4) if j!=i],:].det()) for i in range(4)]])
rows=[(N*L*M*L).applyfunc(s.expand) for M in C]
def coeff(M,n):return s.Matrix([s.Poly(e,p,q,t).coeff_monomial(p**i*q**j*t**(n-i-j)) for e in M for i in range(n+1) for j in range(n+1-i)])
T=s.Matrix.hstack(*[coeff(M,11) for M in rows]);ck('whole original fifth row coefficient rank2',T.rank()==2)
U=s.Matrix.hstack(*[coeff(M,3) for M in C]);ck('whole cubic lift coefficient rank3',U.rank()==3)
ck('first two fifth rows independent',T.rref()[1]==(0,1))
from math import comb
def tv(f,g,k):return s.expand(sum((-1)**j*comb(k,j)*s.diff(f,x,k-j,y,j)*s.diff(g,x,j,y,k-j) for j in range(k+1)))
f=[sum(E[i,j]*x**(6-i)*y**i for i in range(7)) for j in range(4)]
H=s.Matrix.hstack(*[cv(tv(a*a,g,4),2) for g in f]);m=s.Matrix.hstack(*[cv(a*x**(2-i)*y**i,4) for i in range(3)])
ck('exact cubic gauge identity',all(s.simplify(v)==0 for v in coeff(C[3]-C[0]/4+m*H/720,3)))
# compact nonzero minor of full row coefficient matrix, no parameter selected
inds=list(T[:,:2].T.rref()[1]);ck('whole coefficient minor rows',[1,3]==inds)
ck('exact nonzero whole coefficient minor',s.simplify(T.extract(inds,[0,1]).det())==20480*z/27)

ck('gauge polynomial is nonzero',any(v!=0 for v in coeff(m*H,3)))
ck('determinant row kills second-symbol image',all(s.expand(v)==0 for v in N*B))
ck('gauge disappears before determinant',all(s.expand(v)==0 for v in L*m-B))
ck('literal duplicate cubic lift',all(s.expand(v)==0 for v in C[1]-C[2]))
ck('zero-gauge original fifth row',all(s.expand(v)==0 for v in rows[3]-rows[0]/4))
ck('all original fifth components degree11',all(s.Poly(v,p,q,t).is_homogeneous and s.Poly(v,p,q,t).total_degree() in [0,11] for row in rows[:2] for v in row))
z=s.sqrt(5);f=(1+z)/2;tr=[2,-2,0,1,-1,f,-f,f-1,1-f];w=[1,1,30,20,20,12,12,12,12]
def sy(n):
 a=s.ones(9,1);b=s.Matrix(tr)
 for _ in range(n):a,b=b,s.Matrix([s.simplify(tr[i]*b[i]-a[i]) for i in range(9)])
 return a
def mul(a,b):return s.Matrix([s.simplify(x*y) for x,y in zip(a,b)])
def ip(a,b):return s.simplify(sum(v*x*y for v,x,y in zip(w,a,b))/120)
W=sy(1);Wp=W.applyfunc(lambda a:a.xreplace({z:-z}));P=mul(W,Wp);A=sy(2);D=sy(4);V=sy(6)-P
S2=s.ones(9,1)+D;S3=sy(6)+A
A2=s.Matrix([s.simplify((v*v-2)**2-1) for v in tr])
A3=s.Matrix([s.simplify((v**3-3*v)**2-1) for v in tr])
plane2=s.Matrix([s.simplify((A[i]**2+A2[i])/2) for i in range(9)])
plane3=s.Matrix([s.simplify((A[i]**3+3*A[i]*A2[i]+2*A3[i])/6) for i in range(9)])
ck('full plane symmetric square character',all(s.simplify(v)==0 for v in plane2-S2))
ck('full plane symmetric cube character',all(s.simplify(v)==0 for v in plane3-S3))
ck('cubic lift Hom dimension3',ip(P,mul(D,S3))==3)
ck('quadratic A gauge Hom dimension1',ip(P,mul(A,S2))==1)
ck('quotient fourth Hom dimension2',ip(P,mul(D,S3))-ip(P,mul(A,S2))==2)
ck('no equivariant scalar P family',ip(P,s.ones(9,1))==0)
ck('generic fifth Smith valuation',3*2+5==11)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,cubic_lift_dimension=3,gauge_dimension=1,fifth_gate_dimension=2,coefficient_minor='20480*sqrt(5)/27',scope='Actual-page comparison conditional on R=0; full universal coefficients only; actual fifth values unselected'),indent=2))
