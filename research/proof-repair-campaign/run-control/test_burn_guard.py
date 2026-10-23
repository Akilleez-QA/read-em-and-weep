"""Small fixtures only. This does not run the q-middle initializer."""
import json
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest

GUARD = Path(__file__).with_name("burn_guard.py")


class GuardTests(unittest.TestCase):
    def run_fixture(self, code, *limits):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        command = [sys.executable, str(GUARD), "--receipt", str(root / "receipt.json"),
                   "--stdout", str(root / "stdout.txt"), "--stderr", str(root / "stderr.txt"),
                   *limits, "--", sys.executable, "-c", code]
        result = subprocess.run(command, capture_output=True, text=True, timeout=12)
        return result, json.loads((root / "receipt.json").read_text()), root

    def test_success_and_outputs(self):
        result, receipt, root = self.run_fixture("import sys; print('fixture'); print('err', file=sys.stderr)")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(receipt["status"], "success")
        self.assertEqual((root / "stdout.txt").read_text(), "fixture\n")
        self.assertEqual((root / "stderr.txt").read_text(), "err\n")
        self.assertFalse(receipt["enforcement"]["address_space_limit_enforced"])
        self.assertIsNone(receipt["enforcement"]["rss_guaranteed_overshoot_bound_bytes"])
        self.assertGreaterEqual(receipt["child_cpu_seconds"], 0)
        self.assertTrue(receipt["cleanup_complete"])

    def test_tiny_rss_limit(self):
        result, receipt, _ = self.run_fixture("import time; time.sleep(5)", "--rss-bytes", "1")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "rss_limit")
        self.assertGreater(receipt["sampled_group_peak_rss_bytes"], 1)
        self.assertTrue(receipt["cleanup_complete"])
        self.assertIsNotNone(receipt["child_returncode"])

    def test_wall_timeout(self):
        result, receipt, _ = self.run_fixture("import time; time.sleep(5)", "--wall-seconds", "0.25")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "wall_limit")
        self.assertTrue(receipt["cleanup_complete"])
        self.assertLess(receipt["runtime_seconds"], 4)

    def test_invalid_limits_do_not_launch(self):
        for option, value in (("--cpu-seconds", "0"), ("--rss-bytes", "-1"),
                              ("--wall-seconds", "nan"), ("--sample-interval", "0")):
            with self.subTest(option=option):
                result, receipt, root = self.run_fixture("raise RuntimeError('must not launch')", option, value)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(receipt["status"], "invalid_configuration")
                self.assertNotIn("pid", receipt)
                self.assertFalse((root / "stdout.txt").exists())

    def test_lingering_child_is_cleaned(self):
        code = "import subprocess,sys; subprocess.Popen([sys.executable,'-c','import time;time.sleep(5)'])"
        result, receipt, _ = self.run_fixture(code)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "lingering_group")
        self.assertTrue(receipt["cleanup_complete"])

    def test_cpu_limit(self):
        result, receipt, _ = self.run_fixture("while True: pass", "--cpu-seconds", "1")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "cpu_limit")
        self.assertTrue(receipt["cleanup_complete"])

    def test_group_rss_is_aggregate(self):
        child = "import time; b=bytearray(24*1024*1024); time.sleep(5)"
        code = f"import subprocess,sys,time; children=[subprocess.Popen([sys.executable,'-c',{child!r}]) for _ in range(2)]; time.sleep(5)"
        limit = 64 * 1024 * 1024
        result, receipt, _ = self.run_fixture(code, "--rss-bytes", str(limit))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "rss_limit")
        self.assertGreater(receipt["sampled_group_peak_rss_bytes"], limit)
        self.assertTrue(all(item["rss_bytes"] < limit for item in receipt["peak_group_members"]))
        self.assertTrue(receipt["cleanup_complete"])

    def test_term_ignoring_descendant_requires_kill(self):
        child = "import signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); print('ready',flush=True); time.sleep(5)"
        code = f"import subprocess,sys; p=subprocess.Popen([sys.executable,'-c',{child!r}],stdout=subprocess.PIPE); p.stdout.readline()"
        result, receipt, _ = self.run_fixture(code)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(receipt["status"], "lingering_group")
        self.assertIn("SIGKILL", receipt["signals_sent"])
        self.assertTrue(receipt["cleanup_complete"])

    def test_supervisor_interruption_cleans_group(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = [sys.executable, str(GUARD), "--receipt", str(root / "receipt.json"),
                       "--stdout", str(root / "stdout.txt"), "--stderr", str(root / "stderr.txt"),
                       "--", sys.executable, "-c", "import time; time.sleep(5)"]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                deadline = time.monotonic() + 3
                while time.monotonic() < deadline:
                    if (root / "receipt.json").exists():
                        receipt = json.loads((root / "receipt.json").read_text())
                        if receipt.get("status") == "running":
                            break
                    time.sleep(0.02)
                else:
                    self.fail("fixture guard did not reach running state")
                process.send_signal(signal.SIGTERM)
                process.communicate(timeout=8)
                receipt = json.loads((root / "receipt.json").read_text())
                self.assertEqual(receipt["status"], "interrupted")
                self.assertTrue(receipt["cleanup_complete"])
                self.assertIsNotNone(receipt["child_returncode"])
            finally:
                if process.poll() is None:
                    process.terminate()
                    process.communicate(timeout=8)


if __name__ == "__main__":
    unittest.main()
