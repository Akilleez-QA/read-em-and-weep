import sympy as s,json
from math import comb
x,y,p,q,t,aa,bb=s.symbols('x y p q t alpha beta');z=s.sqrt(5)
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
G6=gram(6);GD=gram(4);E=G6.inv()*Pi.T*(Pi*G6.inv()*Pi.T).inv();GP=s.simplify(E.T*G6*E)
a=p*x*x+q*x*y+t*y*y
L=s.Matrix.hstack(*[Pi*cv(a*x**(4-i)*y**i,6) for i in range(5)])
Ls=s.simplify(GD.inv()*L.T*GP)
def rho(n):return s.Matrix.hstack(*[cv(s.diff(a,x)*s.diff(x**(n-i)*y**i,y)-s.diff(a,y)*s.diff(x**(n-i)*y**i,x),n) for i in range(n+1)])
DP=s.simplify(Pi*rho(6)*E);DD=rho(4)
R1=s.simplify(DD*Ls);R2=s.simplify(Ls*DP)
