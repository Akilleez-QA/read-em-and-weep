"""Total finite-tuple request planning; actual execution is always unavailable."""
from dataclasses import dataclass
from pathlib import Path
import sys,importlib.util,json,hashlib
from fractions import Fraction
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'inserted-coefficients'))
import interfaces as I
need=I.need

def pair(p):
 need(type(p)in(tuple,list)and len(p)==2 and all(type(i)is int for i in p)and tuple(p)in((0,1),(2,3)),'ordered pair')
 return tuple(p)

@dataclass(frozen=True)
class RequestPlan:
 cochain:str
 owners:tuple
 sorted_owners:tuple
 permutation:tuple
 sorting_sign:int
 effective_sign:int
 zero_reason:str
 repeated_physical:bool
 occurrence_alias:bool
 pair:tuple
 def describe(self):
  return {'cochain':self.cochain,'owners':[o.data()for o in self.owners],
   'sorted_owners':[o.data()for o in self.sorted_owners],'permutation':self.permutation,
   'sorting_sign':self.sorting_sign,'effective_sign':self.effective_sign,'zero_reason':self.zero_reason,
   'repeated_physical':self.repeated_physical,'occurrence_alias':self.occurrence_alias,
   'pair':self.pair,'normalization_only':True,'actual_zero_coefficient_evaluated':False,
   'source_slots_evaluated':False,'physical_admission':False,'frame_plan':frame_plan(self)}

def frame_plan(plan):
 """Pure coefficient-frame routing, independent of permutation normalization.

 Scalar F/T already use their common finite frame. Raw Rsharp is row-End
 at the original first vertex; changing first vertex also conjugates.
 """
 need(type(plan)is RequestPlan,'literal request plan')
 if plan.cochain in('F','T'):
  return {'value_frame':'common_finite_fixed_frame','coefficient_type':'scalar',
   'transport':'identity','parity':plan.effective_sign,'physical_transport_evaluated':False}
 original=plan.owners[0]if plan.owners else None
 canonical=plan.sorted_owners[0]if plan.sorted_owners else None
 same=original is None or original.common_key==canonical.common_key
 transition={'from_owner':original.data()if original else None,
  'to_owner':canonical.data()if canonical else None,
  'symbol':'g(original_first,canonical_first)',
  'ordered_edge_request':(original.data(),canonical.data())if original else None,
  'edge_direction':'original first to canonical first; never silently sort into forward order'}
 return {'value_frame':'row_End_at_original_first_owner','coefficient_type':'End_matrix',
  'original_first_owner':original.data()if original else None,
  'canonical_first_owner':canonical.data()if canonical else None,
  'transition':transition,'transport':'identity'if same else 'ordered_conjugation',
  'ordered_actions':['X_canonical']if same else ['inverse(g(original_first,canonical_first))','X_canonical','g(original_first,canonical_first)'],
  'parity':plan.effective_sign,'zero_reason':plan.zero_reason,
  'zero_plan_requires_no_transport_evaluation':bool(plan.zero_reason),
  'empty_tuple_has_no_base_owner':original is None,'physical_transport_evaluated':False}

def request_plan(cochain,owners,p=(0,1)):
 """Pure cover/cochain normalization, including all degenerate tuples.

 F is the source pullback; T and Rsharp are general common cochains here.
 These metadata never authorize early return from an actual coefficient call.
 """
 need(cochain in('F','T','Rsharp'),'cochain scope');p=pair(p)
 need(type(owners)in(tuple,list)and all(type(o)is I.FullOwner for o in owners),'literal full owner tuple')
 owners=tuple(owners)
 if cochain=='F':need(len(owners)==3,'F is a source two-cochain')
 need(not owners or len({o.seed for o in owners})==1,'coherent seed')
 perm=tuple(sorted(range(len(owners)),key=lambda j:owners[j].source_key))
 sign=(-1)**sum(perm[i]>perm[j]for i in range(len(perm))for j in range(i+1,len(perm)))
 common=len({o.common_key for o in owners})<len(owners)
 physical=len({o.physical_key for o in owners})<len(owners)
 reason='repeated_common'if common else 'source_F_repeated_physical'if cochain=='F'and physical else ''
 return RequestPlan(cochain,owners,tuple(owners[j]for j in perm),perm,sign,0 if reason else sign,reason,physical,len({o.occurrence for o in owners})<len(owners),p)

