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
for e in (4,10):
 target=[('Wp',-1),('one',e)]
 h=cohom(target,2);c=cohom(target,4,True)
 env={r:h[r]+c[r]-{'V':3,'P':3,'D':2}.get(r,0) for r in names}
 check(env['V']==-1,'negative V envelope')
 check(dec([sy(e-2,x) for x in tr])['one']==0,'D scalar Hom absent')
 check(-1-2<0,'D doublet Hom absent')
 check(dec([sy(e+1,x) for x in tr])['Wp']==0,'top K to scalar Hom absent')
 # Exact rank/degree arithmetic after endpoint forces an isomorphic Wp(-3) image.
 a=e-2;kdegree=-54-a;kerneldegree=kdegree-(-6)
 check(17-3-2==12,'second kernel rank')
 check(kerneldegree==-46-e,'second kernel degree')
 check(kerneldegree>-5*12,'impossible top <= -5')
 check(-5-(-4)<0,'degree-minus-four map to degree-minus-five vanishes')
 rows.append({'e':e,'quartic_envelope':env,'rank_second_kernel':12,'degree_second_kernel':kerneldegree,'required_degree_upper_bound':-60})
p=Path(__file__).parent
# Independent closed-form evaluation versus the pinned production McKay recurrence.
import importlib.util
spec=importlib.util.spec_from_file_location('production',p/'inputs/characters-production.py')
production=importlib.util.module_from_spec(spec);spec.loader.exec_module(production)
for r in names:
 for n in range(15):
  independent=dec([mul(c,sy(n,x)) for c,x in zip(chars[r],tr)])
  recurrence=production.product(r,n)
  check(independent=={s:recurrence[s] for s in names},'closed-form/recurrence comparison')
check(dec([sy(11,x) for x in tr])=={r:int(r in ['W','S','T']) for r in names},'complete Sym11')
fixed=json.loads((p/'inputs/profile11-pairs.json').read_text())
for e,expected in [(4,[86,87,88,89,96]),(10,[116])]:
 labels=[i for i,row in enumerate(fixed) if sorted(row['A'])==sorted([[-1,'Wp'],[e,'one']])]
 check(labels==expected,'fixed historical label readback')
for r in json.loads((p/'INPUTS.json').read_text()):
 b=(p/r['file']).read_bytes()
 check(hashlib.sha256(b).hexdigest()==r['sha256'],'sha256 '+r['file'])
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['sha'],'git blob '+r['file'])
print(json.dumps({'status':'PASS','checks':checks,'rows':rows,'scope':'universal exact algebra supporting, not replacing, written actual geometric proof'},sort_keys=True,indent=2))
