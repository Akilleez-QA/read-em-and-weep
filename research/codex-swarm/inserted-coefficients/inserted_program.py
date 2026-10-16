"""Exact finite demand convolutions and both padded prism sums, synthetic only."""
from fractions import Fraction as Q
from itertools import product,islice
from interfaces import FullOwner,RegularExtensionWitness,need,exponent,require_synthetic,sorted_source
from polynomial_coefficients import Budget

ZERO=(0,0,0,0)

def actual_z_shift(edge):return tuple(5250*sum((o.standard_tag>>(3-i))&1 for o in edge)for i in range(4))

def box_union(boxes):
 boxes=[b for b in boxes if b is not None]
 return None if not boxes else(tuple(min(b[0][i]for b in boxes)for i in range(4)),tuple(max(b[1][i]for b in boxes)for i in range(4)))
def box_sum(a,b):return None if a is None or b is None else(tuple(x+y for x,y in zip(a[0],b[0])),tuple(x+y for x,y in zip(a[1],b[1])))
def valid_box(b):
 if b is None:return b
 lo,hi=map(exponent,b);need(all(x<=y for x,y in zip(lo,hi)),'finite enclosure');return lo,hi

class SparseOracle:
 mode='synthetic'
 def __init__(self,terms,budget):
  self.terms={exponent(m):Q(c)for m,c in terms.items()if c};self.budget=budget
 def support_box(self):
  return None if not self.terms else(tuple(min(m[i]for m in self.terms)for i in range(4)),tuple(max(m[i]for m in self.terms)for i in range(4)))
 def coefficient(self,e):require_synthetic(self.mode);self.budget.debit('queries');return self.terms.get(exponent(e),Q(0))

class ProductOracle:
 def __init__(self,factors,budget):
  need(factors,'product factors');self.factors=tuple(factors);self.budget=budget;self.mode='synthetic'if all(f.mode=='synthetic'for f in factors)else'physical'
  self.left=factors[0];self.right=ProductOracle(factors[1:],budget)if len(factors)>2 else factors[1]if len(factors)==2 else None
 def support_box(self):
  out=(ZERO,ZERO)
  for f in self.factors:out=box_sum(out,valid_box(f.support_box()))
  return out
 def coefficient(self,e):
  require_synthetic(self.mode);e=exponent(e)
  if self.right is None:return self.left.coefficient(e)
  A,B=valid_box(self.left.support_box()),valid_box(self.right.support_box())
  if A is None or B is None:return Q(0)
  ranges=[range(max(A[0][i],e[i]-B[1][i]),min(A[1][i],e[i]-B[0][i])+1)for i in range(4)];out=Q(0)
  for a in product(*ranges):
   self.budget.debit('splits');out+=self.left.coefficient(a)*self.right.coefficient(tuple(x-y for x,y in zip(e,a)))
  return out

class SumOracle:
 def __init__(self,terms,budget):self.terms=tuple(terms);self.budget=budget;self.mode='synthetic'if all(f.mode=='synthetic'for _,f in terms)else'physical'
 def support_box(self):return box_union([f.support_box()for _,f in self.terms])
 def coefficient(self,e):require_synthetic(self.mode);return sum((Q(c)*f.coefficient(e)for c,f in self.terms),Q(0))

class DerivativeOracle:
 def __init__(self,f,axis):need(type(axis)is int and 0<=axis<4,'axis');self.f=f;self.axis=axis;self.mode=f.mode
 def support_box(self):
  b=self.f.support_box()
  return None if b is None else(tuple(x-int(i==self.axis)for i,x in enumerate(b[0])),tuple(x-int(i==self.axis)for i,x in enumerate(b[1])))
 def coefficient(self,e):
  require_synthetic(self.mode);e=exponent(e);ee=list(e);ee[self.axis]+=1
  return(e[self.axis]+1)*self.f.coefficient(tuple(ee))

