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

# Complete abstract binary coefficient identity, not actual source evaluation.
bS,bT,aa,bb=s.symbols('binaryS binaryT alpha beta')
qq=s.symbols('quartic0:5')
gg=sum(qq[i]*bS**(4-i)*bT**i for i in range(5))
pp=bS*bS*(aa*bS+bb*bT)
tau2=s.expand(s.diff(gg,bS,2)*s.diff(pp,bT,2)-2*s.diff(gg,bS,bT)*s.diff(pp,bS,bT)+s.diff(gg,bT,2)*s.diff(pp,bS,2))
expected=(12*aa*qq[2]-12*bb*qq[1])*bS**3+(36*aa*qq[3]-12*bb*qq[2])*bS*bS*bT+72*aa*qq[4]*bS*bT*bT+24*bb*qq[4]*bT**3
assert s.expand(tau2-expected)==0
rr=s.symbols('row0:4')
paired=s.expand(sum(rr[i]*tau2.coeff(bS,3-i).coeff(bT,i) for i in range(4)))
assert paired.coeff(aa).coeff(qq[2])==12*rr[0]
assert paired.coeff(aa).coeff(qq[3])==36*rr[1]
assert paired.coeff(aa).coeff(qq[4])==72*rr[2]
assert paired.coeff(bb).coeff(qq[4])==24*rr[3]
print('PASS: the full five-space acting on ell^2 W spans the entire cubic space, coefficient by coefficient.')
print('PASS: no nonzero row can satisfy the necessary pure-right-factor principal equation.')
print('No actual source coefficient, matrix, rank, selected point, or scan was evaluated.')
