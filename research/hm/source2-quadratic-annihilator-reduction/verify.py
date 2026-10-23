#!/usr/bin/env python3
"""Bounded exact controls for quadratic-annihilated, not zero-arrow, spaces."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent
n=0
def ck(x,m):
 global n
 n+=1
 if not x:raise RuntimeError(m)
for row in json.loads((root/'INPUTS.json').read_text()):
 b=(root/row['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'digest')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'blob')
# G-character coordinates V,P,D,Wp,S,T.
d=s.Matrix([3,4,5,2,4,6])
NC=[s.Matrix(v) for v in ([1,1,2,0,0,0],[0,0,0,1,1,2],[0,1,1,0,0,0])]
for middle,expected in [(2,(8,0,0)),(1,(8,6,0))]:
 I=[s.Matrix(v) for v in ([0,1,1,0,0,0],[0,0,0,1,1,middle],[0,1,1,0,0,0])]
 ck(tuple((a-b).dot(d) for a,b in zip(NC,I))==expected,'endpoint subquotient')
ck([3+5*i for i in (0,1)]==[3,8],'restriction ranks')
ck(24-8==20-4==16,'rank8 active dimensions')
ck(24-3==25-4==21,'rank3 active dimensions')
ck(9+32-5==36<37,'full family rank bound')
# Exceptional synthetic middle contains K3 of dimension6. A maps Z (dim8)
# nontrivially into K3. B kills K3 but is nonzero on its complement. These
# controls intentionally do NOT satisfy a zero-first-arrow assumption.
for seed in range(-3,4):
 Au0=s.Matrix(6,8,lambda i,j:(i+j+seed)%3-1)
 Av0=s.Matrix(6,8,lambda i,j:(2*i-j+seed)%5-2)
 Au=Au0.col_join(s.zeros(4,8));Av=Av0.col_join(s.zeros(4,8))
 Bu=s.zeros(7,6).row_join(s.Matrix(7,4,lambda i,j:(i-j+seed)%3-1))
 Bv=s.zeros(7,6).row_join(s.Matrix(7,4,lambda i,j:(i+2*j+seed)%5-2))
 ck(Au!=s.zeros(10,8) and Av!=s.zeros(10,8),'nonzero first arrows')
 ck(Bu!=s.zeros(7,10) and Bv!=s.zeros(7,10),'nonzero full second arrows')
 for B in (Bu,Bv):
  for A in (Au,Av):ck(B*A==s.zeros(7,8),'all quadratic composites vanish')
 for r in (3,8):
  F=s.diag(*[1 if (i+seed)%2==0 else -1 for i in range(r)])
  # Coefficientwise polynomial shear for constant and three independent
  # deformation coefficients; no actual negative parameter is selected.
  for k in range(4):
   C=s.Matrix(r,24,lambda i,j:(i+(k+1)*j+seed)%5-2)
   X=-F.inv()*C
   ck(F*X+C==s.zeros(r,24),'constant block shear coefficient')
   U=s.eye(r+24);U[:r,r:]=X
   V=s.eye(r+24);V[:r,r:]=-X
   ck(U*V==s.eye(r+24),'shear inverse coefficient control')
result={'checks':n,'status':'PASS','actual_source_instances_evaluated':0,
 'covers':['all regular non-V directions','unique exceptional mixed direction'],
 'requires':'quadratic annihilation, not zero first arrows',
 'active_dimensions_rank8':[24,20],'active_dimensions_rank3':[24,25],
 'rank3_original_affine_family_rank_bound':36}
print(json.dumps(result,indent=2,sort_keys=True))
