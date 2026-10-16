"""Invented 2x2 rational controls; no physical source input or evaluation."""
from fractions import Fraction as Q
import unittest

def add(*xs):return tuple(sum(x[i] for x in xs) for i in range(4))
def scale(a,x):return tuple(a*v for v in x)
def mul(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def tr(a):return a[0]+a[3]
I=(Q(1),Q(0),Q(0),Q(1))
def tf(a):return add(a,scale(-tr(a)/2,I))
def comm(a,b):return add(mul(a,b),scale(-1,mul(b,a)))

class Cancellation(unittest.TestCase):
 def test_exact_complete_identity(self):
  for n in range(1,9):
   a=(Q(n),Q(2),Q(3),Q(-n));b=(Q(0),Q(n+1),Q(1),Q(0))
   kp=scale(Q(1,4),comm(a,b));kq=scale(Q(1,4),comm(b,add(a,I)))
   self.assertEqual(tr(kp),0);self.assertEqual(tr(kq),0)
   bp,bq,cp,cq=Q(n,3),Q(2*n,5),Q(n-2,7),Q(n+1,11)
   kinetic=(Q(n),Q(2*n+1),Q(3-n),Q(4))
   ep,eq=tf(a),tf(b)
   full=add(tf(add(kinetic,scale(-bp,kq),scale(-bq,kp),scale(-bp*bq,I))),scale(bq-cq,kp),scale(bp-cp,kq),ep,eq)
   reduced=add(tf(kinetic),scale(-cq,kp),scale(-cp,kq),ep,eq)
   self.assertEqual(full,reduced)
   # Dropping a noncentral gerbe subtraction without changing Fk is wrong.
   wrong=add(tf(add(kinetic,scale(-bp,kq),scale(-bp*bq,I))),scale(bq-cq,kp),scale(bp-cp,kq),ep,eq)
   self.assertNotEqual(wrong,reduced)
 def test_tracefree_hypothesis_is_essential(self):
  kp=I;kq=(Q(0),Q(1),Q(0),Q(0));bp=bq=Q(1)
  full=add(tf(add(scale(-bp,kq),scale(-bq,kp),scale(-bp*bq,I))),scale(bq,kp),scale(bp,kq))
  self.assertEqual(full,I)
  self.assertNotEqual(full,(0,0,0,0))

if __name__=='__main__':unittest.main(verbosity=2)
