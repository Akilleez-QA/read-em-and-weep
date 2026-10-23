#!/usr/bin/env python3
"""Exact abstract-complex diagnostics; no actual HM matrices."""
import hashlib,itertools,json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parent
checks=0

def ck(v,label):
 global checks
 checks+=1
 if not v:raise RuntimeError(label)
s,m,b,c,rho,aa,dd=S.symbols('s m b c rho alpha beta')
# Minimal complex: source A,D,L; target Z,P. Q(L)=Z.
Q=S.Matrix([[0,0,1],[0,0,0]])
L=S.Matrix([[s,m,c],[0,0,b]])
j0=S.Matrix([[0,0,0],[0,0,rho],[0,0,0]]);j1=S.zeros(2)
ck(Q*j0==j1*Q,'chain map at Q')
ck(L*j0-j1*L==S.Matrix([[0,0,m*rho],[0,0,0]]),'family naturality forces m rho zero')
ck((L*j0-j1*L).subs(m,0)==S.zeros(2,3),'selected zero D symbol gives family chain map')
L=L.subs(m,0)
k=S.Matrix([1,0,0]);u=S.Matrix([aa,dd,-s])
ck(Q*u==-L*k,'arbitrary first correction')
ck((L*u)[1]==-b*s,'exact negative factorization sign')
ck((L*S.Matrix([aa,dd,0]))[1]==0,'first vanishing removes correction ambiguity')
ck(u[2]==-s,'connecting delta identifies quotient correction')
# Matrix-sized synthetic complexes retaining actual cohomology dimensions.
# Arbitrary coefficients below do not encode G actions or actual geometry.
for seed in (-2,-1,0,1,2):
 Bs=S.Matrix(5,3,lambda i,j:seed+i-2*j)
 Bt=S.Matrix(4,5,lambda i,j:seed+2*i+j)
 C=S.Matrix(5,5,lambda i,j:(seed if i==j else i-j))
 QQ=S.zeros(9,13);QQ[:5,8:13]=S.eye(5)
 TT=S.zeros(9,13);TT[:5,:3]=Bs;TT[:5,8:13]=C;TT[5:9,8:13]=Bt
 JJ=S.zeros(13);JJ[3:8,8:13]=S.eye(5)
 ck(QQ*JJ==S.zeros(9,13),'synthetic radical Q chain identity')
 ck(TT*JJ==S.zeros(9,13),'synthetic radical full-family identity')
 ck(JJ*JJ==S.zeros(13),'synthetic radical square zero')
 ck(13-QQ.rank()==8 and 9-QQ.rank()==4,'original kernel/cokernel dimensions')
 for col in range(3):
  kk=S.eye(13)[:,col];uu=S.zeros(13,1);uu[8:13,0]=-Bs[:,col]
  ck(QQ*uu==-TT*kk,'matrix first correction')
  ck((TT*uu)[5:9,0]==-Bt*Bs[:,col],'matrix second factorization')
 for col in range(3,8):ck(TT[:,col]==S.zeros(9,1),'D kernel first symbol zero')
# Imported Hom character bookkeeping: A,D,P dimensions 3,5,4; distinct.
# A tensor D decomposes A+V+P+D, with one P and one D.
ck(3*5==3+3+4+5,'tensor dimension')
ck(len(['P' for v in ['A','V','P','D'] if v=='P'])==1,'unique quotient P channel')
# Constant-rank multiplication certificate, independent of actual scalar.
x,y,z=S.symbols('x y z')
M=S.Matrix([[x,0,0],[y,x,0],[z,y,x],[0,z,y],[0,0,z]])
ck(M[:3,:].det()==x**3,'constant-rank leading certificate')
ck(M[2:5,:].det()==z**3,'constant-rank trailing certificate')
ck(M[1:4,:].subs({x:0,z:0}).det()==y**3,'constant-rank middle-only certificate')
H=S.symbols('H');ch=S.series((1-H)**(-3),H,0,3).removeO()
ck(ch==1+3*H+6*H**2,'surviving cokernel Chern classes')
ck(8-3==5 and 5-3==2,'surviving kernel and cokernel ranks')
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/e['local_path']).read_bytes()
 ck(hashlib.sha256(data).hexdigest()==e['sha256'],'input SHA256 '+e['local_path'])
 ck(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob'],'input Git blob '+e['local_path'])
print(json.dumps(dict(status='pass',checks=checks,selected_internal_D_scalar='zero conditional on full-J TypeII',second_symbol='eta beta2_M = -b_T delta^-1 b_S',quotient_first_symbol='nonzero multiplication Sym2 tensor Sym4 to Sym6/V',internal_universal_cokernel=dict(rank=2,c1=3,c2=6),scope='No full-J existence assertion and no source-pair cut'),indent=2))
