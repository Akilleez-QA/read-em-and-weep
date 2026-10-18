"""Universal owner-aware regularization certificate; no physical source inputs.

All algebra tests use independent formal indeterminates/functions. No source
polynomial reader, evaluator, compiler import, or execution-admission API exists.
"""
from dataclasses import dataclass
from collections import Counter

@dataclass(frozen=True, order=True)
class Owner:
    seed: int
    occurrence: int
    carrier: int
    legal_mask: int
    standard_tag: int
    def __post_init__(self):
        vals=(self.seed,self.occurrence,self.carrier,self.legal_mask,self.standard_tag)
        if not all(type(x) is int for x in vals): raise ValueError('integer full-owner fields')
        if self.occurrence<0 or self.carrier not in range(6) or not 0<=self.legal_mask<16 or not 0<=self.standard_tag<16:
            raise ValueError('owner domain')
    @property
    def geometric(self): return (self.carrier,self.legal_mask,self.standard_tag)

def standard_bits(tag):
    if type(tag) is not int or not 0<=tag<16: raise ValueError('standard tag')
    return tuple((tag>>(3-i))&1 for i in range(4))

def active_weight(v):
    """Necessary structural nonzero predicate, not a nonvanishing claim."""
    bits=standard_bits(v.standard_tag);s=sum(bits)
    if any(((v.legal_mask>>i)&1) and not bits[i] for i in range(4)): return False
    if v.carrier!=5 and v.carrier>s: return False
    if s==4 and v.carrier not in (4,5): return False
    return True

def alternating_sort(vertices):
    # Occurrence labels do not turn equal geometric vertices into distinct opens.
    # Source-first order uses star BEFORE the primaries.
    keys=[(-1 if v.carrier==5 else v.carrier,v.legal_mask,v.standard_tag) for v in vertices]
    if len(set(keys))!=len(keys): return 0,tuple(vertices)
    sign=(-1)**sum(keys[i]>keys[j] for i in range(len(keys)) for j in range(i+1,len(keys)))
    return sign,tuple(v for _,v in sorted(zip(keys,vertices),key=lambda t:t[0]))

def source_F_sort(vertices):
    """Alternating pullback s*F: repeated SOURCE labels vanish across tags.

    This is source-specific and must not be used for a general common cochain.
    The returned vertices retain all five owner fields even in a zero branch.
    """
    sign,ordered=alternating_sort(vertices)
    source_keys=[(v.carrier,v.legal_mask) for v in vertices]
    if len(set(source_keys))!=len(source_keys):sign=0
    return sign,ordered

def cancel_owned(denominator,clearing):
    """No merging by polynomial value; keys are (Owner,kind,coordinate)."""
    for ledger in (denominator,clearing):
        for (owner,kind,i),a in ledger.items():
            if not isinstance(owner,Owner) or kind not in ('H','L','Z') or type(a) is not int or a<0:
                raise ValueError('owned factor')
            if (kind=='H' and i is not None) or (kind!='H' and (type(i) is not int or i not in range(4))):
                raise ValueError('factor coordinate')
    if any(clearing.get(k,0)<a for k,a in denominator.items()): raise ValueError('missing matching clearance')
    return {k:a-denominator.get(k,0) for k,a in clearing.items() if a>denominator.get(k,0)}

def derivative_orders(orders):
    if any(type(a) is not int or a<0 for a in orders.values()): raise ValueError('order')
    return {k:a+1 for k,a in orders.items() if a>0}

def prism_branch(output,inserted):
    if len(output)!=2 or len(inserted) not in (1,2): raise ValueError('prism arity')
    if alternating_sort(output)[0]!=1: raise ValueError('increasing source-first output edge required; extend alternatingly separately')
    if any(v.standard_tag!=output[i].standard_tag for i,v in enumerate(inserted)):
        raise ValueError('inserted tag must equal designated output row')
    suffix=output if len(inserted)==1 else output[1:]
    sign,sorted_vertices=source_F_sort(tuple(inserted)+tuple(suffix))
    if any(not active_weight(v) for v in inserted): sign=0
    return {'sign':sign*(1 if len(inserted)==1 else -1),'source':sorted_vertices,'inserted':tuple(inserted),'suffix':tuple(suffix)}

def h_adjoint(cell,exponents,twists,pivot):
    if len(cell)!=4 or len(exponents)!=4 or len(twists)!=4 or pivot not in range(4): raise ValueError('tensor shape')
    if any(s not in ('A','B','C') for s in cell) or any(n not in (0,-2) for n in twists): raise ValueError('tensor state')
    target=list(cell)
    for i in range(pivot):
        if twists[i]==0:
            if cell[i] not in ('A','B') or exponents[i]!=0: return None
            target[i]='B'
        elif cell[i]!='C' or exponents[i]!=-1: return None
    state=cell[pivot];e=exponents[pivot]
    if state=='A' and e>=0: sign=-1
    elif state=='B' and e<0 and e<=twists[pivot]: sign=1
    else: return None
    sign*=(-1)**cell[:pivot].count('C');target[pivot]='C'
    return sign,tuple(target),tuple(exponents)

