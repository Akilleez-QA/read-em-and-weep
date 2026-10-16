"""Finite first-hit partition lowering. Actual N14: metadata only."""
import sys,itertools,math,json,hashlib,subprocess
from pathlib import Path
from fractions import Fraction as Q
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'inserted-coefficients'))
from interfaces import FullOwner,need,exponent,require_synthetic
from polynomial_coefficients import Ring,Budget
ZERO=(0,0,0,0)

def authenticate_sources(repo=None):
 repo=Path(repo)if repo else Path(__file__).resolve().parents[3]
 pins=json.loads(Path(__file__).with_name('source-pins.json').read_text())
 for row in pins['sources']:
  raw=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=repo,timeout=10)
  need(hashlib.sha256(raw).hexdigest()==row['sha256'],'quotient source pin drift')
 return pins


class FiniteRing(Ring):
 def __init__(self,mode,budget):super().__init__(mode,budget);self.index_visits=0;self.max_index_visits=20000
 def debit_index(self):
  self.index_visits+=1;need(self.index_visits<=self.max_index_visits,'bounded index visit cap')
 def first_hit(self,cs,vs,j,T,L):return self.node('first_hit',tuple(cs),tuple(vs),j,T,L)
 def affine_sum(self,terms):return self.node('affine_sum',tuple(terms))
 def bound(self,r):
  if r in self.bounds:return self.bounds[r]
  op,*a=self.nodes[r]
  if op=='first_hit':
   cs,vs,j,T,L=a
   # Discarding the threshold subtraction only enlarges degree bounds.
   bs=[tuple(x+y for x,y in zip(self.bound(c)or ZERO,self.bound(v)or ZERO))for c,v in zip(cs,vs)]
   b=tuple(L*max(z[i]for z in bs)for i in range(4))
  elif op=='affine_sum':
   bs=[self.bound(z)for z in a[0]];bs=[z for z in bs if z is not None]
   b=tuple(max(z[i]for z in bs)for i in range(4))if bs else None
  else:return super().bound(r)
  self.bounds[r]=b;return b
 def _coefficient(self,r,e):
  require_synthetic(self.mode);op,*a=self.nodes[r]
  if op not in('first_hit','affine_sum'):
   out=super()._coefficient(r,e)
   need(out.numerator.bit_length()<=4096 and out.denominator.bit_length()<=4096,'coefficient bit cap')
   return out
  key=(r,e)
  if key in self.cache:return self.cache[key]
  self.budget.debit('queries');b=self.bound(r)
  if b is None or any(x<0 or x>y for x,y in zip(e,b)):return Q(0)
  out=Q(0)
  if op=='affine_sum':
   for z in a[0]:self.debit_index();out+=self._coefficient(z,e)
  else:
   cs,vs,j,T,L=a;d=len(cs)
   def compositions(i,left,prefix):
    self.debit_index()
    if i==d:
     if left==0:yield prefix
     return
    lo=T if i==j else 0;hi=min(left,T-1)if i<j else left
    for n in range(lo,hi+1):yield from compositions(i+1,left-n,prefix+(n,))
   for ns in compositions(0,L,()):
    coefficient=1;left=L;factors=[]
    for i,n in enumerate(ns):
     coefficient*=math.comb(left,n);left-=n
     factors.extend((self.power(cs[i],n),self.power(vs[i],n-T*(i==j))))
    term=self.times(self.const(coefficient),*factors);out+=self._coefficient(term,e)
  need(out.numerator.bit_length()<=4096 and out.denominator.bit_length()<=4096,'coefficient bit cap')
  need(len(self.cache)<self.budget.max_cache,'cache cap');self.cache[key]=out;return out

class ArtificialCatalog:
 mode='synthetic'
 def __init__(self,v,h,a,complete):
  need(len(v)==len(h)==len(complete)==5,'artificial catalog slots')
  for poly in [*v,*h,a,*complete]:
   need(type(poly)is dict and len(poly)<=32,'artificial sparse input cap')
   for e,c in poly.items():
    need(all(0<=z<=2 for z in exponent(e)),'artificial input degree cap')
    q=Q(c);need(q.numerator.bit_length()<=16 and q.denominator.bit_length()<=16,'artificial input coefficient cap')
  self.v=v;self.h=h;self.a=a;self.complete=complete
 def bind(self,R,bits):
  return([R.polynomial(p)for p in self.v],[R.polynomial(p)for p in self.h],R.polynomial(self.a),[R.polynomial(p)for p in self.complete])

