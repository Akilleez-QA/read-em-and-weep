"""Independent coefficient-free RS01 checks at the PR88 immutable pin.

All algebra below uses formal letters and exact rational numbers. It never
loads/evaluates the physical model, executes a compiler, creates a physical
jet, or iterates a physical fiber. Source files are read only as bytes/AST/JSON.
"""
import ast
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
import subprocess
import sys
import types
import unittest

REVIEW_COMMIT = 'd18d9810f7333d9f94a895c4e26985520cc60057'
RS_PATH = 'research/codex-swarm/full-source-application/'
PINS_SHA256 = '80de123d734a20c27de405cbef32282aedb6b9487cc0738f57c270e6d0f16c44'


class PinnedInputs:
    """Read immutable Git objects; optional snapshot mode reproduces this audit.

    Git mode is the public default and needs no unpublished input directory.
    It never fetches, checks out, modifies, or executes the repository. The
    four necessary immutable commits must already exist in the object store.
    """
    def __init__(self, repo=None, snapshot=None):
        if repo is not None and snapshot is not None:
            raise ValueError('select one input transport')
        self.repo = Path(repo) if repo is not None else Path(__file__).resolve().parent
        self.snapshot = Path(snapshot) if snapshot is not None else None
        self.cache = {}

    def read(self, commit, path):
        key = (commit, path)
        if key not in self.cache:
            if self.snapshot is None:
                try:
                    raw = subprocess.check_output(
                        ['git', '-C', str(self.repo), 'show', commit + ':' + path],
                        timeout=15, stderr=subprocess.PIPE)
                except subprocess.CalledProcessError as error:
                    raise RuntimeError('Cannot read immutable Git input ' + commit + ':' + path
                                       + '; use --repo with a checkout containing this commit. '
                                       + error.stderr.decode(errors='replace')) from error
            else:
                relative = ('full-source-application/' + path[len(RS_PATH):]
                            if commit == REVIEW_COMMIT and path.startswith(RS_PATH) else path)
                raw = (self.snapshot / relative).read_bytes()
            self.cache[key] = raw
        return self.cache[key]

    def rs(self, name):
        return self.read(REVIEW_COMMIT, RS_PATH + name)

    def pins(self):
        raw = self.rs('source-pins.json')
        if hashlib.sha256(raw).hexdigest() != PINS_SHA256:
            raise ValueError('immutable RS source-pin manifest drift')
        return json.loads(raw)

    def direct(self, path):
        row = next(row for row in self.pins()['sources'] if row['path'] == path)
        raw = self.read(row['commit'], row['path'])
        if hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError('immutable direct source drift: ' + path)
        return raw


INPUTS = PinnedInputs()


def atom(name, scalar=False):
    return {((name,), ()) if scalar else ((), (name,)): Q(1)}


ONE = {((), ()): Q(1)}
INVERSE = {'A': 'Ai', 'Ai': 'A', 'B': 'Bi', 'Bi': 'B',
           'D': 'Di', 'Di': 'D'}


