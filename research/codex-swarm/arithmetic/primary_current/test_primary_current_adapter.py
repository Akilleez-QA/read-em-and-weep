"""Finite integer/Boolean and syntactic DAG controls only; no evaluator."""
import copy
import unittest
import primary_current_adapter as a


def records(triples=((1, 0, 0), (2, 1, 8), (4, 15, 15))):
    return [dict(seed=7, owner=i + 1, carrier=b, legal_mask=m, standard_tag=t)
            for i, (b, m, t) in enumerate(triples)]


def request(pair=(0, 1)):
    return {'schema': 'a05-primary-current-request-v1', 'owners': records(), 'pair': list(pair)}


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = a.build(request())

    def test_general_tags_and_full_owners(self):
        self.assertEqual([v[-1] for v in self.result['owners']], [0, 8, 15])
        self.assertEqual([v[1] for v in self.result['owners']], [1, 2, 3])
        self.assertEqual(self.result['source_pin'], a.SOURCE)

    def test_all_tag_and_active_mask_metadata(self):
        # No source current scan: only 16*16 finite metadata bit controls.
        for tag in range(16):
            bits = a.owned.decode_standard_tag(tag)
            for mask in range(16):
                legal = a.owned.decode_legal_mask(mask)
                active = not any(m and not b for m, b in zip(legal, bits))
                self.assertEqual(active, mask & ~sum(b << i for i, b in enumerate(bits)) == 0)
        # Several non-staircase owners incl equal carriers with different full labels.
        lo = a.PrimaryLower(records(((2, 0, 5), (2, 1, 8), (3, 0, 12))))
        self.assertEqual(len(lo.vs), 3)
        self.assertNotEqual(lo.key(lo.vs[0], 'H'), lo.key(lo.vs[1], 'H'))

    def test_four_terms_both_pairs(self):
        for p in ((0, 1), (2, 3)):
            r = self.result if p == (0, 1) else a.build(request(p))
            terms = r['four_terms']
            self.assertEqual([t['sign'] for t in terms], [1, -1, 1, -1])
            self.assertEqual([t['derivative_index'] for t in terms], [p[0], p[1], p[1], p[0]])
            self.assertEqual([t['current_index'] for t in terms], [p[1], p[0], p[0], p[1]])
            self.assertEqual([t['edge_owner_indices'] for t in terms], [[1,2],[1,2],[0,1],[0,1]])
            self.assertEqual(r['input_pair'], [2,3] if p == (0,1) else [0,1])
            for t in terms:
                self.assertEqual(t['character_conversion']['c'],1)
                self.assertEqual(t['character_conversion']['alpha'],1)
                self.assertEqual(t['character_conversion']['beta'],0)
                for key in ('A', 'B'):
                    for row in t[key]:
                        for cell in row:
                            self.assertEqual([l['owner'] for l in cell['owner_ledger']], r['owners'])

    def test_denominator_multiplicity_and_diff(self):
        lo = a.PrimaryLower(records(((2, 0, 5), (2, 1, 8), (3, 0, 12))))
        inv = lo.edge_inverse((0,1))
        for v in lo.vs[:2]:
            self.assertEqual(inv[1][lo.key(v,'H')], 14)
        product = lo.mul(inv, inv)
        for v in lo.vs[:2]:
            self.assertEqual(product[1][lo.key(v,'H')], 28)
        differentiated = lo.diff(inv, 0)
        # Inherited diff conservatively joins zero derivative summands too.
        self.assertEqual(differentiated[1][lo.key(lo.vs[0],'Z',1)], 5251)
        self.assertLessEqual(max(differentiated[1].values()), 5251)
        for bad in ({'alien':1}, {lo.key(lo.vs[0],'H'):-1}, {lo.key(lo.vs[0],'H'):True}):
            with self.assertRaises(ValueError):lo.rat(lo.g.c(1), bad)
        for kind, axis, count in (('H',None,55), ('L',0,30), ('Z',1,5252)):
            with self.assertRaises(ValueError):
                lo.cancel(lo.rat(lo.g.c(1), {lo.key(lo.vs[0],kind,axis):count}))

    def test_active_finite_restrictions_and_sums(self):
        lo = a.PrimaryLower(records(((1,0,0),(2,1,8),(4,15,15))))
        self.assertEqual(lo.quotient(lo.vs[0]), lo.g.c(0))
        for v in lo.vs[1:]:lo.quotient(v)
        sums = [n for n in lo.g.nodes if n[0] == 'bounded_composition_sum']
        self.assertTrue(sums)
        for _, domain, body in sums:
            self.assertEqual(domain['total'], domain['dimension']*534+1)
            self.assertEqual(domain['threshold'],535)
            self.assertIn(domain['chosen'],range(domain['dimension']))
            self.assertEqual(len(body['coefficient']['factors']),domain['dimension'])
        lo = a.PrimaryLower(records(((1,1,0),(2,1,8),(4,15,15))))
        self.assertEqual(lo.quotient(lo.vs[0]),lo.g.c(0))

    def test_syntax_only_inverses_and_log_derivatives(self):
        lo = a.PrimaryLower(records())
        q = lo.log(lo.vs[1],0)[0][0]
        dq = lo.diff(q,0)
        self.assertEqual(dq[1][lo.key(lo.vs[1],'L',0)],2)
        for op,*args in self.result['dag']:
            self.assertIn(op, ('rational','coordinate','add','multiply','power'))
            if op == 'power' and args[1] < 0:
                self.assertEqual(self.result['dag'][args[0]][0], 'coordinate')

    def test_factor_metadata_and_clearing(self):
        cert=a.factor_identity_metadata()
        self.assertEqual(cert['v2_a_factors'],[1]*5)
        self.assertEqual([r['carrier'] for r in cert['primary']],[1,2,3,4])
        lo=a.PrimaryLower(records())
        inv=lo.edge_inverse((1,2))
        cleared=lo.cancel(inv)
        self.assertEqual(len(cleared['derived_denominators']),3)
        # Clearing may contain only coordinate inverses. Composition stays symbolic.
        for op,*args in lo.g.nodes:
            if op=='power' and args[1]<0:
                self.assertEqual(lo.g.nodes[args[0]][0],'coordinate')
        with self.assertRaises(ValueError):lo.normal_order((False,True))

    def test_rejections(self):
        mutations = []
        for key,value in [('carrier',5),('carrier',0),('carrier',True),('standard_tag',16),
                          ('legal_mask',False),('owner',-1),('seed','7')]:
            r=request();r['owners'][0][key]=value;mutations.append(r)
        r=request();r['owners'].reverse();mutations.append(r)
        r=request();r['owners'][1]=copy.deepcopy(r['owners'][0]);mutations.append(r)
        r=request();r['owners'][1]['owner']=r['owners'][0]['owner'];mutations.append(r)
        r=request();r['carrier_map']={};mutations.append(r)
        r=request();r['owners'][0]['extra']=0;mutations.append(r)
        for pair in ([0,2],[False,True],[1,0],['0',1]):
            r=request();r['pair']=pair;mutations.append(r)
        for r in mutations:
            with self.assertRaises(ValueError):a.build(r)
        lo=a.PrimaryLower(records())
        for method,args in ((lo.current,('bad',0)),(lo.current,('L',True)),
                            (lo.admitted_weighted_derivative,()),(lo.block,(lo.vs[0],'H0'))):
            with self.assertRaises(ValueError):method(*args)

    def test_gates_and_mutation(self):
        gates = ['actual_source_admitted','source_pole_domain_proved','weighted_derivative_admitted',
                 'Laurent_admitted','actual_factorization_accepted','execution_release',
                 'physical_polynomial_expansion','physical_polynomial_evaluation']
        for key in gates:self.assertIs(self.result[key], False)
        mutated=copy.deepcopy(self.result);mutated['execution_release']=True
        with self.assertRaises(ValueError):a.validate_result(request(),mutated)
        mutated['execution_release']=0
        with self.assertRaises(ValueError):a.validate_result(request(),mutated)
        with self.assertRaises(ValueError):a.authenticate_directory('/tmp')

if __name__ == '__main__':unittest.main()
