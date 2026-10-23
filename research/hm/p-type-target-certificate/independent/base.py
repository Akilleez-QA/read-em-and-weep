"""Independent character-inner-product audit, not a geometric proof."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json, importlib.util, hashlib
ROOT=Path(__file__).resolve().parent
checks=0
def need(x):
 global checks
 checks+=1
 if not x: raise RuntimeError('independent check '+str(checks))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(n,a):return (n*a[0],n*a[1])
def sub(a,b):return add(a,scale(-1,b))
z=(F(0),F(0));one=(F(1),F(0))
tr=[(F(2),F(0)),(F(-2),F(0)),(F(1,2),F(1,2)),(F(-1,2),F(-1,2)),(F(1,2),F(-1,2)),(F(-1,2),F(1,2)),one,(-one[0],one[1]),z]
sizes=[1,1,12,12,12,12,20,20,30]
sym=[[one]*9,tr]
for n in range(2,41):sym.append([sub(mul(x,a),b) for x,a,b in zip(tr,sym[-1],sym[-2])])
chars=dict(zip(['one','W','A','S','D','T'],sym[:6]))
chars['P']=[(F(x),F(0)) for x in [4,4,-1,-1,-1,-1,1,1,0]]
chars['V']=[sub(a,b) for a,b in zip(sym[6],chars['P'])]
chars['Wp']=[sub(mul(a,b),c) for a,b,c in zip(tr,chars['P'],sym[5])]
def inner(a,b):
 t=z
 for n,x,y in zip(sizes,a,b):t=add(t,scale(F(n,120),mul(x,y)))
 return t
for a,x in chars.items():
 for b,y in chars.items():need(inner(x,y)==(F(a==b),F(0)))
def decompose(c):
 out=Counter()
 for r,x in chars.items():
  a,b=inner(c,x);need(b==0 and a.denominator==1)
  if a:out[r]=int(a)
 return out
def product(r,n):return Counter() if n<0 else decompose([mul(a,b) for a,b in zip(chars[r],sym[n])])
def h0(blocks,t):
 out=Counter()
 for e,r in blocks:out.update(product(r,e+t))
 return out
def chi(blocks,t):
 out=h0(blocks,t)
 for e,r in blocks:out.subtract(product(r,-e-t-2))
 return out

