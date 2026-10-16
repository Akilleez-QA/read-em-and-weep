import unittest
from fractions import Fraction as Q
from unittest.mock import patch
from raw_engine import RF,I,PhysicalModel,Mat,raw_scalar_formula
from artificial import run_artificial,source_constant
import program as P

class Tests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.result=run_artificial()
 def test_full_cancellation(self):
  r=self.result
  self.assertEqual(r['value'],0);self.assertEqual(len(r['rows']),24)
  self.assertTrue(all(a['contribution']for a in r['rows']))
  self.assertTrue(r['complete_staircase_sum']);self.assertFalse(r['physical_source_evaluated'])
 def test_partial_not_complete(self):
  r=run_artificial(staircase_limit=1,weight_scale=2)
  self.assertEqual(r['value'],2*Q(-190793,282920400));self.assertFalse(r['complete_staircase_sum'])
 def test_source_corrections_material(self):
  ex=RF.Execution();r,p=source_constant(ex,labels=(0,1,3))
  self.assertEqual(r,((Q(-1,2),Q(1)),(Q(0),Q(1,2))))
  self.assertEqual(set(p),{'baseline','Fk12','Fk34','E12','E34'})
  for omitted in ('baseline','Fk12','Fk34'):
   self.assertNotEqual(source_constant(ex,omit=omitted,labels=(0,1,3))[0],r)
 def test_incomplete_zero(self):
  self.assertEqual(P.assumed_authenticated_detector_results({30:0}),'UNDECIDED')
  self.assertEqual(P.assumed_authenticated_detector_results({30:Q(1,7)}),'NONZERO')
  self.assertEqual(P.assumed_authenticated_detector_results(dict.fromkeys(range(32),0)),'ZERO')
  with self.assertRaises(ValueError):P.assumed_authenticated_detector_results({True:0})
 def test_physical_refuses_before_arithmetic(self):
  with patch.object(RF,'Execution',side_effect=AssertionError('arithmetic')),patch.object(I,'FullOwner',side_effect=AssertionError('physical owner construction')):
   for f in (lambda:P.actual_route30(),lambda:P._actual_body(None),lambda:PhysicalModel(None,None),lambda:PhysicalModel._build_body(None,None,None),lambda:P.weighted_assignment(None,None,()),lambda:P.outer_weight(None,None),lambda:P.first_hit(None,None,None,0,535,2671),lambda:next(P.potential_owners(0,('t',0)))):
    with self.assertRaises(I.PhysicalAdmissionMissing):f()
 def test_structural_outer_alphabet(self):
  with patch.object(I,'FullOwner',side_effect=AssertionError('physical owner construction')):
   self.assertEqual([P.alphabet_count(t)for t in(0,8,12,14,15)],[2,6,16,40,32])
  self.assertEqual(24*2*6*16*40*32,5898240)
 def test_first_hit_exact_multiplicity(self):
  ex=RF.Execution();one=ex.scalar(1);r=P.first_hit(ex,[one,one],[one,one],0,2,3)
  # n0=2,3 yields binomial3,2+binomial3,3=4.
  self.assertEqual(r.rational_x().laurent_coefficient((0,0,0,0)),4)
 def test_raw_scalar_endpoint_terms(self):
  ex=RF.Execution();M=Mat(ex);one=((ex.scalar(1),),);zero=((ex.scalar(0),),)
  # Four one-dimensional artificial blocks isolate endpoint linear terms.
  ans=raw_scalar_formula(M,([one]*4,[zero]*4),([zero]*4,[zero]*4),ex.scalar(0),ex.scalar(2))
  self.assertEqual(ans.rational_x().laurent_coefficient((0,0,0,0)),-1)

 def test_exact_source_pins(self):
  import bindings
  p=bindings.authenticate();self.assertFalse(p['physical_execution_admitted'])

 def test_corrupt_dependency_rejected(self):
  import bindings
  with patch.object(bindings.Path,'read_bytes',return_value=b'corrupt'):
   with self.assertRaises(ValueError):bindings.authenticate()

if __name__=='__main__':unittest.main()
