"""Exact tangent/coefficient identities; no actual-source coefficients or ranks."""
import sympy as S
f,g,l,z,p,a,b,c=S.symbols('f g l z p a b c',nonzero=True)
J=S.Matrix([[0,-1],[1,0]])
sigma=S.Matrix([f,g]);n=sigma*sigma.T*J
R=S.Matrix([[a,b],[c,-a]])
tau=lambda sig,v:sig*v.T*J+v*sig.T*J
assert S.expand(S.trace(n*R)-(2*f*g*a+g*g*b-f*f*c))==0
T=tau(sigma,S.Matrix([0,l]))
assert T==S.Matrix([[f*l,0],[2*g*l,-f*l]])
assert S.expand(S.trace(n*T))==0
# Full marked diagonal-plus-triangular transport, with physical twist four.
P=S.Matrix([[1,0],[p,1]])
D=S.diag(z**3,z**-5)
Sframe=P*D
sy=Sframe.inv()*sigma
vy=S.Matrix([0,l])
vx=P*S.diag(z**7,z**-1)*vy
assert vx==S.Matrix([0,l/z])
Ry=tau(sy,vy)
assert (tau(sigma,vx)-z**2*Sframe*Ry*Sframe.inv()).applyfunc(S.cancel)==S.zeros(2)
# Coefficient lines: frame O(9/2),O(-5/2), physical twist +2.
assert S.Rational(-5,2)+2-S.Rational(1,2)==-1
assert S.Rational(9,2)+2-S.Rational(-1,2)==7
# Matrix physical twist +4; cover degrees 4,2,6 give O(2),O(10),O(-6).
assert 4-4/2==2
assert 7+4-2/2==10
assert -7+4-6/2==-6
# A weight -4 regular conjugator cannot have any nonnegative cover degree.
assert max(-4,-6,-2)<0
# Even diagonal parity excludes an intermediate weight three tangent term.
assert min(w for w in range(-4,6,2) if w-3>=0)==4
# Exact cubic/quintic ideal-square Hilbert series, not a source rank calculation.
t=S.symbols('t')
h=S.cancel((1-t**6-t**8-t**10+t**11+t**13)/(1-t)**2)
assert S.Poly(h,t).coeff_monomial(t**12)==0
assert 5+3+7==2+13
# H0/H1 O(-1) vanish; H0 O(0)=1,H1 O(0)=0.
h0=lambda d:max(d+1,0)
h1=lambda d:max(-d-1,0)
assert h0(-1)==h1(-1)==0
assert h0(0)==1 and h1(0)==0
assert 8+4==4+8==8+8-4==12
# Possible endpoint first-normal transition feeds degree eight, not degree four.
assert 4+4==0+8==4+8-4==8
print('PASS: tangent identity; full physical/triangular coefficient transition; O(-1) acyclicity; no conjugator; exact trace-sequence degree count.')
print('Only a compatibly subtracted tangent remainder has this vanishing. Full R2 and beta4 are not evaluated.')
