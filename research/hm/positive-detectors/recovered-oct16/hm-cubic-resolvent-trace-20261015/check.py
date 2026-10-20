"""Small universal invariant/trace controls; no source imports or values."""
import itertools, json, math, random
import sympy as s
P=list(itertools.permutations(range(4)))
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
x=s.symbols('x1:5')
e=[s.Integer(1)]+[sum(s.prod(x[i] for i in I) for I in itertools.combinations(range(4),k)) for k in range(1,5)]
u=[x[0]*x[1]+x[2]*x[3],x[0]*x[2]+x[1]*x[3],x[0]*x[3]+x[1]*x[2]]
T=s.Symbol('T')
R=T**3-e[2]*T**2+(e[1]*e[3]-4*e[4])*T-(e[3]**2+e[1]**2*e[4]-4*e[2]*e[4])
assert s.expand(s.prod(T-z for z in u)-R)==0
Delta=s.prod(x[i]-x[j] for i in range(4) for j in range(i+1,4))
a=[(x[0]-x[1])*(x[2]-x[3]),-(x[0]-x[2])*(x[1]-x[3]),(x[0]-x[3])*(x[1]-x[2])]
for i in range(3): assert s.expand(a[i]*s.diff(R,T).subs(T,u[i])-Delta)==0
expected=[s.Integer(4),4*e[2],4*(e[2]**2-e[1]*e[3]+2*e[4])]
for j in range(3):
 f=x[2]**2*x[3]**2*a[0]*u[0]**j
 alt=s.expand(sum(sign(p)*f.xreplace({x[i]:x[p[i]] for i in range(4)}) for p in P))
 assert s.expand(alt-Delta*expected[j])==0

def homogeneous(coords):
 X,Y=zip(*coords)
 v=[sum(math.prod(X[i] if i in I else Y[i] for i in range(4)) for I in itertools.combinations(range(4),k)) for k in range(5)]
 u=X[0]*X[1]*Y[2]*Y[3]+Y[0]*Y[1]*X[2]*X[3]
 bracket=lambda i,j:X[i]*Y[j]-X[j]*Y[i]
 a=bracket(0,1)*bracket(2,3)
 d=math.prod(bracket(i,j) for i in range(4) for j in range(i+1,4))
 q=X[2]**2*X[3]**2*Y[0]**2*Y[1]**2
 return v,u,a,d,q
rng=random.Random(2718)
points=[]
for i in range(24):
 c=[(rng.randint(-3,3),rng.randint(1,3)) for _ in range(4)]
 if i%3==0:c[0]=(1,0)
 if i%3==1:c[1]=c[0]
 points.append(c)
for c in points:
 v,u,a,d,q=homogeneous(c)
 assert u**3-v[2]*u**2+(v[1]*v[3]-4*v[0]*v[4])*u-(v[0]*v[3]**2+v[1]**2*v[4]-4*v[0]*v[2]*v[4])==0
 target=[4,4*v[2],4*(v[2]**2-v[1]*v[3]+2*v[0]*v[4])]
 for j in range(3):
  total=0
  for p in P:
   _,up,ap,_,qp=homogeneous([c[i] for i in p])
   total+=sign(p)*qp*ap*up**j
  assert total==d*target[j]
for r in range(13):
 n=math.comb(r+2,2)
 assert n*(n+1)//2==sum(math.comb(r+4-j,4) if r>=j else 0 for j in range(3))
# Coordinate proof of the global kernel, over formal symmetric variables.
v0,v1,v2,v3,v4=s.symbols('v0:5')
g=v2**2-v1*v3+2*v0*v4
M=s.Matrix([[1,-v2,-g],[0,1,0],[0,0,1]])
assert M.det()==1
assert s.Matrix([[4,4*v2,4*g]])*M==s.Matrix([[4,0,0]])
print(json.dumps({'affine_cubic_identity':True,'affine_trace_basis_identities':3,'pair_derivative_identities':3,'homogeneous_points':len(points),'homogeneous_cubic_controls':len(points),'homogeneous_trace_controls':3*len(points),'dimension_controls':13,'kernel_basis_control':True,'production_values_evaluated':False}))
