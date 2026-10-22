from pathlib import Path
import contextlib,io,sympy as s
base=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
 exec((base/'verify_higher_cartan_lift_and_product_anomaly.py').read_text().split('# Every coefficient below is universal')[0])
ad=s.zeros(3)
for i,Mi in enumerate(Ms):
 com=M*Mi-Mi*M;ad[:,i]=s.Matrix([com[0,1],com[1,0],com[0,0]])
Jv=extract*(s.kronecker_product(ad,s.eye(2))+s.kronecker_product(s.eye(3),M))*Kinc
Fv=Jv*Jv-Q*s.eye(4)
PA=extract*getp(A(p))
zero_matrix(Jv*PA-PA.jacobian(p)*M*p)
zero_matrix(Fv*PA)
zero_matrix(Fv*Fv-8*Q*Fv)
ha,hb,hc,hd,hf=s.symbols('ha hb hc hd hf')
HH=s.Matrix([[ha,hb,hc],[hd,ha,hf],[2*hf,2*hc,-2*ha]])
CH=extract*s.kronecker_product(-HH.T,s.eye(2))*Kinc
hphys=(s.Matrix([[x,y,z]])*HH*s.Matrix([y/2,x/2,z]))[0]/theta
zero_matrix(CH*Fv+Fv*CH-4*theta*hphys*s.eye(4)-8*Q*CH)
assert s.expand(s.trace(CH*Fv)-8*theta*hphys)==0
R=s.Matrix(4,4,s.symbols('R0:16'));r0,r1,r2=s.symbols('r0 r1 r2')
Rs=(r0*u*u+r1*u*w+r2*w*w)*R
Sop=Rs*Fv
# This is w-degree 2 and TOTAL degree 4. The differentiation is w-only.
def full_lift(Sop,eta):
 out=[{},{}]
 for wi,i in [(u,3),(w,4)]:
  out=adds(out,[contract(coords,wedge({(i,):1},f)) for f in E_R(Sop.diff(wi)/2,eta)])
 return out
for wi in [u,w]:zero_matrix(Sop.diff(wi)*PA)
eqvec(full_lift(Sop,A(p)),[{},{}]);eqvec(full_lift(Sop,B(p)),[{},{}])
print('PASS: complete marked Clifford factor, anticommutator, and BOTH full arrow annihilations.')


Am=PA.jacobian(p);Amadj=J.inv()*Am.T*J4
ca=s.Rational(2,3)*theta
zero_matrix(Amadj*Am-ca*phys*s.eye(2))
zero_matrix(Fv-8*theta*phys*s.eye(4)+(8*theta/ca)*Am*Amadj)
# All 24 coefficients of a linear V tensor U -> P map remain free.
BT=s.Matrix(4,6,s.symbols('linearB0:24'))
raw=s.Matrix.vstack(x*s.eye(2),y*s.eye(2),z*s.eye(2))
Blin=BT*raw
BR=BT*Kinc;BZ=BT*spin
zero_matrix(Blin-BR*Am-BZ*M)
# Complete Cartan/spin decomposition, not a source-instance rank computation.
zero_matrix(s.Matrix.hstack(Kinc,spin)*s.Matrix.vstack(extract,cliff)-s.eye(6))
zero_matrix(s.Matrix.vstack(extract,cliff)*s.Matrix.hstack(Kinc,spin)-s.eye(6))
# Full quadratic-w coefficient symbols; by linearity this covers all 72.
q0w,q1w,q2w=s.symbols('base0 base1 base2')
fbase=q0w*u*u+q1w*u*w+q2w*w*w
Bw=fbase*Blin
SS=Bw*Amadj
for wi in [u,w]:zero_matrix(SS.diff(wi)*Am-ca*phys*Bw.diff(wi))
Lnew=[{},{}]
for wi,ii in [(u,3),(w,4)]:
 coeff=putp(Kinc*Bw.diff(wi)*p)
 Lnew=adds(Lnew,sc(ca/2,[contract(coords,wedge({(ii,):1},F)) for F in coeff]))
eqvec(full_lift(SS,A(p)),sc(phys,Lnew))
eqvec(full_lift(SS,B(p)),[{},{}])
# The actual positive off-diagonal block lies in the new spin sector.
Z_H=extract*s.kronecker_product(-HH.T,s.eye(2))*spin
AH=Am.subs({x:(s.Matrix([[x,y,z]])*HH)[0],y:(s.Matrix([[x,y,z]])*HH)[1],z:(s.Matrix([[x,y,z]])*HH)[2]},simultaneous=True)
zero_matrix(Z_H*M+CH*Am+AH)
print('PASS: marked A-adjoint factorization and full Cartan/spin decomposition of all 24 linear tensors.')
print('PASS: complete q-divisible A column and exact vanishing B column, including mixed coefficients.')
print('PASS: the actual positive off-diagonal tensor appears in the additional spin sector.')
print('No actual source coefficient, monad instance, rank, selected point, or scan was evaluated.')
