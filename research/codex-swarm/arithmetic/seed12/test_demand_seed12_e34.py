"""Tiny integer/Boolean metadata checks only; no physical arithmetic."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest
import demand_seed12_e34 as d

class DemandChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out=d.compile_request(copy.deepcopy(d.REQUEST))

    def test_exact_input_and_word(self):
        b=self.out['selector_binding']
        self.assertEqual(b['owners'],[tuple(v) for v in d.OWNERS])
        self.assertEqual(b['weighted_owners'],(0,1,2,3))
        self.assertEqual(b['deleted_prefix_owners'],(0,))
        self.assertEqual(b['tail_owners'],[tuple(v) for v in d.OWNERS[1:]])
        self.assertEqual([b['entry'],b['coefficient'],b['exponent']],[[2,6],2,(-1,-2,-3,-3)])
        self.assertEqual([x['block'] for x in self.out['kernel_block_occurrences']],['H0','I','P'])
        self.assertTrue(all(x['tree_occurrences']==1 for x in self.out['kernel_block_occurrences']))

    def test_all_four_terms_and_full_owners(self):
        terms=self.out['terms']
        self.assertEqual([(t['derivative_coordinate'],t['current'],t['E_sign']) for t in terms],
                         [(2,['L',3],1),(3,['L',2],-1),(3,['U',2],1),(2,['U',3],-1)])
        self.assertEqual(json.loads(d.canonical([t['edge_owners'] for t in terms])),
                         [d.OWNERS[2:],d.OWNERS[2:],d.OWNERS[1:3],d.OWNERS[1:3]])
        for t in terms:
            self.assertEqual((t['terminal_coefficient'],t['E_denominator'],t['orientation']),(2,2,1))
            self.assertTrue(t['current_block_occurrences'])
        self.assertEqual(len(self.out['outer_weight_nodes']),4)

    def test_shared_current_dag_and_physical_logs(self):
        nodes=self.out['dag']
        self.assertEqual(len({d.canonical(n) for n in nodes}),len(nodes))
        uses={}
        for i,(op,payload) in enumerate(nodes):
            for child in payload['children']:
                self.assertLess(child,i)
                uses[child]=uses.get(child,0)+1
        # The complete core transpose is shared, so its block children need only one parent.
        self.assertTrue(any(n[0]=='public_matrix' and n[1]['matrix_op']=='transpose'
                            and uses.get(i,0)>1 for i,n in enumerate(nodes)))
        logs=[n for n in nodes if n[0]=='public_matrix' and n[1]['matrix_op']=='logarithmic_diagonal_frame']
        self.assertEqual(len(logs),6)  # B,C,D logs in both coordinates, with sharing.
        self.assertTrue(any(n[0]=='public_matrix' and n[1]['matrix_op']=='adjugate_over_determinant' for n in nodes))

    def test_no_unprepared_derivative_or_execution(self):
        self.assertTrue(all(v is False for v in self.out['gates'].values()))
        self.assertFalse(self.out['lower_capability']['supported'])
        self.assertFalse(self.out['lower_capability']['fallback_used'])
        for op,p in self.out['dag']:
            if op=='derivative_after_cancellation_request':
                self.assertIs(p['enabled'],False)
                parent=self.out['dag'][p['children'][0]]
                self.assertEqual(parent[0],'combined_inner_regularization_request')
                self.assertIsNone(parent[1]['witness'])
                self.assertEqual(parent[1]['branches'],['Hrho','Pi Kcov R','Pi S h A R'])
        self.assertEqual(len(self.out['Rsharp_context']),5)

    def test_fail_closed_schema(self):
        mutations=[]
        x=copy.deepcopy(d.REQUEST);x['carrier_map']={};mutations.append(x)
        x=copy.deepcopy(d.REQUEST);x['orientation']=True;mutations.append(x)
        x=copy.deepcopy(d.REQUEST);x['seed']=12.0;mutations.append(x)
        x=copy.deepcopy(d.REQUEST);x['owners'][1][4]=3;mutations.append(x)
        x=copy.deepcopy(d.REQUEST);x['execution_release']=True;mutations.append(x)
        x=copy.deepcopy(d.REQUEST);del x['frame'];mutations.append(x)
        x=copy.deepcopy(d.REQUEST);x['owners'][0]=None;mutations.append(x)
        for x in mutations:
            with self.subTest(input=x),self.assertRaises(ValueError):d.compile_request(x)

    def test_integer_normal_order_identity(self):
        # Finite exponent-index bookkeeping, never source polynomial arithmetic.
        kappa=(-1,-2,-3,-3)
        for coordinate in (2,3):
            for nu in ((0,0,0,0),(1,-1,2,-3),(-2,1,-2,-2)):
                alpha=tuple(kappa[i]-nu[i]+int(i==coordinate) for i in range(4))
                self.assertEqual(tuple(alpha[i]+nu[i]-int(i==coordinate) for i in range(4)),kappa)
                self.assertEqual(alpha[coordinate],kappa[coordinate]-nu[coordinate]+1)

    def test_reproducible_artifact_and_cap(self):
        self.assertEqual(json.loads(Path('seed12-e34-demand.json').read_text()),json.loads(d.canonical(self.out)))
        self.assertLess(len(d.canonical(self.out).encode()),262144)

if __name__=='__main__':unittest.main()
