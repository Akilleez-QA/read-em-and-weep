#!/usr/bin/env python3
"""Bounded demand construction only. No scalar evaluation or physical lowering."""
import sys
sys.dont_write_bytecode = True
import argparse
from collections import Counter
import hashlib
import importlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path

RELEASE = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
SOURCE = '08b73637d4136f91606aad332c46cafd064417f8'
PUBLIC = package_path()
MANIFEST_SHA256 = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'
ENDPOINT = Path(__file__).resolve().parents[2] / 'certificates' / 'endpoint-support.json'
ENDPOINT_SHA256 = '18faf702e382b1484ca6b3f8e08ff2f8500f615cc9d3c27227dee968306aa24e'
MODULES = ('owned_scalar_denominator_binding', 'physical_current_source_binding',
           'outer_partition_source_binding', 'compile_refined_detector_metadata',
           'prune_refined_selector_paths', 'resolution_selector_source_binding',
           'lower_selected_kernel_denominators')
OWNERS = [[12,0,5,8,1], [12,1,1,9,9], [12,2,2,11,13], [12,3,4,15,15]]
REQUEST = {'schema':'a01-seed12-e34-request-v1','release_pin':RELEASE,
           'source_pin':SOURCE,'seed':12,'q':3,'row':4,'entry':['M10',2,6],
           'staircase':[1,9,13,15],'orientation':1,'owners':OWNERS,
           'operator':'E34(T12F12)','word':'H0_A I_B transpose(Rbar_BCD) P_B',
           'frame':'global-finite-stripped; normalized residual at B'}

def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def load_public():
    raw = (PUBLIC/'release-manifest.json').read_bytes()
    require(hashlib.sha256(raw).hexdigest()==MANIFEST_SHA256,'manifest hash mismatch')
    manifest = json.loads(raw)
    for name in MODULES:
        path=PUBLIC/(name+'.py')
        require(hashlib.sha256(path.read_bytes()).hexdigest()==manifest['files_sha256'][path.name],
                'public module hash mismatch: '+name)
        if name in sys.modules:
            require(Path(sys.modules[name].__file__).resolve()==path.resolve(),'foreign module: '+name)
    sys.path.insert(0,str(PUBLIC))
    result=[importlib.import_module(name) for name in MODULES]
    for name,mod in zip(MODULES,result):
        require(Path(mod.__file__).resolve()==(PUBLIC/(name+'.py')).resolve(),'wrong import path')
    return result

def block_occurrences(ast):
    """Tree multiplicities, including shared leaves; NOT derived pole orders."""
    counts=Counter()
    def walk(node):
        if isinstance(node,dict) and 'op' in node:
            if node['op'] in ('pinned_rational_block','pinned_resolution_rational_block'):
                _,owner,name,den=node['args']
                counts[(tuple(owner),name,den)]+=1
            for arg in node['args']:walk(arg)
        elif isinstance(node,(list,tuple)):
            for child in node:walk(child)
    walk(ast)
    return [{'owner':list(o),'block':n,'denominator':d,'tree_occurrences':c}
            for (o,n,d),c in sorted(counts.items())]

