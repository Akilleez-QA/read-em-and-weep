"""Independent tiny edge-domain regression; no actual HM source is imported."""
from fractions import Fraction as Q
import unittest
from interfaces import FullOwner,RegularExtensionWitness,sorted_source,need,require_synthetic
from polynomial_coefficients import Budget
from inserted_program import PrismProgram,WholeNumerator,SparseOracle,SyntheticFibers,SyntheticQuotients,ZERO


class SingleTripleSource:
    mode='synthetic'
    def degree_upper(self,owners,pair=(0,1)):return ZERO
    def coefficient(self,owners,e,pair=(0,1)):
        require_synthetic(self.mode)
        need(tuple(owners)==sorted_source(owners)[0],'already source-sorted triple')
        return Q(int(e==ZERO and tuple(o.carrier for o in owners)==(2,3,4)))


def fixture(edge=None):
    a=FullOwner(0,'a',1,0,0);b=FullOwner(0,'b',2,0,8)
    edge=(a,b)if edge is None else tuple(edge)
    budget=Budget();source=SingleTripleSource()
    fibers=SyntheticFibers(0,{0:[(3,0)],8:[(4,0)]})
    quotients=SyntheticQuotients({(3,0,0):{ZERO:1},(4,0,8):{ZERO:1}})
    witness=RegularExtensionWitness('synthetic','edge-domain-artificial-source',tuple(o.standard_tag for o in edge),edge,'tiny-constant-domain')
    one=SparseOracle({ZERO:1},budget)
    return edge,source,fibers,quotients,witness,one,budget


def program(edge=None):
    edge,source,fibers,quotients,witness,one,budget=fixture(edge)
    return PrismProgram(edge,source,quotients,fibers,one,ZERO,witness,budget)


def unguarded_raw_formula(edge):
    """Independent scalar specialization of proof(3), intentionally no domain guard.

    This controls the mathematical reason that reversing and re-evaluating
    the raw prism formula cannot define the alternating extension.
    """
    edge,source,fibers,quotients,witness,one,budget=fixture(edge);a,b=edge
    def F(owners):
        ordered,sign=sorted_source(owners)
        return sign*source.coefficient(ordered,ZERO)
    out=Q(0)
    for u in fibers.owners(a.standard_tag,('raw','u')):
        out+=F((u,a,b))
        for v in fibers.owners(b.standard_tag,('raw','v')):out-=F((u,v,b))
    return out


class EdgeDomainControls(unittest.TestCase):
    def test_raw_reevaluation_counterexample(self):
        (a,b),*_=fixture()
        self.assertEqual(unguarded_raw_formula((a,b)),-1)
        self.assertEqual(unguarded_raw_formula((b,a)),0)
        self.assertNotEqual(unguarded_raw_formula((b,a)),-unguarded_raw_formula((a,b)))
    def test_valid_increasing_edge_complete_numerator(self):
        p=program();one=SparseOracle({ZERO:1},p.budget);zero=SparseOracle({},p.budget)
        N=WholeNumerator(zero,p,one,(ZERO,ZERO))
        self.assertLess(p.edge[0].source_key,p.edge[1].source_key)
        self.assertEqual(p.coefficient('prism1',ZERO),0)
        self.assertEqual(p.coefficient('prism2',ZERO),-1)
        self.assertEqual(N.coefficient(ZERO),-1)
    def test_reversed_common_edge_must_be_rejected(self):
        (a,b),*_=fixture()
        with self.assertRaises(ValueError):program((b,a))
    def test_repeated_common_edge_must_be_rejected_even_distinct_occurrences(self):
        (a,b),*_=fixture();copy=FullOwner(a.seed,'a-second-occurrence',a.carrier,a.legal_mask,a.standard_tag)
        self.assertEqual(a.source_key,copy.source_key);self.assertNotEqual(a,copy)
        with self.assertRaises(ValueError):program((a,copy))
        with self.assertRaises(ValueError):program((a,a))
    def test_same_physical_vertex_different_standard_tags_is_valid_common_edge(self):
        (a,b),*_=fixture();other=FullOwner(a.seed,'same-source-different-standard',a.carrier,a.legal_mask,8)
        self.assertEqual(a.physical_key,other.physical_key)
        self.assertLess(a.source_key,other.source_key)
        p=program((a,other))
        self.assertEqual(p.edge,(a,other))
        self.assertEqual(p.coefficient('prism1',ZERO),0)
        self.assertEqual(p.coefficient('prism2',ZERO),0)

if __name__=='__main__':unittest.main()
