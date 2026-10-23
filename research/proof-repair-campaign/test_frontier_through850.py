from copy import deepcopy
import hashlib, unittest
import verify_frontier_through850 as v
class Through850Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_accounting(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],5);self.assertEqual(a['profile_counts'],{'11':4,'12':0,'21':1});self.assertEqual(a['pair_accounting']['remaining_necessary_pairs'],591);self.assertEqual(a['pair_accounting']['additional_removed_pairs'],6)
 def test_exact_two_labels_three_pairs_each(self):
  a=v.build(*self.inputs);self.assertEqual({r['id'] for r in a['new_full_label_exclusion_ledger']},set(v.LABELS.values()));self.assertEqual([r['actual_additional_pair_count'] for r in a['new_full_label_exclusion_ledger']],[3,3]);self.assertEqual(a['new_source_edge_exclusions'],[])
 def test_four_and_eight_original_entries(self):
  r=v.build(*self.inputs)['complete_original_source_coverage'];self.assertEqual([sum(x['original_source_index']==i for x in r) for i in [112,115]],[4,8])
 def test_missing_original_source(self):
  s,c,p,o=deepcopy(self.inputs);o[115]['compatible_E_types'].pop()
  with self.assertRaises(ValueError):v.build(s,c,p,o)
 def test_duplicate_original_source(self):
  s,c,p,o=deepcopy(self.inputs);o[112]['compatible_E_types'][0]=o[112]['compatible_E_types'][1]
  with self.assertRaises(ValueError):v.build(s,c,p,o)
 def test_all_divisor_and_mismatch_cases_required(self):
  for name,cases in v.COVERAGE.items():
   for case in cases:
    c=deepcopy(v.COVERAGE);del c[name][case]
    with self.subTest(name=name,case=case),self.assertRaises(ValueError):v.validate_coverage(c,v.TAIL_SCOPE)
 def test_each_geometric_tail_premise_required(self):
  for premise in v.TAIL_SCOPE:
   t=deepcopy(v.TAIL_SCOPE);t.remove(premise)
   with self.subTest(premise=premise),self.assertRaises(ValueError):v.validate_coverage(v.COVERAGE,t)
 def test_previous_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-pr846.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_all_survivors_unchanged(self):
  old={r['id']:r for r in self.inputs[0]['records']}
  for r in v.build(*self.inputs)['records']:self.assertEqual(r,old[r['id']])
 def test_8ae_untouched(self):
  a=v.build(*self.inputs);r=next(r for r in a['records'] if r['id']=='G3.11.8ae96830fd21');self.assertEqual(r['remaining_source_pair_count'],4)
 def test_duplicate_pair_not_recounted(self):
  s,c,p,o=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.LABELS[112]);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,c,p,o)
 def test_full_blocks_required(self):
  s,c,p,o=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==v.o26.SOURCES['E13']['coefficients']);e['blocks'].pop()
  with self.assertRaises(ValueError):v.build(s,c,p,o)
 def test_local_ids_not_keys(self):
  s,c,p,o=deepcopy(self.inputs);mapping={e['id']:e['id']*31+9000 for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,p,o)['pair_accounting']['remaining_necessary_pairs'],591)
 def test_boundary_and_848_deferred(self):
  a=v.build(*self.inputs);self.assertEqual(a['deferred'][0]['pr'],848);self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['realization_count'])
if __name__=='__main__':unittest.main()
