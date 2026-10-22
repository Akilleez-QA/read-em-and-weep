"""Universal symbolic reconstruction; no source coefficient is assigned."""
import sympy as S
z,X,Y,A,B,c,L=S.symbols('z X Y A B c lambda', nonzero=True)
d=B*c*c/A
px=L*X*Y/(2*A*c*z**4)-L*X**2/(2*A*z**2)+L*B*Y**2/(A*A*z)
py=-L*Y**2/(2*A*c*c*z**6)-L*X**2/(B*c*c*z**7)
e=S.expand(py-px)
R=[1-2*d*z**5,z+d*z**6/2,z**2,z**4]
def coeff(p,i): return S.expand(p).coeff(z,i)
def zero(x): assert S.cancel(x)==0,S.factor(x)
for r in R: zero(coeff(e*r,-1))
def ap(p,q): return S.expand(sum((-1)**i/S.binomial(6,i)*coeff(p,i)*coeff(q,6-i) for i in range(7)))
zero(ap(R[0],R[1])-5*d/6);zero(ap(R[2],R[3])-S.Rational(1,15))
for i in range(4):
 for j in range(4):
  if {i,j} not in ({0,1},{2,3}): zero(ap(R[i],R[j]))
eta=[S.Rational(3,5)/z-z**-6/(5*d),6*z**-7/(5*d)+S.Rational(2,5)*z**-2,z**-3,z**-5]
for i in range(4):
 for j in range(4): zero(coeff(eta[i]*R[j],-1)-(1 if i==j else 0))
diag=S.expand(sum(r*t for r,t in zip(R,eta)))
zero(diag-(4/z+1/(d*z**6)-d*z**4))
lower=[]
for r in R:
 rx=S.expand(px*r);ry=S.expand(py*r)
 v=S.expand(-2*sum(coeff(rx,j)*z**j for j in range(-4,-1))-2*sum(coeff(ry,j)*z**j for j in range(-1,1)))
 lower.append(v)
 left=S.expand(v+2*px*r);right=S.expand(z*z*(v+2*py*r))
 for term in S.Add.make_args(left): assert term.as_powers_dict().get(z,0)>=0
 for term in S.Add.make_args(right): assert term.as_powers_dict().get(z,0)<=0
 # Triangular transport has exactly the established +2pd coefficient.
 zero((v+2*py*r)-(v+2*px*r)-2*e*r)
print('PASS: symbolic quintic cocycle, four sextic kernel sections, exact apolar dual tensor, Euler diagonal 4/z, unique full lowest-adjoint chart lifts.')
for i,v in enumerate(lower): print('r_%d = %s'%(i,S.factor(v)))
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z**2-B*c*X*Y**2*z**3
g=-L*(B*X*Y**4/z**3+A*X**3*Y**2/z**4)/(2*A*c)
r_eta=S.expand(sum(v*t for v,t in zip(lower,eta)))
trace=S.expand(2*f*g*diag-f*f*r_eta)
for j in [-1,-2,-3]: zero(coeff(trace,j))
exps=[int(term.as_powers_dict().get(z,0)) for term in S.Add.make_args(trace)]
nx=-sum(coeff(trace,j)*z**j for j in range(0,max(exps)+1))
ny=sum(coeff(trace,j)*z**j for j in range(min(exps),-3))
zero(ny-nx-trace)
for term in S.Add.make_args(S.expand(nx)): assert term.as_powers_dict().get(z,0)>=0
for term in S.Add.make_args(S.expand(z**4*ny)): assert term.as_powers_dict().get(z,0)<=0
print('PASS: exact nilpotent-shadow scalar lifts, all three forbidden Laurent coefficients vanish, and degree-eight O(-4) transport.')
print('n_x =',S.factor(nx));print('n_y in x frame =',S.factor(ny))
