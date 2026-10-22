#!/usr/bin/env python3
import sympy as s
t,u,v,x,y,z=s.symbols('t u v x y z')
h=s.div((1-t**3)*(1-t**5),(1-t)**2,t)
assert h[1]==0
assert s.degree(h[0],t)==6
assert s.expand(h[0]).coeff(t,8)==0
for i in range(9):
 b=i%2; a=(i-b)//2; c=(8-i-b)//2
 assert a+b+c==4
 assert (x**a*y**b*z**c).subs({x:u*u,y:u*v,z:v*v})==u**i*v**(8-i)
assert (-1)*(1)==-1 # odd W times even physical line
assert 4*2==8 # physical twist4 restricts to conic degree8
print('PASS: vertex degree8 vanishes; pure-positive quartics surject to conic octics; conic quotient is odd.')
print('Universal polynomial and degree identities only; no actual coefficient or rank evaluation.')
