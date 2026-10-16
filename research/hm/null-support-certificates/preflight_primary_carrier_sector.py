"""Exhaustive legal-label-only support certificate for one fixed carrier sector.

Never expands/evaluates physical polynomials or enumerates composition summands.
"""
from pathlib import Path
from itertools import product
import hashlib,json
import lower_primary_carrier_sector as lowering
from preflight_selected_coefficient_support import Support,PIN,COMPILER,literal_unit_sum
ROOT=Path(__file__).parent
STANDARDS=(3,11,15)
KAPPA=(-1,-2,-2,-2)
CHAR=(0,0,-2,-2)

def active_masks(tag):
    bits=lowering.owned.decode_standard_tag(tag)
    return tuple(m for m in range(16) if all(not ((m>>i)&1) or bits[i] for i in range(4)))

def check_tuple(masks,carriers):
    a=lowering.build(masks,carriers);s=Support(a['dag'])
    degrees=[[5320+(3 if (m>>i)&1 else 1) for i in range(4)] for m in masks]
    result=[]
    for t in a['terms']:
        M=[CHAR[i]+sum(degrees[o][i] for o in t['edge']) for i in range(4)]
        for kind in ('A','B'):
            shift=[int(kind=='B' and i==t['coordinate']) for i in range(4)]
            root=t[kind]['root'];w=(1,0,1,1) if t['edge']==(1,2) else ((0,-1,1,1) if carriers==(1,3,4) else (0,-1,0,1))
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
    return {'carriers':carriers,'legal_masks':masks,'owners':a['owners'],'vertex_degrees':degrees,'dag_sha256':hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'multipliers':result,'terminal_composition_unit_identities':units,'status':'certified_zero' if all(r['certificate'] for r in result) else 'unresolved'}


def scan_new():
    from concurrent.futures import ProcessPoolExecutor
    import time
    jobs=[]
    for carriers in ((1,1,4),(1,3,4)):
        for masks in product(*(active_masks(t) for t in STANDARDS)):
            keys=list(zip(carriers,masks,STANDARDS))
            if keys==sorted(keys):jobs.append((masks,carriers))
    with ProcessPoolExecutor(max_workers=4) as pool:
        rows=[]
        for row in pool.map(run_job,jobs,chunksize=4):
            rows.append(row)
            if len(rows)%64==0:print('checked',len(rows),'unresolved',sum(r['status']=='unresolved' for r in rows),flush=True)
    result={'scope':'new primary carrier sectors(1,1,4),(1,3,4), seed4 row2 standards(3,11,15); all source-ordered active legal masks','results':rows,'counts':{'active_tuples':len(rows),'certified_zero':sum(r['status']=='certified_zero' for r in rows),'unresolved':sum(r['status']=='unresolved' for r in rows)},'support_semantics':'Separation proves zero; overlap remains unresolved, never nonzero.','physical_polynomial_evaluation':False,'physical_polynomial_expansion':False,'physical_products_spent':0,'execution_release':False,'actual_factorization_accepted':False,'held_limits':{'private_resource_configuration_omitted':True}}
    (ROOT/'primary-carrier-sector-support.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(result['counts'],flush=True)
def run_job(job):return check_tuple(*job)
if __name__=='__main__':scan_new()
