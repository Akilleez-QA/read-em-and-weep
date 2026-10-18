"""Portable static support audit: no production imports, polynomial products or evaluations."""
import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
n=0
def need(x,m):
 global n
 n+=1
 if not x: raise RuntimeError(m)
b=(P/'model.json').read_bytes()
need(hashlib.sha256(b).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926','model pin')
m=json.loads(b)
edges=[(0,2,1,1),(0,3,4,1),(9,3,1,-1),(9,0,2,-1),(6,0,3,-1),(6,2,4,-1)]
for r,c,j,s in edges:
 e=[0]*4;e[j-1]=1
 need(m['gamma'][r][c]==[[','.join(map(str,e)),s]],'cycle record')
need(sum(s*j for s,j in zip([1,-1,1,-1,1,-1],[e[2] for e in edges]))==-5,'cycle degree')
def records(x):return {tuple(map(int,e.split(','))):c for e,c in x}
def parity(d):return {e:c*(-1)**sum((j+1)*a for j,a in enumerate(e)) for e,c in d.items()}
N=records(m['charts'][1]['I'][5][1])
need(N=={(3,0,0,0):-1,(1,2,1,0):-1},'numerator')
need(parity(N)=={(3,0,0,0):1,(1,2,1,0):-1},'CM numerator signs')
D={(0,1,1,1):1,(4,0,0,0):1}
# Signed exponent-lattice reduction mod D after localizing v2,v3.
# Only label transformation and integer coefficient collection, no polynomial products.
def labels(d):
 out={}
 for (a,b,c,d4),q in d.items():
  e=(a+4*d4,b-d4,c-d4);out[e]=out.get(e,0)+q*(-1)**d4
 return {e:q for e,q in out.items() if q}
need(labels(D)=={},'formal relation')
expected=[{(5,0,0):-1,(0,0,0):-1},{(5,0,0):-2},{(5,0,0):-1,(0,5,0):-1},{(5,0,0):-1,(0,0,5):-1},{(5,0,0):-1,(20,-5,-5):1},{(6,-1,0):1}]
den=[{(1,1,1,1):1,(0,0,0,0):-1}]+[{(1,1,1,1):1,tuple(5 if i==j else 0 for i in range(4)):-1}for j in range(4)]+[{(2,0,1,1):-1}]
need(len(m['charts'])==6,'six carriers')
for i,c in enumerate(m['charts']):
 for key in ['di','dp','dh']:need(records(c[key])==den[i],'literal denominator '+key)
 need(labels(den[i])==expected[i] and bool(expected[i]),'nonzero denominator class')
need(labels(parity(N))=={(3,0,0):1,(1,2,1):-1},'nonzero numerator class')
# Mutation controls: prime divisor itself is zero; sign mutation collides correctly.
need(labels({(1,1,1,1):1,(5,0,0,0):1})=={},'transformed denominator class')
need(parity(N)!=N,'sign mutation caught')
need((-5)%2==1 and (-5)%5==0,'character negative/positive controls')
for e in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:need(bool(labels({e:1})),'coordinate factor regular')
x=json.loads((P/'SOURCE_EXCERPTS.json').read_text())
for rec in x['raw_engine']['excerpts'].values():need(hashlib.sha256(rec['text'].encode()).hexdigest()==rec['sha256'],'excerpt pin')
print(json.dumps({'status':'pass','checks':n,'scope':'literal records, signed degree/exponent labels only','production_imports':False,'source_jet_matrix_evaluations':False,'polynomial_products':False},indent=2))
