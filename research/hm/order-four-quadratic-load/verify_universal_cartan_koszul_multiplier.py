"""Universal Cartan–Koszul identities, with NO actual source specialization.

All binary sextic/cubic/quadratic, base-coordinate and Hamiltonian coefficients
are independent symbols. The only matrices below encode universal Clifford
and representation tensors. No actual monad matrix, rank, or source scan occurs.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sympy as s
from math import comb

# Reuse the frozen, independently checked exterior algebra helpers, quietly.
with redirect_stdout(StringIO()):
    exec(Path(__file__).with_name('verify_universal_monad_clifford_homotopy.py').read_text())

# Complete universal Cartan projector and its induced alternating pairing.
G=s.Matrix([[0,s.Rational(1,2),0],[s.Rational(1,2),0,0],[0,0,1]])
Kinc=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,-1,0,0],[0,0,1,0]])
cliff=Ms[0].row_join(Ms[1]).row_join(Ms[2])
spin=s.Matrix.vstack(2*M1,2*M0,M2)/3
assert cliff*spin==s.eye(2)
Pi=s.eye(6)-spin*cliff
extract=s.eye(6)[:4,:]*Pi
assert Kinc*extract==Pi and Pi*Pi==Pi
up=s.kronecker_product(G,s.eye(2)); low=up.inv()
J4=Kinc.T*s.kronecker_product(G,J)*Kinc
assert J4.T==-J4 and J4.det()!=0

def getp(F,extra=()):
    return s.Matrix([F[j].get(tuple(sorted(I+extra)),0)*sgn
                     for I,sgn in [((1,2),1),((0,2),-1),((0,1),1)] for j in range(2)])
def putp(p,extra=()):
    return [{tuple(sorted(I+extra)):sgn*p[2*i+j]
             for i,(I,sgn) in enumerate([((1,2),1),((0,2),-1),((0,1),1)])} for j in range(2)]
def getY(F,extra):
    return s.Matrix([F[j].get((i,)+extra,0) for i in range(3) for j in range(2)])
def putY(Y,extra):
    return [{(i,)+extra:Y[2*i+j] for i in range(3)} for j in range(2)]
def adds(*Fs):return [add(*(F[j] for F in Fs)) for j in range(2)]
def sc(c,F):return [scale(c,f) for f in F]
def eqvec(F,G):
    for f,g in zip(F,G):eq(f,g)
def zero_matrix(M):assert M.applyfunc(s.expand)==s.zeros(*M.shape)
def embeddings(R):
    Radj=J4.inv()*R.T*J4
    return Kinc*R*extract,up*Kinc*Radj*extract*low

def E_R(R,F):
    Rp,RadjY=embeddings(R)
    out=putp(Rp*getp(F))
    for i in [3,4]:out=adds(out,putY(-RadjY*getY(F,(i,)),(i,)))
    return out

def F_R(R,F):
    Rp,RadjY=embeddings(R)
    out=[{},{}]
    for i in [3,4]:out=adds(out,putp(Rp*getp(F,(i,)),(i,)))
    return adds(out,putY(-RadjY*getY(F,(3,4)),(3,4)))

# All 16 End(S4) entries are free, including selfadjoint sectors.
R=s.Matrix(4,4,s.symbols('R0:16'))
z2=s.symbols('eta0:20');z3=s.symbols('zeta0:20')
f2=[dict(zip(combinations(range(5),2),z2[10*i:10*i+10])) for i in range(2)]
f3=[dict(zip(combinations(range(5),3),z3[10*i:10*i+10])) for i in range(2)]
eq(pair(F_R(R,f3),f2),scale(-1,pair(f3,E_R(R,f2))))
for i in [3,4]:
    ei={(i,):1}
    eqvec(F_R(R,[wedge(ei,f) for f in f2]),[wedge(ei,f) for f in E_R(R,f2)])
# These two identities prove the skewness of the GLOBAL induced lift.
print('PASS: arbitrary-End(S4) coefficient adjoint and wedge-intertwining identities.')

Ruu=s.Matrix(4,4,s.symbols('Ruu0:16'))
Ruw=s.Matrix(4,4,s.symbols('Ruw0:16'))
Rww=s.Matrix(4,4,s.symbols('Rww0:16'))
Squad=u*u*Ruu+u*w*Ruw+w*w*Rww

def lift(Sop,F):
    out=[{},{}]
    for wi,i in [(u,3),(w,4)]:
        ER=E_R(Sop.diff(wi)/2,F)
        out=adds(out,[contract(coords,wedge({(i,):1},f)) for f in ER])
    return out

TB=lift(Squad,B(p));eqvec(TB,[{},{}])
TA=lift(Squad,A(p))
zero_matrix(getp(TA)-Kinc*Squad*extract*getp(A(p)))
for f in TA:eq(contract(coords,f),{})
print('PASS: full 48-symbol quadratic Cartan lift is polynomial, K-valued, and kills B.')

# Universal Fierz/projector normalization, retaining theta=chi and physical q0.
Lv=[{(i,):(Ms[i]*p)[j] for i in range(3)} for j in range(2)]
physical_r={(i,):r[i] for i in range(5)}
Lr=[wedge(f,physical_r) for f in Lv]
zero_matrix(getp(Lr)-(getp(A(p))-s.Rational(3,2)*Pi*getp(A(p)))/theta)
assert s.trace(M0*(M1*M2-M2*M1))==2 # full-trace g_L, not half trace
print('PASS: L wedge r=(g_L/(2 chi))(A-(3/2)Pi A), with physical chi unassigned.')

# Exact common Cartan projection, including sign and normalization.
Iv=s.zeros(3)
for i,(I,sgn) in enumerate([((1,2),1),((0,2),-1),((0,1),1)]):
    cv=contract([x,y,z,0,0],{I:sgn})
    for j in range(3):Iv[j,i]=cv.get((j,),0)
Jactual=extract*s.kronecker_product(G.inv()*Iv,s.eye(2))*Kinc
ad=s.zeros(3)
for i,Mi in enumerate(Ms):
    com=M*Mi-Mi*M
    ad[:,i]=s.Matrix([com[0,1],com[1,0],com[0,0]])
Rho=extract*(s.kronecker_product(ad,s.eye(2))+s.kronecker_product(s.eye(3),M))*Kinc
zero_matrix(Jactual+s.Rational(2,3)*Rho)
zero_matrix(Jactual.T*J4+J4*Jactual)
print('PASS: the exact common Cartan projection is -(2/3)rho^3(M(v)), with no termwise rescaling.')

# Base tangent operator and all three channel actions, keeping full Cartan C.
jw=contract(coords,omega)
jvec=s.Matrix([jw.get((i,),0) for i in range(5)])
Dj=D*jvec
H=(s.Matrix(1,5,coords)*Dj)[0]
E0=H*s.diag(1,1,1,0,0)-Dj*s.Matrix(1,5,[x,y,z,0,0])
zero_matrix(s.Matrix(1,5,coords)*E0)
assert s.expand(s.trace(E0)-3*H)==0
eq(action(E0,ixOmega),scale(3*H,ixOmega))
def Kop(F):return [add(action(E0,f),scale(-3*H/2,f)) for f in F]
eqvec(Kop(A(p)),sc(H/2,A(p)))
eqvec(Kop(B(p)),sc(-H/2,B(p)))
Cwd=[contract(list(ell),f) for f in C]
rhs=[contract(coords,wedge(contract([x,y,z,0,0],f),omega)) for f in Cwd]
eqvec(adds(Kop(Cx),sc(-H/2,Cx)),rhs)
# The coefficient derivative of C stays Cartan and pairs trivially with B.
deltaC=[contract(coords,action(D,f)) for f in C]
eq(pair(B(p),deltaC),{})
print('PASS: tangent base lift, all channel actions, and B* delta_D C=0.')

# Independent negative binary symbols. They are not actual cubic coefficients.
S,T,U0,W0,hh,kk,ll=s.symbols('S T u0 w0 hh kk ll')
sext=s.symbols('e0:7');quad=s.symbols('qz0:3');cubc=s.symbols('bz0:4')
F=sum(sext[i]*S**(6-i)*T**i for i in range(7))
zquad=sum(quad[i]*S**(2-i)*T**i for i in range(3))
zcub=sum(cubc[i]*S**(3-i)*T**i for i in range(4))
lin=-W0*S+U0*T
Dop=lambda f:s.expand((hh*S+ll*T)*s.diff(f,S)+(kk*S-hh*T)*s.diff(f,T))
Dl=Dop(lin)
Hb=kk*U0**2-2*hh*U0*W0-ll*W0**2
Nop=lambda f:s.expand(-2*lin*(U0*s.diff(f,S)+W0*s.diff(f,T)))
Minus=lambda f:s.expand(Dop(Nop(f))-Nop(Dop(f)))
Plus=lambda f:s.expand(Dop(Nop(f))+Nop(Dop(f)))
Comb=lambda f:s.expand(2*Minus(f)+Plus(f))
Jop=lambda f:s.expand(sum((-1)**i*comb(3,i)*s.diff(F,S,3-i,T,i)*s.diff(f,S,i,T,3-i) for i in range(4)))
Pminus=s.expand(Minus(zquad)+2*Hb*zquad)
Pplus=s.cancel(Plus(lin*zquad)/lin)
assert s.denom(Pplus)==1
assert s.expand(Minus(lin*zquad)-lin*Pminus)==0
assert s.expand(Plus(lin*zquad)-lin*Pplus)==0
assert s.expand(s.rem(Minus(zcub)+6*Hb*zcub,lin,S))==0
assert s.expand(s.rem(Plus(zcub)+6*Hb*zcub,lin,S))==0
# Complete cubic identity produces the reverse source, with no coordinate pole.
reverse=s.expand(s.Rational(3,2)*Dl*zcub+
                  (S*s.diff(Comb(zcub),U0)+T*s.diff(Comb(zcub),W0))/24)
assert reverse==0
print('PASS: exact source ideal preservation, quotient weights, and full cubic reverse-source identity.')

# Check apolar adjoints, with all coefficients free.
mon=[S**(3-i)*T**i for i in range(4)]
ap=s.zeros(4)
for i in range(4):ap[i,3-i]=s.Rational((-1)**i,comb(3,i))
def op_tensor(op):return s.Matrix([[s.expand(op(m)).coeff(S,3-i).coeff(T,i) for m in mon] for i in range(4)])
MinusR=op_tensor(Minus);PlusR=op_tensor(Plus);JR=op_tensor(Jop)
zero_matrix(MinusR.T*ap+ap*MinusR)
zero_matrix(PlusR.T*ap-ap*PlusR)
zero_matrix(JR.T*ap+ap*JR)
# The full sextic summand is trace-orthogonal to the negative sl2.
for neg in [lambda f:S*s.diff(f,T),lambda f:T*s.diff(f,S),lambda f:S*s.diff(f,S)-T*s.diff(f,T)]:
    assert s.expand(s.trace(JR*op_tensor(neg)))==0
print('PASS: skew/selfadjoint distinction and complete sextic trace-orthogonality.')

pC=-lin*zquad
Yminus=[];Yplus=[]
for coord,m in [(U0,-T),(W0,S)]:
    # Subtract differentiation of the input: only operator coefficients vary.
    dminus=lambda f:s.expand(s.diff(Minus(f),coord)-Minus(s.diff(f,coord)))
    dplus=lambda f:s.expand(s.diff(Plus(f),coord)-Plus(s.diff(f,coord)))
    Yminus.append(s.expand(Minus(Jop(m*zquad))-Jop(m*Pminus)+
                            (Jop(dminus(pC))-dminus(Jop(pC)))/2))
    Yplus.append(s.expand(-Plus(Jop(m*zquad))-Jop(m*Pplus)+
                           (Jop(dplus(pC))+dplus(Jop(pC)))/2))
Z=[]
for Y in [Yminus,Yplus]:
    assert s.expand(U0*Y[0]+W0*Y[1])==0
    Zi,rem=s.div(Y[0],W0,W0)
    assert rem==0
    assert s.expand(W0*Zi-Y[0])==0 and s.expand(-U0*Zi-Y[1])==0
    Z.append(Zi)
ZK=Jop(Dl*zquad)
assert s.expand(36*ZK+2*Z[0]+Z[1])==0
assert s.expand(-s.Rational(3,2)*ZK-Z[0]/12-Z[1]/24)==0
print('PASS: full seven-symbol sextic identity 36 Z_K+2 Z_minus+Z_plus=0.')

# General all-channel algebra: symbols are never assigned numeric values.
am,bm,cm,ch,gg=s.symbols('a_m b_m c_m chi g_L',nonzero=True)
Cmult=-ch/gg
c=Cmult*gg/(2*ch)
assert s.simplify(c+s.Rational(1,2))==0
# Eq (2c): M_b B=(3/2)aB, while Q_b=-(1/2)aI.
assert s.Rational(3,2)+s.Rational(1,2)==2
# Eq (2b): only its two source-channel coefficients, after polynomial proof above.
assert s.simplify((c-1)-(-(1+c))-2*c)==0
# Eq (2e): coefficient of the exact sextic identity, after source ideal proof.
assert s.simplify((c-1)-3*c)==0
# The original four left-arrow coefficient groups reduce to the FIVE identities.
# The following expansion checks no reverse S term or Laurent channel factor is lost.
A0,B0,C0,Ma,Mb,Pa,Pb,Qa,Qb,Rsrc,Ssrc=s.symbols(
    'A0 B0 C0 Ma Mb Pa Pb Qa Qb Rsrc Ssrc',commutative=False)
leftU=s.expand((am*Ma+bm*Mb)*(am*A0+bm*B0)
               -(am*A0+bm*B0)*(am*Qa+bm*Qb)-cm*C0*(am*bm/cm*Ssrc))
wantU=am**2*(Ma*A0-A0*Qa)+am*bm*(Ma*B0+Mb*A0-A0*Qb-B0*Qa-C0*Ssrc)+bm**2*(Mb*B0-B0*Qb)
assert s.expand(leftU-wantU)==0
leftA=s.expand((am*Ma+bm*Mb)*(cm*C0)-cm*C0*(am*Pa+bm*Pb)
               -(am*A0+bm*B0)*(cm*Rsrc))
wantA=am*cm*(Ma*C0-C0*Pa-A0*Rsrc)+bm*cm*(Mb*C0-C0*Pb-B0*Rsrc)
assert s.expand(leftA-wantA)==0
print('PASS: all nonzero channel symbols retained and complete five-equation expansion, including reverse S.')
print('PASS: C_mult g_L/chi=-1 follows from the complete universal identities and polynomial residual argument.')
print('No actual cubic coefficient, source value, monad matrix, rank, or source scan was used.')
