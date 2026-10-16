"""Authenticated 32-test transport template; actual-source admission fails closed.

No cochain/source values are evaluated. Pending null theorem adapters are explicit,
non-self-certifying slots; a supplied Boolean or proof-looking string cannot fill one.
"""
import hashlib
import json
from pathlib import Path
import subprocess
from lift_schema import closed_lift_schema, source_components

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PINS_SHA = 'c64b506220ca636632e6d74f04c08050eff7c3c549a8191e5121ef2d32fd7d94'
SELECT_SHA = '54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d'
WEIGHT_SHA = 'f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0'
# Only a separately reviewed code/registry update may populate these exact proof
# pins. Requests cannot nominate their own trusted proof or mutate a success gate.
ADAPTER_SLOTS = {
    'all_twenty_row_regular_transport_domain': {'commit': '43193bc8badf3f29a1363132135d956cc12d46ad', 'path': 'research/hm/null-source-integration/scalar-family-transport/PROOF.md', 'git_blob': 'fc8befcc863efd073d4a66dc6eec12c722504447', 'sha256': 'e0fac7c2a2564dd1521a6055238e175fcf83e11e1b4bf9302eacad13ed040db3', 'scope': 'conditional whole-source standard-target regular extension; all20 scalar rows; full J0..J3'},
    'first_current_tracefree_wrapper_equivalence': {'commit': '43193bc8badf3f29a1363132135d956cc12d46ad', 'path': 'research/hm/null-source-integration/tracefree-currents/PROOF.md', 'git_blob': '405a46728161bce487ef6d5b147ee6b7a73c7e17', 'sha256': 'e77328364f7d738430d5ef4ebcde16ae1aa827ce59cd48f9300c1ad5319407b3', 'scope': 'first L/U currents only; branchwise tf wrapper identity for eight seed12/30 E34 requests; no M0/second-jet assertion'},
    'complete_source_and_closed_lift': None,
    'source_order_identification_or_full_comparison': None,
}
FRAME = {'matrix_frame': 'original-resolution', 'deck_character': 'full-sign',
         'deck_product_removed_count': 1, 'scalar_internal_degree': -2,
         'scalar_tau_exponent': -4, 'standard_bits': 'high bit 3-i',
         'legal_mask_bits': 'low bit i', 'row_End_transpose_count_in_j': 1,
         'frozen_endpoint_rule': 'constant endpoint jets only; never drop moving frame derivatives'}

def need(ok, message):
    if not ok: raise ValueError(message)

def canonical(x): return json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)
def exact(a, b, message): need(canonical(a) == canonical(b), message)
def digest(raw): return hashlib.sha256(raw).hexdigest()

def authenticate():
    raw = (HERE/'source-pins.json').read_bytes()
    need(digest(raw) == PINS_SHA, 'transport proof pin manifest changed')
    pins = json.loads(raw)
    need(pins['schema'] == 'tr01-source-pins-v1', 'proof pin schema')
    content = {}
    for p in pins['sources']:
        data = subprocess.check_output(['git', 'show', p['commit']+':'+p['path']], cwd=ROOT, timeout=10)
        need(len(data) == p['bytes'] and digest(data) == p['sha256'], 'proof bytes changed')
        need(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == p['git_blob'], 'proof Git object changed')
        content[p['path']] = data
    pair = 'research/hm/null-source-integration/combined-pole/certificate.json'
    pole = json.loads(content[pair])
    need(pole['recipe']['generic_full_sum_identity_proved'] is True, 'combined identity premise absent')
    need(pole['recipe']['source_clearing_verified_by_this_artifact'] is False, 'combined identity scope drift')
    exact(pole['bounds']['scalar_orders'], {'carrier':14, 'legal':1, 'standard':5250}, 'scalar bound mismatch')
    exact(pole['bounds']['derivative_orders'], {'carrier':15, 'legal':2, 'standard':5251}, 'derivative bound mismatch')
    selection_raw = (HERE.parent/'detector-selection/selection.json').read_bytes()
    weighted_raw = (HERE.parent/'detector-selection/weighted-requests.json').read_bytes()
    need(digest(selection_raw) == SELECT_SHA and digest(weighted_raw) == WEIGHT_SHA, 'weighted selection drift')
    external_weighted=json.loads(content['research/hm/null-source-integration/scalar-family-transport/weighted-requests.json'])
    exact(external_weighted,json.loads(weighted_raw),'null theorem inspected different weighted requests')
    tf=json.loads(content['research/hm/null-source-integration/tracefree-currents/certificate.json'])
    need(tf['raw_projected_first_current_equivalence_proved'] is True and tf['baseline_equivalence_proved'] is False,'first-current equivalence scope drift')
    need(tf['branch_count']==8 and tf['seed_scope']==[12,30],'first-current request scope')
    return pins, json.loads(selection_raw), json.loads(weighted_raw), pole

def epsilon(t):
    return 0 if len(set(t)) != 5 else (-1)**sum(t[i]>t[j] for i in range(5) for j in range(i+1,5))

