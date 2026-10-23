#!/usr/bin/env python3
"""Bounded universal character audit. No actual source, coefficients, or points."""
from functools import lru_cache
N=('one','W','Wp','A','V','P','S','D','T')
dim=(1,2,2,3,3,4,4,5,6)
def ch(**kw):return tuple(kw.get(n,0)for n in N)
Z=ch()
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def times(k,x):return tuple(k*a for a in x)
TW={
'one':ch(W=1),'W':ch(one=1,A=1),'Wp':ch(P=1),
'A':ch(W=1,S=1),'V':ch(T=1),'P':ch(Wp=1,T=1),
'S':ch(A=1,D=1),'D':ch(S=1,T=1),'T':ch(D=1,V=1,P=1)}
def Wmul(x):
 y=Z
 for n,a in zip(N,x):y=add(y,times(a,TW[n]))
 return y
@lru_cache(None)
def prod_sym(x,n):
 assert n>=0
 if n==0:return x
 if n==1:return Wmul(x)
 return sub(Wmul(prod_sym(x,n-1)),prod_sym(x,n-2))
def sym(n):return prod_sym(ch(one=1),n)
assert all(sum(a*d for a,d in zip(TW[n],dim))==2*dim[i]for i,n in enumerate(N))
assert sym(7)==ch(Wp=1,T=1)
assert sym(8)==ch(P=1,D=1)
assert sym(9)==ch(S=1,T=1)
assert sym(10)==ch(A=1,V=1,D=1)
assert sym(12)==ch(one=1,A=1,P=1,D=1)
assert sym(14)==ch(A=1,V=1,P=1,D=1)
assert sym(18)==ch(A=1,V=1,P=2,D=1)
assert sym(20)==ch(one=1,A=1,V=1,P=1,D=2)
assert sym(28)==ch(A=1,V=1,P=2,D=3)
assert sym(29)==ch(W=1,Wp=1,S=2,T=3)
R=ch(P=1,D=2);B=sub(sym(28),R);c3=sub(Wmul(R),sym(29))
assert B==ch(A=1,V=1,P=1,D=1) and c3==ch(W=-1)
parity={n:0 if n in ('one','A','V','P','D')else 1 for n in N}
rows=[]
for j in range(4,19):
 for n in N:
  if parity[n]!=j%2:continue
  h2=prod_sym(ch(**{n:1}),j-4)
  assert all(x>=0 for x in h2)
  if not all(x<=y for x,y in zip(h2,B)):continue
  h3=Z if j==4 else prod_sym(ch(**{n:1}),j-5)
  rows.append((j,n,h2,h3))
assert [(j,n)for j,n,_,_ in rows if j>=10]==[(10,'one'),(12,'one'),(14,'one'),(18,'one')]
assert [(j,n)for j,n,_,h3 in rows if h3[N.index('W')]]==[(6,'one'),(7,'W'),(8,'A'),(18,'one')]
solutions=[]
def visit(i,rem,h3,parts):
 if i==len(rows):
  if any(rem):return
  r3=add(c3,h3)
  if min(r3)<0:return
  assert all(not a or parity[n]==1 for n,a in zip(N,r3))
  sol=tuple([(3,n,a)for n,a in zip(N,r3)if a]+parts)
  assert sum(a*dim[N.index(n)] for j,n,a in sol)==13
  assert sum(-j*a*dim[N.index(n)]for j,n,a in sol)==-54
  solutions.append(sol);return
 j,n,x,y=rows[i]
 for a in range(1+min(u//v for u,v in zip(rem,x)if v)):
  visit(i+1,sub(rem,times(a,x)),add(h3,times(a,y)),parts+([(j,n,a)]if a else []))
visit(0,B,Z,[])
assert len(solutions)==18
with_tail=[s for s in solutions if any(j>=10 for j,_,_ in s)]
expected=[
 ((3,'S',1),(3,'T',1),(7,'W',1),(10,'one',1)),
 ((3,'S',1),(3,'T',1),(6,'one',1),(8,'one',1),(10,'one',1)),
 ((3,'T',1),(4,'D',1),(6,'one',1),(10,'one',1)),
 ((3,'Wp',1),(3,'T',1),(4,'V',1),(6,'one',1),(12,'one',1)),
 ((3,'Wp',1),(3,'S',1),(3,'T',1),(18,'one',1))]
assert set(with_tail)==set(expected)
def hom(j,U,k,V):
 return 0 if j<k else prod_sym(ch(**{V:1}),j-k)[N.index(U)]
for s in solutions:
 for target in [[(10,'one',2),(12,'one',1)],[(10,'one',1),(11,'W',1)]]:
  channels=[(j,U,k,V,a*b*hom(j,U,k,V))for j,U,a in s for k,V,b in target if hom(j,U,k,V)]
  assert all((j,U,k,V)in [(10,'one',10,'one'),(12,'one',12,'one'),(12,'one',11,'W')]for j,U,k,V,_ in channels)
for j,C,L in [(10,ch(A=1,D=1),ch(Wp=1,T=1)),(12,ch(A=1,V=1),ch(S=1,T=1))]:
 assert sub(B,sym(j-4))==C
 assert sub(sym(29),sym(j-5))==add(Wmul(C),L)
assert hom(2,'D',1,'Wp')==0 and hom(2,'D',1,'T')==1
assert hom(2,'D',0,'A')==1 and hom(2,'D',0,'D')==1
assert [(U,V,hom(2,U,1,V))for U in ['P','D']for V in ['S','T']]==[('P','S',0),('P','T',1),('D','S',1),('D','T',1)]
assert sym(18)[0]==0 and sym(20)[0]==1
print('PASS: all 18 small kernel supports; five tail configurations; exact internal Hom channels; both first-polar splittings; invariant obstruction.')
