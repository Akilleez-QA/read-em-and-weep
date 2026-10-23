#!/usr/bin/env python3
"""Universal integer/character certificate; no actual map or historical scan.

The imported geometric theorems, and the separate lower bound r>=4, are
mathematical premises. This program does not establish their hypotheses.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
NAMES = ('1', 'W', 'A', 'S4', 'D', 'T6', 'P', "W'", 'V')
DIMS = (1, 2, 3, 4, 5, 6, 4, 2, 3)
PARITY = (0, 1, 0, 1, 0, 1, 0, 1, 0)
EDGES = ((0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (5,8))
EXPECTED_HASHES = {
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
 'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md': '0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
 'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md': '868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
 'four-sources.md': 'd5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e',
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def vec(**kw):
    return tuple(kw.get(name, 0) for name in NAMES)

def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(9))

def scale(v, n):
    return tuple(n*x for x in v)

def sub(a,b):
    return add(a,scale(b,-1))

def dim(v):
    return sum(x*d for x,d in zip(v,DIMS))

def times_W(v):
    out=[0]*9
    for i,j in EDGES:
        out[i]+=v[j]
        out[j]+=v[i]
    return tuple(out)

def times_sym(v,n):
    require(n>=0, 'negative symmetric-power index')
    prev=(0,)*9
    now=v
    for _ in range(n):
        prev,now=now,sub(times_W(now),prev)
    return now

def euler_block(v,n):
    if n>=0:
        return times_sym(v,n)
    if n==-1:
        return (0,)*9
    return scale(times_sym(v,-n-2),-1)

def character_name(v):
    return {name:c for name,c in zip(NAMES,v) if c}

def authenticate_inputs():
    entries=json.loads((ROOT/'INPUTS.json').read_text())
    require(len(entries)==4,'exactly four retained direct inputs required')
    seen=set()
    for entry in entries:
        name=Path(entry['file']).name
        require(name not in seen and name in EXPECTED_HASHES,'unexpected/duplicate input')
        seen.add(name)
        raw=(ROOT/entry['file']).read_bytes()
        digest=hashlib.sha256(raw).hexdigest()
        require(digest==EXPECTED_HASHES[name]==entry['sha256'],'source SHA256 mismatch')
        require(len(raw)==entry['bytes'],'source byte count mismatch')
        require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==entry['git_blob_sha1'],'Git blob mismatch')
        require(entry['url']=='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+entry['ref']+'/'+entry['path'],'source URL mismatch')
    require(seen==set(EXPECTED_HASHES),'missing direct input')

def character_checks():
    for i in range(9):
        v=tuple(int(j==i) for j in range(9))
        require(dim(times_W(v))==2*DIMS[i],'McKay dimension failure')
        require(all(not c or PARITY[j]!=PARITY[i] for j,c in enumerate(times_W(v))),'McKay parity failure')
    M2=vec(A=1,V=2,P=3,D=4)
    M3=vec(**{"W'":3,'S4':3,'T6':6})
    M4=vec(V=2,P=4,D=3)
    require((dim(M2),dim(M3),dim(M4))==(41,54,37),'coefficient-space dimensions')
    H=sub(sub(times_W(M3),M2),M4)
    require(H==vec(A=2,V=2,P=2,D=2) and dim(H)==30,'actual ambient character')
    e1=sub(M3,times_W(M4))
    e2=sub(times_W(M3),times_sym(M4,2))
    e3=sub(times_sym(M3,2),times_sym(M4,3))
    s3=sub(times_sym(M3,2),times_sym(M2,3))
    require(e1==vec(**{"W'":-1,'T6':-3}),'E(1) Euler character')
    require(e2==vec(V=-1),'E(2) Euler character')
    require(e3==vec(**{"W'":1,'T6':2}),'E(3) Euler character')
    require(s3==vec(W=-2,S4=-1,T6=1),'Q*(3) Euler character')

    # Solve only the four-variable universal equation after the imported
    # actual primary inclusion. No historical 28/37/159-record scan is run.
    compositions=[(b,c,e,f) for b in range(1,4) for c in range(1,4)
                  for e in range(4) for f in range(4) if b+c+e+f==3]
    require(set(compositions)=={(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)},'four-source composition')
    sources={
      'D':[(2,vec(D=1)),(3,vec(**{"W'":1,'T6':1})),(4,vec(V=1)),(8,vec(**{'1':1}))],
      'P':[(2,vec(P=1)),(3,vec(**{"W'":1,'T6':1})),(4,vec(V=1)),(5,vec(**{"W'":1}))],
      'V':[(2,vec(V=1)),(3,vec(**{"W'":1,'T6':1})),(4,vec(V=2))],
      'Z':[(3,vec(**{"W'":1,'T6':2})),(4,vec(V=1))],
    }
    expected_h0_2={'D':vec(D=1),'P':vec(P=1),'V':vec(V=1),'Z':vec()}
    result={}
    for name,blocks in sources.items():
        require(sum(dim(v) for _,v in blocks)==17,'source rank')
        require(-sum(j*dim(v) for j,v in blocks)==-54,'source degree')
        require(all(not c or PARITY[i]==j%2 for j,v in blocks for i,c in enumerate(v)),'source central parity')
        for twist,expected in ((1,e1),(2,e2),(3,e3)):
            require(add(*(euler_block(v,twist-j) for j,v in blocks))==expected,'source Euler character')
        h0_2=add(*(times_sym(v,2-j) for j,v in blocks if j<=2))
        require(h0_2==expected_h0_2[name],'quadratic visibility')
        result[name]={'h0_E2_character':character_name(h0_2),'h0_E2_dimension':dim(h0_2),
                      'forward_bound':2 if dim(h0_2)>0 else 3,
                      'top_negative_degree':min(j for j,_ in blocks)}
    return {'H':character_name(H),'chi_E3':character_name(e3),'chi_Qstar3':character_name(s3)},result

def ceil_even_fraction(n,d):
    return 2*((n+2*d-1)//(2*d))

def degree_witness(r,k,l,top_degree):
    # Integers only, exhibiting consistency of this limited determinant
    # inequality. NOT an equivariant-bundle or actual-map realization.
    p,q=17-r*k,13-r*l
    lower_abs=top_degree*p+(top_degree*p)%2
    c=ceil_even_fraction(-54-r*k*(k-1)+lower_abs,k)
    if q==0:
        require((54-r*l*(2*k+l-1))%l==0,'full-endpoint degree divisibility')
        c=(54-r*l*(2*k+l-1))//l
    a=-54-k*c-r*k*(k-1)
    b=-54+l*c+r*l*(2*k+l-1)
    cs=[c+2*r*i for i in range(k+l)]
    require(all(x%2==0 for x in [a,b]+cs),'determinant parity')
    require(a<=-lower_abs,'lower endpoint degree bound')
    require((b==0) if q==0 else (b<=-(q+q%2)),'upper endpoint degree bound')
    require(a+sum(cs[:k])==-54 and a+sum(cs)==b,'plateau degree sums')
    return {'lower_endpoint_degree':a,'block_degrees':cs,'upper_endpoint_degree':b,
            'all_adjacent_determinant_defects':0}

def derive():
    authenticate_inputs()
    characters,sources=character_checks()
    profiles=[]
    refined=[]
    rows=[]
    for r in range(4,14):
        current=[]
        for k in range(1,18):
            for l in range(1,14):
                if r*k>17 or r*l>13 or k>3 or l>3:
                    continue
                p,q=17-r*k,13-r*l
                require(p>0 and q>=0,'endpoint rank budget')
                upper_endpoint=[0,0] if q==0 else [1,min(r-1,q)]
                record={'r':r,'k':k,'l':l,'lower_endpoint_rank':p,'upper_endpoint_codimension':q,
                        'lower_endpoint_SF_rank_range':[1,min(r-1,p)],
                        'upper_endpoint_SF_rank_range':upper_endpoint,
                        'integer_degree_witness':degree_witness(r,k,l,2)}
                profiles.append(record);current.append(record)
                for source,data in sources.items():
                    if l<=data['forward_bound']:
                        refined.append({'source':source,'r':r,'k':k,'l':l,
                            'integer_degree_witness':degree_witness(r,k,l,data['top_negative_degree'])})
        require(len(current)==[9,6,4,2,2,1,1,1,1,1][r-4],'rank row size')
        rows.append({'r':r,'k_max':min(3,17//r),'l_max':min(3,13//r),
                     'l_max_D_P_V':min(2,13//r),'coarse_bins':len(current),
                     'positive_square_rank':24+r,'positive_square_kernel_dimension':17-r,
                     'positive_square_cokernel_dimension':13-r,
                     'status':'auxiliary-surjectivity-success-if-attained' if r==13 else 'unresolved-bad-rank'})
    require(len(profiles)==28 and sum(p['r']<13 for p in profiles)==27,'coarse counts')
    require(len(refined)==103 and sum(p['r']<13 for p in refined)==99,'source-refined counts')
    require({(p['r'],p['k'],p['l']) for p in profiles if p['upper_endpoint_codimension']==0}=={(13,1,1)},'ambient endpoint classification')
    require(all(p['source']=='Z' and p['r']==4 for p in refined if p['l']==3),'length-three forward source restriction')
    require([p for p in profiles if p['r']==13][0]['k']==1,'successful rank profile')
    return {'certificate':'universal finite necessary-profile bounds only',
            'lower_rank_bound':{'value':4,'status':'separate theorem assumed, not proved here'},
            'geometric_realization_asserted':False,'actual_rank_computed':False,
            'full_adjoint_success_asserted':False,'original_repair_asserted':False,
            'rank_strata':10,'unresolved_bad_rank_strata':9,
            'coarse_profile_upper_bins':28,'bad_coarse_profile_upper_bins':27,
            'source_refined_upper_bins':103,'bad_source_refined_upper_bins':99,
            'characters':characters,'sources':sources,'rows':rows,
            'profiles':profiles,'source_refined_profiles':refined}

def main():
    result=derive()
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
