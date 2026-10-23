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


M3=3*Wp+3*S+6*T;H=3*Wp+3*S+3*T;K=3*Wp+3*S+2*T;F=Wp+2*T
check('odd common kernel quotient T',simp(H-K-T)==s.zeros(9,1))
check('F3 has exactly two T copies',ip(F,T)==2)
check('common kernel T equals F3 T',ip(K,T)==2)
check('no Wprime or S map to marked T',ip(Wp,T)==0 and ip(S,T)==0)
check('W tensor P quotient contains unique T',simp(prod(W,P)-Wp-T)==s.zeros(9,1))
check('full theta rank12',(2*T)[0]==12)
check('full theta kernel dimension42',(M3-2*T)[0]==42)
check('odd theta rank6',T[0]==6)
check('odd operator socle dimension30',K[0]==30)
# Formal quotient computation with independent I2 and I4 coefficients.
ix=s.Matrix(s.symbols('ix0:5'));iy=s.Matrix(s.symbols('iy0:5'))
px=s.Matrix(s.symbols('px0:4'));py=s.Matrix(s.symbols('py0:4'))
hx=ix.col_join(px);hy=iy.col_join(py)
quot=s.zeros(8,18)
for i in range(4):quot[i,5+i]=1;quot[4+i,14+i]=1
check('literal determinant quotient sign',quot*(hy.col_join(-hx))==py.col_join(-px))
# Universal multiplicity normal form, not an actual source matrix.
J=s.zeros(6);Theta=s.zeros(6);J[1,0]=1;Theta[2,0]=1;Theta[1,3]=1
Q=s.zeros(3,6)
for i in range(3):Q[i,i+3]=1
Hinc=s.eye(6)[:,:3];Finc=s.eye(6)[:,1:3];Iinc=s.eye(6)[:,1:2]
q=s.zeros(1,6);q[0,2]=1;jrow=s.zeros(1,6);jrow[0,0]=1
check('full theta multiplicity rank2',Theta.rank()==2)
check('full theta quotient is j row',q*Theta==jrow)
check('all four products vanish',all(A*B==s.zeros(6) for A in [J,Theta] for B in [J,Theta]))
check('full theta image inside Q kernel',Q*Theta==s.zeros(3,6))
check('both operators kill F3 T',J*Finc==s.zeros(6,2) and Theta*Finc==s.zeros(6,2))
check('full theta image equals F3 T',Theta.row_join(Finc).rank()==2)
check('odd theta rank1', (Theta*Hinc).rank()==1)
check('odd image complementary to I3',(Theta*Hinc).row_join(Iinc).rank()==2)
check('odd images span full F3 T',(Theta*Hinc).row_join(J*Hinc).rank()==2)
# On H in basis generator,epsilon,eta these are regular multiplication.
E=J[:3,:3];N=Theta[:3,:3];u=s.Matrix([1,0,0])
check('regular module cyclic basis',s.Matrix.hstack(u,E*u,N*u)==s.eye(3))
a,b,c=s.symbols('a b c')
check('faithful algebra coefficients',(a*s.eye(3)+b*E+c*N).reshape(9,1).jacobian([a,b,c]).rank()==3)
check('linear combinations same kernel when nonzero',(b*E+c*N)==s.Matrix([[0,0,0],[b,0,0],[c,0,0]]))
# Restricted terminal factorization and strict domain boundary.
ell=s.Matrix([[1,0,0]]);Jinc=s.eye(6)[:,1:]
check('old factorization on ker j3',Theta*Jinc==Iinc*ell*Q*Jinc)
check('no extension of old factorization to full M3',Theta!=Iinc*ell*Q)
check('theta kernel contained in ker j3',all(J*v==s.zeros(6,1) for v in Theta.nullspace()))
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,full_theta_rank=12,odd_theta_rank=6,odd_module='T tensor C[epsilon,eta]/(epsilon,eta)^2 plus trivial 3Wprime+3S',boundary='Universal normal form only; actual maps justified by pinned proof.'),indent=2))
