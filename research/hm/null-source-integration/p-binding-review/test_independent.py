"""PB01 independent metadata controls. No physical polynomial construction."""
import copy
import itertools
import unittest
import p_binding as pb
from source_program import pair_nodes


class IndependentPBControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.binding = pb.ActualPBinding()

    def test_exact_graph_shapes_and_both_raw_pair_renamings(self):
        p = self.binding.symbolic_program_definition()
        nodes = p['dag']
        self.assertEqual((len(nodes), p['cleared_P']), (153, 152))
        shapes = []
        for row in nodes:
            op, *a = row
            if op == 'catalog_cleared_primitive':
                s = (2, 15) if a[1] == 'P' else (15, 2)
            elif op in ('owned_polynomial_factor', 'mask_times_x_squared_plus_one_over_two', 'binary_mask_q_numerator'):
                s = ()
            elif op == 'polynomial_diagonal': s = (2, 2)
            elif op == 'transpose': s = tuple(reversed(shapes[a[0]]))
            elif op == 'trace':
                self.assertEqual(shapes[a[0]][0], shapes[a[0]][1]); s = ()
            elif op == 'scale': s = shapes[a[2]]
            elif op == 'sum':
                s = shapes[a[0]]; self.assertTrue(all(shapes[k] == s for k in a))
            elif op == 'power': s = ()
            elif op == 'polynomial_partial_after_elementary_substitution': s = shapes[a[0]]
            elif op == 'ordered_product':
                matrices = [shapes[k] for k in a if shapes[k]]
                for left, right in zip(matrices, matrices[1:]):
                    self.assertEqual(left[1], right[0])
                s = (matrices[0][0], matrices[-1][1]) if matrices else ()
            else: self.fail(op)
            shapes.append(s)
        self.assertEqual(shapes[152], ())
        for pair in ((0, 1), (2, 3)):
            q = self.binding.symbolic_program_definition(pair)['dag']
            self.assertEqual(q, pair_nodes(nodes, pair))
            self.assertEqual([tuple(x['shape']) for x in pb.audit_shapes(q, 152)], shapes)
            for x, y in zip(nodes, q):
                if x[0] in ('catalog_cleared_primitive', 'ordered_product', 'scale', 'transpose', 'trace'):
                    self.assertEqual(x, y)
        self.assertEqual(pb.rename_pair(pb.rename_pair(nodes, (2, 3)), (2, 3)), nodes)

    def test_owner_degrees_are_divisor_sum_plus_character(self):
        for carriers in itertools.product(range(6), repeat=3):
            for masks in ((0, 0, 0), (15, 15, 15), (1, 4, 9), (3, 12, 15)):
                owners = tuple(sorted((pb.FullOwner(30, i, c, m, i)
                    for i, (c, m) in enumerate(zip(carriers, masks))), key=lambda o:o.source_key))
                for pair in ((0, 1), (2, 3)):
                    expected = []
                    for axis in range(4):
                        value = 0
                        for owner in owners:
                            value += 14 * (4 if owner.carrier == 5 else 5)
                            if axis in pair:
                                value += 3 if owner.legal_mask & (1 << axis) else 1
                        expected.append(value - (2 if axis in pair else 0))
                    self.assertEqual(self.binding.degree_upper(owners, pair), tuple(expected))

    def test_common_source_repeat_distinction_and_occurrence_guards(self):
        owners = (pb.FullOwner(1, 'a', 1, 3, 0), pb.FullOwner(1, 'b', 1, 3, 8), pb.FullOwner(1, 'c', 2, 7, 12))
        report = self.binding.describe(owners)
        self.assertTrue(report['source_order']['repeated_physical_source_labels_zero'])
        self.assertEqual([x['owner'] for x in report['owned_clearings']], [list(o.data()) for o in owners])
        for bad in (owners[::-1], (owners[0], owners[0], owners[2]),
                    (owners[0], pb.FullOwner(2, 'b', 1, 3, 8), owners[2]),
                    (owners[0], pb.FullOwner(1, 'a', 1, 3, 8), owners[2])):
            with self.assertRaises(ValueError): self.binding.describe(bad)

    def test_primitive_weighted_bridges_preserve_auxiliary_v0(self):
        owners = tuple(pb.FullOwner(1, i, i, 0, i) for i in range(3))
        bridges = self.binding.describe(owners)['primitive_bridges']
        self.assertEqual(len(bridges), 6)
        for c, bridge in enumerate(bridges):
            self.assertEqual(bridge['assigned_H_degree'], 4 if c == 5 else 5)
            self.assertEqual(len(bridge['entry_degrees']), 60)
            for entry in bridge['entry_degrees']:
                weight = entry['column'] if entry['block'] == 'I' else -entry['row']
                self.assertEqual(entry['weight'], weight)
                self.assertEqual(entry['stored_numerator_homogenization_degree'], (6 if c == 5 else 5) + weight)
        self.assertEqual(bridges[5]['homogeneous_H'], 'v0*v1*v3*v4')
        self.assertEqual(bridges[5]['finite_di_dp'], '-v1^2*v3*v4')
        self.assertEqual(bridges[5]['homogeneous_H_squared_primitive'], '-v3*v4*hom_(6+w)(stored_num)')

    def test_fail_closed_even_for_malformed_or_negative_demands(self):
        for method in (self.binding.coefficient, self.binding.alternating_coefficient):
            for args in ((), (None,), ('untrusted', (-1, 0, 0, 0))):
                with self.assertRaises(pb.PhysicalAdmissionMissing): method(*args)
        for pair in ((False, 1), (1, 0), (0, 3)):
            with self.assertRaises(ValueError): self.binding.symbolic_program_definition(pair)

    def test_copy_isolation_and_semantic_type_rejections(self):
        p = self.binding.symbolic_program_definition()
        p['dag'][0] = ['unrelated_callback']
        self.assertNotEqual(p, self.binding.symbolic_program_definition())
        for graph in ([['catalog_cleared_primitive', True, 'I']],
                      [['owned_polynomial_factor', [0, 'H', 0]]],
                      [['ordered_product', 0]]):
            with self.assertRaises(ValueError): pb.audit_shapes(graph, 0)


if __name__ == '__main__':
    unittest.main()
