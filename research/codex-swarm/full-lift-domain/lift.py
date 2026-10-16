"""Exact tiny HPL executor and source-free full-lift owner/degree program.

Actual model coefficients and actual common fibers are never executable here.
"""
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
import json
from pathlib import Path
import sys

BASE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(BASE/'inserted-coefficients'))
import interfaces as I
need=I.need
SIGNS=(1,1,-1,1)
BOUNDS=((36,20),(42,23),(48,26),(54,29))
def parity(r):
    need(type(r)is int,'integer internal degree')
    return -1 if r%2 else 1

def zero(rows,cols=None):return tuple(tuple(Q(0)for _ in range(rows if cols is None else cols))for _ in range(rows))
def identity(n):return tuple(tuple(Q(i==j)for j in range(n))for i in range(n))
def add(a,b):
    need(len(a)==len(b)and all(len(x)==len(y)for x,y in zip(a,b)),'matrix sum shape')
    return tuple(tuple(x+y for x,y in zip(r,s))for r,s in zip(a,b))
def scale(c,a):return tuple(tuple(c*x for x in r)for r in a)
def transpose(a):return tuple(zip(*a))
def times(a,b):
    need(a and b and all(len(r)==len(b)for r in a),'matrix product shape')
    return tuple(tuple(sum((a[i][k]*b[k][j]for k in range(len(b))),Q(0))for j in range(len(b[0])))for i in range(len(a)))
def inverse(a):
    n=len(a);need(n and all(len(r)==n for r in a),'square inverse')
    m=[list(r)+list(s)for r,s in zip(a,identity(n))]
    for j in range(n):
        k=next((i for i in range(j,n)if m[i][j]),None);need(k is not None,'singular artificial matrix')
        m[j],m[k]=m[k],m[j];p=m[j][j];m[j]=[x/p for x in m[j]]
        for i in range(n):
            if i!=j:
                c=m[i][j];m[i]=[x-c*y for x,y in zip(m[i],m[j])]
    return tuple(tuple(r[n:])for r in m)
def checked_matrix(a):
    need(type(a)in(list,tuple)and a and all(type(r)in(list,tuple)for r in a),'literal artificial matrix')
    need(len(a)<=12 and all(len(r)==len(a[0])<=12 for r in a),'tiny matrix cap')
    need(all(type(x)is int or isinstance(x,Q)for r in a for x in r),'exact matrix entries')
    return tuple(tuple(Q(x)for x in r)for r in a)

class TinyContraction:
    """Validated artificial local contraction. No actual catalog path exists."""
    mode='synthetic'
    def __init__(self,d,inc,proj,h,grades):
        self.d=checked_matrix(d);self.inc=checked_matrix(inc);self.proj=checked_matrix(proj);self.h=checked_matrix(h)
        self.grades=tuple(grades);self.n=len(d);need(self.n<=12 and len(grades)==self.n and all(type(g)is int and 0<=g<=3 for g in grades),'four-term grades')
        self.E=times(self.inc,self.proj);z=zero(self.n)
        need(times(self.d,self.d)==z,'d squared')
        need(times(self.proj,self.inc)==identity(len(self.proj)),'PI')
        need(add(times(self.d,self.h),times(self.h,self.d))==add(identity(self.n),scale(-1,self.E)),'dH+Hd')
        need(times(self.h,self.h)==z,'H squared')
        need(times(self.h,self.inc)==zero(self.n,len(self.proj)),'HI')
        need(times(self.proj,self.h)==zero(len(self.proj),self.n),'PH')
        need(times(self.d,self.inc)==zero(self.n,len(self.proj))and times(self.proj,self.d)==zero(len(self.proj),self.n),'inclusion/projection chain maps')
        self.check_degree(self.d,1);self.check_degree(self.h,-1);self.check_degree(self.E,0)
        need(all(not x or self.grades[i]==1 for i,r in enumerate(self.inc)for x in r),'cohomology placed in K1')
    def check_degree(self,f,r):
        need(type(r)is int,'integer internal degree')
        need(all(not f[i][j]or self.grades[i]-self.grades[j]==r for i in range(self.n)for j in range(self.n)),'homogeneous End degree')
    def differential(self,f,r):
        self.check_degree(f,r)
        return add(times(self.d,f),scale(-parity(r),times(f,self.d)))
    def homotopy(self,f,r):
        self.check_degree(f,r)
        return add(times(self.h,f),scale(parity(r),times(times(self.E,f),self.h)))
    def inclusion(self,row_residual):return times(times(self.inc,transpose(row_residual)),self.proj)

