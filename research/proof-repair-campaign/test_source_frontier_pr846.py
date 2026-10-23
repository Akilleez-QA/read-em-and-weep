from copy import deepcopy
import hashlib, unittest
import verify_source_frontier_pr846 as v
class Pr846Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_exact_cuts(self):
  a=v.build(*self.inputs);self.assertEqual([r['actual_additional_pair_count'] for r in a['new_source_edge_exclusion_ledger']],[17,17,17,9,32,32]);self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':721,'additional_removed_pairs':124,'remaining_necessary_pairs':597})
 def test_no_label_cuts(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],7);self.assertEqual(a['profile_counts'],{'11':6,'12':0,'21':1});self.assertEqual(a['new_full_label_exclusions'],[]);self.assertTrue(all(r['remaining_source_pairs'] for r in a['records']))
 def test_remaining_counts(self):
  a=v.build(*self.inputs);d={r['id']:r['remaining_source_pair_count'] for r in a['records']};self.assertEqual([d[v.LABELS[i]] for i in [113,125,127]],[85,72,352])
 def test_untouched_four_records(self):
  old={r['id']:r for r in self.inputs[0]['records']}
  for r in v.build(*self.inputs)['records']:
   if r['id'] not in v.LABELS.values():self.assertEqual(r,old[r['id']])
 def test_prior_hash(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-through847.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_no_double_cuts(self):
  with self.assertRaises(ValueError):v.intersect(self.inputs[0],self.inputs[1],v.RULES+[v.RULES[0]])
 def test_every_scope_case_required(self):
  for name,cases in v.COVERAGE.items():
   for case in cases:
    c=deepcopy(v.COVERAGE);c[name].remove(case)
    with self.subTest(name=name,case=case),self.assertRaises(ValueError):v.validate_coverage(c)
 def test_divisor_branch_required(self):
  c=deepcopy(v.COVERAGE);c['common'].remove('positive_divisor_at_least12_leaves_at_most7_sections')
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_full_source_blocks(self):
  s,c,p=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==v.TUPLES['eg']);e['blocks'].remove([-9,'W'])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_arbitrary_local_ids(self):
  s,c,p=deepcopy(self.inputs);mapping={e['id']:9000+e['id']*23 for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,p)['pair_accounting']['remaining_necessary_pairs'],597)
 def test_pair_duplicates_rejected(self):
  s,c,p=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.LABELS[113]);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_no_double_label_ids(self):
  s,c,p=deepcopy(self.inputs);s['records'].append(s['records'][0])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_deferred_and_boundary(self):
  a=v.build(*self.inputs);self.assertEqual([r['pr'] for r in a['deferred']],[845]);self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['realization_count'])
if __name__=='__main__':unittest.main()
