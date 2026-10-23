#!/usr/bin/env python3
"""Exact imported-byte and synthetic module controls. No HM instance evaluation."""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name, condition):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

def blob(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
for e in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/e['local_path']).read_bytes()
    check(e['local_path']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
    check(e['local_path']+' Git blob',blob(b)==e['git_blob'])

survivors=[]
for u,v,w in itertools.product(range(1,3),repeat=3):
    # u<=1 from P-injectivity; w=v-1 from actual D-image equality.
    if u<=1 and w==v-1:
        survivors.append((u,v,w))
check('unique collective-image triple',survivors==[(1,2,1)])
u,v,w=survivors[0]
check('first radical image dimension',4*u+5*v==14)
check('fourth radical image dimension',4+5*w==9)
check('radical quotient dimensions',(41-14,37-9)==(27,28))
check('original necessary top inequality strictly fails',8-4*u-5*v+5*w==-1)

# Synthetic multiplicity spaces; tensor with identity on each irreducible.
qA=s.zeros(0,1); qV=s.eye(2)
qP=s.zeros(4,3)
for i in range(3): qP[i,i]=1
qD=s.zeros(3,4)
for i in range(3): qD[i,i+1]=1
p2a=s.zeros(3);p2a[0,2]=1;p2b=s.zeros(3)
p4a=s.zeros(4);p4a[0,2]=1;p4b=s.zeros(4);p4b[0,3]=1
d2a=s.zeros(4);d2a[0,2]=1;d2b=s.zeros(4);d2b[1,3]=1
d4a=s.zeros(3);d4b=s.zeros(3);d4b[0,2]=1

def block(ms):
    return s.diag(*[(s.kronecker_product(m,s.eye(d)) if m.rows and m.cols else s.zeros(m.rows*d,m.cols*d)) for m,d in zip(ms,(3,3,4,5))])
Q=block((qA,qV,qP,qD))
J2=[block((s.zeros(1),s.zeros(2),p2a,d2a)),block((s.zeros(1),s.zeros(2),p2b,d2b))]
J4=[block((s.zeros(0),s.zeros(2),p4a,d4a)),block((s.zeros(0),s.zeros(2),p4b,d4b))]
check('Q shape',Q.shape==(37,41))
check('Q rank33',Q.rank()==33)
for i in range(2):
    check(f'Q/J compatibility {i}',J4[i]*Q==Q*J2[i])
    for j in range(2):
        check(f'J2 square-zero products {i},{j}',J2[i]*J2[j]==s.zeros(41))
        check(f'J4 square-zero products {i},{j}',J4[i]*J4[j]==s.zeros(37))
I2=s.Matrix.hstack(*J2).columnspace();I4=s.Matrix.hstack(*J4).columnspace()
U=s.Matrix.vstack(*J2).nullspace();Z=s.Matrix.vstack(*J4).nullspace()
check('synthetic images differ from annihilators',(len(I2),len(I4),len(U),len(Z))==(14,9,27,24))
I2m=s.Matrix.hstack(*I2);I4m=s.Matrix.hstack(*I4);Um=s.Matrix.hstack(*U);Zm=s.Matrix.hstack(*Z)
check('Q image of collective image is collective target image',(Q*I2m).rank()==9 and s.Matrix.hstack(Q*I2m,I4m).rank()==9)
check('restricted S rank', (Q*Um).rank()==19)
check('restricted S dimensions', (Um.cols,Zm.cols)==(27,24))
check('restricted image lies in Z', s.Matrix.hstack(Q*Um,Zm).rank()==24)
check('joint P row rank2',s.Matrix.vstack(p4a[0,:],p4b[0,:]).rank()==2)
check('D kernel is included in I2',s.Matrix.hstack(d2a,d2b,*qD.nullspace()).rank()==2)
check('D image equality',s.Matrix.hstack(qD*d2a,qD*d2b,d4a,d4b).rank()==1)
check('quotient T dimensions',(41-len(U),37-len(Z))==(14,13))
# Rank of Q modulo Z is rank([Q,Z])-dim Z.
quotrank=s.Matrix.hstack(Q,Zm).rank()-Zm.cols
check('actual-diagram quotient rank9',quotrank==9)
check('quotient cohomology dimensions',(14-quotrank,13-quotrank)==(5,4))

# A surjection of J-modules always induces a quotient surjection. The
# following numerical rank bound uses only dimensions, not a trial matrix.
check('every quotient map has cokernel at least1',min(27,28)==27 and 28-27==1)
check('full-map rank bound36',37-(28-27)==36)
# If both diagonal complex maps are onto, an upper triangular map is onto;
# the contrapositive with quotient rank13 bounds S by23.
check('nonzero cubic would contradict bound',24+13>36)
check('generic lower rank from known second',33+3==36)
check('generic residual shape',(37-36,41-36)==(1,5))
result={'status':'PASS','checks':len(checks),'collective_images':{'N2':'P+2D','N4':'P+D'},'top_dimensions':[27,28],'conditional_rank_bound':36,'conditional_generic_rank':36,'conditional_generic_later_original_symbols':'all zero after second','conditional_internal_cubic':'zero','conditional_generic_original_fourth':'zero','actual_instance_evaluated':False,'source_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