def gamma(i, a, k):
    wp = lambda n: ((n+2)%5, (n+3)%5)
    wm = lambda n: ((n+1)%5, (n+4)%5)
    return epsilon((k, *(wp(a) if i<5 or i>=10 else wm(a)),
                    *(wp(i) if i<5 else wm(i-5) if i<10 else wm(i-10))))

def scalar_terms(i, b):
    need(type(i) is int and 0<=i<15 and type(b) is int and 0<=b<2, 'scalar row index')
    terms = [{'block':'X13', 'entry':[i,b], 'coefficient':1}]
    for a in range(5):
        for k in range(5):
            z = gamma(i,a,k)
            if z: terms.append({'block':'X02', 'entry':[a,5*b+k], 'coefficient':-z})
    return terms

def validate_frame(frame): exact(frame, FRAME, 'original frame/deck product/tau convention mismatch')

def validate_owner_term(term):
    need(type(term) is dict and set(term)=={'owners','outer_weight_owners','target_standard_tags','source_sorted_owners','sorting_sign'}, 'owner-term fields')
    owners = term['owners']
    need(type(owners) is list and len(owners)>0, 'explicit occurrence owners required')
    for v in owners:
        need(type(v) is list and len(v)==5 and all(type(x) is int for x in v), 'full five-field integer owner required')
        test, occurrence, carrier, mask, standard = v
        need(0<=test<32 and occurrence>=0 and 0<=carrier<=5 and 0<=mask<16 and 0<=standard<16, 'owner domain')
    need(len({(v[0],v[1])for v in owners})==len(owners), 'owner occurrence merged')
    exact(term['outer_weight_owners'], owners, 'deleted/prefix weight owner lost')
    tags = term['target_standard_tags']
    need(type(tags) is list and all(type(x) is int and 0<=x<16 for x in tags), 'target standard tags')
    need(all(v[4] in tags for v in owners), 'owner standard is not a target unit')
    order = sorted(range(len(owners)),key=lambda j:(-1 if owners[j][2]==5 else owners[j][2],owners[j][3],owners[j][4]))
    exact(term['source_sorted_owners'], [owners[j]for j in order], 'source owner permutation changed')
    sign=(-1)**sum(order[a]>order[b]for a in range(len(order))for b in range(a+1,len(order)))
    exact(term['sorting_sign'], sign, 'source-sorting parity mismatch')
    return True

def validate_actual_packet(packet, supplied_adapters):
    """Validate structure, then reject every pending theorem adapter.

    This currently cannot issue physical or mathematical source admission. In
    particular a full-looking closed-lift AST is not a checked physical cochain.
    """
    authenticate()
    need(type(packet) is dict and set(packet)=={'schema','source_components','lift','frame','projection_terms','source_order','intended_order','order_witness','closure_witnesses','projection_mode','whole_standard_extension_witnesses'}, 'actual packet fields')
    need(packet['schema']=='tr01-actual-source-packet-v1', 'packet schema')
    exact(packet['source_components'], source_components(), 'missing corrected source component or projected E summand')
    need(packet['projection_mode']=='complete_Rsharp_only', 'projected directional source is not complete Rsharp')
    exact(packet['lift'], closed_lift_schema(), 'missing top J3 or changed closed-lift direction/sign')
    validate_frame(packet['frame'])
    need(type(packet['projection_terms']) is list and packet['projection_terms'], 'no explicit outer owner/target binding')
    for term in packet['projection_terms']: validate_owner_term(term)
    extensions=packet['whole_standard_extension_witnesses']
    need(type(extensions) is list and len(extensions)==len(packet['projection_terms']), 'whole standard-target extension witnesses required')
    for term,w in zip(packet['projection_terms'],extensions):
        need(type(w) is dict and set(w)=={'scope','denominator_owners','target_standard_tags','identity_sha256','domain_sha256'}, 'whole extension witness fields')
        need(w['scope']=='whole_lift_component_and_all_prism_restrictions_on_standard_target', 'common-localized or directional-only regularity is insufficient')
        exact(w['denominator_owners'],term['owners'],'extension denominator owner lost')
        exact(w['target_standard_tags'],term['target_standard_tags'],'extension target changed')
        need(all(type(w[k]) is str and len(w[k])==64 and all(c in '0123456789abcdef'for c in w[k])for k in ('identity_sha256','domain_sha256')), 'actual extension identity/domain proof hashes required')
    need(type(packet['source_order']) is str and packet['source_order'] and type(packet['intended_order']) is str and packet['intended_order'], 'authenticated source orders required')
    witness = packet['order_witness']
    need(type(witness) is dict and set(witness)=={'kind','proof_sha256','source_definition_sha256'}, 'missing order witness')
    need(witness['kind'] in ('same_defined_alternating_source','full_closed_source_and_detector_comparison'), 'sorting is not source-order equivalence')
    need(all(type(witness[k]) is str and len(witness[k])==64 and all(c in '0123456789abcdef'for c in witness[k]) for k in ('proof_sha256','source_definition_sha256')), 'order/source proof hashes required')
    if packet['source_order'] != packet['intended_order']:
        need(witness['kind']=='full_closed_source_and_detector_comparison', 'fresh/historical identification missing')
    equations=closed_lift_schema()['closure_equations']
    need(type(packet['closure_witnesses']) is dict and set(packet['closure_witnesses'])==set(equations), 'all five closed-lift witness slots required, including delta J3')
    need(all(type(v) is dict and set(v)=={'proof_sha256','domain_sha256'} and all(type(x) is str and len(x)==64 and all(c in '0123456789abcdef'for c in x)for x in v.values()) for v in packet['closure_witnesses'].values()), 'self-asserted closure is not a proof reference')
    need(type(supplied_adapters) is dict and set(supplied_adapters)==set(ADAPTER_SLOTS), 'all null theorem adapter slots required')
    for name, accepted_pin in ADAPTER_SLOTS.items():
        need(accepted_pin is not None, 'pending independently reviewed null adapter: '+name)
        exact(supplied_adapters[name], accepted_pin, 'untrusted theorem adapter '+name)
    raise ValueError('no actual-source admission implementation; reviewed adapters/lowering still required')

