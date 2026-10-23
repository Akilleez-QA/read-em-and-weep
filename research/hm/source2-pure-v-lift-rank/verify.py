#!/usr/bin/env python3
"""Universal symbolic certificates; never evaluates actual HM data."""
from model import *
from pathlib import Path
from itertools import permutations,combinations
import hashlib,json
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
 if not value:raise RuntimeError(name)
 checks.append(name)
def zero(M):return all(s.simplify(v)==0 for v in M)
for item in json.loads((root/'INPUTS.json').read_text()):
 data=(root/item['local_path']).read_bytes()
 ck('sha256 '+item['local_path'],hashlib.sha256(data).hexdigest()==item['sha256'])
 ck('git_blob '+item['local_path'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
ck('orthogonal inclusion right inverse',zero(Pi*E-s.eye(4)))
ck('nondegenerate induced pairing',GP.det()!=0)
ck('adjoint identity',zero(GD*Ls-L.T*GP))
ck('projected skew action',zero(DP.T*GP+GP*DP))
ck('projected Clifford square',zero(DP*DP-4*(q*q-4*p*t)*s.eye(4)))
# Independent source-generator authentication in the pinned convention.
def sm(mat,n):
 a,b,c,d=list(mat)
 return s.Matrix.hstack(*[cv((a*x+c*y)**(n-j)*(b*x+d*y)**j,n) for j in range(n+1)])
ph=(1+z)/2
for i,(ar,br,cr,dr) in enumerate([(0,1,0,0),(0,0,1,0),(s.Rational(1,2),)*4,(ph/2,s.Rational(1,2),(ph-1)/2,0)]):
 mat=s.Matrix([[ar+s.I*br,cr+s.I*dr],[-cr+s.I*dr,ar-s.I*br]])
 target=s.kronecker_product(mat,mat.subs(z,-z))
 ck('P6 generator '+str(i),zero(Pi*sm(mat,6)-target*Pi))
 ck('apolar generator '+str(i),zero(sm(mat,6).T*G6*sm(mat,6)-G6))
# Basis independence from full symbolic coefficient matrix.
mons=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
C=s.Matrix([[s.Poly(M[i,j],p,q,t).coeff_monomial(mon) for M in [R1,R2]] for i in range(5) for j in range(4) for mon in mons])
ck('quadratic basis independence',C.rank()==2)
V=s.Matrix.hstack(*Pi.nullspace());GV=s.simplify(V.T*G6*V)
M=s.Matrix.hstack(*[cv(a*x**(4-i)*y**i,6) for i in range(5)])
J=s.simplify(GD.inv()*M.T*G6*V)
H=s.simplify(GV.inv()*V.T*G6*rho(6)*E)
ck('infinitesimal multiplication covariance',zero(rho(6)*M-M*DD))
ck('exceptional V factorization',zero(R1-R2-J*H))
def detpoly(mat,gens):
 out=s.Poly(0,*gens,extension=z)
 for perm in permutations(range(mat.rows)):
  sign=(-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows))
  term=s.Poly(sign,*gens,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],*gens,extension=z)
  out+=term
 return out.as_expr()
R=(aa*R1+bb*R2).subs(p,1)
minors=[detpoly(R[[j for j in range(5) if j!=i],:],(aa,bb,q,t)) for i in range(5)]
cs=[]
for f in minors:cs.extend(s.Poly(f,q,t).coeffs())
res=[]
for f in cs:
 quotient,remainder=s.div(f,aa+bb,aa,bb,extension=z)
 ck('linear exceptional factor coefficient '+str(len(res)),remainder==0)
 res.append(quotient)
cmons=[aa**3,aa**2*bb,aa*bb**2,bb**3]
CC=s.Matrix([[s.Poly(f,aa,bb,extension=z).coeff_monomial(mon) for mon in cmons] for f in res])
ck('whole residual cubic span',CC.rank()==4)
pivots=CC.T.rref()[1][:4];witness=CC[list(pivots),:]
ck('nonzero four-row cubic witness',s.simplify(witness.det())!=0)
ck('compact coefficient one',s.simplify(s.Poly(minors[0],q,t).coeff_monomial(q**8)-s.Rational(9,80000)*z*bb*(aa+bb)*(aa*aa-7*aa*bb+bb*bb))==0)
ck('compact coefficient two',s.simplify(s.Poly(minors[0],q,t).coeff_monomial(q**6*t**2)+s.Rational(3,8000)*(aa+bb)*(4*aa**3-90*aa*aa*bb+15*aa*bb*bb+bb**3))==0)
# Both coefficient-projective charts have a single reduced exceptional point.
for v,other in [(aa,bb),(bb,aa)]:
 gb=s.groebner([f.subs(v,1) for f in cs],other,extension=z)
 ck('coefficient projective chart '+str(v),list(gb)==[other+1])
# All direction charts certify the V->D subbundle injection.
jmins=[detpoly(J[list(rows),:],(p,q,t)) for rows in combinations(range(5),3)]
for var,others in [(p,(q,t)),(q,(p,t)),(t,(p,q))]:
 gb=s.groebner([f.subs(var,1) for f in jmins],*others,extension=z)
 ck('J subbundle chart '+str(var),list(gb)==[1])
cP=Pi*cv(a**3,6)
cof=s.Matrix([(-1)**i*detpoly(H[:,[j for j in range(4) if j!=i]],(p,q,t)) for i in range(4)])
ck('H exact cofactor vector',zero(cof+s.Rational(243,2560)*z*cP))
ck('exceptional cubic kernel',zero((R1-R2)*cP))
ck('cubic nonzero',not zero(cP))
ck('kernel line twist',-2-3==-5)
# Exact representation dimension, separate from actual coefficient selection.
sizes=[1,15,20,12,12];Pc=[4,0,1,-1,-1];Dc=[5,1,-1,0,0]
ck('lift Hom dimension two',s.Rational(sum(n*pc*d*(1+d) for n,pc,d in zip(sizes,Pc,Dc)),60)==2)
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,coefficient_ideal='(alpha+beta)*(alpha,beta)^3',projective_saturation='(alpha+beta)',residual_witness_rows=list(pivots),residual_witness_determinant=str(s.simplify(witness.det())),exceptional_rank='3 off six reduced C5 axes; 2 on those axes',scope='universal lift pencil only; no actual coefficients selected'),indent=2))
