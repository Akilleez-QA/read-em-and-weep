#!/usr/bin/env python3
"""Regression and metamorphic tests for the new campaign frontier dependency."""
from copy import deepcopy
import unittest
import verify_frontier as v

class FrontierTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.base,cls.prior,cls.pins=v.load_inputs()
 def fresh(self):return deepcopy(self.base),deepcopy(self.prior),deepcopy(self.pins)
 def test_exact_replay(self):
  a=v.build(*self.fresh());self.assertEqual((a['remaining_label_count'],a['pair_accounting']['current17_baseline_relation']),(17,1790))
 def test_no_double_exclusion(self):
  with self.assertRaisesRegex(ValueError,'Double label'):v.apply_label_cuts(self.base['remaining_ids'],v.LABEL_CUTS+[v.LABEL_CUTS[0]])
 def test_duplicate_inside_cut(self):
  c=deepcopy(v.LABEL_CUTS);c[0]['ids']*=2
  with self.assertRaisesRegex(ValueError,'Duplicate ID'):v.apply_label_cuts(self.base['remaining_ids'],c)
 def test_source_edges_not_labels(self):
  c=[{'kind':'source_edge','source':'pr796','ids':['G3.12.37914c53373c']}]
  with self.assertRaisesRegex(ValueError,'Source-edge'):v.apply_label_cuts(self.base['remaining_ids'],c)
 def test_profile_accounting(self):
  b,p,s=self.fresh();b['profiles']['11']=18
  with self.assertRaisesRegex(ValueError,'profile'):v.build(b,p,s)
 def test_record_profile_accounting(self):
  b,p,s=self.fresh();p['records'][0]['profile']='21'
  with self.assertRaisesRegex(ValueError,'profile'):v.build(b,p,s)
 def test_all_survivors_keep_original_ids(self):
  a=v.build(*self.fresh());self.assertTrue(set(a['remaining_ids'])<=set(self.base['remaining_ids']))
  self.assertEqual({r['id'] for r in a['records']},set(a['remaining_ids']))
  self.assertEqual(a['remaining_ids'][-1],'G3.21.d610e381ed75')
 def test_unknown_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Unknown'):v.apply_label_cuts(self.base['remaining_ids'],[{'kind':'full_label','source':'bad','ids':['G3.11.nonexistent']}])
 def test_catalog_reindexing_preserves_pairs_and_blocks(self):
  b,p,s=self.fresh();a=v.build(b,p,s);mapping={e['id']:1000+17*e['id'] for e in p['E_catalog']}
  for e in p['E_catalog']:e['id']=mapping[e['id']];e['blocks'].reverse()
  p['E_catalog'].reverse()
  for r in p['records']:
   for key in ('remaining_source_pairs','removed_source_pairs'):r[key]=[[mapping[e],q] for e,q in r[key]]
  replay=v.build(b,p,s)
  self.assertEqual(a['remaining_ids'],replay['remaining_ids'])
  for x,y in zip(a['records'],replay['records']):self.assertEqual(y['baseline_pairs'],[[mapping[e],q] for e,q in x['baseline_pairs']])
 def test_preserves_correlated_pairs_not_projection_product(self):
  a=v.build(*self.fresh());source={r['id']:r for r in self.prior['records']}
  for r in a['records']:self.assertEqual(r['baseline_pairs'],source[r['id']]['remaining_source_pairs'])
 def test_duplicate_pair_rejected(self):
  b,p,s=self.fresh();r=p['records'][0];r['remaining_source_pairs'].append(r['remaining_source_pairs'][0])
  with self.assertRaisesRegex(ValueError,'Duplicate source'):v.build(b,p,s)
 def test_inherited_exclusion_not_recounted(self):
  a=v.build(*self.fresh());new={i for c in a['full_label_exclusion_ledger'] for i in c['ids']}
  self.assertEqual(len(new),6);self.assertTrue(new.isdisjoint(a['inherited_exclusions_not_recounted']))
 def test_stage_arithmetic(self):
  a=v.build(*self.fresh());self.assertEqual([c['after_label_count'] for c in a['full_label_exclusion_ledger']],[22,20,19,17])
  self.assertEqual([c['removed_pr796_baseline_pairs'] for c in a['subsequent_pair_removal_ledger']],[32,78,96])
if __name__=='__main__':unittest.main(verbosity=2)
