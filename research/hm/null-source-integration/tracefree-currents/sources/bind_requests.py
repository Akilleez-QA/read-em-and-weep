"""Read-only v5 graph specialization. No compiler imports or source arithmetic.

Input is exactly request(seed) for seed12/30 below; JSON types are significant.
Git objects are read at one immutable commit. The bounded gzip contains metadata,
not expanded source polynomials. No all-seed compiler/checker is executed.
"""
import argparse
import copy
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess

REV='ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18'
PREFIX='research/hm/null-operator-compiler/'
FRAME='global-finite-product-frame'
MANIFEST_BLOB='7e4a18ed9fe8a9c32cc6cf3b710e276c69af5c79'
ARCHIVE_SHA='545c29e4c0aba0a2dedb0c58e61ca57b490840367f6415104b568b511f965124'
GRAPH_SHA='cc21900c9071899dd1e607ba476451877e6ea3a92e44cd8dd926f5bfbdadd6fe'
GRAPH_BYTES=3379185
GRAPH_CANONICAL_SHA='85c7d3f5147c558ffc02821260bfb425014844913a77819d90e0f6491be93e16'
PINS_CANONICAL_SHA='aebd4c19f98a41e7d413b2bfc3343ce7b0e106c010f7a75689f12ab08a3e907a'
OWNERS={12:[[12,0,5,8,1],[12,1,1,9,9],[12,2,2,11,13],[12,3,4,15,15]],
        30:[[30,i,i,m,t] for i,(m,t) in enumerate(zip((0,1,3,7,15),(0,8,12,14,15)))]}

def need(ok,msg):
    if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def request(seed):
    need(type(seed) is int and seed in OWNERS,'seed12/30 only')
    return {'schema':'codex-v5-e34-request-v1','seed':seed,'owners':[o[:] for o in OWNERS[seed]],
            'orientation':1,'frame':FRAME,'channel':'E34(T12F12)','prefix_mask_scope':'fixed-mask-term'}
def git_read(repo,name):return subprocess.check_output(['git','show',REV+':'+PREFIX+name],cwd=repo)
def git_blob(raw):return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def authenticate(repo,reader=None):
    read=reader or (lambda name:git_read(repo,name))
    manifest=read('SHA256SUMS');need(git_blob(manifest)==MANIFEST_BLOB,'manifest blob drift')
    pins={}
    for line in manifest.decode().splitlines():
        digest,name=line.split(None,1);need(Path(name).name==name,'nonlocal manifest filename');pins[name]=digest
    names=('compile_actual_scalar_differential_kernel.py','physical_current_source_binding.py',
           'resolution_selector_source_binding.py','owned_scalar_denominator_binding.py',
           'outer_partition_source_binding.py','hm-pinned-model.json','hm-pinned-source-formulas.js',
           'authenticated-refined-detector-composition.md','refined-prefix-pruning-audit.md',
           'outer-pinned-source-identity.md','outer-pinned-frames-and-poles.md',
           'compile_refined_detector_metadata.py','prune_refined_selector_paths.py',
           'actual-scalar-differential-kernel.json.gz')
    blobs={};archive=None
    for name in names:
        raw=read(name);need(hashlib.sha256(raw).hexdigest()==pins[name],'source drift: '+name)
        blobs[name]={'git_blob':git_blob(raw),'sha256':pins[name]}
        if name.endswith('.gz'):archive=raw
    need(hashlib.sha256(archive).hexdigest()==ARCHIVE_SHA,'archive pin')
    with gzip.GzipFile(fileobj=io.BytesIO(archive)) as stream:raw=stream.read(GRAPH_BYTES+1)
    need(len(raw)==GRAPH_BYTES and hashlib.sha256(raw).hexdigest()==GRAPH_SHA,'graph size/hash')
    graph=json.loads(raw)
    need(graph['schema']=='hm-actual-scalar-rational-kernel-v5' and graph['seed_count']==78 and graph['edge_branch_count']==624,'graph schema')
    need(all(graph[k] is False for k in ('actual_factorization_accepted','actual_detector_authenticated','execution_release','physical_source_evaluated')),'source gates')
    return graph,{'commit':REV,'manifest_git_blob':MANIFEST_BLOB,'files':blobs,'graph_sha256':GRAPH_SHA}
