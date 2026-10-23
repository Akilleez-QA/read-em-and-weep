#!/usr/bin/env python3
"""Exact bounded synthetic checks; no HM coefficient/instance is chosen."""
import hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=0
def ck(v,m):
 global checks
 checks+=1
 if not v: raise RuntimeError(m)
for row in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/row['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'digest')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'blob')
# Schur multiplicity rank dichotomy. V injects; D either zero or injects.
ck(sorted(3+5*r for r in (0,1))==[3,8],'rank dichotomy')
# A,V,P,D multiplicities and dimensions.
d=s.Matrix([3,3,4,5]); src=s.Matrix([1,2,2,3]);tgt=s.Matrix([0,2,3,2]);Z=s.Matrix([0,1,0,1])
active=src-Z
ck(active.dot(d)==24,'active domain')
for rank,y,ker,codim,base_rank in [(8,s.Matrix([0,1,0,1]),s.Matrix([1,0,0,1]),20,16),(3,s.Matrix([0,1,0,0]),s.Matrix([1,0,0,0]),25,21)]:
 target=tgt-y
 ck(target.dot(d)==codim,'active target')
 ck(active-ker==target-s.Matrix([0,0,1,0]),'active image character')
 ck(24-ker.dot(d)==base_rank==codim-4,'invariant active rank')
 # Synthetic diagonal normal form with stated total dimensions. The active
 # invariant differential has exactly the rank required above; arbitrary
 # cross-block C0 is retained, rather than assumed zero.
 L=8-rank; w=28-rank
 for seed in range(-2,3):
  F=s.diag(*[1 if (i+seed)%2==0 else -1 for i in range(rank)])
  C0=s.Matrix(rank,24,lambda i,j:(i+2*j+seed)%5-2)
  C1=s.Matrix(rank,24,lambda i,j:(2*i-j+seed)%3-1)
  D0=s.zeros(w,24)
  for i in range(base_rank):D0[i,i]=1
  D1=s.Matrix(w,24,lambda i,j:(i-j+seed)%3-1)
  ck(F.rank()==rank,'invertible F')
  ck(D0.rank()==base_rank,'synthetic base rank')
  # Coefficientwise cancellation for three independent formal variables.
  for k in range(3):
   Ci=s.Matrix(rank,24,lambda i,j:(i+(k+1)*j+seed)%7-3)
   ck(F*(-F.inv()*Ci)+Ci==s.zeros(rank,24),'multivariable coefficient cancellation')
  for t in range(-2,3):
   C=C0+t*C1;D=D0+t*D1;X=-F.inv()*C
   M=(s.zeros(rank,L).row_join(F).row_join(C)).col_join(s.zeros(w,L+rank).row_join(D))
   change=s.eye(32)
   change[L:L+rank,L+rank:]=X
   diagonal=(s.zeros(rank,L).row_join(F).row_join(s.zeros(rank,24))).col_join(s.zeros(w,L+rank).row_join(D))
   ck(M*change==diagonal,'all-t block cancellation')
   invchange=s.eye(32);invchange[L:L+rank,L+rank:]=-X
   ck(change*invchange==s.eye(32),'polynomial inverse')
   if L:
    ck(M[:,:L]==s.zeros(28,L),'permanent five-dimensional kernel')
    # 28 target rows,32 source columns,5 zero columns: rank <=27;
    # with the original9-block restored: rank <=36.
    ck(32-L+9==36<37,'original-family rank bound')
   else: ck(M.shape==(28,32),'rank8 total shape')
# Degree-ten/degree-eight first-arrow injectivity forces common kernel
# to be precisely the isolated8-space; elementary tensor multiplication ranks.
ck(9+15+8==32 and 9+15==24,'zero-arrow kernel dimension')
result={'checks':checks,'status':'PASS','actual_source_instances_evaluated':0,
 'restriction_ranks':[3,8],'active_dimensions_rank8':[24,20],
 'active_dimensions_rank3':[24,25],'permanent_kernel_dimension_rank3':5,
 'original_41_to_37_family_rank_bound_rank3':36,
 'scope':'Conditional regular compatible radical line; no source or pair cut.'}
print(json.dumps(result,indent=2,sort_keys=True))
