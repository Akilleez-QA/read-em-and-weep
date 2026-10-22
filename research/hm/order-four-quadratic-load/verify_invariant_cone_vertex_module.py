import sympy as s
r=s.sqrt(5); I=s.I; half=s.Rational(1,2);ph=(1+r)/2
U=s.Matrix([[0,1,0,-1,0,-r,0,-r,0],[-r,0,-1,0,1,0,-3,0,r],[-r,0,3,0,-1,0,1,0,r],[0,r,0,r,0,1,0,-1,0]])
def w(q):
 a,b,c,d=q;return s.Matrix([[a+I*b,c+I*d],[-c+I*d,a-I*b]])
def sy(m):
 a,b,c,d=list(m);return s.Matrix([[a*a,a*b,b*b],[2*a*c,a*d+b*c,2*b*d],[c*c,c*d,d*d]])
for q in [(0,1,0,0),(0,0,1,0),(half,half,half,half),(ph/2,half,(ph-1)/2,0)]:
 m=w(q);mp=m.subs(r,-r)
 err=(U*s.kronecker_product(sy(mp),sy(m))-s.kronecker_product(mp,m)*U).applyfunc(s.simplify)
 assert err==s.zeros(4,9)
# The first three matrices generate binary tetrahedral order24; the fourth
# has order10. Inside the binary icosahedral group of order120 they generate it.
x,y=s.symbols('x y')
J=s.Matrix([[0,1],[-1,0]])
Q=s.Matrix([[0,0,1],[0,-s.Rational(1,2),0],[1,0,0]])
Us=[s.Matrix([[x*U[0,3*i+j]+y*U[1,3*i+j] for j in range(3)],
              [x*U[2,3*i+j]+y*U[3,3*i+j] for j in range(3)]]) for i in range(3)]
Vs=[Q.inv()*u.T*J for u in Us]
zero=lambda m:m.applyfunc(s.simplify)==s.zeros(*m.shape)
for i in range(3):
 for j in range(i): assert zero(Us[i]*Vs[j]-Us[j]*Vs[i])
assert not zero(Vs[1]*Us[0]-Vs[0]*Us[1])
assert s.expand((Vs[1]*Us[0]-Vs[0]*Us[1])[0,0])==2*x*x+2*r*y*y
assert zero((Us[0]*Vs[2]+Us[2]*Vs[0])/2-Us[1]*Vs[1])
coneA=((Vs[0]*Us[2]+Vs[2]*Us[0])/2-Vs[1]*Us[1]).applyfunc(s.simplify)
assert coneA==s.Matrix([[8*x*y,4*y*y,0],[-8*x*x,0,8*y*y],[0,-4*x*x,-8*x*y]])
# With a=e1 and b=e2*, order the multiplicity pieces as A,B1,B2.
Xs=[]
for uu,vv in zip(Us,Vs):
 X=s.zeros(7);X[3:5,0:3]=uu;X[0:3,5:7]=vv;Xs.append(X)
for X in Xs:
 for Y in Xs:
  assert zero(X*Y-Y*X)
  for Z in Xs: assert zero(X*Y*Z)
assert zero(Xs[0]*Xs[2]-Xs[1]*Xs[1])
assert not zero(Xs[0]*Xs[0])
print('PASS: exact universal intertwiners; relations iff b(a)=0; normalized nonzero pair has cube-zero and nonzero square action. No actual HM coefficient/rank was evaluated.')
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
vm,inn=q['vmul'],q['inner']; A,V,W,Wp=[q[n] for n in ('A','V','W','Wp')]
assert inn(vm(V,A),vm(Wp,W))==q['z'](1)
assert inn(vm(V,Wp),vm(A,W))==q['z'](1)
assert inn(vm(V,A),vm(A,W))==q['z'](0)
assert inn(vm(V,Wp),vm(Wp,W))==q['z'](0)
print('PASS: exactly two off-diagonal channels and no diagonal channels.')
