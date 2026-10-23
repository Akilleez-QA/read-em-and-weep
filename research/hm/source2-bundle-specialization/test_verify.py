import unittest
from unittest.mock import patch
from copy import deepcopy
import verify as v
class Tests(unittest.TestCase):
 def setUp(self):self.a=deepcopy(v.load())
 def reject(self):
  with self.assertRaises(ValueError):v.build(*self.a)
 def test_manifest_tamper(self):
  with patch.object(v,'MANIFEST_SHA256','0'*64):
   with self.assertRaises(ValueError):v.load()
 def test_result(self):
  r=v.build(*self.a);self.assertEqual(r['pair_accounting'],{'before':114,'removed':77,'after':37});self.assertEqual(r['source2']['matched_pair'],[13,21]);self.assertFalse(r['source2_excluded'])
 def test_output_partition(self):
  r=v.build(*self.a)
  for row in r['records']:
   self.assertEqual(row['input_necessary_pair_count'],row['remaining_source_pair_count']+row['removed_pair_count'])
   self.assertEqual(row['removed_pair_count'],len(row['removed_source_pairs']))
   self.assertFalse(set(map(tuple,row['removed_source_pairs'])) & set(map(tuple,row['remaining_source_pairs'])))
  row=next(x for x in r['records'] if x['id']==v.LABEL)
  self.assertEqual(set(map(tuple,row['removed_source_pairs'])),set(map(tuple,r['source2']['E_mismatch_removed']+r['source2']['Qstar_mismatch_removed'])))
 def test_input_partition_corrupt(self):
  self.a[0]['records'][0]['removed_pair_count']+=1;self.reject()
 def test_unaffected(self):
  r=v.build(*self.a)
  for old,new in zip(self.a[0]['records'],r['records']):
   if old['id']!=v.LABEL:self.assertEqual(old,new)
 def test_no_input_mutation(self):
  old=deepcopy(self.a);v.build(*self.a);self.assertEqual(old,self.a)
 def test_e_reindex(self):
  s,c,o=self.a;m={r['id']:100+r['id'] for r in c['E_catalog']}
  for r in c['E_catalog']:r['id']=m[r['id']]
  for r in s['records']:r['remaining_source_pairs']=[[m[e],q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,o)['source2']['matched_pair'],[113,21])
 def test_q_reindex(self):
  s,c,o=self.a;n=len(c['Q_catalog']);c['Q_catalog'].reverse()
  for r in s['records']:r['remaining_source_pairs']=[[e,n-1-q] for e,q in r['remaining_source_pairs']]
  self.assertEqual(v.build(s,c,o)['source2']['matched_pair'],[13,n-22])
 def test_block_order(self):
  for r in self.a[1]['E_catalog']:r['blocks'].reverse()
  for r in self.a[1]['Q_catalog']:r.reverse()
  self.assertEqual(v.build(*self.a)['pair_accounting']['after'],37)
 def test_wrong_source_index(self):
  next(r for r in self.a[2]['cases'] if r['id']==v.LABEL)['source_index']=127;self.reject()
 def test_wrong_profile(self):
  next(r for r in self.a[2]['cases'] if r['id']==v.LABEL)['profile']='11';self.reject()
 def test_wrong_endpoint(self):
  next(r for r in self.a[0]['records'] if r['id']==v.LABEL)['A'][0][0]-=1;self.reject()
 def test_duplicate_pair(self):
  r=self.a[0]['records'][0];r['remaining_source_pairs'].append(r['remaining_source_pairs'][0]);r['remaining_source_pair_count']+=1;self.reject()
 def test_missing_pair(self):
  r=next(r for r in self.a[0]['records'] if r['id']==v.LABEL);r['remaining_source_pairs'].remove([13,21]);r['remaining_source_pair_count']-=1;self.reject()
 def test_wrong_e_tuple(self):
  self.a[1]['E_catalog'][13]['coefficients'][1]=0;self.reject()
 def test_duplicate_e_match(self):
  self.a[1]['E_catalog'].append(deepcopy(self.a[1]['E_catalog'][13]));self.reject()
 def test_duplicate_q_match(self):
  self.a[1]['Q_catalog'].append(deepcopy(self.a[1]['Q_catalog'][21]));self.reject()
 def test_wrong_orientation(self):
  with self.assertRaises(ValueError):v.build(*self.a,qb=[[-d,r] for d,r in v.QB])
 def test_missing_scope(self):
  for i in range(len(v.GATES)):
   with self.assertRaises(ValueError):v.build(*self.a,gates=v.GATES[:i]+v.GATES[i+1:])
 def test_wrong_snapshot(self):
  self.a[0]['checkpoint']='whole-label-through911';self.reject()
 def test_wrong_pair_type(self):
  self.a[0]['records'][0]['remaining_source_pairs'][0][0]=True;self.reject()
if __name__=='__main__':unittest.main()
