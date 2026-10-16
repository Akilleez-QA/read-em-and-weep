"""Launcher-only tests: invented data or synthetic processes, never source values."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('launcher',HERE/'checked_launcher.py')
L=importlib.util.module_from_spec(s);s.loader.exec_module(L)

class Checks(unittest.TestCase):
    def test_physical_parent_held_before_load(self):
        with patch.object(L,'load_checked',side_effect=AssertionError('input reached')):
            with self.assertRaises(L.PhysicalHeld): L.supervise('physical')
    def test_physical_child_held_before_load(self):
        with patch.object(L,'load_checked',side_effect=AssertionError('input reached')):
            with self.assertRaises(L.PhysicalHeld): L.child('physical')
    def test_module_drift_rejected_before_import(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            (p/'prepare_omega.py').write_text("raise AssertionError('must not import')")
            with patch.object(L,'HERE',p):
                with self.assertRaisesRegex(RuntimeError,'digest mismatch'): L.load_checked()
    def test_combined_output_cap(self):
        command=[sys.executable,'-I','-c',"import os;os.write(1,b'x'*40);os.write(2,b'y'*40)"]
        out,err,code,reason=L.capture(command,timeout=2,cap=64)
        self.assertEqual(reason,'combined output cap')
        self.assertEqual(len(out)+len(err),65)
    def test_wall_timeout_kills(self):
        out,err,code,reason=L.capture([sys.executable,'-I','-c','import time;time.sleep(5)'],timeout=.1)
        self.assertEqual(reason,'wall timeout');self.assertNotEqual(code,0)
    def test_complete_protocol(self):
        out,err,code,reason=L.capture([sys.executable,'-I','-c',"import os;os.write(1,b'{}\\n');os.write(2,b'EVALUATION_STARTED\\n')"],timeout=2)
        self.assertEqual((out,err,code,reason),(b'{}\n',L.STARTED,0,None))
    def test_failed_child_keeps_started_and_no_value(self):
        with patch.object(L,'limits'),patch.object(L,'load_checked'),patch.object(L,'capture',return_value=(b'partial secret matrix',L.STARTED,-9,'wall timeout')):
            r=L.supervise('artificial')
        self.assertTrue(r['evaluation_started']);self.assertFalse(r['result_complete'])
        self.assertFalse(r['physical_source_evaluated']);self.assertNotIn('omega_stripped',r)
    def test_kill_without_marker_reports_unknown(self):
        with patch.object(L,'limits'),patch.object(L,'load_checked'),patch.object(L,'capture',return_value=(b'',b'',-9,'wall timeout')):
            r=L.supervise('artificial')
        self.assertEqual(r['evaluation_started'],'unknown')
        self.assertFalse(r['physical_source_evaluated'])
    def test_child_refusal_reason_survives_without_values(self):
        raw=b'{"status":"REFUSED_INCONCLUSIVE","reason":"integer_ops limit","omega_stripped":"must discard"}'
        with patch.object(L,'limits'),patch.object(L,'load_checked'),patch.object(L,'capture',return_value=(raw,L.STARTED,3,None)):
            r=L.supervise('artificial')
        self.assertEqual(r['reason'],'integer_ops limit')
        self.assertNotIn('omega_stripped',r)
    def test_bad_protocol_refuses(self):
        with patch.object(L,'limits'),patch.object(L,'load_checked'),patch.object(L,'capture',return_value=(b'{}',b'',0,None)):
            with self.assertRaisesRegex(RuntimeError,'protocol'):L.supervise('artificial')
    def test_emit_counts_newline(self):
        with patch.object(L,'CAP',20),patch.object(L,'STARTED',b''):
            with self.assertRaisesRegex(RuntimeError,'output cap'):L.emit({'text':'x'*20})

if __name__=='__main__': unittest.main()
