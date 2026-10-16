"""STD-R bounded artificial controls, stdlib only; no producer fixtures."""
from collections import defaultdict
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product, combinations
import unittest
from unittest.mock import patch
import standard as S
I=S.I
E=(0,0,0,0)
CELLS=tuple(product('ABC',repeat=4))
def clean(d):return {k:v for k,v in d.items() if v}
def faces(s):return [(s[:j]+s[j+1:],(-1)**j) for j in range(len(s))]
def bd(chain):
 out=defaultdict(Q)
 for s,c in chain.items():
  if len(s)>1:
   for t,z in faces(s):out[t]+=c*z
 return clean(out)
def regular(c,e,n):return all(s=='C' or (x>=0 if s=='A' else x<=t) for s,x,t in zip(c,e,n))
def differential(v):
 # Independent forward delta: A -> -C, B -> C, with tensor signs.
 out=defaultdict(Q)
 for c,z in v.items():
  for j,s in enumerate(c):
   if s!='C':out[c[:j]+('C',)+c[j+1:]]+=z*(-1)**c[:j].count('C')*(-1 if s=='A' else 1)
 return clean(out)
def h(v,e,n):
 out={}
 for c in CELLS:
  if regular(c,e,n):out[c]=sum(z*v.get(t,0) for z,t,_ in S.h_requests(c,e,n))
 return clean(out)
def projection(c,e,n):
 options=[]
 for s,x,t in zip(c,e,n):
  if t==0 and s=='B' and x==0:options.append(('A','B'))
  elif t==-2 and s=='C' and x==-1:options.append(('C',))
  else:return {}
 return {c:Q(1) for c in product(*options)}
def edge(a=0,b=12):return (I.FullOwner(17,('outer',2),5,3,a),I.FullOwner(17,('outer',3),5,3,b))
def witness(os,t):return I.RegularExtensionWitness('synthetic','whole-toy-summand',tuple(t),tuple(os),'entire-standard-target')
class Fibers:
 mode='synthetic'
 def owners(self,t,o):return (I.FullOwner(23,o,{0:2,8:0,12:5}[t],t,t),)
class Numerator:
 mode='synthetic'
 def __init__(self):self.calls=[]
 def degree_upper(self,os,pair=(0,1)):return (1,0,0,0)
 def coefficient(self,os,e,pair=(0,1)):
  if [o.carrier for o in os]!=[5,0,2]:raise ValueError('auxiliary-first sorted source required')
  if min(e)<0:raise ValueError('negative polynomial request')
  self.calls.append((tuple(os),e,pair))
  return {E:Q(5,7),(1,0,0,0):Q(-2,3)}.get(e,Q(0))
class Quotients:
 mode='synthetic'
 def factor_terms(self,o,pair=(0,1)):return [((-1,0,0,0),Q(1,2)),(E,Q(-3,2))]
def pi_fixture(extension=witness,fibers=None,quotients=None):
 n=Numerator();return S.PiCoefficientProgram(n,quotients or Quotients(),fibers or Fibers(),extension),n

