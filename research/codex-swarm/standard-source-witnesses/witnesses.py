"""Coefficient-free standard extension theorem bookkeeping.

Proposal validation is structural only. It never authenticates a physical
source by trusting a string, hash, status, or a Boolean field.
"""
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys

SHARED=Path(__file__).resolve().parent.parent/'inserted-coefficients'
if str(SHARED)not in sys.path:sys.path.insert(0,str(SHARED))
import interfaces as I
need=I.need

PAIR_ORDER=((0,1),(2,3))
OBLIGATIONS=('actual_homogeneous_P_identity','fixed_partition_Qhat_identity',
    'fresh_source_order_and_frame_identity','old_scalar_exactness_and_domain_identity')
ORDER='auxiliary5-first, primary0..4, numeric-low-bit-mask, high-bit-standard-tag'

def strict_equal(a,b):
    if type(a)is not type(b):return False
    if type(a)is list:return len(a)==len(b)and all(strict_equal(x,y)for x,y in zip(a,b))
    if type(a)is dict:return set(a)==set(b)and all(strict_equal(a[k],b[k])for k in a)
    return a==b

def owner_data(owner):return json.loads(json.dumps(owner.data()))

def pair(value):
    need(type(value)in(tuple,list)and len(value)==2 and all(type(x)is int for x in value)and tuple(value)in PAIR_ORDER,'ordered pair')
    return tuple(value)

def bits(t):
    need(type(t)is int and 0<=t<16,'standard tag')
    return tuple((t>>(3-i))&1 for i in range(4))

def full_owners(owners):
    need(type(owners)in(tuple,list)and len(owners)==3 and all(isinstance(o,I.FullOwner)for o in owners),'complete source triple owners')
    need(len({(o.seed,o.occurrence)for o in owners})==3,'three owned occurrences required')
    return tuple(owners)

def divisor_degree(owner,p):
    need(isinstance(owner,I.FullOwner),'full divisor owner');p=pair(p)
    carrier_degree=4 if owner.carrier==5 else 5
    return tuple(14*carrier_degree+((3 if(owner.legal_mask>>i)&1 else 1)if i in p else 0)for i in range(4))

def numerator_degree(owners,p):
    owners=full_owners(owners);p=pair(p);degrees=[divisor_degree(o,p)for o in owners]
    return tuple(sum(d[i]for d in degrees)+(-2 if i in p else 0)for i in range(4))

def regular(tags,e,p):
    e=I.exponent(e);p=pair(p);rows=[bits(t)for t in tags]
    for i in range(4):
        states={row[i]for row in rows}
        if states=={0}and e[i]<0:return False
        if states=={1}and e[i]>(-2 if i in p else 0):return False
    return True

def _terms(poly):
    need(type(poly)is dict and len(poly)<=32,'tiny artificial polynomial dictionary')
    out={}
    for e,c in poly.items():
        e=I.exponent(e);need(type(c)is int or isinstance(c,Fraction),'exact artificial coefficient')
        if c:out[e]=Fraction(c)
    return out

def synthetic_extension_control(owners,p,numerator,quotients,mode='synthetic'):
    """Multiply only tiny artificial data after checking the theorem premises.

    Local regularity of rho/C means Qhat exponent >=0 at a finite owner,
    and <= -deg(C) at an infinity owner, in the global finite frame.
    No actual source adapters or files can be executed through this helper.
    """
    I.require_synthetic(mode);owners=full_owners(owners);p=pair(p)
    need(type(quotients)in(tuple,list)and len(quotients)==3,'three owned quotient polynomials')
    P=_terms(numerator);Qs=[_terms(q)for q in quotients];D=numerator_degree(owners,p)
    need(all(all(0<=e[i]<=D[i]for i in range(4))for e in P),'P must have its exact owner-dependent homogeneous degree')
    for o,q in zip(owners,Qs):
        c=divisor_degree(o,p);b=bits(o.standard_tag)
        need(all(all(e[i]<=-c[i]if b[i]else e[i]>=0 for i in range(4))for e in q),'Qhat lacks regular O(-deg C) target extension')
    need(len(P)*max(1,len(Qs[0]))*max(1,len(Qs[1]))*max(1,len(Qs[2]))<=4096,'tiny artificial convolution cap')
    result={}
    for terms in itertools.product(P.items(),*(q.items()for q in Qs)):
        e=tuple(sum(t[0][i]for t in terms)for i in range(4));c=Fraction(1)
        for exponent,value in terms:c*=value
        result[e]=result.get(e,Fraction(0))+c
    result={e:c for e,c in result.items()if c}
    need(all(regular([o.standard_tag for o in owners],e,p)for e in result),'extension conclusion failed')
    return result

def proposal(owners,p):
    """An explicitly unbound handoff template; this is never a source proof."""
    owners=full_owners(owners);p=pair(p);source,sign=I.sorted_source(owners)
    return {'schema':'whole-standard-source-witness-proposal-v1',
        'owners':[owner_data(o)for o in owners], 'pair':list(p),
        'target_standard_tags':[o.standard_tag for o in owners],
        'source_sorted_owners':[owner_data(o)for o in source],'source_sorting_sign':sign,
        'source_order':ORDER,'numerator_scope':'whole_actual_F=b-tr(C)/2',
        'numerator_degree':list(numerator_degree(owners,p)),
        'divisor_degrees':[list(divisor_degree(o,p))for o in owners],
        'extension_scope':'whole_coefficient_on_standard_target',
        'obligations':{k:{'status':'unbound','candidate_proof_sha256':None}for k in OBLIGATIONS},
        'source_faithful_oracle_identity_accepted':False,'physical_execution_authorized':False,
        'actual_source_evaluated':False,'admitted':False}

def validate_proposal(data):
    """Check a candidate's shape and theorem indices, not its proof truth."""
    need(type(data)is dict,'proposal object')
    raw=data.get('owners');need(type(raw)is list and len(raw)==3,'full three-owner list')
    owners=[]
    for o in raw:
        need(type(o)is list and len(o)==5,'five-field owner')
        owners.append(I.FullOwner(*o))
    expected=proposal(owners,data.get('pair'))
    need(set(data)==set(expected),'exact proposal fields required')
    for key,value in expected.items():
        if key!='obligations':
            # Equality alone accepts False==0; admission fields require bool.
            if type(value)is bool:need(type(data[key])is bool and data[key]is False,'proposal cannot authenticate or release execution')
            else:need(strict_equal(data[key],value),'proposal indices/scope changed: '+key)
    obs=data['obligations'];need(type(obs)is dict and set(obs)==set(OBLIGATIONS),'obligation slots')
    for item in obs.values():
        need(type(item)is dict and set(item)=={'status','candidate_proof_sha256'},'proof proposal fields')
        need(item['status']in('unbound','candidate'),'a string cannot authenticate a source proof')
        h=item['candidate_proof_sha256']
        if item['status']=='unbound':need(h is None,'unbound proof must stay empty')
        else:need(type(h)is str and len(h)==64 and all(c in'0123456789abcdef'for c in h),'candidate proof hash')
    return {'shape_valid':True,'conditional_extension_theorem_applicable_if_obligations_proved':True,
        'actual_source_identity_accepted':False,'physical_execution_authorized':False,'admitted':False}

def require_actual_admission(*args,**kwargs):
    raise I.PhysicalAdmissionMissing('schema checks do not authenticate P/Qhat/source or discharge actual proof obligations')
