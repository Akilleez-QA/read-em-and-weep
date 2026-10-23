#!/usr/bin/env python3
"""Canonical-transfer types, characters and universal normalization only."""
from pathlib import Path
from math import comb
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(data).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
# Types of restricted maps whose landing spaces are proved in the text.
types={'G':('Z','N2'),'h':('N4','N2'),'Ta':('N2','N4'),'Q':('N2','N4'),'j2':('N2','N2'),'j4':('N4','I4'),'Pi':('Z','imh'),'Tbh':('imh','Z'),'s':('I4','imh'),'hr':('N4','imh'),'Qh':('imh','I4'),'B':('I4','I2'),'hZ':('Z','I2'),'L':('I2','I4')}
def typ(word):
 for a,b in zip(word,word[1:]):
  if types[a][0]!=types[b][1]:raise RuntimeError('ill typed '+str(word))
 return types[word[-1]][0],types[word[0]][1]
for name,word,expected in [('transfer',('h','Ta','G'),('Z','N2')),('Q transfer',('Qh','Pi'),('Z','I4')),('L h restriction',('L','hZ'),('Z','I4')),('bilinear family',('Pi','Tbh','s'),('I4','imh')),('mixed left',('Pi','Tbh','hr'),('N4','imh')),('mixed right',('B','j4'),('N4','I2'))]:
 check(name+' type',typ(word)==expected)
# The two correction minus signs multiply to plus, followed by j2 G=h.
J,H,T,G,S=s.symbols('J H T G S',commutative=False)
x1=-G*T*S;x2=s.expand(-G*T*x1)
check('two exact correction signs',x2==G*T*G*T*S)
check('lift substitution j2G=h has plus sign',s.expand(J*x2).subs(J*G,H)==H*T*G*T*S)
# Exact A5 character table for the even representations.
z=s.sqrt(5);phi=(1+z)/2;phibar=(1-z)/2
one=s.Matrix([1,1,1,1,1]);A=s.Matrix([3,-1,0,phi,phibar]);V=s.Matrix([3,-1,0,phibar,phi]);P=s.Matrix([4,0,1,-1,-1]);D=s.Matrix([5,1,-1,0,0]);sizes=[1,15,20,12,12];square=[0,0,2,4,3]
def prod(a,b):return s.Matrix([s.expand(x*y) for x,y in zip(a,b)])
def inner(a,b):return s.simplify(sum(w*x*y for w,x,y in zip(sizes,a,b))/60)
Sym=s.Matrix([s.simplify((A[i]**2+A[square[i]])/2) for i in range(5)])
Alt=s.Matrix([s.simplify((A[i]**2-A[square[i]])/2) for i in range(5)])
check('Sym2 A decomposition',Sym==one+D)
check('Lambda2 A decomposition',Alt==A)
check('symmetric transfer multiplicity2',inner(prod(Sym,P),D)==2)
check('alternating transfer multiplicity1',inner(prod(Alt,P),D)==1)
check('A tensor D to D unique',inner(prod(A,D),D)==1)
check('A tensor P to D unique',inner(prod(A,P),D)==1)
check('no A in actual imQ',inner(2*V+3*P+3*D,A)==0)
check('no P to actual kernelQ',inner(P,A+D)==0)
check('transfer quotient dimension29',(2*V+2*P+3*D)[0]==29)
# Pinned universal bilinear adjoints, not actual HM matrices.
x,y,p,q,t,u,v,w=s.symbols('x y p q t u v w')
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,comb(n,i)) if i+j==n else 0)
def zero(M):return all(s.expand(e)==0 for e in M)
G6=gram(6);GD=gram(4);E=G6.inv()*Pi.T*(Pi*G6.inv()*Pi.T).inv();GP=s.simplify(E.T*G6*E)
a=p*x*x+q*x*y+t*y*y;b=u*x*x+v*x*y+w*y*y
L=s.Matrix.hstack(*[Pi*cv(a*x**(4-i)*y**i,6) for i in range(5)])
Ls=s.simplify(GD.inv()*L.T*GP)
def rho(f,n):return s.Matrix.hstack(*[cv(s.diff(f,x)*s.diff(x**(n-i)*y**i,y)-s.diff(f,y)*s.diff(x**(n-i)*y**i,x),n) for i in range(n+1)])
rhoa=rho(a,4);rhob=rho(b,4);Lsb=Ls.subs({p:u,q:v,t:w},simultaneous=True)
B=rhoa*Lsb;Bswap=rhob*Ls;R1=rhoa*Ls;R2=Ls*Pi*rho(a,6)*E
check('universal adjoint convention',zero(GD*Ls-L.T*GP))
check('bilinear diagonal is R1 in correct order',zero(B.subs({u:p,v:q,w:t},simultaneous=True)-R1))
check('symmetric part retains R1 diagonal',zero(((B+Bswap)/2).subs({u:p,v:q,w:t},simultaneous=True)-R1))
check('alternating part has zero diagonal',zero((B-Bswap).subs({u:p,v:q,w:t},simultaneous=True)))
# Check independence using full polynomial coefficients, never point evaluation.
mons=[p*p,p*q,p*t,q*q,q*t,t*t]
coeff=s.Matrix([[s.Poly(s.expand(M[i,j]),p,q,t).coeff_monomial(mon) for M in [R1,R2]] for i in range(5) for j in range(4) for mon in mons])
check('pinned R1 R2 remain independent',coeff.rank()==2)
check('universal rho channel is nonzero',not zero(rhoa))
check('universal adjoint channel is nonzero',not zero(Ls))
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'new_constraint':'dim F4=9 implies R=gamma R1, gamma unselected and possibly zero','boundary':'Actual map identities require the pinned proofs; no source-instance evaluation.'},indent=2))