class TinyLift:
    """Execute the SAME alternating-face/HPL recursion on artificial matrices."""
    mode='synthetic'
    def __init__(self,contractions,residual):
        need(type(contractions)is dict and 1<=len(contractions)<=8,'tiny artificial vertex domain')
        need(all(type(v)is int for v in contractions),'literal artificial vertex IDs')
        need(all(type(c)is TinyContraction for c in contractions.values()),'artificial contractions only')
        ds={c.d for c in contractions.values()};need(len(ds)==1,'fixed original resolution frame/differential')
        self.local=contractions;self.R=residual;self.calls=[]
    @lru_cache(maxsize=2048)
    def component(self,s,vertices):
        need(type(s)is int and 0<=s<=3 and type(vertices)is tuple and len(vertices)==3+s,'lift component arity')
        need(all(type(v)is int and v in self.local for v in vertices),'literal artificial vertex IDs')
        need(tuple(sorted(vertices))==vertices and len(set(vertices))==len(vertices),'increasing artificial tuple')
        c=self.local[vertices[0]]
        if s==0:return c.inclusion(checked_matrix(self.R(vertices)))
        f=self.delta(s-1,vertices);self.calls.append((s,vertices[0],vertices))
        return scale(SIGNS[s],c.homotopy(f,1-s))
    def delta(self,s,vertices):
        need(len(vertices)==4+s,'delta component arity');n=next(iter(self.local.values())).n
        out=zero(n)
        for j in range(len(vertices)):out=add(out,scale((-1)**j,self.component(s,vertices[:j]+vertices[j+1:])))
        return out

def _ordered_owners(owners,length):
    need(type(owners)in(tuple,list)and len(owners)==length and all(type(o)is I.FullOwner for o in owners),'complete lift owners')
    need(len({o.seed for o in owners})==1 and len({o.occurrence for o in owners})==len(owners),'coherent distinct owned occurrences')
    need(all(owners[j].source_key<owners[j+1].source_key for j in range(len(owners)-1)),'strict source-first common tuple')
    return tuple(owners)

def owner_tuple(owners,s):
    need(type(s)is int and 0<=s<=3,'J0..J3')
    return _ordered_owners(owners,3+s)

def lift_terms(s,owners):
    """Finite exact face words with ownership retained; no source values.

    Expands only at most120 face words, not common-cover labels or matrices.
    Each H records its owner before its next face deletion.
    """
    owners=owner_tuple(owners,s)
    def recurse(level,current,prefix,sign,word):
        if level==0:
            return [{'coefficient':sign,'operator_word':word+[{'op':'j','owner':current[0].data(),'transpose_row_input_once':True}],
                'Rsharp_owners':[o.data()for o in current],'retained_prefix_owners':[o.data()for o in prefix],
                'all_factor_owners':[o.data()for o in prefix+current]}]
        out=[];first=current[0]
        hom={'op':'H_End','input_internal_degree':1-level,'owner':first.data(),
            'formula':'H_K F+(-1)^r (IP)F H_K','restriction_frame':'original resolution; no row conjugation'}
        for j in range(len(current)):
            out.extend(recurse(level-1,current[:j]+current[j+1:],prefix+(first,),sign*SIGNS[level]*(-1)**j,
                word+[hom,{'op':'signed_Cech_face','deleted_owner':current[j].data(),'face_index':j}]))
        return out
    return {'schema':'JC01-full-lift-face-program-v1','component':'J'+str(s),'bidegree':(2+s,-s),
        'target_owners':[o.data()for o in owners],'terms':recurse(s,owners,(),1,[]),
        'source_evaluated':False,'physical_execution_authorized':False}

