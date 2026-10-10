#!/usr/bin/env python3
"""Mock subprocess outcomes to test bounded orchestration, never real source work."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import evaluate_quotient as E
import run_quotient as R


class WrapperTests(unittest.TestCase):
    def exercise(self, outcomes, expected_status):
        roles = [0, 1, 2, 3]
        d = {'sumNodes': [{'sourceSymbol': 16, 'terms': [[['1', '1'], 0, [[1, 1]]]]}],
             'root': {'factors': [[16, 1]]}}
        k = {'nodes': [{'sourceSymbol': 16, 'denominator': '1'}],
             'root': {'denominator': '64'}}
        contract = {'roles': roles, 'field': 'Q', 'fixture': 'wrapper-only'}
        calls, limits, kills = [], [], []
        with tempfile.TemporaryDirectory(prefix='hm-wrapper-fixture-') as temp:
            output = Path(temp) / 'edge'
            cfg = {'outputDirectory': str(output)}
            def popen(command, **kwargs):
                index = len(calls)
                calls.append(command)
                with patch.object(R.os, 'setsid'), patch.object(R.resource, 'setrlimit', side_effect=lambda *args: limits.append(args)):
                    kwargs['preexec_fn']()
                outcome = outcomes[index]
                class FakeProcess:
                    pid = 424242
                    waits = 0
                    def wait(self, timeout=None):
                        self.waits += 1
                        if outcome == 'timeout':
                            if self.waits == 1:
                                assert timeout == 900
                                raise subprocess.TimeoutExpired(command, timeout)
                            return -9
                        assert timeout == 900
                        if outcome == 'failed': return 1
                        if outcome == 'finished':
                            (output / 'quotient.json').write_text('{}')
                            return 0
                        assert outcome == 'budget'
                        state = {'contract': contract, 'rootDenominator': 64,
                            'nextIndex': 0, 'vals': {1: {0: 1}, 2: {0: 1}, 3: {803: 1}},
                            'liveDenominators': {1: 1, 2: 1, 3: 1}, 'refs': {1: 1, 16: 1},
                            'elapsedSeconds': 1.0, 'operations': {}, 'reason': 'budget'}
                        (output / 'checkpoint.json').write_bytes(E.encode_checkpoint(state))
                        (output / 'progress.jsonl').write_text('{}\n')
                        return 0
                return FakeProcess()
            with patch.object(E, 'contract_and_inputs', return_value=(cfg, d, k, contract)), \
                 patch.object(R.subprocess, 'Popen', side_effect=popen), \
                 patch.object(R, 'validate', return_value={'status': 'PASS', 'fixture': True}), \
                 patch.object(R.os, 'killpg', side_effect=lambda *args: kills.append(args)), \
                 patch('builtins.print'):
                status = R.run(Path(temp) / 'unused-sources', roles, output)
            self.assertEqual(status, expected_status)
            self.assertEqual(len(calls), len(outcomes))
            self.assertTrue(all(call[-2:] == ['--seconds', '840'] for call in calls))
            self.assertEqual(limits, [(R.resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))] * len(outcomes))
            report = json.loads((output / 'run-report.json').read_text())
            self.assertEqual(len(report['attempts']), len(outcomes))
            if len(outcomes) == 2:
                self.assertTrue((output / 'attempt-1' / 'checkpoint.json').exists())
                self.assertTrue((output / 'attempt-1' / 'stdout.log').exists())
                self.assertFalse((output / 'attempt-2').exists())
            if 'timeout' in outcomes:
                self.assertEqual(kills, [(424242, R.signal.SIGKILL)])

    def test_finished(self): self.exercise(['finished'], 'FINISHED')
    def test_resume_then_finished(self): self.exercise(['budget', 'finished'], 'FINISHED')
    def test_attempt_bound(self): self.exercise(['budget', 'budget'], 'CHECKPOINTED_MAX_ATTEMPTS')
    def test_failure_stops(self): self.exercise(['failed'], 'FAILED')
    def test_hard_timeout_stops(self): self.exercise(['timeout'], 'HARD_TIMEOUT')
    def test_nonempty_output_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'preserved.json').write_text('{}')
            with self.assertRaisesRegex(AssertionError, 'new and empty'):
                R.run(root / 'sources', [0, 1, 2, 3], root)
            self.assertEqual((root / 'preserved.json').read_text(), '{}')


if __name__ == '__main__':
    unittest.main()
