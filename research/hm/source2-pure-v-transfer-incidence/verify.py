#!/usr/bin/env python3
"""Universal symbolic D-channel incidence certificate; no HM instance."""
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
x,y,X,Y=s.symbols('x y X Y');p,q,t=s.symbols('p q t');fs=s.symbols('f0:5')
a=p*x*x+q*x*y+t*y*y;f=sum(fs[i]*x**(4-i)*y**i for i in range(5))
def inc(f):return s.expand((X*y-Y*x)*(X*s.diff(f,x)+Y*s.diff(f,y)))
e=inc(f);B=[x*x,x*y,y*y];C=[X*X,X*Y,Y*Y]
parts=[s.Poly(e,X,Y).coeff_monomial(c) for c in C]
check('complete biform coefficient formula',all(s.expand(a-b)==0 for a,b in zip(parts,[y*s.diff(f,x),y*s.diff(f,y)-x*s.diff(f,x),-x*s.diff(f,y)])))
def tv(g,u,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(g,x,k-j,y,j)*s.diff(u,x,j,y,k-j) for j in range(k+1)))
rho=s.diff(a,x)*s.diff(f,y)-s.diff(a,y)*s.diff(f,x)
check('all formal coefficients exact minus14 identity',s.expand(sum(tv(g,a*u,2) for g,u in zip(B,parts))+14*rho)==0)
check('rho family nonzero as polynomial',s.Poly(rho,p,q,t,*fs,x,y).as_expr()!=0)
# Exact sl2 equivariance of inclusion, on the full formal quartic.
for name,source,target in [
 ('raising',lambda f:x*s.diff(f,y),lambda e:x*s.diff(e,y)+X*s.diff(e,Y)),
 ('lowering',lambda f:y*s.diff(f,x),lambda e:y*s.diff(e,x)+Y*s.diff(e,X)),
 ('weight',lambda f:x*s.diff(f,x)-y*s.diff(f,y),lambda e:x*s.diff(e,x)-y*s.diff(e,y)+X*s.diff(e,X)-Y*s.diff(e,Y))]:
 check('D inclusion equivariance '+name,s.expand(target(e)-inc(source(f)))==0)
def cv(poly,n):
 poly=s.Poly(s.expand(poly),x,y);return s.Matrix([poly.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
E=s.Matrix.hstack(*[s.Matrix.vstack(*[cv(s.Poly(inc(x**(4-i)*y**i),X,Y).coeff_monomial(c),4) for c in C]) for i in range(5)])
check('universal D inclusion rank five',E.rank()==5)
Q=s.Matrix.hstack(*[cv(tv(g,x**(6-i)*y**i,1),6).col_join(cv(tv(g,x**(6-i)*y**i,2),4)) for g in B for i in range(7)])
Delta=s.zeros(21,9)
for k in range(9):
 for j in range(3):
  if 0<=k-j<=6:Delta[j*7+k-j,k]=s.binomial(8-k,2-j)*s.binomial(k,j)
Mul=s.Matrix.hstack(*[cv(g*x**(6-i)*y**i,8) for g in B for i in range(7)])
check('polarization injective normalization',Mul*Delta==28*s.eye(9))
check('transvectant quotient kills polarization',Q*Delta==s.zeros(12,9))
check('complete quotient exact dimensions',Q.rank()==12 and Delta.rank()==9)
# Even character table and all multiplicities used by actual-map arguments.
z=s.sqrt(5);phi=(1+z)/2;phibar=(1-z)/2
A=s.Matrix([3,-1,0,phi,phibar]);V=s.Matrix([3,-1,0,phibar,phi]);P=s.Matrix([4,0,1,-1,-1]);D=s.Matrix([5,1,-1,0,0]);sizes=[1,15,20,12,12]
def inner(a,b):return s.simplify(sum(w*x*y for w,x,y in zip(sizes,a,b))/60)
def prod(a,b):return s.Matrix([s.expand(x*y) for x,y in zip(a,b)])
check('unique D in N0 source',inner(P+D,D)==1)
check('no P to radical D',inner(P,D)==0)
check('unique D in N8 source',inner(prod(A,D),D)==1)
check('unique D in N8 endpoint',inner(V+P+D,D)==1)
check('no D in Sym6',inner(V+P,D)==0)
check('no D to A lift ambiguity',inner(D,A)==0)
check('no A in imQ lift ambiguity',inner(2*V+3*P+3*D,A)==0)
check('source repeated D handled',inner(V+P+2*D,D)==2 and inner(A+D,D)==1)
check('NC endpoint multiplicity free',inner(P+D,P)==1 and inner(P+D,D)==1)
check('universal transfer channel unique',inner(prod(A,D),D)==1)
check('intersection dimensions alternatives',[P[0],(P+D)[0]]==[4,9])
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'universal_identity':'C2(a e_D(f))=-14 rho_D(a)f','actual_conditional_conclusion':'endpoint9: gamma=0 iff NC4 subset Q(NC2); otherwise intersection is I4','scope':'No actual coefficient, direction or source instance evaluated.'},indent=2))
