"""Tiny artificial-only test of the e844d047 exponent-observation repair.

python -B test_height_repair.py --field PATH_TO_field.py --bounds PATH_TO_rf_bounds.py
No SR imports, physical model values, source jets, fibers, or coefficients.
"""
import argparse,importlib.util,sys,unittest
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--field',type=Path,required=True);p.add_argument('--bounds',type=Path,required=True)
a,rest=p.parse_known_args()
def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
RF=load('ac01_fix_RF',a.field);RB=load('ac01_fix_RB',a.bounds)
class Repair(unittest.TestCase):
 def test_sparse_integer_exponent_observations(self):
  cases=0
  for degree in (0,1,2,1024,2**20):
   for coefficient in (1,2**20):
    left=dict(terms=1,degree=degree,bits=coefficient.bit_length())
    for right_degree,right_coefficient in ((0,0),(0,1),(degree,1)):
     right=dict(terms=int(bool(right_coefficient)),degree=right_degree,bits=1)
     for kind in ('add','mul','neg','partial'):
      ex=RF.Execution();x=ex.poly([((degree,0,0,0),coefficient)]);y=ex.poly([((right_degree,0,0,0),right_coefficient)])
      prediction=RB.rf_poly_bound(kind,left,right if kind in ('add','mul')else None)
      # Unary predictions need only cover their own input and operation.
      prior=x.ex.counts['bit_height'];before=dict(ex.counts)
      result=x+y if kind=='add'else x*y if kind=='mul'else -x if kind=='neg'else x.partial(0)
      self.assertLessEqual(ex.counts['bit_height'],prediction['observed_bit_height_upper'])
      for key,upper in prediction['counter_upper'].items():self.assertLessEqual(ex.counts[key]-before[key],upper)
      cases+=1
  self.assertEqual(cases,120)
 def test_rational_composition_includes_degree(self):
  for degree in (1024,2**20):
   for kind in ('add','mul','partial'):
    ex=RF.Execution();x=ex.rational(ex.poly([((degree,0,0,0),1)]));one=dict(terms=1,degree=0,bits=1)
    b=dict(numerator=dict(terms=1,degree=degree,bits=1),denominator=one)
    prediction=RB.rf_rational_bound(kind,b,b if kind!='partial'else None)
    result=x+x if kind=='add'else x*x if kind=='mul'else x.partial(0)
    self.assertLessEqual(ex.counts['bit_height'],prediction['observed_bit_height_upper'])
if __name__=='__main__':unittest.main(argv=[sys.argv[0],*rest],verbosity=2)
