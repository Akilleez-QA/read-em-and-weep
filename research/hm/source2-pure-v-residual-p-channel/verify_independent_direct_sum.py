#!/usr/bin/env python3
"""Independent quotient-injectivity certificate without transvectants."""
import sympy as s
from math import comb
x,y=s.symbols('x y'); z=s.sqrt(5)
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
G=s.Matrix(7,7,lambda i,j:s.Rational((-1)**i,comb(6,i)) if i+j==6 else 0)
E=G.inv()*Pi.T
# Polarize by literal coefficient extraction from f(x+X,y+Y), degree 2 in X,Y.
X,Y=s.symbols('X Y')
def polarization(n):
 cols=[]
 for k in range(n+3):
  f=s.Poly(s.expand((x+X)**(n+2-k)*(y+Y)**k),X,Y,x,y)
  cols.append(s.Matrix([f.coeff_monomial(X**(2-j)*Y**j*x**(n-i)*y**i) for j in range(3) for i in range(n+1)]))
 return s.Matrix.hstack(*cols)
P=polarization(4)*E
cols=[]
for b in range(3):
 for c in range(4):
  v=s.zeros(21,1)
  for j in range(3):
   for i in range(5):v[j*7+i+b,0]+=P[j*5+i,c]
  cols.append(v)
D=polarization(6); T=s.Matrix.hstack(D,*cols)
value=s.simplify(T.det())
if T.shape!=(21,21) or value==0:raise RuntimeError('direct quotient independence failed')
print('PASS: direct polarization-plus-descendants determinant =',value)
