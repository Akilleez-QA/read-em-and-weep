#!/usr/bin/env python3
import sys
if not __debug__:raise SystemExit(2)
import unittest
import traverse_selected_scalar_demand as m
class IndependentSelectedDemandAudit(unittest.TestCase):
 def test_frame_and_signs(self):
  nodes=m.build()['nodes'];fs=[n for n in nodes if n['op']=='rank2_frame_conversion']
  self.assertEqual([(n['owner'],n['entry'],n['factor']) for n in fs],[('a',[1,0],'nu(a)^2'),('a',[0,0],'1')])
  self.assertEqual([n['coefficient'] for n in nodes if n['op']=='owned_weighted_coefficient'],[1,1])
  for n in nodes:
   if n['op']=='source_leaf':
    self.assertIs(n['pointwise_nu_normalization'],False)
    if n['name'].startswith(('M0','k_','current_')):self.assertEqual(n['source_frame'],'true-physical-unnormalized-line-constants')
 def test_homogeneous_degrees_and_E_signs(self):
  # Integer exponent support only; no source polynomial multiplication.
  a_terms=[(0,3,0,0,1),(1,1,0,2,0)]
  b_terms=[(2,3,0,0,0),(1,1,2,1,0)]
  self.assertEqual([sum(t)-5 for t in a_terms],[-1,-1])
  self.assertEqual([sum(t)-5 for t in b_terms],[0,0])
  nodes=m.build()['nodes']
  kernels=[n for n in nodes if n.get('name')=='selector_homogeneous']
  self.assertEqual([n['expression'] for n in kernels],['2*v1*(v1^2*v4+v0*v3^2)/h1','2*v0*v1*(v0*v1^2+v2^2*v3)/h1'])
  self.assertEqual([n['homogeneous_weight'] for n in kernels],[-1,0])
  es=[n for n in nodes if n['op']=='multiply' and 'coefficient' in n]
  self.assertEqual([n['coefficient'] for n in es],[[1,2],[-1,2],[1,2],[-1,2]]*4)
  for n in es:
   current,derivative=(nodes[i] for i in n['inputs'])
   self.assertEqual(derivative['coefficient_pullback'],{'requested':'xi','input':'eta=xi+unit(d)','factor':'xi[d]+1'})
 def test_wrong_frame_and_double_normalization(self):
  for mutation in ('already_bare','normalized_jets','double_nu','missing_nu','wrong_owner'):
   d=m.build();f=next(n for n in d['nodes'] if n['op']=='rank2_frame_conversion');l=next(n for n in d['nodes'] if n['op']=='source_leaf' and n['name'].startswith('M0'))
   if mutation=='already_bare':l['source_frame']='bare-carrier-rank2'
   if mutation=='normalized_jets':l['pointwise_nu_normalization']=True
   if mutation=='double_nu':f['factor']='nu(a)^4'
   if mutation=='missing_nu':f['factor']='1'
   if mutation=='wrong_owner':f['owner']='b'
   with self.subTest(mutation=mutation),self.assertRaises(m.ContractError):m.validate(d)
 def test_exact_ahs_families(self):
  self.assertEqual(m.ah_paths((3,11),(2,3)),[])
  cases=[((3,11),(0,1),[[0,'eq',-1],[1,'ge',0]]),((11,15),(0,1),[[0,'le',-2]]),((11,15),(2,3),[[0,'le',-1]])]
  for edge,pair,guard in cases:
   paths=m.ah_paths(edge,pair)
   self.assertEqual([p['sign'] for p in paths],[1,-1]);self.assertEqual([p['standard'] for p in paths],[[3,11,15],[3,7,15]])
   self.assertTrue(all(p['eta_guards']==guard and p['cell']=='CCBB' for p in paths))
 def test_blocked_rational_branches(self):
  d=m.build();self.assertFalse(d['product_budget_pass']);self.assertFalse(d['physical_polynomial_evaluation']);self.assertTrue(d['scope']['uncovered'])
  for n in d['nodes']:
   if n['op']=='derivative_request':self.assertFalse(n['ready']);self.assertEqual(n['required_order'],['cancel_inserted','differentiate_regularized'])
   if n['op']=='Pi_inner_coefficient_family':self.assertEqual(n['state'],'blocked_until_exact_quotient')
if __name__=='__main__':unittest.main(verbosity=2)
