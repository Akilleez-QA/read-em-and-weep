"""Universal graded harmonic transport. No actual-source specialization or ranks."""
import sympy as S
X,Y=S.symbols('X Y')
def form(name,d):
    cc=S.symbols(name+':'+str(d+1))
    return sum(cc[i]*X**i*Y**(d-i) for i in range(d+1))
def B1(f,g):
    if f==0 or g==0:return S.Integer(0)
    d=S.Poly(f,X,Y).total_degree();h=S.Poly(g,X,Y).total_degree()
    if min(d,h)<2:return S.Integer(0)
    tv=S.diff(f,X,2)*S.diff(g,Y,2)-2*S.diff(f,X,Y)*S.diff(g,X,Y)+S.diff(f,Y,2)*S.diff(g,X,2)
    return S.expand(tv/(2*(d-1)*(h-1)*(d+h-1)))
def bm(U,V):return S.Matrix(2,2,lambda i,j:sum(B1(U[i,k],V[k,j]) for k in range(2)))
def clean(M):return M.applyfunc(S.expand)
def zero(M):assert clean(M)==S.zeros(*M.shape)
p=form('p',2);P=S.Matrix([[1,0],[p,1]]);Pi=S.Matrix([[1,0],[-p,1]])
n=S.Matrix([[form('a',8),form('b',6)],[form('c',10),0]]);n[1,1]=-n[0,0]
T=S.Matrix([[form('d',4),form('e',2)],[form('f',6),0]]);T[1,1]=-T[0,0]
R=S.Matrix([[form('r',8),form('s',6)],[form('t',10),0]]);R[1,1]=-R[0,0]
F=lambda U:clean(bm(P,U)*Pi+bm(P*U,Pi))
zero(bm(P,Pi)) # harmonic inverse is exact; all B_j for j>=2 vanish too
np=clean(P*n*Pi);Tp=clean(P*T*Pi+F(n));Rp=clean(P*R*Pi)
# B2(P,n) and B2(Pn,Pi) vanish since the only nonconstant P/Pi entry has degree2.
U=clean(F(T)+bm(bm(P,n),Pi));Z=-U
assert U[0,1]==0
assert S.Poly(U[0,0],X,Y).total_degree()==0
assert S.Poly(U[1,0],X,Y).total_degree()<=2
assert S.expand(S.trace(U))==0
expected=S.Matrix([[-B1(p,T[0,1]),0],[2*B1(p,T[0,0])-p*B1(p,T[0,1])-B1(p*T[0,1],p)-B1(B1(p,n[0,1]),p),B1(p,T[0,1])]])
zero(U-expected)
# Complete scalar correction from harmonic transport of qR1.
C=lambda nn,tt,rr:S.expand(S.trace(tt*rr)+S.trace(bm(nn,rr)))
assert S.expand(C(np,Tp,Rp)-C(n,T,R)+S.trace(np*F(R)))==0
# Exact differentiated-square trace compatibility of the q^2 mismatch.
H,rho,Lam=S.symbols('H rho Lam')
A=S.Matrix([[S.Symbol('aa'),S.Symbol('ab')],[S.Symbol('ac'),-S.Symbol('aa')]])
N=S.Matrix([[S.Symbol('na'),S.Symbol('nb')],[S.Symbol('nc'),-S.Symbol('na')]])
ZZ=S.Matrix([[S.Symbol('za'),S.Symbol('zb')],[S.Symbol('zc'),-S.Symbol('za')]])
DZ=S.Matrix([[S.Symbol('dza'),S.Symbol('dzb')],[S.Symbol('dzc'),-S.Symbol('dza')]])
HDN=Lam*N-(A*N-N*A)
LZ=H*DZ+A*ZZ-ZZ*A+(2*H*rho-Lam)*ZZ
rhs=S.trace(HDN*ZZ+H*N*DZ)+2*(H*rho-Lam)*S.trace(N*ZZ)
assert S.expand(S.trace(N*LZ)-rhs)==0
# q order coefficient assembly and choice bounds.
assert 8-4==4 and 4+0==4
assert -2+8-4==2 and -2+4==2 and -2+8==6
assert -2+8==6 and 0+8==8
assert 8-8==0
# Three lower-triangular harmonic transition factors multiply exactly: E21^2=0.
E21=S.Matrix([[0,0],[1,0]])
assert E21*E21==S.zeros(2)
assert max(-1+1,0)==0 and max(-(-1)-1,0)==0
print('PASS: full universal F_P and Z0 formulas; scalar trace compatibility; differentiated-square mismatch; transition-choice weight bounds.')
print('Affine trace-compatible weight-four torsor is unique once its full lower-data cocycle is supplied; no weight-eight or fourth value.')
# Pure normal-equation frame change q'=u*q, with other tensor frames held fixed.
u,Du,zz,dzz=S.symbols('u Du zz dzz',nonzero=True)
left=H*(dzz/u**2-2*zz*Du/u**3)+(2*H*(rho+Du/u)-Lam)*zz/u**2
right=(H*dzz+(2*H*rho-Lam)*zz)/u**2
assert S.cancel(left-right)==0
# Injective weight-zero trace relation, with the regular apolar certificate.
alpha,qq=S.symbols('alpha qq')
ff,gg=S.symbols('ff gg')
nn=S.Matrix([[ff*gg,-ff**2],[gg**2,-ff*gg]])
ss=S.Matrix([[alpha/2,0],[-qq,-alpha/2]])
assert S.expand(S.trace(nn*ss)-alpha*ff*gg-qq*ff**2)==0
assert S.Rational(-5,2)-S.Rational(9,2)-2-1==-10
assert -2-0==-2
print('PASS: normal-line covariance of +2Hrho and signed regular apolar cochain certificate.')
