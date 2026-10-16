"""Artificial arithmetic/germ and static/refusal checks. No actual evaluation."""
from contextlib import ExitStack
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('omega_preparation', HERE/'prepare_omega.py')
P = importlib.util.module_from_spec(sp)
sp.loader.exec_module(P)
E = P.E


class Artificial(unittest.TestCase):
    def test_01_rational_operations_against_fraction(self):
        m = E.Meter()
        for a, b, c, d in ((2, 3, -5, 7), (0, 11, 4, 9), (-3, 5, -7, 2)):
            x, y = E.Rat(m, a, b), E.Rat(m, c, d)
            u, v = Fraction(a, b), Fraction(c, d)
            for actual, wanted in ((x+y, u+v), (x-y, u-v), (x*y, u*v), (x/y, u/v)):
                self.assertEqual((actual.n, actual.d), (wanted.numerator, wanted.denominator))

    def test_02_poisoned_context_and_zero_denominator(self):
        m = E.Meter(rational_ops=1)
        a = E.Rat(m, 1)
        with self.assertRaises(E.Refusal):
            a+a
        self.assertTrue(m.poisoned)
        with self.assertRaises(E.Refusal):
            E.Rat(m, 0)
        q = E.Meter()
        with self.assertRaises(E.Refusal):
            E.Rat(q, 1, 0)
        self.assertTrue(q.poisoned)

    def test_03_intermediate_height_preflight_and_integer_budget(self):
        m = E.Meter(bits=8)
        x = E.Rat(m, 127)
        with self.assertRaises(E.Refusal):
            x*x
        self.assertLessEqual(m.counts['max_integer_bits'], 8)
        n = E.Meter(integer_ops=1)
        self.assertEqual(n.integer('mul', 2, 3), 6)
        with self.assertRaises(E.Refusal):
            n.integer('neg', 2)

    def test_04_foreign_context_before_arithmetic(self):
        m, n = E.Meter(), E.Meter()
        a, b = E.Rat(m, 1, 2), E.Rat(n, 2, 3)
        before = dict(m.counts)
        with self.assertRaises(E.Refusal):
            a+b
        self.assertEqual(m.counts, before)
        self.assertTrue(m.poisoned)

    def test_05_independent_mixed_quotient_rule(self):
        m = E.Meter()
        x, y = E.Mixed4.coordinate(m, E.Rat(m, 3), 0, (0, 2)), E.Mixed4.coordinate(m, E.Rat(m, 4), 2, (0, 2))
        f = (x*y+x*x)/(x+1)
        self.assertEqual(f.v[3], E.Rat(m, 1, 16))
        a, b = E.Jet11.coordinate(m, E.Rat(m, 3), 0), E.Jet11.coordinate(m, E.Rat(m, 4), 2)
        g = (a*b+a*a)/(a+1)
        self.assertEqual(g.coefficient(0, 2), f.v[3])
        with self.assertRaises(E.Refusal):
            g.coefficient(0, 0)

    def test_06_full_elementary_mixed_hessian(self):
        m = E.Meter()
        point = [E.Rat(m, k) for k in (3, 4, 5, 6)]
        e = P.elementary_by_products([E.Jet11.coordinate(m, x, i) for i, x in enumerate(point)])
        p = e[2]*e[2]
        direct = P.direct_polynomial_mixed([['0,2,0,0', 1]], point, (0, 2))
        for r, mask in enumerate((0, 1, 4, 5)):
            self.assertEqual(p.v[E.INDEX[mask]], direct.v[r])
        self.assertEqual(e[2].coefficient(0, 2), E.Rat(m, 1))
        first_only = 2*e[2].coefficient(0)*e[2].coefficient(2)
        self.assertEqual(p.coefficient(0, 2)-first_only, 2*e[2].v[0])
        self.assertNotEqual(p.coefficient(0, 2), first_only)

    def test_07_moving_frames_are_not_frozen_and_gamma_differs(self):
        m = E.Meter()
        point = [E.Rat(m, k) for k in (3, 4, 5, 6)]
        frame = P.unit_frame(point, 5, (0, 2))
        f = frame[0][0]
        self.assertEqual(f.v[0], E.Rat(m, 1))
        self.assertEqual(f.v[1], E.Rat(m, 5, 24))
        self.assertEqual(f.v[3], E.Rat(m, 13, 576))
        self.assertFalse(f.v[1].is_zero())
        old_gamma = E.Rat(m, 1, 24)
        self.assertEqual(P.qdiag(point, 5, 0)[0][0]-old_gamma, E.Rat(m, 1, 6))
        zero = P.unit_frame(point, 0, (0, 2))[0][0]
        self.assertEqual(zero.v, (E.Rat(m, 1), E.Rat(m, 0), E.Rat(m, 0), E.Rat(m, 0)))

    def test_08_omega_factor_sign_and_cross_gram(self):
        m = E.Meter()
        z = lambda: [[E.Rat(m, 0) for _ in range(2)] for _ in range(2)]
        h, j = [z() for _ in range(4)], [z() for _ in range(4)]
        h[3][1][0], j[0][0][1] = E.Rat(m, 1), E.Rat(m, 1)
        omega, gram, skew = P.omega_and_gram(h, j)
        self.assertEqual([[v.text() for v in r] for r in omega], [['1/8', '0'], ['0', '-1/8']])
        self.assertEqual(gram[1][2], E.Rat(m, 1))
        self.assertEqual(skew[0], E.Rat(m, 1))
        swapped, _, _ = P.omega_and_gram(j, h)
        self.assertTrue(E.equal_matrix(swapped, E.mscale(omega, E.Rat(m, -1))))

    def test_09_literal_artificial_pipeline_independent_derivatives(self):
        with patch.object(P, 'authenticate_sources', side_effect=AssertionError('actual source read')):
            result = P.artificial_body()
        self.assertEqual(result['status'], 'ARTIFICIAL_EXACT_GERM_COMPLETE')
        self.assertFalse(result['physical_source_evaluated'])
        self.assertTrue(result['independent_chain_rule_and_direct_frame_checks'])
        self.assertTrue(result['PI_determinant_and_cocycle_germ_checks'])
        self.assertEqual(result['omega_stripped'], [['1634347/403200', '0'], ['-443634889/201600', '-1634347/403200']])
        self.assertLess(result['counts']['rational_ops'], 2_000_000)
        self.assertLess(result['counts']['integer_ops'], 20_000_000)

    def test_10_physical_body_refuses_before_input_or_arithmetic(self):
        with patch.object(P, 'authenticate_sources', side_effect=AssertionError('source touched')), \
             patch.object(P, 'calculate_one', side_effect=AssertionError('arithmetic started')), \
             patch.object(P.E, 'Meter', side_effect=AssertionError('context allocated')):
            with self.assertRaises(P.PhysicalHeld):
                P._physical_body()
            with self.assertRaises(P.PhysicalHeld):
                P.physical_review_required()

    def test_11_static_auth_and_interval_proof_are_metadata_only(self):
        with patch.object(P, 'calculate_one', side_effect=AssertionError('actual evaluation')), \
             patch.object(P, 'polynomial', side_effect=AssertionError('polynomial evaluated')), \
             patch.object(P, 'direct_polynomial_mixed', side_effect=AssertionError('derivatives evaluated')):
            report = P.static_report()
        self.assertEqual(report['status'], 'STATIC_ONLY')
        self.assertFalse(report['source_values_evaluated'])
        self.assertEqual(len(report['selected_metadata']), 3)

    def test_12_same_size_source_drift_and_selection_drift_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            for name in ('spec.json', 'source-pins.json', 'sources'):
                src, dst = HERE/name, root/name
                shutil.copytree(src, dst) if src.is_dir() else shutil.copyfile(src, dst)
            with patch.object(P, 'HERE', root):
                P.authenticate_sources()
                p = root/'sources/model.json'
                original = p.read_bytes()
                p.write_bytes(original.replace(b'"pivot":0', b'"pivot":1', 1))
                if p.read_bytes() == original:
                    p.write_bytes(b' '+original[1:])
                self.assertEqual(len(p.read_bytes()), len(original))
                with self.assertRaises(E.Refusal):
                    P.authenticate_sources()
                p.write_bytes(original)
                spec = root/'spec.json'
                spec.write_bytes(spec.read_bytes().replace(b'13/6', b'14/6'))
                with self.assertRaises(E.Refusal):
                    P.fixed_spec()

    def test_13_process_and_network_descendants_refuse(self):
        import os
        import subprocess
        names = ('fork', 'forkpty', 'posix_spawn', 'posix_spawnp', 'execv', 'execve', 'execvp', 'execvpe', 'system')
        with ExitStack() as stack:
            stack.enter_context(patch.object(subprocess, 'Popen', subprocess.Popen))
            stack.enter_context(patch.object(socket, 'socket', socket.socket))
            for name in names:
                if hasattr(os, name):
                    stack.enter_context(patch.object(os, name, getattr(os, name)))
            P.deny_descendants()
            with self.assertRaises(E.Refusal):
                subprocess.Popen(['never-launched'])
            with self.assertRaises(E.Refusal):
                socket.socket()
            if hasattr(os, 'fork'):
                with self.assertRaises(E.Refusal):
                    os.fork()


if __name__ == '__main__':
    P.process_limits()
    unittest.main()
