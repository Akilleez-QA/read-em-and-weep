"""TP-R: pure plans, tiny artificial values and guarded definition metadata.

Run directly, normally and with -O. Never enumerates an actual fiber or calls
an actual polynomial/coefficient implementation. Pins checked before import
and after the suite are provenance checks, never admission tokens.
"""
from contextlib import ExitStack
from dataclasses import FrozenInstanceError
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import resource
import subprocess
import sys
import types
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = HERE.parents[2]
MARKER_SHA = '03dbc4a68984e973528c9584bbf042f44e53c5f74579e7a0737884b3d1f591b1'
PINS_SHA = '84b292ec6a9f9260e0dfd52dd39aa2f8abd9c2f6d16b38948aabca0a675bd186'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def authenticate_snapshot():
    """Read-only closure of TP workspace pins and PB/QB/FD/QH exact pins."""
    result = {}
    def record(path, expected=None):
        raw = path.read_bytes()
        value = sha(raw)
        if expected is not None and value != expected:
            raise RuntimeError('review input drift: '+str(path))
        result[str(path.relative_to(ROOT))] = value
        return raw
    marker = json.loads(record(HERE/'producer-ready.json', MARKER_SHA))
    for name, expected in marker['files'].items():
        record(HERE/name, expected)
    tp = json.loads(record(HERE/'source-pins.json', PINS_SHA))
    for row in tp['workspace_inputs']:
        record(BASE/row['path'], row['sha256'])
    manifests = ('source-faithful-P', 'source-faithful-Q',
                 'source-domain-application', 'inner-quotient')
    immutable = {}
    for name in manifests:
        pins = json.loads(record(BASE/name/'source-pins.json'))
        for row in pins.get('workspace_inputs', []):
            record(BASE/row['path'], row['sha256'])
        for row in pins.get('canonical_definition_workspace_inputs', []):
            record(ROOT/row['path'], row['sha256'])
        for key in ('sources', 'immutable_dependencies'):
            for row in pins.get(key, []):
                immutable[(row['commit'], row['path'])] = row
    for (commit, path), row in immutable.items():
        raw = subprocess.check_output(['git', 'show', commit+':'+path], cwd=ROOT, timeout=10)
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if sha(raw) != row['sha256'] or blob != row['git_blob']:
            raise RuntimeError('immutable pin drift: '+path)
        if 'bytes' in row and len(raw) != row['bytes']:
            raise RuntimeError('immutable byte length drift: '+path)
        result[commit+':'+path] = sha(raw)
    # Record the imported acceptance premises without pretending their hashes
    # alone prove their semantic conclusions.
    for name in ('source-faithful-P', 'source-faithful-Q', 'source-domain-application'):
        record(BASE/name/'review-independent.md')
    return result


BEFORE = authenticate_snapshot()
import provider as P
I = P.I
Z = (0, 0, 0, 0)


def owner(c, m, t, j=0, seed=37):
    return I.FullOwner(seed, ('artificial', j), c, m, t)


def literal_key(o):
    return ((5, 0, 1, 2, 3, 4).index(o.carrier), o.legal_mask, o.standard_tag)


def reference(raw, kind):
    # Independent sign: count out-of-order input pairs, rather than using
    # source_key, sorted_source or the producer's permutation inversions.
    sign = -1 if sum(literal_key(a) > literal_key(b)
                    for i, a in enumerate(raw) for b in raw[i+1:]) % 2 else 1
    common = len({(o.carrier, o.legal_mask, o.standard_tag) for o in raw}) < len(raw)
    physical = len({(o.carrier, o.legal_mask) for o in raw}) < len(raw)
    reason = 'repeated_common' if common else 'source_F_repeated_physical' if kind == 'F' and physical else ''
    return sign, reason, physical


class Poison:
    def __getattribute__(self, name):
        raise AssertionError('request inspected: '+name)
    def __iter__(self):
        raise AssertionError('request iterated')
    def __bool__(self):
        raise AssertionError('request tested')
    def __eq__(self, other):
        raise AssertionError('request compared')


