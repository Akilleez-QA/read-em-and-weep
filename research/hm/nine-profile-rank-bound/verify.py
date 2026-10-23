#!/usr/bin/env python3
"""Finite implication contract only; imported geometric theorems are assumptions."""
import copy
import hashlib
import itertools
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_SHA = 'b1f376130b3f6fe84e6d8e723b99751b90823c14604de4063e94b7b27b6c2cbc'
REGISTRY_SHA = '6aed378989ec3a929feb8b0d798c047111a9ac0c2e0d3a1087ad83dc565107c6'
GEOMETRY = dict(actual=True,ambient_dimension=30,coefficient_dimension=54,rank_E=17,degree_E=-54,rank_Qdual=13,degree_Qdual=-54,physical_parameter='one_fixed_determinant_identification',independent_rotation=False,horizontal_birkhoff=False,actual_images_retained=True,inherited_necessity_assumed=True,conditional_on_pinned_inputs=True)
PLATEAU = dict(source='ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md',maximal=True,ordered=True,k_range=[1,2,3],l_range=[1,2,3],cubic_sections_E=True,cubic_sections_Qdual=True,saturated_sheaf_kernels=True,endpoint_rank_at_most=2)
C22 = dict(necessity_chain_retained=True,original_positive_defect_retained=True,second_dual_defect12_retained=True,endpoint_rank3_assumed=False)
C31 = dict(cubic_ranks=[1,2,3],rank2_quotients=[[4,2],[6,2],[8,2],[6,4],[8,4]],last_rank2_sectors=['single11','doubled9'],rank1_degrees=[9,11],last_e9_shapes=['two_O4','O4_plus_O6','W_O5'],endpoint_rank3_assumed=False)
BRIDGE = dict(source='POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md',source_dimension=41,middle_dimension=54,target_dimension=37,first_map_injective=True,second_map_surjective=True,map_identity='actual_Koszul_derivative',rank_offset=24)
KEYS = {'schema','geometry','plateau','lower_exclusions','profiles','four_sources','branches32','coverage22','coverage31','bridge','claim','lower_support'}

class Rejected(ValueError):
    pass

def need(condition, reason):
    if not condition:
        raise Rejected(reason)

def same(a,b,reason):
    # Distinguishes booleans from integers, unlike Python's ordinary equality.
    need(json.dumps(a,sort_keys=True)==json.dumps(b,sort_keys=True),reason)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def authenticate(records, loader):
    seen=set()
    for r in records:
        need(set(r)=={'file','ref','path','url','bytes','sha256','git_blob_sha1'},'manifest schema')
        need(r['file'] not in seen,'duplicate input')
        seen.add(r['file'])
        need(r['file'].startswith('inputs/') and '..' not in r['file'].split('/'),'unsafe input')
        need(re.fullmatch('[0-9a-f]{40}',r['ref']) is not None,'immutable commit missing')
        same(r['url'],'https://github.com/Akilleez-QA/read-em-and-weep/blob/'+r['ref']+'/'+r['path'],'public source mismatch')
        data=loader(r['file'])
        need(type(r['bytes']) is int and len(data)==r['bytes'],'byte count mismatch')
        same(digest(data),r['sha256'],'SHA256 mismatch')
        blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        same(blob,r['git_blob_sha1'],'Git blob mismatch')
    return {r['file'].split('/',1)[1] for r in records}

