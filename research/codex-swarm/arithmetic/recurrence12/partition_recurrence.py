"""A03: source-bound outer-weight recurrence specifications; no physical evaluator.
Run with python -B. Physical source construction is symbolic only. Synthetic
integer metadata convolution lives in synthetic_affine_dp.py, a separate API.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path
import hashlib
import importlib
import json
import sys

RELEASE = package_path()
PIN = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
OLD_PIN = '08b73637d4136f91606aad332c46cafd064417f8'
HASHES = {
 'owned_scalar_denominator_binding':'ef82c151febff2f82e4e27a24e38f7f884814d0a99b75a75b81459abfc356018',
 'physical_current_source_binding':'8cc3f3be47c6944e983a8b1922470a27c1a413b3fe9059f97c75b7a2cd967d3d',
 'outer_partition_source_binding':'e99e4a8c8a3736a7ef583d66f8de21680fae7dca5fe253bff7483426c513fa00',
 'lower_selected_kernel_denominators':'8c3bb290df33a2d17da477cd30a36cc581aeddc4cdb3e276fdfbf35973ced89d',
 'resolution_selector_source_binding':'77743aa6a9334db0f7c2054602d69f0adae9286826ca74cb50985da917c0809f',
 'prune_refined_selector_paths':'1f146ef1a38d6fbc396944753800509c85fa07c2cc16607b3ebdb138bc62b407',
 'compile_refined_detector_metadata':'5a83ae06faf8489d8b7e34a390b9564206df451c85ed97a9e634ebc791947710',
}
OWNERS = ((12,0,5,8,1),(12,1,1,9,9),(12,2,2,11,13),(12,3,4,15,15))
GATES = {k:False for k in ('actual_source_admitted','source_pole_certificate_derived',
 'Laurent_admitted','physical_polynomial_expansion','physical_polynomial_evaluation',
 'arithmetic_cost_certificate','execution_release','actual_factorization_accepted')}


def load_public():
    if not sys.dont_write_bytecode:
        raise ValueError('run python -B to avoid writing public modules')
    for name,digest in HASHES.items():
        path = RELEASE / (name+'.py')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
            raise ValueError('public hash mismatch: '+name)
        if name in sys.modules and Path(sys.modules[name].__file__).resolve()!=path.resolve():
            raise ValueError('foreign module already imported: '+name)
    sys.path.insert(0,str(RELEASE))
    try:
        modules={name:importlib.import_module(name) for name in HASHES}
    finally:
        sys.path.pop(0)
    for name,module in modules.items():
        if Path(module.__file__).resolve()!=(RELEASE/(name+'.py')).resolve():
            raise ValueError('import outside authenticated directory')
    return modules


def affine(constant, coefficients):
    return {'constant':constant,'coefficients':coefficients}


def bounded_k(g, lo, hi, top, factors):
    """Each factor is (base, constant, slope); no k is enumerated."""
    return g.node('bounded_affine_sum', {'index':'k','lower':lo,'upper':hi},
        {'coefficient':{'op':'binomial','top':top,'bottom':'k'},
         'powers':[{'base':b,'exponent':affine(c,[s])} for b,c,s in factors]})


def outer_quotient_plan(v, modules):
    """Interpret outer.formulas, reuse actual composition_sum; no Lower bypass.
    Local references are unevaluated polynomials, tagged with the full owner.
    Returned root is Q_v = rho_v / matching local clearing factors only.
    """
    owned=modules['owned_scalar_denominator_binding']
    outer=modules['outer_partition_source_binding']
    base=modules['lower_selected_kernel_denominators']
    if tuple(v.data()) not in OWNERS:raise ValueError('unsupported owner')
    e=owned.decode_standard_tag(v.standard_tag); m=owned.decode_legal_mask(v.legal_mask)
    s=sum(e); d=s+1; T=535; L=d*534+1; g=base.DAG()
    ref=lambda kind,*args:g.node('owned_local_polynomial_reference',v.data(),kind,*args)
    vl=[ref('v',i) for i in range(5)]
    # c_i=(-1)^(s-i) H_(s-i) in the finite variables; retain as reference.
    cs=[ref('signed_complete_homogeneous',s-i,(-1)**(s-i),[h for h in range(4) if not e[h]]) for i in range(d)]
    a=ref('a'); v2a=g.mul(vl[2],a)
    js=range(d) if v.carrier==5 else (v.carrier,)
    if v.carrier!=5 and v.carrier>s:raise ValueError('unsupported literal-zero chart')
    pieces=[]; composition=[]
    for j in js:
        B=base.composition_sum(g,d,j,T,cs,vl[:d])
        h=ref('h',j)
        if v.carrier==5:
            C=bounded_k(g,0,53,107,((h,0,1),(vl[2],107,-1),(a,53,-1)))
        else:
            C=bounded_k(g,54,107,107,((h,-54,1),(v2a,107,-1)))
        pieces.append(g.mul(B,C))
        composition.append({'chosen':j,'dimension':d,'total':L,'threshold':T,
          'index_degree_sum_of_body_powers':2*L-T,
          'summand_count_symbolic':f'sum_(a=0..{j}) (-1)^a binom({j},a) binom({L-T}+{d-1}-{T}*a,{d-1}); binom(n,r)=0 if n<r',
          'actual_polynomial_term_count':None,
          'recurrence':{'state':['slot','consumed_total','exponent_vector'],
            'initial':'D[0,0,zero_vector]=1; every other state=0',
            'n_bounds_by_slot':[[0,T-1] if i<j else [T,L] if i==j else [0,L] for i in range(d)],
            'transition_domain':'n in slot bounds intersect [0,L-consumed_total]',
            'transition':'D[i+1,r+n,alpha+beta] += D[i,r,alpha] binom(L-r,n) coefficient(f[i,j,n],beta)',
            'factor':'f[i,j,n]=c[i]^n * v[i]^(n-T*[i=j])',
            'answer':'coefficient(B_j,alpha)=D[d,L,alpha]',
            'prune_only':'certified remaining-support exclusion; UNKNOWN is never zero',
            'physical_coefficient_atom_enabled':False},
          'degree_bound_per_coordinate_affine_in_n':[
             {'constant':-T*(int(j>=1) if not e[h] else int(j<=3)),
              'coefficients':[(s-i if not e[h] else 0)+(int(i>=1) if not e[h] else int(i<=3)) for i in range(d)]}
             for h in range(4)]})
    root=g.add(*pieces);line_degrees=[]
    for i,bit in enumerate(e):
        if not bit:
            if m[i]:raise ValueError('unsupported zero finite-mask quotient')
            line_degrees.append(0);continue
        t=ref('local_coordinate',i);q=ref('one_minus_t_squared',i)
        if m[i]:line=bounded_k(g,0,28,57,((t,0,2),(q,28,-1)))
        else:line=bounded_k(g,29,57,57,((t,-29,2),(q,57,-1)))
        root=g.mul(root,line);line_degrees.append(56 if m[i] else 85)
    weight_degree=4 if v.carrier==5 else 5
    shift=[-(weight_degree*54+(3 if m[i] else 1)*29) if bit else 0 for i,bit in enumerate(e)]
    return {'owner':v.data(),'standard_bits_high':e,'legal_bits_low':m,
       'outer_source_reference':outer.bind_reference(v),'root':root,'dag':g.nodes,
       'composition':composition,'carrier_kernel_coordinate_degree_cap':319 if v.carrier==5 else 265,
       'legal_coordinate_degree_caps':line_degrees,
       'scalar_clearing_pullback_shift':shift,
       'global_exponent_map':'local alpha -> beta_i=(-1)^e_i alpha_i; add clearing shift and -standard_order_i, then convolve with remaining finite H/ell factors and factored source numerator',
       'source_denominator_orders':None,'source_denominator_orders_derived':False,
       'owner_capacities':{'carrier':54,'legal':[29]*4,'standard':[5251]*4}}


def declared_clearing_ledger(records):
    """Validate complete DECLARED orders, never certify their source derivation."""
    if type(records) is not list or len(records)!=4:raise ValueError('four owner records required')
    out=[]
    for owner,r in zip(OWNERS,records):
        if type(r) is not dict or set(r)!={'owner','carrier','legal','standard'}:raise ValueError('unsupported ledger fields')
        if type(r['owner']) not in (list,tuple) or any(type(n) is not int for n in r['owner']) or tuple(r['owner'])!=owner:raise ValueError('full owner mismatch')
        if type(r['carrier']) is not int or not 0<=r['carrier']<=54:raise ValueError('carrier order')
        for name,bound in (('legal',29),('standard',5251)):
            a=r[name]
            if type(a) is not list or len(a)!=4 or any(type(n) is not int or not 0<=n<=bound for n in a):raise ValueError(name+' orders')
        m=owner[3];tag=owner[4]
        for i in range(4):
            if not ((m>>i)&1) and r['legal'][i]:raise ValueError('unowned legal divisor')
            if not ((tag>>(3-i))&1) and r['standard'][i]:raise ValueError('unowned standard divisor')
        out.append({'owner':list(owner),'remaining_carrier_power':54-r['carrier'],
          'remaining_legal_powers':[(29-r['legal'][i]) if (m>>i)&1 else 0 for i in range(4)],
          'standard_orders':r['standard'][:]})
    return {'declared_orders_checked_only':True,'owners':out,'gate':GATES.copy()}



def validate_a01_request(request):
    expected={'schema':'a01-seed12-e34-request-v1','release_pin':PIN,
      'source_pin':OLD_PIN,'seed':12,'q':3,'row':4,'entry':['M10',2,6],
      'staircase':[1,9,13,15],'orientation':1,'owners':[list(o) for o in OWNERS],
      'operator':'E34(T12F12)','word':'H0_A I_B transpose(Rbar_BCD) P_B',
      'frame':'global-finite-stripped; normalized residual at B'}
    if type(request) is not dict or json.dumps(request,sort_keys=True,allow_nan=False)!=json.dumps(expected,sort_keys=True):
        raise ValueError('unsupported A01 request fields or exact-domain mutation')
    return True


def build():
    request_path=Path(__file__).resolve().parents[1] / 'seed12' / 'seed12-e34-request.json'
    request_raw=request_path.read_bytes()
    request_hash=hashlib.sha256(request_raw).hexdigest()
    if request_hash!='0208f95688e0b07e6320994713f807baf1e7e49c1938415bbe6b61d903fcfdb6':
        raise ValueError('A01 exact request hash changed; review required')
    request=json.loads(request_raw);validate_a01_request(request)
    modules=load_public();owned=modules['owned_scalar_denominator_binding']
    selector=modules['resolution_selector_source_binding']
    witness_evidence=modules['outer_partition_source_binding'].authenticate_public_sources()
    vs=tuple(owned.VertexLabel(*o) for o in OWNERS)
    binding=selector.bind_seed(12,vs)
    expected={'seed':12,'row':4,'coefficient':2,'entry':[2,6],
      'staircase_standard_tags':[1,9,13,15],'exponent':(-1,-2,-3,-3)}
    for key,value in expected.items():
        if json.dumps(binding[key])!=json.dumps(value):raise ValueError('unexpected seed12 binder '+key)
    endpoint_path=Path(__file__).resolve().parents[2] / 'certificates' / 'endpoint-support.json'
    endpoint_raw=endpoint_path.read_bytes();endpoint=json.loads(endpoint_raw)
    if endpoint['source_commit']!=PIN or endpoint['domain_is_flag_superdomain'] is not True:raise ValueError('endpoint provenance')
    row=next(r for r in endpoint['results'] if r['q']==3 and r['row']==4)
    candidates=[r for r in row['unknown_records'] if r['sampled_carriers']==[5,1,2,4] and r['sorted_carriers']==[5,1,2,4]]
    if len(candidates)!=1:raise ValueError('not exactly one UNKNOWN carrier flag')
    return {'schema':'A03-outer-recurrence-plan-v1','release_pin':PIN,'immutable_formula_pin':OLD_PIN,
      'public_module_directory':'PR79@'+PIN+'/research/hm/null-support-certificates','public_module_sha256':HASHES,
      'outer_witness_evidence':witness_evidence,
      'domain':'seed12 E34(T12F12), positive staircase (1,9,13,15), carriers (5,1,2,4), masks (8,9,11,15); outer54/legal29 ONLY',
      'a01_request_evidence':{'path':'research/codex-swarm/arithmetic/seed12/seed12-e34-request.json','sha256':request_hash,'request':request},
      'selector_binding':binding,'sorting_orientation':1,'candidate_status':'BOOLEAN_UNKNOWN',
      'endpoint_evidence':{'sha256':hashlib.sha256(endpoint_raw).hexdigest(),'record':candidates[0]},
      'weights':[outer_quotient_plan(v,modules) for v in vs],
      'prefix_policy':'owner0 H0 and outer Q remain separate from tail owners1,2,3; never merge carrier/pole owners',
      'source_current_policy':'keep A01 numerator factored; no actual coefficient atom is produced',
      'exceptional_source_denominator':'actual dh5=-v1*a; on D(a), (v1*a)^(-d)=(v0*v3*v4)^d*a^(-2d), with sign (-1)^d for dh5; this requires the actual prefix order, not yet derived here',
      'reviewer':['Codex-A04','Codex-V05'],'artifact_review':'pending','gate':GATES.copy(),
      'gap':['actual source denominator ledger and cancellation witness','inner N14 quotient and prepared derivatives','actual target finite-support and arithmetic schedule'],
      'next_step':'A04/V05 review recurrence, pullback and exceptional prefix; A01 supplies derived full-owner source ledger before any cancellation or coefficient extraction'}

if __name__=='__main__':
    print(json.dumps(build(),sort_keys=True,indent=2))
