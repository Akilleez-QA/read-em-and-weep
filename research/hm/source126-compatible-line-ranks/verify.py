#!/usr/bin/env python3
"""Exact synthetic endpoint certificates, never actual HM-instance evaluation."""
from pathlib import Path
import hashlib,json,itertools
import sympy as s
ROOT=Path(__file__).resolve().parent
count=0
def check(x,label):
 global count
 if not bool(x): raise RuntimeError(label)
 count+=1
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(hashlib.sha256(b).hexdigest()==item['sha256'],'sha256 '+item['local_path'])
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'blob '+item['local_path'])
rows=[]
for u,k,d in itertools.product(range(2),repeat=3):
 v=d+k
 if u==k==0: continue
 rows.append((u,k,d,v,4*u+5*v,4+5*d))
check({x[4:] for x in rows}=={(4,4),(9,9),(5,4),(10,9),(9,4),(14,9)},'six rows')
check({x[4:] for x in rows if x[3]<=1}=={(4,4),(9,9),(5,4),(9,4)},'Type I rows')
check({x[4:] for x in rows if x[2]==1}=={(9,9),(10,9),(14,9)},'Type III rows')
for u,k,d,v,r2,r4 in rows:
 # P: Q is the inclusion C^3 into C^4. Extra target supplies j4
 # when its row is zero on im Q.
 qp=s.zeros(4,3)
 for i in range(3): qp[i,i]=1
 jp2=s.zeros(3); jp4=s.zeros(4)
 if u: jp2[0,1]=jp4[0,1]=1
 else: jp4[0,3]=1
 # D: Q is projection C^4 onto first three coordinates; ker=e3.
 qd=s.zeros(3,4)
 for i in range(3): qd[i,i]=1
 jd2=s.zeros(4); jd4=s.zeros(3)
 if d: jd2[0,1]=jd4[0,1]=1
 if k: jd2[3,2 if d else 0]=1
 Q=s.diag(s.zeros(0,3),s.eye(6),s.kronecker_product(qp,s.eye(4)),s.kronecker_product(qd,s.eye(5)))
 J2=s.diag(s.zeros(3),s.zeros(6),s.kronecker_product(jp2,s.eye(4)),s.kronecker_product(jd2,s.eye(5)))
 J4=s.diag(s.zeros(6),s.kronecker_product(jp4,s.eye(4)),s.kronecker_product(jd4,s.eye(5)))
 check(Q.shape==(37,41),'Q dimensions')
 check(Q.rank()==33,'actual character-model Q rank')
 check(J2*J2==s.zeros(41) and J4*J4==s.zeros(37),'square-zero')
 check(J4*Q==Q*J2,'compatibility')
 check((J2.rank(),J4.rank())==(r2,r4),'endpoint rank pair')
 check(jd2.rank()==v and jd4.rank()==d,'D ranks')
 # Directly verify all Q-kernel vectors annihilated.
 check(all(J2*z==s.zeros(41,1) for z in Q.nullspace()),'kernel killed')
 U=s.Matrix.hstack(*J2.nullspace()); Zdim=37-r4
 check(Zdim-(Q*U).rank()==4*u+5*k,'restricted cokernel')
 check(J4*Q*U==s.zeros(37,U.cols),'annihilator subcomplex')
 # quotient-Q rank can be read as rank(j4 Q), since j4 identifies N4/Z with im j4.
 qr=(J4*Q).rank()
 check((r2-qr,r4-qr)==(5*k,4*(1-u)),'quotient kernel/cokernel')
 check(r2-r4==4*(u-1)+5*k,'top difference')
 allowed=0<=r2-r4<=4
 check(allowed==(not(u==k==1)), 'bad rows')
 if allowed:
  # Jordan-module source and target: pairs (e_i,f_i), epsilon f_i=e_i,
  # followed by simple blocks. Construct an explicit module surjection.
  a,b=r2,r4; n,m=41,37
  ns=s.zeros(n); nt=s.zeros(m); F=s.zeros(m,n)
  for i in range(a): ns[2*i,2*i+1]=1
  for i in range(b): nt[2*i,2*i+1]=1; F[2*i,2*i]=F[2*i+1,2*i+1]=1
  tops=[2*i+1 for i in range(b,a)]+list(range(2*a,n))
  check(len(tops)>=m-2*b,'enough simple tops')
  for target,source in zip(range(2*b,m),tops): F[target,source]=1
  check(F*ns==nt*F,'explicit module map')
  check(F.rank()==m,'explicit surjection')
 else:
  check((37-r4)-(41-r2)==1,'forced cokernel line')
print(f'PASS: {count} exact checks; six endpoint footprints, four synthetic surjections; no actual HM evaluation.')
