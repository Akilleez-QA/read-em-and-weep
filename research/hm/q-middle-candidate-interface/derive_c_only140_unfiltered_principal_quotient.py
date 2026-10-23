"""Complete symbolic full-conic and full-bicubic c-source certificate."""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s,sys,pickle
ROOT=Path(__file__).resolve().parent
__file__=str(ROOT/'verify_w_action_mixed_interface_one_ninth.py')
with redirect_stdout(StringIO()):exec(Path(__file__).read_text().split('\nR6=s.Matrix')[0])
ns={};exec((ROOT/'universal_complete_w_action_symbols.py').read_text(),ns)
r0,r1=s.symbols('r0 r1');rr=s.Matrix([r0,r1]);vv={x:r0*r0,y:-r1*r1,z:-r0*r1}
Ap=s.Matrix.hstack(*[extract*getp(A(s.eye(2)[:,j])) for j in range(2)])
Av=Ap.subs(vv,simultaneous=True);pure=(Av*rr).applyfunc(s.expand)
Pstd=s.Matrix.hstack(*[s.Matrix([s.Poly(e,r0,r1).coeff_monomial(r0**(3-j)*r1**j) for e in pure])/s.binomial(3,j) for j in range(4)])
B6=(Kinc*Pstd).row_join(spin);B6inv=B6.inv()
JB=s.diag(-ns['J3']/2,-J/3)
assert B6.T*J6*B6==JB
FB,FC,FD=s.symbols('FB FC FD',nonzero=True);FA=-9*FB*FC/FD
fstd=s.Matrix([[0,0,FC,0],[FA,0,0,0],[0,0,0,FD],[0,FB,0,0]])
fmat=Pstd*fstd;finv=fmat.inv()
S,T=s.symbols('S T');mons=[S**3,S*S*T,S*T*T,T**3]
DD=lambda p:s.expand((h*S+l*T)*s.diff(p,S)+(k*S-h*T)*s.diff(p,T))
ellpoly=-w*S+u*T
NN=lambda p:s.expand(-2*ellpoly*(u*s.diff(p,S)+w*s.diff(p,T)))
rep=lambda fun:s.Matrix([[s.Poly(fun(p),S,T).coeff_monomial(m) for p in mons] for m in mons])
D0,N0=rep(DD),rep(NN)
DP=fstd*D0*fstd.inv();NP=fstd*N0*fstd.inv()
H0=Pstd.inv()*extract*HH*Kinc*Pstd
rq_symbols,rh_symbols,Theta=ns['build_symbols'](fstd,H0,DP,NP,abase)
newns={'__file__':str(ROOT/'universal_commutator_w_action_symbols.py')};exec(Path(newns['__file__']).read_text(),newns)
rqC,rhC=newns['build_commutator_action_symbols'](fstd,H0,DP)
import sys
sys.path.insert(0,str(ROOT))
from universal_complete_identity_w_coefficients import build_complete_identity_w_coefficients
rqI,rhI=build_complete_identity_w_coefficients(fstd,H0)
assert len(rqI)==87 and len(rhI)==10
cs=s.symbols('co0:140');mode='c_only140_unfiltered'
# NO seed or U filter: all140 operator coordinates are initially free.
# Coordinates0..42 are the complete fixed-D33 and retained commutator-W10.
# Coordinates43..139 use the complete identity-W COEFFICIENT spanning set.
# Its87 Rq coefficients are intentionally redundant; no exterior independence
# is assumed. No U screen or normalization is inherited.
sol=tuple(cs)
pars=sorted(set().union(*[e.free_symbols for e in sol]),key=str)
print(mode,'remaining parameters',pars,flush=True)
MQ=sum((sol[i]*M for i,(_,M) in enumerate(rq_symbols)),s.zeros(6)).applyfunc(s.expand)
MH=sum((sol[27+i]*M for i,(_,M) in enumerate(rh_symbols)),s.zeros(6)).applyfunc(s.expand)
Q6=(B6*MQ*B6inv).applyfunc(s.expand);H6=(B6*MH*B6inv).applyfunc(s.expand)
MQC=sum((sol[33+i]*MM for i,(_,MM) in enumerate(rqC)),s.zeros(6)).applyfunc(s.expand)
MHC=sum((sol[42+i]*MM for i,(_,MM) in enumerate(rhC)),s.zeros(6)).applyfunc(s.expand)
Q6C=(B6*MQC*B6inv).applyfunc(s.expand);H6C=(B6*MHC*B6inv).applyfunc(s.expand)
MQI=sum((sol[43+i]*MM for i,(_,MM) in enumerate(rqI)),s.zeros(6)).applyfunc(s.expand)
MHI=sum((sol[130+i]*MM for i,(_,MM) in enumerate(rhI)),s.zeros(6)).applyfunc(s.expand)
Q6I=(B6*MQI*B6inv).applyfunc(s.expand)
H6I=(B6*MHI*B6inv).applyfunc(s.expand)
print('combined full-six-space coefficients formed',flush=True)
source=[S*S,S*T,T*T];ellD=-DD(ellpoly)
pD=-fmat*s.Matrix([[s.Poly(ellD*z2,S,T).coeff_monomial(m) for z2 in source] for m in mons])
cv=s.Matrix.hstack(*[s.Matrix([contract([vv[x],vv[y],vv[z],0,0],ff).get((i,),0) for i in range(3) for ff in putp(Kinc[:,j])]) for j in range(4)])
def ER(R):
 rf={(i,):R[i].subs(vv,simultaneous=True) for i in range(3)}
 return s.Matrix.hstack(*[getp([wedge(rf,{(i,):s.eye(6)[2*i+j,col] for i in range(3)}) for j in range(2)]) for col in range(6)])
