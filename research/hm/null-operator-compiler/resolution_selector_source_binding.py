"""Pinned factored resolution selectors; no physical polynomial evaluation."""
from pathlib import Path
import hashlib
import json
import owned_scalar_denominator_binding as owned
import physical_current_source_binding as current
import prune_refined_selector_paths as pruning
import compile_refined_detector_metadata as spec

Matrix=current.Matrix
MODEL_SHA256=current.MODEL_SHA256
PROOFS={'authenticated-refined-detector-composition.md':'28a7db43cc9d8660d9d040f6bc40e4b7a1868cca8b10e93e72036b8f4a6995b3',
        'refined-prefix-pruning-audit.md':'6b3fb5db68a210d690d098397e73c0b74d58f751df65d5d6d598e3e714113d3f'}
SHAPES={'I':(15,2),'P':(2,15),'H0':(5,15),'H1':(15,10),'eta':(10,2)}

def authenticate(path=None):
    model=current.authenticate(path)
    for name,digest in PROOFS.items():
        if hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()!=digest:
            raise ValueError('selector proof hash mismatch: '+name)
    for index,c in enumerate(model['charts']):
        if c['pivot']!=(0,1,2,3,4,0)[index]:raise ValueError('pinned pivot')
        for name in ('H0','H1'):
            shape=SHAPES[name]
            if len(c[name])!=shape[0] or any(len(r)!=shape[1] for r in c[name]):raise ValueError('homotopy block shape')
    return model

def block(v,name):
    if not isinstance(v,owned.VertexLabel):raise ValueError('complete vertex required')
    if name=='E':return current.mul(block(v,'I'),block(v,'P'))
    if name not in SHAPES:raise ValueError('unknown resolution block')
    if name=='eta':
        return Matrix('pinned_pivot_section',(MODEL_SHA256,v.data(),(0,1,2,3,4,0),'eta[5*h+pivot,h]=1/v_pivot; v0=1', 'pivot=0:1; pivot=j>0:(v_j^4-product(v_k,k=0..4,k!=j))/h_j', 'h_j=v_j^5-product(v_k,k=0..4)=v_j*(v_j^4-product(v_k,k!=j)); denominator owned by this carrier'),SHAPES[name])
    denominator={'I':'di','P':'dp','H0':'dh','H1':'dh'}[name]
    return Matrix('pinned_resolution_rational_block',(MODEL_SHA256,v.data(),name,denominator),SHAPES[name])

def _product(factors):
    out=factors[0]
    for factor in factors[1:]:out=current.mul(out,factor)
    return out

def selector_matrices(path,vertices):
    """Resolve H by actual graded multiplication, including K3 -> K2 eta."""
    left=[]
    for kind,owner in path['left']:
        left.append(block(vertices[owner], 'H0' if kind=='H' else kind))
    right=[]
    for kind,owner in path['right']:
        name=('H1' if not right or right[-1].shape[1]==15 else 'eta') if kind=='H' else kind
        right.append(block(vertices[owner],name))
    return _product(left),_product(right)

