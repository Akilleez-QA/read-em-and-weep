"""Independent tiny artificial identity/metadata controls; no physical values."""
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).parent/'source'))
import domain as D

class Independent(unittest.TestCase):
    def test_raw_gerbe_conversion_in_each_toy_order(self):
        # Two arbitrary scalar 0-cochains on three abstract vertices.
        a=(Q(2),Q(-1),Q(4)); b=(Q(3),Q(5),Q(-2))
        def qa(i,j): return a[j]-a[i]
        def qb(i,j): return b[j]-b[i]
        def r(i,j): return qa(i,j)*qb(i,j)
        for i,j,k in permutations(range(3)):
            cup_ab=qa(i,j)*qb(j,k); cup_ba=qb(i,j)*qa(j,k)
            dr=r(j,k)-r(i,k)+r(i,j)
            self.assertEqual(dr,-cup_ab-cup_ba)
            pi_aw=-Q(1,8)*(cup_ab-cup_ba)
            self.assertEqual(-15*pi_aw,Q(15,4)*cup_ab+Q(15,8)*dr)
        # Reversing raw r is not the alternating-extension rule.
        self.assertEqual(r(1,0),r(0,1)); self.assertNotEqual(r(1,0),-r(0,1))

    def test_same_physical_different_common_keeps_three_owners(self):
        os=(D.I.FullOwner(30,'a',5,0,0),D.I.FullOwner(30,'b',5,0,8),D.I.FullOwner(30,'c',0,0,15))
        got=D.repetition_scope(os)
        self.assertTrue(got['physical_source_pullback_repeated'])
        self.assertFalse(got['general_common_cochain_repeated'])
        self.assertEqual(got['denominator_occurrences_retained'],3)
        domain=D.FullFiberDomain(30,'a',0)
        self.assertTrue(domain.contains(os[0]));self.assertFalse(domain.contains(os[1]))

    def test_exact_owned_degree_all_infinity_single_tuple(self):
        os=(D.I.FullOwner(30,'a',5,1,15),D.I.FullOwner(30,'b',0,2,15),D.I.FullOwner(30,'c',4,4,15))
        for p in ((0,1),(2,3)):
            degree=tuple(sum(14*(4 if o.carrier==5 else 5)+(1+2*((o.legal_mask>>i)&1) if i in p else 0)for o in os)-2*(i in p)for i in range(4))
            result=D.extension_contract(os,p)
            self.assertEqual(result['whole_P_exact_homogeneous_degree'],degree)
            self.assertEqual(result['Pi_summand_finite_enclosure'][1],tuple(-2*(i in p)for i in range(4)))
            self.assertFalse(result['actual_source_oracle_identity_accepted'])
            self.assertFalse(result['physical_execution_authorized'])

    def test_full_domain_refusal_even_for_structural_zero(self):
        domain=D.FullFiberDomain(30,'a',0)
        self.assertEqual(domain.descriptor()['cardinality']['value'],96)
        for call in (lambda:iter(domain),lambda:domain.owners(),lambda:domain.coefficient((0,0,0,0)),lambda:D.actual_coefficient(None)):
            with self.assertRaises(D.I.PhysicalAdmissionMissing):call()

if __name__=='__main__':unittest.main()
