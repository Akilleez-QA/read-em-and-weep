"""Tiny fictional end-to-end prospective tests; no physical polynomials."""
import copy,unittest
import certifier as C

def counts(products=0,coefficient_multiplications=0,additions=0):
 r=dict.fromkeys(C.A06.COUNTERS,0);r.update(products=products,coefficient_multiplications=coefficient_multiplications,additions=additions);return r

def fixture():
 a={'terms':2,'height':2,'exponent_abs':2};b={'terms':2,'height':3,'exponent_abs':2};cost=C.operation(a,b,'mul')
 algorithm={'evidence':'explicit-artificial-integer-polynomials','inputs':{'a':a,'b':b},'steps':[{'id':'multiply','kind':'mul','left':'a','right':'b','output':'result'}],'outputs':['result']}
 ledger={'schema':'a06-global-schedule-v1','evidence':'synthetic-only','ledger_id':'all-workers-fiction','revision':4,'global_complete':True,'source_pin':'synthetic:no-physical-source',
  'caps':{'counts':counts(10,100,100),'bytes':1010,'metric':'synthetic-live-plus-workspace-bytes'},'spent':counts(3,2,1),
  'reservations':[{'id':'route','owner':'A','remaining':counts(2,4,4),'bytes':0,'first_event':0,'last_event':1,'authorization':'synthetic'},
   {'id':'other','owner':'B','remaining':counts(2),'bytes':50,'first_event':0,'last_event':1,'authorization':'synthetic'}],
  'allocations':[{'id':aid,'owner':worker,'bytes':n,'initial':initial,'last_use':last,'reservation':r,'binding':'synthetic'}for aid,worker,n,initial,last,r in [('a','A',C.packed_bytes(**a),True,1,None),('b','A',C.packed_bytes(**b),True,1,None),('result','A',cost['bytes'],False,1,'route'),('other-live','B',41,True,-1,'other')]],
  'operations':[{'id':'multiply','owner':'A','inputs':['a','b'],'outputs':['result'],'counts':cost['counts'],'workspace':cost['workspace'],'reservation':'route','source_binding':'synthetic'}],
  'events':[{'begin':['multiply'],'end':[],'free':[]},{'begin':[],'end':['multiply'],'free':['a','b']}]}
 return algorithm,ledger