def compile_request(request):
    require(type(request) is dict and canonical(request)==canonical(REQUEST),
            'unsupported request fields or changed exact input')
    owned,current,outer,spec,prune,selector,lower=load_public()
    endpoint_raw=ENDPOINT.read_bytes()
    require(hashlib.sha256(endpoint_raw).hexdigest()==ENDPOINT_SHA256,'endpoint evidence changed')
    endpoint=json.loads(endpoint_raw)
    require(endpoint['source_commit']==RELEASE,'endpoint release mismatch')
    flags=[r for row in endpoint['results'] if row['q']==3 and row['row']==4
           for r in row['unknown_records'] if r['sampled_carriers']==[5,1,2,4]
           and r['sorted_carriers']==[5,1,2,4]]
    require(len(flags)==1,'missing exact UNKNOWN carrier flag')
    vs=tuple(owned.VertexLabel(*v) for v in request['owners'])
    binding=selector.bind_seed(12,vs)
    require(binding['row']==4 and binding['entry']==[2,6] and binding['coefficient']==2,
            'source selector mismatch')
    require(binding['tail_owners']==[v.data() for v in vs[1:]],'tail mismatch')
    # This bounded guard must reject before creating any physical polynomial DAG.
    try:
        lower.Lower(vs[1:])
    except ValueError as exc:
        require(str(exc)=='selected staircase only','unexpected Lower rejection')
        lower_status={'supported':False,'reason':str(exc),'actual_tail_tags':[9,13,15],
                      'required_tail_tags':[3,11,15],'fallback_used':False}
    else:
        raise ValueError('Lower domain changed; new independent review required')
    g=lower.DAG()  # Only node interning; never poly, current, cancel, diff or build.
    def node(op,children=(),**fields):
        require(len(g.nodes)<2048,'metadata node cap')
        return g.node(op,{'children':list(children),**fields})
    def matrix(m):
        children=[];args=[]
        for arg in m.args:
            if isinstance(arg,current.Matrix):
                args.append({'child':len(children)});children.append(matrix(arg))
            else:args.append({'literal':arg})
        return node('public_matrix',children,matrix_op=m.op,shape=list(m.shape),args=args)
    kernel=matrix(current.mul(selector.block(vs[0],'H0'),selector.block(vs[1],'I')))
    projection=matrix(selector.block(vs[1],'P'))
    weights=[node('outer_weight_reference',owner=v.data(),binding=outer.bind_reference(v),
                  powers={'carrier':54,'legal':29,'standard_unit_bound':5251}) for v in vs]
    kappa=spec.ROWS[4][2]
    terms=[]
    # Zero-based d=2,3 represent physical coordinates 3,4. E signs are +,-,+,-.
    for edge,d,kind,c,sign in (((2,3),2,'L',3,1),((2,3),3,'L',2,-1),
                               ((1,2),3,'U',2,1),((1,2),2,'U',3,-1)):
        curr=current.normalized_current(kind,c,vs[1:])
        curr_id=matrix(curr)
        # Keep tf explicit, as in the published selected lowering; do not infer tr=0.
        tf=node('tracefree',(curr_id,),rule='R-tr(R)/2 Id')
        transpose=node('transpose',(tf,))
        contraction=node('entry_of_matrix_product',(kernel,transpose,projection),entry=[2,6],
                         word='H0_A I_B transpose(tf(current_BCD)) P_B')
        multiplier=node('symbolic_product',(*weights,contraction),
                        prefix_owner=vs[0].data(),weights_kept_separate=True)
        edge_owners=[vs[i].data() for i in edge]
        # The full prism/K/AHS combination must be canceled together, before any derivative.
        pending=node('combined_inner_regularization_request',owners=edge_owners,
                     scalar='s12=T12F12',pair=[0,1],inner_partition=[14,1],
                     branches=['Hrho','Pi Kcov R','Pi S h A R'],
                     inserted_owner_sums='bounded symbolic; common vertices with source-first signs',
                     denominator_definition='owned_scalar_denominator_binding.denominator',
                     suffix_denominators=[{'owner':v,'carrier':14,
                         'legal':list(owned.decode_legal_mask(v[3])),
                         'standard':[5250*b for b in owned.decode_standard_tag(v[4])]} for v in edge_owners],
                     witness=None,status='UNRESOLVED; no cancellation executed')
        derivative=node('derivative_after_cancellation_request',(pending,),coordinate=d,
                        conversion=owned.character_conversion((2,3),(0,1),d),
                        required_witness='exact full-owner N14 combined quotient',
                        enabled=False,weight_derivatives_retained=True)
        # A schema of the backward coefficient demand, not extraction of any coefficient.
        convolution=node('normal_order_demand',(multiplier,derivative),
                         target_exponent=list(kappa),multiplier_exponent='nu in certified finite support (pending)',
                         scalar_exponent='kappa - nu + unit_d',
                         integer_factor='kappa[d] - nu[d] + 1',
                         zero_rule='omit iff integer_factor == 0',
                         prefix_kernel_is_not_differentiated=True,
                         outer_weights_inside_multiplier=True,
                         coefficient_extraction_enabled=False)
        terms.append({'edge_owners':edge_owners,'derivative_coordinate':d,
                      'current':[kind,c],'current_node':curr_id,'E_sign':sign,
                      'terminal_coefficient':2,'E_denominator':2,'orientation':1,
                      'root':convolution,'current_block_occurrences':block_occurrences(curr.data())})
    root=node('signed_demand_sum',tuple(t['root'] for t in terms),
              coefficients=[[t['terminal_coefficient'],t['E_sign'],t['E_denominator']] for t in terms])
    out={'schema':'a01-seed12-e34-demand-dag-v1','request':request,
         'source_pin':SOURCE,'release_pin':RELEASE,'reviewers':['Codex-A02','Codex-V03'],
         'artifact_review':'pending','status':'BOOLEAN_UNKNOWN; metadata demand only',
         'domain':'characteristic zero; one ordered full-owner quadruple; row4 M10[2,6]; E34(T12F12) only',
         'selector_binding':binding,'lower_capability':lower_status,
         'endpoint_flag_evidence':{'path':'research/codex-swarm/certificates/endpoint-support.json','sha256':ENDPOINT_SHA256,
              'record':flags[0],'scope':'carrier flag superdomain only; no concrete nonzero or active claim'},
         'kernel_block_occurrences':block_occurrences({'op':'multiply','args':[binding['left_ast'],binding['right_ast']]}),
         'outer_weight_nodes':weights,'terms':terms,'root':root,'dag':g.nodes,
         'denominator_policy':{'occurrence_counts':'syntactic tree multiplicities, not pole exponents',
              'full_owner_key_fields':['seed','owner','carrier','legal_mask','standard_tag'],
              'inverse_determinants':'retained as public adjugate_over_determinant nodes',
              'differentiated_block_poles':'unresolved; partial nodes differentiate entire rational block',
              'derived_current_pole_certificate':False},
         'frame':'normalized physical current at B, matching selector conjugation once; both Q terms retained; no infinity derivative substitution',
         'Rsharp_context':['M0^0','B34(F12)','B12(F34)','E34(T12F12)','E12(T34F34)'],
         'evidence':['hash-bound public selector.bind_seed(12, exact owners)',
                     'public current.normalized_current L/U at coordinates 2,3',
                     'public Lower rejects exact requested tail; no substitution',
                     'formal coefficient product/partial identity only'],
         'gates':{k:False for k in ('actual_source_admitted','pole_domain_proved','Laurent_admitted',
              'execution_release','arithmetic_cost_certificate','physical_polynomial_evaluation',
              'physical_polynomial_expansion','active_or_nonzero_proved','complete_Rsharp_proved')},
         'gap':'No combined inner quotient witness, instantiated F12/T12 source DAG, support predicate, or physical pole/execution certificate.',
         'next_step':'A02/V03 review exact word/sign/frame and demand schema; then bind combined N14 quotients for this tuple before derivative lowering.'}
    require(len(canonical(out).encode())<262144,'serialized metadata cap')
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('request',type=Path)
    args=p.parse_args()
    try:
        require(args.request.stat().st_size<16384,'request byte cap')
        def unique(pairs):
            d={}
            for k,v in pairs:
                require(k not in d,'duplicate request key');d[k]=v
            return d
        request=json.loads(args.request.read_text(),object_pairs_hook=unique)
        print(canonical(compile_request(request)))
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr);return 2
    return 0

if __name__=='__main__':
    sys.exit(main())
