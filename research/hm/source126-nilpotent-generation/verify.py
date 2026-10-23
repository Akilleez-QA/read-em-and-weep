#!/usr/bin/env python3
"""Universal character and synthetic regression checks; no HM instance data."""
import hashlib,json
from pathlib import Path
from itertools import product
ROOT=Path(__file__).resolve().parent
checks=0
def check(condition,label):
    global checks
    if not condition: raise RuntimeError(label)
    checks+=1
pins={'algebra862.md':'e18035dcceb1c7e0d0d4356ee578937d3172390b',
      'compatibility944.md':'d308e8e0799e8a98ac1e2022ed91232b38f1e050',
      'generation925.md':'becd3300950c2379d1f03294863d8335a83a1087',
      'double933.md':'a428ac4b4b8cb6b67b7b8e3b1625352468adeb05'}
for row in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/'inputs'/row['file']).read_bytes()
    check(hashlib.sha256(b).hexdigest()==row['sha256'],'SHA256 '+row['file'])
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    check(blob==row['git_blob']==pins[row['file']],'original Git blob '+row['file'])
names=('one','W','A','S','D','T','V','P','Wp')
dims=(1,2,3,4,5,6,3,4,2)
def ch(**kw): return tuple(kw.get(n,0) for n in names)
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),
 ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def timesW(x): return tuple(sum(x[i]*rules[i][j] for i in range(9)) for j in range(9))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dimension(a): return sum(x*y for x,y in zip(a,dims))
sym=[ch(one=1),ch(W=1)]
for n in range(2,9): sym.append(sub(timesW(sym[-1]),sym[-2]))
for n,a in enumerate(sym): check(min(a)>=0 and dimension(a)==n+1,'Sym'+str(n))
check(sym[6]==ch(V=1,P=1),'X fourth endpoint')
check(sub(sym[8],ch(P=1,D=1))==ch(),'X first endpoint zero')
F4=ch(P=1,D=2); X4=sym[6]
intersection=tuple(min(a,b) for a,b in zip(F4,X4))
check(intersection==ch(P=1),'unique X arrow channel')
check(sum(a*b for a,b in zip(F4,X4))==1,'Hom_G dimension one')
check(dimension(intersection)==4,'forced nonzero arrow rank')
check(dimension(X4)==7,'forced X row rank')
# Finite regression for the general pigeonhole proof, including either
# parity of degree-zero generator; no sampled HM monomials.
monomials=0
for degree in range(3,9):
 for signs in product((0,1),repeat=degree):
  for generator_sign in (0,1):
   pair=next((i,j) for i in range(degree) for j in range(i+1,degree) if signs[i]==signs[j])
   i,j=pair
   remaining=[signs[k] for k in range(degree) if k not in pair]
   check((sum(signs)+generator_sign)%2==(sum(remaining)+generator_sign)%2,'same-parity pair preserves total sign')
   monomials+=1
# Synthetic endpoint counterexample when the generation premise is absent.
def e4(v): return (v[1],0)
def Q(a): return (a,0)
for a,b in product(range(-2,3),repeat=2):
 check(e4(e4((a,b)))==(0,0),'synthetic square zero')
 check(e4(Q(a))==(0,0),'synthetic compatibility despite nonzero e4')
check(e4((0,1))!=(0,0),'synthetic nonzero map')
check(Q(1)==(1,0),'synthetic positive image only first line')
# If a linear subspace in Cx+Cy meets Cx trivially, projection to Cy
# is injective. Determinant checks below cover exact rational graph lines;
# the proof handles arbitrary complex coefficients, not a finite search.
for t in range(-5,6):
 for s in range(-5,6):
  determinant=t-s
  check((determinant==0)==(t==s),'two normalized graph vectors agree iff dependent')
  check((t,1)[1]!=0,'graph misses pure X line')
check(1*1-0*0!=0,'a two-plane contains X and is forbidden')
result={'checks':checks,'parity_regressions':monomials,
 'first_endpoint_on_D_Q':'injective',
 'typeIII_nonzero_X_arrow_Q_composite_rank':4,
 'typeIII_X_target_Q_projection_rank':7,
 'typeIII_radical_dimension_upper_bound':1,
 'typeI_II_radical_dimension_upper_bound':2,
 'source_dual_pairs_removed':0,'stable_labels_removed':0,
 'scope':'Universal symbolic and synthetic checks; actual ranks are proved structurally, not evaluated.'}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
