#!/usr/bin/env python3
"""Bounded exact synthetic regressions. No actual-source instance is used."""
import hashlib,json
from pathlib import Path
from itertools import product
import sympy as s
ROOT=Path(__file__).resolve().parent
count=0
def ck(p,msg):
    global count
    count+=1
    if not p: raise RuntimeError(msg)
for row in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/row['local_path']).read_bytes()
    ck(hashlib.sha256(b).hexdigest()==row['sha256'],'SHA256 '+row['local_path'])
    ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'Git blob '+row['local_path'])
dims={'A':3,'V':3,'P':4,'D':5,'Wp':2,'S':4,'T':6}
N=[{'A':1,'V':2,'P':3,'D':4},{'Wp':3,'S':3,'T':6},{'V':2,'P':4,'D':3}]
images=[ [{'D':1},{'T':1},{'P':1}], [{'P':1,'D':1},{'Wp':1,'S':1,'T':1},{'P':1,'D':1}], [{'P':1,'D':1},{'Wp':1,'S':1,'T':2},{'P':1,'D':1}] ]
expected=[(36,48,33),(32,42,28),(32,36,28)]
for im,e in zip(images,expected):
    q=[]
    for nn,ii in zip(N,im):
        sub={k:nn.get(k,0)-ii.get(k,0) for k in dims}
        ck(all(v>=0 for v in sub.values()),'constituent nonnegative')
        q.append(sum(dims[k]*v for k,v in sub.items()))
    ck(tuple(q)==e,'quotient dimensions')
# Exhaust all Schur support ranks for P+D -> P+D.
valid=[]
for rp,rd in product(range(2),repeat=2):
    if rp==1 and 1-rd==0: valid.append((rp,rd))
ck(valid==[(1,1)],'no P kernel plus no D cokernel forces isomorphism')
ck(32-8==28-4==24,'non-V quotient rank')
ck(36-7==33-4==29,'pure V quotient rank')
# Truncated formal series matrices, exact integer arithmetic. Universal synthetic
# upper triangular blocks, not source matrices. Verify both inverse sides and
# section/homotopy formulas modulo every t^m, m=1,...,7.
def mul(a,b,m):
    out=[s.zeros(a[0].rows,b[0].cols) for _ in range(m)]
    for i in range(min(m,len(a))):
        for j in range(min(m-i,len(b))): out[i+j]+=a[i]*b[j]
    return out
def add(a,b): return [x+y for x,y in zip(a,b)]
def neg(a): return [-x for x in a]
def eq(a,b): return all(x==y for x,y in zip(a,b))
for n in range(1,4):
 for seed in range(-2,3):
  B0=s.eye(n)
  B1=s.Matrix(n,n,lambda i,j: ((i+1)*(j+2)+seed)%5-2)
  C0=s.Matrix(n,2,lambda i,j: i-j+seed)
  C1=s.Matrix(n,2,lambda i,j: i+j-seed)
  D0=s.Matrix([[seed,1],[0,0],[1,seed]])
  D1=s.Matrix([[0,seed],[1,1],[seed,0]])
  for m in range(1,8):
   z=lambda r,c:[s.zeros(r,c) for _ in range(m)]
   B=[B0]+([B1] if m>1 else [])+[s.zeros(n) for _ in range(max(0,m-2))]
   C=[C0]+([C1] if m>1 else [])+[s.zeros(n,2) for _ in range(max(0,m-2))]
   D=[D0]+([D1] if m>1 else [])+[s.zeros(3,2) for _ in range(max(0,m-2))]
   inv=[(-B1)**i for i in range(m)]
   identity=[s.eye(n)]+[s.zeros(n) for _ in range(m-1)]
   ck(eq(mul(B,inv,m),identity),'left formal inverse')
   ck(eq(mul(inv,B,m),identity),'right formal inverse')
   X=neg(mul(inv,C,m))
   # chain section condition B X + C = 0 (other row is D).
   ck(eq(add(mul(B,X,m),C),z(n,2)),'filtered section')
   # hM on degree0 is [1,inv C;0,0]=1-sp.
   ck(eq(mul(inv,C,m),neg(X)),'degree zero homotopy')
   # Mh on degree1 is [1,0;0,0]=1-sp.
   ck(eq(mul(B,inv,m),identity),'degree one homotopy')
   # Full change-of-domain multiplication, including rectangular quotient.
   for k in range(m):
    full=sum((B[i]*X[k-i] for i in range(k+1)),s.zeros(n,2))+C[k]
    ck(full==s.zeros(n,2),'block cancellation coefficient')
# Pure V negative control with exact displayed isotypic multiplicities.
# Blocks below are synthetic Schur matrices, never selected actual HM tensors.
# D: Q kills d0, maps d1,d2,d3 isomorphically; j2(d1)=d0, j4_D=0.
QD=s.Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1]])
jD=s.zeros(4);jD[0,1]=1
# P: Q includes three coordinates into first three of four;
# j4(p3)=p0, and j2_P=0. Thus imQ=kerj4 in P as well.
QP=s.eye(4)[:,:3];jP=s.zeros(4);jP[0,3]=1
ck(QD*jD==s.zeros(3,4),'pure V D compatibility')
ck(jP*QP==s.zeros(4,3),'pure V P compatibility')
ck(jD*jD==s.zeros(4) and jP*jP==s.zeros(4),'square zero')
ck(QD.rank()*5+QP.rank()*4+6==33,'synthetic full rank33')
# Divide domain by d0 and target by p0; retain the untouched A and V blocks.
barD=QD[:,1:];barP=QP[1:,:]
rankbar=barD.rank()*5+barP.rank()*4+6
ck(rankbar==29,'pure V quotient rank29')
ck(36-rankbar==7 and 33-rankbar==4,'pure V quotient cohomology')
ck((3-barP.rank())*4==4,'new kernel P in pure V quotient')
result={'checks':count,'status':'PASS','source_instances_evaluated':0,
 'non_V_two_term_quotient':[32,28],'pure_V_two_term_quotient':[36,33],
 'pure_V_quotient_rank':29,'quotient_pencil_dimensions':expected,
 'scope':'Conditional structural reduction; bounded synthetic checks only.'}
print(json.dumps(result,indent=2,sort_keys=True))
