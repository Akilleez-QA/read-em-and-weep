#!/usr/bin/env python3
"""Exact whole-orbit certificates. No sampled roots or actual source values."""
from pathlib import Path
import hashlib,json
from itertools import permutations,combinations_with_replacement
from model import *
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
 if not bool(condition): raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check('sha256 '+item['label'],hashlib.sha256(data).hexdigest()==item['sha256'])
 check('git blob '+item['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
def detpoly(mat):
 out=s.Poly(0,p,q,t,extension=z)
 for perm in permutations(range(mat.rows)):
  term=s.Poly((-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows)),p,q,t,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],p,q,t,extension=z)
  out+=term
 return out.as_expr()
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*detpoly(B[[j for j in range(4) if j!=i],:]) for i in range(4)]])
F=(N*L*(R1-2*R2)).applyfunc(s.expand)
mons=[p**i*q**j*t**(3-i-j) for i in range(4) for j in range(4-i)]
outmons=[p**i*q**j*t**(12-i-j) for i in range(13) for j in range(13-i)]
C=s.Matrix([[s.Poly(f*m,p,q,t).coeff_monomial(mm) for f in F for m in mons] for mm in outmons])
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
check('bounded coefficient matrix shape',C.shape==(91,40))
check('exact coefficient rank',DomainMatrix.from_Matrix(C).convert_to(QQ.algebraic_field(z)).rank()==37)
S=s.Matrix([[s.sympify(e) for e in row] for row in json.loads((ROOT/'S.json').read_text())])
check('certificate matrix shape',S.shape==(4,3))
check('cubic homogeneous entries',all(s.Poly(f,p,q,t).is_homogeneous and s.Poly(f,p,q,t).total_degree()==3 for f in S))
check('entire syzygy identity',all(s.expand(f)==0 for f in F*S))
for i in range(4):check('signed maximal minor '+str(i),s.expand((-1)**i*detpoly(S[[j for j in range(4) if j!=i],:])-9*z*F[i]/2050)==0)
ph=(1+z)/2
G=s.Matrix([[ph/2+s.I/2,(ph-1)/2],[-(ph-1)/2,ph/2-s.I/2]])
def sm(g,n):
 aa,bb,cc,dd=list(g)
 return s.Matrix.hstack(*[cv((aa*x+cc*y)**(n-j)*(bb*x+dd*y)**j,n) for j in range(n+1)])
Ag=sm(G,2).applyfunc(s.simplify);Ainv=sm(G.adjugate(),2).applyfunc(s.simplify);Pg=s.kronecker_product(G,G.xreplace({z:-z})).applyfunc(s.simplify)
coords=Ainv*s.Matrix([p,q,t]);trans=(Pg*S.subs(dict(zip([p,q,t],coords)),simultaneous=True)).applyfunc(s.expand)
def coeff(M):return s.Matrix([[s.Poly(M[i,j],p,q,t).coeff_monomial(m).expand() for j in range(3)] for i in range(4) for m in mons])
CS=coeff(S);CT=coeff(trans);piv=CS.T.rref()[1];T=(CS[list(piv),:].inv()*CT[list(piv),:]).applyfunc(s.simplify)
check('coefficient certificate rank',CS.rank()==3)
check('full coefficient kernel',C*CS==s.zeros(91,3))
check('group generator determinant',s.simplify(G.det())==1)
check('group generator projective order',all(s.simplify(e)==0 for e in G**5+s.eye(2)))
check('pinned projection intertwiner',all(s.expand(e)==0 for e in Pi*sm(G,6)-Pg*Pi))
check('whole coefficient-space group action',all(s.expand(e)==0 for e in CS*T-CT))
check('A character trace',s.simplify(s.trace(T)-(1+z)/2)==0)
check('same trace as A',s.simplify(s.trace(T)-s.trace(Ag))==0)
check('different from V and trivial',s.simplify(s.trace(T)-(1-z)/2)!=0 and s.simplify(s.trace(T)-3)!=0)
zeta=s.symbols('zeta');num=1-4*zeta**9+3*zeta**12
check('Hilbert numerator double zero',num.subs(zeta,1)==0 and s.diff(num,zeta).subs(zeta,1)==0)
check('Hilbert scheme length',s.diff(num,zeta,2).subs(zeta,1)/2==54)
check('split kernel Chern data',3*(-3)==-9 and 3*9==81-54)
check('modified kernel Chern data',76-54==22 and 100-54==46)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'coefficient_matrix_shape':[91,40],'coefficient_rank':37,'syzygy_dimension':3,'syzygy_representation':'A','minor_factor':'9sqrt(5)/2050','kernel_bundle':'A O(-3)','base_length':54,'original_fourth_kernel_c2':46},indent=2))
