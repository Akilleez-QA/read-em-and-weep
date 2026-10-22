"""Constructive full-U reconstruction with general Cartan-input Euler symbols.

Only the public universal_source_balance_helpers module is imported.
Every coefficient is free; decomposable homogeneous tensor factors span
all stated spaces. No actual HM/source coefficients, matrix/rank scans,
curve reduction, or imported unpublished verifiers occur.
"""
import sympy as s
from universal_source_balance_helpers import *

S,T=s.symbols('S T')
ell=u*T-w*S
vp=[x,y,z,0,0]
jw={(3,):-w,(4,):u}

def dpos(ff):
    return add(*[wedge({(i,):1},{I:s.diff(c,coords[i]) for I,c in ff.items()}) for i in range(3)])
def iv(F):return [contract(vp,ff) for ff in F]
def bcoeff(poly,n):
    po=s.Poly(s.expand(poly),S,T)
    return s.Matrix([po.coeff_monomial(S**(n-i)*T**i) for i in range(n+1)])
def bform(cc):
    n=len(cc)-1
    return s.expand(sum(cc[i]*S**(n-i)*T**i for i in range(n+1)))
def Delta(q):return s.expand(S*s.diff(q,u)+T*s.diff(q,w))
def Eb(q):return s.expand(u*s.diff(q,S)+w*s.diff(q,T))
def I2(q):return s.expand(Eb(q)-Eb(Eb(Delta(q)))/4+Eb(Eb(Eb(Delta(Delta(q)))))/36)
def onevec(F):return s.Matrix([ff.get((i,),0) for i in range(3) for ff in F])
def cartan_candidate(L):
    dL=[dpos(ff) for ff in L]
    cz=(cliff*getp(dL)).applyfunc(lambda a:s.Poly(a,x,y,z).coeff_monomial(z))
    return sc(s.Rational(1,3),adds(dL,sc(-1,A(M2*cz))))
def closed_no_vv(L):return sc(-1,[contract(coords,wedge(ff,omega)) for ff in L])

# The full spin-source test and its literal coefficient inverse.
pf=s.Matrix(2,2,s.symbols('pquartic0:4'))
pfd=J.inv()*pf.T*J
ss=[Mi*pf+pfd*Mi for Mi in Ms]
rec=s.Matrix([[ss[1][1,0]/2,-ss[1][0,0]],[ss[0][0,0],ss[0][0,1]/2]])
zero_matrix(rec-pf)
print('PASS: spin-source reconstruction recovers all four free source entries, without an instance matrix or rank.',flush=True)

# A completely general raw VV symbol admits a canonical K0, with no
# principal Cartan quotient condition once Cartan-input coefficients are allowed.
qc=s.symbols('quartic0:5')
q4=sum(qc[i]*u**(4-i)*w**i for i in range(5))
Y=q4*s.Matrix(6,6,s.symbols('raw0:36'))
P=q4*pf
IP=s.kronecker_product(s.eye(3),P)
K0=IP-Y
Ap=getp(A(p))
base=fullT(Y,4,A(p))
eqvec(adds(base,fullT(K0,4,A(p)),sc(-1,A(P*p))),[{},{}])
Gamma=cliff*Y-cliff*IP-(J.inv()*P.T*J)*cliff
lowdef=adj6(K0)*spin+spin*P
zero_matrix(3*lowdef-J6.inv()*Gamma.T*J)
eqvec(adds(fullT(K0,4,B(p)),sc(-1,B(P*p))),
      sc(-3,[contract(coords,wedge(ff,omega)) for ff in putY(up*lowdef*p,())]))
print('PASS: all 180 raw VV directions give K0=I tensor P-Y; high error is source-independent and low error is exactly the spin defect.',flush=True)

