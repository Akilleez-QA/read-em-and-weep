import unittest
from copy import deepcopy
import verify_source_frontier_through877 as a
import verify_source_frontier_through882 as b
class Reconciliation(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s,cls.c,cls.p=a.load_inputs();cls.r=a.build(cls.s,cls.c,cls.p);cls.z=b.build(cls.r,cls.c,cls.p)
 def test_post877_total(self):self.assertEqual(self.r['pair_accounting'],{'input_necessary_pairs':501,'additional_removed_pairs':124,'remaining_necessary_pairs':377})
 def test_post882_total(self):self.assertEqual(self.z['pair_accounting'],{'input_necessary_pairs':377,'additional_removed_pairs':26,'remaining_necessary_pairs':351})
 def test_stable_ids(self):self.assertEqual(self.z['remaining_ids'],self.s['remaining_ids'])
 def test_profile_accounting(self):self.assertEqual(self.z['profile_counts'],{'11':4,'12':0,'21':1})
 def test_empty_relation_not_label_cut(self):
  self.assertEqual(self.z['remaining_label_count'],5);self.assertEqual(self.z['nonempty_relation_label_count'],4);self.assertEqual(self.z['new_full_label_exclusions'],[]);self.assertIn('closed',self.z['whole_label_gate'][a.LABELS[113]])
 def test_exact_rows(self):self.assertEqual({r['id']:r['remaining_source_pair_count'] for r in self.z['records']},{'G3.11.8ae96830fd21':4,a.LABELS[113]:0,a.LABELS[125]:45,a.LABELS[127]:224,'G3.21.d610e381ed75':78})
 def test_no_duplicate_cuts(self):
  ledger=self.r['new_source_edge_exclusion_ledger']+self.z['new_source_edge_exclusion_ledger'];pairs=[(r['label'],*p) for r in ledger for p in r['removed_pairs']];self.assertEqual(len(pairs),len(set(pairs)));self.assertEqual(len(pairs),150)
 def test_duplicate_rule_rejected(self):
  with self.assertRaises(ValueError):a.intersect(self.s,self.c,a.RULES+a.RULES[:1],a.RULES)
 def test_omitted_rule_rejected(self):
  with self.assertRaises(ValueError):a.intersect(self.s,self.c,a.RULES[:-1],a.RULES)
 def test_wrong_label_rejected(self):
  rules=deepcopy(a.RULES);rules[0]=(868,125,'cf',9)
  with self.assertRaises(ValueError):a.intersect(self.s,self.c,rules,a.RULES)
 def test_duplicate_pair_rejected(self):
  s=deepcopy(self.s);r=next(r for r in s['records'] if r['id']==a.LABELS[113]);r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):a.build(s,self.c,self.p)
 def test_source_blocks_not_only_tuple(self):
  c=deepcopy(self.c);eid=self.r['new_source_edge_exclusion_ledger'][0]['matched_local_E_id'];next(r for r in c if r['id']==eid)['blocks']=[]
  with self.assertRaises(ValueError):a.build(self.s,c,self.p)
 def test_missing_divisor_or_image_rejected(self):
  for pr in a.COVERAGE:
   for i in range(len(a.COVERAGE[pr])):
    c={pr:deepcopy(a.COVERAGE[pr])};c[pr].pop(i)
    with self.assertRaises(ValueError):a.validate_coverage(c,[int(pr)])
 def test_cf_divisor0_dependency_explicit(self):self.assertIn('PR861_sections2_to5_exclude_divisor0',self.r['source_branch_coverage']['868'])
 def test_bf_all_five_kernels_explicit(self):
  coverage=self.z['source_branch_coverage']['881'];self.assertEqual(sum(s.startswith('kernel') for s in coverage),5)
 def test_boundary_preserved(self):
  self.assertIn('no HM realization or exclusion',self.z['boundary']['PR869']);self.assertIn('no HM realization or exclusion',self.z['boundary']['PR876'])
 def test_abstract_cdf_retained(self):
  t=[0,0,1,1,0,1,0,0];e=a.accounting.identify(self.c,{'coefficients':t,'blocks':a.accounting.decode(t)});r=next(r for r in self.z['records'] if r['id']==a.LABELS[127]);self.assertEqual(sum(p[0]==e for p in r['remaining_source_pairs']),32)
 def test_unaffected_rows_byte_equal_pairs(self):
  for label in ['G3.11.8ae96830fd21','G3.21.d610e381ed75']:
   old=next(r for r in self.s['records'] if r['id']==label);new=next(r for r in self.z['records'] if r['id']==label);self.assertEqual(old['remaining_source_pairs'],new['remaining_source_pairs'])
 def test_local_catalog_renumbering(self):
  c=deepcopy(self.c);s=deepcopy(self.s);ren={r['id']:r['id']+10000 for r in c}
  for r in c:r['id']=ren[r['id']]
  for r in s['records']:r['remaining_source_pairs']=[[ren[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(a.build(s,c,self.p)['pair_accounting'],self.r['pair_accounting'])
 def test_reapplying_cuts_rejected(self):
  with self.assertRaises(ValueError):a.build(self.r,self.c,self.p)
 def test_original_quotient_mismatch_rejected(self):
  s=deepcopy(self.s);next(r for r in s['records'] if r['id']==a.LABELS[127])['A']=[]
  with self.assertRaises(ValueError):a.build(s,self.c,self.p)
 def test_full_original125_residual_tuples(self):
  row=next(r for r in self.z['records'] if r['id']==a.LABELS[125]);ids={p[0] for p in row['remaining_source_pairs']};tuples={tuple(r['coefficients']) for r in self.c if r['id'] in ids}
  self.assertEqual(tuples,{(0,2,0,0,0,0,0,1),(0,1,1,0,0,0,0,1),(0,1,0,0,1,0,0,1),(0,0,2,0,0,0,0,1),(0,0,1,0,1,0,0,1)})
if __name__=='__main__':unittest.main()
