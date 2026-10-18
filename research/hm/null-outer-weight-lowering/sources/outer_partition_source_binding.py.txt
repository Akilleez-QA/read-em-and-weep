"""Exact, unevaluated outer carrier54/legal29 source definition.

This module binds finite formulas; it has no polynomial evaluator or expansion
entry point. Index sums stay symbolic, including the large multinomial domain.
Every formula lives in Z[x_i,t_i] on its owner's standard chart.
"""
from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib
import json
from owned_scalar_denominator_binding import VertexLabel, decode_standard_tag, decode_legal_mask

CARRIER_POWER = 54
LEGAL_POWER = 29
STANDARD_BOUND = 5251
PIN = '08b73637d4136f91606aad332c46cafd064417f8'
PUBLIC_BLOBS = {
    'outer-pinned-source-identity.md': '7e12e8c7479427db87cd496763f5f003005af9c5',
    'outer-pinned-frames-and-poles.md': '46470b5a7198be2f8c39f9cb5f5a904ae355ec97',
}

def authenticate_public_sources():
    results=[]
    for filename,expected in PUBLIC_BLOBS.items():
        raw=Path(__file__).with_name(filename).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if blob!=expected: raise ValueError('pinned public source blob mismatch: '+filename)
        results.append({'file':filename,'git_blob':blob,'sha256':hashlib.sha256(raw).hexdigest(),'commit':PIN})
    return results

BASE = f'https://github.com/Akilleez-QA/read-em-and-weep/blob/{PIN}/research/hm/current-scalar-geometric-dependencies/'

@dataclass(frozen=True)
class FiniteFormula:
    """A typed finite polynomial formula, with bound variables and exact domain.

    Powers in body must be nonnegative on index_domain. quotient names below
    are polynomial definitions, not rational divisions or localization grants.
    """
    name: str
    coefficient_ring: str
    bound_variables: tuple
    index_domain: str
    body: str
    nonnegative_exponents: tuple
    def data(self): return asdict(self)

@dataclass(frozen=True)
class PartitionChart:
    standard_tag: int
    carrier_power: int = CARRIER_POWER
    legal_power: int = LEGAL_POWER
    def __post_init__(self):
        decode_standard_tag(self.standard_tag)
        for n in (self.carrier_power,self.legal_power):
            if type(n) is not int or n < 1: raise ValueError('positive integral partition power required')
    @property
    def bits(self): return decode_standard_tag(self.standard_tag)
    @property
    def s(self): return sum(self.bits)
    @property
    def M(self): return 2*self.carrier_power-1
    @property
    def threshold(self): return 5*self.M
    @property
    def L(self): return (self.s+1)*(self.threshold-1)+1
    def formulas(self):
        s,N,M,T,L=self.s,self.carrier_power,self.M,self.threshold,self.L
        n=self.legal_power; ml=2*n-1
        ring='Z[x_i for e_i=0, t_i for e_i=1]'
        f=lambda name,variables,domain,body,proof: FiniteFormula(name,ring,variables,domain,body,proof).data()
        return [
            f('v_j',('A',),'A subset {0,1,2,3}; |A|=j; 0<=j<=4',
              'sum_A product_(i in A)(x_i if e_i=0 else 1) * product_(i not in A)(1 if e_i=0 else t_i)',('all powers 0 or 1',)),
            f('H_k',('u_i for e_i=0',),'u_i>=0; sum_i u_i=k; 0<=k<=s',
              'sum_u product_(e_i=0) x_i^u_i',('u_i>=0; empty product=1; empty sum=0 unless k=0',)),
            f('B_j',('n_0,...,n_s',),f'0<=j<={s}; n_i>=0; sum_i n_i={L}; n_j>={T}; n_i<{T} for i<j',
              f'sum_n multinomial({L};n) * product_(i=0..s) [(-1)^(s-i)*H_(s-i)]^n_i * product_(i=0..s) v_i^(n_i-{T}*[i=j])',
              ('n_i>=0','n_j>=threshold','multinomial is integer, defined by chained binomials, not inversion in coefficient ring')),
            f('Cbar_j',('k',),f'{N}<=k<={M}',
              f'sum_k binom({M},k)*h_j^(k-{N})*(v_2*a)^({M}-k)',('k>=N','k<=M')),
            f('Dbar_j',('k',),f'0<=k<{N}',
              f'sum_k binom({M},k)*h_j^k*v_2^({M}-k)*a^({M}-k-{N})',('M-k-N>=0 since M=2N-1 and k<=N-1',)),
            f('carrier_quotient',('j',),f'j=0,...,{s}',
              'Q_b=B_b*Cbar_b for b<=s; Q_b=0 for s<b<=4; Q_5=sum_j B_j*Dbar_j',('all defining sums polynomial','carrier5 means a; never primary h_5')),
            f('line_quotient_infinity_zero',('k',),f'{n}<=k<={ml}',
              f'sum_k binom({ml},k)*t_i^(2*k-{n})*(1-t_i^2)^({ml}-k)',('2*k-n>=0','ml-k>=0')),
            f('line_quotient_infinity_one',('k',),f'0<=k<{n}',
              f'sum_k binom({ml},k)*t_i^(2*k)*(1-t_i^2)^({ml}-k-{n})',('ml-k-n>=0',)),
            f('line_quotient_finite',(), 'mask bit 0 or 1',
              'Q_i0=1; Q_i1=0',('zero polynomial certifies divisibility by [x_i*(x_i^2-1)]^n without division',)),
            f('rho',(), 'b in {0,...,5}; m in {0,...,15}',
              f'H_b^{N}*Q_b * product_(i=0..3) ell_(m_i,i)^{n}*Q_(i,m_i)',('all factors polynomial','no v_j inversion')),
            f('rho_quotient',(), 'same full owner as rho',
              'Q_b*product_(i=0..3) Q_(i,m_i)',('exact quotient after matching owned carrier/legal clearing factors',)),
        ]
    def data(self):
        return {'standard_tag':self.standard_tag,'standard_bits':self.bits,'s':self.s,
                'carrier_power':self.carrier_power,'legal_power':self.legal_power,
                'M':self.M,'threshold':self.threshold,'L':self.L,
                'line_M':2*self.legal_power-1,'formulas':self.formulas()}