def differentiated_h_adjoint(cell,kappa,twists,pivot,axis):
    if twists[axis]!=0: raise ValueError('complementary input character required')
    factor=kappa[axis]+1
    if factor==0:return None
    shifted=list(kappa);shifted[axis]+=1
    result=h_adjoint(cell,shifted,twists,pivot)
    return None if result is None else (factor*result[0],result[1],result[2])

def support_metadata():
    lo=-3*(481+2)-3*73;hi=217+3*1677
    return {'standard_branch_finite_box':[lo,hi], 'standard_pole':max(-lo,hi+2),
            'raw_weight_degree':max(1677+70,481+70+2),
            'scalar_orders':{'carrier':14,'legal':1,'standard':5250},
            'derivative_orders':{'carrier':15,'legal':2,'standard':5251},
            'physical_source_verified':False,'global_regularization_groups_discharged':0,
            'execution_admitted':False}

def inserted_reversal_bound(pair_coordinate,mask,carrier_degree=5):
    """Maximum negative exponent from Qhat; quotient infinity bound <=481.
    Keep coupled legal degree/quotient cases rather than independent maxima.
    """
    if type(mask) is not int or mask not in (0,1) or carrier_degree not in (4,5):raise ValueError('reversal case')
    legal_quotient_degree=(1-mask) if pair_coordinate else 2
    legal_hom_degree=(1 if mask==0 else 3) if pair_coordinate else 0
    return 481+legal_quotient_degree+14*carrier_degree+legal_hom_degree

def standard_exponent_admissible(edge_tags,exponent,twist):
    """Necessary/sufficient monomial regularity on this standard edge."""
    if len(edge_tags)!=2 or len(exponent)!=4 or len(twist)!=4:raise ValueError('shape')
    a,b=map(standard_bits,edge_tags)
    return all(not (a[i]==b[i]==0 and exponent[i]<0) and
               not (a[i]==b[i]==1 and exponent[i]>twist[i]) for i in range(4))

def full_sum_recipe(pair=(0,1)):
    if pair not in ((0,1),(2,3)):raise ValueError('pair')
    return {
        'schema':'combined-inner-regularization-identity-v1',
        'pair':list(pair),
        'output_edge':'increasing source-first common edge; extend the complete result alternatingly to reversed edges; repeated common edge zero',
        'definitions':{
            'C_v':'H_v^14 * product_(i in pair) ell_vi',
            'Z_ab':'product_i Z_(a,i)^5250 Z_(b,i)^5250',
            'D_ab':'C_a C_b Z_ab',
            'Qhat_v':'Qcarrier_v(local) * product_pair Qline_vi(local) * product_complement L_vi(local) * product_(e_vi=1) x_i^(-14*d_v-deg(ell_vi)*[i in pair])',
            'B_ab':'[R(K_cov Pi + A h S Pi)F]_ab; complete standard branch sum',
            'N_ab':'C_a C_b Z_ab B_ab + Z_ab sum_u Qhat_u P_[u,a,b] - C_a Z_ab sum_(u,v) Qhat_u Qhat_v P_[u,v,b]',
            'source_identity':'P_[r,s,t] = C_r C_s C_t (s*F)_[r,s,t]; source-first sign; repeated (carrier,legal_mask) zero even across standard tags',
            'common_alternation':'general common cochains vanish only on repeated (carrier,legal_mask,standard_tag); full five-field denominator owners never merge',
            'identity':'T(F)_ab=N_ab/D_ab',
            'derivative':'partial_i T(F)_ab=(Delta_ab partial_i N_ab - N_ab sum_f a_f(partial_i f) Delta_ab/f)/(D_ab Delta_ab)',
            'Delta_ab':'product of each positive owned factor f in D_ab once; distinct owners are not merged',
        },
        'branches':[
            {'kind':'standard','required':'B_ab complete sum; per-coordinate standard_exponent_admissible; support [-1668,5248]^4'},
            {'kind':'prism1','sign':1,'inserted_tags':['r(a)'],'suffix':['a','b'],'numerator_padding':'Z_ab'},
            {'kind':'prism2','sign':-1,'inserted_tags':['r(a)','r(b)'],'suffix':['b'],'numerator_padding':'C_a Z_ab'},
        ],
        'inserted_negative_bounds':{'pair':max(inserted_reversal_bound(True,m) for m in (0,1)),
                                    'complement':max(inserted_reversal_bound(False,m) for m in (0,1))},
        'source_clearing_verified_by_this_artifact':False,
        'generic_full_sum_identity_proved':True,
        'execution_admitted':False,
    }