class ActualCatalog:
 mode='physical'
 def __init__(self,repo=None):self.source_pins=authenticate_sources(repo)
 def bind(self,R,bits):
  v=[]
  for k in range(5):
   terms=[]
   for A in itertools.combinations(range(4),k):terms.append(R.times(*(R.x(i)for i in range(4)if(i in A and not bits[i])or(i not in A and bits[i]))))
   v.append(R.plus(*terms))
  h=[R.plus(R.power(z,5),R.times(R.const(-1),*v))for z in v];a=R.times(v[0],v[1],v[3],v[4])
  finite=[i for i in range(4)if not bits[i]];H=[]
  for k in range(5):
   terms=[]
   for ns in itertools.product(range(k+1),repeat=len(finite)):
    if sum(ns)==k:terms.append(R.times(*(R.power(R.x(i),n)for i,n in zip(finite,ns))))
   H.append(R.plus(*terms))
  return v,h,a,H

class QuotientProgram:
 def __init__(self,owner,catalog,N=14,pair=(0,1),budget=None):
  need(isinstance(owner,FullOwner),'full quotient owner');need(type(N)is int and N>=1,'positive N')
  need(pair in((0,1),(2,3)),'ordered pair')
  if catalog.mode=='synthetic':need(type(catalog)is ArtificialCatalog and N<=2,'only small artificial catalog parameters execute')
  else:need(type(catalog)is ActualCatalog and N==14,'actual quotient is N14 metadata only')
  self.owner=owner;self.mode=catalog.mode;self.pair=pair;self.N=N;self.budget=budget or Budget();self.R=FiniteRing(self.mode,self.budget);R=self.R
  bits=tuple((owner.standard_tag>>(3-i))&1 for i in range(4));self.bits=bits;s=sum(bits);M=2*N-1;T=5*M;L=(s+1)*(T-1)+1
  self.parameters={'N':N,'M':M,'T':T,'L':L,'s':s,'legal_power':1}
  v,h,a,H=catalog.bind(R,bits);need(len(v)==len(h)==len(H)==5,'complete catalog slots')
  cs=[R.times(R.const((-1)**(s-i)),H[s-i])for i in range(s+1)]
  pieces=[]
  js=range(s+1)if owner.carrier==5 else (owner.carrier,)if owner.carrier<=s else ()
  for j in js:
   B=R.first_hit(cs,v[:s+1],j,T,L)
   if owner.carrier==5:
    terms=[R.times(R.const(math.comb(M,k)),R.power(h[j],k),R.power(v[2],M-k),R.power(a,M-k-N))for k in range(N)]
   else:
    terms=[R.times(R.const(math.comb(M,k)),R.power(h[j],k-N),R.power(R.times(v[2],a),M-k))for k in range(N,M+1)]
   pieces.append(R.times(B,R.affine_sum(terms)))
  root=R.plus(*pieces)
  for i,bit in enumerate(bits):
   m=(owner.legal_mask>>i)&1
   if not bit:line=R.const(0 if m else 1)
   elif i in pair:line=R.const(1)if m else R.x(i)
   else:line=R.plus(R.const(1),R.times(R.const(-1),R.power(R.x(i),2)))if m else R.power(R.x(i),2)
   root=R.times(root,line)
  self.root=root;d=4 if owner.carrier==5 else 5
  self.shift=tuple(-N*d-((1+2*((owner.legal_mask>>i)&1))if i in pair else 0)if bits[i]else 0 for i in range(4))
 def support_box(self):
  b=self.R.bound(self.root)
  if b is None:return None
  return(tuple(self.shift[i]-b[i]if self.bits[i]else 0 for i in range(4)),tuple(self.shift[i]if self.bits[i]else b[i]for i in range(4)))
 def coefficient(self,e):
  require_synthetic(self.mode);e=exponent(e)
  local=tuple(-(e[i]-self.shift[i])if self.bits[i]else e[i]for i in range(4))
  return self.R.coefficient(self.root,local)
 def factor_terms(self,owner,pair=(0,1)):
  require_synthetic(self.mode);need(owner==self.owner and pair==self.pair,'quotient owner/pair changed')
  box=self.support_box()
  if box is None:return ()
  lo,hi=box;volume=math.prod(y-x+1 for x,y in zip(lo,hi));need(volume<=4096,'complete synthetic stream volume cap')
  out=[]
  for e in itertools.product(*(range(x,y+1)for x,y in zip(lo,hi))):
   c=self.coefficient(e)
   if c:out.append((e,c))
  return tuple(out)
