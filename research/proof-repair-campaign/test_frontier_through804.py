from copy import deepcopy
import hashlib
import unittest
import verify_frontier_through804 as v

class Through804Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.pins=v.load_inputs()
 def test_exact_replay(self):
  a=v.build(self.snapshot,self.pins);self.assertEqual((a['remaining_label_count'],a['pair_accounting']['current12_baseline_relation']),(12,1319))
 def test_historical_snapshot_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier.json').read_bytes()).hexdigest(),v.HISTORICAL_SHA256)
 def test_no_double_cuts(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.restrict(self.snapshot,v.CUTS+[v.CUTS[0]])
 def test_previous_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Unknown'):v.restrict(self.snapshot,[{'source':'pr800','kind':'full_label','ids':['G3.11.18ad6075be86']}])
 def test_source_edge_not_label(self):
  c=deepcopy(v.CUTS);c[0]['kind']='source_edge'
  with self.assertRaisesRegex(ValueError,'Source-edge'):v.restrict(self.snapshot,c)
 def test_counts_and_stable_ids(self):
  ids,ledger,rows=v.restrict(self.snapshot,v.CUTS)
  self.assertEqual(v.historical.counts(ids),{'11':11,'12':0,'21':1})
  self.assertTrue(set(ids)<=set(self.snapshot['remaining_ids']))
  self.assertEqual([s['after_label_count'] for s in ledger],[15,13,12])
 def test_correlated_pairs_unchanged(self):
  _,_,rows=v.restrict(self.snapshot,v.CUTS);original={r['id']:r for r in self.snapshot['records']}
  for row in rows:self.assertEqual(row,original[row['id']])
 def test_hole_not_refilled(self):
  s=deepcopy(self.snapshot);r=next(r for r in s['records'] if r['id']=='G3.21.d610e381ed75');missing=r['baseline_pairs'].pop();r['baseline_pair_count']-=1
  _,_,rows=v.restrict(s,v.CUTS);after=next(r for r in rows if r['id']=='G3.21.d610e381ed75')
  self.assertNotIn(missing,after['baseline_pairs'])
 def test_profile_corruption(self):
  s=deepcopy(self.snapshot);s['records'][0]['profile']='21'
  with self.assertRaisesRegex(ValueError,'profile'):v.restrict(s,v.CUTS)
 def test_duplicate_tuple(self):
  s=deepcopy(self.snapshot);r=s['records'][0];r['baseline_pairs'].append(r['baseline_pairs'][0]);r['baseline_pair_count']+=1
  with self.assertRaisesRegex(ValueError,'Duplicate source'):v.restrict(s,v.CUTS)
if __name__=='__main__':unittest.main(verbosity=2)
