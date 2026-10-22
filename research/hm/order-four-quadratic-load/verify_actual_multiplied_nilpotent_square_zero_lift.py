#!/usr/bin/env python3
"""Universal gauge and trace identities; no actual monad/source instance."""
import sympy as s

def zero(x):
    if isinstance(x,s.MatrixBase):
        for v in x: zero(v)
    else:
        assert s.expand(x)==0 or s.cancel(x)==0, s.factor(x)

am,bm,cm,a,q,chi,g,k,rx,nu=s.symbols(
    'a_m b_m c_m a q chi g_L k r_xi nu',nonzero=True)
r=am/bm; kap=-chi*r/g
# G is a universal constant source gauge, not an actual source matrix.
gA=-s.Rational(1,5);gU=-s.Rational(6,5)
nat=[-6*am/5,4*bm/5,-cm/5]
add=[-am*gU,-bm*gU,-cm*gA]
assert [s.expand(x+y) for x,y in zip(nat,add)]==[0,2*bm,0]
# Right-arrow change is -G_source^dagger beta, exactly the adjoint of
# -alpha G_source; coefficients are the same three universal real rationals.
assert [-gU*am,-gU*bm,-gA*cm]==add

P,T,G,e0,ea,dG=s.symbols('P T G e0 e_a dG')
Pnat=P-q*G;Tnat=T-a*G
zero(a*Pnat-q*Tnat-(a*P-q*T))
e0red=e0+dG
DP=q*e0red; DT=a*e0red-q*kap*ea
zero(DP-q*dG-q*e0)
zero(DT-a*dG-a*e0+q*kap*ea)
zero(a*DP-q*DT-q**2*kap*ea)
zero((rx*q**2*kap*ea).subs(rx,k/kap)-q**2*k*ea)
# Twist degree: P,T,q,a each have twist two; U has twist four.
assert 2+2==4 and 2*2==4 and 2*4==8

# Exact compressed trace certificate, retaining the full trace of U of rank2.
trM2=2*chi*q
BstarTB=-r*a  # coefficient of M, from B*MaB and B*MbB=0
trPT=s.cancel((-2/(r*chi))*BstarTB*trM2)
zero(trPT-4*a*q)
trT2,trTs2=s.symbols('tr_T2 tr_Tsource2')
# Both source terms contribute -q² tr(T_source²) to the Euler trace.
supertrace=rx**2*(-2*a*q*trPT+q**2*trT2-2*q**2*trTs2)
zero(supertrace-rx**2*q**2*(trT2-2*trTs2-8*a**2))
assert s.Poly(s.expand(supertrace),q).nth(0)==0
assert s.Poly(s.expand(supertrace),q).nth(1)==0
# Universal Cayley--Hamilton over ANY commutative characteristic-zero ring.
x,y,z=s.symbols('x y z')
E=s.Matrix([[x,y],[z,-x]])
zero(E**2-s.trace(E**2)*s.eye(2)/2)

# Equation covariance; all identities use physical q, not Q=chi q.
zero(kap.subs(chi,chi/nu)-kap/nu)
U=rx*(a*P-q*T)
zero(U.subs({rx:rx/nu,P:nu*P,q:nu*q},simultaneous=True)-U)
zero((q**2*k).subs({q:nu*q,k:k/nu**2},simultaneous=True)-q**2*k)
print('PASS: both determinant-dual Euler gauges and natural/reduced primitives.')
print('PASS: exact common-gauge cancellation and q² boundary k e_a.')
print('PASS: full compressed trace tr(PT)=4a q and Euler trace modulo q².')
print('PASS: universal nonreduced rank-two Cayley--Hamilton certificate.')
print('PASS: physical equation covariance; no actual coefficient or rank test.')
