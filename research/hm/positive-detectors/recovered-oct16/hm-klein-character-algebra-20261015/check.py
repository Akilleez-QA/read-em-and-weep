"""Formal low-degree algebra controls only. No geometric source evaluation."""
import sympy as S,itertools,json
from pathlib import Path
s,t,w,h,z=S.symbols('s t w h z')
M=S.Matrix([[0,0,w],[1,0,-t],[0,1,s]])
I=S.eye(3);Z=S.zeros(3)
K=S.Matrix([[s*s-4*t,-3*w,-s*w],[2*s,s*s-t,s*t-3*w],[-3,-s,-t]])
def zero(A):return all(S.expand(v)==0 for v in A)
assert zero(M**3-s*M**2+t*M-w*I)
assert zero(K-((s*s-4*t)*I+2*s*M-3*M**2))
MU=S.diag(M,M);MA=Z.row_join(K).col_join(I.row_join(Z))
assert zero(MA*MU-MU*MA)
assert zero(MA**2-S.diag(K,K))
P=z**3-s*z*z+t*z-w
Q=s*s+2*s*z-3*z*z-4*t
vectors=[]
for j in range(6):
 v=S.zeros(6,1);v[j]=1;vectors.append(v)
for i in range(6):
 for j in range(6):
  product=(MU**(i%3))*(MA if i>=3 else S.eye(6))*vectors[j]
  power=i%3+j%3;odd=(i>=3)+(j>=3)
  rem=S.Poly(S.rem(z**power*(Q if odd==2 else 1),P,z),z)
  expected=S.zeros(6,1)
  for k in range(3):expected[k+(3 if odd==1 else 0)]=rem.nth(k)
  assert zero(product-expected)
# Verify the character and relations in independent homogeneous coordinates.
X=S.symbols('X1:5');Y=S.symbols('Y1:5');v=[S.Integer(0)]*5
for subset in itertools.chain.from_iterable(itertools.combinations(range(4),k) for k in range(5)):
 subset=set(subset);v[len(subset)]+=S.prod(X[i] if i in subset else Y[i] for i in range(4))
u=X[0]*X[1]*Y[2]*Y[3]+Y[0]*Y[1]*X[2]*X[3]
a=(X[0]*Y[1]-X[1]*Y[0])*(X[2]*Y[3]-X[3]*Y[2])
assert S.expand(a*a-(v[2]**2+2*v[2]*u-3*u*u-4*v[1]*v[3]+16*v[0]*v[4]))==0
for perm,sgn in [((1,0,2,3),-1),((0,1,3,2),-1),((2,3,0,1),1)]:
 sub={**{X[i]:X[perm[i]] for i in range(4)},**{Y[i]:Y[perm[i]] for i in range(4)}}
 assert S.expand(u.xreplace(sub)-u)==0
 assert S.expand(a.xreplace(sub)-sgn*a)==0
ell=S.Matrix([[1,s,s*s-t-2*h]])
for k in range(3):
 rem=S.Poly(S.rem((z*z-2*h)*z**k,P,z),z)
 assert S.expand(rem.nth(2)-ell[k])==0
kernel=S.Matrix([-s,1,0]);assert (ell*kernel)[0]==0
assert S.expand((ell*M*kernel)[0]+t+2*h)==0
out={'passed':True,'source_values_evaluated':False,'basis_products_checked':36,'homogeneous_square_relation':True,'character_generator_checks':6,'trace_basis_checks':3,'trace_kernel_not_ideal_control':True,'field':'Q','variable_denominators_introduced':False}
Path(__file__).with_name('receipt.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
