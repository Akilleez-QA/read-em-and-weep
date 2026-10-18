from itertools import product,combinations
from fractions import Fraction as F
from collections import defaultdict
import json
from pathlib import Path
AX=(1,2,3,4)
def cur(t,a): return f'{t}{a}'
def jet(t,a,b): return t+''.join(map(str,sorted((a,b))))
def key(pair,out): return (tuple(sorted(pair)),out)
def add(p,k,c):
 p[k]+=c
 if not p[k]: del p[k]
def term(p,x,y,z,c=1): add(p,key((x,y),z),F(c))
def desc(k): return f'd({k[0][0]},{k[0][1]}) {k[1]}'
# Target is N = 8 M2. Cubic fluxes below have corresponding normalization.
b=defaultdict(F)
for a,bb,c,d,e in [(1,3,2,4,1),(1,4,2,3,-1),(2,3,1,4,-1),(2,4,1,3,1)]:
 h=jet('H',c,d); j=jet('J',a,bb)
 # a_ab = d(L_a,U_b)+d(U_a,L_b)+d(U_a,U_b)
 for x,y in [('L','U'),('U','L'),('U','U')]: term(b,cur(x,a),cur(y,bb),h,e)
 # b_cd = d(L_c,L_d)+d(L_c,U_d)+d(U_c,L_d)
 for x,y in [('L','L'),('L','U'),('U','L')]: term(b,cur(x,c),cur(y,d),j,e)
 term(b,cur('U',a),h,cur('L',bb),-e)
 term(b,cur('U',bb),h,cur('U',a),e)
 for t in 'LU':term(b,cur(t,a),h,cur('U',bb),-e)
 term(b,j,cur('L',c),cur('U',d),-e)
 term(b,j,cur('L',d),cur('U',c),-e)
cols=[]; labels=[]
for a in AX:
 rest=[i for i in AX if i!=a]
 for ts in product('LU',repeat=3):
  vs=[cur(t,i) for t,i in zip(ts,rest)]
  for o in range(3):
   pair=[vs[i] for i in range(3) if i!=o]; out=vs[o]
   col=defaultdict(F)
   for pos,v in enumerate(pair+[out]):
    vals=pair+[out]; vals[pos]=jet('H' if v[0]=='L' else 'J',a,int(v[1]))
    term(col,*vals)
   cols.append(col); labels.append((a,key(pair,out)))
rows=sorted(set(b).union(*(set(c) for c in cols)))
# Gaussian elimination over Q, retaining every equation's row combination.
pivots={}; certificate=None
for i,k in enumerate(rows):
 r={j:c[k] for j,c in enumerate(cols) if k in c}; rhs=b[k]; w={i:F(1)}
 while r:
  p=min(r)
  if p not in pivots:
   v=r[p]; r={j:x/v for j,x in r.items()}; rhs/=v; w={j:x/v for j,x in w.items()}
   pivots[p]=(r,rhs,w); break
  rr,rb,rw=pivots[p]; v=r[p]
  for j,x in rr.items():
   r[j]=r.get(j,0)-v*x
   if not r[j]:del r[j]
  rhs-=v*rb
  for j,x in rw.items():
   w[j]=w.get(j,0)-v*x
   if not w[j]:del w[j]
 else:
  if rhs and certificate is None: certificate=(w,rhs)
print('columns',len(cols),'rows',len(rows),'rank',len(pivots))
if certificate:
 w,rhs=certificate
 print('INCONSISTENT; certificate support',len(w),'pairing N',rhs,'pairing M2',rhs/8)
 for i,v in w.items():print(v,desc(rows[i]),'target',b[rows[i]])
 for c in cols:
  if sum(v*c.get(rows[i],0) for i,v in w.items()): raise RuntimeError('Certificate does not annihilate column')
 if sum(v*b.get(rows[i],0) for i,v in w.items())!=rhs:raise RuntimeError('Target mismatch')
 with open(Path(__file__).with_name('certificate.json'),'w') as f:
  json.dump({'normalization':'N=8 M2','rows':[{'pair':rows[i][0],'out':rows[i][1],'weight':str(v),'target':str(b[rows[i]])} for i,v in w.items()],'pairing':str(rhs),'columns':len(cols),'row_count':len(rows),'rank':len(pivots)},f,indent=2)
else: print('CONSISTENT')
if certificate:
 print('\nNonzero column incidences in certificate support:')
 for a,c in enumerate(cols):
  incidence=[(i,v*c.get(rows[i],0)) for i,v in w.items() if c.get(rows[i],0)]
  if incidence:
   print('V'+str(labels[a][0]),desc(labels[a][1]),':', '; '.join(f'{str(v)} [{desc(rows[i])}]' for i,v in incidence))