# Every closed high error with VV=0 has this form, including its WW part.
# The free rank-one coefficient factors span all 216 possible one-forms L.
q2c=s.symbols('negative2_0:3');q2=sum(q2c[i]*u**(2-i)*w**i for i in range(3))
vc=s.symbols('quadratic0:6');vquad=sum(a*b for a,b in zip(vc,[x*x,x*y,x*z,y*y,y*z,z*z]))
lc=s.Matrix(s.symbols('one0:6'));pr=s.Matrix(1,2,s.symbols('input0:2'))
Lv=q2*vquad*lc*(pr*p)[0]
L=putY(Lv,())
DD=closed_no_vv(L)
zero_matrix(getp(DD))
for ff in DD:assert not contract(coords,ff)
Lrec=(getY(DD,(4,)).diff(u)-getY(DD,(3,)).diff(w))/4
zero_matrix(Lrec-Lv)
zero_matrix(s.Matrix([ff.get((3,4),0) for ff in DD])+s.Matrix([contract(vp,ff).get((),0) for ff in L]))
print('PASS: full zero-VV high residual has regular denominator-four recovery, retaining its exact WW=-i_v L component.',flush=True)

# Regular positive Koszul inverse, including its four Cartan tests per
# full input and negative quadratic coefficient. The free 18 coefficients
# span all positive-linear six-space two-forms.
lincoef=s.Matrix(6,3,s.symbols('positive_linear0:18'))
FF=putp(lincoef*s.Matrix([x,y,z]))
LL=iv(FF)
QQ=cartan_candidate(LL)
eqvec(iv(QQ),LL)
Fcart=putp(Kinc*s.Matrix(4,3,s.symbols('cartan_linear0:12'))*s.Matrix([x,y,z]))
eqvec(cartan_candidate(iv(Fcart)),Fcart)
zero_matrix(cliff*getp(cartan_candidate(iv(Fcart))))
print('PASS: positive Cartan contraction has a regular inverse on its image; the reconstructed Cartan condition is exact, not M-right-divisibility.',flush=True)

# Full image-in-ell correction, with all 72 H directions and all 16
# marking coefficients free. Only the fixed inverse marking is used in
# the theorem; its invertibility need not be expanded in this verifier.
F=s.Matrix(4,4,s.symbols('mark0:16'))
def fc(q):return Kinc*F*bcoeff(q,3)
def Cmap(q):
    cc=adds(putp(fc(-T*q),(3,)),putp(fc(S*q),(4,)))
    return [contract(coords,ff) for ff in cc]
Eell=s.Matrix.hstack(*[bcoeff(ell*m,3) for m in [S*S,S*T,T*T]])
hc=s.symbols('cubic0:4');q3=sum(hc[i]*u**(3-i)*w**i for i in range(4))
HH=q3*s.Matrix(3,6,s.symbols('H0:18'))
KH=Kinc*F*Eell*HH
HA=bform(HH*Ap)
Z=Delta(HA)
Lsolve=sc(-s.Rational(1,4),iv(putp(fc(Z))))
Dsolve=closed_no_vv(Lsolve)
eqvec(adds(Dsolve,fullT(KH,4,A(p)),Cmap(HA)),[{},{}])
eqvec(fullT(KH,4,B(p)),[{},{}])
eqvec(cartan_candidate(Lsolve),sc(-s.Rational(1,4),putp(fc(Z))))
assert s.expand(I2(Z)-HA)==0
print('PASS: all 72 general Cartan-input corrections are recovered by the exact I2 inverse and cancel the entire high U error, including signs.',flush=True)

# Full scaled U cancellation is checked with P, arbitrary Cartan raw VV
# symbol, and H free. This spans every admissible spin-VV direction and
# every Cartan-VV direction in the reconstruction theorem.
rawcart=q4*Kinc*s.Matrix(4,6,s.symbols('raw_cartan0:24'))
Ygood=IP+spin*(J.inv()*P.T*J)*cliff+rawcart
Kgood=IP-Ygood+KH
Egood=adds(fullT(Ygood,4,A(p)),Dsolve)
am,bm,cm=s.symbols('a_m b_m c_m',nonzero=True)
reverse=-am*HA/cm
# The source and H contributions are separately universal, so check the
# assembled U identity via its distinct high and low coordinate sectors.
eqvec(adds(Egood,fullT(Kgood,4,A(p)),sc(-1,A(P*p)),sc(-cm/am,Cmap(reverse))),[{},{}])
eqvec(adds(fullT(Kgood,4,B(p)),sc(-1,B(P*p))),[{},{}])
print('PASS: every admissible raw VV direction assembles into full U cancellation with reverse source R=-(a_m/c_m)H A and all monad scales retained.',flush=True)

