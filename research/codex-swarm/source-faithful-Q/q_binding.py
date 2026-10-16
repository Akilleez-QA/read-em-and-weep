"""Coefficient-free fixed N14 quotient and owned C binding. No actual execution."""
import sys,json,hashlib
from pathlib import Path
from itertools import combinations,product
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'inner-quotient'))
import quotient as QH
I=sys.modules['interfaces']
need=I.need

def pair(p):
 need(type(p)in(tuple,list)and len(p)==2 and all(type(i)is int for i in p)and tuple(p)in((0,1),(2,3)),'exact ordered pair')
 return tuple(p)

def authenticate():
 pins=json.loads(Path(__file__).with_name('source-pins.json').read_text())
 for row in pins['workspace_inputs']:
  need(hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()==row['sha256'],'reviewed constructor pin drift')
 QH.authenticate_sources()
 return pins

def degree(owner,p,N=14):
 p=pair(p);need(isinstance(owner,I.FullOwner),'full owned C owner')
 return tuple(N*(4 if owner.carrier==5 else 5)+(1+2*((owner.legal_mask>>i)&1)if i in p else 0)for i in range(4))

def local_reference(R,bits):
 """Independent literal local homogeneous-coordinate substitution; no coefficients."""
 vs=[]
 for j in range(5):
  terms=[]
  for A in combinations(range(4),j):
   # X_i=1,Y_i=t_i on infinity; X_i=x_i,Y_i=1 on finite.
   terms.append(R.times(*(R.x(i)for i in range(4)if(i in A and bits[i]==0)or(i not in A and bits[i]==1))))
  vs.append(R.plus(*terms))
 hs=[R.plus(R.power(v,5),R.times(R.const(-1),*vs))for v in vs]
 aux=R.times(vs[0],vs[1],vs[3],vs[4]);finite=[i for i in range(4)if not bits[i]];complete=[]
 for k in range(5):
  terms=[]
  for ns in product(range(k+1),repeat=len(finite)):
   if sum(ns)==k:terms.append(R.times(*(R.power(R.x(i),n)for i,n in zip(finite,ns))))
  complete.append(R.plus(*terms))
 return vs,hs,aux,complete

class OwnedClearing:
 mode='physical'
 def __init__(self,owner,p,local=False):
  need(isinstance(owner,I.FullOwner),'full owned clearing');self.owner=owner;self.pair=pair(p);self.local=local
  self.R=QH.FiniteRing('physical',QH.Budget());R=self.R
  bits=tuple((owner.standard_tag>>(3-i))&1 for i in range(4))if local else(0,0,0,0)
  v,h,a,H=local_reference(R,bits);carrier=a if owner.carrier==5 else h[owner.carrier]
  factors=[R.power(carrier,14)]
  for i in self.pair:
   mask=(owner.legal_mask>>i)&1;x=R.x(i)
   ell=(R.plus(R.const(1),R.times(R.const(-1),R.power(x,2)))if mask else x)if bits[i]else(R.plus(R.power(x,3),R.times(R.const(-1),x))if mask else R.const(1))
   factors.append(ell)
  self.root=R.times(*factors);self.homogeneous_degree=degree(owner,self.pair)
  self.ledger=({'owner':owner.data(),'kind':'H','axis':None,'power':14},)+tuple({'owner':owner.data(),'kind':'ell','axis':i,'power':1}for i in self.pair)
 def coefficient(self,e):
  raise I.PhysicalAdmissionMissing('actual owned C coefficient execution is unbound') # unconditional
 def support_box(self):
  b=self.R.bound(self.root);return None if b is None else((0,0,0,0),b)

class ActualQuotientBinding:
 mode='physical'
 def __init__(self,owner,p=(0,1)):
  authenticate();need(isinstance(owner,I.FullOwner),'full quotient owner');p=pair(p)
  self.owner=owner;self.pair=p;self.program=QH.QuotientProgram(owner,QH.ActualCatalog(),N=14,pair=p)
  self.finite_C=OwnedClearing(owner,p);self.local_C=OwnedClearing(owner,p,local=True)
  # Compare actual local catalog constructor to literal coefficient-free reference.
  R=self.program.R
  actual=QH.ActualCatalog().bind(R,self.program.bits)
  expected=local_reference(R,self.program.bits)
  need(actual==expected,'actual local catalog semantic mismatch')
  c=degree(owner,p)
  need(self.program.shift==tuple(-c[i]if self.program.bits[i]else 0 for i in range(4)),'owned divisor frame mismatch')
  self.definition={'schema':'source-faithful-inner-Q-definition-v1','owner':owner.data(),'pair':p,
   'parameters':self.program.parameters,'owned_degree':c,'finite_frame_shift':self.program.shift,
   'coordinate_reversal':self.program.bits,'C_ledger':self.finite_C.ledger,
   'local_identity':'rho = C_local * Qcarrier * product_pair Qline * product_complement L',
   'finite_frame_identity':'rho / C_finite = local_quotient(local(x)) * product_infinity x_i^(-c_i)',
   'whole_standard_extension':'Qhat is regular O(-c) on the original owner standard open',
   'actual_coefficient_execution':False,'physical_admission':False,
   'source_P_identity_proved_here':False,'historical_order_identity':False}
 def support_box(self):return self.program.support_box()
 def coefficient(self,e):raise I.PhysicalAdmissionMissing('actual quotient execution is unbound')
 def factor_terms(self,owner,pair=(0,1)):raise I.PhysicalAdmissionMissing('actual quotient stream execution is unbound')

class ArtificialBinding:
 """Tiny external artificial catalog only, never inferred to be actual HM."""
 mode='synthetic'
 def __init__(self,owner,catalog,N=1,p=(0,1),budget=None):
  need(type(catalog)is QH.ArtificialCatalog,'explicit artificial catalog required')
  self.owner=owner;self.pair=pair(p);self.program=QH.QuotientProgram(owner,catalog,N=N,pair=self.pair,budget=budget)
 def coefficient(self,e):return self.program.coefficient(e)
 def support_box(self):return self.program.support_box()
 def factor_terms(self,owner,pair=(0,1)):
  need(owner==self.owner and globals()['pair'](pair)==self.pair,'full quotient owner/pair changed')
  return self.program.factor_terms(owner,self.pair)

class ActualQBinding:
 """Descriptor factory; returned data are definitions, never admission tokens."""
 mode='physical'
 def __init__(self,repo=None):
  canonical=Path(__file__).resolve().parents[3]
  need(repo is None or Path(repo).resolve()==canonical,'only canonical workspace repository is supported')
  self.pins=authenticate()
 def describe(self,owner,pair=(0,1)):
  b=ActualQuotientBinding(owner,globals()['pair'](pair));out=dict(b.definition)
  out['source_inputs']=self.pins
  out['local_Q_AST']={'nodes':b.program.R.nodes,'root':b.program.root}
  out['finite_C_AST']={'nodes':b.finite_C.R.nodes,'root':b.finite_C.root}
  out['local_C_AST']={'nodes':b.local_C.R.nodes,'root':b.local_C.root}
  out['support_box']=b.support_box()
  out['constructor_semantics_checked']=True
  out['scope']='fixed formula definition; not actual source or execution capability'
  return out
 def coefficient(self,owner,e,pair=(0,1)):raise I.PhysicalAdmissionMissing('actual quotient execution is unbound')
 def factor_terms(self,owner,pair=(0,1)):raise I.PhysicalAdmissionMissing('actual quotient stream execution is unbound')

ClearingDefinition=OwnedClearing
