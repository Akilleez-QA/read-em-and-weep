#!/usr/bin/env python3
"""Independent exact free-coordinate jet-symbol audit; Python standard library only."""
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json

def plus(*ps):
 r={}
 for p in ps:
  for m,c in p.items():
   r[m]=r.get(m,Q(0))+c
   if not r[m]: del r[m]
 return r

def scale(p,c): return {m:v*c for m,v in p.items() if v*c}
def mul(p,q):
 r={}
 for a,x in p.items():
  for b,y in q.items():
   m=tuple(sorted(a+b)); r[m]=r.get(m,Q(0))+x*y
 return {m:c for m,c in r.items() if c}
def vec(n): return [{(n+'.'+str(k),):Q(1)} for k in range(3)]
def vp(*xs): return [plus(*(x[k] for x in xs)) for k in range(3)]
def vs(x,c): return [scale(p,c) for p in x]
def dot(x,y): return plus(scale(mul(x[0],y[0]),2),mul(x[1],y[2]),mul(x[2],y[1]))
def sv(p,x): return [mul(p,q) for q in x]
def flat(x): return {(k,m):c for k,p in enumerate(x) for m,c in p.items()}
def jet(t,a,b):return t+''.join(str(i) for i in sorted((a,b)))
def basis(pair,out):return flat(sv(dot(vec(pair[0]),vec(pair[1])),vec(out)))
def leading_derivative(p,a):
 r={}
 for (k,m),c in p.items():
  for i,v in enumerate(m):
   n,coordinate=v.split('.')
   if n[0] not in 'LU':raise RuntimeError('Unexpected non-current flux')
   nv=jet('H' if n[0]=='L' else 'J',a,int(n[1]))+'.'+coordinate
   nm=tuple(sorted(m[:i]+(nv,)+m[i+1:])); key=(k,nm)
   r[key]=r.get(key,Q(0))+c
 return {m:c for m,c in r.items() if c}
def rank(vectors):
 piv={}
 for original in vectors:
  r=dict(original)
  while r:
   p=min(r); v=r[p]
   if p not in piv:
    piv[p]=scale(r,1/v);break
   r=plus(r,scale(piv[p],-v))
 return len(piv)
def require(ok,msg):
 if not ok:raise RuntimeError(msg)

# All symmetric off-diagonal jets and the two untouched axis currents.
rows=[]
for a,b in combinations(range(1,5),2):
 for jt in 'HJ':
  remaining=[i for i in range(1,5) if i not in (a,b)]
  for types in product('LU',repeat=2):
   inputs=[jet(jt,a,b)]+[t+str(i) for t,i in zip(types,remaining)]
   for o in range(3):rows.append((tuple(sorted(inputs[:o]+inputs[o+1:])),inputs[o]))
row_polys=[basis(*r) for r in rows]
require(len(rows)==144 and rank(row_polys)==144,'Rank-two row quotient is not faithful')

# Construct an exact coordinate-to-row decoder, retaining all basis combinations.
piv={}
for i,original in enumerate(row_polys):
 r=dict(original);w={i:Q(1)}
 while r:
  p=min(r);v=r[p]
  if p not in piv:
   piv[p]=(scale(r,1/v),scale(w,1/v));break
  rr,ww=piv[p];r=plus(r,scale(rr,-v));w=plus(w,scale(ww,-v))
 else:raise RuntimeError('Dependent invariant rows')
def decode(original):
 r=dict(original);w={}
 while r:
  p=min(r)
  require(p in piv,'Polynomial lies outside row span')
  rr,ww=piv[p];v=r[p];r=plus(r,scale(rr,-v));w=plus(w,scale(ww,v))
 return w

columns=[]
for a in range(1,5):
 rest=[i for i in range(1,5) if i!=a]
 for types in product('LU',repeat=3):
  names=[t+str(i) for t,i in zip(types,rest)]
  for o in range(3):
   columns.append(decode(leading_derivative(basis(names[:o]+names[o+1:],names[o]),a)))
require(len(columns)==96 and rank(columns)==94,'Unexpected derivative-image rank')

# Literal equation (8), independently formed as scalar-coordinate vector expressions.
N=[{}, {}, {}]
for a,b,c,d,e in ((1,3,2,4,1),(1,4,2,3,-1),(2,3,1,4,-1),(2,4,1,3,1)):
 L={i:vec('L'+str(i)) for i in range(1,5)}
 U={i:vec('U'+str(i)) for i in range(1,5)}
 T={i:vp(L[i],U[i]) for i in range(1,5)}
 H=vec(jet('H',c,d));J=vec(jet('J',a,b))
 aa=plus(dot(T[a],T[b]),scale(dot(L[a],L[b]),-1))
 bb=plus(dot(T[c],T[d]),scale(dot(U[c],U[d]),-1))
 piece=vp(sv(aa,H),sv(bb,J),vs(sv(dot(U[a],H),L[b]),-1),sv(dot(U[b],H),U[a]),vs(sv(dot(T[a],H),U[b]),-1),vs(sv(dot(J,L[c]),U[d]),-1),vs(sv(dot(J,L[d]),U[c]),-1))
 N=vp(N,vs(piece,e))
target=decode(flat(N))
cert=json.loads(Path(__file__).with_name('certificate.json').read_text())
w={}
for r in cert['rows']:
 idx=rows.index((tuple(sorted(r['pair'])),r['out']));w[idx]=Q(r['weight'])
 require(target.get(idx,0)==Q(r['target']),'Certificate target entry mismatch')
def pairing(c,weights=w):return sum(v*c.get(i,0) for i,v in weights.items())
require(all(pairing(c)==0 for c in columns),'Certificate failed a column')
require(pairing(target)==1,'Certificate failed N pairing')
require(rank(columns+[target])==95,'Augmented rank mismatch')
bad=dict(w); first=next(iter(bad));bad[first]=-bad[first]
require(any(pairing(c,bad)!=0 for c in columns),'Negative certificate control did not fail')
require(pairing({})!=1,'Omitted-target negative control did not fail')
print(json.dumps({'verdict':'PASS','row_embedding_rank':144,'columns':96,'image_rank':94,'augmented_rank':95,'certificate_support':len(w),'certificate_pairing_N':str(pairing(target)),'certificate_pairing_M2':str(pairing(target)/8),'negative_controls':['flipped certificate sign rejected','omitted target rejected'],'method':'formal scalar-coordinate coefficient expansion; no evaluation or matrix products'},indent=2))