def substitute(x,seed,owners):
    if isinstance(x,list):
        if len(x)==3 and isinstance(x[0],str) and x[0] in ('carrier','legal_mask','standard_tag'):
            need(x[1]==seed and type(x[2]) is int and 0<=x[2]<len(owners),'foreign symbolic owner')
            return owners[x[2]][{'carrier':2,'legal_mask':3,'standard_tag':4}[x[0]]]
        return [substitute(y,seed,owners) for y in x]
    if isinstance(x,dict):return {k:substitute(v,seed,owners) for k,v in x.items()}
    return x

def bind(req,graph,pins):
    need(hashlib.sha256(canonical(graph).encode()).hexdigest()==GRAPH_CANONICAL_SHA,'unauthenticated or mutated source graph')
    need(hashlib.sha256(canonical(pins).encode()).hexdigest()==PINS_CANONICAL_SHA,'source pin omission/mutation')
    need(isinstance(req,dict) and type(req.get('seed')) is int,'request object/int seed')
    sid=req['seed'];need(canonical(req)==canonical(request(sid)),'exact request/owner/order/frame/channel/scope required')
    src=graph['seeds'][sid];need(src['seed']==sid,'seed index')
    owners=req['owners'];rec=substitute(src,sid,owners)
    need(rec['weighted_owners']==list(range(len(owners))),'lost prefix weight')
    need(rec['standard']==[o[4] for o in owners] and rec['selector_source_binding']['owners']==owners,'owner graph mismatch')
    coeff=2 if sid==12 else 1;need(rec['coefficient']==coeff,'effective coefficient')
    tail=rec['tail'];i,j,k=tail
    expected=[([j,k],2,'L',3,1),([j,k],3,'L',2,-1),([i,j],3,'U',2,1),([i,j],2,'U',3,-1)]
    branches=[b for b in rec['derivative_terms'] if b['derivative_pair']==[2,3]]
    need(len(branches)==4,'four E34 branches')
    records=[]
    for b,(edge,d,kind,c,sign) in zip(branches,expected):
        need((b['edge'],b['coordinate'],b['current'][0],b['current'][1],b['coefficient'])==(edge,d,kind,c,[sign,2]),'branch order/sign')
        binding=b['current_source_binding'];need(binding['moving_frame_log_terms_retained'] is True and binding['physical_matrix_identified_with_normalized'] is False,'frame witness')
        need(b['owned_edge_definition']['vertices']==[owners[o] for o in edge],'edge owner binding')
        records.append({'id':b['id'],'effective_scalar_coefficient':[coeff*sign,2],
                        'demand_current':{'operator':'tracefree','formula':'R-tr(R)/2*I_2',
                         'input_ast':copy.deepcopy(binding['normalized_source_ast']),
                         'frame':FRAME,'shape':[2,2],
                         'raw_v5_projection_equivalence':'unresolved; raw source AST retained for provenance'},
                        'source_branch':b,'normal_order_source_reference':{'function':'compile_term','template':'quotient-and-frame-v1','source_blob':pins['files']['compile_actual_scalar_differential_kernel.py']['git_blob'],
                         'requires_demand_current_projection':True,
                         'template_application':'C must contract demand_current; equivalence to raw v5 C is not asserted'},
                        'pending_null_lemma':{'branch_id':b['id'],'owners':owners,'scalar_edge_owners':[owners[o] for o in edge],
                         'input_pair':[0,1],'derivative_pair':[2,3],'coordinate':d,'frame':FRAME,
                         'numerator_slot':'arbitrary edge numerator in v5; T12F12 realization unresolved',
                         'must_instantiate':['exact combined inner T12F12 branch/prism map and signed source ordering',
                          'full-owner grouped cancellation equality before derivative; physical Q/weight derivatives retained',
                          'actual denominator orders per owner, incl auxiliary5 dh and carrier0 dh where present',
                          'homogeneous standard/frame shifts and derivative suffix bounds',
                          'exact finite Laurent source-domain predicate or proved admissible equivalent'],
                         'proof_reference':None,'discharged':False}})
    selector=copy.deepcopy(rec['selector_source_binding'])
    # v5 carries a prefix-mask family merger. It is NOT applied to this fixed term.
    selector.pop('prefix_mask_merger',None)
    fixed_legal=[{'owner':o[:],'legal_mask':o[3],
                  'definition':'product_i ell_(mask_i,i)^29 * Q_(i,mask_i)',
                  'mask_bits_low_first':[(o[3]>>i)&1 for i in range(4)],
                  'component_of_existing_outer_weight':True,'multiply_as_extra_factor':False,
                  'replace_by_one':False} for o in owners]
    selector['prefix_mask_policy']={'scope':'fixed-mask-term','collapse_applied':False,
      'prefix_owner_positions':rec['deleted_prefix_owners'],
      'legal_weight_replaced_by_one':False,'removed_combinations':0}
    result={'schema':'codex-v5-seed-binding-v1','request':req,'source_authentication':pins,
            'effective_word_coefficient':coeff,'selector_source_binding':selector,
            'source_selector_provenance':{'usage':'provenance-only; collapsed-mask claims do not apply to this request',
             'applied_to_fixed_mask_request':False,'source_record':rec['selector_source_binding']},
            'fixed_mask_legal_weights':fixed_legal,
            'outer_weight_source_bindings':rec['outer_weight_source_bindings'],
            'weighted_owners':rec['weighted_owners'],'deleted_prefix_owners':rec['deleted_prefix_owners'],
            'kernel_owners':rec['kernel_owners'],'kappa':rec['kappa'],'branches':records,
            'compiler_scope':'v5 raw AST provenance plus explicit tracefree request wrapper; equality to raw v5 contraction unresolved',
            'fixed_mask_warning':'one fixed-prefix-mask term, not collapsed prefix-mask family',
            'null_ownership':'combined-inner pole/cancellation algebra and historical-order audit remain with null',
            'unresolved_regularization_group':next(x for x in graph['unresolved_leaves'] if x['id']==f's{sid}:regularization'),
            'gates':{k:False for k in ('raw_v5_projection_equivalence','T12F12_realized','combined_inner_poles_discharged','Laurent_admitted','actual_detector_admitted','execution_release','physical_source_evaluated','historical_order_audit_accepted')}}
    validate_semantics(result)
    return result

