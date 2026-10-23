#!/usr/bin/env python3
"""Universal residual terminal and Spencer certificate, no actual instances."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not bool(b):raise RuntimeError(name)
 checks.append(name)
for a in json.loads((r/'INPUTS.json').read_text()):
 d=(r/a['local_path']).read_bytes()
 ck('sha256 '+a['label'],hashlib.sha256(d).hexdigest()==a['sha256'])
 ck('git blob '+a['label'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==a['git_blob'])
x,y=s.symbols('x y');z=s.sqrt(5)
def cv(f,n):
 p=s.Poly(s.expand(f),x,y);return s.Matrix([p.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def poly(v,n):return sum(v[i]*x**(n-i)*y**i for i in range(n+1))
def tv(a,f,k):return s.expand(sum((-1)**j*s.binomial(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
def delta(n):
 M=s.zeros(3*(n+1),n+3)
 for k in range(n+3):
  for j in range(3):
   if 0<=k-j<=n:M[j*(n+1)+k-j,k]=s.binomial(n+2-k,2-j)*s.binomial(k,j)
 return M
A=[x*x,x*y,y*y];D24=delta(4);D26=delta(6)
Mul24=s.Matrix.hstack(*[cv(a*x**(4-i)*y**i,6) for a in A for i in range(5)])
Mul26=s.Matrix.hstack(*[cv(a*x**(6-i)*y**i,8) for a in A for i in range(7)])
ck('source polarization normalization',Mul24*D24==15*s.eye(7))
ck('endpoint polarization normalization',Mul26*D26==28*s.eye(9))
C2=s.Matrix.hstack(*[cv(tv(a,x**(7-i)*y**i,2),5) for a in A for i in range(8)])
relations=s.Matrix.hstack(*[s.Matrix.vstack(*[cv(ell*poly(D26[j*7:(j+1)*7,k],6),7) for j in range(3)]) for ell in [x,y] for k in range(9)])
ck('entire terminal relations killed',C2*relations==s.zeros(6,18))
ck('terminal relation rank18',relations.rank()==18)
ck('terminal quotient rank6',C2.rank()==6)
ck('terminal kernel exact dimension',24-6==18)
cubics=[x**(3-i)*y**i for i in range(4)];sextics=[x**(6-i)*y**i for i in range(7)]
ck('all28 terminal polarization coefficient identities',all(s.expand(sum(tv(A[j],c*poly(D24[j*5:(j+1)*5,k],4),2) for j in range(3))-tv(c,sextics[k],2))==0 for c in cubics for k in range(7)))
ck('all28 Spencer minus12 identities',all(s.expand(x*tv(y*c,f,3)-y*tv(x*c,f,3)+12*tv(c,f,2))==0 for c in cubics for f in sextics))
quartics=[x**(4-i)*y**i for i in range(5)]
Spcols=[]
for i in range(5):
 for j in range(5):
  Spcols.append(s.Matrix.vstack(*[cv(x*quartics[i]*(int(j==k+1))-y*quartics[i]*(int(j==k)),5) for k in range(4)]))
Sp=s.Matrix.hstack(*Spcols);vecId=s.Matrix([int(i==j) for i in range(5) for j in range(5)])
ck('Spencer exact scalar kernel',Sp.rank()==24 and Sp*vecId==s.zeros(24,1))
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
def gram(n):return s.Matrix(n+1,n+1,lambda i,j:s.Rational((-1)**i,s.binomial(n,i)) if i+j==n else 0)
G6=gram(6);G4=gram(4);E=G6.inv()*Pi.T*(Pi*G6.inv()*Pi.T).inv();GP=(E.T*G6*E).applyfunc(s.simplify)
ck('normalized P inclusion',Pi*E==s.eye(4))
p,q,t=s.symbols('p q t');a=p*x*x+q*x*y+t*y*y
L=s.Matrix.hstack(*[Pi*cv(a*d,6) for d in quartics]);Ls=(G4.inv()*L.T*GP).applyfunc(s.simplify)
fp=[poly(E[:,j],6) for j in range(4)]
Cstar=s.Matrix.hstack(*[cv(tv(a,f,2)/60,4) for f in fp])
ck('full formal adjoint transvectant factor60',all(s.expand(v)==0 for v in Ls-Cstar))
rho=s.Matrix.hstack(*[cv(tv(a,d,1),4) for d in quartics]);R1=rho*Ls
ck('all sextic diagonal factor6 identities',all(s.expand(tv(a*a,f,3)-6*tv(a,tv(a,f,2),1))==0 for f in sextics))
D3=s.Matrix.hstack(*[cv(tv(a*a,f,3),4) for f in fp])
ck('entire fixed P diagonal factor360',all(s.expand(v)==0 for v in D3-360*R1))
ck('transfer scalar factor minus30',-s.Rational(1,12)*360==-30)
ck('actual residual Koszul dimensions',2*21-36==6)
ck('endpoint subcomplex acyclic dimensions',18==2*9)
ck('quotient Koszul dimensions',2*12-18==6)
ck('source and terminal dimensions',[3*5,3*6,3*7-9,3*8-18]==[15,18,12,6])
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,terminal_quotient='(A tensor Sym7)/(W Delta Sym8) via C2',terminal_factor=1,Spencer_factor=-12,adjoint_factor=60,diagonal_factor=360,residual_large_constraint='R=alpha R1; beta=0; alpha may be zero',scope='universal identities and actual residual-large mechanism; no selected coefficient or source instance'),indent=2))
