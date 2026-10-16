"""Independent RF-R-1 repair controls; artificial constants only."""
import hashlib
import json
from pathlib import Path
import unittest
from field import Execution, Limits, LimitExceeded

HERE = Path(__file__).resolve().parent

class ContextFollowup(unittest.TestCase):
    def test_current_producer_bytes(self):
        marker = json.loads((HERE/'producer-ready.json').read_text())
        self.assertEqual(marker['bundle_sha256'], 'dfd6e32864e5739c65600f58da6b91261c3cd3c60dd0f43d8ec63d81f413c7a7')
        for name, expected in marker['files_sha256'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(), expected)
        lines = ''.join(f'{value}  {name}\n' for name,value in sorted(marker['files_sha256'].items()))
        self.assertEqual(hashlib.sha256(lines.encode()).hexdigest(), marker['bundle_sha256'])

    def test_foreign_arguments_reject_before_any_meter_charge(self):
        for mode in ('numerator', 'denominator', 'both'):
            with self.subTest(mode=mode):
                receiver, foreign = Execution(), Execution()
                p, q = foreign.constant(2), foreign.constant(3)
                args = {'numerator':(p, 3), 'denominator':(2, q), 'both':(p,q)}[mode]
                before = (dict(receiver.counts), dict(foreign.counts))
                with self.assertRaises(ValueError): receiver.rational(*args)
                self.assertEqual((dict(receiver.counts),dict(foreign.counts)),before)
                receiver.check(); foreign.check()

    def test_poisoned_receiver_rejects_first_without_charges(self):
        for mode in ('numerator','denominator','both','same','constants'):
            with self.subTest(mode=mode):
                receiver, foreign = Execution(Limits(products=0)), Execution()
                own = receiver.constant(5)
                p,q = foreign.constant(2),foreign.constant(3)
                with self.assertRaises(LimitExceeded): own*own
                args = {'numerator':(p,3),'denominator':(2,q),'both':(p,q),
                        'same':(own,own),'constants':(2,3)}[mode]
                before = (dict(receiver.counts),dict(foreign.counts))
                with self.assertRaises(LimitExceeded): receiver.rational(*args)
                self.assertEqual((dict(receiver.counts),dict(foreign.counts)),before)

    def test_same_context_constructor_remains_valid(self):
        e = Execution(); p,q=e.constant(2),e.constant(3)
        for args in ((p,q),(p,3),(2,q),(p,None),(2,3)):
            with self.subTest(args=tuple(type(a).__name__ for a in args)):
                value=e.rational(*args)
                self.assertIs(value.ex,e)
                expected=e.rational(2,1 if args[1] is None else 3)
                self.assertEqual(value,expected)

if __name__=='__main__': unittest.main()
