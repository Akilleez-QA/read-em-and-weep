#!/usr/bin/env python3
import sympy as s
alpha,beta,nu,detR=s.symbols('alpha beta nu detR', nonzero=True)
f,g,t,u,v=s.symbols('f g t u v')
P=s.diag(alpha,beta); d=alpha*beta
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
Nprime=N.subs({f:alpha*f,g:beta*g})
assert s.simplify(Nprime-d*P*N*P.inv())==s.zeros(2)
T=s.Matrix([[t,u],[v,-t]])
Tprime=s.Matrix([[alpha*beta*t,alpha**2*u],[beta**2*v,-alpha*beta*t]])/detR**2
nuprime=d*nu/detR**2
assert s.simplify(Tprime/nuprime-P*(T/nu)*P.inv())==s.zeros(2)
a,b,c,r=s.symbols('a b c r',nonzero=True)
S=s.eye(2)+s.Matrix([[b*g,-b*f],[-a*g,a*f]])
assert s.simplify(S*s.Matrix([f,g])-s.Matrix([f,g]))==s.zeros(2,1)
assert s.expand(S.det()-1-a*f-b*g)==0
H=s.Matrix([[a,b],[b,c]])
r11,r12,r21,r22,h11,h12,h22=s.symbols('r11 r12 r21 r22 h11 h12 h22')
R=s.Matrix([[r11,r12],[r21,r22]])
H2=s.Matrix([[h11,h12],[h12,h22]])
trans=lambda Q:R.T.inv()*Q*R.inv()
mix=lambda U,V:U[0,0]*V[1,1]+U[1,1]*V[0,0]-2*U[0,1]*V[0,1]
assert s.cancel(trans(H).det()-H.det()/R.det()**2)==0
assert s.cancel(mix(trans(H),trans(H2))-mix(H,H2)/R.det()**2)==0
S1=s.Matrix([[f,0],[2*g,-f]])
assert s.simplify(S1.subs({f:alpha*f,g:beta*g})-alpha*P*S1*P.inv())==s.zeros(2)
assert -s.Rational(2)-s.Rational(5,2)==-s.Rational(9,2)
assert s.Rational(5)-s.Rational(5,2)==s.Rational(5,2)
assert -s.Rational(5,2)-2-s.Rational(1,2)==-5
print('PASS: determinant/normal unit cancellation, diagonal generator covariance, and coefficient line Wprime O(-5).')
print('No actual source coefficients or rank evaluation used; global matching requires the cited geometric inputs.')
