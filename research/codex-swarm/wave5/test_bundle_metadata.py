"""Root integration: explicitly supplied owners and AST metadata, no coefficients."""
import json,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'source-domain-application'))
import domain as D

class BundleMetadata(unittest.TestCase):
 def test_canonical_actual_definitions_join_without_coefficient_calls(self):
  O=D.I.FullOwner
  owners=(O(12,('slot',1),1,5,8),O(12,('slot',0),5,1,0),O(12,('slot',2),4,10,15))
  app=D.ActualDomainApplication()
  for pair in((0,1),(2,3)):
   c=app.describe(owners,pair)
   self.assertTrue(c['definition_metadata_crosschecked']);self.assertEqual(c['source_sorting_sign'],-1)
   self.assertEqual(c['target_standard_tags'],[8,0,15])
   self.assertEqual(c['whole_P_exact_homogeneous_degree'],tuple(c['P_definition']['P_homogeneous_multidegree']))
   self.assertEqual([x['owner']for x in c['Q_definitions']],[o.data()for o in owners])
   self.assertEqual([x['cardinality']['value']for x in c['fiber_domains']],[96]*3)
   self.assertTrue(all(not x['actual_owners_enumerated']for x in c['fiber_domains']))
   profile=c['metadata_profile'];arrays=[]
   def walk(x):
    if isinstance(x,dict):
     for k,v in x.items():
      if k in('dag','nodes')and isinstance(v,list):arrays.append(len(v))
      walk(v)
    elif isinstance(x,(list,tuple)):
     for y in x:walk(y)
   payload={k:v for k,v in c.items()if k!='metadata_profile'};walk(payload)
   self.assertEqual(len(arrays),10)
   self.assertEqual(profile['aggregate_stored_AST_nodes'],sum(arrays))
   self.assertEqual(profile['serialized_payload_bytes'],len(json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode()))
   self.assertFalse(profile['aggregate_resource_supervisor_present'])
   self.assertFalse(profile['physical_coefficient_memory_or_cost_admission'])
   self.assertFalse(c['historical_source_order_equality'])
   for method in(app.coefficient,app.factor_terms,app.owners):
    with self.assertRaises(D.I.PhysicalAdmissionMissing):method(object(),mode='synthetic')

if __name__=='__main__':unittest.main()