def build_template():
    pins, selection, weighted, pole = authenticate()
    I20=selection['I20']
    exact(I20, [[i,0]for i in range(5,11)]+[[i,1]for i in range(15)if i!=5], 'I20 labels')
    need(len(weighted['requests'])==32, '32 tests required')
    scalar_maps=[{'label':{'i':i,'b':b},'input_internal_degree':-2,
                 'directions':[{'block':'X02','source':2,'target':0,'shape':[5,10]},
                               {'block':'X13','source':3,'target':1,'shape':[15,2]}],
                 'linear_terms':scalar_terms(i,b)} for i,b in I20]
    requests=[]
    for r in weighted['requests']:
        need(r['scalar_map'] in [m['label']for m in scalar_maps], 'unknown scalar row')
        requests.append({'test_id':r['id'],'scalar_map':r['scalar_map'],'weight_block':r['block'],
            'operator_order':['complete_Rsharp','closed_resolution_lift_J0_through_J3',
                              'original_frame_full_sign_deck_conversion_once','scalar_L_on_J2',
                              'fixed_outer_Pi54_29_preserving_standard_owners','signed_staircase_S',
                              'weighted_Serre_Laurent_pairing'],
            'weighted_terms':r['terms'],'top_J3_terminal_contribution':0,
            'top_J3_required_for_closure':True,
            'null_row_domain_adapter':'all_twenty_row_regular_transport_domain',
            'J2_global_minus_applied_by_lift':True,
            'signed_staircases_per_Laurent_coefficient':24})
    return {'schema':'tr01-weighted-transport-template-v1','source_pins':pins,
        'selection_sha256':SELECT_SHA,'weighted_requests_sha256':WEIGHT_SHA,
        'source_components':source_components(),'closed_lift':closed_lift_schema(),'required_frame':FRAME,
        'scalar_maps':scalar_maps,'requests':requests,
        'outer_domain':{'carrier':54,'legal':29,'standard_per_owner':5251,
                        'lift_bounds':[[36,20],[42,23],[48,26],[54,29]],
                        'standard_units':'only identical retained owner standard tag on target intersection'},
        'combined_pole_contract':{'pair':pole['recipe']['pair'],'identity':pole['recipe']['definitions']['identity'],
             'derivative':pole['recipe']['definitions']['derivative'],
             'generic_identity_is_not_source_clearing':True,'source_clearing_verified':False},
        'order_comparison':{'fresh_definition':'carrier (aux5 rank-1), numeric low-bit mask, standard',
              'historical_definition':'not authenticated by current source package',
              'reindexing_is_not_rebuilding_cup_source':True,
              'cross_order_equivalence':'unresolved; require full source/detector comparison, not seedwise E zero'},
        'adapter_slots':ADAPTER_SLOTS,'regular_extension_requirement':'WHOLE cleared coefficient must extend onto designated standard target intersection, not only common localization',
        'source_HPL_formula':'-lambda_(L,f) S Pi_out H_-1 delta H_0 delta j(Rsharp)',
        'adjoint_formula':'-j^* delta^* H_0^* delta^* H_-1^* (S Pi_out)^* lambda_(L,f)',
        'finite_domain':{'convolution_predicate':'p_i+sum_finite a_vi-sum_infinity a_vi-shift_i=-m_i-1',
                         'shift_i':'sum_infinity(54*d_b+29*deg(ell_vi)+5251)',
                         'J2_numerator_coordinate_degree_upper':28036,'J2_Laurent_envelope':[-38070,61421],'full_lift_Laurent_envelope':[-45684,73705],'occupied_support':False},
        'distinct_map_exponent_pairs':121,
        'status':'template_bound_to_conditional_null_theorem_actual_source_still_rejected',
        'physical_source_evaluated':False,'actual_source_admitted':False,'execution_release':False,
        'obstruction':'undecided'}

if __name__=='__main__':
    print(json.dumps(build_template(),indent=2,sort_keys=True))
