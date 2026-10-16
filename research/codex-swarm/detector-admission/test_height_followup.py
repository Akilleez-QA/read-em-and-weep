"""Bounded AC-R repair controls: fictional sparse RF values only.
Direct entry supervises normal/-O children; --child self-installs AS/CPU limits.
The supervisor adds a 60-second wall deadline. No historical suites or Git calls.
"""
from fractions import Fraction as Q
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import unittest

import test_independent as I

RF, RB = I.RF, I.RB
ZERO = (0, 0, 0, 0)
ORIGINAL_REVIEW_SHA = '8ba5e4028c0ec9a12f6bf0b76491dce5c422dbe5242b382be3de286fa3da356b'


def frozen_snapshot():
    """All AC files, RF/SR inventories, and locally present pinned dependencies."""
    result = {str(I.HERE/name): digest for name, digest in I.snapshot().items()}
    for directory in ('exact-curve-field', 'detector-realization'):
        p = I.BASE/directory/'producer-ready.json'
        result[str(p)] = I.sha(p.read_bytes())
        marker = I.read_json(p)
        for name, digest in marker.get('files', marker.get('files_sha256', {})).items():
            p = I.BASE/directory/name
            I.require(I.sha(p.read_bytes()) == digest, 'dependency inventory drift: '+str(p))
            result[str(p)] = digest
    for directory, keys, base in (
        ('detector-admission', ('workspace_inputs',), I.BASE),
        ('detector-realization', ('local_dependencies',), I.BASE),
        ('source-boundary-analysis', ('workspace_dependencies',), I.ROOT),
        ('scalar-compiler', ('sources',), I.ROOT),
    ):
        p = I.BASE/directory/'source-pins.json'
        result[str(p)] = I.sha(p.read_bytes())
        data = I.read_json(p)
        for key in keys:
            for row in data[key]:
                p = base/row['path']
                # Immutable records may differ in the workspace; the existing
                # independent suite authenticates their pinned bytes separately.
                if p.is_file():
                    digest = I.sha(p.read_bytes())
                    if 'commit' not in row:
                        I.require(digest == row['sha256'], 'local dependency drift: '+str(p))
                    result[str(p)] = digest
    p = I.HERE/'review-independent.md'
    I.require(I.sha(p.read_bytes()) == ORIGINAL_REVIEW_SHA, 'original report changed')
    result[str(p)] = ORIGINAL_REVIEW_SHA
    return result


class Trace(RF.Execution):
    """Record literal observe calls without changing RF arithmetic or its meter."""
    def __init__(self):
        super().__init__()
        self.observations = []

    def observe(self, q):
        self.observations.append(q)
        return super().observe(q)


def metadata(p):
    return dict(terms=len(p.terms), degree=max([0]+[max(e) for e, c in p.terms]),
                bits=max([1]+[I.bit(c) for e, c in p.terms]))


def rational_metadata(r):
    return dict(numerator=metadata(r.numerator), denominator=metadata(r.denominator))


def monomial(ex, degree, coefficient=1, axis=0):
    e = [0]*4
    e[axis] = degree
    return ex.poly(((tuple(e), coefficient),))


