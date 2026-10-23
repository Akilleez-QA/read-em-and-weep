from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
checks=0
def require(c,msg):
 global checks
 checks+=1
 if not c:raise RuntimeError(msg)
NAMES=('one','W','A','S','D','T','V','P','Wp')
DIM=dict(zip(NAMES,(1,2,3,4,5,6,3,4,2)))
ADJ={'one':['W'],'W':['one','A'],'A':['W','S'],'S':['A','D'],'D':['S','T'],'T':['D','V','P'],'V':['T'],'P':['T','Wp'],'Wp':['P']}
def q(a,b=0):return F(a),F(b)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(a,b):return a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,b):return a*b[0],a*b[1]
def minus(a,b):return plus(a,scale(-1,b))
def sy(n,x):
 a,b=q(1),x
 if n==0:return a
 for _ in range(2,n+1):a,b=b,minus(times(x,b),a)
 return b
tr=[q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0)]
chars={r:[sy(n,x) for x in tr] for r,n in [('one',0),('W',1),('A',2),('S',3),('D',4),('T',5)]}
chars['P']=[q(x) for x in (4,4,-1,-1,-1,-1,1,1,0)]
chars['V']=[minus(sy(6,x),p) for x,p in zip(tr,chars['P'])]
chars['Wp']=[minus(times(x,p),t) for x,p,t in zip(tr,chars['P'],chars['T'])]
for r in NAMES:
 for i in range(9):
  rhs=q(0)
  for s in ADJ[r]:rhs=plus(rhs,chars[s][i])
  require(times(tr[i],chars[r][i])==rhs,'W tensor '+r)
def W(v):
 out=Counter()
 for r,n in v.items():
  for s in ADJ[r]:out[s]+=n
 return out
@lru_cache(None)
def product(R,n):
 if n<0:return Counter()
 if n==0:return Counter({R:1})
 if n==1:return W(product(R,0))
 out=W(product(R,n-1));out.subtract(product(R,n-2))
 if any(v<0 for v in out.values()):raise RuntimeError('nongenuine symmetric power product')
 return +out
def h0(blocks,t):
 out=Counter()
 for e,r in blocks:out.update(product(r,e+t))
 return out
def visible(A):
 c=h0(A,3)
 return c['Wp']>=1 and c['T']>=1,c
