"""Exact universal G-symbols only. No actual HM coefficients or ranks."""
import sympy as s
from itertools import combinations
from pathlib import Path
import runpy
r=s.sqrt(5); I=s.I; R=s.Rational
P6=s.Matrix([[r,0,1,0,-r/3,0,5],[0,r/3,0,-1,0,-r,0],[0,-r,0,-1,0,r/3,0],[5,0,-r/3,0,1,0,r]])
P8=s.Matrix([[0,7*r/40,0,R(1,8),0,-r/40,0,R(1,8),0],[-1,0,r/20,0,-R(1,10),0,-r/20,0,0],[0,0,r/20,0,R(1,10),0,-r/20,0,1],[0,-R(1,8),0,r/40,0,-R(1,8),0,-7*r/40,0]])
x,y=s.symbols('x y')
def cv(f,n):
 f=s.Poly(s.expand(f),x,y)
 return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def sm(m,n):
 a,b,c,d=list(m)
 return s.Matrix.hstack(*[cv((a*x+c*y)**(n-j)*(b*x+d*y)**j,n) for j in range(n+1)])
ph=(1+r)/2
for aa,bb,cc,dd in [(0,1,0,0),(0,0,1,0),(R(1,2),)*4,(ph/2,R(1,2),(ph-1)/2,0)]:
 m=s.Matrix([[aa+I*bb,cc+I*dd],[-cc+I*dd,aa-I*bb]])
 P=s.kronecker_product(m,m.subs(r,-r))
 for n,C in [(6,P6),(8,P8)]:
  assert (C*sm(m,n)-P*C).applyfunc(s.simplify)==s.zeros(4,n+1)
p,q,t,u,v,w=s.symbols('p q t u v w'); a=p*x*x+q*x*y+t*y*y
BA=s.Matrix.hstack(*[P6*cv(a*a*h,6) for h in [x*x,x*y,y*y]])
B0=s.Matrix.hstack(*[P8*cv(a*a*x**(4-i)*y**i,8) for i in range(5)])
B1=s.Matrix.hstack(*[P6*cv(s.diff(a*a,x)*s.diff(h,y)-s.diff(a*a,y)*s.diff(h,x),6) for h in [x**(4-i)*y**i for i in range(5)]])
D=v*B0+w*B1; Dex=D.subs({v:-R(160,3),w:1})
assert all(s.expand(Dex[:,c].det(method='berkowitz'))==0 for c in combinations(range(5),4))
sub={p:1,q:1,t:1}; As=BA.subs(sub); Es=Dex.subs(sub)
assert As.rank()==3 and Es.rank()==3 and As.row_join(Es).rank()==4
mins=[s.Poly(s.expand(D.subs(sub)[:,c].det(method='berkowitz')),v,w,extension=r) for sub in [{p:1,q:1,t:1},{p:1,q:2,t:3}] for c in combinations(range(5),4)]
g=mins[0]
for f in mins[1:]:g=s.gcd(g,f)
assert s.simplify(g.monic().as_expr()-(v+R(160,3)*w))==0
# Universal character count; symmetric cube of A uses Sym^6 W + Sym^2 W.
z=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
inn,vm,va=z['inner'],z['vmul'],z['vadd']; A,Dc,P=z['A'],z['D'],z['P']
assert inn(vm(va(z['one'],Dc),A),P)==z['z'](1)
assert inn(vm(va(z['one'],Dc),Dc),P)==z['z'](2)
six=[z['sym'](6,x) for x in z['W']]
assert inn(va(six,A),P)==z['z'](1)
print('PASS: three universal second-order channels; A-input cyclic symmetry; generic ranks 0/3/4 classified exactly, with exceptional D-channel 3v+160w=0. No actual coefficient or rank evaluated.')

# The surviving channel has a finite length-24 degeneracy scheme.
ams=[s.Poly(s.expand(BA[list(c),:].det(method="berkowitz")),p,q,t,extension=r) for c in combinations(range(4),3)]
ag=ams[0]
for f in ams[1:]:ag=s.gcd(ag,f)
assert ag.total_degree()==0
# Hilbert--Burch: 0 O(-8)^3 -> O(-6)^4 -> I_D -> 0.
z=s.symbols("z")
num=1-4*z**6+3*z**8
assert s.diff(num,z,2).subs(z,1)/2==24
print("PASS: unique A-symbol degeneracy is a finite length-24 scheme; coefficient-free Wronskian proof excludes every square direction.")
