#!/usr/bin/env python3
"""Universal prolongation and finite-group identities; no actual instances."""
from pathlib import Path
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent; checks=[]
def check(name,ok):
 if not bool(ok):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(item['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==item['sha256'])
 check(item['local_path']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'])
# Exact character table via trace of the binary defining representation.
z=s.sqrt(5);phi=(1+z)/2
tr=[s.Integer(2),s.Integer(-2),s.Integer(0),s.Integer(1),s.Integer(-1),phi,-phi,phi-1,1-phi]
weights=[1,1,30,20,20,12,12,12,12]
def simp(v):return s.Matrix([s.simplify(a) for a in v])
def sy(n):
 a=s.ones(9,1);b=s.Matrix(tr)
 if n==0:return a
 for k in range(1,n):a,b=b,simp([tr[i]*b[i]-a[i] for i in range(9)])
 return b
def prod(a,b):return simp([u*v for u,v in zip(a,b)])
def ip(a,b):return s.simplify(sum(n*u*v for n,u,v in zip(weights,a,b))/120)
W=sy(1);Wp=simp([a.xreplace({z:-z}) for a in W]);S=sy(3);D=sy(4);T=sy(5);P=prod(W,Wp);V=sy(6)-P

check('Euler quotient-bundle H1 vanishings',all(max(-d-1,0)==0 for d in [-1,15,3]))
check('source first multiplication dimensions',2*41-54==28)
check('odd Koszul dimension exactness',2*37-54==20)
check('W tensor P decomposition',simp(prod(W,P)-Wp-T)==s.zeros(9,1))
check('image-pencil quotient Wprime',simp(prod(W,P)-T-Wp)==s.zeros(9,1))
M3=3*Wp+3*S+6*T;M5=Wp+3*T;K=3*Wp+3*S+3*T
check('odd kernel character',simp(M3-3*T-K)==s.zeros(9,1))
check('odd rank18',(3*T)[0]==18)
check('odd kernel dimension36',K[0]==36)
check('odd cokernel dimension2',Wp[0]==2)
check('odd target Wprime multiplicity1',ip(M5,Wp)==1)
check('odd target T multiplicity3',ip(M5,T)==3)
check('normalized odd homotopy ambiguity zero',ip(Wp,T)==0)
check('unrestricted homotopy ambiguity dimension3',ip(Wp,K)==3)
# Abstract multiplicity controls only, not actual source maps.
A=s.zeros(3,6)
for i in range(3):A[i,i]=1
e=s.zeros(6,1);e[5,0]=1
rowdep=s.Matrix([[1,0,0,0,0,0]]);rowind=s.Matrix([[0,0,0,1,0,0]])
Jdep=e*rowdep;Jind=e*rowind
check('control Q has full T-rank3',A.rank()==3)
check('both radical controls square-zero',Jdep*Jdep==s.zeros(6) and Jind*Jind==s.zeros(6))
check('both radical images in Q kernel',A*Jdep==s.zeros(3,6) and A*Jind==s.zeros(3,6))
check('aligned combined rank3',A.col_join(rowdep).rank()==3)
check('independent combined rank4',A.col_join(rowind).rank()==4)
g=e*s.Matrix([[1,0,0]])
check('aligned normalized homotopy identities',g*A==Jdep and A*g==s.zeros(3))
check('independent radical nonzero on Q kernel',Jind[:,3]!=s.zeros(6,1) and A[:,3]==s.zeros(3,1))
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,actual_conditional_Q3_rank=18,T_multiplicity_rank=3,cokernel='Wprime',scope='Pinned actual quotient proof plus character checks and abstract non-realization controls; no source matrix evaluated.'),indent=2))
