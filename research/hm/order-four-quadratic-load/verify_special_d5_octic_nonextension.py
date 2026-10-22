"""Universal identities supporting the two independent nonextension proofs.
No actual HM coefficients or selected boundary ranks are evaluated.
"""
import sympy as s
x,y,z,u,B,D,e,c,k,A,rho,sigma=s.symbols('x y z u B D e c k A rho sigma',nonzero=True)
# Short inversion proof: exact plane trace of the explicit baseline.
q=A*y*y+B*u*u; a=c*y; g=k*x*z*z-a*q
base=(rho*x*x+sigma*y*z)*g*g/k**2
assert s.expand(base.subs(x,0)-sigma*y*z*a*a*q*q/k**2)==0
assert len({(1,1,0),(0,0,2),(0,2,0)})==3  # yz, u², z² independent
# Independent two-colon proof, with nonzero parameters still indeterminate.
q=y*y+B*u*u; qc=y*y+D*u*u; g=x*z*z-y*q
alpha=D/B; beta=1-alpha
F0=x*x*q*qc**2-beta**2*x**3*y**3*z*z
assert s.expand(F0-(alpha**2*x*x*q**3+2*alpha*beta*x*x*y*y*q*q-beta**2*x*x*y**3*g))==0
G=x*z*z-y**3
target=(x*x+e*y*z)*G*G
HR=s.cancel((target-F0.subs(u,0))/z)
H1=e*(-alpha*q*q*g+beta*y*g*g)
assert s.expand(H1.subs(x,0)-e*y*q*q*qc)==0
LR=s.cancel((HR-H1.subs(u,0))/x)
assert s.expand(LR.subs(x,0)+e*alpha*y**4*z*z)==0
assert s.Rational(s.binomial(4,2)**2,s.binomial(8,4)) !=0
assert (-14)%5==1
print('PASS: inversion trace identity, independent two-colon contradiction, Cartan coefficient, scalar12 mismatch')

coeffs=[s.Rational(2*s.binomial(4,0)*s.binomial(4,4),s.binomial(8,4)),s.Rational(2*s.binomial(4,1)*s.binomial(4,3),s.binomial(8,4)),s.Rational(s.binomial(4,2)**2,s.binomial(8,4))]
assert coeffs==[s.Rational(1,35),s.Rational(16,35),s.Rational(18,35)]
print('PASS: exact Cartan X^4 Y^4 polarization coefficients 1/35, 16/35, 18/35')
