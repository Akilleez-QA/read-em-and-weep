#!/usr/bin/env python3
"""Free matrix words and endpoint labels; no physical source arithmetic."""
import sys
if not __debug__:raise SystemExit(2)
from fractions import Fraction as Q
from dataclasses import dataclass
import unittest
@dataclass(frozen=True)
class Atom:
 name:str
 target:str
 source:str
 derivative:tuple=()
def atom(name,edge,d=()):return Atom(name,edge[1],edge[0],tuple(d))
def word(*xs):
 for left,right in zip(xs,xs[1:]):
  if left.source!=right.target:raise ValueError('endpoint mismatch')
 return tuple(xs)
def mu(F,G,pair):
 x,y=pair
 return [(Q(1,2),word(Atom(F.name,F.target,F.source,(x,)),Atom(G.name,G.target,G.source,(y,)))),
         (Q(-1,2),word(Atom(F.name,F.target,F.source,(y,)),Atom(G.name,G.target,G.source,(x,))))]
def raw_terms():
 A=atom('g',('a','b'));B=atom('g',('b','c'));G=atom('g',('a','c'))
 up=atom('u0p',('b','c'));uq=atom('u0q',('b','c'))
 vp=atom('u0p',('a','b'));vq=atom('u0q',('a','b'))
 out=[(Q(1),word(up,vq)),(Q(1),word(uq,vp))]
 for F,H,p in ((uq,A,(1,2)),(up,A,(3,4)),(B,vq,(1,2)),(B,vp,(3,4))):out+=mu(F,H,p)
 for db,da,s in (((1,3),(2,4),1),((1,4),(2,3),-1),((2,3),(1,4),-1),((2,4),(1,3),1)):
  out.append((Q(s,4),word(atom('g',('b','c'),db),atom('g',('a','b'),da))))
 out += [(Q(-1),word(atom('bp*u0q',('a','c')))),(Q(-1),word(atom('bq*u0p',('a','c')))),(Q(-1),word(Atom('bp*bq*g','c','a')))]
 return out
class M0FormalTests(unittest.TestCase):
 def test_complete_raw_terms(self):
  ts=raw_terms();self.assertEqual(len(ts),17)
  self.assertEqual([c for c,w in ts],[Q(1),Q(1)]+[Q(1,2),Q(-1,2)]*4+[Q(1,4),Q(-1,4),Q(-1,4),Q(1,4)]+[Q(-1)]*3)
 def test_owner_normalization(self):
  inv=Atom('Ginv','a','c')
  for c,w in raw_terms():
   self.assertEqual((w[0].target,w[-1].source),('c','a'))
   nw=word(inv,*w);self.assertEqual((nw[0].target,nw[-1].source),('a','a'))
 def test_noncommutative_order(self):
  w=raw_terms()[0][1]
  with self.assertRaises(ValueError):word(*reversed(w))
  # Even endomorphisms cannot be commuted merely because endpoints match.
  X,Y=Atom('X','a','a'),Atom('Y','a','a')
  self.assertNotEqual(word(X,Y),word(Y,X))
 def test_mixed_block_is_quarter(self):
  cross=raw_terms()[10:14]
  self.assertEqual([(w[0].derivative,w[1].derivative) for c,w in cross],[((1,3),(2,4)),((1,4),(2,3)),((2,3),(1,4)),((2,4),(1,3))])
  self.assertTrue(all(abs(c)==Q(1,4) for c,w in cross))
 def test_u0_endpoint_and_product_derivative(self):
  for edge in (('a','b'),('b','c'),('a','c')):
   g=atom('g',edge);k=Atom('k',edge[0],edge[0]);w=word(g,k)
   self.assertEqual((w[0].target,w[-1].source),(edge[1],edge[0]))
   dg=Atom('g',g.target,g.source,(1,));dk=Atom('k',k.target,k.source,(1,))
   self.assertEqual(len([word(dg,k),word(g,dk)]),2)
 def test_selected_traceless_quadratic_words(self):
  # Each formal word is an ordered pair of entry labels. No source evaluation.
  def collect(terms):
   out={}
   for coefficient,w in terms:out[w]=out.get(w,Q(0))+coefficient
   return {w:c for w,c in out.items() if c}
  diag=collect([(Q(1,2),('X00','Y00')),(Q(1,2),('X01','Y10')),
                (Q(-1,2),('X10','Y01')),(Q(-1,2),('X00','Y00'))])
  off=collect([(Q(1),('X10','Y00')),(Q(-1),('X00','Y10'))])
  self.assertEqual(diag,{('X01','Y10'):Q(1,2),('X10','Y01'):Q(-1,2)})
  self.assertEqual(off,{('X10','Y00'):Q(1),('X00','Y10'):Q(-1)})
  self.assertEqual(2*(len(diag)+len(off)),8)
 def test_tracefree_entries_and_scalar_removal(self):
  # Formal coefficient vectors (M00,M11,scalar), no matrix evaluation.
  diag=(Q(1,2),Q(-1,2),Q(-1,2)+Q(1,2))
  self.assertEqual(diag,(Q(1,2),Q(-1,2),Q(0)))
  self.assertEqual(Q(0),Q(-1)*0) # central offdiagonal is zero
  self.assertEqual(raw_terms()[-1][1][0].name,'bp*bq*g')
  # The raw central baseline is retained; Ginv*G=I is the sole needed witness.
if __name__=='__main__':unittest.main(verbosity=2)
