"""Synthetic exact closed-boundary/frame controls; never physical source tests."""
import copy,json,unittest
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import transport_binding as tr
from lift_schema import closed_lift_schema,source_components

def add(a,b,c=1):
 out=dict(a)
 for k,v in b.items():
  out[k]=out.get(k,0)+c*v
  if not out[k]:del out[k]
 return out

def scalar(i,b,X):return sum(t['coefficient']*X.get((t['block'],*t['entry']),0)for t in tr.scalar_terms(i,b))
def dw(W,values):
 out={}
 for(a,b),z in W.items():
  for k,v in enumerate(values):out=add(out,{('X02',a,5*b+k):z*v})
  for i in range(15):out=add(out,{('X13',i,b):z*sum(tr.gamma(i,a,k)*values[k]for k in range(5))})
 return out

def cech(C,T):
 out={}
 for j in range(len(T)):out=add(out,C.get(T[:j]+T[j+1:],{}),(-1)**j)
 return out

def mm(a,b):return[[sum(x*y for x,y in zip(row,col))for col in zip(*b)]for row in a]
def tt(a):return[list(x)for x in zip(*a)]
def packet():
 owners=[[0,0,5,0,0],[0,1,1,1,8],[0,2,2,3,12]]
 return dict(schema='tr01-actual-source-packet-v1',source_components=source_components(),lift=closed_lift_schema(),frame=copy.deepcopy(tr.FRAME),projection_mode='complete_Rsharp_only',whole_standard_extension_witnesses=[dict(scope='whole_lift_component_and_all_prism_restrictions_on_standard_target',denominator_owners=copy.deepcopy(owners),target_standard_tags=[0,8,12],identity_sha256='a'*64,domain_sha256='b'*64)],projection_terms=[dict(owners=owners,outer_weight_owners=copy.deepcopy(owners),target_standard_tags=[0,8,12],source_sorted_owners=copy.deepcopy(owners),sorting_sign=1)],source_order='fresh',intended_order='fresh',order_witness=dict(kind='same_defined_alternating_source',proof_sha256='a'*64,source_definition_sha256='b'*64),closure_witnesses={eq:dict(proof_sha256='a'*64,domain_sha256='b'*64)for eq in closed_lift_schema()['closure_equations']})

class Controls(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.plan=tr.build_template()
 def test_authentication_32_127(self):
  self.assertEqual(json.loads(Path(__file__).with_name('transport-template.json').read_text()),self.plan)
  self.assertEqual(len(self.plan['requests']),32);self.assertEqual(sum(len(r['weighted_terms'])for r in self.plan['requests']),127)
 def test_twenty_integer_chainmaps(self):
  n=0
  for row in self.plan['scalar_maps']:
   i,b=row['label']['i'],row['label']['b']
   for a in range(5):
    for bb in range(2):
     for k in range(5):
      self.assertEqual(scalar(i,b,dw({(a,bb):1},[int(j==k)for j in range(5)])),0);n+=1
  self.assertEqual(n,1000)
 def test_wrong_sign(self):
  t=next(t for t in tr.scalar_terms(5,0)if t['block']=='X02');a,col=t['entry'];b,k=divmod(col,5);X=dw({(a,b):1},[int(j==k)for j in range(5)])
  self.assertNotEqual(scalar(5,0,X)-2*t['coefficient']*X.get(('X02',a,col),0),0)
 def test_boundary_and_mandatory_top(self):
  V=tuple(range(6));values=[2,3,5,7,11]
  K2={T:{('X13',5,0):sum(T)+1,('X02',0,0):-1}for T in combinations(V,4)}
  K3={T:({(0,0):1}if T==(0,1,2,3,4)else{})for T in combinations(V,5)}
  J2={T:add(cech(K2,T),dw(K3[T],values))for T in combinations(V,5)};J3=cech(K3,V);defect=cech(J2,V)
  self.assertTrue(J3);self.assertTrue(defect);self.assertEqual(defect,dw(J3,values))
  for row in self.plan['scalar_maps']:
   i,b=row['label']['i'],row['label']['b']
   for T in combinations(V,5):self.assertEqual(scalar(i,b,J2[T]),sum((-1)**j*scalar(i,b,K2[T[:j]+T[j+1:]])for j in range(5)))
   self.assertEqual(scalar(i,b,defect),0)
 def test_frozen_frames_and_twist(self):
  I=[[1,2],[3,5],[7,11]];P=[[2,0,1],[1,3,4]];N=[[Q(2),0],[0,Q(1,2)]];Ni=[[Q(1,2),0],[0,Q(2)]]
  for R in ([[1,2],[3,4]],[[5,7],[11,13]]):self.assertEqual(mm(mm(mm(I,tt(N)),tt(mm(mm(N,R),Ni))),mm(tt(Ni),P)),mm(mm(I,tt(R)),P))
  self.assertNotEqual([[1,0],[0,Q(-1,4)]],[[0,0],[0,0]]) # moving endpoint derivative is not core derivative
  for tau in(Q(2),Q(3,2)):self.assertEqual(tau**-2*tau**-2,tau**-4);self.assertNotEqual(tau**-4,tau**-8)
 def reject(self,change,pattern):
  p=packet();change(p)
  with self.assertRaisesRegex(ValueError,pattern):tr.validate_actual_packet(p,dict(tr.ADAPTER_SLOTS))
 def test_missing_top(self):
  self.reject(lambda p:p['lift']['nodes'].pop(),'missing top J3')
  self.reject(lambda p:p['closure_witnesses'].pop('delta J3=0'),'all five closed-lift')
 def test_projected_source(self):
  self.reject(lambda p:p['source_components'].pop(),'missing corrected source')
  self.reject(lambda p:p.update(projection_mode='tf_E34_only'),'projected directional')
  self.reject(lambda p:p['source_components'][4].update(op='tracefree_directional'),'projected E')
 def test_frame_and_order(self):
  self.reject(lambda p:p['frame'].update(scalar_tau_exponent=-2),'original frame')
  self.reject(lambda p:p['frame'].update(deck_product_removed_count=True),'original frame')
  self.reject(lambda p:p.update(intended_order='historical'),'fresh/historical')
  self.reject(lambda p:p['order_witness'].update(kind='sort_and_rebuild'),'sorting is not')
 def test_owner_retention(self):
  self.reject(lambda p:p['projection_terms'][0]['outer_weight_owners'].pop(),'weight owner lost')
  self.reject(lambda p:p['projection_terms'][0].update(target_standard_tags=[0,8]),'not a target unit')
  self.reject(lambda p:p['projection_terms'][0]['owners'][1].pop(),'five-field')
 def test_whole_standard_extension_required(self):
  self.reject(lambda p:p.update(whole_standard_extension_witnesses=[]),'whole standard-target extension')
  self.reject(lambda p:p['whole_standard_extension_witnesses'][0].update(scope='regular_only_on_common_localization'),'regularity is insufficient')
 def test_no_forged_proof(self):
  with self.assertRaisesRegex(ValueError,'pending independently reviewed null adapter'):tr.validate_actual_packet(packet(),{k:copy.deepcopy(v)for k,v in tr.ADAPTER_SLOTS.items()})
  self.reject(lambda p:p['closure_witnesses'].update({'delta J3=0':True}),'self-asserted closure')
if __name__=='__main__':unittest.main()
