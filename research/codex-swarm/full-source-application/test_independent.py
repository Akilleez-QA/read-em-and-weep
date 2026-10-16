"""RS-R focused controls. Only explicit artificial algebra is evaluated.

Reuse SC-R's reviewed tiny polynomial/evaluator helpers; never run its tests,
compile a graph, lower a physical leaf, or request an actual coefficient.
"""
import copy
from contextlib import ExitStack
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import unittest
from unittest import mock

import r_binding as R
import formal_identities as F

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MARKER = '883490825f5d1b1156ad865e9852ef64e314322418409c9de3b71041f07d3616'
HELPERS = HERE.parent/'scalar-compiler/test_independent.py'
if hashlib.sha256(HELPERS.read_bytes()).hexdigest() != '040b047195aa4ab34077ca011cebf352866943e92717749ae73621656602ce3f':
    raise ValueError('reviewed artificial helpers drift')
spec = importlib.util.spec_from_file_location('rs_reviewed_artificial_helpers', HELPERS)
A = importlib.util.module_from_spec(spec)
spec.loader.exec_module(A)


def plus(*ps):
    out = {}
    for p in ps:
        for w, z in p.items(): out[w] = out.get(w, 0) + z
    return {w: z for w, z in out.items() if z}


def sc(p, z): return {w: v*z for w, v in p.items() if v*z}


def times(*ps):
    out = {(): Q(1)}
    for p in ps:
        out = plus(*({a+b: x*y} for a, x in out.items() for b, y in p.items()))
    return out


def word(s): return {tuple(s.split()): Q(1)}


def jetmul(a, b):
    return [plus(*(times(a[j], b[n-j]) for j in range(n+1))) for n in range(3)]


def artificial():
    # All inputs here are fabricated SL2 polynomials over Q[x0,...,x3].
    x = [A.P({tuple(int(i == j) for j in range(4)): 1}) for i in range(4)]
    a = A.mul(A.upper(x[0]+x[2]), A.lower(x[1]+x[3]))
    b = A.mul(A.upper(x[3]), A.lower(x[0]*x[2]+x[1]))
    gs = (a, b, A.mul(b, a))
    ss = ((x[0]*x[3]+1, x[1]+x[2], x[0]-x[2]*x[3]),
          (x[1]*x[2], x[3]+2, x[0]*x[1]+x[2]))
    linear = sum(x, A.P())
    ss = tuple(tuple(t+linear for t in row) for row in ss)
    return x, gs, ss


def currents(gs, p, s):
    a, b, _ = gs
    i, j = p
    L = lambda d: A.mul(A.inv(a), A.der(a, d))
    U = lambda d: A.mul(A.mul(A.mul(A.inv(a), A.inv(b)), A.der(b, d)), a)
    terms = (A.scale(L(j), s[1].d(i)), A.scale(L(i), -s[1].d(j)),
             A.scale(U(i), s[0].d(j)), A.scale(U(j), -s[0].d(i)))
    return A.scale(A.add(*terms), Q(1, 2)), terms


def mixed(gs, us, bs):
    a, b, g = gs
    p, q = (0, 1), (2, 3)
    up, uq = us
    kinetic = (A.mul(up[1], uq[0]), A.mul(uq[1], up[0]),
               A.mu(uq[1], a, p), A.mu(up[1], a, q),
               A.mu(b, uq[0], p), A.mu(b, up[0], q), A.mu2(b, a))
    gerbe = (A.scale(uq[2], -bs[0]), A.scale(up[2], -bs[1]), A.scale(g, -bs[0]*bs[1]))
    return A.mul(A.inv(g), A.add(*(kinetic+gerbe))), kinetic, gerbe