def release_gate():
    return {'actual_source_admitted':False,'Laurent_admitted':False,
            'physical_polynomial_expansion':False,'physical_polynomial_evaluation':False,
            'arithmetic_cost_certificate':False,'resource_gate_passed':False,
            'private_resource_configuration_omitted':True}

def build_outer_partition_binding(owner):
    if not isinstance(owner,VertexLabel): raise ValueError('complete occurrence owner required')
    authenticate_public_sources()
    tags=range(16) if isinstance(owner.standard_tag,tuple) else (owner.standard_tag,)
    return {'schema':'outer-partition-source-v1','owner':owner.data(),
        'carrier_power':CARRIER_POWER,'legal_power':LEGAL_POWER,
        'chart_selection':{'selector':('standard_tag',owner.data()),'cases':[PartitionChart(t).data() for t in tags]},
        'carrier_selection':{'selector':('carrier',owner.data()),'domain':(0,1,2,3,4,5)},
        'legal_selection':{'selector':('legal_mask',owner.data()),'bit_order':'low bit i'},
        'standard_bit_order':'high bit 3-i','definitions':definitions(), 'gate':release_gate()}

def validate_outer_partition_binding(binding):
    if not isinstance(binding,dict): raise ValueError('binding record required')
    fields=binding.get('owner',())
    if len(fields)!=5: raise ValueError('complete owner tuple required')
    owner=VertexLabel(*fields)
    if binding != build_outer_partition_binding(owner): raise ValueError('partition formula, owner, or gate mutation')
    return True

def shared_definition():
    """Source-definition strings and finite domains, not executable arithmetic AST."""
    return {'schema':'outer-partition-source-v1','representation':'typed finite-formula source-definition strings; NOT executable AST/lowering',
            'public_source_authentication':authenticate_public_sources(),
            'chart_cases':[PartitionChart(t).data() for t in range(16)],
            'definitions':definitions(),'gate':release_gate()}

def bind_reference(owner):
    if not isinstance(owner,VertexLabel): raise ValueError('complete occurrence owner required')
    return {'definition':'outer-partition-source-v1','owner':owner.data(),
            'standard_chart_selector':('standard_tag',owner.data()),
            'carrier_selector':('carrier',owner.data()),
            'legal_mask_selector':('legal_mask',owner.data()),
            'source_formula_bound':True,'executable_AST_lowered':False,
            'source_pole_domain_proved_by_this_record':False,
            'regularized_Laurent_multiplier_proved':False}

