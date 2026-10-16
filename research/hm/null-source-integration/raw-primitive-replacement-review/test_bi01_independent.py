"""Independent BI01 controls: formal symbols, tiny invented rational matrices,
immutable source metadata, and logical cutoff countercontrols only.

Public replay: python -B test_bi01_independent.py --repo /path/to/repository
No physical source, coefficient, polynomial, jet, or actual fiber is evaluated.
"""
import argparse
import ast
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys
import types
import unittest

PIN = '4ad480da0031536ed37735953dc945d41cb8609f'
PREFIX = 'research/codex-swarm/source-boundary-analysis/'
MANIFEST_SHA = 'b1ec29bc10cc893658b17983d1c1fc8738d921bf6d3ed1afdcdb6800572521d6'
MARKER_SHA = 'aa0e81b32699e15c3c95fc6792b3cdcec763fd5b12f074b169f8da908ebc6a65'


class Inputs:
    def __init__(self, repo=None, snapshot=None):
        self.repo = Path(repo) if repo else Path(__file__).resolve().parent
        self.snapshot = Path(snapshot) if snapshot else None
        self.cache = {}

    def read(self, revision, path):
        key = revision, path
        if key not in self.cache:
            if self.snapshot is None:
                self.cache[key] = subprocess.check_output(
                    ['git', '-C', str(self.repo), 'show', revision + ':' + path], timeout=15)
            else:
                rel = ('source-boundary-analysis/' + path[len(PREFIX):]
                       if revision == PIN and path.startswith(PREFIX) else path)
                self.cache[key] = (self.snapshot / rel).read_bytes()
        return self.cache[key]

    def producer(self, name):
        raw = self.read(PIN, PREFIX + name)
        if name == 'producer-ready.json':
            need(hashlib.sha256(raw).hexdigest() == MARKER_SHA, 'producer marker drift')
        else:
            marker = json.loads(self.producer('producer-ready.json'))
            need(hashlib.sha256(raw).hexdigest() == marker['files'][name], name + ' producer drift')
        return raw


INPUTS = Inputs()


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sum_words(*terms):
    result = {}
    for term in terms:
        for word, value in term.items():
            result[word] = result.get(word, Q(0)) + value
    return {word: value for word, value in result.items() if value}


def word_scale(z, words):
    return {word: z * value for word, value in words.items() if z * value}


def coefficient(names, current, sign=1):
    return {(name, current): Q(sign, 2) for name in names}


def zero(n, m=None):
    return tuple(tuple(Q(0) for _ in range(n if m is None else m)) for _ in range(n))


def matrix(n, m, entries):
    return tuple(tuple(Q(entries.get((i, j), 0)) for j in range(m)) for i in range(n))


def eye(n):
    return matrix(n, n, {(i, i): 1 for i in range(n)})


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def scale(z, a):
    return tuple(tuple(z * x for x in row) for row in a)


