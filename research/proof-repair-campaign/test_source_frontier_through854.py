from copy import deepcopy
import hashlib, unittest
import verify_source_frontier_through854 as v
class Through854Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_counts(self):
  a=v.build(*self.inputs);self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':591,'additional_removed_pairs':81,'remaining_necessary_pairs':510});self.assertEqual([r['actual_additional_pair_count'] for r in a['new_source_edge_exclusion_ledger']],[17,32,32])
 def test_no_labels_removed(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],5);self.assertEqual(a['profile_counts'],{'11':4,'12':0,'21':1});self.assertEqual(a['new_full_label_exclusions'],[]);self.assertTrue(all(r['remaining_source_pairs'] for r in a['records']))
 def test_remaining_label_counts(self):
  d={r['id']:r['remaining_source_pair_count'] for r in v.build(*self.inputs)['records']};self.assertEqual(d[v.LABELS[113]],68);self.assertEqual(d[v.LABELS[127]],288)
 def test_other_three_records_unchanged(self):
  old={r['id']:r for r in self.inputs[0]['records']}
  for r in v.build(*self.inputs)['records']:
   if r['id'] not in v.LABELS.values():self.assertEqual(r,old[r['id']])
 def test_old_conditional_not_recounted(self):self.assertEqual(v.build(*self.inputs)['prior_conditional_scope']['additional_cuts_from_old_conditional_branch'],0)
 def test_double_cut_rejected(self):
  with self.assertRaises(ValueError):v.intersect(self.inputs[0],self.inputs[1],v.RULES+[v.RULES[1]])
 def test_every_scope_case_required(self):
  for name,cases in v.COVERAGE.items():
   for case in cases:
    c=deepcopy(v.COVERAGE);c[name].remove(case)
    with self.subTest(name=name,case=case),self.assertRaises(ValueError):v.validate_coverage(c)
 def test_direct_summand_is_required(self):
  c=deepcopy(v.COVERAGE);c['scalar_line_obstruction'].remove('D0_plus_L_saturated_via_direct_summand')
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_full_external_zero_not_only_endpoint(self):
  c=deepcopy(v.COVERAGE);c['127_ff'].remove('full_external_derivative_zero')
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_euler_extra_channel_retained(self):
  c=deepcopy(v.COVERAGE);c['127_fg'].remove('Euler_kernel_Ominus10_channel_retained_not_assumed_zero')
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_prior_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-through850.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_full_blocks_required(self):
  s,c,p=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==v.TUPLES['fg']);e['blocks'].pop()
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_local_ids_not_used_as_identity(self):
  s,c,p=deepcopy(self.inputs);mapping={e['id']:e['id']*37+10000 for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,p)['pair_accounting']['remaining_necessary_pairs'],510)
 def test_pair_duplicates_rejected(self):
  s,c,p=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.LABELS[113]);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_856_deferred_and_boundaries(self):
  a=v.build(*self.inputs);self.assertEqual(a['deferred'][0]['pr'],856);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['source2_closed'])
if __name__=='__main__':unittest.main()
