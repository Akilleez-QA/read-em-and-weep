"""Invented finite split complex only; no physical source imports or data."""
from fractions import Fraction as F
import random, unittest
N=8
blocks=((0,),(1,2,3,4),(5,6),(7,))
signs=(-1,1,1,1,1,-1,-1,1)
def zero(n=N,m=N):return [[F(0) for _ in range(m)] for _ in range(n)]
def add(*xs):return [[sum(x[i][j] for x in xs) for j in range(len(xs[0][0]))] for i in range(len(xs[0]))]
def neg(x):return [[-v for v in row] for row in x]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def prod(*xs):
 a=xs[0]
 for b in xs[1:]:a=mul(a,b)
 return a
def tr(x):return sum(x[i][i] for i in range(len(x)))
def st(x):return sum(signs[i]*x[i][i] for i in range(N))
def comm(a,b):return add(mul(a,b),neg(mul(b,a)))
D=zero();H=zero()
for a,b in ((0,1),(4,5),(6,7)):D[b][a]=1;H[a][b]=1
I=zero(N,2);P=zero(2,N)
for a,b in enumerate((2,3)):I[b][a]=1;P[a][b]=1
class Projection(unittest.TestCase):
 def test_general_even_products(self):
  rng=random.Random(1510)
  def even():
   a=zero()
   for block in blocks:
    for i in block:
     for j in block:a[i][j]=F(rng.randrange(-3,4),rng.randrange(1,4))
   return a
  for _ in range(8):
   A,B=even(),even();TA,TB=comm(D,A),comm(D,B);X=mul(A,B)
   self.assertEqual(st(X),tr(prod(P,X,I))+st(prod(H,comm(D,X))))
   rhs=tr(prod(P,A,I,P,B,I))+st(prod(H,add(mul(TA,B),mul(A,TB))))-tr(prod(P,TA,H,B,I))+tr(prod(P,A,H,TB,I))
   self.assertEqual(st(X),rhs)
 def test_chain_map_specialization(self):
  A=zero();Z=zero()
  for i in range(N):A[i][i]=F(i-3,2)
  for block in blocks:
   for i in block:
    for j in block:A[i][j]+=F(i+j+1,7)
  for a,b,value in ((0,1,2),(4,5,-3),(6,7,4)):Z[a][a]=Z[b][b]=value
  Z[2][2]=1;Z[2][3]=2;Z[3][2]=-1;Z[3][3]=-1
  self.assertEqual(comm(D,Z),zero())
  TA=comm(D,A)
  self.assertEqual(st(mul(A,Z)),tr(prod(P,A,I,P,Z,I))+st(prod(H,TA,Z))-tr(prod(P,TA,H,Z,I)))
if __name__=='__main__':unittest.main(verbosity=2)
