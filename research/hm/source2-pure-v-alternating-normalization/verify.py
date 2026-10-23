#!/usr/bin/env python3
"""Formal universal identities only; no actual source instances."""
import hashlib,json
from pathlib import Path
from math import comb
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,condition):
 if not bool(condition): raise RuntimeError(label)
 checks.append(label)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(data).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
x,y=s.symbols('x y');p,q,t,u,v,w=s.symbols('p q t u v w');cs=s.symbols('c0:7')
a=p*x*x+q*x*y+t*y*y;b=u*x*x+v*x*y+w*y*y
f=sum(cs[i]*x**(6-i)*y**i for i in range(7))
def tr(a,f,k):
 return s.expand(sum((-1)**i*comb(k,i)*s.diff(a,x,k-i,y,i)*s.diff(f,x,i,y,k-i) for i in range(k+1)))
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def zero(M):return all(s.expand(e)==0 for e in M)
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
def mult(a):return s.Matrix.hstack(*[cv(a*x**(4-i)*y**i,6) for i in range(5)])
def rho(a):return s.Matrix.hstack(*[cv(tr(a,x**(4-i)*y**i,1),4) for i in range(5)])
def trans(a):return s.Matrix.hstack(*[cv(tr(a,x**(6-i)*y**i,2),4) for i in range(7)])
br=tr(a,b,1)
check('formal bracket coefficients',s.expand(br-((2*p*v-2*q*u)*x*x+4*(p*w-t*u)*x*y+(2*q*w-2*t*v)*y*y))==0)
check('full formal sextic alternating identity',s.expand(tr(a,tr(b,f,2),1)-tr(b,tr(a,f,2),1)+2*tr(br,f,2))==0)
G4=gram(4);G6=gram(6)
check('apolar multiplication adjoint is transvectant over60',zero(60*G4.inv()*mult(a).T*G6-trans(a)))
z=s.sqrt(5)
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
K=s.simplify(Pi*G6.inv()*Pi.T)
check('quotient pairing is nondegenerate',K.det()!=0)
E=s.simplify(G6.inv()*Pi.T*K.inv());GP=s.simplify(E.T*G6*E)
check('orthogonal inclusion splits projection',zero(Pi*E-s.eye(4)))
check('inclusion and quotient pairing normalization',zero(G6*E-Pi.T*GP))
def adj(a):return s.simplify(G4.inv()*(Pi*mult(a)).T*GP)
La=adj(a);Lb=adj(b);Lc=adj(br)
check('pinned P adjoint transvectant normalization',zero(60*La-trans(a)*E))
B=rho(a)*Lb;Bs=rho(b)*La
check('exact pinned alternating difference coefficient minus2',zero(B-Bs+2*Lc))
check('alternating half coefficient minus1',zero((B-Bs)/2+Lc))
check('symmetric channel formula',zero((B+Bs)/2-(B+Lc)))
check('pinned alternating channel nonzero polynomial',not zero(Lc))
R=rho(a)*La
check('bilinear diagonal equals R1',zero(B.subs({u:p,v:q,w:t},simultaneous=True)-R))
check('R1 nonzero polynomial',not zero(R))
check('alternating channel diagonal zero',zero(Lc.subs({u:p,v:q,w:t},simultaneous=True)))
# Recover full B from its diagonal by its symmetric polarization and bracket.
Rapb=rho(a+b)*adj(a+b);Rb=rho(b)*Lb
check('full B recovery from diagonal and bracket',zero(B-(Rapb-R-Rb)/2+Lc))
gamma=s.symbols('gamma')
check('same scalar in diagonal and alternating channel',zero(gamma*(B-Bs)+2*gamma*Lc))
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'identity':'rho_D(a)L_b* - rho_D(b)L_a* = -2 L_[a,b]*','adjoint_factor':'1/60 for unnormalized second transvectant','boundary':'All quadratic and sextic coefficients formal; endpoint-nine interpretation conditional on canonical-transfer theorem.'},indent=2))
