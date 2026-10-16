"""Exhaustive legal-label-only support certificate for one fixed carrier sector.

Never expands/evaluates physical polynomials or enumerates composition summands.
"""
from pathlib import Path
from itertools import product
import hashlib,json
import lower_legal_mask_sector as lowering
from preflight_selected_coefficient_support import Support,PIN,COMPILER,literal_unit_sum
ROOT=Path(__file__).parent
STANDARDS=(3,11,15)
KAPPA=(-1,-2,-2,-2)
CHAR=(0,0,-2,-2)

def active_masks(tag):
    bits=lowering.owned.decode_standard_tag(tag)
    return tuple(m for m in range(16) if all(not ((m>>i)&1) or bits[i] for i in range(4)))

def check_tuple(masks):
    a=lowering.build(masks);s=Support(a['dag'])
    degrees=[[5320+(3 if (m>>i)&1 else 1) for i in range(4)] for m in masks]
    result=[]
    for t in a['terms']:
        M=[CHAR[i]+sum(degrees[o][i] for o in t['edge']) for i in range(4)]
        for kind in ('A','B'):
            shift=[int(kind=='B' and i==t['coordinate']) for i in range(4)]
            root=t[kind]['root'];w=(1,0,1,1) if t['edge']==(1,2) else (0,-1,0,1)
            dirs=[w]+[x for x in product((-1,0,1),repeat=4) if any(x) and x!=w]
            cert=None
            for w in dirs:
                b=s.bound(root,w)
                if b is None:
                    cert={'literal_zero':True};break
                target=sum(w[i]*(KAPPA[i]+shift[i]) for i in range(4))
                low=sum(w[i]*(shift[i] if w[i]>=0 else M[i]) for i in range(4))
                high=sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))
                needed=(target-b[1],target-b[0])
                if high<needed[0] or low>needed[1]:
                    cert={'normal':w,'multiplier_bounds':b,'target_projection':target,'necessary_numerator_projection':needed,'full_numerator_projection':(low,high),'gap':max(needed[0]-high,low-needed[1])};break
            result.append({'edge':t['edge'],'kind':kind,'derivative':t['coordinate'] if kind=='B' else None,'root':root,'complete_numerator_degree':M,'certificate':cert,'status':'certified_zero' if cert else 'unresolved'})
    units=[literal_unit_sum(s,i) for i,n in enumerate(a['dag']) if n[0]=='bounded_composition_sum' and n[1]['dimension']==5]
    return {'legal_masks':masks,'owners':a['owners'],'vertex_degrees':degrees,'dag_sha256':hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'multipliers':result,'terminal_composition_unit_identities':units,'status':'certified_zero' if all(r['certificate'] for r in result) else 'unresolved'}

def build():
    metadata=json.loads((ROOT/'refined-detector-metadata.json').read_text())
    if metadata['seeds'][4]!={'coefficient':-2,'lift_depth':0,'orientation':1,'row':2,'standard':[3,11,15]}:raise ValueError('seed mismatch')
    if metadata['terminal_rows'][2]!={'cell':'CCBB','coefficient':-2,'entry':['M11',12,6],'exponent':[-1,-2,-2,-2],'q':2}:raise ValueError('terminal mismatch')
    if hashlib.sha256((ROOT/'selected-full-owner-kernel-lowering.json').read_bytes()).hexdigest()!=PIN:raise ValueError('original artifact changed')
    if hashlib.sha256((ROOT/'lower_selected_kernel_denominators.py').read_bytes()).hexdigest()!=COMPILER:raise ValueError('original compiler changed')
    domains=[active_masks(t) for t in STANDARDS]
    active=list(product(*domains));all_labels=list(product(range(16),repeat=3))
    inactive=[m for m in all_labels if m not in set(active)]
    rows=[check_tuple(m) for m in active]
    zero=sum(r['status']=='certified_zero' for r in rows)
    return {'schema':'fixed-carrier-legal-mask-support-v1','scope':{'seed':4,'row':2,'standard':STANDARDS,'carrier':(1,2,4),'terminal_target':KAPPA,'input_character':CHAR},'active_legal_domains':domains,'counts':{'full_legal_tuples':len(all_labels),'structurally_zero_inactive':len(inactive),'active_tuples':len(active),'support_certified_zero_active':zero,'unresolved_active':len(active)-zero,'active_multipliers':8*len(active),'certified_zero_multipliers':sum(x['status']=='certified_zero' for r in rows for x in r['multipliers'])},'inactive_proof':'At least one owner has a legal bit on a finite-standard coordinate. Its exact outer quotient returns literal zero, so every cancelled multiplier contains a zero factor. Inactive labels are retained in the full domain, not deleted from numerator columns.','active_results':rows,'support_semantics':'Cancellation-blind outer envelopes. Separation proves zero; overlap is unresolved and never proves nonzero.','full_degree_rule':'Each owner coordinate degree is 5250+14*5+(3 if legal_bit else 1), including finite-standard coordinates. Edge adds both owner degrees and input character. B domain additionally requires a_derivative>=1.','original_ast_sha256':PIN,'original_compiler_sha256':COMPILER,'held_limits':{'private_resource_configuration_omitted':True},'physical_polynomial_evaluation':False,'physical_polynomial_expansion':False,'physical_products_spent':0,'execution_release':False,'actual_factorization_accepted':False}
if __name__=='__main__':print(json.dumps(build(),sort_keys=True,indent=2))
