"""CO-R independent integer graph/count checks; no physical polynomial arrays."""
import copy,json,unittest
from pathlib import Path
from collections import Counter
import adapter as a
B=Path(__file__).parent.parent

def refs(n):
    if n[0] in ('catalog_cleared_primitive','owned_polynomial_factor','mask_times_x_squared_plus_one_over_two','binary_mask_q_numerator'):return ()
    if n[0] in ('ordered_product','sum'):return tuple(n[1:])
    if n[0]=='scale':return(n[3],)
    return(n[1],)

def reverse_multiplicities(nodes,roots,edges):
    count=[0]*len(nodes)
    for r in roots:count[r]+=1
    for i in range(len(nodes)-1,-1,-1):
        for j in edges(nodes[i]):
            if not(type(j)is int and 0<=j<i):raise ValueError('non-topological source')
            count[j]+=count[i]
    reached=[i for i,v in enumerate(count)if v]
    return len(reached),sum(count),sum(len(edges(nodes[i])) for i in reached)

class Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.g,cls.r=a.build()
    def test_actual_finite_graph_by_reverse_count(self):
        data=json.loads((B/'whole-source-clearing/source-integration.json').read_bytes())['finite_actual_source_clearing']
        actual=reverse_multiplicities(data['dag'],[data['cleared_P']],refs)
        self.assertEqual(actual,(153,333,227))
        s=self.r['finite_template_stats']
        self.assertEqual(actual,(s['unique_nodes'],s['tree_node_visits'],s['edge_references']))
    def test_actual_family_roots_and_closure(self):
        nodes=json.loads((B/'scalar-compiler/compiled-template.json').read_bytes())['nodes']
        roots=[i for i,n in enumerate(nodes)if n['op']=='Laurent_coefficient']
        self.assertEqual(len(roots),121)
        actual=reverse_multiplicities(nodes,roots,lambda n:n['children'])
        self.assertEqual(actual,(2464,24971995,4424))
        got=self.r['family']['demand_union_stats']
        self.assertEqual(actual,(got['unique_nodes'],got['tree_node_visits'],got['edge_references']))
        self.assertGreater(self.r['family']['closure_J3_stats']['unique_nodes'],0)
    def test_scopes_are_separate_not_global_seed_substitution(self):
        f=self.r['fixed_E34'];family=self.r['family']
        self.assertEqual((f['branches'],f['complete_N_edges'],family['actual_map_exponent_demands']),(8,4,121))
        self.assertEqual(f['unpruned_P_instances'],4*(96+96**2))
        self.assertEqual(f['unpruned_P_node_instances'],4*(96+96**2)*153)
        self.assertEqual(family['outer_unpruned_assignments_per_demand'],24*96**5)
        self.assertEqual(family['outer_unpruned_assignments_all_demands'],121*24*96**5)
        self.assertIn('not physical',family['counts_status'])
    def test_dense_bound_semantics_and_exclusions(self):
        # Direct conservative P(2x15)*I(15x2) convolution count from leaf boxes.
        s=13**4;out=25**4
        expected=2*(2*15*2)*s*s+(2*2*14)*out
        self.assertEqual(self.r['finite_template_bound']['nodes'][2]['rational_operations_upper'],expected)
        self.assertEqual(self.r['finite_template_bound']['cleared_P_final_dense_cells_upper'],218**2*211**2)
        for key in ('physical_peak_bytes','physical_coefficient_height_bits','oracle_cost','bit_operations_upper'):
            self.assertIsNone(self.r['finite_template_bound'][key])
        self.assertIsNone(self.r['physical_cost_upper'])
    def test_discharging_B_or_releasing_gate_is_not_valid_metadata(self):
        g=copy.deepcopy(self.g);r=copy.deepcopy(self.r)
        e=g['combined_edges'][0]
        node=next(n for n in e['combined_quotient_shell']['nodes']if n['op']=='pending_complete_B')
        node['op']='admitted_complete_B'
        with self.assertRaises(ValueError):a.validate(g,r)
        r=copy.deepcopy(self.r);r['gates']['execution_release']=True
        with self.assertRaises(ValueError):a.validate(self.g,r)

if __name__=='__main__':unittest.main()
