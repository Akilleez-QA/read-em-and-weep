"""Universal Riemann--Roch identities; no selected HM coefficients or ranks.
Run: python verify_conductor_euler_polynomials.py  (requires sympy).
"""
import sympy as s
r, t, n, k = s.symbols('r t n k')
# ch(Sym^r E), from formal Chern roots with c1(E)=5H,c2(E)=10H^2.
c0 = r + 1
c1 = s.Rational(5, 2)*r*(r+1)
c2 = s.Rational(5, 4)*r*(r+1)*(2*r-1)
c3 = s.Rational(25, 24)*r*r*(r+1)*(r-3)
# td(Q3)=1+3H/2+13H^2/12+H^3/2, integral H^3=2.
chi_Q = s.expand(2*(c0*(t**3/6+3*t*t/4+13*t/12+s.Rational(1,2))
    +c1*(t*t/2+3*t/2+s.Rational(13,12))
    +c2*(t+s.Rational(3,2))+c3))
jet_loss = s.Rational(50,24)*n*(n+1)*(n+2)*(n+3)
structure = s.Poly(s.expand(chi_Q.subs({r:n,t:0})-jet_loss), n)
eigen = s.Poly(s.expand(chi_Q.subs({r:n+2,t:k-5})-jet_loss), n)
assert structure.degree() == 3 and eigen.degree() == 3
assert s.expand(structure.as_expr()-(-55*n**3/s.Integer(6)-20*n*n-59*n/s.Integer(6)+1)) == 0
# ch(O_Gamma)=6a^2-11a^3; coefficient extraction includes factorials.
def pullback_chi(p):
    return s.factor(12*p.nth(2)-66*p.nth(3))
assert pullback_chi(structure) == 365
assert s.expand(pullback_chi(eigen)-15*(2*k*k-10*k+7)) == 0
assert pullback_chi(eigen).subs(k,3) == -75
assert pullback_chi(eigen).subs(k,4) == -15
normal_chi = {3:5-150,4:185-150}
for twist in (3,4):
    target_chi = normal_chi[twist]-pullback_chi(eigen).subs(k,twist)
    assert target_chi == {3:-70,4:50}[twist]
    print(f'k={twist}: chi(normal)={normal_chi[twist]}, chi(S)={pullback_chi(eigen).subs(k,twist)}, chi(conductor)={target_chi}, conductor degree={target_chi-40}')
print('PASS: universal Euler polynomials and conductor degrees')
