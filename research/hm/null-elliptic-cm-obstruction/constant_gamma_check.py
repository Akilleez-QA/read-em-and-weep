"""Solve ONLY the authorized fixed constant-coefficient intertwiner equations.
Reads monomial positions; no source execution or coordinate/matrix values.
"""
import json,hashlib
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parent
p=root/'model.json'
def need(b,m):
 if not b:raise RuntimeError(m)
need(hashlib.sha256(p.read_bytes()).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926','pin')
gamma=json.loads(p.read_text())['gamma']
# slots[j] stores (row,column,coefficient) of v_j, j=0..4.
slots=[[] for _ in range(5)]
for r,row in enumerate(gamma):
 for c,terms in enumerate(row):
  for key,k in terms:
   e=tuple(map(int,key.split(',')))
   need(sum(e)<=1,'linear gamma required')
   j=0 if sum(e)==0 else e.index(1)+1
   slots[j].append((r,c,k))
# Unknowns M[r,k]=15*r+k, N[k,c]=225+5*k+c.
# Coefficient(v_j, row r, col c): sum_k M[r,k] G_j[k,c]
#                                 -(-1)^j sum_k G_j[r,k] N[k,c].
rows=[];labels=[]
for j in range(5):
 for r in range(15):
  for c in range(5):
   d={}
   for a,b,k in slots[j]:
    if b==c:d[15*r+a]=d.get(15*r+a,F(0))+k
    if a==r:d[225+5*b+c]=d.get(225+5*b+c,F(0))-((-1)**j)*k
   rows.append({k:F(v) for k,v in d.items() if v});labels.append([j,r,c])
# Deterministic exact sparse forward elimination, normalization, no physical values.
pivots={};witness=[]
for index,row in enumerate(rows):
 a=dict(row);operations=[]
 while a:
  col=min(a);scale=a[col]
  if col not in pivots:
   pivots[col]={k:v/scale for k,v in a.items()};witness.append({'equation':index,'pivot':col,'normalizer':str(scale),'eliminations':operations});break
  operations.append([col,str(scale)])
  for k,v in pivots[col].items():
   a[k]=a.get(k,F(0))-scale*v
   if not a[k]:del a[k]
rank=len(pivots)
need(rank==250,'full constant-system rank')
# Positive control: identity coordinate action admits M=Id15, N=Id5.
for j in range(5):
 for r in range(15):
  for c in range(5):
   left=sum(k for a,b,k in slots[j] if b==c and a==r)
   right=sum(k for a,b,k in slots[j] if a==r and b==c)
   need(left==right,'identity-action positive control')
report={'unknowns':250,'coefficient_equations':len(rows),'rank':rank,'nullity':250-rank,'pivot_columns':sorted(pivots),'scope':'formal coefficient linear system only; no actual source/matrix evaluation','model_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(root/'constant-gamma-result.json').write_text(json.dumps(report,indent=2)+'\n')
(root/'constant-gamma-elimination.json').write_text(json.dumps({'equation_order':'j=0..4, r=0..14, c=0..4','unknown_order':'M row-major 225 then N row-major 25','pivot_steps':witness},indent=2)+'\n')
print(json.dumps(report,indent=2))
