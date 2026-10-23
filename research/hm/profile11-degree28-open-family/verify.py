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
expected={16:ch(V=1,P=1,D=2),24:ch(one=1,A=1,V=1,P=2,D=2),26:ch(A=1,V=2,P=2,D=2),27:ch(Wp=1,S=2,T=3),28:ch(A=1,V=1,P=2,D=3),29:ch(W=1,Wp=1,S=2,T=3)}
for n,x in expected.items():assert sym(n)==x
assert sym(24)[N.index('one')]==1 and sym(26)[N.index('one')]==0
assert sym(27)[N.index('Wp')]==sym(29)[N.index('Wp')]==1
assert TW['P']==ch(Wp=1,T=1) and TW['V']==ch(T=1)
assert prod_sym(ch(Wp=1),2)==ch(T=1)
C=ch(A=1,V=1,P=1,D=1);U=ch(P=1,D=2);H=times(2,C)
assert sub(sym(28),C)==U and Wmul(C)==sym(29)
# H1(E), H1(E(-1)), and H1(E(-2))-H, respectively.
N4=add(add(U,sym(6)),Wmul(sym(7)))
N3=add(add(Wmul(U),sym(7)),Wmul(sym(8)))
N2=sub(add(add(prod_sym(U,2),sym(8)),Wmul(sym(9))),H)
assert N2==ch(A=1,V=2,P=3,D=4)
assert N3==ch(Wp=3,S=3,T=6)
assert N4==ch(V=2,P=4,D=3)
assert tuple(sum(a*d for a,d in zip(x,dim)) for x in (N2,N3,N4))==(41,54,37)
print('PASS: universal degree28 multiplicities, Euler channels, and pencil characters.')
print('Scope: no chosen point of the parameter family or actual-source evaluation.')
