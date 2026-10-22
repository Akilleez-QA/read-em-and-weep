#!/usr/bin/env python3
"""Universal polynomial identities only. No HM instance is evaluated."""
import sympy as s
u11,u12,u22,v11,v12,v22,a,b=s.symbols('u11 u12 u22 v11 v12 v22 a b')
U=s.Matrix([[u11,u12],[u12,u22]])
V=s.Matrix([[v11,v12],[v12,v22]])
z=s.Matrix([a,b])
f=(z.T*U*z)[0];g=(z.T*V*z)[0]
mix=u11*v22+u22*v11-2*u12*v12
lhs=s.Matrix.hstack(U*z,V*z).det()**2
rhs=f*g*mix-f*f*V.det()-g*g*U.det()
assert s.expand(lhs-rhs)==0
p,q=s.symbols('p q',nonzero=True)
coeff_fg=s.cancel(p*q/((p-1)*(q-1))/(p*p*q*q))
coeff_f2=s.cancel(p*p/(q-1)**2/(p*p*q*q))
coeff_g2=s.cancel(q*q/(p-1)**2/(p*p*q*q))
assert coeff_fg.subs({p:3,q:5})==s.Rational(1,120)
assert coeff_f2.subs({p:3,q:5})==s.Rational(1,400)
assert coeff_g2.subs({p:3,q:5})==s.Rational(1,36)
x,y,z0,F,H,G,K=s.symbols('x y z F H G K')
C=s.Matrix([[x,y],[y,z0]])
fv=s.Matrix([F,H]);gv=s.Matrix([G,K])
u=(fv.T*C*fv)[0];v=(fv.T*C*gv)[0];w=(gv.T*C*gv)[0]
assert s.expand(u*w-v*v-(x*z0-y*y)*(F*K-H*G)**2)==0
t,r,ss=s.symbols('t r ss')
N=s.Matrix([[v,-u],[w,-v]]);T=s.Matrix([[t,ss],[r,-t]])
assert (N*T+T*N-(2*v*t-u*r+w*ss)*s.eye(2)).applyfunc(s.expand)==s.zeros(2)
print('PASS: universal Hessian identity, exact Gram determinant, and first-normal correction.')
print('No actual HM coefficients or ranks; global gluing and the cubic value remain uncomputed.')