class SourceSlice:
 def __init__(self,source,owners,pair=(0,1)):self.source=source;self.owners,self.sign=sorted_source(owners);self.mode=source.mode;self.pair=pair
 def support_box(self):
  b=self.source.degree_upper(self.owners,self.pair);return None if b is None else(ZERO,tuple(b))
 def coefficient(self,e):require_synthetic(self.mode);return self.sign*self.source.coefficient(self.owners,exponent(e),self.pair)

class SyntheticFibers:
 mode='synthetic'
 def __init__(self,seed,domains):
  self.seed=seed;self.domains={k:tuple(v)for k,v in domains.items()}
  for tag,values in self.domains.items():need(len(set(values))==len(values),'duplicate synthetic fiber label')
 def owners(self,tag,occurrence):
  require_synthetic(self.mode);need(tag in self.domains,'synthetic domain completeness undefined at tag')
  return tuple(FullOwner(self.seed,occurrence,c,m,tag)for c,m in self.domains[tag])

class SyntheticQuotients:
 mode='synthetic'
 def __init__(self,terms_by_label):self.terms=terms_by_label
 def factor_terms(self,owner,pair=(0,1)):
  require_synthetic(self.mode);need(pair in((0,1),(2,3)),'ordered source pair')
  key=(owner.carrier,owner.legal_mask,owner.standard_tag);need(key in self.terms,'synthetic quotient undefined')
  return tuple((exponent(e),Q(c))for e,c in self.terms[key].items()if c)

class RequestContext:
 def __init__(self,outer_owners,prefix_owners,outer_weight_owners):
  self.outer=tuple(outer_owners);self.prefix=tuple(prefix_owners);self.weights=tuple(outer_weight_owners)
 def validate(self,edge):
  need(self.weights==self.outer,'outer owner weight/prefix loss')
  need(all(isinstance(v,FullOwner)for v in self.outer),'full outer owners')
  need(all(v in self.outer for v in self.prefix+tuple(edge)),'prefix/scalar edge owner absent')
  need(len({(v.seed,v.occurrence)for v in self.outer})==len(self.outer),'outer owner merged')
  need(len(self.outer)in(4,5)and len(self.prefix)==len(self.outer)-3,'q3/q4 prefix owner cardinality')
  need(self.prefix==self.outer[:len(self.prefix)],'prefix owner reassigned')
  return True

class PrismProgram:
 """N_prism1=Z sumQhat P; N_prism2=-Ca Z sumQhatQhat P.
 C_a is a complete owned polynomial oracle. Z is an exact monomial padding.
 """
 def __init__(self,edge,source,quotient,fibers,C_a,z_shift,witness,budget,context=None,pair=(0,1)):
  need(len(edge)==2 and all(isinstance(o,FullOwner)for o in edge),'edge full owners')
  need(edge[0].seed==edge[1].seed,'edge request seed mismatch')
  need(edge[0].source_key<edge[1].source_key,'raw prism formula requires increasing source-first common edge; alternate the COMPLETE result externally')
  self.edge=tuple(edge);self.source=source;self.quotient=quotient;self.fibers=fibers;self.C_a=C_a;self.Z=exponent(z_shift);self.witness=witness;self.budget=budget
  self.mode='synthetic'if all(x.mode=='synthetic'for x in(source,quotient,fibers,C_a))else'physical'
  need(pair in((0,1),(2,3)),'ordered source pair');self.pair=pair
  self.context=context
  if self.mode=='physical':
   need(self.Z==actual_z_shift(self.edge),'actual Z padding must retain both standard owners')
   need(isinstance(context,RequestContext),'outer prefix/weight context required')
  if context is not None:context.validate(self.edge)
 def _owners(self,tag,occurrence):
  values=tuple(islice(iter(self.fibers.owners(tag,occurrence)),4097))
  need(len(values)<=4096,'finite fiber provider cap')
  need(all(isinstance(o,FullOwner)and o.standard_tag==tag and o.seed==self.edge[0].seed and o.occurrence==occurrence for o in values),'inserted fiber full owner binding')
  need(len({o.common_key for o in values})==len(values),'duplicate inserted fiber label')
  return values
 def _source_product(self,owners,shifts,e,padding=None):
  e=tuple(x-z-sum(a[i]for a,_ in shifts)for i,(x,z)in enumerate(zip(e,self.Z)))
  factor=Q(1)
  for _,c in shifts:factor*=c
  src=SourceSlice(self.source,owners,self.pair)
  return factor*(src.coefficient(e)if padding is None else ProductOracle([padding,src],self.budget).coefficient(e))
 def coefficient(self,kind,e):
  require_synthetic(self.mode);need(kind in('prism1','prism2'),'prism kind');e=exponent(e)
  a,b=self.edge;self.witness.require(self.edge,(a.standard_tag,b.standard_tag));out=Q(0)
  for u in self._owners(a.standard_tag,('inserted',a.occurrence,b.occurrence,'u')):
   need(u.standard_tag==a.standard_tag,'inserted u standard mismatch')
   U=tuple(self.quotient.factor_terms(u,self.pair));need(len(U)<=4096,'finite quotient stream cap')
   if kind=='prism1':
    self.budget.debit('owner_terms')
    for term in U:out+=self._source_product((u,a,b),(term,),e)
   else:
    for v in self._owners(b.standard_tag,('inserted',a.occurrence,b.occurrence,'v')):
     need(v.standard_tag==b.standard_tag,'inserted v standard mismatch');self.budget.debit('owner_terms')
     V=tuple(self.quotient.factor_terms(v,self.pair));need(len(V)<=4096,'finite quotient stream cap')
     for tu in U:
      for tv in V:
       self.budget.debit('splits');out-=self._source_product((u,v,b),(tu,tv),e,self.C_a)
  return out