class Independent(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        if authenticate_snapshot() != BEFORE:
            raise RuntimeError('review inputs changed during tests')

    def check_plan(self, kind, raw, pair):
        p = P.request_plan(kind, raw, pair)
        sign, reason, physical = reference(raw, kind)
        expected_indices = tuple(sorted(range(len(raw)), key=lambda j: literal_key(raw[j])))
        self.assertEqual(p.permutation, expected_indices)
        self.assertEqual(p.sorted_owners, tuple(raw[j] for j in expected_indices))
        self.assertEqual(p.owners, tuple(raw))
        self.assertEqual(p.sorting_sign, sign)
        self.assertEqual(p.effective_sign, 0 if reason else sign)
        self.assertEqual(p.zero_reason, reason)
        self.assertEqual(p.repeated_physical, physical)
        self.assertEqual(p.occurrence_alias, len({o.occurrence for o in raw}) < len(raw))
        self.assertEqual(p.pair, tuple(pair))
        for key in ('actual_zero_coefficient_evaluated', 'source_slots_evaluated', 'physical_admission'):
            self.assertFalse(p.describe()[key])
        return p

    def test_artificial_permutations_all_roles_and_finite_degrees(self):
        pool = (owner(4, 0, 0, 0), owner(0, 15, 2, 1), owner(5, 15, 15, 2),
                owner(0, 15, 1, 3), owner(5, 0, 12, 4))
        for n in range(6):
            for raw in itertools.permutations(pool, n):
                for pair in ((0, 1), (2, 3)):
                    for kind in ('F', 'T', 'Rsharp') if n == 3 else ('T', 'Rsharp'):
                        self.check_plan(kind, raw, pair)
        # Arbitrary finite degree is a plan contract, not a solver-degree claim.
        raw = [pool[j % len(pool)] for j in range(129)]
        for kind in ('T', 'Rsharp'):
            self.check_plan(kind, raw, [2, 3])

    def test_repetition_properties_and_alias_is_not_a_zero_rule(self):
        labels = ((5, 1, 0), (5, 1, 8), (0, 0, 15), (5, 1, 0))
        for triple in itertools.product(labels, repeat=3):
            raw = tuple(owner(*label, j) for j, label in enumerate(triple))
            for kind in ('F', 'T', 'Rsharp'):
                self.check_plan(kind, raw, (0, 1))
        raw = (owner(5, 1, 0, 7), owner(0, 0, 8, 7), owner(4, 15, 15, 7))
        for kind in ('F', 'T', 'Rsharp'):
            p = self.check_plan(kind, raw, (2, 3))
            self.assertTrue(p.occurrence_alias)
            self.assertEqual(p.effective_sign, 1)
        # Occurrence/seed do not create new common vertices.
        raw = (owner(5, 1, 0, 0), owner(5, 1, 0, 1), owner(4, 0, 0, 2))
        self.assertEqual(P.request_plan('Rsharp', raw).zero_reason, 'repeated_common')

    def test_plan_and_full_owner_immutable_with_detached_descriptions(self):
        occurrence = ['nested', [2, 'x']]
        a = I.FullOwner(37, occurrence, 5, 1, 8)
        raw = [a, owner(0, 2, 1, 1), owner(4, 3, 15, 2)]
        p = P.request_plan('F', raw)
        occurrence[1].append('mutation'); raw.reverse()
        self.assertEqual(p.owners[0].occurrence, ('nested', (2, 'x')))
        self.assertIs(p.owners[0], a)
        for obj, field, value in ((p, 'owners', ()), (p, 'effective_sign', 0),
                                   (a, 'seed', 99), (a, 'standard_tag', 0)):
            with self.assertRaises(FrozenInstanceError):
                setattr(obj, field, value)
        d = p.describe(); d['owners'].clear(); d['effective_sign'] = 77
        self.assertEqual(len(p.owners), 3)
        self.assertEqual(p.effective_sign, 1)
        self.assertEqual(len(p.describe()['owners']), 3)

    def test_full96_bijection_proof_and_boundary_index_plans_only(self):
        # Euclidean division gives unique c,m with 0<=m<16; 0<=k<96
        # iff 0<=c<6. Inverse 16*c+m proves completeness, no scan needed.
        d = P.Full96Descriptor(37, ['slot', [4]], 8)
        for k, expected in ((0, (0, 0)), (15, (0, 15)), (16, (1, 0)),
                            (79, (4, 15)), (80, (5, 0)), (95, (5, 15))):
            label = d.label_plan(k)
            self.assertEqual(label, (37, ('slot', (4,)), *expected, 8))
            self.assertEqual(16*label[2]+label[3], k)
        desc = d.describe()
        self.assertEqual(desc['index_domain'], [0, 95])
        self.assertEqual(desc['cardinality'], 6*16)
        self.assertEqual(desc['mask_encoding'], 'low bit i')
        self.assertEqual(desc['standard_encoding'], 'high bit3-i')
        self.assertTrue(desc['zero_weight_labels_retained'])
        desc['index_domain'][0] = -99
        self.assertEqual(d.describe()['index_domain'], [0, 95])
        for bad in (-1, 96, True, False, 1.0, '0', None):
            with self.assertRaises(ValueError):
                d.label_plan(bad)
        with self.assertRaises(FrozenInstanceError):
            d.standard_tag = 0
        for action in (lambda: iter(d), lambda: d.owners(Poison(), verified=True)):
            with self.assertRaises(I.PhysicalAdmissionMissing):
                action()

    def test_exact_input_validation_survives_optimization(self):
        good = (owner(5, 0, 0), owner(0, 1, 8, 1), owner(4, 15, 15, 2))
        for kind, raw, pair in (('unknown', good, (0, 1)), ('F', (), (0, 1)),
                                ('F', good+good[:1], (0, 1)), ('T', iter(good), (0, 1)),
                                ('T', [object()], (0, 1)), ('T', (), (False, True)),
                                ('T', (), (1, 0)), ('T', (), (0, 1, 2)),
                                ('T', [good[0], owner(1, 0, 0, seed=38)], (0, 1))):
            with self.assertRaises(ValueError):
                P.request_plan(kind, raw, pair)
        for args in ((True, 'x', 0), (0, {}, 0), (0, 'x', 16)):
            with self.assertRaises(ValueError):
                P.Full96Descriptor(*args)

    def test_tiny_artificial_coefficients_one_sign_no_stronger_zero_transfer(self):
        raw = (owner(5, 1, 0, 0), owner(5, 1, 8, 1), owner(4, 2, 15, 2))
        keys = tuple((o.carrier, o.legal_mask, o.standard_tag) for o in raw)
        values = {(kind, keys, Z, pair): Fraction(7, 11)
                  for kind in ('T', 'Rsharp') for pair in ((0, 1), (2, 3))}
        supplied = [raw[0]]
        toy = P.ToyProvider(values, {0: supplied})
        values.clear(); supplied.clear()
        self.assertEqual(tuple(toy.owners(0)), (raw[0],))
        for request in itertools.permutations(raw):
            for pair in ((0, 1), (2, 3)):
                self.assertEqual(toy.coefficient('F', request, Z, pair), 0)
                for kind in ('T', 'Rsharp'):
                    self.assertEqual(toy.coefficient(kind, request, Z, pair), reference(request, kind)[0]*Fraction(7, 11))
        for kind in ('F', 'T', 'Rsharp'):
            self.assertEqual(toy.coefficient(kind, (raw[0], raw[0], raw[2]), Z), 0)
        distinct = (raw[0], owner(0, 2, 8, 1), raw[2])
        fkeys = tuple(o.common_key for o in distinct)
        ftoy = P.ToyProvider({('F', fkeys, Z, (0, 1)): Fraction(5, 13)}, {})
        for request in itertools.permutations(distinct):
            self.assertEqual(ftoy.coefficient('F', request, Z), reference(request, 'F')[0]*Fraction(5, 13))
        with self.assertRaises(ValueError):
            toy.coefficient('T', raw, (1, 0, 0, 0))
        with self.assertRaises(ValueError):
            tuple(toy.owners(1))
        for values, fibers in (({('x',): 1.0}, {}), ({}, {0: [raw[0]]*2}),
                                ({}, {0: [raw[0]]*5}), ({}, {16: []})):
            with self.assertRaises(ValueError):
                P.ToyProvider(values, fibers)

    def test_actual_gate_before_normalization_validation_zero_or_support(self):
        actual = P.ActualProvider()
        a = owner(5, 1, 0, 0)
        zero = (a, a, owner(4, 0, 15, 2))
        physical_zero = (a, owner(5, 1, 8, 1), owner(4, 0, 15, 2))
        for mode in ('physical', 'synthetic', 'verified', None):
            actual.mode = mode
            actual.verified = actual.physical_admission = True
            actual.pins['actual_execution'] = True
            with ExitStack() as stack:
                for obj, name in ((P, 'request_plan'), (P, 'pair'), (I, 'exponent'),
                                  (actual.domain, 'describe'), (I.FullOwner, 'source_key'),
                                  (I.FullOwner, 'common_key'), (I.FullOwner, 'physical_key')):
                    stack.enter_context(patch.object(obj, name, side_effect=AssertionError('gate bypass')))
                for method in (actual.coefficient, actual.alternating_coefficient, actual.factor_terms, actual.owners):
                    for args, kwargs in (((), {}), ((Poison(), Poison()), {'pair': Poison()}),
                                          (('F', (), (-999,)), {'mode': 'synthetic', 'verified': True}),
                                          (('F', zero, Z), {}),
                                          (('F', physical_zero, Z), {}),
                                          (('T', zero, (10**9, 0, 0, 0)), {}),
                                          (('F', [None]*3, Z), {})):
                        with self.assertRaises(I.PhysicalAdmissionMissing):
                            method(*args, **kwargs)

    def test_only_eligible_F_triple_joins_and_original_owners_forwarded(self):
        actual = P.ActualProvider()
        a, b, c = owner(5, 0, 0, 0), owner(0, 1, 8, 1), owner(4, 15, 15, 2)
        alias = owner(0, 1, 8, 0)
        physical = owner(5, 0, 8, 1)
        nonjoins = [('F', (a, a, c)), ('F', (a, physical, c)), ('F', (a, alias, c))]
        nonjoins += [(kind, raw) for kind in ('T', 'Rsharp')
                     for raw in ((), (a,), (b, a, c), (a, physical, c), (a, a, c), (a, alias, c))]
        with patch.object(actual.domain, 'describe', side_effect=AssertionError('ineligible join')):
            for kind, raw in nonjoins:
                d = actual.describe(kind, raw)
                self.assertNotIn('source_definition', d)
                self.assertFalse(d['whole_T_or_Rsharp_implementation_supplied'])
                self.assertFalse(d['aggregate_budget_certificate'])
                self.assertEqual(len(d['fiber_domains']), len(raw))
                self.assertTrue(d['normalization_only'])
        # Spy metadata is an artificial adversarial control, not acceptance of
        # a callback-provided source. Constructor injection is separately denied.
        for raw in itertools.permutations((a, b, c)):
            sign = reference(raw, 'F')[0]
            with patch.object(actual.domain, 'describe', return_value={'source_sorting_sign': sign}) as join:
                d = actual.describe('F', raw, [2, 3])
                join.assert_called_once_with(raw, (2, 3))
                self.assertEqual(d['effective_sign'], sign)
            with patch.object(actual.domain, 'describe', return_value={'source_sorting_sign': -sign}):
                with self.assertRaises(ValueError):
                    actual.describe('F', raw)

    def test_canonical_repo_and_foreign_module_rejection(self):
        with patch.object(P, '_authenticate', side_effect=AssertionError('auth too early')):
            for repo in ('/tmp', HERE/'foreign'):
                with self.assertRaises(ValueError):
                    P.ActualProvider(repo)
        for kwargs in ({'catalog': object()}, {'callback': lambda: 0}, {'verified': True}, {'pins': {}}):
            with self.assertRaises(TypeError):
                P.ActualProvider(**kwargs)
        for name in ('tp_actual_domain',):
            with patch.dict(sys.modules, {name: types.SimpleNamespace(__file__='/tmp/foreign.py')}):
                with self.assertRaises(ValueError):
                    P.ActualProvider()
        with patch.object(I, '__file__', '/tmp/interfaces.py'):
            with self.assertRaises(ValueError):
                P._authenticate()
        D = P.ActualProvider().domain
        dm = sys.modules[D.__class__.__module__]
        for name, path in (('fd_actual_P_binding', BASE/'source-faithful-P/p_binding.py'),
                           ('fd_actual_Q_binding', BASE/'source-faithful-Q/q_binding.py')):
            with patch.dict(sys.modules, {name: types.SimpleNamespace(__file__='/tmp/foreign.py')}):
                with self.assertRaises(ValueError):
                    dm._canonical_module(name, path)
        self.assertEqual(P.ActualProvider(ROOT/'.').repo, ROOT)

    def test_pin_byte_tamper_is_detected_without_editing_dependencies(self):
        original = Path.read_bytes
        target = BASE/'standard-coefficients/standard.py'
        def tamper(path):
            raw = original(path)
            return raw+b'\n# artificial drift\n' if path == target else raw
        with patch.object(Path, 'read_bytes', tamper):
            with self.assertRaisesRegex(ValueError, 'dependency drift'):
                P._authenticate()

    def test_one_canonical_join_AST_only_and_one_FD_sort(self):
        actual = P.ActualProvider()
        D = sys.modules['tp_actual_domain']
        pm = D._canonical_module('fd_actual_P_binding', BASE/'source-faithful-P/p_binding.py')
        qm = D._canonical_module('fd_actual_Q_binding', BASE/'source-faithful-Q/q_binding.py')
        import polynomial_coefficients as PC
        # Same explicitly recorded handoff triple as accepted FD; not a scan.
        raw = (I.FullOwner(12, ('toy-contract-slot', 1), 0, 3, 8),
               I.FullOwner(12, ('toy-contract-slot', 0), 5, 0, 0),
               I.FullOwner(12, ('toy-contract-slot', 2), 4, 15, 12))
        with ExitStack() as stack:
            for cls, names in ((PC.Ring, ('coefficient', '_coefficient', 'polynomial')),
                               (PC.Catalog, ('cleared',)), (PC.ClearedSourceProgram, ('__init__',)),
                               (qm.QH.FiniteRing, ('_coefficient',)),
                               (D.FullFiberDomain, ('__iter__', 'owners')),
                               (P.Full96Descriptor, ('__iter__', 'owners'))):
                for name in names:
                    stack.enter_context(patch.object(cls, name, side_effect=AssertionError('physical operation forbidden')))
            sort = stack.enter_context(patch.object(I, 'sorted_source', wraps=I.sorted_source))
            desc = actual.describe('F', raw, (2, 3))
            self.assertEqual(sort.call_count, 1)
        sd = desc['source_definition']
        ordered = [raw[j].data() for j in (1, 0, 2)]
        self.assertEqual(desc['sorting_sign'], -1)
        self.assertEqual(desc['effective_sign'], -1)
        self.assertEqual(sd['source_sorting_sign'], -1)
        self.assertEqual(sd['source_sorted_owners'], ordered)
        self.assertEqual(sd['P_definition']['ordered_owners'], [list(o) for o in ordered])
        self.assertEqual([tuple(q['owner']) for q in sd['Q_definitions']], [o.data() for o in raw])
        self.assertEqual(sd['whole_P_exact_homogeneous_degree'], (196, 196, 199, 199))
        self.assertEqual(len(sd['P_definition']['program']['dag']), 153)
        self.assertEqual(len(desc['fiber_domains']), 3)
        for o, fd in zip(raw, desc['fiber_domains']):
            self.assertEqual((fd['seed'], fd['occurrence'], fd['standard_tag']), (o.seed, o.occurrence, o.standard_tag))
            self.assertEqual(fd['cardinality'], 96)
        for key in ('physical_admission', 'actual_zero_coefficient_evaluated',
                    'aggregate_budget_certificate', 'whole_T_or_Rsharp_implementation_supplied'):
            self.assertFalse(desc[key])
        self.assertFalse(sd['physical_execution_authorized'])
        self.assertFalse(sd['metadata_profile']['aggregate_resource_supervisor_present'])
        json.dumps(desc, allow_nan=False)


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU, (59, 59))
    unittest.main()
