"""Independent exact 32-weight enumeration, no weighted producer imports."""
from collections import Counter
from itertools import combinations,product
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
sraw=(HERE/'selection.json').read_bytes();wraw=(HERE/'weighted-requests.json').read_bytes()
def need(c,m):
 if not c:raise ValueError(m)
need(hashlib.sha256(sraw).hexdigest()=='54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d','selected byte binding')
s=json.loads(sraw);w=json.loads(wraw)
q=[(1,1,0,0),(0,0,1,1)]
def squarefree(k):return [tuple(int(i in a)for i in range(4))for a in combinations(range(4),k)]
def sums(a,b):return Counter(tuple(x+y for x,y in zip(u,v))for u,v in product(a,b))
expected=[]
for i,b in s['I20']:expected.append((i,b,'Q^2',[],sums(q,q)))
for lab in s['selected']['minus1']['labels']:
 k,=lab['base_monomial'];expected.append((lab['i'],lab['b'],'v_k Q',[k],sums(squarefree(k),q)))
for lab in s['selected']['zero']['labels']:
 k,l=lab['base_monomial'];expected.append((lab['i'],lab['b'],'v_k v_l',[k,l],sums(squarefree(k),squarefree(l))))
need(len(w['requests'])==len(expected)==32,'32 requests')
seen=0
for j,(record,(i,b,block,mon,poly))in enumerate(zip(w['requests'],expected)):
 need(record['id']==j and record['scalar_map']=={'i':i,'b':b}and record['block']==block and record['base_monomial']==mon,'label correspondence')
 need(len(record['terms'])==len(poly),'duplicate or missing terms')
 actual={tuple(t['dual_monomial']):t['coefficient']for t in record['terms']};need(actual==poly,'exact weighted coefficients')
 for t in record['terms']:
  m=t['dual_monomial'];e=[-1-v for v in m]
  need(t['laurent_exponents']==e,'residue sign/shift')
  k=t['output_index'];need(type(k)is int and 0<=k<81,'index')
  # Independently decode base-three output index into Laurent exponents.
  recovered=[(k//(3**(3-i)))%3-3 for i in range(4)]
  need(recovered==e,'base3 coordinate order');seen+=1
need(expected[0][-1][(1,1,1,1)]==2,'Q squared cross coefficient')
need(all(x is False for x in w['gates'].values()),'no source release')
print(json.dumps({'status':'independent_exact_weighted_pass','requests':32,'term_records_checked':seen,'Q_squared_cross_coefficient':2,'weighted_sha256':hashlib.sha256(wraw).hexdigest(),'source_values':False,'obstruction':'undecided'},indent=2,sort_keys=True))
