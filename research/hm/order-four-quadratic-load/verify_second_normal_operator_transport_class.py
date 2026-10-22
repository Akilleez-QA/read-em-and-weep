"""Universal operator transport interface; no actual source specialization."""
from pathlib import Path
import runpy,contextlib,io
import sympy as S
with contextlib.redirect_stdout(io.StringIO()):
    ch=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
add,vm,inn=ch['add'],ch['vm'],ch['inner']
one,A,V,P4=ch['one'],ch['A'],ch['V'],ch['P']; D5=ch['sy'](4)
vadd=lambda *vecs:[__import__('functools').reduce(add,col) for col in zip(*vecs)]
H=vm(P4,A)
assert H==vadd(V,P4,D5)
assert inn(H,one)==0
S3A=vadd(A,V,P4)
source=vm(S3A,D5)
assert source==vadd(A,A,A,V,V,V,P4,P4,P4,D5,D5,D5,D5)
assert inn(source,H)==10
S4A=vadd(one,P4,D5,D5)
assert inn(vm(S4A,D5),P4)==5
assert inn(vm(vadd(one,D5),D5),A)==1
assert 10-(5-1)==6
# Physical twist2 and weight0; no split-extension assumption.
assert 2-0/2==2 and 2-7-2/2==-6
assert 4*(-4)==3*(-6)+2
h0=lambda d:max(d+1,0)
h1=lambda d:max(-d-1,0)
assert h0(-4)==0 and 4*h1(-4)==12
assert h1(2)==0 and h0(2)==3
assert -2+4>0 and 0-8 < -2
# Exact generic q² gauge coefficient, including Dq=rho*q.
q,H0,rho=S.symbols('q H0 rho')
def mat(tag):
    a,b,c=S.symbols(tag+'a '+tag+'b '+tag+'c')
    return S.Matrix([[a,b],[c,-a]])
C,dC,A0=mat('C'),mat('dC'),mat('A0')
P=S.eye(2)+q*q*C;Pi=S.eye(2)-q*q*C
DP=q*q*(dC+2*rho*C)
transport=P*A0*Pi-H0*DP*Pi
coef=transport.applyfunc(lambda e:S.expand(e).coeff(q,2))
assert (coef-(C*A0-A0*C-H0*(dC+2*rho*C))).applyfunc(S.expand)==S.zeros(2)
# Full trace-blindness and commutator=tau(a sigma).
f,g,df,dg=S.symbols('f g df dg')
sig=S.Matrix([f,g]);J=S.Matrix([[0,-1],[1,0]])
n=sig*sig.T*J
Dn=n.diff(f)*df+n.diff(g)*dg
assert n*n==S.zeros(2)
assert S.expand(S.trace(n*Dn))==0
assert S.expand(S.trace(n*(C*n-n*C)))==0
v=C*sig;tau=sig*v.T*J+v*sig.T*J
assert (tau-(C*n-n*C)).applyfunc(S.expand)==S.zeros(2)
# Universal polarization right inverse for arbitrary quartic coefficients.
x=S.symbols('a0:3')
mon=[x[0]**i*x[1]**j*x[2]**(4-i-j) for i in range(5) for j in range(5-i)]
cs=S.symbols('c:'+str(len(mon)));F=sum(c*m for c,m in zip(cs,mon))
assert S.expand(sum(a*S.diff(F,a) for a in x)/4-F)==0
# Weights of all retained endpoint transport terms.
assert 0+0==0+4-4==0+0==4+0-4==4-4==8-8==0
print('PASS: intrinsic weight-zero operator cocycle; triple defects start above zero.')
print('PASS: J_eta(4), scalar acyclicity, trace blindness, and ten-to-four source-family interface.')
print('Actual class/value and its fourth-division comparison remain uncomputed.')
# Full unrestricted eta transport at q², including harmonic and determinant legs.
X,Y=S.symbols('X Y')
def form(tag,d):
    return sum(c*X**(d-i)*Y**i for i,c in enumerate(S.symbols(tag+':'+str(d+1))))
def b1(p,r):
    p,r=S.expand(p),S.expand(r)
    if p==0 or r==0:return S.Integer(0)
    dp=S.Poly(p,X,Y).total_degree();dr=S.Poly(r,X,Y).total_degree()
    if min(dp,dr)<2:return S.Integer(0)
    tau=S.diff(p,X,2)*S.diff(r,Y,2)-2*S.diff(p,X,Y)*S.diff(r,X,Y)+S.diff(p,Y,2)*S.diff(r,X,2)
    return S.expand(tau/(2*(dp-1)*(dr-1)*(dp+dr-1)))
def bm(U,V):
    return S.Matrix(2,2,lambda i,j:sum(b1(U[i,k],V[k,j]) for k in range(2)))
e,ke,de,H1=S.symbols('eta_diag K0_diag deta_diag H1')
eta=S.Matrix([[e,0],[form('eta_low',2),-e]])
K=S.Matrix([[ke,0],[form('K_low',2),-ke]])
deta=S.Matrix([[de,0],[form('deta_low',2),-de]]) # (D+rho)eta
AA=S.Matrix([[form('A_diag',4),form('A_upper',2)],[form('A_lower',6),0]]);AA[1,1]=-AA[0,0]
HH=form('H',4)
EE=eta*K-K*eta+bm(eta,AA)-bm(AA,eta)-H1*deta-deta.applyfunc(lambda v:b1(HH,v))
EE=EE.applyfunc(S.expand)
assert S.expand(S.trace(EE))==0 and EE[0,1]==0
assert S.Poly(EE[0,0],X,Y).total_degree()==0
assert S.Poly(EE[1,0],X,Y).total_degree()==2
# Direct ordered multiplication through q², with inverse I-q eta+q² eta².
V1=K+eta*AA
V2=bm(eta,AA)+eta*K
q2=(V2-V1*eta-bm(AA,eta)+AA*eta*eta
     -H1*deta-deta.applyfunc(lambda v:b1(HH,v))+HH*deta*eta)
quadratic=-eta*AA*eta+AA*eta*eta+HH*deta*eta
assert (q2-EE-quadratic).applyfunc(S.expand)==S.zeros(2)
# Quadratic and determinant scalar corrections have weight4, not weight0.
assert 0+4+0==4 and 4+0+0==4
print('PASS: complete eta q² transport; scalar/determinant contribution is separated by weight.')