# New regular ell-division for the low c-VV companion: no division by a
# negative coordinate or actual source coefficient is needed.
def eps(q):return s.expand(s.diff(q,u,T)-s.diff(q,w,S))
def Jell(q):return s.expand(eps(q)/8-ell*eps(eps(q))/112+ell**2*eps(eps(eps(q)))/2016)
cc=s.symbols('source_c0:15')
V=sum(cc[5*i+j]*S**(2-i)*T**i*u**(4-j)*w**j for i in range(3) for j in range(5))
assert s.expand(Jell(ell*V)-V)==0
print('PASS: the c-VV preservation quotient has the regular exact inverse eps/8-ell eps^2/112+ell^2 eps^3/2016 on all 15 coefficients.',flush=True)

# The whole moving-plane preservation gate has a canonical normal form.
# These 5 scalar and 48 cubic coefficients are all free; no family is used.
mucoeff=s.symbols('mu0:5')
mu=sum(mucoeff[i]*u**(4-i)*w**i for i in range(5))
hcc=s.symbols('preserve0:48')
Hcc=s.Matrix(3,4,lambda i,j:sum(hcc[16*i+4*j+k]*u**(3-k)*w**k for k in range(4)))
Tpres=mu*s.eye(4)+Eell*Hcc
lam=s.Matrix([[u**3,u*u*w,u*w*w,w**3]])
row=lam*Tpres
zero_matrix(row-mu*lam)
murec=sum(s.binomial(3,i)*s.diff(row[i],u,3-i,w,i) for i in range(4))/336
assert s.expand(murec-mu)==0
def J34(q):return s.expand(eps(q)/7-ell*eps(eps(q))/84+ell**2*eps(eps(eps(q)))/1260)
for k in range(4):
    assert s.expand(J34(bform((Tpres-mu*s.eye(4))[:,k]))-bform(Hcc[:,k]))==0
zcheck=s.Matrix(s.symbols('check_z0:3'))
zero_matrix(Tpres*Eell*zcheck-Eell*(mu*zcheck+Hcc*Eell*zcheck))
print('PASS: moving-plane preservation has the unique 5+48 normal form, regular 1/336 scalar extraction, and exact 7/84/1260 column inverse.',flush=True)

# Once its low VV term is canceled, the ENTIRE c companion is recovered
# by a denominator-five Koszul map; its Cartan one-form cannot be omitted.
lcv=s.Matrix(s.symbols('c_one0:6'));vv=s.symbols('c_pos0:3')
Lcv=q3*(vv[0]*x+vv[1]*y+vv[2]*z)*lcv
Lcform=putY(Lcv,())
DC=closed_no_vv(Lcform)
Lcrec=(getY(DC,(4,)).diff(u)-getY(DC,(3,)).diff(w))/5
zero_matrix(Lcrec-Lcv)
PC=-cliff*low*Lcv/3
LC=up*Pi*low*Lcv
cartancomp=closed_no_vv(putY(LC,()))
eqvec(DC,adds(B(PC),cartancomp))
eqvec(adds(sc(cm,DC),sc(-cm,B(PC)),sc(-am*cm/bm,A(PC))),
      adds(sc(cm,cartancomp),sc(-am*cm/bm,A(PC))))
print('PASS: complete c mixed/WW source balance retains L_C and residual -c_m i_x(L_C wedge omega)-(a_m c_m/b_m)A(P_C).',flush=True)
print('No actual-family membership, completed c balance, unrestricted cochain obstruction, or fourth value is asserted.')
