"""Reproduce explicit-owner definition AST metadata, never source coefficients."""
import sys,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
sys.path.insert(0,str(BASE/'source-domain-application'))
import domain as D

def main():
 O=D.I.FullOwner
 owners=(O(12,('slot',1),1,5,8),O(12,('slot',0),5,1,0),O(12,('slot',2),4,10,15))
 app=D.ActualDomainApplication();rows=[]
 for pair in((0,1),(2,3)):
  d=app.describe(owners,pair)
  rows.append({'pair':pair,'exact_P_degree':d['whole_P_exact_homogeneous_degree'],'sorting_sign':d['source_sorting_sign'],'metadata_profile':d['metadata_profile']})
 paths=('source-faithful-P/p_binding.py','source-faithful-Q/q_binding.py','source-domain-application/domain.py')
 out={'schema':'canonical-bundle-AST-metadata-only-v1','explicit_owners':[o.data()for o in owners],
  'physical_source_evaluated':False,'actual_fibers_enumerated':False,'physical_memory_or_cost_admitted':False,
  'rows':rows,'implementation_sha256':{n:hashlib.sha256((BASE/n).read_bytes()).hexdigest()for n in paths}}
 (HERE/'bundle-metadata-receipt.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('AST metadata only:',[(r['pair'],r['metadata_profile']['aggregate_stored_AST_nodes'],r['metadata_profile']['serialized_payload_bytes'])for r in rows])
if __name__=='__main__':main()
