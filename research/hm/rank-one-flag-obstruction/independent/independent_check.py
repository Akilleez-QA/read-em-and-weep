#!/usr/bin/env python3
"""Independent exact universal character/degree controls. No actual instance."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json, hashlib
checks=0
def check(c,m):
 global checks
 checks+=1
 if not c: raise RuntimeError(m)
def q(a=0,b=0):return (F(a),F(b))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(n,x):return (n*x[0],n*x[1])
def mul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,n):
 r=q(1)
 for _ in range(n):r=mul(r,x)
 return r
def sy(n,x):
 r=q()
 for k in range(n//2+1):r=add(r,scale((-1)**k*comb(n-k,k),power(x,n-2*k)))
 return r
tr=[q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q()]
sizes=[1,1,12,12,12,12,20,20,30]
names=['one','W','A','S','D','T','V','P','Wp']
chars={r:[sy(n,x) for x in tr] for n,r in enumerate(names[:6])}
chars['P']=[q(a) for a in [4,4,-1,-1,-1,-1,1,1,0]]
chars['V']=[add(sy(6,x),scale(-1,p)) for x,p in zip(tr,chars['P'])]
chars['Wp']=[add(mul(x,p),scale(-1,t)) for x,p,t in zip(tr,chars['P'],chars['T'])]
def inner(x,y):
 z=q()
 for s,a,b in zip(sizes,x,y):z=add(z,scale(F(s,120),mul(a,b)))
 return z
for r in names:
 for s in names:check(inner(chars[r],chars[s])==q(int(r==s)), 'orthogonality '+r+s)
def dec(c):
 out={}
 for r in names:
  a,b=inner(c,chars[r]);check(b==0 and a.denominator==1,'integrality')
  out[r]=int(a)
 return out
def cohom(blocks,twist,euler=False):
 v=[q()]*9
 for r,d in blocks:
  n=d+twist
  if n>=0: sign=1
  elif euler and n<=-2:n=-n-2;sign=-1
  else:continue
  v=[add(a,scale(sign,mul(c,sy(n,x)))) for a,c,x in zip(v,chars[r],tr)]
 return dec(v)
sources={
 'D':[('D',-2),('Wp',-3),('T',-3),('V',-4),('one',-8)],
 'P':[('P',-2),('Wp',-3),('T',-3),('V',-4),('Wp',-5)],
 'V':[('V',-2),('Wp',-3),('T',-3),('V',-4),('V',-4)],
 'Z':[('Wp',-3),('T',-3),('T',-3),('V',-4)]}
dim={r:int(chars[r][0][0]) for r in names}

def vecsum(*vs):return {r:sum(v[r] for v in vs) for r in names}
def neg(v):return {r:-v[r] for r in names}
def sparse(v):return {r:v[r] for r in names if v[r]}
result={}
for r in [3,5]:
 target=[('Wp',-r),('one',16)]
 total=84-2*r
 semigroup=sorted({12*a+20*b+30*c+60*d for a in range(8) for b in range(5) for c in range(3) for d in range(2) if 12*a+20*b+30*c+60*d<=total})
 patterns=[]
 def rec(j,left,ds):
  if j==13:
   if left==0:patterns.append(ds)
   return
  for d in semigroup:
   cost=(13-j)*d
   if cost<=left:rec(j+1,left-cost,ds+[d])
 rec(0,total,[])
 expected=5 if r==3 else 2
 check(len(patterns)==expected,'complete deficit patterns')
 rows=[]
 for ds in patterns:
  bs=[14]
  for d in ds:bs.append(bs[-1]-2-d)
  check(sum(bs)==-70+2*r,'degree')
  check(all(d==0 for d in ds[:7]),'first seven zero')
  residual=vecsum(cohom(sources['P'],0,True),neg(cohom(target,0,True)),neg(cohom([('one',b) for b in bs],0,True)))
  check(any(residual.values()),'full flag contradiction')
  rows.append({'deficits':{str(j):d for j,d in enumerate(ds) if d},'degrees':bs,'residual':sparse(residual)})
 env=vecsum(cohom([('one',0)],10),cohom(target,10,True),cohom([('one',14-2*j) for j in range(7)],10,True),neg(cohom(sources['P'],10,True)))
 check(env['one']==(-1 if r==5 else 0),'F7 trivial coefficient')
 cubic=vecsum(cohom(target,2),cohom(target,4,True),neg(cohom(sources['P'],4,True)))
 check(cubic['V']==-1,'cubic zero impossible')
 result[str(r)]={'patterns':rows,'F7_envelope':sparse(env),'cubic_zero_envelope':sparse(cubic)}
check(cohom([('one',14)],0)['one']==0,'no invariant degree14')
for source in sources.values():check(cohom(source,4,True)==cohom(sources['P'],4,True),'common quartic Euler')
print(json.dumps({'method':'closed binomial SU2 characters in Q(sqrt5), class weighted inner products; independent divisor semigroup DFS','checks':checks,'results':result},sort_keys=True,indent=2))