class IndependentRS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in HERE.iterdir() if p.is_file() and p.name not in ('test_independent.py', 'review-independent.md')}
        cls.app = R.ActualFullSourceApplication()
        cls.pins, cls.raw = R.authenticate(ROOT)
        cls.D = cls.app._domain
        cls.I = cls.D.I

    @classmethod
    def tearDownClass(cls):
        after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in HERE.iterdir() if p.is_file() and p.name not in ('test_independent.py', 'review-independent.md')}
        if after != cls.before: raise AssertionError('producer bytes changed during independent controls')

    def test_snapshot_and_every_exact_pin(self):
        self.assertEqual(hashlib.sha256((HERE/'producer-ready.json').read_bytes()).hexdigest(), MARKER)
        m = json.loads((HERE/'producer-ready.json').read_bytes())
        for name, digest in m['files'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), digest, name)
        self.assertEqual(len(self.pins['sources']), 20)
        for row in self.pins['sources']:
            raw = self.raw[row['commit'], row['path']]
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'])
            self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(), row['git_blob'])

    def test_independent_free_defect_expansion_and_both_descent_remainders(self):
        # Eikl=VW-BH, Eijk=YZ-AW, Eijl=TZ-DH, Fij(Ejkl)=XY-CT.
        pieces = (plus(word('A V W'), sc(word('A B H'), -1)),
                  plus(word('X Y Z'), sc(word('X A W'), -1)),
                  plus(word('C T Z'), sc(word('C D H'), -1)),
                  plus(word('X Y Z'), sc(word('C T Z'), -1)))
        expanded = plus(*(sc(p, z) for p, z in zip(pieces, (1, 1, -1, -1))))
        b1 = plus(word('A V W'), sc(word('X A W'), -1))
        b2 = plus(word('C D H'), sc(word('A B H'), -1))
        self.assertEqual(expanded, plus(b1, b2))
        self.assertEqual(F.defect_syzygy(), (expanded, plus(b1, b2)))
        self.assertTrue(b1); self.assertTrue(b2)
        self.assertNotEqual(expanded, b1); self.assertNotEqual(expanded, b2)
        for j in range(4):
            signs = [1, 1, -1, -1]; signs[j] *= -1
            self.assertNotEqual(plus(*(sc(p, z) for p, z in zip(pieces, signs))), expanded)

    def test_first_unsolved_jet_coefficient_needs_lower_defects_zero(self):
        one = {(): Q(1)}
        ae = jetmul([one, word('b'), word('a2')], [{}, {}, word('Rikl')])
        xe = jetmul([word('gkl'), word('x1'), word('x2')], [{}, {}, word('Rijk')])
        ce = jetmul([one, word('c1'), word('c2')], [{}, {}, word('Rijl')])
        ez = jetmul([{}, {}, word('Rjkl')], [word('gij'), word('z1'), word('z2')])
        result = plus(ae[2], xe[2], sc(ce[2], -1), sc(ez[2], -1))
        self.assertEqual(result, plus(word('Rikl'), word('gkl Rijk'), sc(word('Rijl'), -1), sc(word('Rjkl gij'), -1)))
        bad = jetmul([one, word('b'), word('a2')], [{}, word('E1'), word('Rikl')])
        self.assertEqual(plus(bad[2], sc(ae[2], -1)), word('b E1'))
        # h2 here is extracted only AFTER the universal unprojected identity.

    def test_artificial_exact_reduction_positive_boundary_and_nonzero_trace(self):
        _, gs, ss = artificial()
        pairs = ((0, 1), (2, 3))
        ks = [[A.scale(A.mu(A.inv(g), g, p), -Q(1, 2)) for g in gs] for p in pairs]
        cs = [A.mul(A.inv(gs[2]), A.mu(gs[1], gs[0], p)) for p in pairs]
        fs = [s[1]-s[2]+s[0] for s in ss]
        bs = [f+Q(1, 2)*A.tr(c) for f, c in zip(fs, cs)]
        for k, c in zip(ks, cs):
            dk = A.add(A.mul(A.mul(A.inv(gs[0]), k[1]), gs[0]), A.scale(k[2], -1), k[0])
            self.assertEqual(dk, A.scale(A.tf(c), -1))
        zero_us = [[A.mul(g, k) for g, k in zip(gs, kk)] for kk in ks]
        fresh_us = [[A.mul(g, A.add(k, A.scale(A.I, s))) for g, k, s in zip(gs, kk, st)] for kk, st in zip(ks, ss)]
        m0, _, _ = mixed(gs, zero_us, bs)
        m, _, _ = mixed(gs, fresh_us, bs)
        es = [currents(gs, pairs[j], ss[1-j])[0] for j in range(2)]
        rsharp = A.add(A.tf(m0), A.scale(ks[0][2], fs[1]), A.scale(ks[1][2], fs[0]), *es)
        w = [A.add(A.scale(ks[0][j], ss[1][j]), A.scale(ks[1][j], ss[0][j])) for j in range(3)]
        dw = A.add(A.mul(A.mul(A.inv(gs[0]), w[1]), gs[0]), A.scale(w[2], -1), w[0])
        self.assertEqual(rsharp, A.add(A.tf(m), dw))
        self.assertNotEqual(dw, A.O)
        self.assertNotEqual(rsharp, A.tf(m))
        self.assertNotEqual(rsharp, A.add(A.tf(m), A.scale(dw, -1)))
        self.assertTrue(A.tr(m))  # No pointwise central-vanishing assertion.
        self.assertEqual(F.reduction_identity(), {})
        self.assertTrue(F.reduction_identity(-1))

    def test_existing_twenty_source_records_against_artificial_formula(self):
        x, gs, ss = artificial()
        pairs = ((0, 1), (2, 3))
        ks = [[A.scale(A.mu(A.inv(g), g, p), -Q(1, 2)) for g in gs] for p in pairs]
        records = self.app._template['source_residual_components']
        self.assertEqual([r['owners'] for r in records], [list(t) for t in itertools.combinations(range(6), 3)])
        nodes = self.app._template['nodes']
        for record, bound in zip(records, self.app._source):
            i, j, k = record['owners']; edges = ((i, j), (j, k), (i, k))
            qs = {(e, d): x[d]+(a+1)*(d+2) for a, e in enumerate(edges) for d in range(4)}
            bs = [Q(15, 4)*qs[edges[0], p[0]]*qs[edges[1], p[1]] for p in pairs]
            fs = [b-Q(1, 2)*A.tr(A.mul(A.inv(gs[2]), A.mu(gs[1], gs[0], p))) for b, p in zip(bs, pairs)]
            us = [[A.mul(g, kk) for g, kk in zip(gs, kp)] for kp in ks]
            m0, kinetic, gerbe = mixed(gs, us, bs)
            expected = {'baseline': A.tf(m0), 'Fk12': A.scale(ks[0][2], fs[1]), 'Fk34': A.scale(ks[1][2], fs[0]),
                        'E12': currents(gs, pairs[0], ss[1])[0], 'E34': currents(gs, pairs[1], ss[0])[0]}
            def leaf(n):
                e = tuple(n['owners'])
                if n['name'] == 'g_phys': return gs[edges.index(e)]
                if n['name'] == 'physical_q': return ((qs[e, n['coordinate']],),)
                raise AssertionError('non-source leaf in artificial assignment')
            def solver(n): return ss[pairs.index(tuple(n['pair']))][edges.index(tuple(n['owners']))]
            cache = {}
            evaluate = lambda root: A.peval(nodes, root, leaf, solver, cache)
            for name, root in bound['component_roots'].items(): self.assertEqual(evaluate(root), expected[name], (record['owners'], name))
            self.assertEqual(evaluate(bound['M0_root']), m0)
            self.assertEqual([evaluate(n) for n in bound['kinetic_roots']], list(kinetic))
            self.assertEqual([evaluate(n) for n in bound['gerbe_roots']], list(gerbe))
            self.assertEqual(evaluate(bound['Rsharp_root']), A.add(*expected.values()))
            if record['owners'] == [0, 1, 2]:
                for target in (bound['gerbe_roots'][0], bound['gerbe_roots'][1],
                               bound['kinetic_roots'][6], bound['component_roots']['E12'],
                               bound['component_roots']['E34']):
                    bad = copy.deepcopy(nodes)
                    self.assertEqual(bad[target]['op'], 'rational_scale')
                    bad[target]['coefficient'][0] *= -1
                    self.assertNotEqual(A.peval(bad, bound['Rsharp_root'], leaf, solver), A.add(*expected.values()))
                bad = copy.deepcopy(nodes)
                bad[bound['M0_root']]['children'].reverse()
                self.assertNotEqual(A.peval(bad, bound['Rsharp_root'], leaf, solver), A.add(*expected.values()))
        # Both E endpoint contributions and every sign are observable here.
        for p, s in zip(pairs, ss[::-1]):
            e, terms = currents(gs, p, s)
            for term in terms: self.assertNotEqual(e, A.add(e, A.scale(term, -1)))
        # Transpose reverses row products; it is applied after the formula.
        self.assertNotEqual(A.trans(A.mul(gs[1], gs[0])), A.mul(A.trans(gs[1]), A.trans(gs[0])))

    def test_artificial_ambient_cup_descent_and_exponential_second_jet(self):
        # Explicit fabricated vertex potentials and derivatives; no curve value.
        v = ((Q(0), Q(2, 3), Q(-1), Q(4, 5)),
             (Q(1), Q(0), Q(3, 2), Q(-2)))
        a = ((Q(3), Q(-1), Q(2, 5), Q(0)),
             (Q(-2), Q(1, 4), Q(0), Q(5)))
        q = lambda d, i, j: v[d][j]-v[d][i]
        da = lambda d, i, j: a[d][j]-a[d][i]
        b = lambda i, j, k: Q(15, 4)*q(0, i, j)*q(1, j, k)
        # T edge coefficients in order (V0,V1).
        t = lambda i, j: (Q(15, 4)*q(0, i, j)*a[1][j], Q(15, 4)*a[0][i]*q(1, i, j))
        observed = 0
        for i, j, k, l in itertools.permutations(range(4)):
            self.assertEqual(b(j, k, l)-b(i, k, l)+b(i, j, l)-b(i, j, k), 0)
            dt = tuple(t(j, k)[d]-t(i, k)[d]+t(i, j)[d] for d in range(2))
            poisson = (-Q(15, 4)*q(0, i, j)*da(1, j, k), Q(15, 4)*da(0, i, j)*q(1, j, k))
            self.assertEqual(dt, poisson)
            observed += dt != tuple(-z for z in poisson)
            x, y, z, w = b(i, j, k), b(i, k, l), b(j, k, l), b(i, j, l)
            self.assertEqual(x+y, z+w)
            self.assertEqual(x*x/2+x*y+y*y/2, z*z/2+z*w+w*w/2)
        self.assertGreater(observed, 0)

    def test_moyal_square_and_moving_frame_jet_controls(self):
        pi = ((0, 1, 1), (1, 0, -1), (2, 3, 1), (3, 2, -1))
        coeff = {}
        for i, j, z in pi:
            for k, l, w in pi:
                if len({i, j, k, l}) == 4:
                    key = (tuple(sorted((i, k))), tuple(sorted((j, l))))
                    coeff[key] = coeff.get(key, 0)+Q(z*w, 8)
        self.assertEqual(coeff, {((0, 2), (1, 3)): Q(1, 4), ((0, 3), (1, 2)): -Q(1, 4),
                                 ((1, 2), (0, 3)): -Q(1, 4), ((1, 3), (0, 2)): Q(1, 4)})
        s = A.mat(((1, 0), (0, -1))); g = A.upper(A.P(1))
        dg = A.add(A.mul(s, g), A.scale(A.mul(g, s), -1))
        self.assertEqual(dg, A.mat(((0, 2), (0, 0))))
        self.assertNotEqual(dg, A.O)  # Frame value I does not kill frame jets.

    def test_guarded_canonical_description_both_pairs_and_order(self):
        I, D = self.I, self.D
        owners = (I.FullOwner(12, ('RS-explicit', 0), 5, 0, 0),
                  I.FullOwner(12, ('RS-explicit', 1), 0, 3, 8),
                  I.FullOwner(12, ('RS-explicit', 2), 4, 15, 12))
        pm = D._canonical_module('fd_actual_P_binding', HERE.parent/'source-faithful-P/p_binding.py')
        qm = D._canonical_module('fd_actual_Q_binding', HERE.parent/'source-faithful-Q/q_binding.py')
        import polynomial_coefficients as PC
        with ExitStack() as stack:
            for cls, names in ((PC.Ring, ('coefficient', '_coefficient', 'polynomial')), (PC.Catalog, ('cleared',)),
                               (PC.ClearedSourceProgram, ('__init__',)), (qm.QH.FiniteRing, ('_coefficient',)),
                               (D.FullFiberDomain, ('__iter__', 'owners', 'coefficient'))):
                for name in names: stack.enter_context(mock.patch.object(cls, name, side_effect=AssertionError('physical evaluation/fiber forbidden')))
            result = self.app.describe(owners)
        self.assertEqual(result['SC_source_reference']['slot_binding'], {str(i): list(o.data()) for i, o in enumerate(owners)})
        self.assertEqual(result['SC_source_reference']['bound_triple_record']['compiler_owner_slots'], [0, 1, 2])
        fd = result['fresh_first_lift']['FD_actual_definitions']
        self.assertEqual([d['pair'] for d in fd], [(0, 1), (2, 3)])
        for d, p in zip(fd, ((0, 1), (2, 3))):
            self.assertEqual(d['source_sorting_sign'], 1)
            self.assertEqual(d['P_definition']['ordered_owners'], [list(o.data()) for o in owners])
            self.assertFalse(d['P_definition']['physical_Q_is_gerbe_q'])
            for o, q in zip(owners, d['Q_definitions']):
                self.assertEqual(tuple(q['owner']), o.data())
                self.assertEqual(tuple(q['owned_degree']), D.C_degree(o, p))
        self.assertIn('D_b*', result['actual_physical_leaf_dictionary']['g_phys'])
        self.assertIn('transpose only for later', result['actual_physical_leaf_dictionary']['normalization'])
        for key in ('physical_execution_admitted', 'physical_coefficients_evaluated', 'actual_fibers_enumerated',
                    'historical_order_comparison_established', 'outer_full54_29_5251_domain_discharged',
                    'J0_J3_lift_extension_discharged', 'obstruction_decided'): self.assertIs(result[key], False)
        result['SC_source_reference']['universal_source_triples'].clear()
        self.assertEqual(len(self.app._source), 20)
        for bad in (owners[::-1], owners[:2], (owners[0], owners[0], owners[2]),
                    (owners[0], owners[1], I.FullOwner(13, 'other', 4, 15, 12)),
                    (owners[0], owners[1], I.FullOwner(12, owners[0].occurrence, 4, 15, 12))):
            with self.assertRaises(ValueError): self.app.describe(bad)

    def test_source_contract_branch_gerbe_sign_and_frame_binding(self):
        t = self.app._template
        mutations = [lambda b: b['Rsharp_components'].reverse(),
                     lambda b: b['source_residual_components'].pop(),
                     lambda b: b['source_residual_components'][0]['baseline']['gerbe_terms'].pop(),
                     lambda b: b['source_residual_components'][0]['components'].pop('E34'),
                     lambda b: next(n for n in b['nodes'] if n['op'] == 'physical_jet').__setitem__('frames_differentiated', False)]
        for mutate in mutations:
            b = copy.deepcopy(t); mutate(b)
            with self.assertRaises(ValueError): R.compiler_source_contract(b)
        # This helper is structural, not an arbitrary-template authenticator:
        # actual sign/owner/leaf bytes are fixed by authenticate(), then inspected
        # semantically above. Do not infer hostile Python mutation protection.
        for n in t['nodes']:
            if n['op'] == 'complete_inner_solver':
                self.assertEqual(n['partition'], {'carrier': 14, 'legal': 1, 'pair_specific': True})
                children = [t['nodes'][j] for j in n['children']]
                self.assertEqual([v['op'] for v in children], ['N14_Hrho', 'N14_R_Kcov_Pi', 'N14_R_A_h_S_Pi'])
                self.assertEqual([t['nodes'][j]['sign'] for j in children[0]['children']], [1, -1])
            elif n['op'] == 'physical_jet':
                self.assertTrue(n['frames_differentiated'])
                self.assertEqual(len(n['directions']), len(set(n['directions'])))
                self.assertLessEqual(len(n['directions']), 2)

    def test_byte_manifest_and_canonical_dependency_drift_refuse(self):
        for row in self.pins['sources']:
            key = row['commit'], row['path']
            def corrupt(rev, path):
                b = self.raw[rev, path]
                return b+b' ' if (rev, path) == key else b
            with self.assertRaisesRegex(ValueError, 'source bytes drift'): R.authenticate(ROOT, corrupt)
        original = Path.read_bytes
        def drift(path):
            b = original(path)
            return b+b' ' if path == HERE/'source-pins.json' else b
        with mock.patch.object(Path, 'read_bytes', drift):
            with self.assertRaisesRegex(ValueError, 'manifest drift'): R.authenticate(ROOT)
        target = ROOT/'research/codex-swarm/source-domain-application/domain.py'
        def localdrift(path): return original(path)+b' ' if path == target else original(path)
        with mock.patch.object(Path, 'read_bytes', localdrift):
            with self.assertRaisesRegex(ValueError, 'local canonical dependency drift'):
                R.authenticate(ROOT, lambda rev, path: self.raw[rev, path])
        pins = self.app.source_pins(); pins['sources'].clear()
        self.assertEqual(len(self.app.source_pins()['sources']), 20)

    def test_unconditional_physical_refusal_even_poison_modes_and_forged_gates(self):
        class Poison:
            def __iter__(self): raise AssertionError('request inspected')
            def __bool__(self): raise AssertionError('request inspected')
            def __index__(self): raise AssertionError('request inspected')
        a = self.app
        for kwargs in ({'source': lambda: True}, {'catalog': object()}, {'mode': 'synthetic'},
                       {'verified': True}, {'closure': True}, {'ambient': object()}):
            with self.assertRaises(TypeError): R.ActualFullSourceApplication(**kwargs)
        with self.assertRaises(AttributeError): a.mode = 'synthetic'
        for mode in ('physical', 'synthetic', 'verified', None):
            a.__dict__['mode'] = mode
            a.physical_execution_admitted = True
            a.closure = True
            for method in (a.coefficient, a.factor_terms, a.owners):
                for args, kw in (((), {}), ((Poison(),), {'pair': Poison(), 'mode': mode, 'verified': True}),
                                 (('invalid', (-10**9, False, None)), {})):
                    with self.assertRaises(self.I.PhysicalAdmissionMissing): method(*args, **kw)
        self.assertEqual(a.mode, 'physical')


if __name__ == '__main__': unittest.main()
