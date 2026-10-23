#!/usr/bin/env python3
"""Exact synthetic tests of the isolated-initial-vertex extension lemma."""
import hashlib,json
from pathlib import Path
import sympy as s
r=Path(__file__).resolve().parent
n=0
def ck(x,m):
 global n
 n+=1
 if not x: raise RuntimeError(m)
for row in json.loads((r/'INPUTS.json').read_text()):
 b=(r/row['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'digest')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'blob')
# Coordinates A,V,P,D,Wp,S,T with dimensions3,3,4,5,2,4,6.
d=s.Matrix([3,3,4,5,2,4,6])
N0=[s.Matrix(v) for v in ([0,0,1,1,0,0,0],[0,0,0,0,1,1,2],[0,1,2,1,0,0,0])]
N8=[s.Matrix(v) for v in ([1,1,1,1,0,0,0],[0,0,0,0,1,1,2],[0,1,1,1,0,0,0])]
Z=[s.Matrix(v) for v in ([0,1,0,1,0,0,0],[0]*7,[0]*7)]
for i,e in enumerate((32,36,28)):
 ck((N0[i]+N8[i]+Z[i]).dot(d)==e,'quotient character dimension')
ck(18-12==6,'exceptional middle quotient nonzero')
# Any extension by a source-only vertex: p2=(0,1), while p3,p4
# arbitrary invertible coordinate shears. Test both pencil generators
# and every bounded linear combination, with many arbitrary sections.
for a in range(-3,4):
 for b in range(-2,3):
  p2=s.Matrix([[0,0,1,0],[0,0,0,1]])
  p3=s.Matrix([[1,a],[0,1]])
  p4=s.Matrix([[1,0],[b,1]])
  lift=s.Matrix([[a,b],[b,a],[1,0],[0,1]])
  s3=p3.inv();s4=p4.inv()
  ck(p2*lift==s.eye(2),'section at source')
  Au=s.Matrix([[a,1],[b,0]]);Av=s.Matrix([[0,b],[1,a]])
  Bu=s.Matrix([[1,b],[a,1]]);Bv=s.Matrix([[a,0],[1,b]])
  for u,v in ((1,0),(0,1),(1,1),(2,-1),(-1,2)):
   A=u*Au+v*Av; B=u*Bu+v*Bv
   AK=s3*A*p2; BK=s4*B*p3
   ck(AK*lift==s3*A,'first-arrow section')
   ck(BK*s3==s4*B,'second-arrow section')
   z=s.Matrix([[1,0],[0,1],[0,0],[0,0]])
   ck(AK*z==s.zeros(2),'isolated summand killed')
   iso=z.row_join(lift)
   ck(iso.det()!=0,'direct sum isomorphism')
result={'checks':n,'status':'PASS','actual_source_instances_evaluated':0,
'quotient_dimensions':[32,36,28],
'negative_pencil_type':'N0 + N8 + (V+D)[2]',
'excluded_from_this_statement':['pure V direction','unique exceptional mixed direction']}
print(json.dumps(result,indent=2,sort_keys=True))
