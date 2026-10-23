import unittest
from copy import deepcopy
import verify_frontier_through911 as v
class LabelGate(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.s,cls.c,cls.p,cls.cov=v.load_inputs();cls.r=v.build(cls.s,cls.c,cls.p,cls.cov)
 def reject(self,mutate):
  c=deepcopy(self.cov);mutate(c)
  with self.assertRaises(ValueError):v.coverage_report(c)
 def test_counts(self):self.assertEqual(self.r['remaining_label_count'],3);self.assertEqual(self.r['profile_counts'],{'11':2,'12':0,'21':1});self.assertEqual(self.r['pair_accounting'],{'input_necessary_pairs':146,'additional_removed_pairs':0,'remaining_necessary_pairs':146})
 def test_original_ten(self):self.assertEqual(len(self.r['complete_original_source_coverage']),10)
 def test_missing_row(self):self.reject(lambda c:c['rows'].pop())
 def test_duplicate_row(self):self.reject(lambda c:c['rows'].__setitem__(-1,c['rows'][-2]))
 def test_reordered_row(self):self.reject(lambda c:c['rows'].reverse())
 def test_wrong_tuple(self):self.reject(lambda c:c['rows'][0]['tuple'].__setitem__(0,1))
 def test_wrong_decoded_multiset(self):self.reject(lambda c:c['rows'][0]['bundle'][1].__setitem__(2,1))
 def test_wrong_dependency(self):self.reject(lambda c:c['rows'][3].__setitem__('proof','ce'))
 def test_wrong_commit(self):self.reject(lambda c:c['proofs']['ee'].__setitem__('commit','0'*40))
 def test_conditional_bb_bc_rejected(self):self.reject(lambda c:c['proofs']['bb_bc'].__setitem__('status','conditional'))
 def test_missing_dependency(self):self.reject(lambda c:c['proofs'].pop('cc'))
 def test_review_binding(self):self.reject(lambda c:c['proofs']['bb_bc'].__setitem__('review_sha256','0'*64))
 def test_incomplete_gate(self):self.reject(lambda c:c.__setitem__('closure_state','pending'))
 def test_wrong_label(self):self.reject(lambda c:c.__setitem__('stable_label','G3.11.cce6e3ba4eeb'))
 def test_wrong_endpoint(self):self.reject(lambda c:c['A_q'][1].__setitem__(0,2))
 def test_every_scope_required(self):
  for key in v.SCOPE:
   s=deepcopy(v.SCOPE);s.pop(key)
   with self.assertRaises(ValueError):v.coverage_report(self.cov,s)
 def test_cannot_charge_hidden_pairs(self):
  s=deepcopy(self.s);row=next(r for r in s['records'] if r['id']==v.LABEL);row['remaining_source_pairs']=[[1,1]];row['remaining_source_pair_count']=1
  with self.assertRaises(ValueError):v.build(s,self.c,self.p,self.cov)
 def test_no_double_label_cut(self):
  with self.assertRaises(ValueError):v.build(self.r,self.c,self.p,self.cov)
 def test_all_other_pairs_unchanged(self):
  for row in self.r['records']:self.assertEqual(row,next(r for r in self.s['records'] if r['id']==row['id']))
 def test_fixed_baseline(self):
  d=self.r['fixed_campaign805_comparison'];self.assertEqual((d['baseline_labels'],d['labels_removed'],d['final_labels']),(17,14,3));self.assertEqual((d['baseline_necessary_pairs'],d['necessary_pairs_removed'],d['final_necessary_pairs']),(1790,1644,146))
 def test_remaining_tuple_counts(self):self.assertEqual([len(r['remaining_source_definitions']) for r in self.r['residual_source_summary']],[1,2,13])
 def test_boundary_unchanged(self):self.assertEqual(self.r['boundary'],self.s['boundary'])
 def test_zero_new_source_cuts(self):self.assertEqual(self.r['new_source_edge_exclusions'],[]);self.assertEqual(self.r['new_full_label_exclusion_ledger'][0]['removed_pairs'],[])
if __name__=='__main__':unittest.main()
