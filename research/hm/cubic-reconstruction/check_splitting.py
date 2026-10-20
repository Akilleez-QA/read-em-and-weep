import sympy as s

def require(condition):
    if not condition:
        raise RuntimeError("Universal scalar polynomial identity failed")

u,v,w,U,V,W = s.symbols('u v w U V W')
a,b,c,d,e=u*U,u*V+v*U,u*W+v*V+w*U,v*W+w*V,w*W
I=c*c-3*b*d+12*a*e
J=72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c**3
z=v*V-2*(u*W+w*U)
require(s.expand(z**3-3*I*z-J)==0)
x=s.symbols('x1:5')
x1,x2,x3,x4=x
ss=[(x1+x2)*(x3+x4)-2*(x1*x2+x3*x4),(x1+x3)*(x2+x4)-2*(x1*x3+x2*x4),(x1+x4)*(x2+x3)-2*(x1*x4+x2*x3)]
require(s.expand(sum(ss))==0)
vand=s.prod((ss[i]-ss[j])**2 for i in range(3) for j in range(i+1,3))
rootdisc=s.prod((x[i]-x[j])**2 for i in range(4) for j in range(i+1,4))
require(s.expand(vand-729*rootdisc)==0)
a,b,c,d,e=s.symbols('a b c d e')
I=c*c-3*b*d+12*a*e
J=72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c**3
t=s.symbols('t')
quartic=a*t**4+b*t**3+c*t**2+d*t+e
require(s.expand(4*I**3-J**2-27*s.discriminant(quartic,t))==0)
require(s.Poly(4*I**3-J**2,a,b,c,d,e).coeff_monomial(a**3*e**3)==6912)
h,k,z=s.symbols('I J z')
f=z**3-3*h*z-k
tau=z*z-2*h
require(s.rem(z*tau-h*z-k,f,z)==0)
require(s.rem(tau*tau-(2*h*h+k*z-h*tau),f,z)==0)
print('PASS: six-variable factorization cubic, root-weight sum, Vandermonde, quartic discriminant identity, nonzero universal coefficient, and two multiplication identities; exact symbolic scalar polynomials only.')
