import unittest
from copy import deepcopy
import verify as v
class Tests(unittest.TestCase):
 def setUp(self):self.x=v.load()
 def reject(self,f):
  f(self.x)
  with self.assertRaises(ValueError):v.compose(*self.x)
 def test_accounting(self):self.assertEqual(v.compose(*self.x)['pair_accounting'],{'before':6,'removed':2,'after':4})
 def test_profile_drift(self):self.reject(lambda x:x[0].update(profile_counts={'11':1,'12':1,'21':1}))
 def test_label_drift(self):self.reject(lambda x:x[0]['records'][1].update(id='unrelated'))
 def test_duplicate_cut(self):self.reject(lambda x:x[1]['removed_pairs'].append([10,231]))
 def test_wrong_cut(self):self.reject(lambda x:x[1].update(removed_pairs=[[10,129],[10,249]]))
 def test_missing_cut(self):self.reject(lambda x:x[1]['removed_pairs'].pop())
 def test_extra_survivor(self):self.reject(lambda x:x[1]['retained_pairs'].append([10,231]))
 def test_scope(self):self.reject(lambda x:x[1].update(stable_label='G3.21.d610e381ed75'))
 def test_label_claim(self):self.reject(lambda x:x[1].update(labels_removed=1))
 def test_template(self):self.reject(lambda x:x[1]['template_assignment'].update(III=249))
 def test_ambiguous_e(self):self.reject(lambda x:x[2]['E_catalog'].append(deepcopy(x[2]['E_catalog'][10])))
 def test_ambiguous_q(self):self.reject(lambda x:x[2]['Q_catalog'].append(deepcopy(v.Q[0])))
 def test_wrong_orientation(self):self.reject(lambda x:x[2]['Q_catalog'].__setitem__(129,[[-d,r] for d,r in v.Q[0]]))
 def test_multiset(self):self.reject(lambda x:x[2]['E_catalog'][10]['blocks'].remove([-2,'D']))
 def test_duplicate_row(self):self.reject(lambda x:x[0]['records'].append(deepcopy(x[0]['records'][0])))
 def test_duplicate_pair(self):self.reject(lambda x:x[0]['records'][0]['remaining_source_pairs'].append([10,129]))
 def test_double_apply(self):
  out=v.compose(*self.x)
  with self.assertRaises(ValueError):v.compose(out,*self.x[1:])
 def test_semantic_transport(self):
  s,r,c=self.x;n=len(c['Q_catalog']); em={e['id']:1000+e['id'] for e in c['E_catalog']};qm={i:n-1-i for i in range(n)}
  def trans(p):return [em[p[0]],qm[p[1]]]
  for row in s['records']:row['remaining_source_pairs']=[trans(p) for p in row['remaining_source_pairs']]
  for key in ['starting_pairs','retained_pairs','removed_pairs']:r[key]=[trans(p) for p in r[key]]
  r['template_assignment']={k:qm[q] for k,q in r['template_assignment'].items()}
  for e in c['E_catalog']:e['id']=em[e['id']];e['blocks'].reverse()
  c['Q_catalog'].reverse()
  for q in c['Q_catalog']:q.reverse()
  out=v.compose(s,r,c);self.assertEqual(out['pair_accounting']['after'],4)
 def test_unrelated_unchanged(self):
  out=v.compose(*self.x)
  for old in self.x[0]['records']:
   if old['id']!=v.LABEL:self.assertIn(old,out['records'])
if __name__=='__main__':unittest.main()
