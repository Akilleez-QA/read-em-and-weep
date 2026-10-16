"""RS01 small free identities/artificial scalars and unexecuted metadata."""
import copy
import itertools
import unittest
from fractions import Fraction as Q
import r_binding as rs
import formal_identities as fa


class SourceApplicationControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app=rs.ActualFullSourceApplication()
        I=cls.app._domain.I
        cls.oo=tuple(I.FullOwner(12,('r-test',i),i,0,i)for i in range(3))

    def test_exact_ambient_defect_syzygy_requires_both_relations(self):
        actual,remainder=fa.defect_syzygy()
        self.assertEqual(actual,remainder)
        self.assertEqual(len(remainder),4)
        # Drop either published coherence relation: a nonzero obstruction
        # remains. Changing any one of the four defect signs also fails.
        for j in range(4):
            signs=[1,1,-1,-1];signs[j]*=-1
            self.assertNotEqual(fa.defect_syzygy(signs)[0],remainder)
        words=set(remainder)
        self.assertIn(('A','V','W'),words)
        self.assertIn(('C','D','H'),words)

    def test_positive_boundary_sign_in_exact_Rsharp_identity(self):
        self.assertEqual(fa.reduction_identity(),{})
        self.assertTrue(fa.reduction_identity(boundary_sign=-1))

    def test_mixed_Moyal_square_coefficient_and_ordered_four_terms(self):
        pi=[(0,1,1),(1,0,-1),(2,3,1),(3,2,-1)]
        out={}
        for i,j,c in pi:
            for a,b,d in pi:
                if len({i,j,a,b})==4:
                    key=(tuple(sorted((i,a))),tuple(sorted((j,b))))
                    out[key]=out.get(key,Q(0))+Q(c*d,8)
        self.assertEqual(out,{((0,2),(1,3)):Q(1,4),((0,3),(1,2)):Q(-1,4),
                              ((1,2),(0,3)):Q(-1,4),((1,3),(0,2)):Q(1,4)})
        self.assertNotEqual(next(iter(out.values())),Q(1,8))

    def test_fresh_gerbe_cocycle_on_artificial_new_orders(self):
        # Arbitrary rational scalar cocycles and every new order. No curve
        # value or physical mask polynomial is evaluated.
        a=[Q(0),Q(2,3),Q(-1),Q(4,5)];b=[Q(1),Q(0),Q(3,2),Q(-2)]
        def gerbe(i,j,k):return Q(15,4)*(a[j]-a[i])*(b[k]-b[j])
        for i,j,k,l in itertools.permutations(range(4)):
            self.assertEqual(gerbe(j,k,l)-gerbe(i,k,l)+gerbe(i,j,l)-gerbe(i,j,k),0)

    def test_compiler_contract_rejects_missing_gerbe_branch_and_framejets(self):
        t=self.app._template
        self.assertEqual(len(rs.compiler_source_contract(t)),20)
        for change in ['gerbe','branch','jet']:
            bad=copy.deepcopy(t)
            if change=='gerbe':bad['source_residual_components'][0]['baseline']['gerbe_terms'].pop()
            elif change=='branch':bad['source_residual_components'][0]['components'].pop('Fk12')
            else:next(n for n in bad['nodes']if n['op']=='physical_jet')['frames_differentiated']=False
            with self.assertRaises(ValueError):rs.compiler_source_contract(bad)

    def test_actual_definition_metadata_and_all_physical_calls_refuse(self):
        c=self.app.describe(self.oo)
        self.assertEqual(c['schema'],'actual-fresh-full-source-application-v1')
        self.assertEqual(c['same_representative_identity']['boundary_sign'],1)
        self.assertFalse(c['same_representative_identity']['pointwise_Rsharp_equals_M'])
        self.assertEqual(len(c['fresh_first_lift']['FD_actual_definitions']),2)
        self.assertEqual(set(c['SC_source_reference']['bound_triple_record']['component_roots']),
                         {'baseline','Fk12','Fk34','E12','E34'})
        self.assertFalse(c['outer_full54_29_5251_domain_discharged'])
        for method in [self.app.coefficient,self.app.factor_terms,self.app.owners]:
            with self.assertRaises(self.app._domain.I.PhysicalAdmissionMissing):method('invalid',(-10**9,0,0,0))
        with self.assertRaises(ValueError):self.app.describe(self.oo[::-1])
        with self.assertRaises(TypeError):rs.ActualFullSourceApplication(source=lambda:True)

    def test_pin_drift_refuses_and_returned_metadata_is_detached(self):
        pins,raws=rs.authenticate(rs.HERE.parents[2])
        def corrupt(rev,path):
            raw=raws[rev,path]
            return raw+b' ' if path.endswith('ambient-second-jet.md')else raw
        with self.assertRaisesRegex(ValueError,'source bytes drift'):
            rs.authenticate(rs.HERE.parents[2],corrupt)
        pins=self.app.source_pins();pins['sources'].clear()
        self.assertTrue(self.app.source_pins()['sources'])


if __name__=='__main__':unittest.main()
