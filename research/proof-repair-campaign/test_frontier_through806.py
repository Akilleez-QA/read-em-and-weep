from copy import deepcopy
import hashlib
import unittest
import verify_frontier_through806 as v

class Through806Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.pins=v.load_inputs()
 def test_exact_replay(self):
  a=v.build(self.snapshot,self.pins);self.assertEqual((a['remaining_label_count'],a['pair_accounting']['current9_baseline_relation']),(9,1004))
 def test_checkpoints_unchanged(self):
  self.assertEqual(hashlib.sha256((v.ROOT/'frontier-through804.json').read_bytes()).hexdigest(),v.PRIOR_SHA256)
  self.assertEqual(hashlib.sha256((v.ROOT/'frontier.json').read_bytes()).hexdigest(),v.prior.HISTORICAL_SHA256)
 def test_distinct_append_only_cuts(self):
  a=v.build(self.snapshot,self.pins);cuts=a['cumulative_full_label_exclusion_ledger'];ids=[i for c in cuts for i in c['ids']]
  self.assertEqual(len(ids),len(set(ids)));self.assertEqual(len(ids),14)
  self.assertEqual([c['after_label_count'] for c in cuts],[22,20,19,17,15,13,12,9])
 def test_double_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.prior.restrict(self.snapshot,v.CUTS*2)
 def test_older_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Unknown'):v.prior.restrict(self.snapshot,v.prior.CUTS[:1])
 def test_source_edge_rejected(self):
  c=deepcopy(v.CUTS);c[0]['kind']='source_edge'
  with self.assertRaisesRegex(ValueError,'Source-edge'):v.prior.restrict(self.snapshot,c)
 def test_exact_pair_restriction_and_stable_ids(self):
  a=v.build(self.snapshot,self.pins);old={r['id']:r for r in self.snapshot['records']}
  for r in a['records']:self.assertEqual(r,old[r['id']])
  self.assertEqual(a['remaining_profile_counts'],{'11':8,'12':0,'21':1});self.assertIn('G3.21.d610e381ed75',a['remaining_ids'])
 def test_corruption_rejected(self):
  s=deepcopy(self.snapshot);s['records'][0]['baseline_pair_count']+=1
  with self.assertRaisesRegex(ValueError,'tuple count'):v.build(s,self.pins)
if __name__=='__main__':unittest.main(verbosity=2)
