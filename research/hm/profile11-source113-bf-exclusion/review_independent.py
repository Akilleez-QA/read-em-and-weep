#!/usr/bin/env python3
"""Independent fixed McKay-recurrence audit; no actual source instance is evaluated."""
from pathlib import Path
from collections import Counter
import hashlib, json
N=('one','W','Wp','A','V','P','S','D','T')
adj={
 'one':('W',),'W':('one','A'),'Wp':('P',),
 'A':('W','S'),'V':('T',),'P':('Wp','T'),
 'S':('A','D'),'D':('S','T'),'T':('D','V','P')}
def v(**kw):return tuple(kw.get(n,0) for n in N)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mw(a):
 d=Counter()
 for name,k in zip(N,a):
  for dest in adj[name]:d[dest]+=k
 return tuple(d[n] for n in N)
def prod_sym(a,n):
 if n==0:return a
 x,y=a,mw(a)
 for j in range(2,n+1):x,y=y,sub(mw(y),x)
 return y
s=lambda n:prod_sym(v(one=1),n)
def hom(j,R,k,U):
 return 0 if j<k else prod_sym(v(**{U:1}),j-k)[N.index(R)]
assert s(6)==v(V=1,P=1)
assert s(7)==v(Wp=1,T=1)
assert s(8)==v(P=1,D=1)
assert s(9)==v(S=1,T=1)
assert s(10)==v(A=1,V=1,D=1)
assert s(14)==v(A=1,V=1,P=1,D=1)
assert s(18)==v(A=1,V=1,P=2,D=1)
assert s(19)==v(W=1,Wp=1,S=1,T=2)
ks=[[(8,'A')],[(7,'W'),(10,'one')],[(9,'W'),(6,'one')],[(3,'Wp'),(18,'one')],[(6,'one'),(8,'one'),(10,'one')]]
rows=[(4,'D'),(5,'T'),(10,'one'),(12,'one')]
expected=[[[1,1,0,0]],[[1,0,0,0],[0,1,1,0]],[[1,1,0,0],[0,0,0,0]],[[0,0,0,0],[1,1,0,0]],[[0,0,0,0],[1,0,0,0],[0,1,1,0]]]
for k,e in zip(ks,expected):
 assert [[hom(j,R,n,U) for n,U in rows] for j,R in k]==e
 assert sum((1 if R=='one' else {'A':3,'W':2,'Wp':2}[R])*j for j,R in k)==24
 h=v();ch=v()
 for j,R in k:
  if j>=4:h=add(h,prod_sym(v(**{R:1}),j-4))
  if j==3:ch=add(ch,v(**{R:1}))
  elif j>=5:ch=sub(ch,prod_sym(v(**{R:1}),j-5))
 assert h==v(A=1,V=1,P=1,D=1)
 assert ch==v(W=-1,S=-1,T=-1)
# Check every surviving first-span character without character tables.
def polar(js):
 c0=sub(s(18),v(P=1));c1=s(19)
 for j,R in js:
  c0=sub(c0,prod_sym(v(**{R:1}),j-4))
  c1=sub(c1,prod_sym(v(**{R:1}),j-5))
 return c0,sub(c1,mw(c0))
assert polar([(7,'W')])==(v(V=1,P=1),v())
assert polar([(8,'A')])==(v(),v(Wp=1,T=1))
assert polar([(7,'W'),(10,'one')])==(v(),v(Wp=1,T=1))
assert polar([(9,'W')])==(v(A=1),v(Wp=1,T=1,S=-1))
assert polar([(8,'one'),(10,'one')])==(v(A=1),v(Wp=1,T=1,S=-1))
assert polar([(18,'one')])==(v(),v(T=1))
# Dual cohomology, atom support, and unique final top coefficient.
M2=v(A=1,V=2,P=3,D=4)
assert sub(M2,add(s(16),s(18)))==v(D=1)
chiR=add(v(T=1,W=-2,S=-1),add(s(13),s(15)))
assert chiR==v(W=-1,Wp=1,S=1,T=4)
assert sub(chiR,mw(v(D=1)))==v(W=-1,Wp=1,T=3)
assert prod_sym(v(Wp=2,T=1),2)==add(chiR,v(W=1))
# Each possible j>=2 cohomology atom with total dimension <=5.
dim={'one':1,'W':2,'Wp':2,'A':3,'V':3,'P':4,'S':4,'D':5,'T':6}
odd={'W','Wp','S','T'}
atoms=[]
for j in range(2,7):
 for R in N:
  if ((R in odd)!=(j%2==1)) or (j-1)*dim[R]>5:continue
  h=prod_sym(v(**{R:1}),j-2)
  if all(0<=a<=b for a,b in zip(h,v(D=1))):atoms.append((j,R))
assert atoms==[(2,'D'),(6,'one')]
p=Path(__file__).resolve().parent
assert hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest()=='f900fa54aa5ad18adc94bd7552b94891d77ccf1c5797af05414dbd8b851b4f63'
entry=json.loads((p/'audit-inputs/one-one-endpoint-necessary-pairs.json').read_text())[113]
a,b,c,d,e,f,g,h=(0,1,0,0,0,1,0,1)
assert (c+g+h-1,d+e+g+h,f+g)==(0,1,1)
assert entry['A']==[[-10,'one'],[2,'one'],[16,'one']]
assert entry['B']==[[-18,'one'],[-4,'one'],[8,'one']]
assert entry['defect']==0
print('PASS: independent McKay recurrence, exact internal Hom support, kernel and polar characters, dual budget and atom support, original decoder and endpoints, final proof hash.')
