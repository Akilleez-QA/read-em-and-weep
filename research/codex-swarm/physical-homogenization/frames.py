"""PH01: physical F12 chart identification, formal weights/jet coefficients only.

No physical polynomial evaluator, expansion, numerical source specialization,
coefficient solver, order change or F12-to-F34 renaming is implemented.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import subprocess

CLR_REV='82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc'
CLR='research/codex-swarm/whole-source-clearing/'
CLR_MANIFEST_BLOB='a05411d32d543a6f45cd0f13b27bb4c539f60ff4'
BASE_REV='08b73637d4136f91606aad332c46cafd064417f8'
V5_REV='ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18'
PAIR_REV='02d0e727ffb95dfd9281906cc284c56e8bffd018'
PINS=[(BASE_REV,'research/hm/current-scalar-geometric-dependencies/frames-and-poles.md','876cad001a8f96bb207ca246873e3efe67afd9a394cc4d2a0796992596b84916'),
 (BASE_REV,'research/hm/current-scalar-residual-attribution/closure-and-characters.md','434aa106d0780f6eeef956335cc207a8b436d35db52f515f52bb5d49204292a2'),
 (V5_REV,'research/hm/null-operator-compiler/physical_current_source_binding.py','8cc3f3be47c6944e983a8b1922470a27c1a413b3fe9059f97c75b7a2cd967d3d'),
 (V5_REV,'research/hm/null-operator-compiler/hm-pinned-model.json','635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'),
 (V5_REV,'research/hm/null-operator-compiler/hm-pinned-source-formulas.js','c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94'),
 (CLR_REV,CLR+'review-independent.md','e1fc22e0352c91212df870a8591299986efa6f372909177e9174ac8cc1982226'),
 (CLR_REV,CLR+'review-degree.md','24de3cf66a2815f7cc81dfed8538648eb80c84f5b1bbf0596893ff1c04d30662'),
 (PAIR_REV,'research/hm/null-source-integration/complementary-pair/PROOF.md','edf2efafdb0f1891af0c9adf02a133e683633466686813e0f8aba48f85abe6bc'),
 (PAIR_REV,'research/hm/null-source-integration/complementary-pair/independent-review.md','9cae0a103bab76d25fccefb24f8be40d43d0ea2a6726055887ef4fb0d86c8388')]
ACCEPTANCE_URLS=['https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6211273493','https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6211347824']
SEED_TAILS={12:[[12,1,1,9,9],[12,2,2,11,13],[12,3,4,15,15]],30:[[30,2,2,3,12],[30,3,3,7,14],[30,4,4,15,15]]}

def need(ok,msg):
    if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def read(repo,rev,path):return subprocess.check_output(['git','show',rev+':'+path],cwd=repo)
def authenticate(repo,reader=None):
    reader=reader or (lambda rev,path:read(repo,rev,path));proofs=[]
    for rev,path,sha in PINS:
        raw=reader(rev,path);need(hashlib.sha256(raw).hexdigest()==sha,'source pin drift: '+path)
        proofs.append({'commit':rev,'path':path,'sha256':sha,'git_blob':blob(raw)})
    raw=reader(CLR_REV,CLR+'producer-ready.json');need(blob(raw)==CLR_MANIFEST_BLOB,'CLR manifest drift')
    manifest=json.loads(raw);values={}
    for name,sha in manifest['files_sha256'].items():
        need(Path(name).name==name,'nonlocal CLR path');data=reader(CLR_REV,CLR+name)
        need(hashlib.sha256(data).hexdigest()==sha,'CLR producer drift: '+name);values[name]=data
        proofs.append({'commit':CLR_REV,'path':CLR+name,'sha256':sha,'git_blob':blob(data)})
    integration=json.loads(values['source-integration.json']);finite=integration['finite_actual_source_clearing']
    need(finite['schema']=='whole-F-finite-factored-clearing-v1','actual finite source schema')
    need(finite['pair']==[0,1] and finite['finite_carrier_orders']==[5,6,5],'finite source domain')
    need(finite['refined_finite_coordinate_degree_bound']['pair']==217 and finite['refined_finite_coordinate_degree_bound']['complement']==210,'reviewed degree bound')
    return {'proofs':proofs,'finite_AST_sha256':hashlib.sha256(canonical(finite).encode()).hexdigest(),
            'finite_P_root':finite['cleared_P'],'finite_F_equation':finite['source_definition'],
            'finite_scope_acceptance_comments':ACCEPTANCE_URLS,
            'complementary_finite_property_comment':'https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6211504649'}

def bits(tag):
    need(type(tag) is int and tag in range(16),'literal standard tag0..15')
    return [(tag>>(3-i))&1 for i in range(4)]
def strict_owners(owners):
    need(type(owners) is list and len(owners)==3,'ordered full source triple required')
    for v in owners:
        need(type(v) is list and len(v)==5 and all(type(n) is int for n in v),'five integer owner fields')
        seed,occ,carrier,mask,tag=v
        need(occ>=0 and carrier in range(6) and mask in range(16) and tag in range(16),'owner domain')
    need(len({(v[0],v[1]) for v in owners})==3 and len({v[0] for v in owners})==1,'distinct occurrence identity, same seed')
    keys=[(-1 if v[2]==5 else v[2],v[3],v[4]) for v in owners]
    need(keys==sorted(keys) and len(set(keys))==3,'fresh source-first distinct common owners')
    return owners

def ordered_pair(pair):
    need(type(pair) in (list,tuple) and len(pair)==2 and all(type(i) is int for i in pair)
         and tuple(pair) in ((0,1),(2,3)),'ordered pair01/23 only')
    return tuple(pair)

def primitive_bridge():
    return [{'carrier':c,'assigned_H_degree':4 if c==5 else 5,
      'raw_di_dp_affine_degree':4 if c in (0,5) else 5,
      'canonical_e_domain':list(range(3)) if c==5 else list(range(2)) if c==0 else [0],
      'v0_padding':'2-e' if c==5 else '1-e' if c==0 else '0',
      'cleared_homogeneous_primitive':'-v3*v4*hom_(6+w)(stored_num)' if c==5 else '-H*hom_(5+w)(stored_num)',
      'identity':'H^2*actual_weighted_homogeneous_primitive=cleared_homogeneous_primitive',
      'weights':{'I_columns':[0,1],'P_rows':[0,-1]},
      'zero_entries':'zero polynomial; do not assign degree to zero',
      'auxiliary_warning':'affine denominator degree4; ordinary homogenization is -v1*a/v0, not -v1*a of degree5'} for c in range(6)]

def chain_splitting_balance():
    source=[('U0.gamma',1,-2),('U0.Icol0',0,0),('U0.Icol1',1,-2),('U0.H1W',-1,2),
            ('U1.W',0,0),('U1.eta',-1,2),('Q0.H0',-1,2),('Q0.Prow0',0,0),
            ('Q0.Prow1',-1,2),('Q0.Ldelta',1,-2),('Q1.L',0,0),('Q1.ev',1,-2)]
    result=[]
    for block,d,p in source:
        need(2*d+p==0,'actual source splitting frame mismatch')
        result.append({'source_block':block,'homogeneous_degree':d,'nu_power':p,'twice_total_tau_exponent':2*d+p})
    return result

def chart_frame(tag,pair=(0,1)):
    pair=ordered_pair(pair);e=bits(tag);entries=[]
    for r,s in product(range(2),repeat=2):
        w=r-s;sig_r=1-2*r;sig_s=1-2*s
        conjugation=Q(sig_r-sig_s,2)
        need(w+conjugation==0,'physical K conjugation')
        residual=Q(w)+Q(sig_r-sig_s,2)
        need(residual==0,'common endpoint Q omitted')
        entries.append({'entry':[r,s],'core_tau_weight':w,'physical_D_conjugation_tau_weight':int(conjugation),
                        'physical_g_total_tau_weight':0,'infinity_T_extra_connection_coefficient':[residual.numerator,residual.denominator]})
    coordinates=[]
    for i,inverted in enumerate(e):
        coordinates.append({'axis':i,'local_variable':('t' if inverted else 'x')+str(i),
          'ordinary_chain':{'sign':-1 if inverted else 1,'local_power':-2 if inverted else 0},
          'invariant_stripped_local_operator_sign':-1 if inverted else 1,
          'stripped_T_factor':{'sign':1,'local_power':-2 if inverted else 0},
          'Q_local_cases':{'mask0':'1/(2*t)' if inverted else '0',
                           'mask1':'-t/(1-t^2)' if inverted else '(x^2+1)/(2*x*(x^2-1))'},
          'Q_transport': '1/(2*t)-mask*t^-2*rf(1/t)' if inverted else 'mask*rf(x)',
          'gerbe_transport':{'finite_q':'deltaMask/x','dlogx_sign':-1 if inverted else 1,
           'invariant_V_sign':-1 if inverted else 1,'local_stripped_q_sign':1,
           'local_stripped_q_power':-1,'local_variable':'t' if inverted else 'x'},
          'y_deck_strip':{'finite_y_from_local':'z/t^2' if inverted else 'y',
                          'strip_factor_power':-2 if inverted else 0}})
    cycles=[]
    for r,s,u in product(range(2),repeat=3):
        weights=[r-s,s-u,u-r];need(sum(weights)==0,'ordered trace covariance')
        cycles.append({'indices':[r,s,u],'factor_tau_weights':weights,'total':0})
    fpower=[-2*e[i] if i in pair else 0 for i in range(4)]
    return {'schema':'physical-scalar-pair-chart-frame-v1','pair':list(pair),'representation_standard_tag':tag,'representation_bits_high':e,
      'owner_standard_tags_reassigned':False,'tau':'product_(e_i=1) t_i',
      'line_frame':{'nu_local_squared_over_pulled_finite_squared':'tau','common_base_line_frame_per_owner':True,
       'owner_constants':'retained; no independent owner normalization/reset to1',
       'square_root_sign':'one coherent base-line frame transition, central signs cancel in normalized trace',
       'deck_frame_signs':'D_v transforms by a central sign under deck change; normalized ordered trace cancels endpoint signs',
       'physical_I_scalar_tau_power':[1,2],'physical_P_scalar_tau_power':[-1,2]},
      'entries':entries,'coordinates':coordinates,'ordered_trace_cycles':cycles,
      'F_transition':{'character':[-2 if i in pair else 0 for i in range(4)],'local_power':fpower,'sign':1,
       'identity':'Fpair_local=product_pairInfinity(t_i^-2)*Fpair_finite(x_i=1/t_i)',
       'local_actual_trace_formula':'b_transported-(epsilon_pair0*epsilon_pair1)/4*tr[K20(T12,p*T01,q-T12,q*T01,p)]; T here ordinary local derivative, epsilon_i=-1 only on inverted factors',
       'source_derivation':['physical g=D_b K D_a^-1 is unchanged as a rational matrix under representation change',
         'ordinary tangent pulls back with inversion Jacobian; invariant-vector minus cancels its sign',
         'gerbe q comes from transported dlog x, with the same stripped y factor',
         'normalize the complete ordered trace and b in this same frame before subtraction']}}

def local_ell(mask,tag,i):
    m=(mask>>i)&1;e=bits(tag)[i]
    return {'mask_bit':m,'homogeneous_degree':3 if m else 1,'equation':'X*(X^2-Y^2)' if m else 'Y',
            'local_coefficient':('1-t^2' if m else 't') if e else ('x*(x^2-1)' if m else '1')}
def local_standard_unit(owner_tag,tag,i):
    original=bits(owner_tag)[i];representation=bits(tag)[i]
    return ('1' if original else 't') if representation else ('x' if original else '1')

def bind_triple(owners,tag,pair=(0,1)):
    pair=ordered_pair(pair);strict_owners(owners);frame=chart_frame(tag,pair);e=bits(tag);C=[];degree=[0]*4
    for v in owners:
        d=4 if v[2]==5 else 5
        legal=[local_ell(v[3],tag,i) for i in range(4)]
        cv=[14*d+(legal[i]['homogeneous_degree'] if i in pair else 0) for i in range(4)]
        degree=[a+b for a,b in zip(degree,cv)]
        C.append({'owner':v[:],'representation_standard_tag':tag,'carrier_equation_degree':d,
          'H_homogeneous_equation':'v0*v1*v3*v4' if v[2]==5 else 'v'+str(v[2])+'^5-v0*v1*v2*v3*v4',
          'H_local_identity':'H_local=tau^d * H_finite(pullback); use actual homogeneous hj or a including v0',
          'legal_sections':legal,'C_definition':'H_owner^14 * product_(i in ordered_pair) ell_owner,i',
          'C_multidegree':cv,'C_local_pullback_power':[e[i]*cv[i] for i in range(4)],
          'original_standard_units':[local_standard_unit(v[4],tag,i) for i in range(4)],
          'domain':'each original standard equation, source carrier H and all original legal sections is nonzero on the restricted common overlap; no relabeling'})
    target=[degree[i]-(2 if i in pair else 0) for i in range(4)]
    need(min(target)>=0 and all(target[i]<=(217 if i in pair else 210) for i in range(4)),'reviewed target degree')
    cpower=[e[i]*degree[i] for i in range(4)];fpower=frame['F_transition']['local_power']
    ppower=[e[i]*target[i] for i in range(4)]
    need([a+b for a,b in zip(cpower,fpower)]==ppower,'C*physicalF versus polynomial homogenization')
    return {'schema':'actual-physical-pair-homogenization-instance-v1','pair':list(pair),'owners':copy_owners(owners),
      'representation_standard_tag':tag,'frame':frame,'C_owner_records':C,
      'source_finite_slot_map':{'0':owners[0][:],'1':owners[1][:],'2':owners[2][:]},
      'finite_candidate_reference':({'kind':'reviewed actual F12 family, source slots in this order','commit':CLR_REV,'direct_F12_root_on_target_owners':True}
         if pair==(0,1) else {'kind':'null constructive F34 property from ordered raw inverse image','commit':PAIR_REV,
          'direct_F12_root_on_target_owners':False,'inverse_image_may_be_unsorted':True,
          'ordered_slot_positions_preserved':True,'finite_coefficient_payload_instantiated_by_PH01':False}),
      'P_target_multidegree':target,'product_C_transition_power':cpower,'physical_F_transition_power':fpower,
      'P_transition_power':ppower,'homogeneous_identity':'P_hom_local=(product_v C_v,local)*actual_Fpair_local',
      'proof_equation':'product_C_local*actual_F_local=t^(D_C+n_pair)*P_finite(pullback)=P_hom_local',
      'polynomial_reversal':'for each finite monomial exponent a_i<=P_target_i, infinity exponent is P_target_i-a_i>=0; no actual coefficient is extracted',
      'polynomial_frame_chosen_arbitrarily':False,
      'source_domain_scope':'rational identity on every represented common overlap; cleared numerator extends polynomially to the full standard chart',
      'finite_source_scope':'reviewed actual F12 finite property' if pair==(0,1) else 'null fixed-ordered-triple F34 property; not equality of sorted alternating cochains',
      'not_supplied':['complete standard-B/inner coefficient program','standard-target weighted detector coefficient extension program','historical-order/source identification','arithmetic/execution admission']}
def copy_owners(owners):return [v[:] for v in owners]

def validate_instance(result):
    try:
        expected=bind_triple(result['owners'],result['representation_standard_tag'],result['pair'])
        need(canonical(result)==canonical(expected),'mutated physical frame/sign/divisor/owner identity')
    except (KeyError,TypeError,IndexError) as exc:raise ValueError('malformed frame instance') from exc
    return True

def build(repo):
    source=authenticate(repo)
    return {'schema':'physical-scalar-pair-homogenization-proof-v1','source_authentication':source,
      'universal_domain':'both ordered pairs01/23; every ordered source-first triple with carriers0..5, all legal masks and unchanged standard owners; all16 representation charts; repeated source-label zeros use null source pullback convention',
      'abstract_frame_catalog':[chart_frame(tag) for tag in range(16)],
      'complementary_frame_catalog':[chart_frame(tag,(2,3)) for tag in range(16)],
      'homogeneous_primitive_bridge':primitive_bridge(),
      'chain_splitting_balance':chain_splitting_balance(),
      'seed_examples':[{'seed':seed,'instances':[bind_triple(owners,tag) for tag in range(16)]} for seed,owners in SEED_TAILS.items()],
      'complementary_seed_examples':[{'seed':seed,'instances':[bind_triple(owners,tag,(2,3)) for tag in range(16)]} for seed,owners in SEED_TAILS.items()],
      'claimed_mathematical_progress':'actual physical homogeneous F12 and F34 representatives identified with source-derived pair degree217/complement210 homogenizations via transition/connection/gerbe/deck identities, not by choosing twists or sorting renamed cochains',
      'review_status':'producer proof, independent review pending',
      'global_gates':{k:False for k in ('full_Rsharp_source_realized','standard_B_coefficient_program_realized','historical_order_equivalence','arithmetic_execution','physical_polynomial_evaluation','obstruction_computed')}}
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--repo',default=str(Path(__file__).resolve().parents[3]));a=p.parse_args()
    print(json.dumps(build(a.repo),indent=2,sort_keys=True))
