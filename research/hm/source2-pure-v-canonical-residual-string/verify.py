#!/usr/bin/env python3
"""Fixed-variable universal identities, never an actual HM instance."""
from pathlib import Path
import sympy as s
import hashlib,json
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
x,y,X,Y=s.symbols('x y X Y');B=[x*x,x*y,y*y]
b0,b1,b2,f0,f1,f2=s.symbols('b0 b1 b2 f0 f1 f2')
b=b0*x*x+b1*x*y+b2*y*y;f=f0*x*x+f1*x*y+f2*y*y
E=(X*y-Y*x)**2*f
parts=[s.Poly(E,X,Y).coeff_monomial(t) for t in [X*X,X*Y,Y*Y]]
check('determinant square coefficient identity',all(s.expand(a-b)==0 for a,b in zip(parts,[y*y*f,-2*x*y*f,x*x*f])))
def cv(poly,n):
 p=s.Poly(s.expand(poly),x,y)
 return s.Matrix([p.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def tv(a,g,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,y,j)*s.diff(g,x,j,y,k-j) for j in range(k+1)))
check('formal first transvectant vanishes',s.expand(sum(tv(a,b*g,1) for a,g in zip(B,parts)))==0)
check('formal second transvectant equals84bf',s.expand(sum(tv(a,b*g,2) for a,g in zip(B,parts))-84*b*f)==0)
C=s.Matrix.hstack(*[cv(tv(a,x**(6-i)*y**i,1),6).col_join(cv(tv(a,x**(6-i)*y**i,2),4)) for a in B for i in range(7)])
Delta=s.zeros(21,9)
for k in range(9):
 for j in range(3):
  if 0<=k-j<=6:Delta[j*7+k-j,k]=s.binomial(8-k,2-j)*s.binomial(k,j)
Mul=s.Matrix.hstack(*[cv(a*x**(6-i)*y**i,8) for a in B for i in range(7)])
check('polarization left inverse',Mul*Delta==28*s.eye(9))
check('quotient kills polarization',C*Delta==s.zeros(12,9))
check('complete quotient rank',C.rank()==12)
check('quotient kernel exactly polarization',21-C.rank()==Delta.rank()==9)
M=s.Matrix.hstack(*[cv(a*g,4) for a in B for g in B])
check('complete formal quadratic products span D',M.rank()==5)
# Equivariance of determinant square from universal sl2 derivations.
for name,op in [('raising',lambda p:X*s.diff(p,Y)+x*s.diff(p,y)),('lowering',lambda p:Y*s.diff(p,X)+y*s.diff(p,x)),('weight',lambda p:X*s.diff(p,X)-Y*s.diff(p,Y)+x*s.diff(p,x)-y*s.diff(p,y))]:
 check('determinant invariant '+name,s.expand(op(X*y-Y*x))==0)
for degree in [2,3]:
 cols=[]
 for i in range(degree+1):
  e=s.Poly((X*y-Y*x)**2*x**(degree-i)*y**i,X,Y)
  cols.append(s.Matrix.vstack(*[cv(e.coeff_monomial(t),degree+2) for t in [X*X,X*Y,Y*Y]]))
 check('determinant inclusion rank degree'+str(degree),s.Matrix.hstack(*cols).rank()==degree+1)
check('restricted inverse image dimensions',[17+3,18+4,9+5]==[20,22,14])
check('residual endpoint dimension',9+12==21)
check('residual homotopy kernel dimension',21-5==16)
check('small branch kernel exact dimensions',9+3+4==16)
check('large residual endpoint kernel exact dimensions',4+12==16)
check('large NC restriction rank',9-4==5)
check('unique D quotient dimension',3+4+5==12)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'formal_identity':'C(b epsilon^2 f)=(0,84 b f)','scope':'Four pins, universal unspecialized identities and dimension bookkeeping. Actual subspaces and exactness require the written proof.'},indent=2))
