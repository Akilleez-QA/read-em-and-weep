from copy import deepcopy
import hashlib, unittest
import verify_frontier_through847 as v
class Through847Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_exact_counts(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],7);self.assertEqual(a['profile_counts'],{'11':6,'12':0,'21':1});self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':721,'additional_removed_pairs':0,'remaining_necessary_pairs':721})
 def test_only_split_label(self):
  a=v.build(*self.inputs);self.assertEqual([r['id'] for r in a['new_full_label_exclusion_ledger']],[v.SPLIT]);self.assertEqual(a['new_source_edge_exclusions'],[])
 def test_all_survivors_unchanged(self):
  old={r['id']:r for r in self.inputs[0]['records']}
  for r in v.build(*self.inputs)['records']:self.assertEqual(r,old[r['id']])
 def test_prior_gate_and_hash_preserved(self):
  self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through844.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256);self.assertEqual(self.inputs[0]['whole_label_gate']['status'],'held_closed')
 def test_complete_ten_in_original_order(self):self.assertEqual([r['source_name'] for r in v.build(*self.inputs)['original_ten_tuple_exhaustion']],['ff','ef','ee','cf','ce','cc','bf','be','bc','bb'])
 def test_missing_tuple_rejected(self):
  s,c,o,p,t=deepcopy(self.inputs);o['compatible_E_types'].pop()
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_duplicate_tuple_rejected(self):
  s,c,o,p,t=deepcopy(self.inputs);o['compatible_E_types'][0]=o['compatible_E_types'][1]
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_all_branch_parts_required(self):
  for name,branches in v.BRANCHES.items():
   for branch in branches:
    c=deepcopy(v.BRANCHES);c[name].remove(branch)
    with self.subTest(name=name,branch=branch),self.assertRaises(ValueError):v.validate_branches(c)
 def test_both_bb_lines_required(self):
  for branch in ['rank_one_O4_pr814','rank_one_O6_pr814']:
   c=deepcopy(v.BRANCHES);c['bb'].remove(branch)
   with self.assertRaises(ValueError):v.validate_branches(c)
 def test_no_double_label_cut(self):
  s,c,o,p,t=deepcopy(self.inputs);s['registered_ids'].append(v.SPLIT)
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_no_pair_recount(self):
  s,c,o,p,t=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.SPLIT);r['remaining_source_pairs']=[[1,2]]
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_full_blocks_not_tuple_alone(self):
  s,c,o,p,t=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==[0,0,0,0,2,0,0,1]);e['blocks'].remove([-2,'P'])
  with self.assertRaises(ValueError):v.build(s,c,o,p,t)
 def test_numbering_irrelevant(self):
  s,c,o,p,t=deepcopy(self.inputs)
  for e in c:e['id']+=9000;e['blocks'].reverse()
  c.reverse();a=v.build(s,c,o,p,t);b=v.build(*self.inputs)
  for x,y in zip(a['original_ten_tuple_exhaustion'],b['original_ten_tuple_exhaustion']):self.assertEqual(x['matched_local_E_id'],y['matched_local_E_id']+9000)
 def test_deferred_845_846_and_boundaries(self):
  a=v.build(*self.inputs);self.assertEqual([r['pr'] for r in a['deferred']],[845,846]);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['global_completion'])
if __name__=='__main__':unittest.main()
