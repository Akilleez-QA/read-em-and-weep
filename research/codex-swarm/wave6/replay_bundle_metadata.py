"""One explicit RS triple and JC six-owner J3 description; AST metadata only."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module);return module


def profile(value):
    arrays=[]
    def walk(v,path=''):
        if type(v)is dict:
            for k,a in v.items():
                if k in('dag','nodes')and type(a)is list:arrays.append({'path':path+'/'+k,'nodes':len(a)})
                walk(a,path+'/'+k)
        elif type(v)in(list,tuple):
            for j,a in enumerate(v):walk(a,path+'/'+str(j))
    walk(value)
    return {'stored_AST_arrays':arrays,'aggregate_stored_AST_nodes':sum(x['nodes']for x in arrays),
            'canonical_descriptor_bytes':len(json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False).encode()),
            'physical_arithmetic_cost_or_memory_admission':False}


def build_receipt():
    jc=load('wave6_canonical_JC',BASE/'full-lift-domain/lift.py')
    O=jc.I.FullOwner
    owners=tuple(O(12,('wave6-explicit',i),c,m,t)for i,(c,m,t)in enumerate(
        [(5,1,0),(0,2,1),(1,3,3),(2,7,7),(3,11,11),(4,15,15)]))
    # All six owners are explicit constructor inputs, never fiber enumeration.
    app=jc.ActualFullLiftApplication()
    rs=app.source_definition(owners[:3])
    lift=app.describe(3,owners)
    return {'schema':'wave6-canonical-AST-metadata-only-v1','explicit_owners':[o.data()for o in owners],
            'RS':{'schema':rs['schema'],'profile':profile(rs),'boundary_sign':rs['same_representative_identity']['boundary_sign'],
                  'source_component_ids':list(rs['SC_source_reference']['bound_triple_record']['component_roots']),
                  'source_graph_reference_nodes':rs['SC_source_reference']['node_count']},
            'JC':{'schema':lift['schema'],'profile':profile(lift),'producer_profile':lift['metadata_profile'],
                  'component':lift['lift_program']['component'],'face_terms':len(lift['lift_program']['terms']),
                  'source_leaf_bindings':len(lift['source_leaf_bindings']),'frame':lift['frame'],
                  'scalar_maps':len(lift['all20_scalar_maps']),'weighted_tests':len(lift['all32_weighted_tests'])},
            'implementation_sha256':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest()for p in
                [BASE/'full-source-application/r_binding.py',BASE/'full-lift-domain/lift.py']},
            'actual_source_coefficients_evaluated':False,'actual_fibers_enumerated':False,
            'physical_memory_or_cost_admitted':False,'execution_release':False}


def main():print(json.dumps(build_receipt(),indent=2,sort_keys=True))
if __name__=='__main__':main()
