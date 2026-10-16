"""Factored finite whole-F identity and seed12/30 combined-numerator binding.
No physical polynomial evaluator or expanded matrix product is implemented.
"""
from collections import Counter
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import subprocess

REV='10810ee877fdaf291399198ad60d7dd0c316a42d'
MODEL='research/hm/null-operator-compiler/hm-pinned-model.json'
SOURCE='research/hm/null-operator-compiler/hm-pinned-source-formulas.js'
PINS={MODEL:'635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926',SOURCE:'c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94',
'research/hm/null-source-integration/combined-pole/PROOF.md':'03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25',
'research/hm/null-source-integration/combined-pole/certificate.py':'57fc3b13f0853a1364d2a5911884fe0d89bd3b287c9913bf2f377f24da0eff26',
'research/hm/null-support-certificates/pinned-homogeneous-identities.json':'55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018'}
ORDER='research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md'

def need(ok,msg):
    if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def read(repo,path):return subprocess.check_output(['git','show',REV+':'+path],cwd=repo)
def authenticate(repo):
    values={};pins={}
    for path,digest in PINS.items():
        raw=read(repo,path);need(hashlib.sha256(raw).hexdigest()==digest,'pin drift '+path)
        values[path]=raw;pins[path]={'sha256':digest,'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
    raw=read(repo,ORDER);pins[ORDER]={'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()}
    cert=json.loads(values['research/hm/null-support-certificates/pinned-homogeneous-identities.json'])
    model=json.loads(values[MODEL])
    need(cert['modelSha256']==hashlib.sha256(json.dumps(model,separators=(',',':')).encode()).hexdigest(),'contraction certificate model binding')
    need(cert['byIdentity']['P_I']==24 and cert['byIdentity']['P_gamma']==60 and cert['byIdentity']['delta_I']==120 and cert['byIdentity']['E_identity']==1350,'contraction certificate scope')
    return model,pins

def primitive_catalog(model):
    """Literal denominator metadata only; never substitute/evaluate a polynomial."""
    result=[]
    for c,chart in enumerate(model['charts']):
        if c==0:expected={(1,1,1,1):1,(0,0,0,0):-1}
        elif c<5:expected={(1,1,1,1):1,tuple(5 if i==c-1 else 0 for i in range(4)):-1}
        else:expected={(2,0,1,1):-1}
        for block,den in (('I','di'),('P','dp')):
            got={tuple(map(int,e.split(','))):a for e,a in chart[den]}
            need(len(chart[den])==len(expected) and got==expected,'primitive denominator identity')
            shape=(15,2) if block=='I' else (2,15)
            need(len(chart[block])==shape[0] and all(len(row)==shape[1] for row in chart[block]),'primitive shape')
            for row_index,row in enumerate(chart[block]):
                for col_index,poly in enumerate(row):
                    weight=col_index if block=='I' else -row_index
                    for exponent,coefficient in poly:
                        exps=tuple(map(int,exponent.split(',')))
                        raw_bound=(6 if c==5 else 5)+weight
                        need(len(exps)==4 and min(exps)>=0 and sum(exps)<=raw_bound,
                             'primitive weighted finite degree bound')
        result.append({'carrier':c,'source_numerators':['charts',c,'I/P'],'source_denominators':['charts',c,'di/dp'],
          'H':'a=v1*v3*v4' if c==5 else 'h'+str(c),
          'denominator_identity':'-v1*a' if c==5 else '-H',
          'cleared_primitive_multiplier':'-v3*v4' if c==5 else '-H',
          'assigned_carrier_degree':4 if c==5 else 5,
          'finite_carrier_degree':3 if c==5 else 4 if c==0 else 5,
          'cleared_multiplier_degree_bound':2 if c==5 else 4 if c==0 else 5,
          'finite_primitive_weight_excess':2 if c==5 else 1 if c==0 else 0,
          'stored_numerator_degree_bound':str(6 if c==5 else 5)+'+column_index for I; same constant-row_index for P',
          'identity':'H^2 * primitive = cleared_primitive_multiplier * stored_numerator',
          'frame':'common finite v0=1, vk=e_k(x0,x1,x2,x3)'})
    return result

class DAG:
    def __init__(self):self.nodes=[];self.ids={}
    def n(self,op,*args):
        key=canonical([op,*args])
        if key not in self.ids:
            need(len(self.nodes)<4000,'factored metadata cap');self.ids[key]=len(self.nodes);self.nodes.append([op,*args])
        return self.ids[key]
    def factor(self,key):return self.n('owned_polynomial_factor',list(key))
    def mul(self,*xs):return self.n('ordered_product',*xs)
    def add(self,*xs):return self.n('sum',*xs)
    def scale(self,x,n,d=1):return self.n('scale',n,d,x)
    def rat(self,num,den=None):return num,Counter(den or {})
    def times(self,a,b):return self.rat(self.mul(a[0],b[0]),a[1]+b[1])
    def plus(self,a,b):
        den=a[1]|b[1]
        def lift(r):return self.mul(r[0],*(self.n('power',self.factor(k),v-r[1].get(k,0)) for k,v in sorted(den.items()) if v>r[1].get(k,0)))
        return self.rat(self.add(lift(a),lift(b)),den)
    def negative(self,r):return self.rat(self.scale(r[0],-1),r[1])
    def partial(self,r,d):
        out=self.rat(self.n('polynomial_partial_after_elementary_substitution',r[0],d),r[1])
        for factor,power in r[1].items():
            den=r[1].copy();den[factor]+=1
            term=self.rat(self.mul(self.scale(r[0],-power),self.n('polynomial_partial_after_elementary_substitution',self.factor(factor),d)),den)
            out=self.plus(out,term)
        return out
    def primitive(self,slot,block):
        # Catalog gives the exact six source cases for this polynomial reference.
        return self.rat(self.n('catalog_cleared_primitive',slot,block),{(slot,'H',-1):2})
    def core(self,a,b):
        r=self.times(self.primitive(a,'P'),self.primitive(b,'I'))
        return self.rat(self.n('transpose',r[0]),r[1])
    def log(self,slot,d):
        return self.rat(self.n('polynomial_diagonal',self.n('mask_times_x_squared_plus_one_over_two',slot,d)),{(slot,'ell',d):1})
    def tangent(self,a,b,d):
        k=self.core(a,b)
        return self.plus(self.plus(self.partial(k,d),self.times(self.log(b,d),k)),self.negative(self.times(k,self.log(a,d))))
    def q(self,a,b,d):
        # (m_b-m_a)/x = m_b(1-m_a)(x²-1)/ell_b -m_a(1-m_b)(x²-1)/ell_a.
        p=self.rat(self.n('binary_mask_q_numerator',a,b,d,1),{(b,'ell',d):1})
        n=self.rat(self.n('binary_mask_q_numerator',a,b,d,-1),{(a,'ell',d):1})
        return self.plus(p,n)

def whole_source(catalog):
    g=DAG();A0=g.tangent(0,1,0);A1=g.tangent(0,1,1)
    B0=g.tangent(1,2,0);B1=g.tangent(1,2,1)
    mixed=g.plus(g.times(B0,A1),g.negative(g.times(B1,A0)))
    normalized=g.times(g.core(2,0),mixed) # K02^-1 = K20 from pinned contractions.
    trace=g.rat(g.n('trace',normalized[0]),normalized[1])
    b=g.times(g.q(0,1,0),g.q(1,2,1));b=g.rat(g.scale(b[0],15,4),b[1])
    f=g.plus(b,g.rat(g.scale(trace[0],-1,4),trace[1]))
    clearing={(slot,'H',-1):14 for slot in range(3)}
    clearing.update({(slot,'ell',i):1 for slot in range(3) for i in (0,1)})
    need(all(clearing.get(k,0)>=v for k,v in f[1].items()),'actual whole-F denominator exceeds C product')
    P=g.mul(f[0],*(g.n('power',g.factor(k),v-f[1].get(k,0)) for k,v in sorted(clearing.items()) if v>f[1].get(k,0)))
    return {'schema':'whole-F-finite-factored-clearing-v1','pair':[0,1],'catalog':catalog,'dag':g.nodes,'F_numerator':f[0],
      'F_denominator':[{'factor':list(k),'exponent':v} for k,v in sorted(f[1].items())],
      'cleared_P':P,'clearing':[{'factor':list(k),'exponent':v} for k,v in sorted(clearing.items())],
      'source_definition':'F12=b12-tr(K02^-1(T12,0*T01,1-T12,1*T01,0))/4; stripped common y0*y1',
      'separate_scalar_definitions':{'physical_Q':'diag(m*(x_i²+1)/(2*x_i*(x_i²-1)),-m*(x_i²+1)/(2*x_i*(x_i²-1)))',
       'gerbe_q':'(mask_b,i-mask_a,i)/x_i; only b12 uses this',
       'b12':'15/4*gerbe_q(0,1,0)*gerbe_q(1,2,1)'},
      'polynomial_factor_definitions':{'H':'H_carrier, owned by slot; primary hj=vj^5-product(v0..v4); auxiliary a=v1v3v4 in v0=1',
       'ell':'1 if mask bit0; x_i*(x_i²-1) if mask bit1, pair coordinates only',
       'mask_times_x_squared_plus_one_over_two':'m_slot,i*(x_i²+1)/2; diagonal gives (z,-z)',
       'binary_mask_q_numerator':'sign+ gives m_b*(1-m_a)*(x²-1); sign- gives -m_a*(1-m_b)*(x²-1)',
       'catalog_cleared_primitive':'use literal carrier case in catalog, multiply stored matrix polynomial after elementary substitution',
       'polynomial_partial_after_elementary_substitution':'exact formal derivative of the entire polynomial reference AFTER vk=e_k; no derivative of a frozen value'},
      'proved_identity':'P_finite=(product_slots H^14 ell_0 ell_1)*actual_F12_finite by exact quotient-ring algebra; no coefficient evaluation',
      'source_triple_order':'evaluate whole-F formula once on increasing source-first order (star5 before0..4, numeric low-bit mask, standard); otherwise alternate this defined cochain, never rebuild nonlinear source on a permutation',
      'finite_carrier_orders':[f[1].get((s,'H',-1),0) for s in range(3)],
      'naive_finite_coordinate_degree_bound':{'pair':218,'complement':210,
       'per_tuple_formula':'14*sum_v d_v + [i in pair]*(sum_v degree(ell_vi)-1)',
       'proof':'source entry weights cancel in ordered trace; each first derivative and each Q_i or gerbe_q_i lowers coordinate_i bound by1'},
      'refined_finite_coordinate_degree_bound':{'pair':217,'complement':210,
       'per_tuple_formula':'14*sum_v d_v + [i in pair]*(sum_v degree(ell_vi)-2)',
       'noncritical_slack':'pair target gap <=1-12*count(carrier0)-10*count(aux5)-count(mask_i0)',
       'critical_case':'all carriers1..4, all mask_i1: T_rs=partial_i K_rs-2*(r-s)*rf_i*K_rs; degree<=r-s-2 because rf_i=1/(2*x_i)+O(x_i^-3); gerbe_q_i=0',
       'scope':'polynomial degree proof using actual primitive exponent metadata, rational degree rules and universal leading-weight cancellation; not physical coefficient evaluation'},
      'required_geometric_coordinate_degree_bound':{'pair':217,'complement':210,
       'per_tuple_formula':'14*sum_v d_v + [i in pair]*(sum_v degree(ell_vi)-2)'},
      'top_layer_resolution':'extra leading cancellation follows from the critical-case covariant identity; no actual source leading coefficient is evaluated',
      'polynomial_homogenization_candidate':'homogenize each coordinate of P_finite to14*sum d+pair*(sum degree ell-2)',
      'physical_homogeneous_frame_identification_verified':False,
      'remaining_source_implication':'independent source/frame audit must identify this polynomial homogenization with the intended physical F12 homogeneous character representative; do not infer geometric/infinity admission from finite clearing alone'}

def compiler_module():
    path=Path(__file__).resolve().parents[1]/'arithmetic/compiler_v5/bind_requests.py'
    spec=importlib.util.spec_from_file_location('clr_v5_source',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m,path

def build(repo):
    model,pins=authenticate(repo);source=whole_source(primitive_catalog(model));v5,path=compiler_module();graph,vpins=v5.authenticate(repo)
    requests=[]
    for sid in (12,30):
        binding=v5.bind(v5.request(sid),graph,vpins);edges={}
        for branch in binding['branches']:
            lemma=branch['pending_null_lemma'];edge=lemma['scalar_edge_owners'];key=canonical(edge)
            if key not in edges:
                a,b=edge;tag=lambda v:[(v[4]>>(3-i))&1 for i in range(4)]
                edges[key]={'id':'N_'+str(sid)+'_'+str(a[1])+'_'+str(b[1]),'output_edge':edge,
                 'C_output':[{'owner':o,'H_power':14,'pair_ell_powers':[1,1,0,0]} for o in edge],
                 'Z_output':[{'owner':o,'standard_powers':[5250*z for z in tag(o)]} for o in edge],
                 'inserted_owner_maps':{'u':{'occurrence':['inserted',sid,a[1],b[1],'u'],'carrier_domain_inclusive':[0,5],'mask_domain_inclusive':[0,15],'standard_tag':a[4]},
                   'v':{'occurrence':['inserted',sid,a[1],b[1],'v'],'carrier_domain_inclusive':[0,5],'mask_domain_inclusive':[0,15],'standard_tag':b[4]}},
                 'whole_source_P':'call whole-F finite factored schema on source-first sorted triple, then multiply sorting sign; preserve full owners; repeated source labels zero by null proof',
                 'N_fullsum':{'standard':'C_a*C_b*Z_ab*B_ab, B=complete R(Kcov Pi + A h S Pi)F12; never split into free leaves',
                  'prism1':'Z_ab*sum_u Qhat_u*P_[u,a,b]',
                  'prism2':'-C_a*Z_ab*sum_(u,v) Qhat_u*Qhat_v*P_[u,v,b]',
                  'padding':{'standard':['C_a','C_b','Z_ab'],'prism1':['Z_ab'],'prism2':['C_a','Z_ab']}},
                 'D':'C_a*C_b*Z_ab','derivative':'(Delta*dN-N*sum_f a_f*(df)*product_(g!=f)g)/(D*Delta)',
                 'Delta':'each positive owned factor in D once; equal polynomial values at different owners stay distinct',
                 'standard_B_requirements':{'complete_sum':True,'support':[-1668,5248],'monomial_predicate':'both finite =>e>=0; both infinity=>e<=character_i; mixed unrestricted','proof':'null combined-pole PROOF.md section3; source-bound executable B circuit remains unresolved'},
                 'Qhat_requirements':'null exact N14 polynomial quotient definitions and tag-matched reversal; no extra twist on rho',
                 'geometric_source_premise_discharged':False}
            branch['combined_numerator_reference']=edges[key]['id']
            branch['differentiation_order']='form complete N_fullsum, cancel inserted factors, then one complementary derivative'
        requests.append({'v5_binding':binding,'combined_edges':list(edges.values())})
    return {'schema':'codex-whole-source-integration-v1','source_commit':REV,'source_pins':pins,
      'compiler_adapter_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'finite_actual_source_clearing':source,'requests':requests,
      'order_scope':'fresh auxiliary-first numeric(mask),standard source order; historical comparison unresolved and null-owned',
      'proved_progress':'explicit actual finite whole-F polynomial numerator, plus exact seed/edge/padding/one-derivative instantiation of null universal recipe',
      'unresolved':['identify the explicit degree217/210 polynomial homogenization with intended physical homogeneous character F12; geometric infinity/frame audit','actual complete standard B and inner quotient coefficient circuits','full source-order/transport comparison, null-owned','coefficient support, detector assembly and resource admission'],
      'gates':{k:False for k in ('homogeneous_source_clearing','combined_geometric_poles','Laurent_admission','historical_order_equivalence','physical_source_evaluation','arithmetic_execution')}}
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--repo',default=str(Path(__file__).resolve().parents[3]));a=p.parse_args();print(json.dumps(build(a.repo),indent=2,sort_keys=True))
