"""Regression: a nonzero replay or unit-test exit fails the review command."""

from __future__ import annotations

import importlib.util
import io
import subprocess
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

_REVIEW_PATH = Path(__file__).resolve().parents[1] / "review.py"
_SPEC = importlib.util.spec_from_file_location("hsd_review", _REVIEW_PATH)
review = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(review)


def _completed(command, code):
    return subprocess.CompletedProcess(command, code, stdout="", stderr="")


class ReplayStatusTests(unittest.TestCase):
    def _run(self, replay_exit, tests_exit, *, checks_pass=True, replay=True):
        def fake_run(command, **kwargs):
            if "unittest" in command:
                return _completed(command, tests_exit)
            if any(str(part).endswith("replay.py") for part in command):
                return _completed(command, replay_exit)
            raise AssertionError(command)

        item = {"pass": checks_pass}
        argv = ["review.py", "--replay"] if replay else ["review.py"]
        stdout = io.StringIO()
        with (
            mock.patch.object(review, "check_inverses", return_value=item),
            mock.patch.object(review, "check_minors", return_value=item),
            mock.patch.object(review, "check_quadratic", return_value=item),
            mock.patch.object(review, "check_weights", return_value=item),
            mock.patch.object(review.subprocess, "run", side_effect=fake_run),
            mock.patch.object(review.sys, "argv", argv),
            redirect_stdout(stdout),
        ):
            code = review.main()
        return code, stdout.getvalue()

    def test_failing_replay_and_failing_tests_exit_nonzero(self):
        replay_code, replay_out = self._run(1, 0)
        self.assertNotEqual(replay_code, 0)
        self.assertIn("replay stage failed: exit 1", replay_out)
        self.assertNotIn("tests stage failed", replay_out)

        tests_code, tests_out = self._run(0, 2)
        self.assertNotEqual(tests_code, 0)
        self.assertIn("tests stage failed: exit 2", tests_out)
        self.assertNotIn("replay stage failed", tests_out)

        both_code, both_out = self._run(3, 4)
        self.assertNotEqual(both_code, 0)
        self.assertIn("replay stage failed: exit 3", both_out)
        self.assertIn("tests stage failed: exit 4", both_out)

    def test_zero_replay_and_tests_exit_zero_when_checks_pass(self):
        code, output = self._run(0, 0)
        self.assertEqual(code, 0)
        self.assertNotIn("stage failed", output)

    def test_failed_independent_checks_still_exit_nonzero(self):
        code, output = self._run(0, 0, checks_pass=False, replay=False)
        self.assertNotEqual(code, 0)
        self.assertNotIn("stage failed", output)


if __name__ == "__main__":
    unittest.main()
