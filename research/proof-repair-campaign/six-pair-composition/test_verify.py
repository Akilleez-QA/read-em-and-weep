import unittest
from copy import deepcopy
import verify as v
class CompositionTests(unittest.TestCase):
 def setUp(self):self.x=v.load()
 def reject(self,fn):
  fn(self.x)
  with self.assertRaises(ValueError):v.compose(*self.x)
 def test_replay(self):self.assertEqual(v.compose(*self.x)['pair_accounting']['after'],6)
 def test_duplicate_pair(self):self.reject(lambda x:x[1]['records'][0]['remaining_source_pairs'].append([10,129]))
 def test_duplicate_label(self):self.reject(lambda x:x[0]['records'].append(deepcopy(x[0]['records'][0])))
 def test_wrong_scope(self):self.reject(lambda x:x[2].update(label=v.S))
 def test_wrong_tuple(self):self.reject(lambda x:x[2].update(source_tuple=[1]*8))
 def test_wrong_orientation(self):self.reject(lambda x:x[2].update(quotient_dual_blocks=[[-a,b] for a,b in x[2]['quotient_dual_blocks']]))
 def test_duplicate_cut(self):self.reject(lambda x:x[2]['removed_pairs'].append(x[2]['removed_pairs'][0]))
 def test_missing_cut(self):self.reject(lambda x:x[2]['removed_pairs'].pop())
 def test_wrong_cut(self):self.reject(lambda x:x[2]['removed_pairs'].__setitem__(0,[14,148]))
 def test_wrong_keep(self):self.reject(lambda x:x[2].update(kept_pairs=[[14,18]]))
 def test_wrong_numeric_id(self):self.reject(lambda x:x[2].update(Q_catalog_id=18))
 def test_duplicate_semantics(self):self.reject(lambda x:x[3]['Q_catalog'].append(deepcopy(x[2]['quotient_dual_blocks'])))
 def test_unrelated_endpoint(self):self.reject(lambda x:x[1]['records'][0]['A'].append([0,'one']))
 def test_unrelated_pair(self):self.reject(lambda x:x[1]['records'][0]['remaining_source_pairs'].__setitem__(0,[10,130]))
 def test_noninteger_id(self):self.reject(lambda x:x[1]['records'][0]['remaining_source_pairs'].__setitem__(0,[True,129]))
 def test_double_apply(self):
  out=v.compose(*self.x);self.x[1]['records']=out['records']
  with self.assertRaises(ValueError):v.compose(*self.x)
 def test_semantic_reindex(self):
  x=self.x;n=len(x[3]['Q_catalog']);emap={e['id']:e['id']+1000 for e in x[3]['E_catalog']};qmap={q:n-q-1 for q in range(n)}
  def pair(p):return [emap[p[0]],qmap[p[1]]]
  for snap in x[:2]:
   for row in snap['records']:row['remaining_source_pairs']=[pair(p) for p in row['remaining_source_pairs']]
  x[1]['source2']['matched_pair']=pair(x[1]['source2']['matched_pair'])
  for key in ['kept_pairs','removed_pairs']:x[2][key]=[pair(p) for p in x[2][key]]
  x[2]['E_catalog_id']=emap[x[2]['E_catalog_id']];x[2]['Q_catalog_id']=qmap[x[2]['Q_catalog_id']]
  for e in x[3]['E_catalog']:e['id']=emap[e['id']];e['blocks'].reverse()
  x[3]['Q_catalog'].reverse()
  for q in x[3]['Q_catalog']:q.reverse()
  out=v.compose(*x);self.assertEqual(out['pair_accounting']['after'],6)
 def test_multiset_not_set(self):
  self.assertNotEqual(v.canon([[-1,'T']]),v.canon([[-1,'T'],[-1,'T']]))
if __name__=='__main__':unittest.main()
