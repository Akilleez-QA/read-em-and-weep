"""FD-R: bounded metadata and artificial algebra, never physical coefficients.

Run this filename directly (also with -O). Exactly one canonical describe call
uses the explicitly listed handoff triple; no actual fiber is instantiated.
"""
from collections import Counter
from contextlib import ExitStack
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import resource
import subprocess
import unittest
from unittest import mock

import domain as D

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
I = D.I
MARKER_SHA = '85ce3c680d9def1203aeaac071b0b86868b0ee860cd934a4d94e94d1364886aa'
PINS_SHA = 'af8e2dbdb8b4b307f79d6d8e08617422b199319942464e9373e47bde7c084d86'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def toy(tags=(0, 8, 12)):
    return tuple(I.FullOwner(31, ('artificial', j), c, m, t)
                 for j, (c, m, t) in enumerate(zip((5, 2, 4), (0, 5, 10), tags)))


class Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        marker = (HERE/'producer-ready.json').read_bytes()
        if digest(marker) != MARKER_SHA:
            raise RuntimeError('reviewed ready marker changed')
        cls.manifest = json.loads(marker)['files']
        cls.before = {name: digest((HERE/name).read_bytes()) for name in cls.manifest}
        if cls.before != cls.manifest:
            raise RuntimeError('producer files do not match ready marker')

    @classmethod
    def tearDownClass(cls):
        after = {name: digest((HERE/name).read_bytes()) for name in cls.manifest}
        if after != cls.before or digest((HERE/'producer-ready.json').read_bytes()) != MARKER_SHA:
            raise RuntimeError('producer changed during independent tests')

    def test_exact_source_pins(self):
        raw = (HERE/'source-pins.json').read_bytes()
        self.assertEqual(digest(raw), PINS_SHA)
        pins = json.loads(raw)
        self.assertEqual(len(pins['immutable_dependencies']), 13)
        for row in pins['immutable_dependencies']:
            with self.subTest(path=row['path']):
                raw = subprocess.check_output(['git', 'show', row['commit']+':'+row['path']], cwd=ROOT, timeout=10)
                self.assertEqual(digest(raw), row['sha256'])
                self.assertEqual(len(raw), row['bytes'])
                self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(), row['git_blob'])
        for row in pins['canonical_definition_workspace_inputs']:
            self.assertEqual(digest((ROOT/row['path']).read_bytes()), row['sha256'])

    def test_descriptor_membership_and_provenance_without_iteration(self):
        f = D.FullFiberDomain(31, ['slot', 2], 8)
        d = f.descriptor()
        self.assertEqual(d['carrier_domain'], {'minimum': 0, 'maximum': 5, 'inclusive': True})
        self.assertEqual(d['legal_mask_domain']['maximum'], 15)
        self.assertEqual(d['cardinality'], {'expression': '6 * 16', 'value': 96})
        # Two explicitly supplied boundary labels, including a zero-weight branch.
        for c, m in ((0, 0), (5, 15)):
            self.assertTrue(f.contains(I.FullOwner(31, ('slot', 2), c, m, 8)))
        for seed, occurrence, tag in ((32, ('slot', 2), 8), (31, 'other', 8), (31, ('slot', 2), 0)):
            self.assertFalse(f.contains(I.FullOwner(seed, occurrence, 5, 15, tag)))
        for action in (lambda: iter(f), lambda: f.owners(None), lambda: f.coefficient(None)):
            with self.assertRaises(I.PhysicalAdmissionMissing):
                action()

    def test_three_distinct_equal_equation_occurrences_survive(self):
        a = I.FullOwner(31, 'a', 5, 3, 0)
        b = I.FullOwner(31, 'b', 5, 3, 8)
        c = I.FullOwner(31, 'c', 5, 3, 12)
        r = D.repetition_scope((a, b, c))
        self.assertTrue(r['physical_source_pullback_repeated'])
        self.assertFalse(r['general_common_cochain_repeated'])
        contract = D.extension_contract((a, b, c), (0, 1))
        self.assertEqual(len(contract['owners']), 3)
        self.assertEqual(len({tuple(o[:2]) for o in contract['owners']}), 3)
        same_common = I.FullOwner(31, 'b', 5, 3, 0)
        self.assertTrue(D.repetition_scope((a, same_common, c))['general_common_cochain_repeated'])
        with self.assertRaises(ValueError):
            D.extension_contract((a, I.FullOwner(32, 'b', 5, 3, 8), c), (0, 1))
        with self.assertRaises(ValueError):
            D.extension_contract((a, I.FullOwner(31, 'a', 5, 3, 8), c), (0, 1))

    def test_source_order_sign_on_only_tiny_artificial_permutations(self):
        a = toy()
        for perm in itertools.permutations(range(3)):
            ordered, sign = I.sorted_source(tuple(a[j] for j in perm))
            self.assertEqual(ordered, a)
            # Exterior sign from the three differences, independent of sorting code.
            vandermonde = (perm[1]-perm[0])*(perm[2]-perm[0])*(perm[2]-perm[1])
            self.assertEqual(sign, 1 if vandermonde > 0 else -1)
        b = (I.FullOwner(31, 'b', 0, 1, 8), I.FullOwner(31, 'a', 0, 1, 0), I.FullOwner(31, 'c', 0, 2, 0))
        self.assertEqual(I.sorted_source(b), ((b[1], b[0], b[2]), -1))

    def test_exact_degree_and_whole_target_endpoint_inequalities(self):
        # Supplied artificial triples only; no 96-label or actual fiber product.
        for p in ((0, 1), (2, 3)):
            for tags in ((0, 0, 0), (15, 15, 15), (0, 8, 12), (8, 8, 8)):
                owners = toy(tags)
                x = D.extension_contract(owners, p)
                expected_c = [(57, 57, 56, 56), (73, 71, 70, 70), (71, 73, 70, 70)] if p == (0, 1) else [(56, 56, 57, 57), (70, 70, 73, 71), (70, 70, 71, 73)]
                self.assertEqual(x['C_degrees'], expected_c)
                expected_D = (199, 199, 196, 196) if p == (0, 1) else (196, 196, 199, 199)
                self.assertEqual(x['whole_P_exact_homogeneous_degree'], expected_D)
                lo, hi = x['Pi_summand_finite_enclosure']
                for i in range(4):
                    states = {(tag >> (3-i)) & 1 for tag in tags}
                    if states == {0}:
                        self.assertEqual(lo[i], 0)
                    elif states == {1}:
                        self.assertEqual(hi[i], -2 if i in p else 0)
                    else:
                        self.assertEqual(x['standard_target_conditions'][i], 'mixed intersection: coordinate invertible')
                if tags == (15, 15, 15):
                    # Coarse 217/210 padding would leave forbidden positive slack.
                    coarse = (217, 217, 210, 210) if p == (0, 1) else (210, 210, 217, 217)
                    self.assertTrue(all(coarse[i]-sum(c[i] for c in expected_c) > hi[i] for i in range(4)))

    def test_sharp_imported_reversal_bounds_not_support(self):
        for tag, finite, infinity in ((0, 66, None), (8, 335, 213), (12, 872, 347), (14, 1677, 481), (15, None, 66)):
            for p in ((0, 1), (2, 3)):
                o = I.FullOwner(31, 'q', 5, 5, tag)
                q = D.Qhat_frame_enclosure(o, p)
                low, high = q['exponent_enclosure']
                for i in range(4):
                    if tag & (1 << (3-i)):
                        c = q['C_degree'][i]
                        extra = (0 if i in (0, 2) else 1) if i in p else 2
                        self.assertEqual((low[i], high[i]), (-c-infinity-extra, -c))
                    else:
                        self.assertEqual((low[i], high[i]), (0, finite))
                self.assertFalse(q['occupied_support_computed'])
                self.assertFalse(q['extra_pair_twist_attached'])

    def test_metadata_counts_stored_occurrences_and_utf8_bytes(self):
        shared = [['coordinate', 0], ['power', 0, 14]]
        payload = {'P': {'dag': shared}, 'Q': [{'nodes': shared}, {'nodes': []}], 'note': '\u03c1', 'not_ast': [1, 2, 3]}
        profile = D.metadata_profile(payload)
        self.assertEqual(profile['aggregate_stored_AST_nodes'], 4)
        self.assertEqual([a['stored_nodes'] for a in profile['stored_AST_arrays']], [2, 2, 0])
        self.assertEqual(profile['serialized_payload_bytes'], len(json.dumps(payload, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()))
        self.assertNotIn('metadata_profile', payload)
        self.assertFalse(profile['physical_coefficient_memory_or_cost_admission'])
        self.assertFalse(profile['aggregate_resource_supervisor_present'])

    def test_tiny_lazy_provider_is_explicit_and_not_full_descriptor(self):
        t = D.LazyToyFibers(31, {8: [(5, 15), (0, 0)]})
        g = t.owners(8, 'explicit-toy')
        self.assertEqual(t.yields, 0)
        self.assertEqual(next(g).data(), (31, 'explicit-toy', 5, 15, 8))
        self.assertEqual(t.yields, 1)
        with self.assertRaises(ValueError):
            D.LazyToyFibers(31, D.FullFiberDomain(31, 'x', 8))
        with self.assertRaises(ValueError):
            D.LazyToyFibers(31, {8: [(0, 0)]*5})

    def test_unconditional_refusal_with_poison_requests_and_mode_changes(self):
        class Poison:
            def __iter__(self):
                raise AssertionError('request inspected')
            def __bool__(self):
                raise AssertionError('request inspected')
        a = D.ActualDomainApplication()
        f = D.FullFiberDomain(31, 'zero-weight', 0)
        for mode in ('physical', 'synthetic', 'verified', None):
            a.mode = mode
            a.physical_execution_authorized = True
            for method in (a.coefficient, a.factor_terms, a.owners, D.actual_coefficient, f.coefficient, f.owners):
                with self.assertRaises(I.PhysicalAdmissionMissing):
                    method(Poison(), pair=Poison(), mode='synthetic', verified=True)
        for kwargs in ({'catalog': object()}, {'callback': lambda: 0}, {'verified': 'yes'}, {'repo': '/tmp'}):
            with self.assertRaises((TypeError, ValueError)):
                D.ActualDomainApplication(**kwargs)

    def test_one_explicit_canonical_description_ast_only(self):
        # The three owners explicitly recorded in application-contract.json;
        # one swap exercises external parity. This is the only actual describe.
        owners = (I.FullOwner(12, ('toy-contract-slot', 1), 0, 3, 8),
                  I.FullOwner(12, ('toy-contract-slot', 0), 5, 0, 0),
                  I.FullOwner(12, ('toy-contract-slot', 2), 4, 15, 12))
        pmod = D._canonical_module('fd_actual_P_binding', HERE.parent/'source-faithful-P/p_binding.py')
        qmod = D._canonical_module('fd_actual_Q_binding', HERE.parent/'source-faithful-Q/q_binding.py')
        import polynomial_coefficients as PC
        with ExitStack() as stack:
            for cls, names in ((PC.Ring, ('coefficient', '_coefficient', 'polynomial')), (PC.Catalog, ('cleared',)), (PC.ClearedSourceProgram, ('__init__',)), (qmod.QH.FiniteRing, ('_coefficient',)), (D.FullFiberDomain, ('__iter__', 'owners'))):
                for name in names:
                    stack.enter_context(mock.patch.object(cls, name, side_effect=AssertionError('forbidden physical evaluation/iteration')))
            sort = stack.enter_context(mock.patch.object(I, 'sorted_source', wraps=I.sorted_source))
            result = D.ActualDomainApplication().describe(owners, (0, 1))
            self.assertEqual(sort.call_count, 1)
        self.assertEqual(result['source_sorting_sign'], -1)
        sorted_data = [owners[j].data() for j in (1, 0, 2)]
        self.assertEqual(result['source_sorted_owners'], sorted_data)
        self.assertEqual(result['P_definition']['ordered_owners'], [list(o) for o in sorted_data])
        self.assertEqual(len(result['P_definition']['program']['dag']), 153)
        self.assertEqual(result['whole_P_exact_homogeneous_degree'], (201, 201, 196, 196))
        self.assertEqual([tuple(q['owner']) for q in result['Q_definitions']], [o.data() for o in owners])
        self.assertEqual(result['P_definition']['P_homogeneous_multidegree'], [201, 201, 196, 196])
        for o, q in zip(owners, result['Q_definitions']):
            self.assertEqual(tuple(q['owned_degree']), D.C_degree(o, (0, 1)))
        profile = result.pop('metadata_profile')
        arrays = [result['P_definition']['program']['dag']]
        arrays += [q[key]['nodes'] for q in result['Q_definitions'] for key in ('local_Q_AST', 'finite_C_AST', 'local_C_AST')]
        self.assertEqual(len(profile['stored_AST_arrays']), 10)
        self.assertEqual(profile['aggregate_stored_AST_nodes'], sum(map(len, arrays)))
        self.assertEqual(profile['serialized_payload_bytes'], len(json.dumps(result, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()))
        self.assertFalse(result['physical_execution_authorized'])
        self.assertFalse(result['actual_source_oracle_identity_accepted'])
        self.assertFalse(result['historical_source_order_equality'])
        # Review the actual bound objects' public refusal methods without describe.
        p = pmod.ActualPBinding.__new__(pmod.ActualPBinding)
        q = qmod.ActualQBinding.__new__(qmod.ActualQBinding)
        for method, args in ((p.coefficient, (None, None)), (p.alternating_coefficient, (None, None)), (q.coefficient, (None, None)), (q.factor_terms, (None,))):
            with self.assertRaises(I.PhysicalAdmissionMissing):
                method(*args, pair=None)

    def test_formal_unsymmetrized_transgression_requires_both_mixed_terms(self):
        # Free associative words: A has even total degree, B odd, dB=D.
        # This checks the local RAW derivation, not the scalar solver machinery.
        degree = {'A': 2, 'B': 1, 'D': 2}
        def differential(words):
            out = Counter()
            for word, coefficient in words.items():
                for j, letter in enumerate(word):
                    if letter == 'B':
                        out[word[:j]+('D',)+word[j+1:]] += coefficient*(-1)**sum(degree[x] for x in word[:j])
            return {w: c for w, c in out.items() if c}
        raw = {('B', 'A'): 1, ('A', 'B'): 1, ('B', 'D'): 1}
        expected = {('D', 'A'): 1, ('A', 'D'): 1, ('D', 'D'): 1}
        self.assertEqual(differential(raw), expected)  # (A+D)^2-A^2
        self.assertNotEqual(differential({('B', 'A'): 2, ('B', 'D'): 1}), expected)
        self.assertNotEqual(differential({('B', 'A'): 1, ('A', 'B'): 1}), expected)

    def test_fresh_increasing_edge_cup_correction_all_artificial_orders(self):
        # Vertex potentials supply cocycles on arbitrary ordered indices. Values
        # are evaluated on NEW increasing edges before alternating extension.
        potentials = {'z': (F(2, 3), F(-3, 5)), 'a': (F(7, 4), F(5, 2)), 'm': (F(-1, 2), F(4, 7))}
        def q(i, j, axis):
            return potentials[j][axis]-potentials[i][axis]
        for order in itertools.permutations(potentials):
            i, j, k = order
            r = lambda u, v: q(u, v, 0)*q(u, v, 1)
            dr = r(j, k)-r(i, k)+r(i, j)
            ab, ba = q(i, j, 0)*q(j, k, 1), q(i, j, 1)*q(j, k, 0)
            self.assertEqual(dr, -ab-ba)
            omega = (ab-ba)/4  # ordinary contraction of theta wedge theta
            b = F(15, 4)*ab
            self.assertEqual(F(30, 4)*omega-F(15, 8)*dr, b)
            self.assertNotEqual(F(30, 4)*omega+F(15, 8)*dr, b)
            # A raw nonlinear edge is symmetric here; alternation is imposed,
            # never inferred by re-evaluating that edge backwards.
            self.assertEqual(r(j, i), r(i, j))
            self.assertNotEqual(r(j, i), -r(i, j))

    def test_row_column_trace_sign_with_noncommuting_artificial_matrices(self):
        def mul(a, b):
            return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
        def tr(a):
            return a[0][0]+a[1][1]
        pa, pb = ((1, 2), (3, -1)), ((2, -1), (4, -2))
        qa, qb = ((3, 1), (-2, -3)), ((-1, 4), (2, 1))
        row_C_trace = F(tr(mul(qa, pb))-tr(mul(qb, pa)), 2)
        column_wedge_trace = tr(mul(qb, pa))-tr(mul(qa, pb))
        self.assertNotEqual(row_C_trace, 0)
        self.assertEqual(row_C_trace, -F(1, 2)*column_wedge_trace)
        self.assertEqual(F(1, 4)*column_wedge_trace, -F(1, 2)*row_C_trace)


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU, (59, 59))
    unittest.main()
