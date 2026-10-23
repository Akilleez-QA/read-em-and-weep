from copy import deepcopy
import hashlib, unittest
import verify_frontier_through842 as v
class Through842Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_accounting(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],8);self.assertEqual(a['profile_counts'],{'11':7,'12':0,'21':1});self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':759,'additional_removed_pairs':0,'remaining_necessary_pairs':759})
 def test_exactly_one_label(self):
  a=v.build(*self.inputs);self.assertEqual([r['id'] for r in a['new_full_label_exclusion_ledger']],[v.BALANCED]);self.assertEqual(a['new_source_edge_exclusions'],[])
 def test_all_survivors_unchanged(self):
  a=v.build(*self.inputs);old={r['id']:r for r in self.inputs[0]['records']}
  for r in a['records']:self.assertEqual(r,old[r['id']])
 def test_prior_hash_and_gate_preserved(self):
  self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through839.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256);self.assertEqual(self.inputs[0]['whole_label_gate']['status'],'held_closed')
 def test_original_ten_not_seven(self):
  a=v.build(*self.inputs);self.assertEqual(len(a['original_ten_tuple_exhaustion']),10);self.assertEqual([r['source_name'] for r in a['original_ten_tuple_exhaustion']],['ff','ef','ee','cf','ce','cc','bf','be','bc','bb'])
 def test_missing_original_rejected(self):
  s,c,o,p,t=deepcopy(self.inputs);o['compatible_E_types'].pop()
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_duplicate_original_rejected(self):
  s,c,o,p,t=deepcopy(self.inputs);o['compatible_E_types'][0]=o['compatible_E_types'][1]
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_e_extra_P_not_optional(self):
  s,c,o,p,t=deepcopy(self.inputs)
  target=next(e for e in c if e['coefficients']==[0,0,0,0,2,0,0,1]);target['blocks'].remove([-2,'P'])
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_arbitrary_ids_not_mathematical_keys(self):
  s,c,o,p,t=deepcopy(self.inputs)
  for e in c:e['id']+=10000;e['blocks'].reverse()
  c.reverse();a=v.build(s,c,o,p,t);b=v.build(*self.inputs)
  for x,y in zip(a['original_ten_tuple_exhaustion'],b['original_ten_tuple_exhaustion']):self.assertEqual(x['matched_local_E_id'],y['matched_local_E_id']+10000)
 def test_each_branch_required(self):
  for name,branches in v.BRANCHES.items():
   for branch in branches:
    x=deepcopy(v.BRANCHES);x[name].remove(branch)
    with self.subTest(name=name,branch=branch),self.assertRaises(ValueError):v.validate_branches(x)
 def test_no_double_label(self):
  s,c,o,p,t=deepcopy(self.inputs);s['registered_ids'].append(v.BALANCED)
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_nonempty_label_not_silently_cut(self):
  s,c,o,p,t=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.BALANCED);r['remaining_source_pairs']=[[1,2]];r['remaining_source_pair_count']=1
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_boundaries_and_split_preserved(self):
  a=v.build(*self.inputs);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['realization_count']);self.assertEqual(a['split_residual'],self.inputs[0]['split_residual'])
 def test_proof_tuple_mutation_rejected(self):
  s,c,o,p,t=deepcopy(self.inputs);t=t.replace('ff = (0,0,0,0,0,2,0,1)','ff = (0,0,0,0,1,1,0,1)')
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
if __name__=='__main__':unittest.main()
