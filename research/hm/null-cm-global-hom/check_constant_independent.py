"""Independent integer row elimination of fixed formal coefficient equations."""
import json,hashlib,math,functools
from pathlib import Path
P=Path(__file__).resolve().parent
b=(P/'model.json').read_bytes()
def need(ok,msg):
 if not ok:raise RuntimeError(msg)
need(hashlib.sha256(b).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926','model pin')
g=json.loads(b)['gamma'];need(len(g)==15 and all(len(r)==5 for r in g),'shape')
def degree(key):
 e=list(map(int,key.split(',')));need(len(e)==4 and min(e)>=0 and sum(e)<=1,'affine linear')
 return sum((i+1)*a for i,a in enumerate(e))
def equations(cm):
 # Independently assemble each left and right coefficient by output location.
 a=[[0]*250 for _ in range(375)]
 for r in range(15):
  for c in range(5):
   for k in range(15):
    for key,value in g[k][c]:a[degree(key)*75+r*5+c][r*15+k]+=value
   for k in range(5):
    for key,value in g[r][k]:
     j=degree(key);a[j*75+r*5+c][225+k*5+c]-=value*((-1)**j if cm else 1)
 return a
def integer_rank(a):
 # Fraction-free row replacement with gcd normalization after each operation.
 rank=0
 for c in range(250):
  q=next((q for q in range(rank,len(a)) if a[q][c]),None)
  if q is None:continue
  a[rank],a[q]=a[q],a[rank];pivot=a[rank][c]
  for r in range(rank+1,len(a)):
   if not a[r][c]:continue
   value=a[r][c];d=math.gcd(pivot,value);u=pivot//d;v=value//d
   a[r]=[u*x-v*y for x,y in zip(a[r],a[rank])]
   norm=functools.reduce(math.gcd,a[r],0)
   if norm:a[r]=[x//norm for x in a[r]]
  rank+=1
 return rank
cm=equations(True);identity=equations(False)
# Identity has the explicitly known simultaneous pair (I15,I5).
indices=[i*16 for i in range(15)]+[225+i*6 for i in range(5)]
need(all(sum(r[i] for i in indices)==0 for r in identity),'identity intertwiner control')
need(any(sum(r[i] for i in indices)!=0 for r in cm),'CM excludes identity control')
rank=integer_rank(cm);identityrank=integer_rank(identity)
need(rank==250,'CM full column rank');need(identityrank<250,'identity nonzero kernel')
# Independently replay the author's selected-row exact pivot certificate.
from fractions import Fraction
certificate=json.loads((P/'constant-gamma-elimination.json').read_text())
raw=equations(True);basis={}
for step in certificate['pivot_steps']:
 row={c:Fraction(x) for c,x in enumerate(raw[step['equation']]) if x}
 for col,scale_text in step['eliminations']:
  scale=Fraction(scale_text)
  need(col in basis and row and min(row)==col and row[col]==scale,'certificate elimination')
  for c,value in basis[col].items():
   row[c]=row.get(c,0)-scale*value
   if not row[c]:del row[c]
 col=step['pivot'];scale=Fraction(step['normalizer'])
 need(col not in basis and row and min(row)==col and row[col]==scale,'certificate pivot')
 basis[col]={c:value/scale for c,value in row.items()}
need(sorted(basis)==list(range(250)),'certificate full coverage')
print(json.dumps({'status':'pass','equations':375,'unknowns':250,'cm_exact_integer_rank':rank,'cm_nullity':250-rank,'identity_rank':identityrank,'identity_pair_verified':True,'author_certificate_independently_replayed':True,'method':'independent dense integer fraction-free elimination with gcd normalization','physical_source_evaluated':False,'matrix_polynomial_products':False},indent=2))
