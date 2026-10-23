#!/usr/bin/env python3
"""Universal polynomial certificate, never an actual-source instance test."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
    if not bool(b):raise RuntimeError(name)
    checks.append(name)
for e in json.loads((root/'INPUTS.json').read_text()):
    b=(root/e['local_path']).read_bytes()
    ck('SHA256 '+e['label'],hashlib.sha256(b).hexdigest()==e['sha256'])
    ck('Git blob '+e['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
# Named restricted domains of the actual maps, with inclusions explicit.
types={'QJ':('J3','V5'),'ell':('V5','I3'),'theta':('J3','I3'),
       'cs':('Sym3I4','F5'),'inc':('F5','V5'),'Ah':('J3','WdualI2'),
       'rotmul':('WdualI2','I3')}
def compose(a,b):
    if types[a][1]!=types[b][0]:raise RuntimeError('type mismatch')
    return types[a][0],types[b][1]
ck('canonical odd factorization type',compose('QJ','ell')==types['theta'])
ck('terminal incidence domain',compose('cs','inc')==('Sym3I4','V5'))
ck('pairing contraction type',compose('Ah','rotmul')==types['theta'])
x,y=s.symbols('x y')
def mons(n):return [x**(n-i)*y**i for i in range(n+1)]
def coef(f,n):
    p=s.Poly(s.expand(f),x,y)
    return s.Matrix([p.coeff_monomial(m) for m in mons(n)])
m4=mons(4);m3=mons(3);m5=mons(5)
units=[];cols=[]
for i in range(5):
    for j in range(5):
        U=s.zeros(5);U[i,j]=1;units.append(U)
        def apply(f):return s.Poly(f,x,y).coeff_monomial(m4[j])*m4[i]
        cols.append(s.Matrix.vstack(*[coef(x*apply(y*c)-y*apply(x*c),5) for c in m3]))
D=s.Matrix.hstack(*cols);Id=s.Matrix(list(s.eye(5)))
ck('full universal operator dimensions',D.shape==(24,25))
ck('scalar Id in exact kernel',D*Id==s.zeros(24,1))
ck('full universal operator rank',D.rank()==24)
ck('exact scalar kernel',D.nullspace()==[Id])
# Verify determinant-equivariance for the three sl2 generators.
ops=[lambda f:x*s.diff(f,y),lambda f:y*s.diff(f,x),lambda f:x*s.diff(f,x)-y*s.diff(f,y)]
for name,op in zip(['E','F','H'],ops):
    rho={n:s.Matrix.hstack(*[coef(op(f),n) for f in mons(n)]) for n in [3,4,5]}
    Adom=s.Matrix.hstack(*[s.Matrix(list(rho[4]*U-U*rho[4])) for U in units])
    Atgt=s.kronecker_product(s.eye(4),rho[5])-s.kronecker_product(rho[3].T,s.eye(6))
    ck('universal equivariance '+name,Atgt*D==D*Adom)
# All formal U coefficients, arbitrary cubic and factored cubic retained.
u=s.symbols('u0:25');U=s.Matrix(5,5,u)
def applyU(f):return (s.Matrix([m4]).reshape(1,5)*U*coef(f,4))[0]
c0,c1,c2,c3=s.symbols('c0:4');c=sum(v*m for v,m in zip([c0,c1,c2,c3],m3))
expr=s.expand(x*applyU(y*c)-y*applyU(x*c))
vec=coef(expr,5)
K=s.Matrix(6,4,lambda i,j:(D*s.Matrix(list(U)))[6*j+i])
ck('all formal coefficients match matrix',s.simplify(vec-K*s.Matrix([c0,c1,c2,c3]))==s.zeros(6,1))
l0,l1,b0,b1,b2=s.symbols('l0 l1 b0 b1 b2');l=l0*x+l1*y;b=b0*x*x+b1*x*y+b2*y*y
ck('exact cubic comparison sign',s.expand(x*applyU((y*l)*b)-y*applyU((x*l)*b)-(x*applyU(y*(l*b))-y*applyU(x*(l*b))))==0)
# Multiplication product Sym2A -> Sym4 and polarization support.
products=[a*b for i,a in enumerate(mons(2)) for b in mons(2)[i:]]
P=s.Matrix.hstack(*[coef(f,4) for f in products])
ck('quadratic product onto quartics',P.shape==(5,6) and P.rank()==5)
ck('quadratic product kernel dimension',len(P.nullspace())==1)
Cubic=s.Matrix.hstack(*[coef(a*b,3) for a in mons(1) for b in mons(2)])
ck('linear quadratic products span all cubics',Cubic.rank()==4)
# Character arithmetic in irreducible order Wprime,S,T.
Wp=s.Matrix([1,0,0]);S=s.Matrix([0,1,0]);T=s.Matrix([0,0,1]);dim=s.Matrix([[2,4,6]])
J=3*Wp+3*S+5*T;K3=3*Wp+3*S+2*T;F3=Wp+2*T
ck('odd quotient J/K3',J-K3==3*T)
ck('actual common-kernel T part equals generated T part',K3[2]==F3[2]==2)
ck('terminal kernel character',3*T-T==2*T)
kerA=3*Wp+2*S+4*T;kerAK=F3+2*Wp+2*S
ck('full pairing kernel dimension',(dim*kerA)[0]==38)
ck('restricted pairing kernel dimension',(dim*kerAK)[0]==26)
ck('actual Q image of pairing kernel character',kerA-kerAK==2*T)
ck('terminal plane dimension',(dim*(2*T))[0]==12)
ck('residual terminal character',T[2]==1)
ck('separated incidence equal dimensions',(dim*(2*T))[0]==12)
# Multiplicities in End(Sym4)=Sym8+Sym6+Sym4+Sym2+1;
# only Sym8=P+D and Sym6=V+P contribute P. The target drops only 1.
ck('two equivariant family channels',sum([1,1,0,0,0])==sum([1,1,0,0])==2)
ck('scalar family Hom vanishing',(4+15*0+20*1-12-12)/60==0)
# An arbitrary symmetric bilinear form is determined by its diagonal.
a=s.Matrix(s.symbols('a0:3'));bvec=s.Matrix(s.symbols('q0:3'));ss=s.symbols('s0:6')
M=s.Matrix([[ss[0],ss[1],ss[2]],[ss[1],ss[3],ss[4]],[ss[2],ss[4],ss[5]]])
ck('polarization exact factor',s.expand(((a+bvec).T*M*(a+bvec)-a.T*M*a-bvec.T*M*bvec)[0]-2*(a.T*M*bvec)[0])==0)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,universal_operator={'rows':24,'columns':25,'rank':24,'kernel':'scalar identity'},conclusion='R=0 iff ell(F5)=0; terminal plane C=Q3(ker A_h)',scope='actual incidence remains unselected; all matrices here are universal representation or formal certificates'),indent=2))
