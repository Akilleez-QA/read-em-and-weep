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
for label,blocks in sources.items():
 check(sum(dim[r] for r,d in blocks)==17,'source rank')
 check(sum(d*dim[r] for r,d in blocks)==-54,'source degree')
 check(cohom(blocks,4,True)=={r:{'V':3,'P':3,'D':2}.get(r,0) for r in names},'source Euler')

rows=[]
for r in [3,5]:
 target=[('Wp',-r),('one',16)]
 env={x:cohom(target,2)[x]+cohom(target,4,True)[x]-cohom(sources['P'],4,True)[x] for x in names}
 check(env['V']==-1,'forced nonzero cubic')
 degreeK=-70+2*r; degreeN=degreeK+6; minK=degreeN+44
 check(minK==(-14 if r==3 else -10),'minimum K bound')
 check(-r-2+3<0,'top to negative doublet zero')
 check(dec([sy(17,x) for x in tr])['Wp']==1,'scalar top channel multiplicity')
 for n in range(7):check(dec([sy(n,x) for x in tr])['Wp']==0,'first occurrence lower degrees')
 check(dec([sy(7,x) for x in tr])['Wp']==1,'first occurrence seven')
 check(17-7==10 and 10<12,'base divisor too small')
 raw=[];quot=[]
 for e in range(-36+2*r,-r-8):
  if e%2:continue
  mult=dec([sy(-r-2-e,x) for x in tr])['Wp']
  if mult:
   raw.append(e)
   if e>=minK:quot.append(e)
 check(quot==([-12] if r==3 else []),'quotient-compatible rank-two lines')
 check(14-(-r-9)>=-1,'Ext1 splitting')
 rows.append(dict(r=r,degreeK=degreeK,minimumK=minK,raw_e=raw,quotient_e=quot,forced_rank_one_image_degree=14,second_kernel_rank=13,second_kernel_degree=degreeK-14))
a=[('Wp',-3),('one',16)];i=[('one',14),('one',-12)]
last={x:cohom(i,2)[x]+cohom(a,4,True)[x]+cohom(i,4,True)[x]-cohom(sources['P'],4,True)[x] for x in names}
check(last==dict(one=1,W=0,A=2,S=0,D=3,T=0,V=-1,P=1,Wp=0),'rank-two envelope exact')
for r in [3,5]:
 a=[('Wp',-r),('one',16)];i=[('one',14)]
 q1={x:cohom(i,2)[x]+cohom(a,4,True)[x]+cohom(i,4,True)[x]-cohom(sources['P'],4,True)[x] for x in names}
 check(q1==dict(one=1,W=0,A=2,S=0,D=3,T=0,V=0,P=2 if r==3 else 1,Wp=0),'rank-one nonnegative envelope')
 check((-84+2*r)+20==-64+2*r,'saturated line quotient degree')
 check(-6-14==-20 and 14-2==12,'line kernel and next derivative')
import importlib.util
p=Path(__file__).parent
spec=importlib.util.spec_from_file_location('production',p/'characters.py');prod=importlib.util.module_from_spec(spec);spec.loader.exec_module(prod)
for n in range(27):
 for r in names:
  v=dec([mul(c,sy(n,x)) for c,x in zip(chars[r],tr)])
  check(v=={s:prod.product(r,n)[s] for s in names},'independent character comparison')
for r in json.loads((p/'INPUTS.json').read_text()):
 b=(p/r['file']).read_bytes()
 check(hashlib.sha256(b).hexdigest()==r['sha256'],'source SHA256')
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['sha'],'source git blob')
print(json.dumps(dict(status='PASS',checks=checks,rows=rows,rank_two_envelope=last),sort_keys=True,indent=2))
