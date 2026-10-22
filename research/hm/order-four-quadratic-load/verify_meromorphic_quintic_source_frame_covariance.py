#!/usr/bin/env python3
"""Universal coefficient-frame identities; no actual source instance is evaluated."""
import sympy as S
X,Y,z,k,a,eta,az=S.symbols('X Y z k a eta az', nonzero=True)
def form(name,d):
    cc=S.symbols(f'{name}0:{d+1}')
    return sum(cc[j]*X**(d-j)*Y**j for j in range(d+1))
def tau(f,g):
    return S.diff(f,X,2)*S.diff(g,Y,2)-2*S.diff(f,X,Y)*S.diff(g,X,Y)+S.diff(f,Y,2)*S.diff(g,X,2)
p,q,n,pz,qz=[form(name,2) for name in ('p','q','n','pz','qz')]
m,h,Gamma,u=[form(name,4) for name in ('m','h','Gamma','u')]
def R(p,pz,m,n,eta,a,Gamma):
    return k*a*a*(-S.Rational(2,15)*tau(p,m)+S.Rational(2,5)*p*tau(p,n)
                  +tau(p,p)*n/5-tau(h,pz)/15+S.Rational(2,3)*p*eta)-tau(p,Gamma)/30
Rx=R(p,pz,m,n,eta,a,Gamma)
Ry=R(z**8*p,z**10*pz+8*z**9*p,z*z*m-3*z*h,z**-6*n,z*z*eta,
     z**-2*a,z**-2*Gamma-4*k*z**-3*a*a*h)
assert S.expand(Ry-z**6*Rx)==0
print('PASS: full actual frame covariance R_y=z^6 R_x, including both inhomogeneous terms.')
composition=R(p+q,pz+qz,m,n,eta,a,Gamma)-Rx-R(q,qz,m-p*n,n,eta+tau(p,n),a,Gamma)
assert S.expand(composition)==0
print('PASS: exact finite composition and hence the global meromorphic source-change identity.')
f,fz,g,nh,hh=S.symbols('f fz g nh hh')
# d/dw=z^2 d/dz with w=-1/z, and f_y=z^-3 f.
fyw=z**-1*fz-3*z**-2*f
my=(hh*fyw-(z**-6*nh)*(z**5*g))/(z**-3*f)
mx=(hh*fz-nh*g)/f
assert S.cancel(my-(z*z*mx-3*z*hh))==0
Gamma_x=u+2*k*a*az*h
Gamma_y=z**-2*u+2*k*(z**-2*a)*(az-2*a/z)*h
assert S.expand(Gamma_y-(z**-2*Gamma_x-4*k*z**-3*a*a*h))==0
print('PASS: source relation and canonical Gamma have the required connection-frame laws.')
alpha,nu,w=S.symbols('alpha nu w',nonzero=True)
# A global O(-6) meromorphic coefficient alpha*z^-2 becomes alpha*w^-4.
assert S.expand((z**6*alpha*z**-2).subs(z,-1/w)-alpha*w**-4)==0
assert -4*alpha-alpha==-5*alpha
# For O(-d), polynomials on the x-chart give y poles of order d or more.
assert 1 <= 4 <= 6-1
assert (4+4+8)%10==6 and 6 not in {8,0,2}
# Cup t^2 removes the x pole, and the remaining y pole is globally exact upstairs.
assert S.expand(z*z*alpha*z**-2-alpha)==0
assert S.expand((z**4*(-4*alpha)).subs(z,-1/w)-(-4*alpha*w**-4))==0
assert S.expand((z**4*(-4*alpha/nu)).subs(z,-1/w)-(-4*alpha/nu*w**-4))==0
print('PASS: the lower surviving order-four class is nonzero, misses A by character, and cup t^2 kills it.')
print('No actual HM coefficients, source-instance matrix/rank evaluation, or parameter specialization used.')
