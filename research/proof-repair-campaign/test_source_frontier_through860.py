from copy import deepcopy
import hashlib, unittest
import verify_source_frontier_through860 as v
class Through860Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.inputs=v.load_inputs()
 def test_exact_accounting(self):
  a=v.build(*self.inputs);self.assertEqual(a['pair_accounting'],{'input_necessary_pairs':510,'additional_removed_pairs':9,'remaining_necessary_pairs':501});self.assertEqual(next(r for r in a['records'] if r['id']==v.LABEL)['remaining_source_pair_count'],63)
 def test_no_label_cut(self):
  a=v.build(*self.inputs);self.assertEqual(a['remaining_label_count'],5);self.assertEqual(a['profile_counts'],{'11':4,'12':0,'21':1});self.assertEqual(a['new_full_label_exclusions'],[])
 def test_other_four_records_unchanged(self):
  old={r['id']:r for r in self.inputs[0]['records']}
  for r in v.build(*self.inputs)['records']:
   if r['id']!=v.LABEL:self.assertEqual(r,old[r['id']])
 def test_predecessor_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through854.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_duplicate_cut_rejected(self):
  with self.assertRaises(ValueError):v.intersect(self.inputs[0],self.inputs[1],(v.LABEL,v.LABEL))
 def test_every_coverage_premise_required(self):
  for name,cases in v.COVERAGE.items():
   for case in cases:
    c=deepcopy(v.COVERAGE);c[name].remove(case)
    with self.subTest(name=name,case=case),self.assertRaises(ValueError):v.validate_coverage(c)
 def test_all_four_internal_images(self):self.assertEqual(len(v.COVERAGE['internal_images']),4)
 def test_saturated_target_factorization_required(self):
  c=deepcopy(v.COVERAGE);c['nonzero_images'].remove('D_to_T_nonzero_AplusV_O8_factors_through_saturated_O16')
  with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_complete_blocks_required(self):
  s,c,p=deepcopy(self.inputs);e=next(e for e in c if e['coefficients']==v.TUPLE);e['blocks'].pop()
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_local_numbering_irrelevant(self):
  s,c,p=deepcopy(self.inputs);mapping={e['id']:9000+e['id']*41 for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,p)['pair_accounting']['remaining_necessary_pairs'],501)
 def test_duplicate_pair_rejected(self):
  s,c,p=deepcopy(self.inputs);r=next(r for r in s['records'] if r['id']==v.LABEL);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,c,p)
 def test_deferred_and_boundary(self):
  a=v.build(*self.inputs);self.assertEqual([r['pr'] for r in a['deferred']],[856,858,859]);self.assertFalse(a['boundary']['formal_lean_proof']);self.assertFalse(a['boundary']['source2_closed']);self.assertFalse(a['boundary']['realization_count'])
if __name__=='__main__':unittest.main()
