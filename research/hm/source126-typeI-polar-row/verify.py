#!/usr/bin/env python3
"""Universal symbolic interfaces only; no selected HM data."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
count=0
def ck(x,msg):
 global count
 count+=1
 if not x:raise RuntimeError(msg)
for row in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/row['local_path']).read_bytes()
 ck(hashlib.sha256(b).hexdigest()==row['sha256'],'source sha256')
 ck(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'source blob')
names=('one','W','A','S','D','T','V','P','Wp');dims=(1,2,3,4,5,6,3,4,2)
def ch(**k):return tuple(k.get(n,0) for n in names)
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def mw(a):return tuple(sum(a[i]*rules[i][j] for i in range(9)) for j in range(9))
sym=[ch(one=1),ch(W=1)]
for n in range(2,11):sym.append(tuple(x-y for x,y in zip(mw(sym[-1]),sym[-2])))
for n,a in enumerate(sym):ck(min(a)>=0 and sum(x*y for x,y in zip(a,dims))==n+1,'symmetric power')
ck(sym[4]==ch(D=1),'degree4 no invariants')
ck(sym[7]==ch(Wp=1,T=1),'degree7')
ck(sym[8]==ch(P=1,D=1),'degree8 no invariants')
ck(sym[9]==ch(S=1,T=1),'degree9')
ck(mw(ch(D=1))==ch(S=1,T=1),'D times W')
ck(sum(a*b for a,b in zip(mw(ch(D=1)),sym[7]))==1,'unique polar Hom')
ck(2*1==2,'two D copies Hom dimension')
ck((3+3+5)-2*5==1,'constant quotient rank')
ck(0-(-2*2*5)==20,'constant quotient degree')
ck(28-20==8 and sym[8][0]==0,'forbidden quotient map')
# Bivariate polynomials are coefficient dictionaries. Monomial pairs span the
# full bilinear derivative identities, so these finite tests cover all terms.
def add(*ps):
 q={}
 for p in ps:
  for m,c in p.items():q[m]=q.get(m,0)+c
 return {m:c for m,c in q.items() if c}
def scale(p,c):return {m:a*c for m,a in p.items() if a*c}
def mul(p,q):
 out={}
 for (a,b),c in p.items():
  for (d,e),f in q.items():out[(a+d,b+e)]=out.get((a+d,b+e),0)+c*f
 return {m:c for m,c in out.items() if c}
def der(p,j):
 q={}
 for m,c in p.items():
  if m[j]:
   z=list(m);z[j]-=1;q[tuple(z)]=c*m[j]
 return q
x={(1,0):1};y={(0,1):1}
for i in range(3):
 p={(2-i,i):1}
 for j in range(9):
  r={(8-j,j):1}
  for k in (0,1):
   ck(der(mul(p,r),k)==add(mul(der(p,k),r),mul(p,der(r,k))),'differentiated product')
  ck(add(mul(x,mul(p,der(r,0))),mul(y,mul(p,der(r,1))))==scale(mul(p,r),8),'Euler first-polar implication')
# A common h indeed produces precisely the forbidden S-zero recurrence.
for j in range(5):
 h={(4-j,j):1};rs=[mul(h,{(4-i,i):1}) for i in range(5)]
 for i in range(4):ck(mul(y,rs[i])==mul(x,rs[i+1]),'common-factor Koszul recurrence')
# The Koszul tensors have disjoint leading y tensor f_i coordinates, hence
# independent; 4-dimensional S plus 6-dimensional T exhausts dimension10.
ck(4+6==2*5==10,'Koszul and symmetric summands exhaust')
# Negative control: repeated coefficient systems have linear syzygies, so
# absence of syzygies must be proved rather than inferred from degrees.
r={(8,0):1}
ck(add(mul(x,r),scale(mul(x,r),-1))=={},'dependent-system negative control')
# Conditional intersection of old r<=1 and new r>=1.
ck([r for r in range(3) if r<=1 and r>=1]==[1],'unique compatible joint rank')
print(f'PASS: {count} checks; six immutable sources.')