class WholeNumerator:
 """Combines ALL THREE branches before any derivative operator can wrap it."""
 def __init__(self,standard_B,prism_program,C_b,prism_support_box):
  self.prism=prism_program;self.box=valid_box(prism_support_box)
  z=SparseOracle({prism_program.Z:1},prism_program.budget)
  self.standard=ProductOracle([prism_program.C_a,C_b,z,standard_B],prism_program.budget)
  self.mode='synthetic'if self.standard.mode==prism_program.mode=='synthetic'else'physical'
 def support_box(self):return box_union([self.standard.support_box(),self.box])
 def coefficient(self,e):
  require_synthetic(self.mode)
  return self.standard.coefficient(e)+self.prism.coefficient('prism1',e)+self.prism.coefficient('prism2',e)

class DifferentiatedCombinedNumerator:
 """Delta*dN - N*sum a_f(df)prod_(g!=f)g; denominator is D*Delta.
 Factor keys include complete owners. Equal polynomials do not merge owners.
 """
 def __init__(self,N,owned_factors,axis,budget):
  need(isinstance(N,WholeNumerator),'differentiate only COMPLETE combined N')
  need(owned_factors,'positive owned denominator factors required');keys=[]
  for owner,name,power,f in owned_factors:
   need(isinstance(owner,FullOwner)and type(name)is str and name,'full owned factor')
   need(type(power)is int and power>0,'positive denominator multiplicity');keys.append((owner,name))
  need(len(set(keys))==len(keys),'duplicate SAME owned factor; sum its multiplicity explicitly')
  one=SparseOracle({ZERO:1},budget)
  delta=ProductOracle([f for _,_,_,f in owned_factors],budget)
  derivatives=[]
  for j,(_,_,power,f)in enumerate(owned_factors):
   others=[g for k,(_,_,_,g)in enumerate(owned_factors)if k!=j]
   derivatives.append((power,ProductOracle([DerivativeOracle(f,axis),*(others or[one])],budget)))
  self.numerator=SumOracle([(1,ProductOracle([delta,DerivativeOracle(N,axis)],budget)),(-1,ProductOracle([N,SumOracle(derivatives,budget)],budget))],budget)
  self.denominator_description={'D':[(o.data(),name,p)for o,name,p,_ in owned_factors],'Delta':[(o.data(),name,1)for o,name,_,_ in owned_factors],'equation':'d(N/D)=numerator/(D*Delta)'}
  self.mode=self.numerator.mode
 def coefficient(self,e):require_synthetic(self.mode);return self.numerator.coefficient(e)