def domain_ledger():
    return {'source':{'carrier':32,'legal':18,'standard':5251},
        'components':[{'id':'J'+str(s),'cech':2+s,'internal':-s,'carrier':c,'legal':l,'standard':5251}for s,(c,l)in enumerate(BOUNDS)],
        'common_outer_partition':{'carrier':54,'legal':29,'standard_unit_order':5251},
        'whole_standard_extension_from_ledger_alone':False}

def actual_coefficient(*args,**kwargs):raise I.PhysicalAdmissionMissing('full-lift domain has no physical coefficient/fiber execution release')

def original_frame(s):
    need(type(s)is int and 0<=s<=3,'lift component frame')
    return {'matrix_frame':'original-resolution','internal_degree':-s,'full_sign_deck_product_removed_count':1,
        'tau_power':-s-2,'scalar_L_applied_after_this_conversion':s==2,
        'frozen_frame_derivatives_used':False}

def _outer_contract(owners,s,target_tags,is_boundary):
    """Whole homogeneous numerator/target indices, not coefficient evidence."""
    need(type(s)is int and 0<=s<=3,'J0..J3 domain')
    owners=_ordered_owners(owners,3+s+int(is_boundary))
    need(type(target_tags)in(tuple,list)and target_tags and all(type(t)is int and 0<=t<16 for t in target_tags),'outer standard target')
    need(all(o.standard_tag in target_tags for o in owners),'retained owner standard equation is not certified a target unit')
    factors=[]
    for o in owners:
        d=4 if o.carrier==5 else 5
        factors.append({'owner':o.data(),'carrier_power':54,'legal_powers':[29]*4,'standard_powers':[5251]*4,
            'degree':tuple(54*d+29*(1+2*((o.legal_mask>>i)&1))+5251 for i in range(4)),
            'standard_tag_is_retained':True})
    degree=tuple(sum(f['degree'][i]for f in factors)-s-2 for i in range(4))
    return {'schema':'JC01-whole-outer-domain-indices-v1','component':('delta 'if is_boundary else'')+'J'+str(s),'factors':factors,
        'cech_degree':2+s+int(is_boundary),'internal_degree':-s,
        'whole_numerator_homogeneous_degree':degree,'target_standard_tags':list(target_tags),
        'source_bundle_degree':[-s-2]*4,'outer_weight_divisibility':{'carrier':54,'legal':29},
        'standard_factors_are_target_units_not_partition_divisors':True,
        'regularity_theorem':'clear whole actual homogeneous coefficient on smooth normal Y; Pi_out weights every sampled owner; H_rho weights inserted owners only and retains suffix carrier/legal divisors in the common-cover domain',
        'fully_weighted_Pi_out_value_extends_full_standard_target':True,
        'prism_full_standard_extension_scope':'appropriately cleared WHOLE coefficient with retained owned suffix divisors',
        'uncleared_prism_full_standard_extension_claimed':False,
        'index_checks_are_not_source_clearing_proof':True,'physical_execution_authorized':False}

def outer_owner_contract(owners,s,target_tags):return _outer_contract(owners,s,target_tags,False)
def outer_boundary_contract(owners,s,target_tags):return _outer_contract(owners,s,target_tags,True)

def _load(name,path):
    need(path.is_file(),'canonical source producer not yet present')
    if name in sys.modules:
        need(Path(sys.modules[name].__file__).resolve()==path.resolve(),'canonical module path changed')
        return sys.modules[name]
    if str(path.parent)not in sys.path:sys.path.insert(0,str(path.parent))
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

