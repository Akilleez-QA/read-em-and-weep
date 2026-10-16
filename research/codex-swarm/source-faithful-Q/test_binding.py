"""Coefficient-free actual metadata and explicit artificial coefficient controls."""
import unittest,json
from fractions import Fraction
import q_binding as B

def owner(c=5,m=0,t=15,occ='u'):return B.I.FullOwner(12,('inserted',occ),c,m,t)
def toy():
 C=lambda n:{(0,0,0,0):n}
 return B.QH.ArtificialCatalog([C(1)]*5,[C(3)]*5,C(5),[C(1),C(2),C(0),C(0),C(0)])

class Controls(unittest.TestCase):
 def test_actual_fixed_definition_and_owned_clearings(self):
  api=B.ActualQBinding();o=owner(5,5,9);d=api.describe(o,(2,3))
  self.assertEqual(d['owner'],o.data());self.assertEqual(d['parameters']['N'],14)
  self.assertEqual(d['owned_degree'],(56,56,59,57))
  self.assertEqual(d['finite_frame_shift'],(-56,0,0,-57))
  self.assertEqual([f['owner']for f in d['C_ledger']],[o.data()]*3)
  self.assertEqual([f['power']for f in d['C_ledger']],[14,1,1])
  self.assertFalse(d['physical_admission']);json.dumps(d)
 def test_every_standard_chart_literal_catalog_matches(self):
  # Only expression node IDs are compared; no physical coefficient is requested.
  for t in range(16):
   R=B.QH.FiniteRing('physical',B.QH.Budget());bits=tuple((t>>(3-i))&1 for i in range(4))
   self.assertEqual(B.QH.ActualCatalog().bind(R,bits),B.local_reference(R,bits))
 def test_always_refuse_even_structural_zero(self):
  api=B.ActualQBinding();o=owner(4,1,0) # unavailable carrier and finite-mask zero
  for e in((0,0,0,0),(-1,0,0,0)):
   with self.assertRaises(B.I.PhysicalAdmissionMissing):api.coefficient(o,e)
  with self.assertRaises(B.I.PhysicalAdmissionMissing):api.factor_terms(o)
  C=B.ClearingDefinition(o,(0,1))
  with self.assertRaises(B.I.PhysicalAdmissionMissing):C.coefficient((-1,0,0,0))
  # Mutable metadata labels cannot turn an actual wrapper into a synthetic capability.
  api.mode=C.mode='synthetic'
  with self.assertRaises(B.I.PhysicalAdmissionMissing):api.coefficient(o,(0,0,0,0))
  with self.assertRaises(B.I.PhysicalAdmissionMissing):api.factor_terms(o)
  with self.assertRaises(B.I.PhysicalAdmissionMissing):C.coefficient((0,0,0,0))
  bound=B.ActualQuotientBinding(o);bound.mode='synthetic'
  with self.assertRaises(B.I.PhysicalAdmissionMissing):bound.coefficient((0,0,0,0))
  with self.assertRaises(B.I.PhysicalAdmissionMissing):bound.factor_terms(o)
 def test_exact_owner_pair_and_no_injected_actual_catalog(self):
  with self.assertRaises(ValueError):B.ActualQBinding().describe(owner(),(False,True))
  with self.assertRaises(ValueError):B.ArtificialBinding(owner(),B.QH.ActualCatalog())
  P=B.ArtificialBinding(owner(0,0,0),toy(),N=2)
  self.assertEqual(P.coefficient((0,0,0,0)),18)
  with self.assertRaises(ValueError):P.factor_terms(owner(0,0,0,'v'))
  with self.assertRaises(ValueError):P.factor_terms(P.owner,(2,3))
 def test_divisor_frame_monomial_law_artificial(self):
  # Formal homogeneous monomial X^a Y^(c-a) at degree c.
  for c in(1,3,4,5,56,70,73):
   for a in(0,c//2,c):
    local_exponent=c-a
    self.assertEqual(c-local_exponent,a) # x^c C_local(1/x)=C_finite
    for q_local in(0,1,2):
     rho_local=local_exponent+q_local
     qhat_exp=-c-q_local
     self.assertEqual(a+qhat_exp,-rho_local) # C_finite Qhat=rho
 def test_bit_encodings_and_pair_degrees(self):
  for t in range(16):
   o=owner(1,2,t)
   for p in((0,1),(2,3)):
    c=B.degree(o,p)
    self.assertEqual(c,tuple(70+(3 if i==1 else 1)if i in p else 70 for i in range(4)))
  with self.assertRaises(ValueError):B.pair((1,0))

if __name__=='__main__':unittest.main()
