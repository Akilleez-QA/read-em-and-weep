from copy import deepcopy
import hashlib
import unittest
import verify_source_frontier_through839 as v

class Through839Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.catalog,cls.pins,cls.original=v.load_inputs()
 def test_exact_counts(self):
  a=v.build(self.snapshot,self.catalog,self.pins,self.original);self.assertEqual(a['pair_accounting']['remaining_necessary_pairs'],759);self.assertEqual(a['pair_accounting']['additional_removed_pairs'],51)
 def test_empty_relation_does_not_decrement_registered_labels(self):
  a=v.build(self.snapshot,self.catalog,self.pins,self.original);self.assertEqual(a['registered_label_count'],9);self.assertEqual(a['nonempty_relation_label_count'],8);self.assertEqual(a['empty_relation_ids'],[v.BALANCED]);self.assertEqual(a['new_adjudicated_full_label_exclusions'],[]);self.assertEqual(a['whole_label_gate']['status'],'held_closed');self.assertFalse(a['whole_label_gate']['immutable_full_exhaustion_publication_verified'])
 def test_original_ten_tuple_coverage(self):
  a=v.build(self.snapshot,self.catalog,self.pins,self.original);r=a['balanced_ten_tuple_relation_coverage'];self.assertEqual(len(r),10);self.assertEqual(sum(x['historical_pr796_pair_count']==0 for x in r),3);self.assertEqual(sum(x['historical_pr796_pair_count'] for x in r),112);self.assertEqual(sum(x['current_pair_count'] for x in r),0)
 def test_original_missing_tuple_rejected(self):
  original=deepcopy(self.original);original['compatible_E_types'].pop()
  with self.assertRaisesRegex(ValueError,'ten-tuple'):v.build(self.snapshot,self.catalog,self.pins,original)
 def test_balanced_bb_onto_alone_insufficient(self):
  c=deepcopy(v.COVERAGE);del c['balanced_bb']['cases']['rank_two_nononto']
  with self.assertRaisesRegex(ValueError,'Incomplete'):v.validate_coverage(c,self.pins)
 def test_balanced_bb_needs_rank_one_exclusion(self):
  p=deepcopy(self.pins);del p['pr814_rank_one']
  with self.assertRaisesRegex(ValueError,'Missing'):v.validate_coverage(v.COVERAGE,p)
 def test_bc_rank_one_alone_insufficient(self):
  c=deepcopy(v.COVERAGE);del c['balanced_bc']['cases']['rank_two']
  with self.assertRaisesRegex(ValueError,'Incomplete'):v.validate_coverage(c,self.pins)
 def test_prior_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through834.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_catalog_reindexing_and_blocks(self):
  s,c=deepcopy(self.snapshot),deepcopy(self.catalog);old,_=v.intersect(s,c);mapping={e['id']:1200+31*e['id'] for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  new,l=v.intersect(s,c)
  for a,b in zip(old,new):self.assertEqual(b['remaining_source_pairs'],sorted([[mapping[e],q] for e,q in a['remaining_source_pairs']]))
  self.assertEqual([r['actual_additional_pair_count'] for r in l],[19,16,16])
 def test_duplicate_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.intersect(self.snapshot,self.catalog,v.RULES+[v.RULES[0]])
 def test_untouched_seven_labels(self):
  rows,_=v.intersect(self.snapshot,self.catalog);old={r['id']:r for r in self.snapshot['records']}
  for r in rows:
   if r['id'] not in (v.SPLIT,v.BALANCED):self.assertEqual(r['remaining_source_pairs'],old[r['id']]['remaining_source_pairs'])
 def test_split_keeps_bf_bc(self):
  a=v.build(self.snapshot,self.catalog,self.pins,self.original);self.assertEqual(a['split_residual']['remaining_necessary_pairs'],38);self.assertEqual(a['split_residual']['source_names'],['bf','bc'])
if __name__=='__main__':unittest.main(verbosity=2)
