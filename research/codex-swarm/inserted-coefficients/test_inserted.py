"""Only artificial catalogs/oracles execute coefficients, including actual153-op topology."""
import unittest
from fractions import Fraction as Q
from pathlib import Path
from interfaces import *
from polynomial_coefficients import *
from source_program import actual_program_definition,ProgramOracle,pair_nodes
from inserted_program import *

class ConstantSource:
 mode='synthetic'
 def __init__(self,budget):self.budget=budget
 def degree_upper(self,owners,pair=(0,1)):return ZERO
 def coefficient(self,owners,e,pair=(0,1)):
  require_synthetic(self.mode);need(tuple(owners)==sorted_source(owners)[0],'sorted SOURCE triple')
  self.budget.debit('queries')
  return Q(int(not any(e)and len({o.physical_key for o in owners})==3))

class Controls(unittest.TestCase):
 def test_exact_elementary_substitution_powers_and_partials(self):
  b=Budget();r=Ring('synthetic',b);e1=r.elementary(1);e2=r.elementary(2)
  self.assertEqual(r.coefficient(e2,(1,1,0,0)),1);self.assertEqual(r.coefficient(e2,(2,0,0,0)),0)
  self.assertEqual(r.coefficient(r.power(e1,2),(1,1,0,0)),2)
  self.assertEqual(r.coefficient(r.partial(r.times(r.power(r.x(0),2),r.x(1)),0),(1,1,0,0)),2)
  self.assertEqual(r.coefficient(r.partial(r.const(7),0),(-1,0,0,0)),0)
 def test_ordered_matrix_products_transpose_trace(self):
  r=Ring('synthetic',Budget());M=lambda a:[[Scalar(r.const(v))for v in row]for row in a]
  A=M([[0,1],[0,0]]);B=M([[0,0],[1,0]])
  AB=times(A,B,r);BA=times(B,A,r)
  self.assertEqual(r.coefficient(AB[0][0].node,ZERO),1);self.assertEqual(r.coefficient(BA[0][0].node,ZERO),0)
 def test_actual_153_topology_under_artificial_identity_catalog(self):
  repo=Path(__file__).resolve().parents[3];definition,actual=actual_program_definition(repo)
  def matrix(rows,cols):return[[[['0,0,0,0',-1]]if i==j and i<2 else[]for j in range(cols)]for i in range(rows)]
  charts=[{'I':matrix(15,2),'P':matrix(2,15)}for _ in range(6)]
  toy=Catalog('synthetic',charts,{c:{ZERO:1}for c in range(6)})
  owners=(FullOwner(12,0,0,0,0),FullOwner(12,1,1,1,8),FullOwner(12,2,2,2,12))
  oracle=ProgramOracle(definition,toy,Budget(max_queries=100000,max_splits=200000))
  expected={ZERO:Q(31,8),(2,0,0,0):Q(-29,8),(0,2,0,0):Q(-29,8),(2,2,0,0):Q(31,8)}
  for e,c in expected.items():self.assertEqual(oracle.coefficient(owners,e),c)
  self.assertEqual(oracle.coefficient(owners,(1,0,0,0)),0)
  # F34 is the raw axis-renamed DAG evaluated on TARGET-sorted owners.
  # No inverse-image F12 sorting is permitted here.
  owners34=tuple(FullOwner(o.seed,o.occurrence,o.carrier,((o.legal_mask&3)<<2)|(o.legal_mask>>2),o.standard_tag)for o in owners)
  for e,c in expected.items():
   self.assertEqual(oracle.coefficient(owners34,(e[2],e[3],e[0],e[1]),(2,3)),c)
  self.assertEqual(pair_nodes(pair_nodes(definition['dag'],(2,3)),(2,3)),definition['dag'])
  # Same real DAG with real catalog can be LOWERED as metadata but NEVER evaluated.
  physical=ProgramOracle(definition,actual,Budget());physical.program(owners)
  with self.assertRaises(PhysicalAdmissionMissing):physical.coefficient(owners,ZERO)
  with self.assertRaises(PhysicalAdmissionMissing):physical.coefficient(owners,(-1,0,0,0))
 def test_missing_physical_frame_or_extension_never_admitted(self):
  o=FullOwner(1,0,1,1,8);w=RegularExtensionWitness('physical','unproved',(8,),(o,),'unproved')
  with self.assertRaises(PhysicalAdmissionMissing):w.require((o,),(8,))
  bad=RegularExtensionWitness('synthetic','toy',(8,),(o,),'toy',scope='common_local_only')
  with self.assertRaises(ValueError):bad.require((o,),(8,))
 def make_combined(self):
  b=Budget();a=FullOwner(12,1,1,1,8);c=FullOwner(12,2,2,3,12)
  prefix=FullOwner(12,0,5,0,0);last=FullOwner(12,3,4,15,15);outer=(prefix,a,c,last)
  context=RequestContext(outer,(prefix,),outer)
  witness=RegularExtensionWitness('synthetic','whole-toy-N',(8,12),(a,c),'exact-toy-polynomial')
  fibers=SyntheticFibers(12,{8:[(3,1)],12:[(4,3)]})
  quotient=SyntheticQuotients({(3,1,8):{ZERO:2},(4,3,12):{ZERO:3}})
  Ca=SparseOracle({ZERO:1,(1,0,0,0):1},b)
  prism=PrismProgram((a,c),ConstantSource(b),quotient,fibers,Ca,(1,0,0,0),witness,b,context)
  N=WholeNumerator(SparseOracle({ZERO:5},b),prism,SparseOracle({ZERO:7},b),((0,0,0,0),(2,0,0,0)))
  return b,a,c,Ca,prism,N
 def test_both_prisms_padding_complete_sum_then_derivative(self):
  b,a,c,Ca,prism,N=self.make_combined()
  self.assertEqual(prism.coefficient('prism1',(1,0,0,0)),2)
  self.assertEqual(prism.coefficient('prism2',(2,0,0,0)),-6)
  self.assertEqual(N.coefficient((1,0,0,0)),31);self.assertEqual(N.coefficient((2,0,0,0)),29)
  derivative=DifferentiatedCombinedNumerator(N,[(a,'toy-f',2,Ca)],0,b)
  self.assertEqual(derivative.coefficient(ZERO),31);self.assertEqual(derivative.coefficient((1,0,0,0)),27)
  self.assertEqual(derivative.coefficient((2,0,0,0)),0)
  with self.assertRaises(ValueError):DifferentiatedCombinedNumerator(prism,[(a,'toy-f',2,Ca)],0,b)
 def test_parity_full_owners_and_prefix_weights(self):
  a=FullOwner(1,0,1,0,8);b=FullOwner(1,1,2,0,12);c=FullOwner(1,2,3,0,15)
  ordered,s=sorted_source((b,a,c));self.assertEqual(ordered,(a,b,c));self.assertEqual(s,-1)
  # Equal carrier does not merge different occurrences or masks.
  aa=FullOwner(1,('inserted','u'),1,1,8);self.assertNotEqual(a,aa)
  budget,a,c,Ca,p,N=self.make_combined()
  with self.assertRaises(ValueError):RequestContext(p.context.outer,p.context.prefix,p.context.outer[1:]).validate((a,c))
 def test_shared_budget_no_reset_and_unknowns(self):
  b=Budget(max_queries=1);o=SparseOracle({ZERO:1},b);self.assertEqual(o.coefficient(ZERO),1)
  with self.assertRaises(ValueError):o.coefficient(ZERO)
  with self.assertRaises(ValueError):FullOwner(1,0,True,0,0)
  with self.assertRaises(ValueError):FullOwner(1,0,1,True,0)
  with self.assertRaises(ValueError):exponent((True,0,0,0))
 def test_standard_endpoint_whole_numerator_integration(self):
  import sys
  sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'standard-coefficients'))
  import standard as S
  self.assertIs(S.I.FullOwner,FullOwner)
  b,a,c,Ca,prism,old=self.make_combined()
  fixture=S.SyntheticStandardCochain({(0,8,12):{ZERO:Q(2)}})
  endpoint=S.StandardEdgeOracle(S.StandardProgram(fixture)).bind((a,c))
  N=WholeNumerator(endpoint,prism,SparseOracle({ZERO:7},b),(ZERO,(2,0,0,0)))
  B=endpoint.coefficient(ZERO)
  self.assertEqual(N.coefficient((1,0,0,0)),7*B-4)
  self.assertEqual(N.coefficient((2,0,0,0)),7*B-6)
 def test_derivative_occurrence_factors_never_merge(self):
  b,a,c,Ca,p,N=self.make_combined();D=DifferentiatedCombinedNumerator(N,[(a,'f',1,Ca),(c,'f',1,Ca)],0,b)
  self.assertEqual(len(D.denominator_description['Delta']),2)
  with self.assertRaises(ValueError):DifferentiatedCombinedNumerator(N,[(a,'f',1,Ca),(a,'f',1,Ca)],0,b)

if __name__=='__main__':unittest.main()
