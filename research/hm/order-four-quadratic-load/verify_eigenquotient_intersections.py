"""Universal intersection arithmetic only; no HM coefficients or rank samples.
Requires Python 3 and SymPy. Run: python verify_eigenquotient_intersections.py
"""
import sympy as s
L,H,k,m=s.symbols('L H k m')
relation=s.Poly(L**2-5*H*L+10*H**2,L)
def integral(expr):
    reduced=s.rem(s.Poly(s.expand(expr),L),relation).as_expr()
    return s.expand(reduced).coeff(L,1).coeff(H,3)*2
T=2*L+(k-5)*H
assert integral(L**4)==50
assert integral(H*L**3)==30
assert integral(H**2*L**2)==10
assert integral(H**3*L)==2
assert s.expand(integral(L**3*T)-(30*k-50))==0
assert s.expand(integral(H*L**2*T)-(10*k+10))==0
Kplus2A=2*L+(k-3)*H
Kplus4A=4*L+(k-3)*H
assert s.expand(integral(Kplus2A*L**2*T)-(10*k*k+40*k-130))==0
assert s.expand(integral(Kplus4A*L**2*T)-(10*k*k+100*k-230))==0
# On the blowup at a point in a smooth fourfold, exceptional E^4=-1;
# positive-degree pullback factors restrict trivially on E.
E=s.symbols('E')
assert s.expand((-E)**3*(-m*E)).coeff(E,4)*(-1)==-m
assert s.expand(s.expand((-E)**2*(-m*E)*(1-m)*E).coeff(E,4)*(-1)-m*(1-m))==0
assert s.expand(s.expand((-E)**2*(-m*E)*(-(m+1))*E).coeff(E,4)*(-1)+m*(m+1))==0
for twist in range(1,5):
    print('twist',twist,'nef degree',30*twist-50,
          'curve canonical degree before corrections',10*twist**2+40*twist-130)
print('PASS: universal projective-bundle and exceptional-divisor identities')
