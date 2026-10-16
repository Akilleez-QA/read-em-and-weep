"""Regression for field.py at 42559cd29f71656893aa0b3c6b87fb1de203f9be.
Only artificial rational constants. Place beside field.py and run with unittest.
"""
import unittest
from fractions import Fraction
from field import Execution, Limits, LimitExceeded

class FactoryOwnershipRegression(unittest.TestCase):
    def test_reject_foreign_polynomial_pair(self):
        requested, foreign = Execution(), Execution()
        numerator, denominator = foreign.constant(2), foreign.constant(3)
        with self.assertRaises(ValueError):
            requested.rational(numerator, denominator)

    def test_poisoned_receiver_stays_closed(self):
        requested = Execution(Limits(products=0))
        foreign = Execution()
        numerator, denominator = foreign.constant(2), foreign.constant(3)
        with self.assertRaises(LimitExceeded):
            requested.mul(Fraction(1), Fraction(1))
        with self.assertRaises(LimitExceeded):
            requested.rational(numerator, denominator)

if __name__ == '__main__':
    unittest.main(verbosity=2)
