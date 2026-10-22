"""Universal exact residue identities with all source parameters unassigned."""
import sympy as S
X,Y,s,t,z,A,B,c,e,k=S.symbols('X Y s t z A B c e k',nonzero=True)
f=A*X**2*Y+B*Y**3*z+A*c*X**3*z*z-B*c*X*Y**2*z**3
mons=[X**4,X**3*Y,X*X*Y*Y,X*Y**3,Y**4]
Q=[e*(-B*X*Y*t*t/(2*A)-B*Y*Y*s*s/(2*A*c)),e*(X*X*s*t+B*Y*Y*t*t/A)/4,-e*X*Y*s*t/2,e*(-A*X*X*s*s/B+Y*Y*s*t)/4,e*(A*X*Y*s*s/B-A*c*X*X*t*t/B)/2]
def q(p):
 return S.expand(sum(S.Poly(p,X,Y).coeff_monomial(m)*v.subs({s:1,t:z}) for m,v in zip(mons,Q)))
px=-B*Y**4-A*c*X**3*Y*z+B*c*X*Y**3*z*z
py=A*X*X*Y*Y/z
assert S.expand(py-px-f*Y/z)==0
assert S.expand(q(px)+e*A*X*Y/2)==0
assert S.expand(q(py)+e*A*X*Y/2)==0
def pair(p,q):
 p=S.Poly(p,X,Y,s,t);q=S.Poly(q,X,Y,s,t)
 return S.expand(sum((-1)**(i+j)/S.binomial(2,i)/S.binomial(2,j)*p.coeff_monomial(X**i*Y**(2-i)*s**j*t**(2-j))*q.coeff_monomial(X**(2-i)*Y**i*s**(2-j)*t**j) for i in range(3) for j in range(3)))
R=X*Y*s*s+c*X*X*t*t/2
for v in Q:assert S.cancel(pair(R,v))==0
assert S.expand(X*Y*s*s-S.Rational(2,3)*R-2*B/(3*e*A)*Q[4])==0
assert S.cancel((-3*k*e*A/(2*B*c))*S.Rational(2,3)+k*e*A/(B*c))==0
print('PASS: actual connecting residue, both regular local lifts, five apolar orthogonality identities, and canonical P4 projection factor2/3.')
print('No fourth value or absolute normal-coordinate scalar is supplied.')
