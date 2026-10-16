"""TP01 independent pure-plan/frame controls; no actual coefficients/fibers."""
from fractions import Fraction as Q
from itertools import permutations
from unittest.mock import patch
import unittest
import provider as P


def owner(c, mask, tag, occurrence):
    return P.I.FullOwner(12, occurrence, c, mask, tag)


def multiply(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


class FrameReview(unittest.TestCase):
    def test_all_four_owner_permutations_route_original_row_end(self):
        canonical = (owner(5, 15, 15, 'star'), owner(0, 0, 0, 'a'),
                     owner(1, 3, 8, 'b'), owner(4, 15, 15, 'c'))
        for raw in permutations(canonical):
            plan = P.request_plan('Rsharp', raw)
            sign = (-1)**sum(raw[i].source_key > raw[j].source_key
                            for i in range(4) for j in range(i+1, 4))
            route = P.frame_plan(plan)
            self.assertEqual(plan.sorted_owners, canonical)
            self.assertEqual(plan.owners, raw)
            self.assertEqual(route['parity'], sign)
            self.assertEqual(route['original_first_owner'], raw[0].data())
            self.assertEqual(route['canonical_first_owner'], canonical[0].data())
            self.assertEqual(route['transition']['ordered_edge_request'],
                             (raw[0].data(), canonical[0].data()))
            if raw[0] == canonical[0]:
                self.assertEqual(route['transport'], 'identity')
            else:
                self.assertEqual(route['transport'], 'ordered_conjugation')
                self.assertEqual(route['ordered_actions'],
                    ['inverse(g(original_first,canonical_first))', 'X_canonical',
                     'g(original_first,canonical_first)'])
            self.assertFalse(route['physical_transport_evaluated'])

    def test_noncommuting_conjugation_direction_and_parity(self):
        # Artificial rational matrices only; not physical transitions.
        g = ((Q(1), Q(2)), (Q(0), Q(1)))
        inverse = ((Q(1), Q(-2)), (Q(0), Q(1)))
        x = ((Q(0), Q(0)), (Q(1), Q(0)))
        correct = multiply(multiply(inverse, x), g)
        wrong_direction = multiply(multiply(g, x), inverse)
        self.assertEqual(correct, ((-2, -4), (1, 2)))
        self.assertNotEqual(correct, x)
        self.assertNotEqual(correct, wrong_direction)
        a, b = owner(0, 0, 0, 'a'), owner(1, 0, 0, 'b')
        route = P.frame_plan(P.request_plan('Rsharp', (b, a)))
        signed = tuple(tuple(route['parity']*v for v in row) for row in correct)
        self.assertEqual(signed, ((2, 4), (-1, -2)))
        self.assertEqual(route['transition']['ordered_edge_request'], (b.data(), a.data()))

    def test_repetition_alias_empty_and_fixed_scalar_frames(self):
        a, b, c = owner(1, 2, 0, 'a'), owner(1, 2, 8, 'b'), owner(4, 15, 15, 'c')
        self.assertEqual(P.request_plan('F', (b, a, c)).effective_sign, 0)
        for role in ('T', 'Rsharp'):
            plan = P.request_plan(role, (b, a, c))
            self.assertEqual(plan.effective_sign, -1)
            self.assertTrue(plan.repeated_physical)
            self.assertEqual(plan.zero_reason, '')
        route = P.frame_plan(P.request_plan('Rsharp', (b, a, c)))
        self.assertEqual(route['transport'], 'ordered_conjugation')
        duplicate = owner(1, 2, 0, 'different-occurrence')
        zero = P.request_plan('Rsharp', (a, duplicate, c))
        self.assertEqual(zero.zero_reason, 'repeated_common')
        self.assertTrue(P.frame_plan(zero)['zero_plan_requires_no_transport_evaluation'])
        alias = owner(2, 2, 0, 'a')
        self.assertTrue(P.request_plan('T', (a, alias)).occurrence_alias)
        self.assertNotEqual(P.request_plan('T', (a, alias)).effective_sign, 0)
        empty = P.frame_plan(P.request_plan('Rsharp', ()))
        self.assertTrue(empty['empty_tuple_has_no_base_owner'])
        self.assertIsNone(empty['transition']['ordered_edge_request'])
        for role in ('F', 'T'):
            route = P.frame_plan(P.request_plan(role, (b, a, c)))
            self.assertEqual(route['value_frame'], 'common_finite_fixed_frame')
            self.assertEqual(route['transport'], 'identity')

    def test_lazy96_boundary_metadata_and_immediate_iteration_refusal(self):
        d = P.Full96Descriptor(12, ['inserted', 'u'], 9)
        for index, expected in ((0, (0, 0)), (15, (0, 15)), (16, (1, 0)),
                                (79, (4, 15)), (80, (5, 0)), (95, (5, 15))):
            result = d.label_plan(index)
            self.assertEqual(result, (12, ('inserted', 'u'), *expected, 9))
            self.assertEqual(16*result[2]+result[3], index)
        for bad in (True, -1, 96, 1.0):
            with self.assertRaises(ValueError): d.label_plan(bad)
        with self.assertRaises(P.I.PhysicalAdmissionMissing): iter(d)
        with self.assertRaises(P.I.PhysicalAdmissionMissing): d.owners('malformed')

    def test_actual_gates_before_validation_normalization_or_frame_routes(self):
        actual = object.__new__(P.ActualProvider)
        actual.mode = 'synthetic'
        poison = AssertionError('pure metadata must not run on gated requests')
        with patch.object(P, 'request_plan', side_effect=poison), \
             patch.object(P, 'frame_plan', side_effect=poison), \
             patch.object(P, 'pair', side_effect=poison):
            for method in (actual.coefficient, actual.alternating_coefficient,
                           actual.factor_terms, actual.owners):
                for args in ((), (None,), ('F', (), (-999, 0, 0, 0))):
                    with self.assertRaises(P.I.PhysicalAdmissionMissing): method(*args)

    def test_F_join_forwards_original_order_and_only_crosschecks_sign(self):
        # This spy tests TP routing only, not canonical FD construction.
        a, b, c = owner(5, 0, 0, 'a'), owner(1, 2, 8, 'b'), owner(4, 15, 15, 'c')
        raw = (b, a, c)
        class DomainSpy:
            def describe(self, owners, pair):
                self.called = (owners, pair)
                return {'source_sorting_sign': -1}
        actual = object.__new__(P.ActualProvider)
        actual.pins = {}
        actual.domain = DomainSpy()
        report = actual.describe('F', raw, (2, 3))
        self.assertEqual(actual.domain.called, (raw, (2, 3)))
        self.assertEqual(report['effective_sign'], -1)
        self.assertEqual(report['source_definition']['source_sorting_sign'], -1)
        self.assertFalse(report['whole_T_or_Rsharp_implementation_supplied'])
        with patch.object(actual.domain, 'describe', side_effect=AssertionError('must not join')):
            for role in ('T', 'Rsharp'):
                self.assertEqual(actual.describe(role, raw)['definition_join'],
                                 'normalization only; no raw source reevaluation')

    def test_workspace_pin_checks_without_actual_definition_construction(self):
        pins = P._authenticate()
        self.assertEqual(len(pins['workspace_inputs']), 10)
        self.assertFalse(pins['actual_execution'])
        with patch.object(P, '_authenticate', side_effect=AssertionError('auth reached')):
            with self.assertRaises(ValueError): P.ActualProvider(P.BASE/'other-repository')


if __name__ == '__main__':
    unittest.main()
