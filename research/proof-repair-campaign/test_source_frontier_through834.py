from copy import deepcopy
import hashlib
import unittest
import verify_source_frontier_through834 as v

class Through834Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.catalog,cls.pins=v.load_inputs()
 def fresh(self):return deepcopy(self.snapshot),deepcopy(self.catalog)
 def test_exact_totals(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertEqual(a['pair_accounting']['remaining_necessary_pairs'],810);self.assertEqual(a['pair_accounting']['older_complete_coverage_pairs_removed'],12)
 def test_prior_snapshot_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through828.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_label_set_unchanged(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertEqual(a['remaining_ids'],self.snapshot['remaining_ids']);self.assertEqual(a['new_full_label_exclusions'],[])
 def test_singletons_and_divisor_boundaries(self):
  a=v.build(self.snapshot,self.catalog,self.pins)
  self.assertEqual([(a['o26_remaining'][l]['source_name'],a['o26_remaining'][l]['possible_top_divisor_degrees'],a['o26_remaining'][l]['remaining_necessary_pairs']) for l in (v.D,v.W,v.T)],[('E6',[0,20],3),('E13',[0,20],3),('E10',[0],4)])
  self.assertTrue(all(not r['realizability_asserted'] for r in a['o26_remaining'].values()))
 def test_missing_divisor_case_rejected(self):
  c=deepcopy(v.COVERAGE);del c['old_E0_D']['cases']['20']
  with self.assertRaisesRegex(ValueError,'Incomplete divisor'):v.intersect(self.snapshot,self.catalog,coverage=c)
 def test_missing_pinned_dependency_rejected(self):
  pins=deepcopy(self.pins);del pins['pr817']
  with self.assertRaisesRegex(ValueError,'Missing pinned'):v.validate_coverage(v.COVERAGE,pins)
 def test_mismatch_needs_divisor_independent_scope(self):
  c=deepcopy(v.COVERAGE);c['mismatch_E6_W']['mode']='delta0_only'
  with self.assertRaisesRegex(ValueError,'Conditional'):v.intersect(self.snapshot,self.catalog,coverage=c)
 def test_duplicate_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.intersect(self.snapshot,self.catalog,v.RULES+[v.RULES[0]])
 def test_catalog_reindexing(self):
  s,c=self.fresh();old,_,_=v.intersect(s,c);m={e['id']:5000+13*e['id'] for e in c}
  for e in c:e['id']=m[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[m[e],q] for e,q in r['remaining_source_pairs']]
  new,ledger,_=v.intersect(s,c)
  for a,b in zip(old,new):self.assertEqual(b['remaining_source_pairs'],sorted([[m[e],q] for e,q in a['remaining_source_pairs']]))
  self.assertEqual([r['actual_additional_pair_count'] for r in ledger],[3]*10)
 def test_repeated_blocks_matter(self):
  s,c=self.fresh();next(e for e in c if e['coefficients']==v.SOURCES['U6']['coefficients'])['blocks'].remove([-2,'P'])
  with self.assertRaisesRegex(ValueError,'Block/tuple'):v.intersect(s,c)
 def test_old_absent_edge_not_recounted(self):
  s,c=self.fresh();eid=v.previous.prior.identify(c,v.SOURCES['U6']);r=next(r for r in s['records'] if r['id']==v.D)
  r['remaining_source_pairs']=[p for p in r['remaining_source_pairs'] if p[0]!=eid];r['remaining_source_pair_count']=len(r['remaining_source_pairs'])
  _,ledger,_=v.intersect(s,c);self.assertEqual(ledger[0]['actual_additional_pair_count'],0);self.assertTrue(ledger[0]['already_absent_in_input'])
 def test_untouched_seven_labels(self):
  rows,_,_=v.intersect(self.snapshot,self.catalog);original={r['id']:r for r in self.snapshot['records']}
  for r in rows:
   if r['id'] not in (v.D,v.W):self.assertEqual(r['remaining_source_pairs'],original[r['id']]['remaining_source_pairs'])
 def test_deferred_split_bf_not_deleted(self):
  a=v.build(self.snapshot,self.catalog,self.pins);s=next(r for r in a['records'] if r['id']=='G3.11.863639aa192e');self.assertEqual(s['remaining_source_pair_count'],57);self.assertTrue(any(x['publication']=='PR830' for x in a['deferred_branch_restrictions']))
if __name__=='__main__':unittest.main(verbosity=2)
