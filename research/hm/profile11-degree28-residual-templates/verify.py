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
assert sym(8)==ch(P=1,D=1)
assert sym(10)==ch(A=1,V=1,D=1)
assert TW['W']==ch(one=1,A=1)
assert TW['P']==ch(Wp=1,T=1)
assert sym(9)==ch(S=1,T=1)
assert sum(a*d for a,d in zip(ch(A=1,V=1),dim))==6
assert 4*(8-4+1)==20 < 12*(4-1)
assert 6*(10-6+1)==30 < 12*(6-2)
assert (2*(1-8),3*(2-10))==(-14,-24)
assert (-14-(-8),-24-(-18))==(-6,-6)
assert (-8)+2*(-9)==-26
print('PASS: universal residual coefficients, Euler channels and jet inequalities.')
print('Scope: no actual source evaluation, model experiment, scan or envelope.')
