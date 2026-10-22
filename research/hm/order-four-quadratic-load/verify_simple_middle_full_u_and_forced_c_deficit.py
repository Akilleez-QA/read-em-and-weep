"""Complete universal exterior identities, with all actual tensor/line parameters free."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s,sys
ROOT=Path(__file__).resolve().parent;sys.path.insert(0,str(ROOT))
from universal_source_balance_helpers import *
import universal_source_balance_helpers as ns

r0,r1=s.symbols('r0 r1');rr=s.Matrix([r0,r1]);vv={x:r0*r0,y:-r1*r1,z:-r0*r1}
Ap=s.Matrix.hstack(*[extract*getp(A(s.eye(2)[:,j])) for j in range(2)])
Av=Ap.subs(vv,simultaneous=True);pure=(Av*rr).applyfunc(s.expand)
Pstd=s.Matrix.hstack(*[s.Matrix([s.Poly(e,r0,r1).coeff_monomial(r0**(3-j)*r1**j) for e in pure])/s.binomial(3,j) for j in range(4)])
H0=Pstd.inv()*extract*HH*Kinc*Pstd
BHcoef=ns.mixed5(ns.quartic(H0))
B6=(Kinc*Pstd).row_join(spin)
K0=s.zeros(6);K0[:4,:4]=s.Rational(3,8)*H0;K0[:4,4:]=-s.Rational(3,2)*BHcoef
KQ=(abase*B6*K0*B6.inv()).applyfunc(s.expand);KH=s.Rational(3,8)*abase*Pi

def op(K,R,F):
 out=[{},{}]
 for ii in range(3):
  first=FW(K,[wedge({(ii,):1},ff) for ff in F])
  second=[wedge({(ii,):1},ff) for ff in FWadj(K,F)]
  out=adds(out,sc(R[ii],[contract(coords,ff) for ff in adds(first,sc(-1,second))]))
 return out
TA=adds(op(KQ,r,A(p)),op(KH,rh,A(p)))
TB=adds(op(KQ,r,B(p)),op(KH,rh,B(p)))
eqvec(TA,[{},{}]);print('FULL A ZERO',flush=True)
print('FULL B ZERO?',all(s.expand(v)==0 for ff in TB for v in ff.values()),flush=True)
yB=getp(TB).applyfunc(s.expand)
assert (cliff*yB).applyfunc(s.expand)==s.zeros(2,1)


ZH=s.Matrix([[hf,hd],[ha,-hf],[hc,ha],[hb,-hc]])
Kbase_spin=s.Rational(3,4)*abase**2/theta*ZH
Kbase=Kinc*Kbase_spin*cliff
assert (yB+Kinc*Kbase_spin*M*p).applyfunc(s.expand)==s.zeros(6,1)
assert (getp(fullT(Kbase,4,A(p)))-Kinc*Kbase_spin*M*p).applyfunc(s.expand)==s.zeros(6,1)
eqvec(fullT(Kbase,4,B(p)),[{},{}])
EU=adds(TB,fullT(Kbase,4,A(p)))
EU=[{I:s.factor(cc) for I,cc in ff.items() if s.expand(cc)!=0} for ff in EU]
print('COMPACT SC PRINCIPAL CANCELLATION PASS',flush=True)
assert not any(EU)
print('PASS: entire U column cancels, including mixed/WW.',flush=True)
print('MIXED E',EU,flush=True)

FB,FC,FD=s.symbols('FB FC FD',nonzero=True);FA=-9*FB*FC/FD
fstd=s.Matrix([[0,0,FC,0],[FA,0,0,0],[0,0,0,FD],[0,FB,0,0]])
fmat=Pstd*fstd;finv=fmat.inv()
S,T=s.symbols('S T');cz=s.symbols('cz0:3');ypoly=cz[0]*S*S+cz[1]*S*T+cz[2]*T*T
mons=[S**3,S*S*T,S*T*T,T**3]
def cf(pol):return Kinc*fmat*s.Matrix([s.Poly(s.expand(pol),S,T).coeff_monomial(mm) for mm in mons])
Cthree=adds(putp(cf(-T*ypoly),(3,)),putp(cf(S*ypoly),(4,)))
Cactual=[contract(coords,ff) for ff in Cthree]
Cd=[contract(coords,action(D,ff)) for ff in Cthree]
T0C=adds(op(KQ,r,Cactual),op(KH,rh,Cactual))
Kc=fullT(Kbase,4,Cactual)
PC=(cliff*(adj6(Kbase.diff(u))*low*getY(Cactual,(4,))-adj6(Kbase.diff(w))*low*getY(Cactual,(3,)))/12).applyfunc(s.factor)
eqvec(Kc,B(PC))
print('FORCED FULL C COMPANION VERIFIED',flush=True)
hphys=s.expand((s.Matrix(1,5,coords)*rh)[0])
EC=adds(T0C,sc(-abase*hphys,Cd),sc(-1,A(PC)))
EC=[{I:s.expand(cc) for I,cc in ff.items() if s.expand(cc)!=0} for ff in EC]
print('HIGH ERROR ZERO?',not any(EC),flush=True)
Y=getp(EC).applyfunc(s.expand)
print('HIGH VV SPIN ZERO?',(cliff*Y).applyfunc(s.expand)==s.zeros(2,1),flush=True)
lam=s.Matrix([[u**3,u*u*w,u*w*w,w**3]])*finv
sigma=s.factor((lam*extract*Y)[0])
sigmac=s.factor(sigma.subs(vv,simultaneous=True))
F=s.factor((lam*pure)[0])
assert (cliff*Y).applyfunc(s.expand)==s.zeros(2,1)
deficit=s.cancel(sigmac/F)
assert s.denom(deficit).free_symbols <= {FB,FC,FD,theta}
unit=s.Poly(s.expand(deficit),*cz,ha,hb,hc,hd,hf,h,k,l,r0,r1,u,w).coeff_monomial(cz[0]*hc*k**2*r0*u**3)
assert s.factor(unit+9*FB*FC/(4*FD*theta))==0
print('PASS: forced c deficit has retained nonzero harmonic coefficient',unit,flush=True)
