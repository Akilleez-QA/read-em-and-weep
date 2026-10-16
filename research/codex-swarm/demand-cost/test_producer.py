"""Producer controls; independent review files intentionally reserved."""
import copy
import json
import unittest
from pathlib import Path
import preflight as p


def toy():
    m = {'i':5,'b':0}; e = [-1,-2,-3,-1]
    group = [{'map':m,'coordinate':e}]
    scope = {'map':m,'coordinate':e,'owners':[[12,0,1,0,0]],
             'source_branch_id':'toy:prism1','frame':'toy-finite'}
    def node(nid, op, inputs):
        return dict(copy.deepcopy(scope),id=nid,op=op,inputs=inputs)
    return group, {'schema':'co01-demand-grammar-v1',
        'nodes':[node('x','leaf',[]),node('s','add',['x','x']),node('p','multiply',['s','s'])],
        'entries':[{'map':m,'coordinate':e,'roots':['p']}]}


class ProducerTests(unittest.TestCase):
    def test_exact_counts(self):
        d = p.build()
        self.assertEqual(d['totals'], {'weighted_requests':32,'actual_maps':20,
            'weighted_term_occurrences':127,'unique_map_coordinates':121,
            'coordinate_reuses':6,'distinct_coordinates_ignoring_map':32,'sum_absolute_weights':149})
        self.assertEqual(d['formal_circuit']['tree_node_visits'],None)

    def test_weighted_reconstruction(self):
        rows = p.requests(); groups = p.demand_join(rows)
        got = [[] for _ in rows]
        for g in groups:
            for u in g['uses']:
                got[u['request_id']].append((g['map'],g['coordinate'],u['weight']))
        for r,actual in zip(rows,got):
            expected = [(r['scalar_map'],t['laurent_exponents'],t['coefficient']) for t in r['terms']]
            self.assertEqual(sorted(actual,key=p.canonical),sorted(expected,key=p.canonical))

    def test_small_dag(self):
        groups,g = toy(); d = p.grammar_join(groups,g)
        self.assertEqual((d['tree_node_visits'],d['reachable_unique_nodes'],d['reuse_visits_avoided'],d['dag_edge_references']), (7,3,4,4))
        self.assertEqual(d['physical_arithmetic_counts'],'UNKNOWN')

    def test_equal_equations_distinct_owners_do_not_share(self):
        groups,g = toy()
        # Same carrier/masks/tag, different actual occurrence: reference must fail.
        g['nodes'][1]['owners'][0][1] = 1
        with self.assertRaisesRegex(ValueError,'cross-scope'):
            p.grammar_join(groups,g)

    def test_distinct_source_branches_do_not_share(self):
        groups,g = toy(); g['nodes'][1]['source_branch_id'] = 'toy:prism2'
        with self.assertRaisesRegex(ValueError,'cross-scope'):
            p.grammar_join(groups,g)

    def test_distinct_maps_do_not_share(self):
        groups,g = toy(); g['nodes'][1]['map']['i'] = 6
        with self.assertRaisesRegex(ValueError,'cross-scope'):
            p.grammar_join(groups,g)

    def test_cycles_and_missing_coverage_rejected(self):
        groups,g = toy(); g['nodes'][0]['inputs'] = ['p']; g['nodes'][0]['op'] = 'add'
        with self.assertRaises(ValueError): p.grammar_join(groups,g)
        groups,g = toy(); g['entries'] = []
        with self.assertRaisesRegex(ValueError,'missing actual map'): p.grammar_join(groups,g)

    def test_fake_admission_cannot_release(self):
        d = p.admission({'CURRENT':True,'caps':10**30,'spent':0,'live_allocations':[],
                         'commitments':[],'whole_source_cleared':True,'cost_upper':1})
        self.assertFalse(d['arithmetic_admission']); self.assertFalse(d['execution_release'])
        self.assertEqual(d['cost_upper'],'UNKNOWN'); self.assertEqual(d['fresh_budget_granted'],0)

    def test_full_sum_padding_and_complete_B(self):
        lemma = p.build()['null_lemma']; a,b,c = lemma['branches']
        self.assertTrue(a['complete_B_required']); self.assertEqual(b['padding'],'Z_ab')
        self.assertEqual(c['padding'],'C_a Z_ab'); self.assertEqual(lemma['max_derivatives'],1)
        self.assertFalse(lemma['source_clearing_proved_here'])

    def test_saved_report(self):
        self.assertEqual(p.build(),json.loads((Path(__file__).parent/'request-report.json').read_bytes()))


if __name__ == '__main__':
    unittest.main()