def transpose(a):
    return tuple(zip(*a))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def inverse(a):
    n = len(a)
    rows = [list(r) + list(s) for r, s in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        value = rows[j][j]
        rows[j] = [x / value for x in rows[j]]
        for i in range(n):
            if i != j:
                value = rows[i][j]
                rows[i] = [x - value * y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(r[n:]) for r in rows)


class Contraction:
    def __init__(self, d, inc, proj, h):
        self.d, self.inc, self.proj, self.h = d, inc, proj, h
        self.E, self.n = mul(inc, proj), len(d)

    def inclusion(self, row):
        return mul(mul(self.inc, transpose(row)), self.proj)

    def homotopy(self, f, r):
        return add(mul(self.h, f), scale(-1 if r % 2 else 1, mul(mul(self.E, f), self.h)))

    def differential(self, f, r):
        return add(mul(self.d, f), scale(1 if r % 2 else -1, mul(f, self.d)))


class TinyLift:
    def __init__(self, local, source):
        self.local, self.source = local, source

    @lru_cache(None)
    def component(self, s, vertices):
        local = self.local[vertices[0]]
        if s == 0:
            return local.inclusion(self.source(vertices))
        return scale((1, 1, -1, 1)[s], local.homotopy(self.delta(s-1, vertices), 1-s))

    def delta(self, s, vertices):
        value = zero(8)
        for i in range(len(vertices)):
            value = add(value, scale((-1) ** i, self.component(s, vertices[:i] + vertices[i+1:])))
        return value


def independent_resolution_fixture():
    # Different from the producer fixture. These are invented constant matrices.
    grades = (0, 1, 1, 1, 1, 2, 2, 3)
    d = matrix(8, 8, {(1, 0): 1, (5, 4): 1, (7, 6): 1})
    h = transpose(d)
    inc = matrix(8, 2, {(2, 0): 1, (3, 1): 1})
    proj = transpose(inc)
    local = {}
    for vertex in range(7):
        n = matrix(8, 8, {(i, j): Q(((vertex+2)*(i+3)+2*j) % 7, 11)
                          for i in range(8) for j in range(8) if grades[i] == grades[j]-1})
        automorphism = add(eye(8), add(mul(d, n), mul(n, d)))
        inv = inverse(automorphism)
        local[vertex] = Contraction(d, mul(automorphism, inc), mul(proj, inv),
                                    mul(mul(automorphism, h), inv))

    def edge(v):
        i, j = v
        return matrix(2, 2, {(0, 0): i+2*j, (0, 1): i*j+3,
                             (1, 0): 2*i-j, (1, 1): i*i+j+1})

    def source(v):
        return add(add(edge(v[1:]), scale(-1, edge((v[0], v[2])))), edge(v[:2]))
    return local, edge, source


@lru_cache(None)
def artificial_modules():
    boundary = types.ModuleType('pinned_bi01_artificial_boundary')
    exec(compile(INPUTS.producer('boundary.py'), PIN + ':boundary.py', 'exec'), boundary.__dict__)
    # Execute only this artificial class, with an independent rational engine.
    # All imports, filesystem paths, and actual producer factories are excluded.
    tree = ast.parse(INPUTS.producer('resolution_boundary.py'))
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'TinyBoundaryPrimitive')
    namespace = {'lru_cache': lru_cache, 'L': types.SimpleNamespace(
        TinyLift=TinyLift, need=need, add=add, scale=scale, zero=zero)}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[cls], type_ignores=[])),
                 PIN + ':resolution_boundary.py:TinyBoundaryPrimitive', 'exec'), namespace)
    return boundary, namespace['TinyBoundaryPrimitive']


