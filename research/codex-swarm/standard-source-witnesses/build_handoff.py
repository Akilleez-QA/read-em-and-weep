"""Regenerate proposal/schema/pins/gap records. Reads proof bytes, no HM eval."""
import hashlib
import json
from pathlib import Path
import subprocess
import witnesses as W

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def write(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def digest(data):return hashlib.sha256(data).hexdigest()

def main():
    owners=tuple(W.I.FullOwner(12,('artificial-template',j),c,m,t)for j,(c,m,t)in enumerate(zip((5,0,4),(0,3,15),(0,8,12))))
    template=W.proposal(owners,(0,1));W.validate_proposal(template);write('witness-template.json',template)
    integer={'type':'integer'}
    owner={'type':'array','minItems':5,'maxItems':5,'prefixItems':[
        {'type':'integer','minimum':0},{'$ref':'#/$defs/occurrence'},
        {'type':'integer','minimum':0,'maximum':5},
        {'type':'integer','minimum':0,'maximum':15},{'type':'integer','minimum':0,'maximum':15}]}
    vector={'type':'array','minItems':4,'maxItems':4,'items':{'type':'integer','minimum':0}}
    proof={'oneOf':[{'type':'object','additionalProperties':False,'required':['status','candidate_proof_sha256'],
        'properties':{'status':{'const':'unbound'},'candidate_proof_sha256':{'type':'null'}}},
        {'type':'object','additionalProperties':False,'required':['status','candidate_proof_sha256'],
        'properties':{'status':{'const':'candidate'},'candidate_proof_sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'}}}]}
    props={key:{'const':value}for key,value in template.items()if type(value)in(str,bool)}
    props.update({'owners':{'type':'array','minItems':3,'maxItems':3,'items':owner},
        'source_sorted_owners':{'type':'array','minItems':3,'maxItems':3,'items':owner},
        'target_standard_tags':{'type':'array','minItems':3,'maxItems':3,'items':{'type':'integer','minimum':0,'maximum':15}},
        'pair':{'enum':[[0,1],[2,3]]},'source_sorting_sign':{'type':'integer','enum':[-1,1]},
        'numerator_degree':vector,'divisor_degrees':{'type':'array','minItems':3,'maxItems':3,'items':vector},
        'obligations':{'type':'object','additionalProperties':False,'required':list(W.OBLIGATIONS),
            'properties':{key:proof for key in W.OBLIGATIONS}}})
    write('witness-schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema',
        'title':'Unbound whole-standard actual-source witness proposal','type':'object','additionalProperties':False,
        'required':list(template),'properties':props,'$defs':{'occurrence':{'anyOf':[integer,{'type':'string'},
            {'type':'array','items':{'$ref':'#/$defs/occurrence'}}]}},
        '$comment':'Cross-field degrees/source sorting/owners require witnesses.validate_proposal. No proof/admission validation is performed.'})
    entries=[('10810ee877fdaf291399198ad60d7dd0c316a42d','research/hm/null-proof-foundations/hm-transition-only-first-lift-alternative.md'),
        ('10810ee877fdaf291399198ad60d7dd0c316a42d','research/hm/null-source-integration/combined-pole/PROOF.md'),
        ('10810ee877fdaf291399198ad60d7dd0c316a42d','research/hm/null-proof-foundations/hm-regular-cover-transport.md'),
        ('08b73637d4136f91606aad332c46cafd064417f8','research/hm/current-scalar-residual-attribution/first-order-source.md'),
        ('82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc','research/codex-swarm/whole-source-clearing/PROOF.md'),
        ('02d0e727ffb95dfd9281906cc284c56e8bffd018','research/hm/null-source-integration/complementary-pair/PROOF.md'),
        ('43193bc8badf3f29a1363132135d956cc12d46ad','research/hm/null-source-integration/scalar-family-transport/PROOF.md')]
    pins=[]
    for commit,path in entries:
        ref=commit+':'+path
        data=subprocess.check_output(['git','show',ref],cwd=ROOT)
        blob=subprocess.check_output(['git','rev-parse',ref],cwd=ROOT,text=True).strip()
        pins.append({'commit':commit,'path':path,'git_blob':blob,'sha256':digest(data),'bytes':len(data)})
    workspace=[]
    for name,status in [('physical-homogenization/PROOF.md','physical theorem premise, independent acceptance external'),
        ('inserted-coefficients/interfaces.py','shared interface identity')]:
        path=HERE.parent/name;data=path.read_bytes()
        workspace.append({'path':str(path.relative_to(ROOT)),'sha256':digest(data),'bytes':len(data),'status':status})
    write('source-pins.json',{'schema':'standard-source-witnesses-pins-v1','repository':'https://github.com/Akilleez-QA/read-em-and-weep',
        'immutable_proof_dependencies':pins,'workspace_dependencies':workspace,'physical_source_evaluated':False})
    write('gap-registry.json',{'schema':'standard-source-binding-gap-v1','owner':'next source-interface identity/domain integrator',
        'math_available':['conditional whole-standard extension from actual homogeneous P and local regular Qhat',
            'existing source-specific P S Pi F=0 and delta T F=F, without new harmonic evaluation'],
        'required_deliverable':{'P':'bind emitted complete P oracle to actual reviewed b-tr(C)/2 with exact owned homogeneous degrees',
            'Qhat':'bind factor oracle to fixed N14 polynomial quotients, one divisor frame conversion, original owner tags',
            'primitive':'bind same fresh source/gerbe/frame and admissible old scalar to pinned delta s_old=F, then apply chain maps',
            'review':'reviewed identity/domain composition, not metadata assertions or coefficient tables'},
        'separate_outer_obligations':['whole Rsharp/J0..J3 source identity and closure','full54/29/5251 standard/prism/restriction domain',
            'coefficient resource schedule and independent execution release','detector values and final obstruction decision'],
        'source_faithful_oracle_identity_accepted':False,'physical_execution_authorized':False,
        'actual_source_evaluated':False,'harmonic_scalar_recomputation_required':False})

if __name__=='__main__':main()
