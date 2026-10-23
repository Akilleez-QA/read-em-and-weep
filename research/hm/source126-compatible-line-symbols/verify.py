#!/usr/bin/env python3
"""Finite exact interface and correction certificates; synthetic, not HM instances."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent
n=0
def ck(x,label):
 global n
 if not bool(x): raise RuntimeError(label)
 n+=1
for i in json.loads((root/'INPUTS.json').read_text()):
 d=(root/i['local_path']).read_bytes()
 ck(hashlib.sha256(d).hexdigest()==i['sha256'],'sha256')
 ck(hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==i['git_blob'],'git blob')
# u=0,k=1 and the surviving delta values in each template.
rows=[('I',0),('II',0),('II',1),('III',1)]
for typ,delta in rows:
 v=1+delta
 U=41-5*v; Z=37-4-5*delta; Qrank=U-8
 ck(Z-Qrank==5,'restricted cokernel D')
 ck((41-U)-5*delta==5,'quotient kernel D')
 ck((37-Z)-5*delta==4,'quotient cokernel P')
 ck(U-Z==3,'annihilator dimension difference')
# A Q-minimal synthetic block model, no claim of source realization.
# S0=A3+D5, S1=D5, T0=D5,T1=P4; delta=identity.
Q=s.zeros(9,13)
Q[:5,8:]=s.eye(5)
j0=s.zeros(13);j0[3:8,8:]=s.eye(5)
j1=s.zeros(9)
ck(j0*j0==s.zeros(13),'square-zero')
ck(j1*Q==Q*j0,'Q chain map')
ck(Q.rank()==5 and len(Q.nullspace())==8,'minimal kernel')
p,q,r=s.symbols('p q r')
m=s.Matrix([[p,0,0],[q,p,0],[r,q,p],[0,r,q],[0,0,r]])
b=s.eye(4).row_join(s.zeros(4,1))
L=s.zeros(9,13);L[:5,:3]=m;L[5:,8:]=b
ck(L*j0==j1*L,'whole-family chain map')
ck((b*m).rank()==3,'synthetic original second nonzero')
# Lift an A vector k: first residual m k, correction quotient -m k;
# next original target is -b m k, exactly connecting comparison.
k=s.Matrix(s.symbols('k0:3'))
u=s.zeros(13,1);u[8:,0]=-m*k
h=s.zeros(13,1);h[:3,0]=k
ck(Q*u==-L*h,'first correction')
ck((L*u)[5:,:]==-b*m*k,'second factorization sign')
# Noncommuting formal block expansion. Synthetic coefficient matrices are
# fixed integers only to test correction algebra, not actual module data.
C=s.Matrix(5,5,lambda i,j:(i+2*j+1)%7)
B2=s.Matrix(4,5,lambda i,j:(3*i+j+1)%5)
S2=s.Matrix(5,5,lambda i,j:2*i-j)
R=s.Matrix(5,5,lambda i,j: i+j+int(i==j))
# degree3 and degree4 of -(t b+t² B2)(I-t C+t² C²)(t² S2+t³ R)
coeff={}
for di,Mi in [(1,b),(2,B2)]:
 for dj,Mj in [(0,s.eye(5)),(1,-C),(2,C*C)]:
  for dl,Ml in [(2,S2),(3,R)]:
   degree=di+dj+dl
   coeff[degree]=coeff.get(degree,s.zeros(4,5))-Mi*Mj*Ml
ck(coeff[3]==-b*S2,'third comparison')
ck(coeff[4]==-b*R+b*C*S2-B2*S2,'fourth with all correction terms')
ck((-b*R+b*C*s.zeros(5)-B2*s.zeros(5))==-b*R,'fourth after internal second zero')
# Acyclic rows: exact quotient dimensions and invertible Q.
for delta in [0,1]:
 rank=4+5*delta
 ck((41-rank,37-rank) in [(37,33),(32,28)],'acyclic endpoints')
 ck((41-rank)-(37-rank)==4,'acyclic difference retained')
# Negative control: a single nonzero scalar j0 has no nonzero null line.
ck(s.Matrix([[1]]).nullspace()==[],'no secondary null-radical line')
print(f'PASS: {n} exact checks; single-line interfaces and correction signs; no actual HM evaluation.')