@dataclass(frozen=True)
class Full96Descriptor:
 seed:int
 occurrence:object
 standard_tag:int
 def __post_init__(self):
  need(type(self.seed)is int and self.seed>=0,'seed');object.__setattr__(self,'occurrence',I.immutable(self.occurrence))
  need(type(self.standard_tag)is int and 0<=self.standard_tag<16,'standard tag')
 def describe(self):
  return {'schema':'lazy-full96-request-domain-v1','seed':self.seed,'occurrence':self.occurrence,'standard_tag':self.standard_tag,
   'index_domain':[0,95],'cardinality':96,'index_bijection':'carrier=index//16; legal_mask=index%16',
   'mask_encoding':'low bit i','standard_encoding':'high bit3-i','zero_weight_labels_retained':True,
   'actual_fiber_enumerated':False,'iteration_admitted':False}
 def label_plan(self,index):
  need(type(index)is int and 0<=index<96,'full96 index')
  return(self.seed,self.occurrence,index//16,index%16,self.standard_tag)
 def __iter__(self):raise I.PhysicalAdmissionMissing('actual96 iteration is not released')
 def owners(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual96 construction is not released')

def _authenticate():
 need(Path(I.__file__).resolve()==(BASE/'inserted-coefficients/interfaces.py').resolve(),'foreign shared interfaces module')
 pins=json.loads(Path(__file__).with_name('source-pins.json').read_text())
 for row in pins['workspace_inputs']:
  need(hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()==row['sha256'],'canonical provider dependency drift: '+row['path'])
 return pins

def _load(name,path):
 if name in sys.modules:
  need(Path(sys.modules[name].__file__).resolve()==path.resolve(),'foreign provider dependency')
  return sys.modules[name]
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module);return module

class ActualProvider:
 """No arbitrary catalog, callback, witness dictionary or verified flag accepted."""
 mode='physical'
 def __init__(self,repo=None):
  canonical=Path(__file__).resolve().parents[3]
  need(repo is None or Path(repo).resolve()==canonical,'canonical repository only')
  self.repo=canonical;self.pins=_authenticate()
  self.domain=_load('tp_actual_domain',BASE/'source-domain-application/domain.py').ActualDomainApplication(canonical)
 def plan(self,cochain,owners,p=(0,1)):return request_plan(cochain,owners,p)
 def describe(self,cochain,owners,p=(0,1)):
  plan=request_plan(cochain,owners,p);out=plan.describe();out['definition_inputs']=self.pins
  out['fiber_domains']=[Full96Descriptor(o.seed,o.occurrence,o.standard_tag).describe()for o in plan.owners]
  if cochain=='F'and not plan.zero_reason and not plan.occurrence_alias:
   # FD sorts once from original owners. We do NOT reapply plan.sign here.
   out['source_definition']=self.domain.describe(plan.owners,plan.pair)
   need(out['source_definition']['source_sorting_sign']==plan.sorting_sign,'single source sorting sign mismatch')
   out['definition_join']='canonical PB/QB/FD definition metadata'
  else:out['definition_join']='normalization only; no raw source reevaluation'
  out['whole_T_or_Rsharp_implementation_supplied']=False
  out['aggregate_budget_certificate']=False
  return out
 def coefficient(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual request refused before normalization/zero/support')
 def alternating_coefficient(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual alternating request is not released')
 def factor_terms(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual quotient iteration is not released')
 def owners(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual fiber iteration is not released')

class ToyProvider:
 """Scalar fixtures only, even for a fixture named Rsharp; no End evaluation."""
 coefficient_scope='scalar_fixture_only'
 mode='synthetic'
 def __init__(self,values,fibers):
  need(type(values)is dict and len(values)<=32,'tiny explicit values');need(type(fibers)is dict and len(fibers)<=4,'tiny explicit fibers')
  need(all(type(v)is int or type(v)is Fraction for v in values.values()),'exact artificial values only')
  self.values=dict(values);self.fibers={}
  for tag,labels in fibers.items():
   need(type(tag)is int and 0<=tag<16 and type(labels)in(tuple,list)and len(labels)<=4,'tiny explicit fiber')
   vals=tuple(labels);need(all(type(o)is I.FullOwner and o.standard_tag==tag for o in vals),'full toy owners')
   need(len({o.common_key for o in vals})==len(vals),'duplicate toy label');self.fibers[tag]=vals
 def owners(self,tag):
  need(tag in self.fibers,'undefined toy fiber')
  yield from self.fibers[tag]
 def coefficient(self,cochain,owners,e,p=(0,1)):
  e=I.exponent(e);plan=request_plan(cochain,owners,p)
  if plan.effective_sign==0:return 0
  key=(cochain,tuple(o.common_key for o in plan.sorted_owners),e,plan.pair)
  need(key in self.values,'undefined artificial coefficient')
  return plan.effective_sign*self.values[key]
