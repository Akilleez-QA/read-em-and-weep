"""Artificial base polynomials only. Actual metadata is never evaluated."""
import unittest,math
from fractions import Fraction as Q
from quotient import *

def C(n):return{ZERO:n}
def catalog():return ArtificialCatalog([C(1)for _ in range(5)],[C(3)for _ in range(5)],C(5),[C(1),C(2),C(0),C(0),C(0)])
def owner(c=0,m=0,t=0):return FullOwner(12,('quotient','u'),c,m,t)

class Controls(unittest.TestCase):
 def test_first_hit_exact_disjoint_domains(self):
  R=FiniteRing('synthetic',Budget());cs=[R.const(-2),R.const(1)];vs=[R.const(1)]*2
  b=[R.first_hit(cs,vs,j,5,9)for j in range(2)]
  expected0=sum(math.comb(9,n)*(-2)**n for n in range(5,10))
  expected1=sum(math.comb(9,n)*(-2)**n for n in range(5))
  self.assertEqual(R.coefficient(b[0],ZERO),expected0)
  self.assertEqual(R.coefficient(b[1],ZERO),expected1)
  self.assertEqual(sum(R.coefficient(x,ZERO)for x in b),-1)
 def test_cbar_dbar_endpoint_ranges(self):
  # N2: Cbar=3*(v2*a)+h=18; Dbar=v2^3*a+3*h*v2^2=14.
  self.assertEqual(QuotientProgram(owner(),catalog(),N=2).coefficient(ZERO),18)
  self.assertEqual(QuotientProgram(owner(5),catalog(),N=2).coefficient(ZERO),14)
 def test_polynomial_convolution_and_no_truncation(self):
  R=FiniteRing('synthetic',Budget());x=R.x(0);b=R.first_hit([R.plus(R.const(1),x)],[R.const(1)],0,5,5)
  for k in range(6):self.assertEqual(R.coefficient(b,(k,0,0,0)),math.comb(5,k))
  self.assertEqual(R.coefficient(b,(6,0,0,0)),0)
 def test_owner_frame_reversal_and_pair_line(self):
  P=QuotientProgram(owner(0,0,8),catalog(),N=1)
  b0=sum(math.comb(9,n)*(-2)**n for n in range(5,10))
  self.assertEqual(P.shift,(-6,0,0,0))
  self.assertEqual(P.coefficient((-7,0,0,0)),b0)
  self.assertEqual(P.coefficient((-6,0,0,0)),0)
  self.assertEqual(P.factor_terms(P.owner),(((-7,0,0,0),Q(b0)),))
  with self.assertRaises(ValueError):P.factor_terms(owner(0,0,9))
  # For complementary axis, raw legal mask0 is t^2, no pair-line shift.
  P34=QuotientProgram(owner(0,0,8),catalog(),N=1,pair=(2,3))
  self.assertEqual(P34.shift,(-5,0,0,0));self.assertEqual(P34.coefficient((-7,0,0,0)),b0)
  Pbit=QuotientProgram(owner(0,1,8),catalog(),N=1,pair=(2,3))
  self.assertEqual(Pbit.coefficient((-5,0,0,0)),b0)
  self.assertEqual(Pbit.coefficient((-7,0,0,0)),-b0)
  Ppair=QuotientProgram(owner(0,1,8),catalog(),N=1)
  self.assertEqual(Ppair.shift,(-8,0,0,0));self.assertEqual(Ppair.coefficient((-8,0,0,0)),b0)
 def test_zero_finite_mask_and_unavailable_carrier(self):
  self.assertEqual(QuotientProgram(owner(0,1,0),catalog(),N=1).coefficient(ZERO),0)
  self.assertEqual(QuotientProgram(owner(1,0,0),catalog(),N=1).coefficient(ZERO),0)
 def test_actual_n14_metadata_refuses_all_coefficient_paths(self):
  P=QuotientProgram(owner(5,15,15),ActualCatalog())
  self.assertEqual(P.parameters,{'N':14,'M':27,'T':135,'L':671,'s':4,'legal_power':1})
  self.assertIsNotNone(P.support_box())
  for e in(ZERO,(-100000,0,0,0)):
   with self.assertRaises(Exception)as ctx:P.coefficient(e)
   self.assertEqual(type(ctx.exception).__name__,'PhysicalAdmissionMissing')
  with self.assertRaises(Exception)as ctx:P.factor_terms(P.owner)
  self.assertEqual(type(ctx.exception).__name__,'PhysicalAdmissionMissing')
  with self.assertRaises(ValueError):QuotientProgram(owner(),catalog(),N=14)
 def test_caps_abort_and_aggregate_state(self):
  R=FiniteRing('synthetic',Budget());R.max_index_visits=1
  b=R.first_hit([R.const(1)],[R.const(1)],0,5,5)
  with self.assertRaises(ValueError):R.coefficient(b,ZERO)
  self.assertGreater(R.index_visits,1)
  with self.assertRaises(ValueError):QuotientProgram(owner(),catalog(),N=True)

if __name__=='__main__':unittest.main()