class IndependentControls(unittest.TestCase):
 def test_explicit_bit_orientation_and_staircase(self):
  self.assertEqual([S.bits(t) for t in (8,4,2,1)],[(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)])
  self.assertEqual(S.stairs(('C','C','B','A')),[(1,(2,10,14)),(-1,(2,6,14))])
  self.assertEqual(S.aw_cells((12,0)),[(-1,('C','B','A','A')),(-1,('A','C','A','A'))])
  self.assertEqual(S.aw_cells((0,0)),[])
  self.assertEqual(S.k_chain((12,0)),{(0,4,12):1})
 def test_cone_higher_degrees_and_rectangle(self):
  for s in ((1,3,5,15),(2,4,9,14),(0,1,4,10,15),(0,1,3,7,11,15)):
   left=defaultdict(Q,bd(S.k_chain(s)))
   for face,z in faces(s):
    for t,a in S.k_chain(face).items():left[t]+=z*a
   right=defaultdict(Q,{s:Q(1)})
   for z,c in S.aw_cells(s):
    for a,t in S.stairs(c):right[t]-=z*a
   self.assertEqual(clean(left),clean(right))
   lo,hi=15,0
   for v in s:lo&=v;hi|=v
   for t in S.k_chain(s):self.assertTrue(all((v&lo)==lo and (v|hi)==hi for v in t))
   self.assertEqual(S.k_chain(s[::-1]),{t:(-1)**(len(s)*(len(s)-1)//2)*z for t,z in S.k_chain(s).items()})
 def test_tensor_identity_regular_basis_thresholds(self):
  es=[E,(-1,-1,0,0),(0,0,-1,-1),(-2,-3,0,1),(2,0,-2,-3),(-1,-2,-1,0),(0,-1,1,-2),(1,2,3,4),(-3,-2,-1,-3)]
  count=0
  for n in (S.TWIST,S.F34_TWIST,E):
   for e in es:
    for c in CELLS:
     if not regular(c,e,n):continue
     v={c:Q(1)};lhs=defaultdict(Q,differential(h(v,e,n)))
     for t,z in h(differential(v),e,n).items():lhs[t]+=z
     rhs=defaultdict(Q,v)
     for t,z in projection(c,e,n).items():rhs[t]-=z
     self.assertEqual(clean(lhs),clean(rhs),(n,e,c));count+=1
  self.assertGreater(count,300)
 def test_nonclosed_identity_requires_B_delta(self):
  e=(-1,-1,0,0);data={(0,8,12):{e:Q(7,3)}}
  p=S.StandardProgram(S.SyntheticStandardCochain(data))
  def f(s):return data.get(s,{}).get(e,Q(0))
  def df(s):return sum(z*f(t) for t,z in faces(s))
  def bdf(s):
   out=sum(z*df(t) for t,z in S.k_chain(s).items())
   for a,c in S.aw_cells(s):
    for b,inc,_ in S.h_requests(c,e):out+=sum(a*b*z*df(t) for z,t in S.stairs(inc))
   return out
  self.assertNotEqual(df((0,1,8,12)),0);nonzero=False
  for s in ((0,1,8),(0,8,12),(1,8,12),(0,4,12),(0,12,15)):
   db=sum(z*sum(p.branches(t,e).values()) for t,z in faces(s));r=bdf(s);nonzero|=r!=0
   self.assertEqual(db+r,f(s)-p.harmonic_image(s,e))
  self.assertTrue(nonzero)
 def test_closed_harmonic_counterexample_both_pairs(self):
  for pair,n in (((0,1),S.TWIST),((2,3),S.F34_TWIST)):
   e=tuple(-1 if j in pair else 0 for j in range(4))
   # Independent cut-bit formula for the AW harmonic image.
   def harmonic(s):
    a,b=pair;bit=lambda t,j:(t>>(3-j))&1
    return (bit(s[1],a)-bit(s[0],a))*(bit(s[2],b)-bit(s[1],b))
   triples=tuple(combinations(range(16),3))
   data={s:{e:Q(harmonic(s))} for s in triples if harmonic(s)}
   p=S.StandardProgram(S.SyntheticStandardCochain(data,n));self.assertEqual(p.harmonic_projection(),1)
   for tetra in ((0,1,8,12),(0,4,8,15),(1,3,7,15)):
    self.assertEqual(sum(z*harmonic(t) for t,z in faces(tetra)),0)
   self.assertTrue(any(harmonic(t) for t in triples))
   for s in triples:
    self.assertEqual(sum(z*sum(p.branches(t,e).values()) for t,z in faces(s)),0)
    self.assertEqual(p.harmonic_image(s,e),harmonic(s))
   self.assertFalse(p.contract()['actual_first_order_primitive_witness'])
 def test_multiterm_Pi_convolution_and_owner_trace(self):
  pi,n=pi_fixture();expected={0:Q(5,7),1:Q(-2,3)}
  # Independent sparse multiplication of (x^-1/2-3/2)^3*(5/7-2x/3).
  for _ in range(3):
   out=defaultdict(Q)
   for a,c in expected.items():
    for b,d in ((-1,Q(1,2)),(0,Q(-3,2))):out[a+b]+=c*d
   expected=clean(out)
  for k in (-4,-3,-2,-1,0,1,2):
   self.assertEqual(pi.coefficient((0,8,12),(k,0,0,0)),-expected.get(k,0))
   self.assertEqual(pi.coefficient((8,0,12),(k,0,0,0)),expected.get(k,0))
  self.assertTrue(n.calls)
  for os,e,pair in n.calls:
   self.assertTrue(0<=e[0]<=1);self.assertEqual([o.seed for o in os],[23]*3)
   self.assertEqual({o.occurrence for o in os},{('Pi',(0,8,12),j) for j in range(3)})
  self.assertTrue(all(t['source_sign']==-1 for t in pi.trace))
  before=len(n.calls);pi.coefficient((0,8,12),E);self.assertEqual(len(n.calls),before)
 def test_extension_refuses_each_lost_binding(self):
  changes=[lambda w:replace(w,scope='common_local_only'),lambda w:replace(w,target_standard_tags=(0,8,13)),lambda w:replace(w,owned_clearings=w.owned_clearings[::-1]),lambda w:replace(w,owned_clearings=tuple(replace(o,seed=99) for o in w.owned_clearings)),lambda w:replace(w,whole_coefficient_id=''),lambda w:replace(w,domain_id='')]
  for change in changes:
   pi,n=pi_fixture(lambda os,t:change(witness(os,t)))
   with self.assertRaises(ValueError):pi.coefficient((0,8,12),E)
   self.assertEqual(n.calls,[])
  pi,n=pi_fixture(lambda os,t:True)
  with self.assertRaises(ValueError):pi.coefficient((0,8,12),E)
  for s,e in (((0,1,2),(-1,0,0,0)),((8,9,10),(-1,0,0,0))):
   with self.assertRaises(ValueError):S.SyntheticStandardCochain({s:{e:1}})
 def test_fiber_and_quotient_refusals(self):
  class Wrong(Fibers):
   def owners(self,t,o):return (replace(super().owners(t,o)[0],occurrence='lost'),)
  class Duplicate(Fibers):
   def owners(self,t,o):
    v=super().owners(t,o)[0];return (v,replace(v,seed=999))
  class Terms(Quotients):
   def factor_terms(self,o,pair=(0,1)):return [(E,1),(E,-1)]
  for fs,qs in ((Wrong(),None),(Duplicate(),None),(None,Terms())):
   pi,n=pi_fixture(fibers=fs,quotients=qs)
   with self.assertRaises(ValueError):pi.coefficient((0,8,12),E)
   self.assertEqual(n.calls,[])
 def test_full_R_and_pre_h_derivatives(self):
  p=S.StandardProgram(S.SyntheticStandardCochain({(0,8,12):{E:Q(2)}}));os=edge()
  self.assertNotEqual(p.coefficient(os,E),0)
  self.assertEqual(p.coefficient(os[::-1],E),-p.coefficient(os,E))
  self.assertEqual(p.coefficient(edge(0,0),E),0)
  with self.assertRaises(ValueError):p.coefficient((os[0],replace(os[1],occurrence=os[0].occurrence)),E)
  with patch.object(p,'branches',wraps=p.branches) as branches:
   with patch.object(S,'h_requests',wraps=S.h_requests) as hh:
    self.assertEqual(p.coefficient(os,(0,0,-2,0),2),0)
    self.assertTrue(hh.call_args_list)
    self.assertTrue(all(c.args[1]==(0,0,-1,0) for c in hh.call_args_list))
   before=branches.call_count;self.assertEqual(p.coefficient(os,(0,0,-1,0),2),0)
   self.assertEqual(branches.call_count,before)
  p2=S.StandardProgram(S.SyntheticStandardCochain({(0,8,12):{(0,0,2,0):Q(3,5)}}))
  self.assertNotEqual(p2.coefficient(os,(0,0,2,0)),0)
  self.assertEqual(p2.coefficient(os,(0,0,1,0),2),2*p2.coefficient(os,(0,0,2,0)))
  with self.assertRaises(ValueError):p2.coefficient(os,E,0)
 def test_support_metadata_and_inserted_padding_boundary(self):
  class AllToyTags:
   mode='synthetic'
   def owners(self,t,o):return (I.FullOwner(23,o,t%6,t,t),)
  pi,n=pi_fixture(fibers=AllToyTags())
  self.assertEqual(pi.support_box(),((-3,0,0,0),(1,0,0,0)))
  self.assertEqual(n.calls,[])  # No source values needed for the enclosure.
  from types import SimpleNamespace
  from inserted_program import SparseOracle, WholeNumerator
  from polynomial_coefficients import Budget
  p=S.StandardProgram(S.SyntheticStandardCochain({(0,8,12):{E:Q(2)}}))
  bound=S.StandardEdgeOracle(p).bind(edge())
  self.assertEqual(bound.owners,edge())
  budget=Budget()
  ca=SparseOracle({(1,0,0,0):2},budget)
  cb=SparseOracle({(0,0,1,0):3},budget)
  toy_prism=SimpleNamespace(mode='synthetic',C_a=ca,Z=(0,0,0,1),budget=budget,
                            coefficient=lambda kind,e:Q(0))
  whole=WholeNumerator(bound,toy_prism,cb,None)
  self.assertEqual(whole.support_box(),((1,0,1,1),(1,0,1,1)))
  self.assertNotEqual(bound.coefficient(E),0)
  self.assertEqual(whole.coefficient((1,0,1,1)),6*bound.coefficient(E))
  self.assertEqual(whole.coefficient(E),0)
 def test_physical_modes_rejected_even_with_cached_values(self):
  pi,n=pi_fixture();pi.coefficient((0,8,12),E)
  for obj in (pi.F,pi.Q,pi.fibers):
   obj.mode='physical'
   with self.assertRaises(I.PhysicalAdmissionMissing):pi.coefficient((0,8,12),E)
   obj.mode='synthetic'
  p=S.StandardProgram(S.SyntheticStandardCochain({}));p.coefficient(edge(),E);p.pi.mode='physical'
  with self.assertRaises(I.PhysicalAdmissionMissing):p.coefficient(edge(),E)
  w=witness(Fibers().owners(0,'x'),(0,))
  with self.assertRaises(I.PhysicalAdmissionMissing):replace(w,evidence='physical').require(w.owned_clearings,(0,))
  for bad in (True,1.0):
   with self.assertRaises(ValueError):S.h_requests(('A','C','A','A'),(bad,0,0,0))
   with self.assertRaises(ValueError):S.rational(bad)

if __name__=='__main__':unittest.main()
