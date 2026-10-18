"""Shared finite coefficient interfaces. Physical execution is deliberately unbound."""
from dataclasses import dataclass
from fractions import Fraction
from typing import Protocol

def need(ok,message):
    if not ok:raise ValueError(message)

def immutable(x):
    if type(x) in (int,str):return x
    if type(x) in (tuple,list):return tuple(immutable(v)for v in x)
    raise ValueError('occurrence ID must be immutable integers/strings/tuples')

@dataclass(frozen=True)
class FullOwner:
    seed:int
    occurrence:object
    carrier:int
    legal_mask:int
    standard_tag:int
    def __post_init__(self):
        need(type(self.seed)is int and self.seed>=0,'seed')
        object.__setattr__(self,'occurrence',immutable(self.occurrence))
        need(type(self.carrier)is int and 0<=self.carrier<=5,'canonical carrier')
        need(type(self.legal_mask)is int and 0<=self.legal_mask<16,'legal mask')
        need(type(self.standard_tag)is int and 0<=self.standard_tag<16,'standard tag')
    def data(self):return(self.seed,self.occurrence,self.carrier,self.legal_mask,self.standard_tag)
    @property
    def source_key(self):return(-1 if self.carrier==5 else self.carrier,self.legal_mask,self.standard_tag)
    @property
    def physical_key(self):return(self.carrier,self.legal_mask)
    @property
    def common_key(self):return(self.carrier,self.legal_mask,self.standard_tag)

def sorted_source(owners):
    need(all(isinstance(v,FullOwner)for v in owners),'full owners required')
    p=sorted(range(len(owners)),key=lambda j:owners[j].source_key)
    sign=(-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))
    return tuple(owners[j]for j in p),sign

def exponent(e):
    need(type(e)in(tuple,list)and len(e)==4 and all(type(i)is int for i in e),'four integer exponents')
    return tuple(e)

class PhysicalAdmissionMissing(RuntimeError):pass

def require_synthetic(mode):
    if mode!='synthetic':raise PhysicalAdmissionMissing('actual-source coefficient execution has no authenticated physical admission')

@dataclass(frozen=True)
class RegularExtensionWitness:
    evidence:str
    whole_coefficient_id:str
    target_standard_tags:tuple
    owned_clearings:tuple
    domain_id:str
    scope:str='whole_coefficient_on_standard_target'
    def require(self,owners,target_standard_tags):
        require_synthetic(self.evidence)
        need(self.scope=='whole_coefficient_on_standard_target','common-local-only regularity is insufficient')
        need(type(self.whole_coefficient_id)is str and bool(self.whole_coefficient_id),'whole coefficient identity missing')
        need(type(self.domain_id)is str and bool(self.domain_id),'extension domain missing')
        need(tuple(target_standard_tags)==self.target_standard_tags,'target intersection changed')
        need(tuple(owners)==self.owned_clearings,'clearing occurrence owner lost')
        need(all(v.standard_tag in self.target_standard_tags for v in owners),'owner standard not target unit')
        return True

class ClearedFOracle(Protocol):
    mode:str
    def coefficient(self,sorted_owners:tuple,exponent:tuple,pair:tuple=(0,1))->Fraction:...
    def degree_upper(self,sorted_owners:tuple,pair:tuple=(0,1))->tuple:...

class QuotientOracle(Protocol):
    mode:str
    def factor_terms(self,owner:FullOwner,pair:tuple=(0,1)):...

class FiberProvider(Protocol):
    mode:str
    def owners(self,tag:int,occurrence:object):...
