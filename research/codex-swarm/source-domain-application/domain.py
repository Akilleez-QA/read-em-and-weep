"""Complete symbolic common-fiber domain and coefficient-free degree contracts.

Actual fibers and coefficients are deliberately not iterable/evaluable. The
only provider that yields owners is the explicitly tiny artificial provider.
"""
from dataclasses import dataclass
import importlib.util
import json
from pathlib import Path
import sys

SHARED=Path(__file__).resolve().parent.parent/'inserted-coefficients'
if str(SHARED)not in sys.path:sys.path.insert(0,str(SHARED))
import interfaces as I
need=I.need

def pair(p):
    need(type(p)in(tuple,list)and len(p)==2 and all(type(i)is int for i in p)and tuple(p)in((0,1),(2,3)),'ordered complementary pair')
    return tuple(p)

def bits(tag):
    need(type(tag)is int and 0<=tag<16,'standard high-bit tag')
    return tuple((tag>>(3-i))&1 for i in range(4))

def whole_owners(owners):
    need(type(owners)in(tuple,list)and len(owners)==3 and all(isinstance(o,I.FullOwner)for o in owners),'complete three source owners')
    need(len({o.seed for o in owners})==1,'coherent seed provenance')
    need(len({o.occurrence for o in owners})==3,'source occurrence owners must stay distinct')
    return tuple(owners)

