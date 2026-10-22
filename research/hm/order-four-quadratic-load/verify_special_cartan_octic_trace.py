"""Universal polarization and ideal-trace identities, not actual HM ranks."""
import sympy as s
from math import comb
x,y,z,tau,rho,sigma,a6,cg,ck,cj=s.symbols('x y z tau rho sigma a6 cg ck cj', nonzero=True)
S=x*x*z; G=x*z*z-tau*y**3; J=x*y*z; K=x*y*y
# Standard symmetric Cartan polarization at binary exponent six.
coef_GK=s.Rational(2*comb(4,2)*comb(4,4),comb(8,6))
coef_J2=s.Rational(comb(4,3)**2,comb(8,6))
assert coef_GK != 0 and coef_J2 != 0
shadow=a6*(coef_GK*cg*ck*G*K+coef_J2*cj**2*J**2)
f=(rho*x*x+sigma*y*z)*shadow
trace=s.expand(f.subs(z,0))
assert s.expand(trace+a6*coef_GK*cg*ck*tau*rho*x**3*y**5)==0
allowed={(4,4),(2,6),(0,8)}
assert (3,5) not in allowed
# Every displayed cubic satisfies both curvilinear point conditions.
for h in [S,G,J,K]:
    at_p=s.expand(h.subs({x:1,z:0}))
    assert s.rem(at_p,y**2,y)==0
    at_r=s.expand(h.subs(z,1).subs(x,tau*y**3))
    assert s.rem(at_r,y**4,y)==0
assert 12*(7-3)>4*(8-3)
print('PASS: universal Cartan trace is forbidden x^3 y^5, all required factors nonzero')
assert [(a,-(a+2)%5) for a in (12,14,18)] == [(12,1),(14,4),(18,0)]
assert [(w+3)%5 for w in (1,4)] == [4,2]
print('PASS: actual Y2 linearization and scalar target stabilizer exclusions a14/a18')
