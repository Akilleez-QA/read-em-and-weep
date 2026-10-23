import unittest
from copy import deepcopy
import verify_source_frontier_through893 as v
class SourceCuts(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.s,cls.c,cls.p=v.load_inputs();cls.r=v.build(cls.s,cls.c,cls.p)
 def test_exact_total(self):self.assertEqual(self.r['pair_accounting'],{'input_necessary_pairs':310,'additional_removed_pairs':41,'remaining_necessary_pairs':269})
 def test_exact_cuts(self):self.assertEqual([r['actual_additional_pair_count'] for r in self.r['new_source_edge_exclusion_ledger']],[32,9])
 def test_all_labels_retained(self):self.assertEqual(self.r['remaining_ids'],self.s['remaining_ids']);self.assertEqual(self.r['remaining_label_count'],4);self.assertEqual(self.r['profile_counts'],{'11':3,'12':0,'21':1});self.assertEqual(self.r['new_full_label_exclusions'],[])
 def test_exact_row_counts(self):self.assertEqual({r['id']:r['remaining_source_pair_count'] for r in self.r['records']},{'G3.11.8ae96830fd21':4,'G3.11.cce6e3ba4eeb':160,'G3.11.ea6bced3bddf':27,'G3.21.d610e381ed75':78})
 def test_no_doublecut(self):
  pairs=[(r['label'],*p) for r in self.r['new_source_edge_exclusion_ledger'] for p in r['removed_pairs']];self.assertEqual(len(set(pairs)),41)
 def test_duplicate_rule_rejected(self):
  with self.assertRaises(ValueError):v.intersect(self.s,self.c,v.RULES+v.RULES[:1])
 def test_885_not_wholeedge(self):
  rules=deepcopy(v.RULES);rules[1]=(885,*rules[1][1:])
  with self.assertRaises(ValueError):v.intersect(self.s,self.c,rules)
 def test_all_scope_obligations_required(self):
  for pr in v.COVERAGE:
   for i in range(len(v.COVERAGE[pr])):
    c=deepcopy(v.COVERAGE);c[pr].pop(i)
    with self.assertRaises(ValueError):v.validate_coverage(c)
 def test_maximal_profile_required(self):
  s=deepcopy(self.s);next(r for r in s['records'] if r['id']=='G3.11.cce6e3ba4eeb')['profile']='12'
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_original_maximal_profile_required(self):
  with self.assertRaises(ValueError):v.validate_profile({'profile':'11'},{'profile':'12'})
 def test_nested_bounds_not_rank_addition_through_extension(self):
  p=deepcopy(v.MAXIMAL_PROFILE);p['next_gain_upper']=3
  with self.assertRaises(ValueError):v.validate_profile({'profile':'11'},{'profile':'11'},p)
 def test_both_Vlow_and_q_branches(self):
  c=self.r['source_branch_coverage']['893'];self.assertTrue(any('Vlow_nonzero' in x for x in c));self.assertTrue(any('Vlow_zero' in x for x in c));self.assertTrue(any('q_nonzero' in x for x in c));self.assertTrue(any('q_zero' in x for x in c))
 def test_source_blocks_required(self):
  c=deepcopy(self.c);e=self.r['new_source_edge_exclusion_ledger'][0]['matched_local_E_id'];next(r for r in c if r['id']==e)['blocks']=[]
  with self.assertRaises(ValueError):v.build(self.s,c,self.p)
 def test_endpoints_not_transferred(self):
  s=deepcopy(self.s);next(r for r in s['records'] if r['id']=='G3.11.cce6e3ba4eeb')['A']=[[-10,'one'],[2,'one'],[16,'one']]
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_duplicate_pair_rejected(self):
  s=deepcopy(self.s);r=next(r for r in s['records'] if r['id']=='G3.11.cce6e3ba4eeb');r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_catalog_renumbering(self):
  s=deepcopy(self.s);c=deepcopy(self.c);ren={r['id']:r['id']+20000 for r in c}
  for r in c:r['id']=ren[r['id']]
  for r in s['records']:r['remaining_source_pairs']=[[ren[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,self.p)['pair_accounting'],self.r['pair_accounting'])
 def test_remaining_source_counts(self):
  for label,n in [('G3.11.ea6bced3bddf',3),('G3.11.cce6e3ba4eeb',5)]:
   r=next(r for r in self.r['records'] if r['id']==label);self.assertEqual(len({e for e,q in r['remaining_source_pairs']}),n)
 def test_abstract_boundaries_untouched(self):
  self.assertEqual(self.r['boundary'],self.s['boundary'])
  t=[0,0,1,1,0,1,0,0];e=v.accounting.identify(self.c,{'coefficients':t,'blocks':v.accounting.decode(t)});r=next(r for r in self.r['records'] if r['id']=='G3.11.cce6e3ba4eeb');self.assertEqual(sum(a==e for a,q in r['remaining_source_pairs']),32)
 def test_unaffected_rows_unchanged_pairs(self):
  for label in ['G3.11.8ae96830fd21','G3.21.d610e381ed75']:
   self.assertEqual(next(r for r in self.r['records'] if r['id']==label)['remaining_source_pairs'],next(r for r in self.s['records'] if r['id']==label)['remaining_source_pairs'])
 def test_reapplying_cuts_rejected(self):
  with self.assertRaises(ValueError):v.build(self.r,self.c,self.p)
if __name__=='__main__':unittest.main()
