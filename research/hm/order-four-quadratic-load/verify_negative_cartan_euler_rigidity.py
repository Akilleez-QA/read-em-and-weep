"""Universal negative-quartic Euler rigidity and full c companions.

No selected HM/source values, actual-instance matrices/ranks, scans or
normal-form division. Factorized generic symbols suffice because every
identity is linear in the corresponding middle coefficient; decomposable
coefficients span the complete 180- and 72-coefficient spaces.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import sympy as s
from universal_source_balance_helpers import *
S,T=s.symbols('S T')
lin=u*T-w*S

def ivp(pp):
    return s.Matrix([contract(coords,ff).get((i,),0)
                     for i in range(3) for ff in putp(pp)])
def dpos(ff):
    return add(*[wedge({(i,):1},{I:s.diff(c,coords[i]) for I,c in ff.items()}) for i in range(3)])
def bcoeff(poly,n):
    pp=s.Poly(s.expand(poly),S,T)
    return s.Matrix([pp.coeff_monomial(S**(n-i)*T**i) for i in range(n+1)])
def binform(cc):
    n=len(cc)-1
    return s.expand(sum(cc[i]*S**(n-i)*T**i for i in range(n+1)))
def gradlift(pp):
    return adds(putp(pp.diff(u),(3,)),putp(pp.diff(w),(4,)))

# Complete low U action, with all 36 coefficient directions and all five
# quartic monomials symbolic. No Cartan-preservation hypothesis is used.
R6=s.Matrix(6,6,s.symbols('k0:36'))
qq=s.symbols('q4_0:5')
q4=sum(qq[i]*u**(4-i)*w**i for i in range(5))
K=q4*R6
LB=putY(up*adj6(K)*spin*p,())
B_rhs=sc(-3,[contract(coords,wedge(ff,omega)) for ff in LB])
eqvec(fullT(K,4,B(p)),B_rhs)
print('PASS: complete 180-coefficient low U identity T4(K)B=-3 i_x(up adj(K) spin p wedge omega).',flush=True)

# A source-shaped coefficient on the full six-space has no hidden mixed
# A companion, even though P itself depends on negative coordinates.
source0=s.Matrix(2,2,s.symbols('source0:4'))
sourceP=q4*source0
sourceK=s.kronecker_product(s.eye(3),sourceP)
eqvec(fullT(sourceK,4,A(p)),A(sourceP*p))
print('PASS: T4(I_V tensor P)A=A(P), with the full quartic source free.',flush=True)

# Full image-Cartan/ell family. All f coefficients remain free, without
# inversion or a conformal normalization. The 18-by-4 symbolic tensor
# factors span every cubic H: V6 -> Sym^2(W).
F=s.Matrix(4,4,s.symbols('f0:16'))
H0=s.Matrix(3,6,s.symbols('hh0:18'))
cc=s.symbols('hcubic0:4')
c3=sum(cc[i]*u**(3-i)*w**i for i in range(4))
H=c3*H0
Eell=s.Matrix.hstack(*[bcoeff(lin*mm,3) for mm in [S*S,S*T,T*T]])
K=Kinc*F*Eell*H

def fc(poly):return Kinc*F*bcoeff(poly,3)
def cthree(yy):return adds(putp(fc(-T*yy),(3,)),putp(fc(S*yy),(4,)))
def Cmap(yy):return [contract(coords,ff) for ff in cthree(yy)]
Ap=getp(A(p));Y=binform(H*Ap)
Delta=lambda pp:s.expand(S*s.diff(pp,u)+T*s.diff(pp,w))
res=adds(fullT(K,4,A(p)),Cmap(Y))
rhs=sc(s.Rational(1,4),[contract([x,y,z,0,0],wedge(ff,{(3,):-w,(4,):u})) for ff in putp(fc(Delta(Y)))])
eqvec(res,rhs)
eqvec(fullT(K,4,B(p)),[{},{}])
print('PASS: all 72 image-in-ell Cartan coefficients obey the full U Clebsch identity, including mixed/WW.',flush=True)

# Adjacent-degree Euler inversion, independent of v/input coefficients.
a=s.symbols('adj0:12')
Yfree=sum(a[4*i+j]*S**(2-i)*T**i*u**(3-j)*w**j for i in range(3) for j in range(4))
E=lambda pp:s.expand(u*s.diff(pp,S)+w*s.diff(pp,T))
def I2(pp):return s.expand(E(pp)-E(E(Delta(pp)))/4+E(E(E(Delta(Delta(pp)))))/36)
assert s.expand(I2(Delta(Yfree))-Yfree)==0
print('PASS: Delta on bidegree (2,3) has the exact polynomial inverse I2.',flush=True)

# A literal left inverse to positive contraction on the Cartan-valued
# positive-linear two-form sector. Coefficient extraction is not evaluation.
ff=s.symbols('lin0:12')
FV=Kinc*s.Matrix([sum(ff[3*i+j]*coords[j] for j in range(3)) for i in range(4)])
forms=putp(FV)
iF=[contract([x,y,z,0,0],f) for f in forms]
diF=[dpos(f) for f in iF]
zcoef=(cliff*getp(diF)).applyfunc(lambda v:s.Poly(v,x,y,z).coeff_monomial(z))
reconstructed=sc(s.Rational(1,3),adds(diF,sc(-1,A(M2*zcoef))))
eqvec(forms,reconstructed)
print('PASS: a Cartan positive-linear VV tensor with i_v=0 is zero, by a checked explicit left inverse.',flush=True)

# The lower balance for K=I_V tensor P has trivial kernel, by literal
# coefficient recovery, not a matrix/rank argument.
pa,pb,pc,pd=s.symbols('pa pb pc pd')
PP=s.Matrix([[pa,pb],[pc,pd]])
Pd=J.inv()*PP.T*J
D0=Pd*M0+M0*PP;D1=Pd*M1+M1*PP
assert s.Matrix([[D1[1,0]/2,-D1[0,0]],[D0[0,0],D0[0,1]/2]])==PP
print('PASS: lower U balance recovers P explicitly, so P=0 whenever all defects vanish.',flush=True)

# Full c companion in the same natural family. The full quadratic input
# and every f coefficient remain symbolic. No lower component is omitted.
zz=s.symbols('zz0:3');zzpoly=zz[0]*S*S+zz[1]*S*T+zz[2]*T*T
CC=Cmap(zzpoly);TC=fullT(K,4,CC)
pC=getp(CC);C3=getY(CC,(3,));C4=getY(CC,(4,))
F3=-up*adj6(K)*low*C3;F4=-up*adj6(K)*low*C4
Sn=u*F3+w*F4
for wi,idx,Fi in [(u,3,F3),(w,4,F4)]:
    expected=(ivp(K.diff(wi)*pC)+5*Fi-Sn.diff(wi))/4
    zero_matrix(getY(TC,(idx,))-expected)
ww=(s.Matrix(1,3,[x,y,z])*s.Matrix(3,2,lambda i,j:(up*(adj6(K.diff(u))*low*C4-adj6(K.diff(w))*low*C3))[2*i+j]))/4
zero_matrix(s.Matrix([ff.get((3,4),0) for ff in TC])-ww.T)
ys=binform(H*fc(lin*zzpoly))
DC=adds(TC,sc(-1,Cmap(ys)))
zero_matrix(getp(DC))
L=(getY(DC,(4,)).diff(u)-getY(DC,(3,)).diff(w))/5
for idx,ji in [(3,-w),(4,u)]:zero_matrix(getY(DC,(idx,))-ji*L)
PC=-(cliff*low*L)/3
LC=up*Pi*low*L
cartan_companion=sc(-1,[contract(coords,wedge(ff,omega)) for ff in putY(LC,())])
eqvec(DC,adds(B(PC),cartan_companion))
print('PASS: complete c identity T4(K)C=C(y_C)+B(P_C)-i_x(L_C wedge omega), all mixed/WW retained.',flush=True)

# Literal source-scaled c residual after balancing the C and B terms.
am,bm,cm=s.symbols('a_m b_m c_m',nonzero=True)
scaled=adds(sc(cm,TC),sc(-cm,Cmap(ys)),sc(-cm,B(PC)),sc(-am*cm/bm,A(PC)))
eqvec(scaled,adds(sc(cm,cartan_companion),sc(-am*cm/bm,A(PC))))
print('PASS: source scales force residual -c_m i_x(L_C wedge omega)-(a_m c_m/b_m)A(P_C).',flush=True)
print('No fourth value, unrestricted obstruction, actual specialization, or curve-division certificate is asserted.')
