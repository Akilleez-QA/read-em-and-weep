"""Only explicit tiny toy fibers and source-free owner/degree metadata."""
import unittest
import domain as D
I=D.I

def owners(tags=(0,8,12)):
    return tuple(I.FullOwner(12,('toy-slot',j),c,m,t)for j,(c,m,t)in enumerate(zip((5,0,4),(0,3,15),tags)))

class Controls(unittest.TestCase):
    def test_symbolic_full96_descriptor_no_enumeration(self):
        f=D.FullFiberDomain(12,('Pi',(0,8,12),1),8);d=f.descriptor()
        self.assertEqual(d['cardinality'],{'expression':'6 * 16','value':96})
        self.assertEqual(d['carrier_domain']['maximum'],5);self.assertEqual(d['legal_mask_domain']['maximum'],15)
        for callback in(lambda:iter(f),lambda:f.owners(),lambda:f.coefficient((0,0,0,0))):
            with self.assertRaises(I.PhysicalAdmissionMissing):callback()
    def test_full_owner_membership_not_weight_survival(self):
        f=D.FullFiberDomain(12,'slot',0);o=I.FullOwner(12,'slot',5,15,0)
        self.assertTrue(f.contains(o)) # zero finite legal weight is still indexed
        self.assertFalse(f.contains(I.FullOwner(12,'other-slot',5,15,0)))
        self.assertFalse(f.contains(I.FullOwner(13,'slot',5,15,0)))
        self.assertFalse(f.contains(I.FullOwner(12,'slot',5,15,8)))
    def test_lazy_toy_only_yields_requested_owners(self):
        f=D.LazyToyFibers(12,{0:[(5,0),(0,1)],8:[(4,15)]});g=f.owners(0,('toy','u'))
        self.assertEqual(f.yields,0);a=next(g);self.assertEqual(f.yields,1)
        self.assertEqual(a,I.FullOwner(12,('toy','u'),5,0,0));self.assertEqual(next(g).carrier,0)
        with self.assertRaises(StopIteration):next(g)
    def test_same_physical_is_not_same_common_vertex(self):
        a=owners();a=(a[0],I.FullOwner(12,'new',5,0,8),a[2]);r=D.repetition_scope(a)
        self.assertTrue(r['physical_source_pullback_repeated']);self.assertFalse(r['general_common_cochain_repeated'])
        r=D.repetition_scope((a[0],I.FullOwner(12,'new',5,0,0),a[2]))
        self.assertTrue(r['general_common_cochain_repeated']);self.assertEqual(r['denominator_occurrences_retained'],3)
    def test_exact_degrees_both_pairs_and_all_infinity_target(self):
        a=owners((15,15,15))
        self.assertEqual(D.extension_contract(a,(0,1))['whole_P_exact_homogeneous_degree'],(201,201,196,196))
        c=D.extension_contract(a,(2,3));self.assertEqual(c['whole_P_exact_homogeneous_degree'],(196,196,199,199))
        self.assertEqual(c['Pi_summand_finite_enclosure'][1],(0,0,-2,-2))
    def test_frame_bounds_and_shift_has_no_extra_pair_twist(self):
        o=I.FullOwner(12,'q',1,15,8);q=D.Qhat_frame_enclosure(o,(0,1))
        self.assertEqual(q['finite_frame_shift'],(-73,0,0,0))
        self.assertEqual(q['exponent_enclosure'],((-286,0,0,0),(-73,335,335,335)))
        self.assertTrue(q['zero_weight_predicate']);self.assertFalse(q['extra_pair_twist_attached'])
        self.assertEqual(D.Qhat_frame_enclosure(I.FullOwner(12,'q',5,0,15),(2,3))['exponent_enclosure'],((-124,-124,-124,-124),(-56,-56,-57,-57)))
    def test_mixed_and_finite_target_extension_bounds(self):
        for tags in((0,8,12),(0,0,0)):
            c=D.extension_contract(owners(tags),(0,1));self.assertFalse(c['physical_execution_authorized'])
            self.assertFalse(c['actual_fibers_enumerated']);self.assertFalse(c['actual_source_oracle_identity_accepted'])
    def test_reject_bool_and_lost_owner_provenance(self):
        with self.assertRaises(ValueError):D.FullFiberDomain(True,'u',0)
        with self.assertRaises(ValueError):D.FullFiberDomain(0,'u',False)
        with self.assertRaises(ValueError):D.LazyToyFibers(0,{0:[(True,0)]})
        with self.assertRaises(ValueError):D.extension_contract(owners(),(False,1))
        a=owners()
        with self.assertRaises(ValueError):D.extension_contract((a[0],I.FullOwner(13,'new',0,3,8),a[2]),(0,1))
        with self.assertRaises(ValueError):D.extension_contract((a[0],I.FullOwner(12,a[0].occurrence,0,3,8),a[2]),(0,1))
        with self.assertRaises(I.PhysicalAdmissionMissing):D.actual_coefficient(owners(),(0,0,0,0))
    def test_actual_factory_all_value_and_enumeration_entries_refuse(self):
        a=D.ActualDomainApplication()
        for f in(a.coefficient,a.factor_terms,a.owners):
            with self.assertRaises(I.PhysicalAdmissionMissing):f(owners(),(-1,0,0,0))
        with self.assertRaises(ValueError):D.ActualDomainApplication('/tmp/unrelated-model')
        with self.assertRaises(TypeError):D.ActualDomainApplication(catalog='arbitrary')
    def test_aggregate_metadata_profile_is_only_a_descriptor_count(self):
        x={'P':{'program':{'dag':[['a'],['b']]}},'Q':[{'nodes':[['c'],['d'],['e']]},{'nodes':[['f']]}]}
        p=D.metadata_profile(x);self.assertEqual(p['aggregate_stored_AST_nodes'],6)
        self.assertEqual(len(p['stored_AST_arrays']),3);self.assertGreater(p['serialized_payload_bytes'],0)
        self.assertFalse(p['physical_coefficient_memory_or_cost_admission'])
        self.assertFalse(p['aggregate_resource_supervisor_present'])

if __name__=='__main__':unittest.main()
