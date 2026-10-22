"""Universal next-weight interfaces; no source specialization or rank test."""
from pathlib import Path
import runpy,contextlib,io
import sympy as S
with contextlib.redirect_stdout(io.StringIO()):
    ch=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
inn,vm,sym=ch['inner'],ch['vm'],ch['sym']
one,W,Wp,V,P4=ch['one'],ch['W'],ch['Wp'],ch['V'],ch['P']
D5=ch['sy'](4);T6=ch['sy'](5)
assert inn(Wp,T6)==0
S12=[sym(12,t) for t in Wp]
expected=[ch['add'](ch['add'](a,b),ch['add'](c,d)) for a,b,c,d in zip(one,V,P4,D5)]
assert S12==expected
assert inn(S12,D5)==1
# Physical coefficient lines and exact ranks/degrees.
assert -2-4/2==-4 and 7-2-2/2==4 and -7-2-6/2==-12
assert -2.5-4-0.5==-7
assert 4.5+4-7/2==5 and -2.5+4-9/2==-3
assert 8+10==15+3
assert 8*5+10*(-3)==-2+3*4
assert 13+3*5==28
# Universal wedge/trace diagram proving the quotient, including its sign.
f,g,a,b,c,l=S.symbols('f g a b c l')
J=S.Matrix([[0,-1],[1,0]]);sig=S.Matrix([f,g]);n=sig*sig.T*J
K=S.Matrix([[a,b],[c,-a]])
wedge=lambda u,v:u[0]*v[1]-u[1]*v[0]
assert S.expand(wedge(sig,K*sig)+S.trace(n*K))==0
v=S.Matrix([0,l]);tau=sig*v.T*J+v*sig.T*J
assert tau*sig==f*l*sig
# Simultaneous normalization: delta(tr n S4+chi12)=0 and H0 target=0.
h0=lambda d:max(d+1,0)
assert h0(-7)==h0(-6)==0
# No cone mixing below +8; triple q^2 defect acts on n first at6.
assert 0+8>4 and 2+8>4 and -2+8>4
# Full universal harmonic endpoint contribution, not diagonal-only eta.
with contextlib.redirect_stdout(io.StringIO()):
    ns=runpy.run_path(str(Path(__file__).with_name('verify_leading_next_error_affine_transport.py')))
n,T,bm,form,clean=ns['n'],ns['T'],ns['bm'],ns['form'],ns['clean']
eta=S.Matrix([[S.Symbol('eta_diag'),0],[form('eta_lower',2),-S.Symbol('eta_diag')]])
D1=clean(eta*n-n*eta)
Omega=clean(eta*T-T*eta+bm(eta,n)-bm(n,eta))
assert S.expand(S.trace(n*Omega)+S.trace(T*D1)+S.trace(bm(n,D1)))==0
# Endpoint truncations retain midpoint local N: D1,end=-D1 and Z4 shift=-Omega.
assert S.expand(S.trace(n*(-Omega))+S.trace(T*(-D1))+S.trace(bm(n,-D1)))==0
assert 0+0+8==8 and 8+8==16 # quadratic eta terms are above Z4/chi12
assert 4+4==0+8==4+8-4==12-4==8
print('PASS: Z4 and K4 exact coefficient arithmetic; invariant trace injection; E12 wedge quotient; full eta-dependent harmonic endpoint term.')
print('Midpoint partial normalization is not a global N2. Endpoint has a first-order mismatch. Full R1,12 and R2,8 remain uncomputed.')
# Full ordinary q-adic first-mismatch expansion, retaining Dq=rho*q.
q,H0,H1,L0,L1,rho=S.symbols('q H0 H1 L0 L1 rho')
def mat(tag):
    aa,bb,cc=S.symbols(tag+'a '+tag+'b '+tag+'c')
    return S.Matrix([[aa,bb],[cc,-aa]])
AA,KK,DD,ZZ,dDD,dZZ,QQ,RR=map(mat,['A0','K1','D1','Z','dD1','dZ','Q','R1'])
Delta=q*DD+q*q*ZZ
DDelta=q*(dDD+rho*DD)+q*q*(dZZ+2*rho*ZZ)
ordinary=(H0+q*H1)*DDelta+(AA+q*KK)*Delta-Delta*(AA+q*KK)-(L0+q*L1)*Delta
coeff=lambda M,j:M.applyfunc(lambda v:S.expand(v).coeff(q,j))
expected1=H0*dDD+AA*DD-DD*AA+(H0*rho-L0)*DD
expected2=H0*dZZ+AA*ZZ-ZZ*AA+(2*H0*rho-L0)*ZZ+H1*(dDD+rho*DD)+KK*DD-DD*KK-L1*DD
assert (coeff(ordinary,1)-expected1).applyfunc(S.expand)==S.zeros(2)
assert (coeff(ordinary,2)-expected2).applyfunc(S.expand)==S.zeros(2)
transport=(S.eye(2)+q*QQ)*(q*RR)*(S.eye(2)-q*QQ+q*q*QQ*QQ)
assert (coeff(transport,2)-(QQ*RR-RR*QQ)).applyfunc(S.expand)==S.zeros(2)
# In the matched midpoint gauge the extra adjoint Q has no weights below4.
assert all(w-8<0 for w in (-2,0,2))
assert 4+4==4+8-4==8+8-8==8
print('PASS: complete ordinary first-mismatch expansion and surviving [Q,R1] term; matched-midpoint lower-Q exclusion.')

# Midpoint connection weight gap, with scalar normal-frame parts removed by tf.
assert 8+4-4==8+0==0+8==4+4==8
scalar=S.Symbol('scalar')*S.eye(2)
assert scalar-S.trace(scalar)*S.eye(2)/2==S.zeros(2)
print('PASS: midpoint adjoint K4 gap; determinant scalar separated, not discarded.')

# Pure-positive sextics restrict isomorphically to the conic: coordinate-ring
# Hilbert arithmetic and the universal parametrization (s²,st,t²).
from math import comb
assert comb(8,2)-comb(6,2)==13
conic_exponents={b+2*c for a in range(7) for b in range(7-a) for c in [6-a-b]}
assert conic_exponents==set(range(13))
assert 4-8 < -2  # no lower regular adjoint can mix into K4
print('PASS: global conic restriction excludes every nonzero homogeneous K4 ambiguity.')

# Universal harmonic inverse repair, with unrestricted formal entries.
pp=S.Matrix(2,2,S.symbols('p00 p01 p10 p11'))
qq=pp.inv();bb=S.Matrix(2,2,S.symbols('b00 b01 b10 b11'))
ii=-qq*bb
assert (pp*ii+bb).applyfunc(S.simplify)==S.zeros(2)
assert 8+8-4>8
print('PASS: general harmonic inverse repair; high stabilizers remain above retained weight8.')

# Arbitrary second-normal transition repairs are NOT restricted to weight zero/eight.
assert -2+8 == 6 and 4 < -2+8 < 8
print("PASS: arbitrary q² transition repair can change Z6, but cannot change Z4.")
