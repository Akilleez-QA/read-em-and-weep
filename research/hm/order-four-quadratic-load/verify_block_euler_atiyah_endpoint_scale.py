#!/usr/bin/env python3
"""Universal marked-extension, Cech-sign, and scalar comparison identities."""
import contextlib
import io
from pathlib import Path
import runpy
import sympy as S

with contextlib.redirect_stdout(io.StringIO()):
    runpy.run_path(str(Path(__file__).with_name('verify_apolar_normal_section_euler.py')))
print('PASS: exact apolar normal/section comparison has Euler coefficient one.')

mu,rhoC,rhov,z,f,g=S.symbols('mu rho_C rho_v z f g',nonzero=True)
J0=S.Matrix([[0,-1],[1,0]])
sigma=S.Matrix([f,g]);n=sigma*sigma.T*J0;NC=-n
I=S.eye(2)
def zero(x):
    if isinstance(x,S.MatrixBase):
        for e in x: zero(e)
    else:
        assert S.cancel(S.expand(x))==0,S.factor(x)

conic=mu**-2*rhoC;vertex=mu**2*rhov
normalized_conic=S.cancel(conic/mu**2)
zero(vertex/mu**2-rhov)
zero(S.diff(normalized_conic,mu).subs(mu,1)+4*rhoC)
t=rhoC/z
P=I+mu**-4*t*NC
Pinv=I-mu**-4*t*NC
zero(P*Pinv-I)
euler=(S.diff(P,mu)*Pinv).subs(mu,1)
zero(euler+4*t*NC)
zero(euler-4*rhoC*n/z)
zero(S.trace(euler))
# The coefficient and nilpotent have separate weights -2.
zero(mu**-2*mu**-2-mu**-4)
assert 3*S.Rational(-2,5)+2*S.Rational(3,5)==0
print('PASS: fully marked torus derivative is -4 rho_C N_C/z = +4 rho_C n/z.')

# Same positive source-to-target transition for section and operator defects.
q,e,b,c,a12,a21,a11,H,rho,de,db,dc=S.symbols(
    'q e b c a12 a21 a11 H rho de db dc')
eta=S.Matrix([[e,b],[c,-e]])
deta=S.Matrix([[de,db],[dc,-de]])
A=S.Matrix([[a11,a12],[a21,-a11]])
Pplus=I+q*eta;invplus=I-q*eta
coefficient=lambda matrix:matrix.applyfunc(lambda x:S.expand(x).coeff(q,1))
boundary=coefficient(n-Pplus*n*invplus)
zero(boundary+eta*n-n*eta)
dP=q*(deta+rho*eta)
operator_defect=coefficient(A-(Pplus*A*invplus-H*dP*invplus))
zero(operator_defect-(H*deta+A*eta-eta*A+H*rho*eta))
print('PASS: positive transition gives boundary -[eta,N], but operator defect +L(eta).')

theta,r,kappa,ell,nu=S.symbols('theta r kappa ell nu',nonzero=True)
k=r*kappa
cb=2*rhoC*r/theta
zero(cb/k-2*rhoC/(theta*kappa))
zero((-cb)/k+2*rhoC/(theta*kappa))
# Fixed-N Serre remarking: rho_C and theta have the same inverse-square factor.
zero(2*(rhoC/ell**2)/((theta/ell**2)*kappa)-cb/k)
# Fixed-N physical equation change q0 -> nu q0.
zero((cb/nu)/(k/nu**2)-2*rhoC/(theta*(kappa/nu)))
# Exchange with fixed N and boundary-normalized xi.
rp=-r;kp=-kappa;k_boundary_prime=rp*kp
zero(k_boundary_prime-k)
zero(2*rhoC*rp/theta+cb)
# In contrast, naturally transported xi has r unchanged and k reversed.
zero(r*kp+k)
print('PASS: single ambient multiplier formula, section/equation factors, and both endpoint normalizations.')
print('No actual value of kappa, endpoint distance, or fourth Bockstein is supplied.')
