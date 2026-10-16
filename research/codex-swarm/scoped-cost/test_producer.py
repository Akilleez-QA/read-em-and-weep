"""Small stdlib controls; no physical polynomial evaluation."""
import copy
import unittest
from unittest.mock import patch
import adapter as a


class ProducerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.grammar, cls.report = a.build()

    def test_actual_sources_and_pin_authentication(self):
        self.assertGreater(len(a.authenticate()['sources']), 50)
        self.assertEqual(len(self.grammar['finite_F12_template']['dag']),153)
        self.assertEqual(len(self.grammar['family_template']['nodes']),4270)

    def test_actual_demands_and_complete_source(self):
        g=self.grammar; r=self.report
        self.assertEqual((len(g['actual_demands']),r['family']['weighted_occurrences']), (121,127))
        self.assertEqual(r['family']['repeated_coefficient_references'],6)
        self.assertEqual(len({a.canonical([x['map'],x['exponent']]) for x in g['actual_demands']}),121)
        self.assertEqual(len(g['family_template']['Rsharp_components']),5)
        self.assertFalse(g['family_template']['closure']['top_J3_discarded'])
        self.assertGreater(r['family']['closure_J3_stats']['unique_nodes'],0)

    def test_full_owner_and_standard_boundaries(self):
        g=self.grammar
        self.assertEqual(len(g['fixed_branches']),8)
        self.assertEqual(len(g['combined_edges']),4)
        for b in g['fixed_branches']:
            owners=b['scope']['ordered_full_owners']
            self.assertTrue(all(len(o)==5 for o in owners))
            self.assertEqual([o[3] for o in owners],b['scope']['legal_masks'])
            self.assertEqual([o[4] for o in owners],b['scope']['standard_tags'])
            self.assertEqual(b['current_AST_nodes'][b['root']]['op'],'tracefree')
        for e in g['combined_edges']:
            self.assertFalse(e['complete_B_boundary']['split_into_free_leaves'])
            self.assertEqual([c['unpruned_instances'] for c in e['calls']],[96,9216])
            shell=e['combined_quotient_shell']; n=shell['nodes']
            whole=n[shell['whole_N_root']]
            self.assertEqual(whole['op'],'whole_N_sum')
            self.assertEqual(len(whole['children']),3)
            self.assertEqual(n[0]['op'],'pending_complete_B')
            self.assertEqual(len(shell['derivative_roots']),2)

    def test_integer_bound_and_shape_semantics(self):
        bound=self.report['finite_template_bound']
        self.assertEqual(bound['cleared_P_final_dense_cells_upper'],218**2*211**2)
        self.assertTrue(all(type(x['rational_operations_upper']) is int for x in bound['nodes']))
        self.assertIsNone(bound['physical_coefficient_height_bits'])
        self.assertIsNone(self.report['physical_cost_upper'])
        # One univariate degree-two scalar and its cube: 2*3*3 + 2*5*3.
        tiny=[['mask_times_x_squared_plus_one_over_two',0,0],['power',0,3]]
        b=a.dense_bound(tiny)
        self.assertEqual(b['nodes'][1]['degree'],[6,0,0,0])
        self.assertEqual(b['rational_operations_upper'],48)

    def test_reference_decoding_never_treats_slots_as_nodes(self):
        self.assertEqual(a.refs(['binary_mask_q_numerator',0,1,0,-1]),[])
        self.assertEqual(a.refs(['scale',-2,1,3]),[3])
        with self.assertRaises(ValueError):
            a.refs(['invented_operation',0])
        with self.assertRaises(ValueError):
            a.stats([['sum',True]],[0],a.refs,lambda n:n[0])
        with self.assertRaises(ValueError):
            a.dense_bound([['mask_times_x_squared_plus_one_over_two',0,0],['power',0,True]])

    def test_tree_counts_and_known_template_sharing(self):
        ns=[{'op':'leaf','children':[]},{'op':'multiply','children':[0,0]}]
        s=a.stats(ns,[1],lambda n:n['children'],lambda n:n['op'])
        self.assertEqual((s['tree_node_visits'],s['unique_nodes'],s['reuse_visits_avoided']),(3,2,1))
        f=self.report['finite_template_stats']
        self.assertEqual((f['unique_nodes'],f['tree_node_visits'],f['edge_references']),(153,333,227))
        self.assertEqual(self.report['fixed_E34']['unpruned_P_node_instances'],5698944)

    def test_exact_validation_rejects_mutated_scope_bound_and_gate(self):
        # Rebuilding is separately tested above; patch only to keep mutation controls tiny.
        with patch.object(a,'build',return_value=(self.grammar,self.report)):
            self.assertTrue(a.validate(self.grammar,self.report))
            for which in ('scope','bound','gate'):
                g=copy.deepcopy(self.grammar); r=copy.deepcopy(self.report)
                if which=='scope':g['fixed_branches'][0]['scope']['ordered_full_owners'][0][3]^=1
                elif which=='bound':r['finite_template_bound']['rational_operations_upper']=0
                else:r['gates']['execution_release']=True
                with self.assertRaises(ValueError):a.validate(g,r)

    def test_report_has_explicit_pending_programs_and_held_gates(self):
        ids={x['id'] for x in self.report['unresolved_cost_leaves']}
        for e in self.grammar['combined_edges']:
            self.assertIn(e['id']+':complete_B',ids)
            self.assertIn(e['id']+':Qhat',ids)
        self.assertFalse(self.report['gates']['arithmetic_admission'])
        self.assertFalse(self.report['gates']['execution_release'])
        self.assertEqual(self.report['gates']['fresh_budget_granted'],0)


if __name__=='__main__':
    unittest.main()
