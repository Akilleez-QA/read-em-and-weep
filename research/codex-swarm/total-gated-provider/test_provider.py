"""TP01 pure normalization, metadata and explicit toy controls."""
import unittest,itertools,json
from fractions import Fraction
from dataclasses import FrozenInstanceError
from unittest.mock import patch
import provider as P
Z=(0,0,0,0)
def o(c,m,t,j):return P.I.FullOwner(12,('slot',j),c,m,t)

class Controls(unittest.TestCase):
 def test_raw_row_end_frame_route_and_noncommuting_control(self):
  a,b,c=o(0,0,0,0),o(1,1,8,1),o(4,15,15,2)
  plan=P.request_plan('Rsharp',(b,a,c));route=plan.describe()['frame_plan']
  self.assertEqual(route['transport'],'ordered_conjugation')
  self.assertEqual(route['original_first_owner'],b.data())
  self.assertEqual(route['canonical_first_owner'],a.data())
  self.assertEqual(route['parity'],-1)
  self.assertEqual(route['transition']['ordered_edge_request'],(b.data(),a.data()))
  self.assertEqual(route['ordered_actions'],['inverse(g(original_first,canonical_first))','X_canonical','g(original_first,canonical_first)'])
  # Independent artificial rational matrices: g^-1 X g != X.
  mat=lambda rows:tuple(tuple(Fraction(v)for v in row)for row in rows)
  mul=lambda A,B:tuple(tuple(sum(A[i][k]*B[k][j]for k in range(2))for j in range(2))for i in range(2))
  g=mat([[1,1],[0,1]]);gi=mat([[1,-1],[0,1]]);X=mat([[1,0],[0,-1]])
  transported=mul(mul(gi,X),g)
  self.assertEqual(transported,mat([[1,2],[0,-1]]));self.assertNotEqual(transported,X)
  self.assertEqual(tuple(tuple(-v for v in row)for row in transported),mat([[-1,-2],[0,1]]))
  self.assertEqual(P.frame_plan(P.request_plan('Rsharp',(a,c,b)))['transport'],'identity')
  self.assertEqual(P.frame_plan(P.request_plan('Rsharp',()))['empty_tuple_has_no_base_owner'],True)
  zero=P.frame_plan(P.request_plan('Rsharp',(b,a,a)))
  self.assertTrue(zero['zero_plan_requires_no_transport_evaluation']);self.assertFalse(zero['physical_transport_evaluated'])
  for k in('F','T'):
   route=P.frame_plan(P.request_plan(k,(b,a,c)))
   self.assertEqual(route['value_frame'],'common_finite_fixed_frame');self.assertEqual(route['coefficient_type'],'scalar')
  self.assertEqual(P.ToyProvider.coefficient_scope,'scalar_fixture_only')
  samephysical=(o(1,2,8,0),o(1,2,0,1),c)
  self.assertNotEqual(P.request_plan('Rsharp',samephysical).effective_sign,0)
  self.assertEqual(P.frame_plan(P.request_plan('Rsharp',samephysical))['transport'],'ordered_conjugation')
 def test_common_vs_source_repetition(self):
  a=o(1,2,0,0);b=o(1,2,8,1);c=o(4,15,15,2)
  self.assertEqual(P.request_plan('F',(a,b,c)).zero_reason,'source_F_repeated_physical')
  for kind in('T','Rsharp'):
   plan=P.request_plan(kind,(a,b,c));self.assertNotEqual(plan.effective_sign,0)
   self.assertTrue(plan.repeated_physical)
   self.assertEqual(P.request_plan(kind,(a,a,c)).zero_reason,'repeated_common')
 def test_all_permutations_one_sign_and_original_owner_retention(self):
  owners=(o(5,0,0,0),o(1,2,8,1),o(4,15,15,2))
  for perm in itertools.permutations(range(3)):
   raw=tuple(owners[j]for j in perm);plan=P.request_plan('F',raw)
   expected=(-1)**sum(perm[i]>perm[j]for i in range(3)for j in range(i+1,3))
   self.assertEqual(plan.effective_sign,expected);self.assertEqual(plan.sorted_owners,owners)
   self.assertEqual(plan.owners,raw)
   with self.assertRaises(FrozenInstanceError):plan.effective_sign=7
  with self.assertRaises(FrozenInstanceError):owners[0].legal_mask=1
 def test_lazy96_descriptor_without_actual_iteration(self):
  D=P.Full96Descriptor(12,['inserted','u'],9)
  self.assertEqual(D.describe()['cardinality'],96)
  self.assertEqual(D.label_plan(0),(12,('inserted','u'),0,0,9))
  self.assertEqual(D.label_plan(95),(12,('inserted','u'),5,15,9))
  for bad in(-1,96,True):
   with self.assertRaises(ValueError):D.label_plan(bad)
  with self.assertRaises(P.I.PhysicalAdmissionMissing):iter(D)
  with self.assertRaises(P.I.PhysicalAdmissionMissing):D.owners()
 def test_explicit_toy_provider_zero_scope_and_alternation(self):
  a=o(1,2,0,0);b=o(1,2,8,1);c=o(4,15,15,2);owners=(a,b,c)
  key=lambda k:(k,tuple(x.common_key for x in owners),Z,(0,1))
  toy=P.ToyProvider({key('T'):7,key('Rsharp'):11},{0:[a],8:[b]})
  self.assertEqual(toy.coefficient('F',owners,Z),0)
  self.assertEqual(toy.coefficient('T',owners,Z),7)
  self.assertEqual(toy.coefficient('T',(b,a,c),Z),-7)
  self.assertEqual(toy.coefficient('Rsharp',owners,Z),11)
  self.assertEqual(toy.coefficient('T',(a,a,c),Z),0)
  self.assertEqual(tuple(toy.owners(0)),(a,))
  with self.assertRaises(ValueError):tuple(toy.owners(15))
 def test_actual_gate_precedes_every_zero_support_or_validation(self):
  actual=P.ActualProvider();actual.mode='synthetic'
  with patch.object(P,'request_plan',side_effect=AssertionError('gate was bypassed')):
   for method in(actual.coefficient,actual.alternating_coefficient,actual.factor_terms,actual.owners):
    with self.assertRaises(P.I.PhysicalAdmissionMissing):method('F',(),(-999,0,0,0))
 def test_canonical_repository_rejected_before_auth(self):
  with patch.object(P,'_authenticate',side_effect=AssertionError('auth called')):
   with self.assertRaises(ValueError):P.ActualProvider(P.BASE/'noncanonical')
 def test_actual_definition_join_and_total_degenerate_plans(self):
  actual=P.ActualProvider();owners=(o(5,0,0,0),o(1,2,8,1),o(4,15,15,2))
  d=actual.describe('F',(owners[1],owners[0],owners[2]),(2,3))
  self.assertEqual(d['source_definition']['source_sorting_sign'],-1)
  self.assertEqual(d['source_definition']['source_sorted_owners'],[x.data()for x in owners])
  self.assertFalse(d['physical_admission']);json.dumps(d)
  for raw in((owners[0],)*3,(owners[0],owners[1],o(1,2,15,2))):
   d=actual.describe('F',raw);self.assertEqual(d['effective_sign'],0)
   self.assertEqual(d['definition_join'],'normalization only; no raw source reevaluation')
  self.assertEqual(actual.describe('T',())['effective_sign'],1)
  self.assertEqual(actual.describe('Rsharp',(owners[0],))['effective_sign'],1)
 def test_invalid_owner_fields_and_occurrence_alias_are_explicit(self):
  with self.assertRaises(ValueError):P.I.FullOwner(12,'u',1,True,0)
  with self.assertRaises(ValueError):P.request_plan('F',(),(0,1))
  with self.assertRaises(ValueError):P.request_plan('T',(),(False,True))
  raw=(o(0,0,0,0),o(1,1,8,0),o(2,3,12,2))
  self.assertTrue(P.request_plan('F',raw).occurrence_alias)
  self.assertEqual(P.ActualProvider().describe('F',raw)['definition_join'],'normalization only; no raw source reevaluation')

if __name__=='__main__':unittest.main()
