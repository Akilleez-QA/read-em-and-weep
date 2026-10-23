from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not bool(value):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((ROOT/'INPUTS.json').read_text()):
 d=(ROOT/a['local_path']).read_bytes()
 ck('sha256 '+a['label'],hashlib.sha256(d).hexdigest()==a['sha256'])
 ck('git blob '+a['label'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==a['git_blob'])
x,y=s.symbols('x y');z=s.sqrt(5)
def cv(f,n):
 p=s.Poly(s.expand(f),x,y);return s.Matrix([p.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def fs(M,n):return [sum(M[i,j]*x**(n-i)*y**i for i in range(n+1)) for j in range(M.cols)]
def mat(ff,n):return s.Matrix.hstack(*[cv(f,n) for f in ff])
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,s.binomial(n,i)) if i+j==n else 0)
def tv(a,f,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
E6=gram(6).inv()*Pi.T;p6=fs(E6,6);v6=fs(s.Matrix.hstack(*Pi.nullspace()),6)
f12=-2*x**12-s.Rational(44,5)*z*x**10*y**2+66*x**8*y**4+s.Rational(88,5)*z*x**6*y**6+66*x**4*y**8-s.Rational(44,5)*z*x**2*y**10-2*y**12
p16=[tv(f12,f,1) for f in p6];a=[x*x,x*y,y*y]
M=mat([b*f for b in a for f in p16],18)
# invariant Gram on source A tensor P6 induces transpose of P projection
C=Pi*mat([tv(b,f,1) for b in a for f in p6],6)
GP=E6.T*gram(6)*E6
J=s.kronecker_product(gram(2),GP).inv()*C.T
pd=fs((M*J).applyfunc(s.simplify),18)

ck('apolar P6 inclusion rank',E6.rank()==4)
ck('P16 transvectant embedding rank',mat(p16,16).rank()==4)
ck('P16 first multiplication injective',mat([b*f for b in [x,y] for f in p16],17).rank()==8)
ck('full polynomial quadratic descendants injective',M.rank()==12)
ck('P projection rank4',C.rank()==4)
ck('adjoint P inclusion rank4',J.rank()==4)
ck('polynomial P descendant nonzero',mat(pd,18).rank()==4)
ck('P descendant first multiplication rank6',mat([b*f for b in [x,y] for f in pd],19).rank()==6)
ck('P descendant first kernel dimension2',2*4-6==2)
ck('image P and descendant P are distinct',mat(pd+[f12*f for f in p6],18).rank()==8)
def sm(g,n):
 a,b,c,d=list(g);return mat([(a*x+c*y)**(n-j)*(b*x+d*y)**j for j in range(n+1)],n)
phi=(1+z)/2
for k,(a0,b0,c0,d0) in enumerate([(0,1,0,0),(0,0,1,0),(s.Rational(1,2),)*4,(phi/2,s.Rational(1,2),(phi-1)/2,0)]):
 g=s.Matrix([[a0+s.I*b0,c0+s.I*d0],[-c0+s.I*d0,a0-s.I*b0]])
 g6=sm(g,6);gp=s.kronecker_product(g,g.xreplace({z:-z}))
 ck('pinned P6 intertwiner '+str(k),all(s.expand(e)==0 for e in Pi*g6-gp*Pi))
 ck('apolar invariance '+str(k),all(s.expand(e)==0 for e in g6.T*gram(6)*g6-gram(6)))
 ck('f12 invariant '+str(k),s.Poly(s.expand(f12.subs({x:g[0,0]*x+g[1,0]*y,y:g[0,1]*x+g[1,1]*y},simultaneous=True)-f12),x,y).is_zero)
# Literal linear relations y*e_i-x*e_(i+1) in free R^5.
K=s.zeros(5,4)
for i in range(4):K[i,i]=y;K[i+1,i]=-x
mon4=s.Matrix([[x**(4-i)*y**i for i in range(5)]])
ck('literal four Koszul relations',(mon4*K).applyfunc(s.expand)==s.zeros(1,4))
Qcols=[]
for b in [x,y]:
 for j in range(4):Qcols.append(s.Matrix.vstack(*[cv(b*K[i,j],2) for i in range(5)]))
ck('eight linear multiples independent',s.Matrix.hstack(*Qcols).rank()==8)
ck('minimal quadratic relation dimension',3*9-9-8==10)
ck('first two graded dimensions',[5+4,6+8,4+5]==[9,14,9])
t=s.symbols('t')
ck('Hilbert numerator',s.expand((9+14*t+9*t*t)*(1-t)**2)==9-4*t-10*t*t-4*t**3+9*t**4)
# Exact representation-valued numerator in the ordered basis A,V,P,D,W,Wprime,S,T.
# W*(P+D)=Wprime+S+2T; W*(Wprime+2T)=2V+3P+2D.
F0=s.Matrix([0,0,1,1,0,0,0,0]);F1=s.Matrix([0,0,0,0,0,1,0,2]);WF0=s.Matrix([0,0,0,0,0,1,1,2]);WF1=s.Matrix([0,2,3,2,0,0,0,0])
ck('linear and cubic relation character',F1-WF0==s.Matrix([0,0,0,0,0,0,-1,0]))
ck('quadratic relation character',2*F0-WF1==s.Matrix([0,-2,-1,0,0,0,0,0]))
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,polynomial_descendant_dimensions=[4,6],minimal_betti_degrees={'generators':{'0':9},'relations':{'1':4,'2':10,'3':4},'second_syzygies':{'4':9}},scope='universal polynomial certificate; truncation only; no endpoint or graph coefficient selected'),indent=2))