def check(c,registry,available):
    need(set(c)==KEYS,'top-level schema')
    same(c['schema'],'actual-nine-profile-v1','schema version')
    same(c['geometry'],GEOMETRY,'actual geometry/premise contract')
    same(c['plateau'],PLATEAU,'actual maximal plateau contract')
    same(c['coverage22'],C22,'22 coverage/defect contract')
    same(c['coverage31'],C31,'31 complete image-rank branches')
    same(c['bridge'],BRIDGE,'actual square bridge')
    same(c['lower_exclusions'],registry['lower_rules'],'lower-rank exclusions missing')
    same(c['lower_support'],registry['lower_support'],'lower-rank necessity chain missing')
    same(c['four_sources'],registry['source_tuples'],'actual four-source alternatives')
    same(c['branches32'],registry['branches32'],'incomplete source32 branch cover')
    required=set(registry['lower_rules'].values())|set(registry['lower_support'])
    required.add(registry['plateau_source'])
    required.add(c['bridge']['source'])
    rows=c['profiles']
    need(type(rows) is list,'profile list')
    profile_rules={}
    for row in rows:
        need(type(row) is dict and set(row)=={'k','l','sources'},'profile schema')
        k,l=row['k'],row['l']
        need(type(k) is int and type(l) is int,'integer ordered lengths')
        pair=(k,l)
        need(pair not in profile_rules,'duplicate profile does not replace missing direction')
        label=str(k)+str(l)
        need(label in registry['profile_rules'],'unproved profile')
        same(row['sources'],registry['profile_rules'][label],'profile source chain mismatch')
        profile_rules[pair]=row['sources']
        required.update(row['sources'])
    universe=set(itertools.product(c['plateau']['k_range'],c['plateau']['l_range']))
    need(set(profile_rules)==universe,'not every ordered plateau excluded')
    need(required<=available,'required proof input missing')

    # Check the four source types against the original *given* splitting equations.
    # This does not regenerate the historical classification.
    source_shapes={}
    for name,t in c['four_sources'].items():
        need(len(t)==8 and all(type(x) is int and x>=0 for x in t),'nonnegative source tuple')
        a,b,cc,d,e,f,g,h=t
        need(a+d+g+h==1 and b+cc+d+e+f+2*g+h==3 and cc+g+h>=1,'source equations')
        need(a>=1 and b>=1,'canonical primary terminal missing')
        r2=3*(cc+g+h-1)+4*(d+e+g+h)+5*(f+g)
        blocks=[(2,r2),(3,2*a+6*b),(4,3*cc+4*d),(5,2*e),(8,f),(9,2*g),(10,h)]
        rank=sum(mult for _,mult in blocks)
        degree=-sum(twist*mult for twist,mult in blocks)
        need((rank,degree)==(17,-54),'source rank degree')
        source_shapes[name]={'rank':rank,'degree':degree,'quadratic_dimension':r2}
    need(len({tuple(t) for t in c['four_sources'].values()})==4,'duplicate source')

    # Logical elimination of generic rank0,1,2 separately from the rank3 profile cover.
    eliminated={int(x) for x in c['lower_exclusions']}
    need(eliminated=={0,1,2},'lower-bound gap')
    if set(profile_rules)==universe and len(universe)==9:
        eliminated.add(3)
    ranks=[r for r in range(min(GEOMETRY['rank_E'],GEOMETRY['rank_Qdual'])+1) if r not in eliminated]
    need(ranks and min(ranks)==4,'generic rank inference')
    r=min(ranks)
    source,middle,target=[c['bridge'][k] for k in ('source_dimension','middle_dimension','target_dimension')]
    kernel_B=middle-target
    coker_A=middle-source
    need(kernel_B==GEOMETRY['rank_E'] and coker_A==GEOMETRY['rank_Qdual'],'kernel quotient ranks')
    offset=source-kernel_B
    need(offset==target-coker_A==c['bridge']['rank_offset'],'exact sequence rank offset')
    square=offset+r
    claim=dict(generic_SF_rank_lower=r,generic_square_rank_lower=square,kernel_upper=source-square,positive_double_hyperplane_sections_upper=GEOMETRY['rank_E']-r,cokernel_upper=target-square,generic_only=True,proof_assistant_verified=False,full_adjoint=False,original_repair=False,surjective=False,cone_rank36_improved=False)
    same(c['claim'],claim,'unsupported conclusion')
    return {'allowed_generic_SF_ranks':ranks,'profile_count':len(universe),'source_shapes':source_shapes,'consequences':claim,'required_mathematical_source_count':len(required)}

def altered_values(value,path=()):
    if isinstance(value,dict):
        for key,item in value.items():
            yield path+('DROP_KEY',key),None
            yield from altered_values(item,path+(key,))
    elif isinstance(value,list):
        for idx,item in enumerate(value):
            yield path+('DROP_INDEX',idx),None
            yield from altered_values(item,path+(idx,))
    elif type(value) is bool:
        yield path,not value
    elif type(value) is int:
        yield path,value+1
        yield path,bool(value)
    elif type(value) is str:
        yield path,value+'_MUTATED'
    else:
        raise Rejected('unsupported certificate leaf')

def mutate(base,path,value):
    result=copy.deepcopy(base)
    if len(path)>=2 and path[-2] in ('DROP_KEY','DROP_INDEX'):
        parent=result
        for key in path[:-2]: parent=parent[key]
        del parent[path[-1]]
    else:
        parent=result
        for key in path[:-1]: parent=parent[key]
        parent[path[-1]]=value
    return result

def rejection(call, label):
    try:
        call()
    except (Rejected,KeyError,TypeError,IndexError):
        return
    raise Rejected('mutation accepted: '+label)

def main():
    manifest_bytes=(ROOT/'INPUTS.json').read_bytes()
    registry_bytes=(ROOT/'REGISTRY.json').read_bytes()
    same(digest(manifest_bytes),MANIFEST_SHA,'frozen input manifest')
    same(digest(registry_bytes),REGISTRY_SHA,'frozen theorem-scope registry')
    records=json.loads(manifest_bytes); registry=json.loads(registry_bytes)
    available=authenticate(records,lambda name:(ROOT/name).read_bytes())
    c=json.loads((ROOT/'COVERAGE.json').read_text())
    result=check(c,registry,available)
    tested=0
    for path,value in altered_values(c):
        m=mutate(c,path,value)
        rejection(lambda:check(m,registry,available),str(path))
        tested+=1
    for r in records:
        name=r['file']; original=(ROOT/name).read_bytes()
        rejection(lambda:authenticate([r],lambda _:original+b'!'),'corrupt '+name);tested+=1
        m=copy.deepcopy(r);m['ref']='main'
        rejection(lambda:authenticate([m],lambda _:original),'mutable pin '+name);tested+=1
        required_names=set(sum(registry['profile_rules'].values(),[])+list(registry['lower_rules'].values())+registry['lower_support']+[registry['plateau_source']])
        if name.split('/',1)[1] in required_names:
            rejection(lambda:check(c,registry,available-{name.split('/',1)[1]}),'missing '+name)
            tested+=1
    # Controls preserve meaning while changing irrelevant traversal order.
    positive_controls=0
    for order in [list(reversed(c['profiles'])),c['profiles'][3:]+c['profiles'][:3]]:
        d=copy.deepcopy(c);d['profiles']=order
        same(check(d,registry,available),result,'order-independent inference');positive_controls+=1
    output={'status':'PASS','scope':'conditional finite implication contract, not geometric or proof-assistant verification','authenticated_input_count':len(records),'rejected_mutations':tested,'positive_order_controls':positive_controls,**result}
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=='__main__':
    main()
