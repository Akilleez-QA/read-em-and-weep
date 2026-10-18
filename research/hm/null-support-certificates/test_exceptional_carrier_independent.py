"""Independent metadata/zero-pattern audit. No physical polynomial arithmetic."""
import hashlib, itertools, json, unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch
import lower_exceptional_carrier_sector as candidate
import resolution_selector_source_binding as selector
ROOT=Path(__file__).parent

class ExceptionalIndependentTests(unittest.TestCase):
    def test_domain_by_cartesian_product_and_full_keys(self):
        # Independent of candidate combinations-with-replacement enumerator.
        pairs=tuple(itertools.product(range(6),range(16)))
        counts=Counter();anchors=Counter();active_sectors=Counter()
        tags=(3,11,15)
        for triple in itertools.product(pairs,repeat=3):
            keys=tuple((c if c!=5 else -1,m,t) for (c,m),t in zip(triple,tags))
            if not keys[0]<keys[1]<keys[2]:continue
            counts['full']+=1
            if all(c in (1,2,3,4) for c,m in triple):counts['prior_primary']+=1;continue
            counts['remaining_exceptional']+=1
            self.assertIn(triple[0][0],(0,5));anchors[str(triple[0][0])]+=1
            active=True
            for (c,m),t in zip(triple,tags):
                bits=tuple((t>>(3-i))&1 for i in range(4));s=sum(bits)
                eligible=all(not ((m>>i)&1) or bits[i] for i in range(4)) and (c==5 or (c<=s and (s!=4 or c==4)))
                active &= eligible
            counts['exceptional_outer_not_structurally_zero' if active else 'exceptional_outer_literal_zero']+=1
            counts['exceptional_selected_contraction_zero']+=1
            if active:active_sectors[','.join(str(c) for c,m in triple)]+=1
        saved=json.loads((ROOT/'exceptional-carrier-domain-partition.json').read_text())
        counts['unresolved_exceptional']=0
        self.assertEqual(dict(counts),saved['counts'])
        self.assertEqual(dict(anchors),saved['anchor_counts'])
        self.assertEqual(dict(active_sectors),saved['potentially_active_carrier_sectors'])
        self.assertEqual((counts['full'],counts['remaining_exceptional']),(152096,106336))
        self.assertEqual((counts['exceptional_outer_literal_zero'],counts['exceptional_outer_not_structurally_zero']),(101962,4374))

    def test_pinned_model_and_certificate_bridge_without_execution(self):
        raw=(ROOT/'hm-pinned-model.json').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926')
        model=json.loads(raw);cert=json.loads((ROOT/'pinned-homogeneous-identities.json').read_text())
        self.assertEqual(hashlib.sha256(json.dumps(model,separators=(',',':')).encode()).hexdigest(),cert['modelSha256'])
        auth=candidate.authentication()
        for name,digest in auth['contraction_certificate']['files_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),digest)
        for b in (0,5):
            self.assertEqual(model['charts'][b]['pivot'],0)
            self.assertEqual([row[6] for row in model['charts'][b]['P']],[[],[]])
        self.assertEqual(model['charts'][5]['dp'],[['2,0,1,1',-1]])
        self.assertFalse(auth['contraction_certificate']['historical_checker_executed_now'])

    def test_selector_orientation_and_all_four_arbitrary_entries(self):
        model=selector.authenticate()
        for b in (0,5):
            vs=tuple(candidate.base.owned.VertexLabel(4,o,c,0,t) for o,(c,t) in enumerate(zip((b,1,4),(3,11,15))))
            binding=selector.bind_seed(4,vs)
            self.assertEqual((binding['coefficient'],binding['entry'],binding['row']),(-2,[12,6],2))
            ast=binding['source_ast'];self.assertEqual(ast['op'],'multiply')
            self.assertEqual(ast['args'][0]['args'][1]['op'],'transpose')
            self.assertEqual(ast['args'][1]['op'],'column')
            self.assertEqual(ast['args'][1]['args'][1],6)
            # Each independent coefficient of R[w,u] contains P[w,6]=0.
            for u,w in itertools.product(range(2),repeat=2):
                self.assertEqual(model['charts'][b]['P'][w][6],[])
            lo=candidate.ExceptionalLower(vs)
            symbolic=[[lo.rat(lo.g.node('audit_free_R',w,u)) for u in range(2)] for w in range(2)]
            with patch.object(lo,'current',return_value=symbolic), patch.object(lo,'tracefree',side_effect=lambda r:r):
                root,den=lo.selected_contraction('L',0)
                self.assertEqual(lo.g.nodes[root],['rational',0,1])
            for fn in (lo.cancel,lo.edge_inverse,lo.quotient):
                with self.assertRaises(ValueError):fn(None)

    def test_partition_does_not_build_currents_or_clear_denominators(self):
        with patch.object(candidate.ExceptionalLower,'__init__',side_effect=AssertionError('no rational lowering needed')):
            saved=candidate.partition()
        self.assertFalse(saved['physical_polynomial_evaluation'])
        self.assertFalse(saved['physical_polynomial_expansion'])
        self.assertEqual(saved['physical_products_spent'],0)
        self.assertFalse(saved['execution_release'])
        self.assertFalse(saved['actual_factorization_accepted'])

    def test_full_seed_has_uncovered_sorted_standard_permutations(self):
        # Pi_out labels the fixed staircase independently, then source-sorts.
        # This outer-active PRIMARY example lies outside the 152096 slice.
        assigned=((2,0,3),(1,0,11),(4,0,15))
        for c,m,t in assigned:self.assertTrue(candidate.outer_maybe_active(c,m,t))
        ordered=tuple(sorted(assigned))
        self.assertEqual(tuple(t for c,m,t in ordered),(11,3,15))
        self.assertNotEqual(tuple(t for c,m,t in ordered),candidate.STANDARDS)
        self.assertEqual(96**3,884736)
        self.assertLess(152096,96**3)

    def test_all_standard_permutations_exceptional_selector(self):
        model=selector.authenticate()
        for tags in itertools.permutations((3,11,15)):
            for b in (0,5):
                vs=tuple(candidate.base.owned.VertexLabel(4,o,b,o,t) for o,t in enumerate(tags))
                bound=selector.bind_seed(4,vs)
                self.assertEqual(bound['entry'],[12,6])
                self.assertEqual(bound['coefficient'],-2)
                self.assertEqual(bound['source_ast']['args'][1]['args'][1],6)
                self.assertEqual(bound['right_ast']['args'][1],list(vs[0].data()))
                self.assertEqual([r[6] for r in model['charts'][b]['P']],[[],[]])
        counts=Counter();permutations=Counter()
        pairs=tuple(itertools.product(range(6),range(16)))
        for assigned in itertools.product(pairs,repeat=3):
            owners=tuple((c,m,t) for (c,m),t in zip(assigned,(3,11,15)))
            ordered=sorted(owners,key=lambda v:(-1 if v[0]==5 else v[0],v[1],v[2]))
            exceptional=any(c in (0,5) for c,m,t in owners)
            counts['exceptional' if exceptional else 'primary']+=1
            if exceptional:
                self.assertIn(ordered[0][0],(0,5))
                permutations[tuple(t for c,m,t in ordered)]+=1
        self.assertEqual(dict(counts),{'exceptional':622592,'primary':262144})
        self.assertEqual(permutations[(3,11,15)],106336)
        self.assertEqual(sum(permutations.values()),96**3-64**3)

    def test_primary_artifact_hash_bridge(self):
        doc=json.loads((ROOT/'primary-carrier-full-domain-partition.json').read_text())
        for filename,digest in doc['certificates_sha256'].items():
            self.assertEqual(hashlib.sha256((ROOT/filename).read_bytes()).hexdigest(),digest)
        audit=doc['independent_audit']
        self.assertEqual(hashlib.sha256((ROOT/audit['log']).read_bytes()).hexdigest(),audit['sha256'])
        self.assertEqual(sum(doc['counts'][k] for k in ('outer_literal_zero','selected_contraction_literal_zero','prior_support_excluded','new_support_excluded')),45760)

if __name__=='__main__':unittest.main()
