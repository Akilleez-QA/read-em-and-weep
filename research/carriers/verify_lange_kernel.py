"""Exact cohomological check only; does not compute Ext or an Atiyah obstruction."""
from fractions import Fraction as Q
from itertools import combinations
import sympy as s
# e0,...,e3 holomorphic; e4,...,e7 antiholomorphic.
def add(a,b,k=1):
 r=a.copy()
 for w,v in b.items():
  r[w]=r.get(w,0)+k*v
  if not r[w]:del r[w]
 return r
def wedge(a,b):
 r={}
 for u,x in a.items():
  for v,y in b.items():
   if set(u)&set(v):continue
   sign=(-1)**sum(i>j for i in u for j in v)
   w=tuple(sorted(u+v));r[w]=r.get(w,0)+sign*x*y
 return {w:v for w,v in r.items() if v}
def con(a,i):
 return {w[:w.index(i)]+w[w.index(i)+1:]:v*(-1)**w.index(i) for w,v in a.items() if i in w}
def scale(a,k):return {w:k*v for w,v in a.items() if k*v}
def biv(a,i,j):return con(con(a,i),j)
def kap(a,i,j):return wedge({(4+j,):1},con(a,i))
theta={(i,4+i):1 for i in range(4)}
t2=wedge(theta,theta);t4=wedge(t2,t2)
d=8 # m=2 explicit product seed
ch=add(add({():2},t2,-d),t4,Q(d*d,12))
cols=[];labels=[]
for i,j in combinations(range(4),2):
 cols.append(wedge({(4+i,4+j):1},ch));labels.append(('eta',i,j))
for i in range(4):
 for j in range(4):cols.append(kap(ch,i,j));labels.append(('kappa',i,j))
for i,j in combinations(range(4),2):cols.append(biv(ch,i,j));labels.append(('pi',i,j))
words=[w for n in range(9) for w in combinations(range(8),n)]
M=s.Matrix([[c.get(w,0) for c in cols] for w in words])
assert M.rank()==12 and len(M.nullspace())==16
# Six compensated bivectors; seven product-polarized directions.
known=[]
for i,j in combinations(range(4),2):
 pi=scale(biv(t2,i,j),Q(1,2))
 z=add(biv(ch,i,j),wedge(pi,ch),d)
 assert not z
 v=s.zeros(28,1);v[labels.index(('pi',i,j))]=1
 for (a,b),n in pi.items():v[labels.index(('eta',a-4,b-4))]=d*n
 known.append(v)
for i in range(4):
 v=s.zeros(28,1);v[labels.index(('kappa',i,i))]=1;known.append(v)
for i,j in combinations(range(1,4),2):
 v=s.zeros(28,1);v[labels.index(('kappa',i,j))]=1;v[labels.index(('kappa',j,i))]=1;known.append(v)
K=s.Matrix.hstack(*known)
assert K.rank()==13 and M*K==s.zeros(256,13)
for j in range(1,4):
 v=s.zeros(28,1);v[labels.index(('kappa',0,j))]=1;v[labels.index(('kappa',j,0))]=1;known.append(v)
assert s.Matrix.hstack(*known).rank()==16
print('ch-action rank 12; annihilator dimension 16')
print('6 compensated bivectors + 7 product-polarized directions: independent dimension 13')
print('3 symmetric mixed kappa directions complete the annihilator')
print('No Ext evaluation or mixed Atiyah-class vanishing computed.')
