"""Build FD proof pin/descriptor records from text and toy owner metadata only."""
import hashlib
import json
from pathlib import Path
import subprocess
import domain as D
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent

def write(name,data):(HERE/name).write_text(json.dumps(data,indent=2)+'\n')
def sha(data):return hashlib.sha256(data).hexdigest()

def main():
    rev='7d73d540981a3a152d807c39844ec63bc9913b89';old='08b73637d4136f91606aad332c46cafd064417f8';null='10810ee877fdaf291399198ad60d7dd0c316a42d'
    items=[(rev,'research/codex-swarm/standard-source-witnesses/PROOF.md'),
        (rev,'research/codex-swarm/standard-source-witnesses/review-independent.md'),
        (rev,'research/codex-swarm/physical-homogenization/PROOF.md'),
        (rev,'research/codex-swarm/physical-homogenization/review-independent.md'),
        (rev,'research/codex-swarm/whole-source-clearing/PROOF.md'),
        (old,'research/hm/current-scalar-residual-attribution/first-order-source.md'),
        (old,'research/hm/current-scalar-geometric-dependencies/frames-and-poles.md'),
        (null,'research/hm/null-proof-foundations/hm-transition-only-first-lift-alternative.md'),
        (null,'research/hm/null-source-integration/combined-pole/PROOF.md'),
        (null,'research/hm/null-proof-foundations/hm-regular-cover-transport.md'),
        (null,'research/hm/null-proof-foundations/transposed-scalar-demand-grammar.md'),
        ('02d0e727ffb95dfd9281906cc284c56e8bffd018','research/hm/null-source-integration/complementary-pair/PROOF.md'),
        ('5ac24746a9f27356b0ca148e0531e1588e1390a2','research/hm/null-source-integration/standard-source-review/REVIEW.md')]
    pins=[]
    for commit,path in items:
        ref=commit+':'+path;raw=subprocess.check_output(['git','show',ref],cwd=ROOT)
        blob=subprocess.check_output(['git','rev-parse',ref],cwd=ROOT,text=True).strip()
        pins.append({'commit':commit,'path':path,'git_blob':blob,'sha256':sha(raw),'bytes':len(raw)})
    workspace=[]
    for path in('source-faithful-P/p_binding.py','source-faithful-P/source-pins.json',
        'source-faithful-Q/q_binding.py','source-faithful-Q/source-pins.json','inserted-coefficients/interfaces.py'):
        f=BASE/path
        workspace.append({'path':str(f.relative_to(ROOT)),'sha256':sha(f.read_bytes())if f.is_file()else None,
            'scope':'definition implementation snapshot; independent acceptance external; never an admission token'})
    write('source-pins.json',{'schema':'FD01-source-pins-v1','PR86_baseline':rev,'immutable_dependencies':pins,
        'canonical_definition_workspace_inputs':workspace,'physical_source_evaluated':False})
    descriptor=D.FullFiberDomain(12,('descriptor-only','Pi-slot',0),0).descriptor()
    write('fiber-descriptor.json',descriptor)
    toy=tuple(D.I.FullOwner(12,('toy-contract-slot',j),c,m,t)for j,(c,m,t)in enumerate(zip((5,0,4),(0,3,15),(0,8,12))))
    contract=D.extension_contract(toy,(0,1))
    contract.update({'instance_scope':'illustrative supplied owner metadata; not an actual fiber expansion',
        'actual_definition_interface':{'P':'source-faithful-P/p_binding.py:ActualPBinding(repo).describe(ordered_owners,pair)',
            'Q':'source-faithful-Q/q_binding.py:ActualQBinding(repo).describe(owner,pair)'},
        'fresh_raw_primitive_theorem':'delta s_fresh=b-tr(C)/2, by universal raw transgression restricted to new increasing tuples, then alternating extension',
        'primitive_domain':'same formula-local carrier14/legal1 source theorem covers s_fresh, F_fresh, restrictions and delta',
        'harmonic_conclusion':'P_H S Pi F_fresh=0; no coefficient recomputation required',
        'historical_nonlinear_source_order_identity':False,
        'implementation_review_status':'P/Q acceptance is external and pending until independently recorded; no self-certification here',
        'physical_coefficients_always_refuse':True,
        'separate_outer_obligations':['complete Rsharp/J0..J3 identity and closure','whole54/29/5251 prism/restriction domain',
            'complete actual source coefficient provider integration','global cost/memory schedule','detector values and global obstruction decision']})
    write('application-contract.json',contract)

if __name__=='__main__':main()
