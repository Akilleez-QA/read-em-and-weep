"""Four universal exterior presentation identities; no curve reducer or actual f."""
from universal_source_balance_helpers import *

r0,r1=s.symbols('formal_r0 formal_r1')
rr=s.Matrix([r0,r1]); vv={x:r0*r0,y:-r1*r1,z:-r0*r1}
AP=s.Matrix.hstack(*[extract*getp(A(s.eye(2)[:,j])) for j in range(2)])
cubic=(AP.subs(vv,simultaneous=True)*rr).applyfunc(s.expand)
Pstd=s.Matrix.hstack(*[s.Matrix([s.Poly(e,r0,r1).coeff_monomial(r0**(3-j)*r1**j) for e in cubic])/s.binomial(3,j) for j in range(4)])
B6=(Kinc*Pstd).row_join(spin); B6inv=B6.inv()
JP=-J3/2; JS=-J/3
assert B6.T*J6*B6==s.diag(JP,JS)
H0=Pstd.inv()*extract*HH*Kinc*Pstd
hp=quartic(H0); BH=mixed5(hp)
assert op4(hp)==H0

def EC(X):
 out=s.zeros(6);out[:4,:4]=X;return out
def ES(X):
 out=s.zeros(6);out[4:,4:]=X;return out
def E10(X):
 out=s.zeros(6);out[:4,4:]=X;return out
def E01(X):
 out=s.zeros(6);out[4:,:4]=JS.inv()*X.T*JP;return out
def pV(X):
 return s.trace(binary_H*X)*binary_H/20+(s.trace(binary_F*X)*binary_E+s.trace(binary_E*X)*binary_F)/10
def spinrep(X):
 return s.trace(binary_F*X)*E1/10+s.trace(binary_E*X)*F1/10+s.trace(binary_H*X)*H1/20
def mixedV(X):
 v=s.trace(binary_F*X)*S*S/10-s.trace(binary_H*X)*S*T/10-s.trace(binary_E*X)*T*T/10
 return s.Matrix.hstack(*[coeff(v*z0,3) for z0 in mon(1)])
def splitV(B0):
 act=lambda A0,A1,Y:A0*Y-Y*A1
 C=act(binary_H,H1,act(binary_H,H1,B0))+2*(act(binary_E,E1,act(binary_F,F1,B0))+act(binary_F,F1,act(binary_E,E1,B0)))
 return (24*B0-C)/16

def op(Q,R,F):
 K=(B6*Q*B6inv).applyfunc(s.expand);out=[{},{}]
 for ii in range(3):
  one=FW(K,[wedge({(ii,):1},ff) for ff in F])
  two=[wedge({(ii,):1},ff) for ff in FWadj(K,F)]
  out=adds(out,sc(R[ii],[contract(coords,ff) for ff in adds(one,sc(-1,two))]))
 return out
zz=s.symbols('free_form0:20');keys=list(combinations(range(5),2))
freeform=[dict(zip(keys,zz[10*j:10*j+10])) for j in range(2)]
zv=s.symbols('free_lie0:3'); Z=zv[0]*binary_E+zv[1]*binary_F+zv[2]*binary_H
K19=-EC(Z)/2+ES(spinrep(Z))/2-E10(mixedV(Z))+E01(mixedV(Z))
eqvec(op(K19,r,freeform),[{},{}])
print('PASS: positive-Lie identity (co19 type), full20-symbol exterior input.',flush=True)
K28=-2*EC(H0)+8*E10(BH)+8*E01(BH)
eqvec(adds(op(K28,r,freeform),op(s.eye(6),rh,freeform)),[{},{}])
print('PASS: quartic/positive-H identity (co28 type), full20-symbol exterior input.',flush=True)
Q=op4(gen4); PV=pV(H0*Q-Q*H0)
scalar=tv(hp,gen4,4)/s.factorial(4)**2
jd=tv(hp,gen4,2)/144
K32=s.Rational(3,2)*scalar*s.eye(6)-s.Rational(15,32)*(EC(PV)+ES(spinrep(PV)))-s.Rational(3,2)*EC(op4(jd))+6*E10(mixed5(jd))+6*E01(mixed5(jd))
L32=-EC(Q)/4+E10(mixed5(gen4))+E01(mixed5(gen4))
eqvec(adds(op(K32,r,freeform),op(L32,rh,freeform)),[{},{}])
print('PASS: bilinear-quartic identity (co32 type), both quartics and exterior input free.',flush=True)
ss=s.symbols('free_sextic0:7'); sext=sum(c*m for c,m in zip(ss,mon(6)));X=op6(sext)
PV=pV(H0*X+X*H0); BM=splitV(X*BH)
zero_matrix(BM+s.Rational(5,8)*mixedV(PV))
K9=s.Rational(5,16)*(EC(PV)-ES(spinrep(PV)))-E10(BM)+E01(BM)
eqvec(op(K9,r,freeform),[{},{}])
print('PASS: sextic/quartic identity (co9 type), full20-symbol exterior input.',flush=True)
print('All identities hold before applying any monad arrow or curve quotient.')
