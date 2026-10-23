import unittest
from copy import deepcopy
import verify_frontier_through884 as v
class Gate(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.args=v.load_inputs();cls.r=v.build(*cls.args)
 def test_exact_four_profiles(self):self.assertEqual(self.r['profile_counts'],{'11':3,'12':0,'21':1});self.assertEqual(self.r['remaining_label_count'],4)
 def test_no_double_pair_charge(self):self.assertEqual(self.r['pair_accounting']['additional_removed_pairs'],0);self.assertEqual(self.r['pair_accounting']['remaining_necessary_pairs'],351)
 def test_only_target_label_removed(self):self.assertEqual(set(self.args[0]['remaining_ids'])-set(self.r['remaining_ids']),{v.LABEL})
 def test_survivors_unchanged(self):self.assertEqual(self.r['records'],[r for r in self.args[0]['records'] if r['id']!=v.LABEL])
 def test_complete_original_ten(self):self.assertEqual(len(self.r['complete_original_source_coverage']),10)
 def test_missing_original_tuple_rejected(self):
  c=deepcopy(self.args[3]);c['coverage'].pop()
  with self.assertRaises(ValueError):v.coverage_report(c,self.args[4])
 def test_duplicate_original_tuple_rejected(self):
  c=deepcopy(self.args[3]);c['coverage'][-1]=c['coverage'][0]
  with self.assertRaises(ValueError):v.coverage_report(c,self.args[4])
 def test_wrong_source_theorem_rejected(self):
  c=deepcopy(self.args[3]);c['coverage'][0]['pr']=854
  with self.assertRaises(ValueError):v.coverage_report(c,self.args[4])
 def test_missing_divisor_dependency_rejected(self):
  p=deepcopy(self.args[4]);p['PR861-CF-REDUCTION.md']['url']='missing'
  with self.assertRaises(ValueError):v.coverage_report(self.args[3],p)
 def test_missing_branch_scope_rejected(self):
  s=deepcopy(v.SCOPE);s.pop('bf')
  with self.assertRaises(ValueError):v.coverage_report(self.args[3],self.args[4],s)
 def test_nonempty_gate_rejected(self):
  args=list(deepcopy(self.args));row=next(r for r in args[0]['records'] if r['id']==v.LABEL);row['remaining_source_pairs']=[[1,1]];row['remaining_source_pair_count']=1
  with self.assertRaises(ValueError):v.build(*args)
 def test_two_direct_multiplicity_exclusions(self):
  rows=self.r['complete_original_source_coverage'];self.assertEqual({r['name'] for r in rows if r['kind']=='strict_top'},{'ee','cc'});self.assertEqual(v.sym(18)['V'],1);self.assertEqual(v.sym(18)['P'],2)
 def test_abstract_boundaries_retained(self):self.assertEqual(self.r['boundary'],self.args[0]['boundary'])
if __name__=='__main__':unittest.main()
