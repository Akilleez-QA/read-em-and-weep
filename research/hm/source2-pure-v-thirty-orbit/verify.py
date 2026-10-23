#!/usr/bin/env python3
"""Whole-orbit symbolic ideal-power and conic-divisibility certificate."""
from model import *
from pathlib import Path
from itertools import permutations,combinations_with_replacement
import hashlib,json
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
for item in json.loads((root/'INPUTS.json').read_text()):
 data=(root/item['local_path']).read_bytes()
 ck('sha256 '+item['local_path'],hashlib.sha256(data).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
def detpoly(mat):
 out=s.Poly(0,p,q,t,extension=z)
 for perm in permutations(range(mat.rows)):
  term=s.Poly((-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows)),p,q,t,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],p,q,t,extension=z)
  out+=term
 return out.as_expr()
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*detpoly(B[[j for j in range(4) if j!=i],:]) for i in range(4)]])
ck('determinant cokernel map',all(s.expand(f)==0 for f in N*B))
F1=(N*L*R1).applyfunc(s.expand);F2=(N*L*R2).applyfunc(s.expand)
ck('homogeneous nonic rows',all(s.Poly(f,p,q,t).is_homogeneous and s.Poly(f,p,q,t).total_degree()==9 for F in [F1,F2] for f in F))

U=p*p-s.Rational(2,5)*z*p*t+t*t
V=p*p+s.Rational(2,3)*z*p*t+t*t
f=aa*p**3+z*aa*p*p*t/3-aa*p*t*t+z*aa*t**3/5+2*z*bb*p*p*t/15+2*z*bb*t**3/5
g=aa*p**3-z*aa*p*p*t+5*aa*p*t*t/3+z*aa*t**3+2*bb*p**3+2*bb*p*t*t/3
mirror=(aa*F1+bb*F2).subs(q,0)
expected=s.Matrix([[s.Rational(20,3)*z*U**2*V*f,0,0,s.Rational(20,3)*U**2*V*g]])
ck('whole mirror exact nonic factorization',all(s.expand(v)==0 for v in mirror-expected))
def hgcd(polys):
 out=s.Poly(0,p,t,extension=z)
 for v in polys:out=s.gcd(out,s.Poly(v,p,t,extension=z))
 return out.monic().as_expr()
cP=Pi*cv(a**3,6)
ck('C5 mirror intersection exactly U',s.expand(hgcd([v.subs(q,0) for v in cP])-U)==0)
minors=[detpoly(L[:,[j for j in range(5) if j!=i]]) for i in range(5)]
ck('C3 mirror intersection exactly V',s.expand(hgcd([v.subs(q,0) for v in minors])-V)==0)
res=s.factor(s.resultant(f.subs(t,1),g.subs(t,1),p))
expectedres=-s.Rational(65536,2025)*z*(aa-bb/2)**2*(aa+bb/2)**2*(aa+bb)**2
ck('exact homogeneous binary resultant',s.simplify(res-expectedres)==0)
ck('resultant has homogeneous coefficient degree6',s.Poly(res,aa,bb).is_homogeneous and s.Poly(res,aa,bb).total_degree()==6)
ck('coefficient infinity alpha0 has no zero',s.simplify(res.subs(aa,0)/bb**6)==-s.Rational(4096,2025)*z)
# Boundary common roots would force both coefficient variables to vanish.
ck('direction t0 coefficient equations',s.expand(f.subs(t,0)-aa*p**3)==0 and s.expand(g.subs(t,0)-(aa+2*bb)*p**3)==0)
ck('direction p0 coefficient equations',s.expand(f.subs(p,0)-z*(aa+2*bb)*t**3/5)==0 and s.expand(g.subs(p,0)-z*aa*t**3)==0)
ck('both boundary equation pairs independent',s.Matrix([[1,0],[1,2]]).det()!=0 and s.Matrix([[1,2],[1,0]]).det()!=0)
for label,c,h in [('ell5',2,U),('ell3',-2,V),('rank',-1,p*p-t*t)]:
 ff=s.expand(f.subs(bb,c*aa)/aa);gg=s.expand(g.subs(bb,c*aa)/aa)
 ck(label+' complete homogeneous residual gcd',s.expand(hgcd([ff,gg])-h)==0)
 ck(label+' residual common divisor reduced',s.discriminant(h.subs(t,1),p)!=0)
ck('axis pair factors disjoint',all(s.resultant(h1.subs(t,1),h2.subs(t,1),p)!=0 for h1,h2 in [(U,V),(U,p*p-t*t),(V,p*p-t*t)]))
# Pinned binary group generators, acting on the entire quadratic space.
i=s.I
h1=s.Matrix([[i,0],[0,-i]]);h2=s.Matrix([[0,1],[-1,0]])
def sympower(m,n):
 a0,b0,c0,d0=list(m)
 return s.Matrix.hstack(*[cv((a0*x+c0*y)**(n-j)*(b0*x+d0*y)**j,n) for j in range(n+1)])
A1=sympower(h1,2);A2=sympower(h2,2);A3=A1*A2
ck('pinned first involution minus plane q0',A1==s.diag(-1,1,-1))
ck('pinned second involution plus axis q0 p=t',A2==s.Matrix([[0,0,1],[0,-1,0],[1,0,0]]))
ck('pinned third involution plus axis q0 p=-t',A3==s.Matrix([[0,0,-1],[0,-1,0],[-1,0,0]]))
ck('Klein four relations',A1*A2==A2*A1 and A1**2==s.eye(3) and A2**2==s.eye(3) and A3**2==s.eye(3))
for j,h in enumerate([h1,h2]):
 PP=s.kronecker_product(h,h.subs(z,-z))
 ck('pinned generator quotient intertwining '+str(j),Pi*sympower(h,6)==PP*Pi)
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,resultant=str(expectedres),exceptional_residual_gcds={'[1:2]':str(U),'[1:-2]':str(V),'[1:-1]':'p**2-t**2'},conclusion='No nonzero universal pencil member has a thirty-point base orbit',scope='entire involution mirror and symbolic coefficient pencil; no actual source selected'),indent=2))
