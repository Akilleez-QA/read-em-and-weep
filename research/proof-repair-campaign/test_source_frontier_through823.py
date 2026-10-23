from copy import deepcopy
import hashlib
import unittest
import verify_source_frontier_through823 as v

class SourceFrontierTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.catalog,cls.pins=v.load_inputs()
 def fresh(self):return deepcopy(self.snapshot),deepcopy(self.catalog)
 def test_exact_replay(self):
  a=v.build(self.snapshot,self.catalog,self.pins)
  self.assertEqual(a['pair_accounting'],{'input_historical_pairs':1004,'additional_removed_pairs':24,'already_absent_target_edges':0,'remaining_necessary_pairs':980})
 def test_no_label_cut(self):
  a=v.build(self.snapshot,self.catalog,self.pins)
  self.assertEqual(a['remaining_ids'],self.snapshot['remaining_ids']);self.assertEqual(a['new_full_label_exclusions'],[])
 def test_old_snapshot_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-through806.json').read_bytes()).hexdigest(),v.HISTORICAL_SHA256)
 def test_catalog_renumbering_and_order(self):
  s,c=self.fresh();original,_,_=v.intersect(s,c);mapping={e['id']:3000+19*e['id'] for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['baseline_pairs']=[[mapping[e],q] for e,q in r['baseline_pairs']]
  result,ledger,_=v.intersect(s,c)
  for x,y in zip(original,result):self.assertEqual(y['remaining_source_pairs'],sorted([[mapping[e],q] for e,q in x['remaining_source_pairs']]))
  self.assertEqual([x['actual_additional_pair_count'] for x in ledger],[4,4,16])
 def test_full_block_multiplicity_matters(self):
  s,c=self.fresh();e=next(e for e in c if e['coefficients']==v.SOURCES['E0']['coefficients']);e['blocks'].remove([-2,'D'])
  with self.assertRaisesRegex(ValueError,'Block/tuple'):v.intersect(s,c)
 def test_tuple_and_blocks_must_agree(self):
  s,c=self.fresh();next(e for e in c if e['coefficients']==v.SOURCES['bf']['coefficients'])['coefficients']=[9]*8
  with self.assertRaisesRegex(ValueError,'Block/tuple'):v.intersect(s,c)
 def test_duplicate_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.intersect(self.snapshot,self.catalog,v.RULES+[v.RULES[0]])
 def test_conditional_cut_rejected(self):
  rules=deepcopy(v.RULES);rules[0]['coverage']='delta0_only'
  with self.assertRaisesRegex(ValueError,'Conditional'):v.intersect(self.snapshot,self.catalog,rules)
 def test_already_absent_edges_not_recounted(self):
  s,c=self.fresh();eid=v.identify(c,v.SOURCES['E0']);r=next(r for r in s['records'] if r['id']==v.O26)
  r['baseline_pairs']=[p for p in r['baseline_pairs'] if p[0]!=eid];r['baseline_pair_count']=len(r['baseline_pairs'])
  _,ledger,_=v.intersect(s,c)
  self.assertEqual([x['actual_additional_pair_count'] for x in ledger],[0,4,16]);self.assertTrue(ledger[0]['already_absent_in_input'])
 def test_pair_hole_stays_absent(self):
  s,c=self.fresh();r=next(r for r in s['records'] if r['id']=='G3.21.d610e381ed75');missing=r['baseline_pairs'].pop();r['baseline_pair_count']-=1
  rows,_,_=v.intersect(s,c);self.assertNotIn(missing,next(r for r in rows if r['id']=='G3.21.d610e381ed75')['remaining_source_pairs'])
 def test_other_labels_unchanged(self):
  rows,_,_=v.intersect(self.snapshot,self.catalog);old={r['id']:r for r in self.snapshot['records']}
  for r in rows:
   if r['id'] not in (v.O26,v.BALANCED):self.assertEqual(r['remaining_source_pairs'],sorted(old[r['id']]['baseline_pairs']))
 def test_bf_requires_zero_and_nonzero_coverage(self):
  a=v.build(self.snapshot,self.catalog,self.pins);coverage=a['coverage_certificate'][v.BALANCED]
  self.assertFalse(coverage['PR823_alone_is_full_source_exclusion']);self.assertIn('PR814',coverage['J_zero']);self.assertIn('PR823',coverage['J_nonzero'])
 def test_singleton_is_not_realization(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertFalse(a['coverage_certificate'][v.O26]['remaining_is_realizable'])
  row=next(r for r in a['records'] if r['id']==v.O26);self.assertEqual(row['remaining_source_pair_count'],4)
if __name__=='__main__':unittest.main(verbosity=2)
