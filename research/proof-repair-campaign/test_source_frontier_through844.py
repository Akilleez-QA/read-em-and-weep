from copy import deepcopy
import hashlib, unittest
import verify_source_frontier_through844 as v
class Through844Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_counts(self):
  a=v.build(*self.inputs);self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':759,'bf_removed':19,'bc_removed':19,'additional_removed_pairs':38,'remaining_necessary_pairs':721})
 def test_gate_stays_closed(self):
  a=v.build(*self.inputs);self.assertEqual(a['registered_label_count'],8);self.assertEqual(a['registered_profile_counts'],{'11':7,'12':0,'21':1});self.assertEqual(a['nonempty_relation_label_count'],7);self.assertEqual(a['empty_relation_ids'],[v.SPLIT]);self.assertEqual(a['new_adjudicated_full_label_exclusions'],[]);self.assertEqual(a['whole_label_gate']['status'],'held_closed');self.assertFalse(a['whole_label_gate']['immutable_full_exhaustion_publication_verified'])
 def test_prior_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-through842.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_other_seven_records_unchanged(self):
  a=v.build(*self.inputs);old={r['id']:r for r in self.inputs[0]['records']}
  for r in a['records']:
   if r['id']!=v.SPLIT:self.assertEqual(r,old[r['id']])
 def test_double_cut_rejected(self):
  with self.assertRaises(ValueError):v.intersect(self.inputs[0],self.inputs[1],('bf','bc','bf'))
 def test_each_branch_required(self):
  for source,cases in v.COVERAGE.items():
   for case in cases:
    c=deepcopy(v.COVERAGE);del c[source][case]
    with self.subTest(source=source,case=case),self.assertRaises(ValueError):v.validate_coverage(c)
 def test_pr830_not_whole_source_alone(self):
  c=deepcopy(v.COVERAGE);del c['bf']['rank_one']
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_split_specific_d_not_omitted(self):
  c=deepcopy(v.COVERAGE);del c['descent']['terminal_d']
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_multiset_not_id_matching(self):
  s,c,p=deepcopy(self.inputs);mapping={e['id']:1000+e['id']*19 for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  a=v.build(s,c,p);self.assertEqual([r['actual_additional_pair_count'] for r in a['new_source_edge_exclusion_ledger']],[19,19])
 def test_wrong_source_blocks_rejected(self):
  s,c,p=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==v.SOURCES['bf']['coefficients']);e['blocks'].pop()
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_pair_duplication_rejected(self):
  s,c,p=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.SPLIT);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_845_not_encoded_as_cut(self):
  a=v.build(*self.inputs);self.assertEqual(a['deferred'][0]['pr'],845);self.assertEqual(a['deferred'][0]['kind'],'necessary_forms_not_exclusion');self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['formal_lean_proof'])
if __name__=='__main__':unittest.main()
