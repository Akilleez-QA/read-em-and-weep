"""Pin proof bytes and construct tiny owner/face examples; no HM arithmetic."""
import hashlib
import json
from pathlib import Path
import subprocess
import lift as L
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent
def write(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def sha(raw):return hashlib.sha256(raw).hexdigest()

def main():
    rev='e011d7c2e0b79f1b885e001c9b0e39b97618a424';old='08b73637d4136f91606aad332c46cafd064417f8';null='10810ee877fdaf291399198ad60d7dd0c316a42d'
    items=[('43193bc8badf3f29a1363132135d956cc12d46ad','research/hm/null-source-integration/scalar-family-transport/PROOF.md'),
        (null,'research/hm/null-proof-foundations/refined-tracefree-pole-domain.md'),
        (null,'research/hm/null-proof-foundations/hm-regular-cover-transport.md'),
        (null,'research/hm/null-source-integration/combined-pole/PROOF.md'),
        (old,'research/hm/current-scalar-proof/map-and-comparison.md'),
        (old,'research/hm/current-scalar-geometric-dependencies/source-identity.md'),
        (old,'research/hm/current-scalar-residual-attribution/first-order-source.md'),
        (old,'research/hm/current-scalar-geometric-dependencies/frames-and-poles.md'),
        (rev,'research/codex-swarm/physical-homogenization/PROOF.md'),
        (rev,'research/codex-swarm/physical-homogenization/frames.py'),
        (rev,'research/codex-swarm/physical-homogenization/review-independent.md'),
        (rev,'research/codex-swarm/source-domain-application/PROOF.md'),
        (rev,'research/codex-swarm/source-domain-application/review-independent.md')]
    pins=[]
    for commit,path in items:
        ref=commit+':'+path;raw=subprocess.check_output(['git','show',ref],cwd=ROOT)
        blob=subprocess.check_output(['git','rev-parse',ref],cwd=ROOT,text=True).strip()
        pins.append({'commit':commit,'path':path,'git_blob':blob,'sha256':sha(raw),'bytes':len(raw)})
    workspace=[]
    for name in('full-source-application/r_binding.py','full-source-application/PROOF.md',
        'full-source-application/source-pins.json','full-source-application/formal_identities.py',
        'full-source-application/producer-ready.json','transport-binding/transport_binding.py',
        'transport-binding/lift_schema.py','transport-binding/source-pins.json','inserted-coefficients/interfaces.py'):
        p=BASE/name;raw=p.read_bytes();workspace.append({'path':str(p.relative_to(ROOT)),
            'sha256':sha(raw),'bytes':len(raw),'scope':'canonical definition/proof snapshot; independent review external, not admission capability'})
    write('source-pins.json',{'schema':'JC01-source-pins-v1','immutable_dependencies':pins,
        'canonical_workspace_dependencies':workspace,'actual_coefficients_evaluated':False})
    owners=tuple(L.I.FullOwner(12,('toy-outer',j),c,0,t)for j,(c,t)in enumerate(zip((5,0,1,2,3,4),(0,1,3,7,11,15))))
    write('face-program-example.json',L.lift_terms(2,owners[:5]))
    seventh=owners+(L.I.FullOwner(12,'seventh-toy-owner',4,1,15),)
    write('lift-contract.json',{'schema':'JC01-lift-domain-contract-v1','source_constructor':'full-source-application/r_binding.py:ActualFullSourceApplication(repo).describe',
        'claim_scope':'coefficient-free theorem for the same actual definitions; conditional on explicit RS actual closure/homogeneity and pinned primitive premises, independent implementation acceptance external',
        'recurrences':['J0=I Rsharp^transpose P','J1=H_0 delta J0','J2=-H_-1 delta J1','J3=H_-2 delta J2'],
        'closure':['d J0=0','delta J0-d J1=0','delta J1+d J2=0','delta J2-d J3=0','delta J3=0'],
        'top_closure_reason':'d_End injective in internal degree-3 because H0 gamma=1; universal7-owner equation, not a6-owner source DAG assertion',
        'frames':[L.original_frame(s)for s in range(4)],'ledger':L.domain_ledger(),
        'outer_J2_indices_example':L.outer_owner_contract(owners[:5],2,[o.standard_tag for o in owners[:5]]),
        'outer_delta_J3_seven_owner_indices_example':L.outer_boundary_contract(seventh,3,[o.standard_tag for o in seventh]),
        'whole_standard_extension':'actual homogeneous whole source/combined derivative identity + owned pole theorem -> clear all codimension1 poles on normal smoothY; multiply exact matching outer quotient, leave original-tag standard equations as units',
        'all20_maps_same_domain':True,'all32_tests_same_domain':True,'J3_is_mandatory_closure_witness':True,
        'generic_ledger_or_string_is_not_actual_clearing_evidence':True,
        'historical_order_identity':False,'actual_fibers_enumerated':False,'physical_coefficients_evaluated':False,
        'physical_execution_authorized':False,'arithmetic_resource_schedule_accepted':False,'obstruction_decided':False,
        'separate_remaining_work':['independent canonical RS/JC implementation review','complete actual coefficient/provider realization',
            'global arithmetic/storage schedule and execution release','32 weighted values and authenticated obstruction conclusion']})

if __name__=='__main__':main()