def definitions():
    return {
      'homogeneous_generators':'h_j=v_j^5-v_0*v_1*v_2*v_3*v_4; a=v_0*v_1*v_3*v_4; H_5=a; H_j=h_j for 0<=j<=4',
      'generator_multidegrees':{'primary':5,'auxiliary':4,'legal_mask0':1,'legal_mask1':3},
      'legal_local':'finite: ell_0=1, ell_1=x_i*(x_i^2-1); infinity: ell_0=t_i, ell_1=1-t_i^2',
      'unit_identity':'sum_(j=0..s) (-1)^(s-j)*H_(s-j)*v_j=1',
      'multinomial':'multinomial(L;n)=product_(i=0..s) binom(L-sum_(h<i)n_h,n_i)',
      'chart_pullback':'v_local=tau*v_finite(x_i=1/t_i); tau=product_(e_i=1)t_i; h_local=tau^5*h_finite; a_local=tau^4*a_finite',
      'legal_pullback':'ell_local=t_i^d*ell_finite(1/t_i), d=1 for mask0, d=3 for mask1; no extra t inverse is introduced in local ratios',
      'section_frame':'c_local=tau^(r-2)*c_finite(1/t_i); this is full-sign End degree r; scalar rho has twist zero and is restricted as a function',
      'standard_equation':'Z_e=Y_i for e_i=0 else X_i; Z_e=1 in its own chart; Z_e is a unit on every target intersection retaining this standard tag',
      'standard_owner_rule':'retain bound5251 for each actual occurrence and coordinate; a target intersection must include the identical standard tag before treating Z_e as unit',
      'cancellation':'rho_v/(H_v^54*product_i ell_vi^29)=Q_v as a polynomial identity on U_e, proved before evaluation; use only matching full owner v',
      'smaller_poles':'for actual exponents a<=54,b_i<=29, multiply Q_v by H_v^(54-a)*product ell_vi^(29-b_i); no arbitrary inverse or owner merging',
      'derivative_rule':'cancel inserted scalar-prism carrier/legal factors before differentiating; raw Leibniz summands do not have independent clearance certificates',
      'target_restriction':'restrict fixed chart weights to intersections; never recompute with a new standard tag or independently on faces',
      'proof_obligations':[
        'Source must satisfy carrier<=54 and legal<=29 per actual occurrence in homogeneous physical frames, with standard<=5251 retained.',
        'Do not use whole-cochain cancellation to admit an uncombined raw summand; validate the selected expression domain separately.',
        'Use one source ordering and alternating extension; no nonlinear re-evaluation on reordered tuples.',
        'No factor cancellation across distinct owners even if their polynomials agree.',
        'Finite/infinity substitutions and full-sign frame conversion happen exactly once, including signs of invariant derivatives.',
        'Supply executable rational/Laurent lowering and a complete static product/peak-byte certificate before arithmetic admission.'],
      'pinned_public_sources': [BASE+'source-identity.md',BASE+'frames-and-poles.md'],
      'local_formula_sources':['public outer source witnesses','refined-tracefree-pole-domain.md sections5-6']}

def check_cancellation_domain(owner, target_standard_tags, carrier_order, legal_orders, standard_orders):
    if not isinstance(owner,VertexLabel): raise ValueError('complete occurrence owner required')
    if type(owner.standard_tag) is not int: raise ValueError('instantiate integer non-Boolean standard tag for domain check')
    for tag in target_standard_tags: decode_standard_tag(tag)
    if owner.standard_tag not in target_standard_tags: raise ValueError('standard owner lost under projection')
    if type(carrier_order) is not int or not 0<=carrier_order<=54: raise ValueError('carrier outside certified domain')
    for orders,bound,name in ((legal_orders,29,'legal'),(standard_orders,5251,'standard')):
        if len(orders)!=4 or any(type(v) is not int or not 0<=v<=bound for v in orders): raise ValueError(name+' outside certified domain')
    return {'owner':owner.data(),'carrier_legal_cancelled_by_formula':True,'standard_equations_are_target_units':True,
            'declared_orders_checked_only':True,'source_pole_certificate_derived':False,
            'actual_source_admitted':False}

if __name__=='__main__':
    print(json.dumps({'schema':'outer-partition-source-v1','parameters':PartitionChart(15).data(),
                      'definitions':definitions(),'gate':release_gate()},sort_keys=True))
