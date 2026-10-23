import unittest
from copy import deepcopy
import verify_source_frontier_through917 as v

class ExactSource917(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.s,cls.c,cls.p=v.load_inputs();cls.r=v.build(cls.s,cls.c,cls.p)
 def test_total(self):self.assertEqual(self.r['pair_accounting'],dict(input_necessary_pairs=146,additional_removed_pairs=32,remaining_necessary_pairs=114))
 def test_no_label_cut(self):
  self.assertEqual(self.r['remaining_ids'],self.s['remaining_ids']);self.assertEqual(self.r['remaining_label_count'],3);self.assertEqual(self.r['new_full_label_exclusions'],[])
 def test_profiles(self):self.assertEqual(self.r['profile_counts'],{'11':2,'12':0,'21':1})
 def test_partition_exact_ids(self):
  before={(r['id'],*p) for r in self.s['records'] for p in r['remaining_source_pairs']}
  after={(r['id'],*p) for r in self.r['records'] for p in r['remaining_source_pairs']}
  cut={(x['label'],*p) for x in self.r['new_source_edge_exclusion_ledger'] for p in x['removed_pairs']}
  self.assertEqual(len(cut),32);self.assertFalse(cut&after);self.assertEqual(before,after|cut)
 def test_same_tuple_other_label_survives(self):
  eid=self.r['new_source_edge_exclusion_ledger'][0]['matched_local_E_id']
  before={(r['id'],*p) for r in self.s['records'] for p in r['remaining_source_pairs'] if r['id']!=v.LABEL and p[0]==eid}
  after={(r['id'],*p) for r in self.r['records'] for p in r['remaining_source_pairs'] if r['id']!=v.LABEL and p[0]==eid}
  self.assertTrue(before);self.assertEqual(before,after)
 def test_unaffected_labels_exact(self):
  for old in self.s['records']:
   if old['id']==v.LABEL:continue
   new=next(r for r in self.r['records'] if r['id']==old['id'])
   self.assertEqual(old['remaining_source_pairs'],new['remaining_source_pairs'])
 def test_cdf_exact(self):
  eid=v.accounting.identify(self.c,{'coefficients':[0,0,1,1,0,1,0,0],'blocks':v.accounting.decode([0,0,1,1,0,1,0,0])})
  old=next(r for r in self.s['records'] if r['id']==v.LABEL);new=next(r for r in self.r['records'] if r['id']==v.LABEL)
  self.assertEqual([p for p in old['remaining_source_pairs'] if p[0]==eid],new['remaining_source_pairs']);self.assertEqual(len(new['remaining_source_pairs']),32)
 def test_boundary_preserved(self):self.assertEqual(self.r['boundary'],self.s['boundary'])
 def test_missing_scope(self):
  for i in range(len(v.SCOPE)):
   with self.assertRaises(ValueError):v.build(self.s,self.c,self.p,scope=v.SCOPE[:i]+v.SCOPE[i+1:])
 def test_extra_scope(self):
  with self.assertRaises(ValueError):v.build(self.s,self.c,self.p,scope=v.SCOPE+['invented'])
 def test_wrong_tuple(self):
  with self.assertRaises(ValueError):v.build(self.s,self.c,self.p,target=[0,0,1,1,0,1,0,0])
 def test_reapply(self):
  with self.assertRaises(ValueError):v.build(self.r,self.c,self.p)
 def test_wrong_checkpoint(self):
  s=deepcopy(self.s);s['checkpoint']='wrong'
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_wrong_predecessor_count(self):
  s=deepcopy(self.s);s['pair_accounting']['remaining_necessary_pairs']=147
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_duplicate_pair_count_preserved(self):
  s=deepcopy(self.s);r=s['records'][0];r['remaining_source_pairs'][1]=r['remaining_source_pairs'][0]
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_duplicate_label(self):
  s=deepcopy(self.s);s['remaining_ids'][1]=s['remaining_ids'][0]
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_wrong_endpoint(self):
  for key in ['A','B']:
   s=deepcopy(self.s);next(r for r in s['records'] if r['id']==v.LABEL)[key][0][0]+=1
   with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_fabricated_pair_id_count_preserved(self):
  s=deepcopy(self.s);r=next(r for r in s['records'] if r['id']==v.LABEL);r['remaining_source_pairs'][0][1]='fabricated'
  with self.assertRaises(ValueError):v.build(s,self.c,self.p)
 def test_missing_catalog_identity(self):
  eid=self.r['new_source_edge_exclusion_ledger'][0]['matched_local_E_id']
  with self.assertRaises(ValueError):v.build(self.s,[x for x in self.c if x['id']!=eid],self.p)
 def test_ambiguous_catalog_identity(self):
  eid=self.r['new_source_edge_exclusion_ledger'][0]['matched_local_E_id'];c=deepcopy(self.c);extra=deepcopy(next(x for x in c if x['id']==eid));extra['id']='duplicate-definition';c.append(extra)
  with self.assertRaises(ValueError):v.build(self.s,c,self.p)
 def test_catalog_order_irrelevant(self):self.assertEqual(v.build(self.s,list(reversed(self.c)),self.p),self.r)
 def test_historical_snapshot_untouched(self):
  s,c,p=v.load_inputs();self.assertEqual(s,self.s);self.assertEqual(s['pair_accounting']['remaining_necessary_pairs'],146)
 def test_baseline(self):self.assertEqual(self.r['fixed_campaign805_comparison'],dict(baseline_labels=17,remaining_labels=3,labels_removed=14,baseline_necessary_pairs=1790,remaining_necessary_pairs=114,necessary_pairs_removed=1676))
 def test_scope_not_solution(self):self.assertIn('no actual-instance or formal-proof claim',self.r['scope'])

if __name__=='__main__':unittest.main()