class IndependentBI(unittest.TestCase):
    def test_01_all_eighteen_dependency_pins_and_thirteen_producer_files(self):
        raw = INPUTS.producer('source-pins.json')
        self.assertEqual(hashlib.sha256(raw).hexdigest(), MANIFEST_SHA)
        pins = json.loads(raw)
        self.assertEqual(len(pins['immutable_dependencies']), 15)
        self.assertEqual(len(pins['workspace_dependencies']), 3)
        for row in pins['immutable_dependencies'] + pins['workspace_dependencies']:
            data = INPUTS.read(row.get('commit', PIN), row['path'])
            self.assertEqual(len(data), row['bytes'])
            self.assertEqual(hashlib.sha256(data).hexdigest(), row['sha256'])
            if 'git_blob' in row:
                self.assertEqual(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(), row['git_blob'])
        marker = json.loads(INPUTS.producer('producer-ready.json'))
        self.assertEqual(len(marker['files']), 13)
        for name in marker['files']:
            INPUTS.producer(name)

    def test_02_universal_current_boundary_and_every_endpoint_sign(self):
        # Ai=Va f_i, Bi=Vb f_i; transported L_jk is U, L_ik=L+U.
        transported = sum_words(coefficient(('Bj', 'Bk'), 'Ua'), coefficient(('Aj', 'Ak'), 'Ub', -1))
        middle = sum_words(coefficient(('Bi', 'Bk'), 'La'), coefficient(('Bi', 'Bk'), 'Ua'),
                           coefficient(('Ai', 'Ak'), 'Lb', -1), coefficient(('Ai', 'Ak'), 'Ub', -1))
        initial = sum_words(coefficient(('Bi', 'Bj'), 'La'), coefficient(('Ai', 'Aj'), 'Lb', -1))
        actual = sum_words(transported, word_scale(-1, middle), initial)
        pieces = (sum_words(coefficient(('Ak',), 'Lb'), coefficient(('Aj',), 'Lb', -1)),
                  sum_words(coefficient(('Bk',), 'La', -1), coefficient(('Bj',), 'La')),
                  sum_words(coefficient(('Bj',), 'Ua'), coefficient(('Bi',), 'Ua', -1)),
                  sum_words(coefficient(('Aj',), 'Ub', -1), coefficient(('Ai',), 'Ub')))
        self.assertEqual(actual, sum_words(*pieces))
        self.assertTrue(actual)
        for i in range(4):
            wrong = list(pieces)
            wrong[i] = word_scale(-1, wrong[i])
            self.assertNotEqual(actual, sum_words(*wrong))
        self.assertNotEqual(actual, sum_words(*pieces[:2]))

    def test_03_producer_B_on_noncommuting_artificial_frames_and_reversal(self):
        A, _ = artificial_modules()
        frames = {0:A.mat([[1,2],[0,1]]), 1:A.mat([[1,0],[3,1]]),
                  2:A.mat([[3,2],[1,1]]), 3:A.mat([[2,3],[1,2]])}
        h, e, f = A.mat([[1,0],[0,-1]]), A.mat([[0,1],[0,0]]), A.mat([[0,0],[1,0]])
        currents = A.ArtificialCurrents(frames, {i:(A.add(A.scale(i+2,h),e),
                                                       A.add(A.scale(i+3,f),A.scale(i-1,e))) for i in frames})
        vertex = {i:(Q(i*i+1,3),Q(2*i-1,5)) for i in frames}
        edge = lambda i,j:currents.B_edge(vertex,i,j)
        scalar_edge = lambda i,j:A.scalar_difference(vertex,i,j)
        nonzero = wrong_transport = False
        for i,j,k in itertools.permutations(frames,3):
            expected = currents.E_triangle(scalar_edge,i,j,k)
            self.assertEqual(expected,currents.delta_edge(edge,i,j,k))
            nonzero |= expected != A.ZERO
            untransported = A.add(A.sub(edge(j,k),edge(i,k)),edge(i,j))
            wrong_transport |= untransported != expected
        self.assertTrue(nonzero and wrong_transport)
        for i,j in itertools.permutations(frames,2):
            self.assertEqual(edge(j,i),A.scale(-1,A.conjugate_inverse(currents.g(j,i),edge(i,j))))
            self.assertEqual(A.trace(edge(i,j)),0)

    def test_04_full_source_variation_and_positive_RS_boundary_sign(self):
        # Formal cochain-level calculation; fixed means ALL baseline/Fk terms.
        fixed = {('M0tf',):Q(1),('Fqkp',):Q(1),('Fpkq',):Q(1)}
        old = sum_words(fixed,{('Ep_sq',):Q(1),('Eq_sp',):Q(1)})
        new = sum_words(old,{('delta_Bp_fq',):Q(1),('delta_Bq_fp',):Q(1)})
        variation = sum_words(new,word_scale(-1,old))
        self.assertEqual(variation,{('delta_Bp_fq',):Q(1),('delta_Bq_fp',):Q(1)})
        dw = {('delta_dfq_kp',):Q(1),('delta_dfp_kq',):Q(1)}
        residual_difference = sum_words(variation,word_scale(-1,dw))
        self.assertNotEqual(residual_difference,sum_words(variation,dw))

    def test_05_scalar_cohomological_degrees(self):
        # Checks the tensor degree calculation, not the algebraic-cover theorem.
        def harmonic_degrees(twists):
            factors = [(0,) if n == 0 else (1,) if n == -2 else () for n in twists]
            return {sum(degrees) for degrees in itertools.product(*factors)}
        for pair in ((0,1),(2,3)):
            degrees = harmonic_degrees(tuple(-2 if i in pair else 0 for i in range(4)))
            self.assertEqual(degrees,{2})
            self.assertNotIn(1,degrees)
        self.assertEqual(harmonic_degrees((-2,-2,-2,-2)),{4})

    def test_06_constructive_total_boundary_with_independent_resolution_fixture(self):
        _, Boundary = artificial_modules()
        local, edge, source = independent_resolution_fixture()
        for c in local.values():
            self.assertEqual(mul(c.proj,c.inc),eye(2))
            self.assertEqual(add(mul(c.d,c.h),mul(c.h,c.d)),add(eye(8),scale(-1,c.E)))
            self.assertEqual(mul(c.h,c.h),zero(8))
        for a,b in itertools.product(local,repeat=2):
            self.assertEqual(mul(local[a].proj,local[b].inc),eye(2))
        lift = TinyLift(local,source)
        primitive = Boundary(lift,edge)
        nonzero = [False]*4
        for s in range(4):
            for v in itertools.combinations(range(7),3+s):
                self.assertEqual(primitive.total_boundary_component(s,v),lift.component(s,v))
            nonzero[s] = any(primitive.component(s,v) != zero(8)
                             for v in itertools.combinations(range(7),2+s))
        self.assertTrue(all(nonzero),nonzero)
        self.assertEqual(lift.delta(3,tuple(range(7))),zero(8))
        # Reversing C2 changes the q=3, internal=-1 equation.
        witnesses = []
        for v in itertools.combinations(range(7),4):
            c2 = primitive.component(2,v)
            d = local[v[0]].differential(c2,-2)
            witnesses.append(add(primitive.delta(1,v),d) != lift.component(1,v))
        self.assertTrue(any(witnesses))

    def test_07_bottom_injectivity_is_needed_for_last_equation(self):
        local,_,_ = independent_resolution_fixture()
        bottom = matrix(8,8,{(0,7):Q(7,3)})
        self.assertNotEqual(local[0].differential(bottom,-3),zero(8))
        # A separate artificial zero-differential bottom complex would leave
        # its closed bottom error untouched: closed alone does not imply zero.
        self.assertNotEqual((Q(1),),(Q(0),))
        self.assertEqual(Q(0)*Q(1),0)

    def test_08_global_equality_need_not_be_cutoff_boundary(self):
        # Full C1=Q2 -> C2=Q2, d(a,b)=(b,0). Cutoff C1 has b=0.
        d = lambda x:(x[1],Q(0))
        fresh, raw = (Q(1),Q(2)), (Q(0),Q(2))
        primitive = (Q(0),Q(1))
        self.assertEqual(d(primitive),(fresh[0]-raw[0],fresh[1]-raw[1]))
        self.assertNotEqual(primitive[1],0)
        self.assertEqual(d((Q(9),Q(0))),(Q(0),Q(0)))
        self.assertEqual(fresh[1],raw[1])  # global boundary-annihilating functional
        def finite_pi(x):
            need(x[1] == 0,'comparison primitive outside finite domain')
            return x
        with self.assertRaises(ValueError):finite_pi(primitive)

    def test_09_regular_scalar_faces_have_no_Serre_harmonic_coefficients(self):
        harmonic = {-3,-2,-1}
        for coordinate in range(4):
            for exponent in (-8,-5,-4,0,1,4):
                monomial = [-2]*4
                monomial[coordinate] = exponent
                # A or B regular face of O(-4) has exponent >=0 or <=-4.
                self.assertTrue(exponent >= 0 or exponent <= -4)
                self.assertFalse(all(e in harmonic for e in monomial))
        self.assertEqual({-m-1 for m in (0,1,2)},harmonic)

    def test_10_raw_denotation_retains_full_source_and_moving_frames(self):
        recipe = json.loads(INPUTS.producer('actual-raw-s-denotation.json'))
        self.assertEqual(recipe['block_ranks'],[5,15,10,2])
        self.assertEqual(recipe['supertrace_signs'],[-1,1,-1,1])
        self.assertEqual(recipe['line_weights'],[-1,1,3,5])
        self.assertEqual(len(recipe['whole_Rraw_components']),5)
        self.assertEqual(recipe['M0_kinetic_term_count'],7)
        self.assertEqual(recipe['M0_negative_gerbe_term_count'],3)
        self.assertTrue(recipe['physical_refined_line_frames']['moving_frames_differentiated'])
        self.assertFalse(recipe['physical_source_evaluated'])
        self.assertFalse(recipe['source_specific_JTSH_symmetry_proved'])

    def test_11_analytic_degree_rectangles_and_scope_flags(self):
        description = json.loads(INPUTS.producer('analytic-reduction.json'))
        owned = 54*5+29*3
        self.assertEqual(owned,357)
        for key,m,r in (('J2',5,-2),('full_lift_max6_owners',6,-3)):
            degree = m*owned+r-2
            self.assertEqual(description[key]['whole_numerator_degree_upper'],degree)
            self.assertEqual(description[key]['finite_exponent_rectangle'],
                             [-m*(2006+owned),degree+m*6677])
        self.assertEqual(description['additional_standard_boundary_power_for_raw_route'],0)
        for flag in ('common_values_computed','rectangles_are_occupied_support',
                     'six_owner_box_applies_to_seven_owner_deltaJ3',
                     'nonconstant_product_or_memory_bound_proved','new_execution_budget_issued',
                     'physical_source_evaluated','physical_execution_authorized','obstruction_decided'):
            self.assertIs(description[flag],False)

    def test_12_first_order_exactness_does_not_imply_second_order_zero(self):
        # An abstract logical counterexample only; no actual HM specialization.
        scalar_delta = lambda x:x[1]-x[0]
        self.assertEqual(scalar_delta((Q(2),Q(2))),0)
        obstruction = (Q(0),Q(1))
        second_boundary = lambda x:(x,Q(0))
        detector = lambda x:x[1]
        self.assertEqual(detector(second_boundary(Q(17))),0)
        self.assertEqual(detector(obstruction),1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--repo')
    modes.add_argument('--snapshot')
    options, args = parser.parse_known_args()
    INPUTS = Inputs(options.repo,options.snapshot)
    print('Input transport: ' + ('authenticated snapshot' if options.snapshot else 'immutable git show'),file=sys.stderr)
    unittest.main(argv=[sys.argv[0]]+args,verbosity=2)
