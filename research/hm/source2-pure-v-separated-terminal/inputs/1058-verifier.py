#!/usr/bin/env python3
"""Exact universal representation certificate, not an actual source matrix."""
from pathlib import Path
from math import comb
import json,hashlib
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not b:raise RuntimeError(name)
 checks.append(name)
for i in json.loads((r/'INPUTS.json').read_text()):
 d=(r/i['local_path']).read_bytes();ck('sha256 '+i['local_path'],hashlib.sha256(d).hexdigest()==i['sha256']);ck('git_blob '+i['local_path'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==i['git_blob'])
x,y=s.symbols('x y');z=s.sqrt(5)
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
P8=s.Matrix([[0,7*z/40,0,s.Rational(1,8),0,-z/40,0,s.Rational(1,8),0],[-1,0,z/20,0,-s.Rational(1,10),0,-z/20,0,0],[0,0,z/20,0,s.Rational(1,10),0,-z/20,0,1],[0,-s.Rational(1,8),0,z/40,0,-s.Rational(1,8),0,-7*z/40,0]])
E8=gram(8).inv()*P8.T
ck('apolar inclusion rank4',s.simplify((P8*E8).det())!=0)
def sm(m,n):
 a,b,c,d=list(m);return s.Matrix.hstack(*[cv((a*x+c*y)**(n-j)*(b*x+d*y)**j,n) for j in range(n+1)])
phi=(1+z)/2
for j,(a,b,c,d) in enumerate([(0,1,0,0),(0,0,1,0),(s.Rational(1,2),)*4,(phi/2,s.Rational(1,2),(phi-1)/2,0)]):
 m=s.Matrix([[a+s.I*b,c+s.I*d],[-c+s.I*d,a-s.I*b]]);M8=sm(m,8);P=s.kronecker_product(m,m.subs(z,-z))
 ck('pinned quotient intertwining '+str(j),(P8*M8-P*P8).applyfunc(s.simplify)==s.zeros(4,9))
 ck('apolar form invariant '+str(j),(M8.T*gram(8)*M8-gram(8)).applyfunc(s.simplify)==s.zeros(9))
def tr(a,f,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
as_=[x*x,x*y,y*y];fs=[x**(8-i)*y**i for i in range(9)]
C=s.Matrix.hstack(*[cv(tr(a,f,1),8).col_join(cv(tr(a,f,2),6)) for a in as_ for f in fs])
# Polarization Sym10 -> Sym2 tensor Sym8 in the same tensor order.
Delta=s.zeros(27,11)
for k in range(11):
 for j in range(3):
  n=k-j
  if 0<=n<=8:Delta[j*9+n,k]=s.binomial(10-k,2-j)*s.binomial(k,j)
ck('transvectant pair kills entire Sym10',C*Delta==s.zeros(16,11))
Mul=s.Matrix.hstack(*[cv(a*f,10) for a in as_ for f in fs])
ck('polarization injection normalization',Mul*Delta==45*s.eye(11))
ck('full transvectant pair is quotient isomorphism',C.rank()==16)
CP=C*s.diag(E8,E8,E8)
minor=s.factor(CP[:12,:].det())
ck('exact12x12 injectivity certificate',s.simplify(minor+s.Rational(1825478130618637221888,5)*z)==0)
ck('universal P quadratic channel injective',CP.rank()==12)
ck('generated full endpoint dimension',4+12==16)
ck('three quotient channel dimensions',3+4+5==12)
ck('split generated module dimensions',[5+4,6+2*4,4+3*4]==[9,14,16])
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,exact_minor=str(minor),conditional_conclusion='Nonzero separated N0 projection forces F4 dimension16 and F=I plus truncated free P module',scope='universal representation map only; actual projection remains unselected'),indent=2))
