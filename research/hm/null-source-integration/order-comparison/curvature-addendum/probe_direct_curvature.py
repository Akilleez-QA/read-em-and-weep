"""Read-only factored support probe for a NEW direct F curvature kernel.
Dependencies are supplied explicitly; no physical coefficients are evaluated.
"""
import sys,json,itertools,hashlib
from pathlib import Path
# Fail closed on changed public dependencies before importing their code.
pins=json.loads(Path(__file__).with_name('immutable-source-pins.json').read_text())
for name,expected in pins['git_blobs'].items():
    raw=(Path(sys.argv[1])/name).read_bytes()
    observed=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if observed!=expected:raise ValueError('Pinned public dependency changed: '+name)
sys.path.insert(0,sys.argv[1])
import lower_permuted_standard_sector as core
from preflight_selected_coefficient_support import Support

def build(maskA,maskB,maskC,include_internal=False):
    # Fixed standard tags 3,11,15, then fresh source sort. All owners survive.
    labels=sorted([(1,maskA,3),(1,maskB,11),(4,maskC,15)])
    vs=tuple(core.owned.VertexLabel(4,o,*v) for o,v in enumerate(labels))
    lo=core.Lower(vs);g=lo.g;v=lo.v
    # Exact diagonal selector for local C_swap,N=-B_01(F_N)/2.
    # This is minus C_ON on a swapped pair; zero support is sign invariant.
    gamma=lo.rat(g.mul(g.c(2),v[1],g.add(g.pow(v[1],2),g.mul(g.pow(v[2],2),v[3]))),{lo.key(vs[0],'H'):1})
    logdiff=lo.add(lo.log(vs[1],0)[0][0],lo.neg(lo.log(vs[0],0)[0][0]))
    C=lo.mul(lo.rat(g.c(1,2)),lo.mul(gamma,logdiff))
    den={}
    for owner in vs:
        den[lo.key(owner,'H')]=14
        for i in range(4):
            if owner.legal_mask>>i&1:den[lo.key(owner,'L',i)]=1
    inv=lo.rat(g.c(1),den)
    roots={'A':lo.cancel(lo.mul(C,lo.diff(inv,1))),'B':lo.cancel(lo.mul(C,inv))}
    M=[(0,0,-2,-2)[i]+sum(71+2*(o.legal_mask>>i&1) for o in vs) for i in range(4)]
    s=Support(g.nodes);out=[]
    for kind,item in roots.items():
        shift=[int(kind=='B' and i==1) for i in range(4)];certificate=None
        for w in itertools.product((-1,0,1),repeat=4):
            if not any(w):continue
            bounds=s.bound(item['root'],w)
            if bounds is None:certificate={'literal_zero':True};break
            target=sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
            loP=sum(w[i]*(shift[i] if w[i]>=0 else M[i]) for i in range(4))
            hiP=sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))
            needed=(target-bounds[1],target-bounds[0])
            if hiP<needed[0] or loP>needed[1]:
                certificate={'normal':w,'multiplier_bounds':bounds,'target':target,'numerator_bounds':[loP,hiP],'needed':needed,'gap':max(needed[0]-hiP,loP-needed[1])};break
        out.append({'kind':kind,'certificate':certificate,'denominator_ledger':item['derived_denominators']})
    result={'input_masks':[maskA,maskB,maskC],'owners':[o.data() for o in vs],'complete_F_numerator_degree':M,'results':out}
    if include_internal:result['internal']={'dag':g.nodes,'roots':roots}
    return result

if __name__=='__main__':
    core.outer.authenticate_public_sources()
    core.contraction_certificate()
    rows=[build(a,b,c) for a,b,c in itertools.product((0,4,8,12),(1,5,9,13),range(16))]
    unresolved=[(r['input_masks'],v['kind']) for r in rows for v in r['results'] if v['certificate'] is None]
    gaps=[v['certificate']['gap'] for r in rows for v in r['results'] if v['certificate'] and 'gap' in v['certificate']]
    out={'schema':'seed4-direct-curvature-support-v1','scope':'new direct-F kernels on all 256 active potentially nonzero intra-carrier swap assignments','tuple_count':len(rows),'multiplier_count':2*len(rows),'unresolved':unresolved,'minimum_gap':min(gaps),'physical_polynomial_evaluation':False,'physical_polynomial_expansion':False,'execution_release':False,'results':rows}
    destination=Path(__file__).parent
    (destination/'direct-curvature-support.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n')
    names=['lower_permuted_standard_sector.py','preflight_selected_coefficient_support.py','physical_current_source_binding.py','outer_partition_source_binding.py','owned_scalar_denominator_binding.py','hm-pinned-model.json']
    hashes={name:hashlib.sha256((Path(sys.argv[1])/name).read_bytes()).hexdigest() for name in names}
    (destination/'dependency-hashes.json').write_text(json.dumps(hashes,sort_keys=True,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='results'},sort_keys=True))
