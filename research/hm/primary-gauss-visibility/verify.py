#!/usr/bin/env python3
"""New fixed-list primary-visibility check; never evaluates an actual instance."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
checks=0
def require(c,msg):
 global checks
 checks+=1
 if not c:raise RuntimeError(msg)
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],x['file']+' bytes')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],x['file']+' git blob')
NAMES=('one','W','A','S','D','T','V','P','Wp')
DIM=dict(zip(NAMES,(1,2,3,4,5,6,3,4,2)))
ADJ={'one':['W'],'W':['one','A'],'A':['W','S'],'S':['A','D'],'D':['S','T'],'T':['D','V','P'],'V':['T'],'P':['T','Wp'],'Wp':['P']}
def q(a,b=0):return F(a),F(b)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def times(a,b):return a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,b):return a*b[0],a*b[1]
def minus(a,b):return plus(a,scale(-1,b))
def sy(n,x):
 a,b=q(1),x
 if n==0:return a
 for _ in range(2,n+1):a,b=b,minus(times(x,b),a)
 return b
tr=[q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0)]
chars={r:[sy(n,x) for x in tr] for r,n in [('one',0),('W',1),('A',2),('S',3),('D',4),('T',5)]}
chars['P']=[q(x) for x in (4,4,-1,-1,-1,-1,1,1,0)]
chars['V']=[minus(sy(6,x),p) for x,p in zip(tr,chars['P'])]
chars['Wp']=[minus(times(x,p),t) for x,p,t in zip(tr,chars['P'],chars['T'])]
for r in NAMES:
 for i in range(9):
  rhs=q(0)
  for s in ADJ[r]:rhs=plus(rhs,chars[s][i])
  require(times(tr[i],chars[r][i])==rhs,'W tensor '+r)
def W(v):
 out=Counter()
 for r,n in v.items():
  for s in ADJ[r]:out[s]+=n
 return out
@lru_cache(None)
def product(R,n):
 if n<0:return Counter()
 if n==0:return Counter({R:1})
 if n==1:return W(product(R,0))
 out=W(product(R,n-1));out.subtract(product(R,n-2))
 if any(v<0 for v in out.values()):raise RuntimeError('nongenuine symmetric power product')
 return +out
def h0(blocks,t):
 out=Counter()
 for e,r in blocks:out.update(product(r,e+t))
 return out
def visible(A):
 c=h0(A,3)
 return c['Wp']>=1 and c['T']>=1,c
require(product('Wp',2)==Counter(T=1),'Wp Sym2=T')
require(product('one',5)==Counter(T=1),'Sym5=T')
require(visible([[-1,'Wp'],[2,'one']])==(False,Counter(T=2)),'explicit Wp quotient exclusion')
require(visible([[-8,'one'],[2,'one'],[6,'one']])==(False,Counter(S=1,T=2)),'explicit split quotient exclusion')
base=json.loads((ROOT/'inputs/frontier182.json').read_text())
require(len(base['cases'])==182,'fixed baseline length')
require(len({r['id'] for r in base['cases']})==182,'unique stable labels')
require(Counter(r['profile'] for r in base['cases'])=={'11':159,'12':10,'21':13},'profile baseline')
cut=[];keep=[]
for row in base['cases']:
 require(sum(DIM[R] for e,R in row['A'])==3,row['id']+' rank3')
 ok,c=visible(row['A'])
 if ok:keep.append(row['id'])
 else:cut.append({'id':row['id'],'profile':row['profile'],'source_index':row['source_index'],'A':row['A'],'H0_A3':dict(sorted(c.items())),'missing':{r:1-c[r] for r in ('Wp','T') if c[r]<1}})
require(Counter(r['profile'] for r in cut)=={'11':25,'12':1,'21':4},'exact visibility cuts')
require(len(keep)==152,'visibility survivors')
require(all(r['missing']=={'Wp':1} for r in cut),'every cut lacks Wp')
# Small mutation controls, with no source-instance choices.
require(not visible([[-1,'Wp'],[2,'one']])[0],'missing-Wp rejection')
require(visible([[-3,'Wp'],[4,'one']])[0],'retained witness is only formal')
require(h0([[4,'one'],[4,'one']],3)==Counter(Wp=2,T=2),'multiplicities retained')
require(visible([[4,'one'],[-3,'Wp']])==visible([[-3,'Wp'],[4,'one']]),'block-order invariance')
out={'scope':'New actual-primary visibility condition on the fixed historical182 necessary rows, not a completed coverage proof','sources_authenticated':7,'checks':checks,'original_by_profile':{'11':159,'12':10,'21':13},'excluded_by_profile':{'11':25,'12':1,'21':4},'passes_by_profile':{'11':134,'12':9,'21':9},'cut':cut,'passes':keep,'complete_coverage_proof':False,'actual_instance_evaluated':False,'global_rank_three_exclusion':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'fixed result exact replay')
print(text)
