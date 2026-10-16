import unittest,copy
from collections import Counter
import traverse_selected_scalar_demand as m
class Tests(unittest.TestCase):
 def test_edges(self):
  self.assertEqual(m.triangles((3,11)),[]);self.assertEqual(m.triangles((11,15)),[])
 def test_h_chart_pruning(self):
  self.assertEqual(m.ah_paths((3,11),(2,3)),[])
  self.assertEqual(len(m.ah_paths((11,15),(2,3))),2)
  self.assertEqual(len(m.ah_paths((3,11),(0,1))),2)
  self.assertEqual(len(m.ah_paths((11,15),(0,1))),2)
 def test_exact_guards(self):
  p=m.ah_paths((3,11),(0,1))
  self.assertEqual(p[0]['eta_guards'],[[0,'eq',-1],[1,'ge',0]])
  self.assertEqual([x['sign'] for x in p],[1,-1])
  q=m.ah_paths((11,15),(2,3))
  self.assertEqual(q[0]['eta_guards'],[[0,'le',-1]])
  self.assertEqual([x['standard'] for x in q],[[3,11,15],[3,7,15]])
 def test_dag(self):
  d=m.validate(m.build());self.assertLess(len(m.encode(d)),65536)
  ns=d['nodes'];self.assertEqual(sum(x['op']=='T_edge' for x in ns),16)
  self.assertEqual(sum(x['op']=='Pi_inner_coefficient_family' for x in ns),24)
  self.assertTrue(all(x['K_survivors']==0 for x in ns if x['op']=='T_edge'))
 def test_no_unearned_readiness(self):
  d=m.build()
  for n in d['nodes']:
   if n['op']=='derivative_request':self.assertFalse(n['ready'])
  self.assertFalse(d['product_budget_pass'])
 def test_physical_frame(self):
  ns=[n for n in m.build()['nodes'] if n['op']=='rank2_frame_conversion']
  self.assertEqual([n['factor'] for n in ns],['nu(a)^2','1'])
  self.assertEqual([n['entry'] for n in ns],[[1,0],[0,0]])
  leaves=[n for n in m.build()['nodes'] if n['op']=='source_leaf']
  self.assertTrue(all(n['pointwise_nu_normalization'] is False for n in leaves))
 def test_homogeneous_selector(self):
  ns=[n for n in m.build()['nodes'] if n.get('name')=='selector_homogeneous']
  self.assertEqual([n['homogeneous_weight'] for n in ns],[-1,0])
  self.assertTrue(all(n['coefficient']==1 for n in m.build()['nodes'] if n['op']=='owned_weighted_coefficient'))
 def test_mutations(self):
  for kind in range(5):
   d=m.build()
   if kind==0:d['unresolved']=[]
   if kind==1:d['scope']['tail_carriers_may_repeat']=False
   if kind==2:next(n for n in d['nodes'] if n['op']=='derivative_request')['ready']=True
   if kind==3:next(n for n in d['nodes'] if n['op']=='owned_weighted_coefficient')['outer_partition']=['inner',14,1]
   if kind==4:d['scope']['orientation']=True
   with self.assertRaises(m.ContractError):m.validate(d)
if __name__=='__main__':unittest.main()