def add(*expressions):
    out = {}
    for expression in expressions:
        for key, coefficient in expression.items():
            out[key] = out.get(key, Q(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def scale(expression, coefficient):
    return {key: value * coefficient for key, value in expression.items()
            if value * coefficient}


def neg(expression):
    return scale(expression, -1)


def mul(*expressions):
    result = ONE
    for expression in expressions:
        terms = []
        for (s, word), coefficient in result.items():
            for (t, tail), other in expression.items():
                reduced = []
                for letter in word + tail:
                    if reduced and INVERSE.get(letter) == reduced[-1]:
                        reduced.pop()
                    else:
                        reduced.append(letter)
                if len(reduced) > 12:
                    raise ValueError('tiny free-word length limit')
                terms.append({(tuple(sorted(s + t)), tuple(reduced)):
                              coefficient * other})
        result = add(*terms)
        if len(result) > 256:
            raise ValueError('tiny abstract term limit')
    return result


def jetmul(left, right):
    return [add(*(mul(left[j], right[n-j]) for j in range(n+1)))
            for n in range(3)]


class IndependentClosureChecks(unittest.TestCase):
    def test_01_exact_twenty_direct_source_pins_and_producer_marker(self):
        pins = INPUTS.pins()
        self.assertEqual(len(pins['sources']), 20)
        for row in pins['sources']:
            raw = INPUTS.read(row['commit'], row['path'])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['sha256'])
            blob = b'blob ' + str(len(raw)).encode() + b'\0' + raw
            self.assertEqual(hashlib.sha1(blob).hexdigest(), row['git_blob'])
        marker_raw = INPUTS.rs('producer-ready.json')
        self.assertEqual(hashlib.sha256(marker_raw).hexdigest(),
                         '883490825f5d1b1156ad865e9852ef64e314322418409c9de3b71041f07d3616')
        for name, digest in json.loads(marker_raw)['files'].items():
            self.assertEqual(hashlib.sha256(INPUTS.rs(name)).hexdigest(), digest)

    def test_02_universal_defect_syzygy_and_all_four_sign_mutations(self):
        A, B, C, D, H, V, W, X, Y, Z, T = map(atom, 'A B C D H V W X Y Z T'.split())
        pieces = (mul(A, add(mul(V, W), neg(mul(B, H)))),
                  mul(X, add(mul(Y, Z), neg(mul(A, W)))),
                  mul(C, add(mul(T, Z), neg(mul(D, H)))),
                  mul(add(mul(X, Y), neg(mul(C, T))), Z))
        signs = (1, 1, -1, -1)
        actual = add(*(scale(piece, sign) for piece, sign in zip(pieces, signs)))
        first = mul(add(mul(A, V), neg(mul(X, A))), W)
        second = mul(add(mul(C, D), neg(mul(A, B))), H)
        self.assertEqual(actual, add(first, second))
        self.assertTrue(first)
        self.assertTrue(second)
        self.assertNotEqual(actual, first)
        self.assertNotEqual(actual, second)
        for index in range(4):
            wrong = list(signs)
            wrong[index] *= -1
            self.assertNotEqual(add(*(scale(p, z) for p, z in zip(pieces, wrong))), actual)

    def test_03_first_unsolved_h2_coefficient_requires_lower_defects_zero(self):
        products = [jetmul([ONE, atom('a1'), atom('a2')], [{}, {}, atom('Rikl')]),
                    jetmul([atom('D'), atom('x1'), atom('x2')], [{}, {}, atom('Rijk')]),
                    jetmul([ONE, atom('c1'), atom('c2')], [{}, {}, atom('Rijl')]),
                    jetmul([{}, {}, atom('Rjkl')], [atom('A'), atom('z1'), atom('z2')])]
        result = add(products[0][2], products[1][2], neg(products[2][2]), neg(products[3][2]))
        expected = add(atom('Rikl'), mul(atom('D'), atom('Rijk')),
                       neg(atom('Rijl')), neg(mul(atom('Rjkl'), atom('A'))))
        self.assertEqual(result, expected)
        wrong = jetmul([ONE, atom('a1'), atom('a2')], [{}, atom('E1'), atom('Rikl')])
        self.assertEqual(add(wrong[2], neg(products[0][2])), mul(atom('a1'), atom('E1')))

    def test_04_row_left_normalization_gives_negative_quadruple_identity(self):
        A, B, D, Ai, Bi, Di = map(atom, ('A', 'B', 'D', 'Ai', 'Bi', 'Di'))
        rij, rik, rjl, rjk = map(atom, ('Rijk', 'Rikl', 'Rijl', 'Rjkl'))
        delta_left = add(mul(Ai, Bi, Di, rjk, A), neg(mul(Ai, Bi, Di, rik)),
                         mul(Ai, Bi, Di, rjl), neg(mul(Ai, Bi, rij)))
        actual = mul(D, B, A, delta_left)
        expected = add(mul(rjk, A), neg(rik), rjl, neg(mul(D, rij)))
        self.assertEqual(actual, expected)
        delta_wrong = add(mul(Ai, rjk, Bi, Di, A), neg(mul(rik, Ai, Bi, Di)),
                          mul(rjl, Ai, Bi, Di), neg(mul(rij, Ai, Bi)))
        self.assertNotEqual(mul(D, B, A, delta_wrong), expected)

    def test_05_scalar_linear_reduction_and_positive_boundary(self):
        sjk, sij, sik = [atom(s, True) for s in ('sjk', 'sij', 'sik')]
        kb, ki, ko = map(atom, ('kbar', 'kij', 'kik'))
        c0 = add(neg(kb), ko, neg(ki))
        difference = add(mul(sjk, ki), mul(sij, kb), mul(add(sjk, sij), c0))
        dw = add(mul(sjk, kb), neg(mul(sik, ko)), mul(sij, ki))
        f = add(sjk, neg(sik), sij)
        self.assertEqual(add(difference, dw), mul(f, ko))
        self.assertNotEqual(add(difference, neg(dw)), mul(f, ko))
        self.assertTrue(dw)

    def test_06_central_quadratic_difference_is_not_pointwise_zero(self):
        p = [atom(s, True) for s in ('pij', 'pjk', 'pik')]
        q = [atom(s, True) for s in ('qij', 'qjk', 'qik')]
        cp, cq = atom('cp', True), atom('cq', True)
        fp, fq = add(p[1], neg(p[2]), p[0]), add(q[1], neg(q[2]), q[0])
        bp, bq = add(fp, cp), add(fq, cq)
        actual = add(mul(p[1], q[0]), mul(q[1], p[0]),
                     mul(add(q[1], q[0]), cp), mul(add(p[1], p[0]), cq),
                     neg(mul(bp, q[2])), neg(mul(bq, p[2])))
        delta_product = add(mul(p[1], q[1]), neg(mul(p[2], q[2])), mul(p[0], q[0]))
        expected = add(neg(delta_product), mul(bp, bq), neg(mul(cp, cq)))
        self.assertEqual(actual, expected)
        self.assertTrue(actual)

    def test_07_both_endpoint_product_rules_and_all_current_signs(self):
        A, B, Ai, Bi = map(atom, ('A', 'B', 'Ai', 'Bi'))
        da, db, ea, eb = map(atom, ('dA_a', 'dA_b', 'dB_a', 'dB_b'))
        t, s, ta, tb, sa, sb = [atom(v, True) for v in ('tjk', 'tij', 'Va_tjk', 'Vb_tjk', 'Va_tij', 'Vb_tij')]
        product_rule = scale(add(
            mul(add(mul(ea, t), mul(B, ta)), db),
            neg(mul(add(mul(eb, t), mul(B, tb)), da)),
            mul(ea, add(mul(db, s), mul(A, sb))),
            neg(mul(eb, add(mul(da, s), mul(A, sa))))), Q(1, 2))
        normalized = mul(Ai, Bi, product_rule)
        curvature = scale(mul(Ai, Bi, add(mul(ea, db), neg(mul(eb, da)))), Q(1, 2))
        pieces = (mul(ta, Ai, db), neg(mul(tb, Ai, da)),
                  mul(sb, Ai, Bi, ea, A), neg(mul(sa, Ai, Bi, eb, A)))
        expected = add(mul(add(t, s), curvature), scale(add(*pieces), Q(1, 2)))
        self.assertEqual(normalized, expected)
        for index in range(4):
            wrong = list(pieces)
            wrong[index] = neg(wrong[index])
            self.assertNotEqual(add(mul(add(t, s), curvature), scale(add(*wrong), Q(1, 2))), expected)
        self.assertNotEqual(add(mul(add(t, s), curvature), scale(add(*pieces[:2]), Q(1, 2))), expected)

    def test_08_mixed_moyal_factor_one_quarter_and_character_selection(self):
        pi = [(0, 1, 1), (1, 0, -1), (2, 3, 1), (3, 2, -1)]
        result = {}
        for a, b, sign in pi:
            for c, d, other in pi:
                if len({a, b, c, d}) != 4:
                    continue
                key = (tuple(sorted((a, c))), tuple(sorted((b, d))))
                result[key] = result.get(key, Q(0)) + Q(sign * other, 8)
        self.assertEqual(result, {((0, 2), (1, 3)): Q(1, 4), ((0, 3), (1, 2)): -Q(1, 4),
                                  ((1, 2), (0, 3)): -Q(1, 4), ((1, 3), (0, 2)): Q(1, 4)})
        p, q = 0b0011, 0b1100
        self.assertEqual(p ^ q, 0b1111)
        self.assertEqual(p ^ p, 0)
        self.assertEqual(q ^ q, 0)
        bp, bq = atom('bp', True), atom('bq', True)
        square = scale(mul(add(bp, bq), add(bp, bq)), -Q(1, 2))
        mixed = {key: value for key, value in square.items() if key[0] == ('bp', 'bq')}
        self.assertEqual(mixed, neg(mul(bp, bq)))

    def test_09_aw_cup_sign_and_exponential_coherence_in_every_artificial_order(self):
        # Four fabricated vertex values; no elliptic coordinate is used.
        p = [Q(2), Q(1, 3), Q(-3, 2), Q(5)]
        q = [Q(0), Q(2, 5), Q(-7), Q(3)]
        ap = [Q(-1), Q(4), Q(3, 2), Q(2, 7)]
        aq = [Q(1, 6), Q(-2), Q(3), Q(8)]
        lam = Q(15, 4)
        def b(i, j, k):
            return lam * (p[j] - p[i]) * (q[k] - q[j])
        def tvq(i, j):
            return lam * ap[i] * (q[j] - q[i])
        def tvp(i, j):
            return lam * (p[j] - p[i]) * aq[j]
        for i, j, k, l in itertools.permutations(range(4)):
            self.assertEqual(b(j, k, l) - b(i, k, l) + b(i, j, l) - b(i, j, k), 0)
            self.assertEqual(tvq(j, k) - tvq(i, k) + tvq(i, j),
                             lam * (ap[j] - ap[i]) * (q[k] - q[j]))
            self.assertEqual(tvp(j, k) - tvp(i, k) + tvp(i, j),
                             -lam * (p[j] - p[i]) * (aq[k] - aq[j]))
            x, y, z, w = b(i, j, k), b(i, k, l), b(j, k, l), b(i, j, l)
            self.assertEqual(x + y, z + w)
            self.assertEqual(x*x/2 + x*y + y*y/2, z*z/2 + z*w + w*w/2)

    def test_10_twenty_existing_source_records_full_baseline_and_jets(self):
        template = json.loads(INPUTS.direct('research/codex-swarm/scalar-compiler/compiled-template.json'))
        nodes = template['nodes']
        self.assertEqual(len(nodes), 4270)
        records = template['source_residual_components']
        self.assertEqual([r['owners'] for r in records], [list(t) for t in itertools.combinations(range(6), 3)])
        names = ['baseline', 'Fk12', 'Fk34', 'E12', 'E34']
        self.assertEqual(template['Rsharp_components'], names)
        for r in records:
            baseline = r['baseline']
            self.assertEqual(len(baseline['kinetic_terms']), 7)
            self.assertEqual(len(baseline['gerbe_terms']), 3)
            m0 = nodes[baseline['M0']]
            self.assertEqual(m0['op'], 'matrix_product')
            self.assertEqual(nodes[m0['children'][0]]['op'], 'matrix_inverse')
            inverse_leaf = nodes[nodes[m0['children'][0]]['children'][0]]
            self.assertEqual(inverse_leaf['owners'], [r['owners'][0], r['owners'][2]])
            self.assertEqual(nodes[m0['children'][1]]['children'], baseline['kinetic_terms'] + baseline['gerbe_terms'])
            for gerbe in baseline['gerbe_terms']:
                self.assertEqual(nodes[gerbe]['op'], 'rational_scale')
                self.assertEqual(nodes[gerbe]['coefficient'], [-1, 1])
            root_kids = [r['components'][name] for name in names]
            self.assertEqual(sum(n['op'] == 'add' and n['children'] == root_kids for n in nodes), 1)
        jets = [n for n in nodes if n['op'] == 'physical_jet']
        self.assertTrue(jets)
        self.assertTrue(all(n['frames_differentiated'] is True and len(n['directions']) <= 2
                            and len(set(n['directions'])) == len(n['directions']) for n in jets))
        solvers = [n for n in nodes if n['op'] == 'complete_inner_solver']
        self.assertTrue(solvers)
        for solver in solvers:
            branches = [nodes[k] for k in solver['children']]
            self.assertEqual([b['op'] for b in branches], ['N14_Hrho', 'N14_R_Kcov_Pi', 'N14_R_A_h_S_Pi'])
            self.assertEqual([nodes[k]['sign'] for k in branches[0]['children']], [1, -1])

    def test_11_producer_formal_functions_agree_with_independent_expansion(self):
        raw = INPUTS.rs('formal_identities.py')
        self.assertEqual(hashlib.sha256(raw).hexdigest(),
                         'd248be8d82670c80bb76926b4af7e0ada06f8de8fe2b8bff7863627af5fe8278')
        module = types.ModuleType('rs01_formal_only')
        exec(compile(raw, REVIEW_COMMIT + ':' + RS_PATH + 'formal_identities.py', 'exec'), module.__dict__)
        actual, remainder = module.defect_syzygy()
        expected = {('A', 'V', 'W'): Q(1), ('X', 'A', 'W'): -Q(1),
                    ('C', 'D', 'H'): Q(1), ('A', 'B', 'H'): -Q(1)}
        self.assertEqual(actual, expected)
        self.assertEqual(remainder, expected)
        self.assertEqual(module.reduction_identity(), {})
        self.assertTrue(module.reduction_identity(-1))

    def test_12_static_constructor_and_physical_refusal_contract(self):
        tree = ast.parse(INPUTS.rs('r_binding.py'))
        cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'ActualFullSourceApplication')
        methods = {n.name: n for n in cls.body if isinstance(n, ast.FunctionDef)}
        init = methods['__init__']
        self.assertEqual([a.arg for a in init.args.args], ['self', 'repo'])
        self.assertIsNone(init.args.vararg)
        self.assertIsNone(init.args.kwarg)
        self.assertEqual(len(methods['coefficient'].body), 1)
        self.assertIsInstance(methods['coefficient'].body[0], ast.Raise)
        for name in ('factor_terms', 'owners'):
            self.assertEqual(len(methods[name].body), 1)
            result = methods[name].body[0]
            self.assertIsInstance(result, ast.Return)
            self.assertEqual(ast.unparse(result.value), 'self.coefficient()')
        contract = json.loads(INPUTS.rs('contract.json'))
        self.assertEqual(contract['boundary_sign'], 1)
        for flag in ('J0_J3_extension_discharged', 'actual_fibers_enumerated', 'historical_comparison_established',
                     'obstruction_decided', 'outer_full54_29_5251_domain_discharged',
                     'physical_coefficients_evaluated', 'physical_execution_admitted'):
            self.assertIs(contract[flag], False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    transport = parser.add_mutually_exclusive_group()
    transport.add_argument('--repo', help='repository checkout containing the pinned Git objects')
    transport.add_argument('--snapshot', help='optional authenticated review snapshot; not needed for public replay')
    options, unittest_args = parser.parse_known_args()
    INPUTS = PinnedInputs(repo=options.repo, snapshot=options.snapshot)
    print('Input transport: ' + ('authenticated snapshot' if options.snapshot else 'immutable git show'), file=sys.stderr)
    unittest.main(argv=[sys.argv[0]] + unittest_args, verbosity=2)