def bind_seed(seed,vertices=None):
    authenticate()
    if type(seed) is not int or seed not in range(78):raise ValueError('selector seed')
    path=pruning.generate()['paths'][seed]
    record=spec.seed_records()[seed]
    row=spec.ROWS[record['row']]
    n=row[0]+1
    vertices=tuple(owned.label(seed,o) for o in range(n)) if vertices is None else tuple(vertices)
    if len(vertices)!=n or any(not isinstance(v,owned.VertexLabel) or v.seed!=seed or v.owner!=o for o,v in enumerate(vertices)):
        raise ValueError('full ordered owner ledger required')
    for v in vertices:
        expected=owned.label(seed,v.owner)
        for value,canonical in zip((v.carrier,v.legal_mask,v.standard_tag),(expected.carrier,expected.legal_mask,expected.standard_tag)):
            if isinstance(value,tuple) and value!=canonical:raise ValueError('noncanonical symbolic label')
    if all(type(v.carrier) is int and type(v.legal_mask) is int and type(v.standard_tag) is int for v in vertices):
        keys=[(-1 if v.carrier==5 else v.carrier,v.legal_mask,v.standard_tag) for v in vertices]
        if keys!=sorted(keys) or len(set(keys))!=len(keys):raise ValueError('source-first common tuple required')
        if sorted(v.standard_tag for v in vertices)!=sorted(record['standard']):raise ValueError('staircase standard ownership mismatch')
        prefix=[key[0] for key in keys[:row[0]-1]]
        if any(a>=b for a,b in zip(prefix,prefix[1:])):raise ValueError('pruned equal-carrier prefix')
    left,right=selector_matrices(path,vertices)
    a,b=path['entry']
    if not 0<=a<left.shape[0] or not 0<=b<right.shape[1]:raise ValueError('entry index')
    lr=Matrix('row',(left,a),(1,2));rc=Matrix('column',(right,b),(2,1))
    tail=tuple(vertices[o] for o in path['tail'])
    residual=Matrix('normalized_row_residual_slot',(tuple(v.data() for v in tail),),(2,2))
    contraction=current.mul(current.mul(lr,current.transpose(residual)),rc)
    kernel=current.transpose(current.mul(rc,lr))
    return {'schema':'resolution-selector-source-binding-v1','seed':seed,'row':record['row'],
        'coefficient':path['coefficient'],'entry':[a,b],'entry_indices':'zero-based',
        'terminal_block':row[3],'exponent':row[2],'staircase_standard_tags':record['standard'],
        'standard_owner_rule':'tags are reassigned by exact source-first sorting; retain sorting orientation externally',
        'owners':[v.data() for v in vertices],'tail_owners':[v.data() for v in tail],
        'weighted_owners':path['weighted_owners'],'deleted_prefix_owners':path['deleted_prefix_owners'],
        'prefix_mask_merger':path['prefix_mask_merger'],
        'left_ast':left.data(),'right_ast':right.data(),'source_ast':contraction.data(),
        'dual_kernel_ast':kernel.data(),'pairing':'coefficient * tr(dual_kernel * normalized_row_residual)',
        'frame':'common original resolution frame; normalized residual at first tail owner',
        'frame_identity':'Iphys=I D; Pphys=D^-1 P; Rphys=D Rbar D^-1; Iphys Rphys^t Pphys=I Rbar^t P',
        'frame_current_rule':'consume normalized_source_ast exactly once; retain both logarithmic Q terms',
        'pinned_model_sha256':MODEL_SHA256,'actual_factorization':False,
        'physical_polynomial_evaluation':False,'execution_release':False}

def validate_binding(binding):
    if not isinstance(binding,dict):raise ValueError('selector binding object')
    try:
        vertices=tuple(owned.VertexLabel(*v) for v in binding['owners'])
        expected=bind_seed(binding['seed'],vertices)
    except (KeyError,TypeError) as exc:raise ValueError('malformed selector binding') from exc
    if json.dumps(binding,sort_keys=True)!=json.dumps(expected,sort_keys=True):raise ValueError('mutated selector binding')
    return True

def definition():
    authenticate()
    return {'schema':'resolution-selector-source-binding-v1','pinned_model_sha256':MODEL_SHA256,
        'proof_hashes':PROOFS,'carrier_domain':[0,1,2,3,4,5],'carrier_identity':'5=star; -1 only sorting key',
        'legal_mask_bits':'coordinate i is low bit i','standard_tag_bits':'coordinate i is high bit 3-i',
        'coordinate_rule':'v0=1; vk=elementary_symmetric_k(x0,x1,x2,x3); references remain unexpanded',
        'block_rule':'charts[carrier]: I/di, P/dp, H0/dh, H1/dh; E=I P; eta[5*h+pivot,h]=1/v_pivot and other entries zero',
        'eta_owned_cancellation':'for primary j>0: h_j=v_j^5-product(v_k,k=0..4)=v_j*(v_j^4-product(v_k,k!=j)), so 1/v_j=(v_j^4-product(v_k,k!=j))/h_j; pivot0 including star has v0=1; no new unowned divisor',
        'graded_dimensions':[5,15,10,2],'residual_dimension':2,'paths':78,
        'actual_factorization':False,'physical_polynomial_evaluation':False,'execution_release':False,
        'remaining_obligations':['bounded full common-label sums and sorting signs','outer denominator cancellation','source polynomial arithmetic DAG','coefficient extraction and live-memory budget']}

if __name__=='__main__':
    if not __debug__:raise SystemExit(2)
    print(json.dumps(definition(),sort_keys=True,separators=(',',':')))
