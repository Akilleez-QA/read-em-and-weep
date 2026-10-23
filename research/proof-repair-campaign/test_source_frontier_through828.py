from copy import deepcopy
import hashlib
import unittest
import verify_source_frontier_through828 as v

class SourceThrough828Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.snapshot,cls.catalog,cls.pins=v.load_inputs()
 def fresh(self):return deepcopy(self.snapshot),deepcopy(self.catalog)
 def test_exact_replay(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertEqual(a['pair_accounting']['remaining_necessary_pairs'],840)
 def test_profiles_and_no_label_cut(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertEqual(a['remaining_ids'],self.snapshot['remaining_ids']);self.assertEqual(a['remaining_profile_counts'],{'11':8,'12':0,'21':1});self.assertEqual(a['new_full_label_exclusions'],[])
 def test_historical_snapshot_unchanged(self):self.assertEqual(hashlib.sha256((v.ROOT/'frontier-source-through823.json').read_bytes()).hexdigest(),v.PREVIOUS_SHA256)
 def test_overlapping_split_ce_claim_counted_once(self):
  a=v.build(self.snapshot,self.catalog,self.pins);ce=[r for r in a['new_source_edge_exclusion_ledger'] if r['label']==v.SPLIT and r['source']=='ce']
  self.assertEqual(len(ce),1);self.assertEqual(ce[0]['actual_additional_pair_count'],19);self.assertEqual(a['overlapping_proof_claims_not_recounted'][0]['additional_removed_pair_count'],0)
 def test_duplicate_source_cut_rejected(self):
  with self.assertRaisesRegex(ValueError,'Double'):v.intersect(self.snapshot,self.catalog,v.RULES+[v.rule('pr828',v.SPLIT,'ce')])
 def test_conditional_cut_rejected(self):
  rules=deepcopy(v.RULES);rules[0]['coverage']='rank_two_only'
  with self.assertRaisesRegex(ValueError,'Conditional'):v.intersect(self.snapshot,self.catalog,rules)
 def test_source_id_permutation(self):
  s,c=self.fresh();original,ledger=v.intersect(s,c);mapping={e['id']:7000+23*e['id'] for e in c}
  for e in c:e['id']=mapping[e['id']];e['blocks'].reverse()
  c.reverse()
  for r in s['records']:r['remaining_source_pairs']=[[mapping[e],q] for e,q in r['remaining_source_pairs']]
  changed,newledger=v.intersect(s,c)
  for a,b in zip(original,changed):self.assertEqual(b['remaining_source_pairs'],sorted([[mapping[e],q] for e,q in a['remaining_source_pairs']]))
  self.assertEqual([r['actual_additional_pair_count'] for r in ledger],[r['actual_additional_pair_count'] for r in newledger])
 def test_full_block_multiplicity(self):
  s,c=self.fresh();next(e for e in c if e['coefficients']==v.SOURCES['ce']['coefficients'])['blocks'].remove([-2,'P'])
  with self.assertRaisesRegex(ValueError,'Block/tuple'):v.intersect(s,c)
 def test_already_absent_edge_zero_new_count(self):
  s,c=self.fresh();eid=v.prior.identify(c,v.SOURCES['ef']);r=next(r for r in s['records'] if r['id']==v.SPLIT)
  r['remaining_source_pairs']=[p for p in r['remaining_source_pairs'] if p[0]!=eid];r['remaining_source_pair_count']=len(r['remaining_source_pairs'])
  _,ledger=v.intersect(s,c);self.assertEqual(ledger[0]['actual_additional_pair_count'],0);self.assertTrue(ledger[0]['already_absent_in_input'])
 def test_other_seven_labels_unchanged(self):
  rows,_=v.intersect(self.snapshot,self.catalog);old={r['id']:r for r in self.snapshot['records']}
  for r in rows:
   if r['id'] not in (v.SPLIT,v.BALANCED):self.assertEqual(r['remaining_source_pairs'],old[r['id']]['remaining_source_pairs'])
 def test_no_cartesian_completion(self):
  s,c=self.fresh();r=next(r for r in s['records'] if r['id']=='G3.21.d610e381ed75');missing=r['remaining_source_pairs'].pop();r['remaining_source_pair_count']-=1
  rows,_=v.intersect(s,c);self.assertNotIn(missing,next(r for r in rows if r['id']=='G3.21.d610e381ed75')['remaining_source_pairs'])
 def test_low_positive_subtotals(self):
  a=v.build(self.snapshot,self.catalog,self.pins);self.assertEqual(a['low_positive_remaining'][v.SPLIT],{'source_names':['bf','bc','bb'],'pair_count':57});self.assertEqual(a['low_positive_remaining'][v.BALANCED],{'source_names':['bc','bb'],'pair_count':32})
if __name__=='__main__':unittest.main(verbosity=2)
