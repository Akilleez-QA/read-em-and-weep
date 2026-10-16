"""QH-R independent tiny rational controls; never evaluate physical catalogs."""
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import unittest
from fractions import Fraction as F
from quotient import (FiniteRing, Budget, ZERO, ArtificialCatalog, ActualCatalog,
                      QuotientProgram, FullOwner)
from interfaces import PhysicalAdmissionMissing

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def add(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i+j] = out.get(i+j, F(0)) + x*y
    return {e: c for e, c in out.items() if c}


def power(a, n):
    out = {0: F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def brute_B(cs, vs, T, L, j):
    """Independent rectangular enumeration; factorial multinomial; tiny only."""
    out = {}
    for ns in itertools.product(range(L+1), repeat=len(cs)):
        if sum(ns) != L or ns[j] < T or any(n >= T for n in ns[:j]):
            continue
        weight = math.factorial(L)
        for n in ns:
            weight //= math.factorial(n)
        term = {0: F(weight)}
        for i, n in enumerate(ns):
            term = mul(term, power(cs[i], n))
            term = mul(term, power(vs[i], n-T*(i == j)))
        out = add(out, term)
    return out


def sparse(poly):
    return {(k, 0, 0, 0): c for k, c in poly.items()}


def const(n):
    return {ZERO: F(n)}


def cat():
    return ArtificialCatalog([const(n) for n in [1, 2, 3, 4, 5]],
                             [const(n) for n in [2, 3, 5, 7, 11]],
                             const(F(2, 3)), [const(n) for n in [1, 2, 3, 4, 5]])


def own(carrier=0, mask=0, tag=0, seed=12, occurrence=('review', 'u')):
    return FullOwner(seed, occurrence, carrier, mask, tag)


class IndependentControls(unittest.TestCase):
    def test_first_hit_rational_polynomial_all_coefficients(self):
        cs = [{0: F(-1, 2), 1: F(1)}, {0: F(2, 3)}, {0: F(1), 1: F(-1)}]
        vs = [{0: F(1), 1: F(1)}, {0: F(2)}, {0: F(-1), 1: F(1)}]
        ring = FiniteRing('synthetic', Budget())
        C = [ring.polynomial(sparse(v)) for v in cs]
        V = [ring.polynomial(sparse(v)) for v in vs]
        for j in range(3):
            expected = brute_B(cs, vs, 2, 4, j)
            node = ring.first_hit(C, V, j, 2, 4)
            actual = {k: ring.coefficient(node, (k, 0, 0, 0)) for k in range(9)}
            self.assertEqual({k: c for k, c in actual.items() if c}, expected)
            self.assertEqual(ring.coefficient(node, (9, 0, 0, 0)), 0)
        # Every tiny composition has exactly one FIRST qualifying index.
        for ns in itertools.product(range(5), repeat=3):
            if sum(ns) == 4:
                hits = [j for j in range(3) if ns[j] >= 2 and all(n < 2 for n in ns[:j])]
                self.assertEqual(len(hits), 1)

    def test_primary_and_auxiliary_N2_inclusive_endpoints(self):
        # All-finite chart has B0=v0^0=1. Neither endpoint is discarded.
        c = cat()
        primary = QuotientProgram(own(), c, N=2)
        aux = QuotientProgram(own(5), c, N=2)
        v2, a, h0 = F(3), F(2, 3), F(2)
        self.assertEqual(primary.coefficient(ZERO), 3*v2*a+h0)
        self.assertEqual(aux.coefficient(ZERO), v2**3*a+3*h0*v2**2)
        self.assertEqual(dict(primary.factor_terms(primary.owner)), {ZERO: F(8)})
        self.assertEqual(dict(aux.factor_terms(aux.owner)), {ZERO: F(72)})

    def test_full_owner_two_infinity_axes_and_complete_stream(self):
        # tag9 => infinity0,3; mask9 => both mask1. Pair01 vs pair34 swap
        # pair-line/complement role, preserving occurrence and seed.
        c = cat()
        cs = [{0: F(3)}, {0: F(-2)}, {0: F(1)}]
        vs = [{0: F(1)}, {0: F(2)}, {0: F(3)}]
        total = F(3)*sum(brute_B(cs, vs, 5, 13, j).get(0, F(0)) for j in range(3))
        p = QuotientProgram(own(5, 9, 9), c, N=1)
        expected = {(-7, 0, 0, -4): total, (-7, 0, 0, -6): -total}
        self.assertEqual(dict(p.factor_terms(p.owner)), expected)
        q = QuotientProgram(p.owner, c, N=1, pair=(2, 3))
        self.assertEqual(dict(q.factor_terms(q.owner, (2, 3))),
                         {(-4, 0, 0, -7): total, (-6, 0, 0, -7): -total})
        for changed in [own(5, 9, 9, seed=30), own(5, 9, 9, occurrence=('other',)), own(4, 9, 9), own(5, 8, 9), own(5, 9, 8)]:
            with self.assertRaises(ValueError):
                p.factor_terms(changed)
        with self.assertRaises(ValueError):
            p.factor_terms(p.owner, (2, 3))

    def test_all_finite_mask_zero_and_missing_primary(self):
        for pair in [(0, 1), (2, 3)]:
            p = QuotientProgram(own(5, 1, 0), cat(), N=1, pair=pair)
            self.assertEqual(p.factor_terms(p.owner, pair), ())
            p = QuotientProgram(own(4, 0, 8), cat(), N=1, pair=pair)
            self.assertEqual(p.factor_terms(p.owner, pair), ())

    def test_stream_oversize_raises_before_any_coefficient(self):
        p = QuotientProgram(own(), cat(), N=1)
        p.support_box = lambda: ((0, 0, 0, 0), (4096, 0, 0, 0))
        def forbidden(_):
            self.fail('oversize stream started coefficient enumeration')
        p.coefficient = forbidden
        with self.assertRaises(ValueError):
            p.factor_terms(p.owner)

    def test_shared_aggregate_budget_never_yields_partial_value(self):
        b = Budget(max_queries=0)
        p = QuotientProgram(own(), cat(), N=1, budget=b)
        with self.assertRaises(ValueError):
            p.coefficient(ZERO)
        self.assertGreater(b.queries, b.max_queries)
        r = FiniteRing('synthetic', Budget())
        r.max_index_visits = 2
        n = r.first_hit([r.const(1), r.const(1)], [r.const(1), r.const(1)], 0, 2, 3)
        with self.assertRaises(ValueError):
            r.coefficient(n, ZERO)

    def test_immutable_source_bytes_and_actual_metadata_refusals(self):
        pins = json.loads((HERE/'source-pins.json').read_text())
        for pin in pins['sources']:
            raw = subprocess.check_output(['git', 'show', pin['commit']+':'+pin['path']], cwd=REPO)
            self.assertEqual(hashlib.sha256(raw).hexdigest(), pin['sha256'])
            self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(), pin['git_blob'])
        # Construction compiles bounded metadata; no physical coefficient call
        # reaches the ring, even for a finite-mask structural zero.
        for o in [own(5, 15, 15), own(0, 1, 0)]:
            p = QuotientProgram(o, ActualCatalog(), pair=(2, 3))
            for e in [ZERO, (-10**9, 0, 0, 0)]:
                with self.assertRaises(PhysicalAdmissionMissing):
                    p.coefficient(e)
                with self.assertRaises(PhysicalAdmissionMissing):
                    p.R.coefficient(p.root, e)
            with self.assertRaises(PhysicalAdmissionMissing):
                p.factor_terms(p.owner, (2, 3))


if __name__ == '__main__':
    unittest.main()