@dataclass(frozen=True)
class FullFiberDomain:
    seed:int
    occurrence:object
    standard_tag:int
    def __post_init__(self):
        need(type(self.seed)is int and self.seed>=0,'seed')
        object.__setattr__(self,'occurrence',I.immutable(self.occurrence));bits(self.standard_tag)
    def contains(self,owner):
        return isinstance(owner,I.FullOwner)and(owner.seed,owner.occurrence,owner.standard_tag)==(self.seed,self.occurrence,self.standard_tag)
    def descriptor(self):
        return {'schema':'full-common-fiber-domain-v1','seed':self.seed,'occurrence':self.occurrence,
            'standard_tag':self.standard_tag,'carrier_domain':{'minimum':0,'maximum':5,'inclusive':True},
            'legal_mask_domain':{'minimum':0,'maximum':15,'inclusive':True,'bit_order':'low bit i'},
            'cardinality':{'expression':'6 * 16','value':96},
            'completeness':'exact Cartesian index domain; zero weights do not remove labels',
            'standard_encoding':'high bit 3-i','actual_owners_enumerated':False,
            'actual_coefficients_evaluated':False}
    def __iter__(self):raise I.PhysicalAdmissionMissing('full96 domain is a descriptor, not an enumeration release')
    def owners(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('actual fiber construction is not released')
    def coefficient(self,*args,**kwargs):raise I.PhysicalAdmissionMissing('no physical source coefficients are admitted')

class LazyToyFibers:
    """Only caller-supplied tiny artificial labels; never derived from full96."""
    mode='synthetic'
    def __init__(self,seed,domains):
        need(type(seed)is int and seed>=0,'toy seed');need(type(domains)is dict and len(domains)<=4,'tiny explicit tag domain')
        self.seed=seed;self.domains={};self.yields=0
        for t,labels in domains.items():
            bits(t);need(type(labels)in(tuple,list)and len(labels)<=4,'tiny explicit label list')
            values=[]
            for item in labels:
                need(type(item)in(tuple,list)and len(item)==2,'toy carrier/mask')
                c,m=item;need(type(c)is int and 0<=c<=5 and type(m)is int and 0<=m<16,'toy label bounds')
                values.append((c,m))
            need(len(set(values))==len(values),'duplicate toy label');self.domains[t]=tuple(values)
    def owners(self,tag,occurrence):
        bits(tag);occurrence=I.immutable(occurrence);need(tag in self.domains,'toy domain undefined')
        for c,m in self.domains[tag]:
            self.yields+=1
            yield I.FullOwner(self.seed,occurrence,c,m,tag)

def C_degree(owner,p):
    need(isinstance(owner,I.FullOwner),'complete C owner');p=pair(p)
    d=4 if owner.carrier==5 else 5
    return tuple(14*d+((1+2*((owner.legal_mask>>i)&1))if i in p else 0)for i in range(4))

def Qhat_frame_enclosure(owner,p):
    """Imported mathematical enclosure, not computed occupied support.

    Finite actual-mask1 branches have zero weight, but coefficients still
    refuse. The full domain descriptor does not discard those vertices.
    """
    need(isinstance(owner,I.FullOwner),'full Qhat owner');p=pair(p);b=bits(owner.standard_tag);s=sum(b);c=C_degree(owner,p)
    finite=(66,335,872,1677,None)[s];infinity=(None,213,347,481,66)[s]
    extra=tuple((1-((owner.legal_mask>>i)&1)if i in p else 2)if b[i]else 0 for i in range(4))
    lo=tuple(-c[i]-infinity-extra[i]if b[i]else 0 for i in range(4))
    hi=tuple(-c[i]if b[i]else finite for i in range(4))
    return {'owner':owner.data(),'pair':p,'C_degree':c,'finite_frame_shift':tuple(-c[i]if b[i]else 0 for i in range(4)),
        'exponent_enclosure':(lo,hi),'occupied_support_computed':False,
        'zero_weight_predicate':any(not b[i]and((owner.legal_mask>>i)&1)for i in range(4)),
        'extra_pair_twist_attached':False}

def repetition_scope(owners):
    owners=whole_owners(owners)
    return {'physical_source_pullback_repeated':len({o.physical_key for o in owners})<3,
        'general_common_cochain_repeated':len({o.common_key for o in owners})<3,
        'denominator_occurrences_retained':len(owners),'actual_zero_coefficient_evaluated':False}

def extension_contract(owners,p):
    """Exact indices of SW's implication, conditional on the fixed P/Q proofs."""
    owners=whole_owners(owners);p=pair(p);degrees=[C_degree(o,p)for o in owners]
    n=tuple(-2 if i in p else 0 for i in range(4));D=tuple(sum(c[i]for c in degrees)+n[i]for i in range(4))
    Q=[Qhat_frame_enclosure(o,p)for o in owners]
    lo=tuple(sum(q['exponent_enclosure'][0][i]for q in Q)for i in range(4))
    hi=tuple(D[i]+sum(q['exponent_enclosure'][1][i]for q in Q)for i in range(4))
    tags=[o.standard_tag for o in owners];conditions=[]
    for i in range(4):
        states={bits(t)[i]for t in tags}
        if states=={0}:need(lo[i]>=0,'finite target lower inequality');conditions.append('exponent>=0')
        elif states=={1}:need(hi[i]<=n[i],'infinity target upper inequality');conditions.append('exponent<='+str(n[i]))
        else:conditions.append('mixed intersection: coordinate invertible')
    return {'schema':'conditional-actual-standard-domain-v1','owners':[o.data()for o in owners],'pair':p,
        'target_standard_tags':tags,'C_degrees':degrees,'whole_P_exact_homogeneous_degree':D,
        'Pi_summand_finite_enclosure':(lo,hi),'standard_target_conditions':conditions,
        'source_order':'auxiliary5-first; primary0..4; numeric low-bit mask; high-bit standard tag',
        'source_identity':'complete freshly evaluated fixed-order b-tr(C)/2, then alternating extension',
        'required_definition_producers':['source-faithful-P','source-faithful-Q'],
        'proof_dependency':'standard-source-witnesses/PROOF.md section1',
        'actual_source_oracle_identity_accepted':False,'actual_fibers_enumerated':False,
        'physical_execution_authorized':False}

def actual_coefficient(*args,**kwargs):
    raise I.PhysicalAdmissionMissing('domain theorem is not a physical coefficient execution release')

def metadata_profile(payload):
    """Count stored AST arrays and serialized description bytes, not HM cost."""
    arrays=[]
    def visit(value,path):
        if type(value)is dict:
            for key,item in value.items():
                here=path+'/'+key
                if key in('dag','nodes')and type(item)is list:arrays.append({'path':here,'stored_nodes':len(item)})
                visit(item,here)
        elif type(value)in(list,tuple):
            for j,item in enumerate(value):visit(item,path+'/'+str(j))
    visit(payload,'')
    return {'scope':'stored descriptor AST arrays and JSON payload before adding this profile',
        'stored_AST_arrays':arrays,'aggregate_stored_AST_nodes':sum(a['stored_nodes']for a in arrays),
        'serialized_payload_bytes':len(json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode()),
        'physical_coefficient_memory_or_cost_admission':False,
        'aggregate_resource_supervisor_present':False}

def _canonical_module(name,path):
    need(path.is_file(),'named P/Q source-definition producer is not yet present')
    if name in sys.modules:
        need(Path(sys.modules[name].__file__).resolve()==path.resolve(),'canonical definition module path changed')
        return sys.modules[name]
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module;spec.loader.exec_module(module);return module

class ActualDomainApplication:
    """Coefficient-free adapter to the TWO canonical producer definitions.

    No catalogs, callbacks, proof dictionaries, or admission status may be
    supplied. Descriptions are evidence to review, not authentication tokens.
    This factory does not enumerate any actual full fiber.
    """
    mode='physical'
    def __init__(self,repo=None):
        root=Path(__file__).resolve().parents[3]
        need(repo is None or Path(repo).resolve()==root,'canonical repository only')
        self.repo=root
    def describe(self,owners,p=(0,1)):
        owners=whole_owners(owners);p=pair(p);contract=extension_contract(owners,p)
        source,sign=I.sorted_source(owners)
        need(all(source[i].source_key<source[i+1].source_key for i in range(2)),'Pi target must have three distinct common vertices')
        base=Path(__file__).resolve().parent.parent
        Pmod=_canonical_module('fd_actual_P_binding',base/'source-faithful-P'/'p_binding.py')
        Qmod=_canonical_module('fd_actual_Q_binding',base/'source-faithful-Q'/'q_binding.py')
        P=Pmod.ActualPBinding(repo=self.repo);Q=Qmod.ActualQBinding(repo=self.repo)
        p_description=P.describe(source,p)
        need(tuple(P.degree_upper(source,p))==contract['whole_P_exact_homogeneous_degree'],'actual P exact owner degree mismatch')
        q_descriptions=[]
        for o in owners:
            q=Q.describe(o,p)
            need(tuple(q['owner'])==o.data()and tuple(q['pair'])==p,'Q definition full-owner/pair mismatch')
            need(tuple(q['owned_degree'])==C_degree(o,p),'P/Q owned C degree mismatch')
            need(tuple(q['finite_frame_shift'])==tuple(-x if bit else 0 for x,bit in zip(C_degree(o,p),bits(o.standard_tag))),'Q divisor frame shift mismatch')
            q_descriptions.append(q)
        contract.update({'source_sorted_owners':[o.data()for o in source],'source_sorting_sign':sign,
            'P_definition':p_description,'Q_definitions':q_descriptions,
            'fiber_domains':[FullFiberDomain(o.seed,o.occurrence,o.standard_tag).descriptor()for o in owners],
            'definition_metadata_crosschecked':True,'independent_definition_review_is_external':True,
            'primitive_application':'universal raw transgression theorem applied on fresh increasing edges; then alternating extension',
            'fresh_raw_primitive_theorem_proved_in_note':True,
            'historical_source_order_equality':False,'primitive_source_implementation_review_accepted':False})
        contract['metadata_profile']=metadata_profile(contract)
        return contract
    def coefficient(self,*args,**kwargs):return actual_coefficient()
    def factor_terms(self,*args,**kwargs):return actual_coefficient()
    def owners(self,*args,**kwargs):return actual_coefficient()