class HeightFollowup(unittest.TestCase):
    def check_poly(self, value, bound):
        actual = metadata(value)
        for key in ('terms', 'degree', 'bits'):
            self.assertLessEqual(actual[key], bound[key], key)

    def check_observations(self, ex, start, prior, prediction):
        limit = prediction['observed_bit_height_upper']
        for q in ex.observations[start:]:
            self.assertLessEqual(I.bit(q), limit, repr(q))
        self.assertLessEqual(ex.counts['bit_height'], max(prior, limit))

    def test_01_poly_empty_cancellation_and_large_degree(self):
        # At most two terms per operand. Degree size never controls a loop.
        for degree in (0, 1, 2, 1023, 1024, 2**31, 2**127):
            for variant in ('both-empty', 'zero-right', 'cancel', 'collision'):
                for kind in ('add', 'mul', 'neg', 'partial'):
                    with self.subTest(degree=degree, variant=variant, kind=kind):
                        ex = Trace()
                        a = ex.poly() if variant == 'both-empty' else monomial(ex, degree, Q(5, 7))
                        b = (ex.poly() if variant in ('both-empty', 'zero-right')
                             else monomial(ex, degree, Q(-5, 7) if variant == 'cancel' else Q(7, 11)))
                        ma, mb = metadata(a), metadata(b)
                        prediction = RB.rf_poly_bound(kind, ma, mb if kind in ('add', 'mul') else None)
                        start, prior = len(ex.observations), ex.counts['bit_height']
                        value = (a+b if kind == 'add' else a*b if kind == 'mul'
                                 else -a if kind == 'neg' else a.partial(0))
                        self.check_poly(value, prediction['bound'])
                        self.check_observations(ex, start, prior, prediction)

    def test_02_exponent_carry_and_partial_integer_observation(self):
        ex = Trace()
        d = 2**127-1
        a = monomial(ex, d, axis=3)
        prediction = RB.rf_poly_bound('mul', metadata(a), metadata(a))
        start, prior = len(ex.observations), ex.counts['bit_height']
        result = a*a
        self.assertEqual(result.terms[0][0][3], 2*d)
        self.assertIn(Q(2*d), ex.observations[start:])
        self.assertEqual(prediction['bound']['bits'], 3)
        self.assertEqual(prediction['observed_bit_height_upper'], 128)
        self.check_observations(ex, start, prior, prediction)
        # Differentiation on an absent axis returns zero; on axis3 it observes
        # the OLD exponent as an integer multiplier before constructing d-1.
        for axis in (0, 3):
            prediction = RB.rf_poly_bound('partial', metadata(a))
            start, prior = len(ex.observations), ex.counts['bit_height']
            value = a.partial(axis)
            self.check_poly(value, prediction['bound'])
            self.check_observations(ex, start, prior, prediction)
            if axis == 3:
                self.assertIn(Q(d), ex.observations[start:])
                self.assertEqual(value.terms[0][1], d)
            else:
                self.assertFalse(value.terms)

    def test_03_rational_zero_equal_and_unequal_denominators(self):
        for degree in (0, 1024, 2**63):
            for variant in ('zero-left', 'zero-right', 'equal', 'unequal', 'cancel'):
                for kind in ('add', 'mul', 'partial'):
                    with self.subTest(degree=degree, variant=variant, kind=kind):
                        ex = Trace()
                        n = monomial(ex, degree, Q(5, 7))
                        d = monomial(ex, degree, Q(3, 11), axis=1)+ex.constant(Q(2, 13))
                        a = ex.rational(ex.poly() if variant == 'zero-left' else n, d)
                        if variant == 'zero-right':
                            b = ex.rational(ex.poly(), d)
                        elif variant == 'cancel':
                            b = ex.rational(-a.numerator, a.denominator)
                        elif variant == 'unequal':
                            b = ex.rational(n, monomial(ex, degree, Q(7, 17), axis=2)+ex.constant(1))
                        else:
                            b = ex.rational(n, a.denominator)
                        prediction = RB.rf_rational_bound(kind, rational_metadata(a),
                                                          rational_metadata(b) if kind != 'partial' else None)
                        start, prior = len(ex.observations), ex.counts['bit_height']
                        value = a+b if kind == 'add' else a*b if kind == 'mul' else a.partial(0)
                        for side in ('numerator', 'denominator'):
                            self.check_poly(getattr(value, side), prediction['bound'][side])
                        self.check_observations(ex, start, prior, prediction)
                        if variant == 'cancel' and kind == 'add':
                            self.assertFalse(value.numerator.terms)

    def test_04_rational_composition_propagates_bounds(self):
        ex = Trace()
        a = ex.rational(monomial(ex, 2**80), monomial(ex, 2**79, axis=1)+ex.constant(1))
        bound = rational_metadata(a)
        for kind in ('mul', 'add', 'partial'):
            prediction = RB.rf_rational_bound(kind, bound, bound if kind != 'partial' else None)
            start, prior = len(ex.observations), ex.counts['bit_height']
            a = a*a if kind == 'mul' else a+a if kind == 'add' else a.partial(0)
            for side in ('numerator', 'denominator'):
                self.check_poly(getattr(a, side), prediction['bound'][side])
            self.check_observations(ex, start, prior, prediction)
            bound = prediction['bound']

    def test_05_unrelated_historical_peak_requires_inherited_maximum(self):
        ex = Trace()
        ex.observe(Q(2**2048))
        a = ex.constant(1)
        prediction = RB.rf_poly_bound('neg', metadata(a))
        start, prior = len(ex.observations), ex.counts['bit_height']
        value = -a
        self.check_poly(value, prediction['bound'])
        self.check_observations(ex, start, prior, prediction)
        self.assertGreater(prior, prediction['observed_bit_height_upper'])
        self.assertEqual(ex.counts['bit_height'], prior)

    def test_06_frozen_metadata_regenerates_and_route_is_separate(self):
        frozen_snapshot()
        self.assertEqual(RB.actual_PI_dot_envelope(), I.read_json(I.HERE/'actual-PI-dot-envelope.json'))
        self.assertEqual(RB.rf_operation_recurrences(), I.read_json(I.HERE/'rf-recurrences.json'))
        self.assertEqual(I.WE.build(), I.read_json(I.HERE/'whole-route-envelope.json'))
        route = I.AC.actual_route_certificate()
        self.assertEqual(route, I.read_json(I.HERE/'blocked-route.json'))
        self.assertEqual(route['status'], 'BLOCKED_ROUTE')
        self.assertFalse(route['physical_release'])
        # Neither a numerical giant B nor actual source values are constructed.


def main():
    before = frozen_snapshot()
    if '--child' in sys.argv:
        I.limits()
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(HeightFollowup)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        I.require(frozen_snapshot() == before, 'frozen files changed during followup child')
        raise SystemExit(0 if result.wasSuccessful() else 1)
    for label, optimized in (('height-normal', False), ('height-O', True)):
        command = [sys.executable, '-B']+(['-O'] if optimized else [])+[str(Path(__file__).resolve()), '--child']
        start = time.monotonic()
        done = subprocess.run(command, timeout=60, preexec_fn=I.limits,
                              env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
        I.require(frozen_snapshot() == before, 'frozen files changed during '+label)
        print(json.dumps(dict(suite=label, cases=6, returncode=done.returncode,
                              wall_seconds=round(time.monotonic()-start, 3),
                              address_space_bytes=I.LIMIT, cpu_seconds=59,
                              wall_limit_seconds=60, marker=I.MARKER)), flush=True)
        I.require(done.returncode == 0, 'failed '+label)


if __name__ == '__main__':
    main()