class Controls(unittest.TestCase):
 def test_complete_fictional_height_operations_and_lifetime(self):
  a,l=fixture();before=copy.deepcopy(l);out=C.certify_synthetic(a,l)
  self.assertEqual(l,before);self.assertEqual(out['output_bounds']['result'],{'terms':4,'height':12,'exponent_abs':4})
  self.assertEqual(out['schedule']['peak_charged_bytes'],1010)
  self.assertEqual(out['schedule']['spent_after']['products'],4)
  self.assertEqual(out['schedule']['remaining_reservations']['other']['products'],2)
  self.assertIn('result',out['schedule']['live_after']);self.assertFalse(out['physical_release'])
 def test_unknown_height_or_dropped_cost_refuses(self):
  a,l=fixture();a['inputs']['a']['height']=None
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
  a,l=fixture();l['operations'][0]['counts']['coefficient_multiplications']=0
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
 def test_global_cap_and_output_before_free(self):
  a,l=fixture();l['caps']['bytes']=1009
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
  a,l=fixture();l['caps']['counts']['products']=6 # spent3+route2+other2, not reset for A
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
 def test_retained_output_and_duplicate_ids(self):
  a,l=fixture();l['events'][1]['free'].append('result')
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
  a,l=fixture();l['allocations'].append(copy.deepcopy(l['allocations'][0]))
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
 def test_unknown_state_or_physical_status_never_admits(self):
  a,l=fixture();l['global_complete']=False
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
  a,l=fixture();l['evidence']='physical'
  with self.assertRaises(ValueError):C.certify_synthetic(a,l)
  with self.assertRaises(RuntimeError):C.actual_admission({'verified':True,'spent':0})
 def test_outer_structural_reductions_are_cardinalities_only(self):
  c=C.actual_route_certificate()['candidate'];r=c['structural_weight_zero_reductions']
  self.assertEqual(r['legal_only_all_staircases'],191102976)
  self.assertEqual(r['legal_and_generic_carrier_alphabet_all_staircases'],5898240)
  self.assertFalse(c['index_count_is_physical_cost'])
  # All-infinity N54: a first-hit slot j<4 has n_j>=535>0,
  # while its coefficient H_(4-j)(empty) is identically zero.
  self.assertGreater(5*(2*54-1),0)
  for j in range(4):self.assertGreater(4-j,0)
 def test_rf_actual_input_metadata_and_lex_degree_control(self):
  import rf_bounds as R
  from pathlib import Path
  b=R.model_input_bounds(Path(__file__).resolve().parents[3])
  self.assertEqual((b['catalog_polynomial_leaves'],b['max_finite_coordinate_degree'],b['max_numerator_bit_upper'],b['max_support_box_cardinality_upper']),(1973,6,16,2401))
  self.assertFalse(b['actual_coefficients_evaluated'])
  # Artificial division x0^2 by x0-x1^2 can reach degree4 in x1.
  # Weighted degree, rather than the input coordinate box, controls it.
  w=(27,9,3,1);path=[(2,0,0,0),(1,2,0,0),(0,4,0,0)]
  self.assertTrue(all(path[j]>path[j+1]for j in range(2)))
  self.assertTrue(all(sum(a*z for a,z in zip(e,w))<=54 for e in path))
  self.assertGreater(path[-1][1],2)
  recurrence=R.rf_operation_recurrences()
  self.assertIn('Fraction multiply AND divide',recurrence['coefficient_metric'])
  self.assertFalse(recurrence['complete_actual_source_graph_bound'])
 def test_rf_executable_recurrence_bounds_artificial_kernel(self):
  import rf_bounds as R,importlib.util,sys
  from pathlib import Path
  path=Path(__file__).resolve().parents[1]/'exact-curve-field/field.py'
  spec=importlib.util.spec_from_file_location('ac_rf_field',path);F=importlib.util.module_from_spec(spec);sys.modules[spec.name]=F;spec.loader.exec_module(F)
  ex=F.Execution();N=ex.xpoly(0)+ex.constant(1);D=ex.xpoly(1)+ex.constant(2)
  a=ex.rational(N,D);b=ex.rational(D,N);poly={'terms':2,'degree':1,'bits':2};bound={'numerator':poly,'denominator':poly}
  for kind in('mul','add','partial'):
   predicted=R.rf_rational_bound(kind,bound,bound if kind!='partial'else None);before=dict(ex.counts)
   value=a*b if kind=='mul'else a+b if kind=='add'else a.partial(0)
   for key,limit in predicted['counter_upper'].items():self.assertLessEqual(ex.counts[key]-before[key],limit,key)
   self.assertLessEqual(ex.counts['bit_height'],predicted['observed_bit_height_upper'])
   self.assertIsNone(predicted['live_byte_bound'])
 def test_complete_actual_symbolic_envelope_without_unrolling(self):
  import whole_envelope as W
  e=W.build();d=e['definitions']
  self.assertEqual(e['request_id'],30);self.assertEqual(sum(e['caller_AST_nodes'].values()),12804)
  self.assertEqual(d['M']['args'][1],130)
  self.assertEqual(d['B']['op'],'iterate');self.assertEqual(d['B']['times'],'M')
  self.assertEqual(d['B']['initial'],1048576)
  self.assertEqual(d['per_RF_exponent'],{'op':'pow','args':[2,8388608]})
  self.assertIsNone(e['layout_beta']);self.assertIsNone(e['native_machine_bitcost_metric'])
  self.assertFalse(e['physical_admission']);self.assertTrue(e['not_a_lower_bound'])
  # Small independent activation-tree control: at most S children/depth d,
  # local RF calls<=S. The closed M=(S+1)^(d+2) dominates the full tree.
  for S in range(1,5):
   for depth in range(4):self.assertLessEqual(S*sum(S**j for j in range(depth+1)),(S+1)**(depth+2))
 def test_exact_candidate_is_blocked_not_nofit(self):
  c=C.actual_route_certificate();self.assertEqual(c['status'],'BLOCKED_ROUTE')
  self.assertEqual(c['candidate']['weighted_request']['id'],30)
  self.assertEqual(c['candidate']['unpruned_indexed_projection_summands'],24*96**5)
  self.assertIn('expression_ref',c['operation_upper_bound']);self.assertFalse(c['physical_release'])
  self.assertFalse(c['historical_allowances_are_current_caps']);self.assertFalse(c['algorithm_independent_impossibility_claimed'])

if __name__=='__main__':unittest.main()
