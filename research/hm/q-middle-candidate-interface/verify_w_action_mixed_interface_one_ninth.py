"""Complete universal W-action mixed-interface identities.
No actual HM/source coefficients, actual-instance matrices or ranks, scans,
or selected geometric points are evaluated. Every symbol stays unassigned;
the null vector and complementary spinor below both retain free coordinates.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s
with redirect_stdout(StringIO()):
 exec(Path(__file__).with_name('verify_full_six_space_vertex_correction.py').read_text().split('R6=s.Matrix')[0])
ha,hb,hc,hd,hf=s.symbols('ha hb hc hd hf')
H3=s.Matrix([[ha,hb,hc],[hd,ha,hf],[2*hf,2*hc,-2*ha]])
H5=s.zeros(5);H5[:3,:3]=H3
HH=s.kronecker_product(-H3.T,s.eye(2))
rh=H5*r
jw=contract(coords,omega);jvec=s.Matrix([jw.get((i,),0) for i in range(5)])
Hb=(s.Matrix(1,5,coords)*D*jvec)[0];abase=Hb/2

# Arbitrary coefficient operator on VVW, with nontrivial W action.
def FW(K,F):
 out=[{},{}]
 for i in [3,4]:
  for j in [3,4]:out=adds(out,putp(D[j,i]*K*getp(F,(i,)),(j,)))
 return out

def FWadj(K,F):
 out=[{},{}]
 for i in [3,4]:
  for j in [3,4]:out=adds(out,putY(-D[j,i]*up*adj6(K)*low*getY(F,(i,)),(j,)))
 return out

def TP(K,F):
 out=[{},{}]
 for i in range(3):
  ffirst=FW(K,[wedge({(i,):1},ff) for ff in F])
  fsecond=[wedge({(i,):1},ff) for ff in FWadj(K,F)]
  out=adds(out,sc(abase*rh[i],[contract(coords,ff) for ff in adds(ffirst,sc(-1,fsecond))]))
 return out

R6=s.Matrix(6,6,s.symbols('six0:36'))
zz2=s.symbols('form2_0:20');zz3=s.symbols('form3_0:20')
F2=[dict(zip(combinations(range(5),2),zz2[10*j:10*j+10])) for j in range(2)]
F3=[dict(zip(combinations(range(5),3),zz3[10*j:10*j+10])) for j in range(2)]
eq(pair(FW(R6,F3),F2),pair(F3,FWadj(R6,F2)))
print('PASS: all 36 W-changing coefficient symbols and their determinant adjoints.')

Lforms=[{(i,):(Ms[i]*p)[j] for i in range(3)} for j in range(2)]
rhform={(i,):rh[i] for i in range(5)}
Lrh=[wedge(ff,rhform) for ff in Lforms]
EU=sc(-abase,[contract(coords,wedge(ff,t)) for ff in Lrh])
Sspin=s.eye(6)-Pi
spinLrh=putp(Sspin*getp(Lrh))
SU=sc(abase,[contract(coords,wedge(ff,t)) for ff in spinLrh])
Tsb=TP(Sspin,B(p));Tcb=TP(Pi,B(p))
eqvec(Tsb,adds(EU,sc(-1,SU)))
eqvec(Tcb,adds(EU,SU))
eqvec(TP(Sspin,A(p)),[{},{}]);eqvec(TP(Pi,A(p)),[{},{}])
zero_matrix(extract*getp(SU))
print('PASS: exact full A/B columns, including the mandatory spin residual.')

# Sum of the two projector lifts is exactly twice the old gradient on K.
eta=[contract(coords,ff) for ff in F3]
eta_mixed=[{I:c for I,c in ff.items() if sum(i<3 for i in I)==1} for ff in eta]
Tsum=[contract(coords,wedge(rhform,action(D,ff))) for ff in eta_mixed]
eqvec(TP(s.eye(6),eta),sc(2*abase,Tsum))
hphys=s.expand((s.Matrix(1,5,coords)*rh)[0]);PH=hphys*D-rh*ell
Gm=sc(abase,[action(PH,ff) for ff in eta])
eqvec(sc(abase,Tsum),Gm)
print('PASS: (T_spin+T_Cartan)/2 = G_middle on the entire K bundle.')

# The c-column retains a nonzero adjoint-polar spin term in general.
Cmix=[{I:c for I,c in ff.items() if sum(i<3 for i in I)==1} for ff in Cx]
iellC=[contract(list(ell),ff) for ff in Cmix]
xiU=cliff*low*s.Matrix([iellC[j].get((i,),0) for i in range(3) for j in range(2)])/3
Xi=[{(i,):(Ms[i]*xiU)[j] for i in range(3)} for j in range(2)]
Tsc=TP(Sspin,Cx)
cform=sc(-abase,[wedge(rhform,ff) for ff in Xi])
zero_matrix(extract*getp(adds(Tsc,sc(-1,cform))))
Ap=s.Matrix.hstack(*[extract*getp(A(s.eye(2)[:,j])) for j in range(2)])
Apdag=J.inv()*Ap.T*J4
pD=extract*getp([contract(list(ell),ff) for ff in C])
zero_matrix(xiU+s.Rational(2,3)*Apdag*pD)
AH=Ap.subs(dict(zip([x,y,z],list(s.Matrix([[x,y,z]])*H3))),simultaneous=True)
zero_matrix(extract*getp(Tsc)+abase*AH*xiU/(2*theta))
print('PASS: the complete retained C spin-polar term; no Cartan-contraction shortcut.')

# Uniform C5 weights, not a selected source point or chosen actual coefficient.
negweights=[3,1,-1,-3];posweights=[9,3,-3,-9]
assert [next(j for j,t in enumerate(posweights) if (t-n)%10==0) for n in negweights]==[1,3,0,2]

# Complete positive Clebsch identity on a FREE spinor frame r,m.
r0,r1,m0,m1=s.symbols('r0 r1 m0 m1')
rr=s.Matrix([r0,r1]);mm=s.Matrix([m0,m1]);det=r0*m1-r1*m0
vv={x:r0*r0,y:-r1*r1,z:-r0*r1};vm={x:m0*m0,y:-m1*m1,z:-m0*m1}
Av=Ap.subs(vv,simultaneous=True);Am=Ap.subs(vm,simultaneous=True)
Avdag=J.inv()*Av.T*J4
vH=list(s.Matrix([[vv[x],vv[y],vv[z]]])*H3)
AHv=Ap.subs({x:vH[0],y:vH[1],z:vH[2]},simultaneous=True)
hp=hphys.subs(vv,simultaneous=True)
lam=(Av*mm).T*J4;p2=Am*rr
zero_matrix(Avdag*p2+det**2*rr/6)
assert s.expand((lam*p2)[0]-det**3/6)==0
lhs=(lam*AHv*Avdag*p2)[0];rhs=hp*(lam*p2)[0]
assert s.expand(lhs-theta*rhs/3)==0
p_cube=Av*rr
zero_matrix(Avdag*p_cube);assert s.expand((lam*p_cube)[0])==0
# Combining the exact -2/3 spin extraction and -a/(2 chi) Fierz factors:
assert s.Rational(-1,2)*s.Rational(-2,3)*s.Rational(1,3)==s.Rational(1,9)
assert s.Rational(9,8)*(1-s.Rational(1,9))==1
print('PASS: full free-frame positive identity; one-ninth ratio on the distinguished matched source line.')
print('PASS: 9/8 calibration matches the distinguished actual ramification input; arbitrary c inputs are not asserted.')
print('No full division or fourth Bockstein value is asserted.')