def _validate_semantics(result):
    """Local semantic controls, independent of source-graph hash matching."""
    req=result['request'];owners=req['owners'];sid=req['seed']
    need(req['prefix_mask_scope']=='fixed-mask-term','fixed mask scope')
    active=result['selector_source_binding']
    need('prefix_mask_merger' not in active,'collapsed source merger leaked into active selector')
    need(active['prefix_mask_policy']=={'scope':'fixed-mask-term','collapse_applied':False,
         'prefix_owner_positions':[0] if sid==12 else [0,1],
         'legal_weight_replaced_by_one':False,'removed_combinations':0},'fixed mask policy')
    provenance=result['source_selector_provenance']
    need(provenance['applied_to_fixed_mask_request'] is False and provenance['usage'].startswith('provenance-only;'),'source collapse applied')
    factors=result['fixed_mask_legal_weights']
    need(len(factors)==len(owners),'lost fixed-mask legal weight')
    for o,factor in zip(owners,factors):
        need(factor=={'owner':o,'legal_mask':o[3],
          'definition':'product_i ell_(mask_i,i)^29 * Q_(i,mask_i)',
          'mask_bits_low_first':[(o[3]>>i)&1 for i in range(4)],
          'component_of_existing_outer_weight':True,'multiply_as_extra_factor':False,
          'replace_by_one':False},'fixed legal factor changed')
    for branch in result['branches']:
        demand=branch['demand_current'];source=branch['source_branch']['current_source_binding']
        need(demand['operator']=='tracefree' and demand['formula']=='R-tr(R)/2*I_2','missing tracefree request projection')
        need(demand['input_ast']==source['normalized_source_ast'],'projected wrong current')
        need(demand['frame']==FRAME and demand['shape']==[2,2],'tracefree frame/shape')
        need(branch['normal_order_source_reference']['requires_demand_current_projection'] is True,'normal ordering bypasses projection')
    need(result['gates']['raw_v5_projection_equivalence'] is False,'unproved raw-projection equivalence')
    return True

def validate_semantics(result):
    try:
        return _validate_semantics(result)
    except (KeyError,TypeError,IndexError) as exc:
        raise ValueError('malformed fixed-mask/projection semantics') from exc

def validate_result(req,result,graph,pins):
    validate_semantics(result)
    need(canonical(result)==canonical(bind(req,graph,pins)),'result mutation')
    return True

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',default=str(Path(__file__).resolve().parents[4]));p.add_argument('--seed',type=int,choices=(12,30),required=True);a=p.parse_args()
    graph,pins=authenticate(a.repo);print(json.dumps(bind(request(a.seed),graph,pins),sort_keys=True,indent=2))
if __name__=='__main__':main()