EQ,EH=ER(r),ER(rh)
def phi(K,E):return K*E*cv+E*up*adj6(K)*low*cv
def phiI(K,E):return K*E*cv-E*up*adj6(K)*low*cv
hp=s.expand((s.Matrix(1,5,coords)*rh)[0]).subs(vv,simultaneous=True)
pC=-fmat*s.Matrix([[s.Poly(ellpoly*z2,S,T).coeff_monomial(m) for z2 in source] for m in mons])
res=(phi(Q6,EQ)+phi(H6,EH)-abase*hp*Kinc)*pD+(phi(Q6C,EQ)+phi(H6C,EH))*(-4*abase*pC)+(phiI(Q6I,EQ)+phiI(H6I,EH))*pC

actualvars=[r0,r1,u,w,FB,FC,FD,ha,hb,hc,hd,hf,h,k,l,theta]
spineq=[]
for jj in range(3):
 ss=(cliff*res[:,jj]).applyfunc(s.expand)
 ob=s.expand(-r1*ss[0]+r0*ss[1])
 nn,dd=s.fraction(s.together(ob))
 spineq.extend(s.Poly(nn,*actualvars).coeffs())
 print('complete spin source',jj,'equations assembled',flush=True)
spsol=s.linsolve(spineq,pars)
print('FULL SPIN SOLUTION',spsol,flush=True)
assert spsol!=s.EmptySet
spsub=dict(zip(pars,list(spsol)[0]))
res=res.xreplace(spsub)
pars=sorted(set().union(*[e.free_symbols for e in list(spsol)[0]]),key=str)
lam=s.Matrix([[u**3,u*u*w,u*w*w,w**3]])*finv
F=s.factor((lam*pure)[0]);fn,fd=s.fraction(F)
from universal_cached_lex_module import CachedLexModule
normal=CachedLexModule(s.Poly(fn,r0,r1,u,w,domain=s.QQ.frac_field(FB,FC,FD,theta)))
params=[ha,hb,hc,hd,hf,h,k,l];all_eqs=[];all_remainders=[]
for source_i in range(3):
 Y=res[:,source_i].applyfunc(s.expand)
 sp=(cliff*Y).applyfunc(s.expand)
 assert s.expand(-r1*sp[0]+r0*sp[1])==0
 beta=s.expand((s.diff(sp[0],r0)+s.diff(sp[1],r1))/5)
 us=s.Matrix([-s.diff(beta,r1),s.diff(beta,r0)])/3
 assert (M.subs(vv,simultaneous=True)*us-sp).applyfunc(s.expand)==s.zeros(2,1)
 curve=s.expand((lam*(extract*Y-Av*us))[0]);cp=s.Poly(curve,*params)
 print('source',source_i,'complete H,D components',len(cp.terms()),flush=True)
 remainders=[]
 for n,(powers,coeff) in enumerate(cp.terms()):
  quotient,remainder=normal.reduce_expression(coeff)
  rem=s.Poly(remainder,r0,r1,u,w,domain=s.EX)
  for cc in rem.coeffs():
   num,den=s.fraction(s.factor(cc));assert den.free_symbols <= {FB,FC,FD,theta}
   assert len(s.Poly(den,FB,FC,FD,theta).terms())==1
   all_eqs.extend(s.Poly(num,FB,FC,FD,theta).coeffs())
  remainders.append((powers,rem.as_expr()))
  if n%10==0:print('source',source_i,'H,D coefficient',n,'checked',flush=True)
 all_remainders.append(remainders)
 answer=s.linsolve(all_eqs,pars)
 print('source',source_i,'CURVE SOLUTION',answer,flush=True)
 assert answer!=s.EmptySet, 'The complete retained c principal family is empty.'
 with (ROOT/'c-only140-unfiltered-principal-quotient.pickle').open('wb') as ff:
  pickle.dump({'pars':pars,'solution':answer,'remainders':all_remainders,'eqs':all_eqs,'F':F,'sol':sol,'spin_sub':spsub},ff)
print('PASS: all three complete source coefficients examined.',flush=True)

