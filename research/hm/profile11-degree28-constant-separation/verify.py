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
expected={
 7:ch(Wp=1,T=1),8:ch(P=1,D=1),9:ch(S=1,T=1),
 10:ch(A=1,V=1,D=1),16:ch(V=1,P=1,D=2),
 26:ch(A=1,V=2,P=2,D=2),27:ch(Wp=1,S=2,T=3),
 28:ch(A=1,V=1,P=2,D=3),29:ch(W=1,Wp=1,S=2,T=3)}
for n,x in expected.items():assert sym(n)==x
assert sym(4)[N.index('V')]==0
assert sym(22)[N.index('one')]==0
assert sym(36)[N.index('one')]==1
assert sym(37)[N.index('W')]==1
assert sym(16)[N.index('V')]==sym(28)[N.index('V')]==1
C=ch(A=1,V=1,P=1,D=1)
assert Wmul(C)==sym(29)
assert TW['P']==ch(Wp=1,T=1)
assert TW['Wp']==ch(P=1)
assert all(TW[n][N.index('Wp')]==(n=='P') for n in ('A','V','P','D'))
M2=ch(A=1,V=2,P=3,D=4)
M3=ch(Wp=3,S=3,T=6)
M4=ch(V=2,P=4,D=3)
assert sub(sub(Wmul(M3),M2),M4)==times(2,C)
block=(sym(26),sym(27),ch(P=1,D=2))
remaining=(ch(P=1,D=2),ch(Wp=2,S=1,T=3),ch(V=2,P=3,D=1))
for m,b,r in zip((M2,M3,M4),block,remaining):assert sub(m,b)==r
assert tuple(sum(a*d for a,d in zip(x,dim)) for x in block)==(27,28,14)
assert tuple(sum(a*d for a,d in zip(x,dim)) for x in remaining)==(14,26,23)
print('PASS: declared universal character identities and summand dimensions.')
print('Scope: no actual source coefficients, points, derivatives, matrices, ranks, or envelope.')
