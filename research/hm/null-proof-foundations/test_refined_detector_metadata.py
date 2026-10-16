"""Adversarial metadata tests only; no physical polynomial import or evaluation."""
import copy
import json
import unittest
from dataclasses import replace
import compile_refined_detector_metadata as m

class MetadataTests(unittest.TestCase):
    def test_seed_count_and_distribution(self):
        seeds=m.seed_records()
        self.assertEqual(len(seeds),78)
        self.assertEqual([sum(s['lift_depth']==d for s in seeds) for d in range(3)],[6,24,48])
        self.assertEqual(len({(s['row'],s['standard']) for s in seeds}),78)

    def test_seed_orientation_controls(self):
        rows=[s for s in m.seed_records() if s['row']==0]
        self.assertEqual(rows[0]['standard'],(3,11,15))
        self.assertEqual(rows[0]['orientation'],1)
        self.assertEqual(rows[1]['standard'],(3,7,15))
        self.assertEqual(rows[1]['orientation'],-1)

    def test_deterministic_and_bounded(self):
        a=m.encode_certificate(m.build_certificate())
        self.assertEqual(a,m.encode_certificate(m.build_certificate()))
        self.assertLessEqual(len(a),m.MAX_OUTPUT_BYTES)
        self.assertFalse(json.loads(a)['execution_release'])
        self.assertEqual(len(json.loads(a)['unresolved_leaves']),8)

    def test_small_cap_fails_before_output(self):
        with self.assertRaises(m.ContractError):m.encode_certificate(m.build_certificate(),1)

    def test_invalid_cap(self):
        for cap in (0,-1,True,m.MAX_OUTPUT_BYTES+1):
            with self.subTest(cap=cap),self.assertRaises(m.ContractError):
                m.encode_certificate(m.build_certificate(),cap)

    def test_derivative_before_cancellation_rejected(self):
        with self.assertRaisesRegex(m.ContractError,'before inserted'):
            m.differentiate_regularized(m.raw_inner())

    def test_missing_cancellation_witness(self):
        with self.assertRaises(m.ContractError):m.cancel_inserted(m.raw_inner(),'trust me')

    def test_derivative_replay_rejected(self):
        s=m.differentiate_regularized(m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients'))
        with self.assertRaises(m.ContractError):m.differentiate_regularized(s)

    def test_exact_derivative_state(self):
        s=m.differentiate_regularized(m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients'))
        self.assertEqual((s.inserted_carrier,s.suffix_carrier,s.suffix_legal,s.standard_boundary),
                         (0,15,2,5251))

    def test_inner_outer_partition_mismatch(self):
        with self.assertRaises(m.ContractError):m.check_partition(m.INNER,'outer')
        with self.assertRaises(m.ContractError):m.check_partition(m.OUTER,'inner')

    def test_standard_tag_mismatch(self):
        with self.assertRaises(m.ContractError):m.check_standard_projection((0,3,15),(0,7,15))

    def test_dropped_prefix_owner(self):
        s,_=m.homotopy_adjoint(m.initial_owners(4),0)
        s,_=m.cech_face(s,0)
        self.assertIn('o0',s.kernel_owners)
        self.assertNotIn('o0',s.active)
        with self.assertRaisesRegex(m.ContractError,'dropped prefix'):
            replace(s,kernel_owners=frozenset()).validate()

    def test_dropped_prefix_weight(self):
        s,_=m.homotopy_adjoint(m.initial_owners(4),0)
        s,_=m.cech_face(s,0)
        with self.assertRaises(m.ContractError):
            replace(s,weighted_owners=s.weighted_owners-{'o0'}).validate()

    def test_old_four_tail_and_781_rejected(self):
        for tag in ('old_four_tail','old_781_features','fourtail','781'):
            with self.subTest(tag=tag),self.assertRaises(m.ContractError):
                m.check_source_assumptions({tag})

    def test_h_sign_controls(self):
        n=(-2,-2,0,0)
        a=m.tensor_h_adjoint(n,'ACBB',(0,-1,0,0))
        self.assertEqual(a,[{'pivot':0,'states':'CCBB','exponents':(0,-1,0,0),'coefficient':-1}])
        b=m.tensor_h_adjoint(n,'CBAB',(-1,-2,0,0))
        self.assertEqual(b,[{'pivot':1,'states':'CCAB','exponents':(-1,-2,0,0),'coefficient':-1}])
        c=m.tensor_h_adjoint((0,0,-2,-2),'ABCA',(0,0,-1,0))
        self.assertEqual(c[-1]['coefficient'],1)
        self.assertEqual(c[-1]['states'],'BBCC')

    def test_h_B_zero_is_killed(self):
        out=m.tensor_h_adjoint((0,0,-2,-2),'BBBB',(0,0,-2,-2))
        self.assertTrue(all(row['pivot'] not in (0,1) for row in out))
        self.assertEqual(len(out),1)  # later negative-twist pivot remains legal

    def test_derivative_zero_and_shift(self):
        self.assertIsNone(m.derivative_demand((-1,0,0,0),0))
        self.assertEqual(m.derivative_demand((-2,0,0,0),0),
                         {'exponents':(-1,0,0,0),'coefficient':-1})

    def test_no_release_mutation(self):
        c=m.build_certificate();c['execution_release']=True
        with self.assertRaises(m.ContractError):m.encode_certificate(c)

    def test_no_source_evaluation_mutation(self):
        c=m.build_certificate();c['physical_source_evaluated']=True
        with self.assertRaises(m.ContractError):m.encode_certificate(c)

    def test_missing_seed_rejected(self):
        c=m.build_certificate();c['seeds'].pop()
        with self.assertRaises(m.ContractError):m.encode_certificate(c)

    def test_nested_certificate_mutations_rejected(self):
        mutations = {
            'partition': lambda c: c['partitions'].update(outer=m.INNER),
            'seed_sign': lambda c: c['seeds'][0].update(coefficient=99),
            'seed_row': lambda c: c['seeds'][0].update(row=8),
            'duplicate_seeds': lambda c: c.update(seeds=[c['seeds'][0]]*78),
            'exponent': lambda c: c['terminal_rows'][0].update(exponent=[0,0,0,0]),
            'prefix': lambda c: c['owner_control'].update(kernel=[]),
            'ready_status': lambda c: c.update(status='execution_ready_resource_pass'),
            'empty_leaves': lambda c: c.update(unresolved_leaves=[]),
            'dropped_leaf': lambda c: c['unresolved_leaves'].pop(),
            'domain': lambda c: c['derivative_domain_control'].update(carrier_cap=14),
            'frame': lambda c: c.update(source_order='standard_first'),
            'extra_flag': lambda c: c.update(launch_authorized=True),
            'integer_false': lambda c: c.update(raw_kernel_paths_enumerated=0),
        }
        for name,mutation in mutations.items():
            with self.subTest(name=name),self.assertRaises(m.ContractError):
                c=m.build_certificate();mutation(c);m.encode_certificate(c)

    def test_forged_derivative_domain_rejected(self):
        s=m.differentiate_regularized(m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients'))
        for change in ({'cancellation_witness':''},{'partition':m.OUTER},{'derivative_count':0}):
            with self.subTest(change=change),self.assertRaises(m.ContractError):
                m.outer_domain_check(replace(s,**change),m.OUTER,(0,3,15),(0,3,15))

    def test_derivative_partition_mismatch(self):
        s=m.cancel_inserted(m.raw_inner(),'N14-owned-polynomial-quotients')
        with self.assertRaises(m.ContractError):
            m.differentiate_regularized(replace(s,partition=m.OUTER))

    def test_bad_tuple_and_degree(self):
        with self.assertRaises(m.ContractError):m.initial_owners(6)
        with self.assertRaises(m.ContractError):m.homotopy_adjoint(m.initial_owners(3),1)

if __name__=='__main__':unittest.main()
