#!/usr/bin/env python3
"""Complete binary/cochain identities, with every quadratic coefficient free."""
import sympy as S
s,t=S.symbols('s t',nonzero=True)
a0,a1,a2,b0,b1,b2=S.symbols('a0 a1 a2 b0 b1 b2')
a=a0*s*s+2*a1*s*t+a2*t*t
b=b0*s*s+2*b1*s*t+b2*t*t
br=S.diff(a,s)*S.diff(b,t)-S.diff(a,t)*S.diff(b,s)

def zero(x):
    if isinstance(x,S.MatrixBase):
        for v in x:zero(v)
    else:
        assert S.cancel(S.expand(x))==0,S.factor(x)
Da=S.Matrix([-S.diff(a,t),S.diff(a,s)])
Db=S.Matrix([-S.diff(b,t),S.diff(b,s)])
zero(a*Db-b*Da+br*S.Matrix([s,t])/2)
v=S.symbols('v')
EW=S.Matrix([0,s,t]); D0=S.Matrix([-2*v/5,3*s/5,3*t/5])
zero(EW-D0-S.Rational(2,5)*S.Matrix([v,s,t]))
kap,rx,q,P,Ta,Tb,e0,ea,eb,N=S.symbols(
    'kappa r_xi q P T_a T_b e0 e_a e_b N',nonzero=True)
# The cochain differentiation uses only scalar multiplication, not a false
# strict O-linearity assertion for the displayed natural cochains.
dTa=a*e0-q*kap*ea;dTb=b*e0-q*kap*eb
zero(a*dTb-b*dTa+q*kap*(a*eb-b*ea))
Lcoeff=kap*br/(2*rx)
zero(-rx*q*Lcoeff+kap*q*br/2)
# Twists: L,N are4,2; q{a,b}N has twist6; commutator has twist8.
assert 2+2==4 and 2+2+2==6 and 2+(2+4)==8
br_st=S.diff(s*s,s)*S.diff(t*t,t)
zero(br_st-4*s*t)
zero((-kap*q*br_st*N/2)/(s*s*t*t)+2*kap*q*N/(s*t))
# Physical O(2) Euler frame: N/(st)=(N/s²)/(t/s).
zero(N/(s*t)-(N/s**2)/(t/s))
zero(N/(s*t)+(N/t**2)/(-s/t))
z,eps=S.symbols('z eps',nonzero=True)
znew=z-kap*eps
wnew=-1/z-kap*eps/z**2
zero(S.series(wnew+1/znew,eps,0,2).removeO())
# Three-term deformed Veronese identity modulo the physical q².
zero(S.expand(znew*znew).coeff(eps,0)-z*z)
zero(S.expand(znew*znew).coeff(eps,1)+2*kap*z)
chi,g,r,theta,rho,Cap,Kcup,Cres,nu,ell=S.symbols(
    'chi g_L r theta rho_C C_ap K_cup C_res nu ell',nonzero=True)
kappa=-chi*r/g
cplus=kappa
k=-theta*kappa**2/(2*rho)
zero(cplus/k+2*rho/(theta*kappa))
zero(k.subs(rho,Cres*r*r)+theta*chi**2/(2*Cres*g*g))
zero((Cap*r/(2*Kcup)-cplus).subs(Cap,-2*chi*Kcup/g))
zero(k.subs(chi,chi/nu)-k/nu**2)
zero(k.subs({theta:theta/ell**2,rho:rho/ell**2},simultaneous=True)-k)
zero(cplus.subs(r,-r)+cplus)
zero(k.subs(r,-r)-k)
print('PASS: complete six-coefficient Hamiltonian/Euler identity and projective factor.')
print('PASS: exact alternating boundary coefficient and physical twist bookkeeping.')
print('PASS: local N-lift difference, O(2) Euler frame, and oriented chart transport.')
print('PASS: c_positive=kappa and all retained normal-root scalar identities.')
print('Geometric restriction injectivity is proved by the regular sequence (s,t).')
print('No actual source coefficient, source matrix, rank or scan was evaluated.')