class ActualFullLiftApplication:
    """Canonical RS construction plus exact owner-parametrized lift words.

    No catalog, residual callback, closure Boolean or proof status is accepted.
    Descriptions apply the written theorem; independent implementation review
    remains external and all actual coefficient/fiber entry points refuse.
    """
    mode='physical'
    def __init__(self,repo=None):
        root=Path(__file__).resolve().parents[3]
        need(repo is None or Path(repo).resolve()==root,'canonical repository only');self.repo=root
    def _source(self):
        mod=_load('jc01_actual_RS',BASE/'full-source-application'/'r_binding.py')
        return mod.ActualFullSourceApplication(repo=self.repo)
    def source_definition(self,owners):return self._source().describe(owner_tuple(owners,0))
    def describe(self,s,owners):
        owners=owner_tuple(owners,s);program=lift_terms(s,owners)
        source=self._source();source_definition=source.describe(owners[-3:])
        need(source_definition['schema']=='actual-fresh-full-source-application-v1','canonical complete source schema')
        hom=source_definition['source_homogeneity']
        need(hom['deck_character']==[1,1,1,1]and hom['scalar_character_eigensheaf']=='O(-2,-2,-2,-2)', 'actual full-sign physical source character')
        need(hom['matrix_frame']=='actual physical row-End; conjugation/line frames retained','source row frame was replaced')
        # This parameterized SAME constructor is attached to every source leaf.
        # One explicit instance records its definition; face words bind the
        # other owner tuples without duplicating the large source certificate.
        source_leaves=[];seen=set()
        for t in program['terms']:
            key=json.dumps(t['Rsharp_owners'],sort_keys=True)
            if key not in seen:seen.add(key);source_leaves.append(t['Rsharp_owners'])
        TR=_load('jc01_reviewed_transport',BASE/'transport-binding'/'transport_binding.py')
        template=TR.build_template()
        need(len(template['scalar_maps'])==20 and len(template['requests'])==32,'complete selected scalar family')
        out={'schema':'JC01-actual-full-lift-application-v1','source_definition_instance':source_definition,
            'source_leaf_constructor':'full-source-application/r_binding.py:ActualFullSourceApplication(repo).describe',
            'source_leaf_bindings':source_leaves,'lift_program':program,'frame':original_frame(s),
            'physical_source_homogeneity':hom,
            'outer_whole_domain':outer_owner_contract(owners,s,[o.standard_tag for o in owners]),
            'source_pins':source.source_pins(),'uniform_transport_source_pins':template['source_pins'],
            'all20_scalar_maps':template['scalar_maps'],'all32_weighted_tests':template['requests'],
            'scalar_terminal_component':'J2 only, AFTER original-frame tau^-4 conversion',
            'top_J3_is_required_closure_witness':True,
            'actual_homogeneous_source_and_owned_pole_application':'PROOF.md sections3-5; depends on canonical RS actual physical source/closure, PB/QB/FD whole scalar identity, and pinned contraction/frame proofs',
            'historical_order_identity':False,'physical_coefficients_evaluated':False,'actual_fibers_enumerated':False,
            'physical_execution_authorized':False,'obstruction_decided':False}
        # Explicit aggregate metadata sizes; no arithmetic or memory release.
        arrays=[]
        def count(v,path=''):
            if type(v)is dict:
                for k,a in v.items():
                    if k in('dag','nodes')and type(a)is list:arrays.append({'path':path+'/'+k,'nodes':len(a)})
                    count(a,path+'/'+k)
            elif type(v)in(list,tuple):
                for j,a in enumerate(v):count(a,path+'/'+str(j))
        count(out)
        out['metadata_profile']={'AST_arrays':arrays,'aggregate_stored_AST_nodes':sum(a['nodes']for a in arrays),
            'pre_profile_JSON_bytes':len(json.dumps(out,sort_keys=True,separators=(',',':'),allow_nan=False).encode()),
            'physical_arithmetic_cost_or_memory_admission':False}
        return out
    def coefficient(self,*args,**kwargs):return actual_coefficient()
    def factor_terms(self,*args,**kwargs):return actual_coefficient()
    def owners(self,*args,**kwargs):return actual_coefficient()
