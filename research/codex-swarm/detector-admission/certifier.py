"""Prospective synthetic packed-buffer certificate; actual route stays blocked."""
from pathlib import Path
import sys,importlib.util,json,hashlib,math,copy
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/'arithmetic/ledger'))
import schedule_validator as A06
need=A06.need

def nat(n):need(type(n)is int and n>=0,'unknown count/height/byte bound');return n

def packed_bytes(terms,height,exponent_abs):
 """Specified fictional packed integer layout, not Python occupancy.
 32-byte header; each sparse slot: 4 signed64 exponents,8-byte length,
 8-byte index,1 sign byte, and ceil(log2(height+1)/8) magnitude bytes.
 """
 n,h=nat(terms),nat(height);need(nat(exponent_abs)<2**63,'signed64 exponent overflow');return 32+n*(49+max(1,(h.bit_length()+7)//8))

def operation(left,right,kind):
 for b in(left,right):
  need(set(b)=={'terms','height','exponent_abs'},'exact artificial polynomial bound fields');nat(b['terms']);nat(b['height']);nat(b['exponent_abs'])
 m,n=left['terms'],right['terms'];a,b=left['height'],right['height']
 if kind=='mul':
  out={'terms':m*n,'height':min(m,n)*a*b,'exponent_abs':left['exponent_abs']+right['exponent_abs']};mult=m*n;add=m*n;products=1
 elif kind=='add':
  out={'terms':m+n,'height':a+b,'exponent_abs':max(left['exponent_abs'],right['exponent_abs'])};mult=0;add=m+n;products=0
 else:raise ValueError('specified integer pair-product/merge algorithm only')
 counts=dict.fromkeys(A06.COUNTERS,0);counts.update(products=products,coefficient_multiplications=mult,additions=add)
 # Two complete staging buffers accompany the final output before input frees.
 return {'bound':out,'bytes':packed_bytes(**out),'workspace':2*packed_bytes(**out),'counts':counts}

def certify_synthetic(algorithm,ledger):
 """Authenticate no physical evidence. Join cost/height/layout to global events."""
 need(type(algorithm)is dict and set(algorithm)=={'evidence','inputs','steps','outputs'},'exact algorithm fields')
 need(algorithm['evidence']=='explicit-artificial-integer-polynomials','actual algorithms unsupported')
 need(type(algorithm['inputs'])is dict and type(algorithm['steps'])is list,'finite artificial program')
 need(len(algorithm['inputs'])+len(algorithm['steps'])<=64,'tiny prospective program')
 bounds={};allocs={a['id']:a for a in ledger['allocations']};ops={o['id']:o for o in ledger['operations']}
 used=[]
 for aid,b in algorithm['inputs'].items():
  need(set(b)=={'terms','height','exponent_abs'},'input bound');size=packed_bytes(**b)
  need(aid in allocs and allocs[aid]['initial']and allocs[aid]['bytes']==size,'input allocation/height mismatch');bounds[aid]=dict(b)
 for step in algorithm['steps']:
  need(set(step)=={'id','kind','left','right','output'},'specified step fields')
  oid=step['id'];left=step['left'];right=step['right'];out=step['output']
  need(left in bounds and right in bounds and out not in bounds,'topological unique allocation')
  cost=operation(bounds[left],bounds[right],step['kind']);need(oid in ops,'missing scheduled operation');o=ops[oid]
  need(o['inputs']==list(dict.fromkeys([left,right]))and o['outputs']==[out],'source operation schedule mismatch')
  need(o['counts']==cost['counts']and o['workspace']==cost['workspace'],'missing operation/workspace bound')
  need(out in allocs and allocs[out]['bytes']==cost['bytes'],'output allocation/height mismatch')
  bounds[out]=cost['bound'];used.append(oid)
 need(type(algorithm['outputs'])is list and algorithm['outputs']and all(o in bounds for o in algorithm['outputs']),'retained final outputs')
 replay=A06.validate(copy.deepcopy(ledger))
 need(set(algorithm['outputs'])<=set(replay['live_after']),'final output freed before handoff')
 return {'status':'SYNTHETIC_PROSPECTIVE_CERTIFIED','operation_ids':used,'output_bounds':{o:bounds[o]for o in algorithm['outputs']},
  'layout':'fictional-packed-integer-sparse-v1','schedule':replay,'physical_release':False}

def authenticate_inputs():
 pins=json.loads(Path(__file__).with_name('source-pins.json').read_text())
 for row in pins['workspace_inputs']:
  need(hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest()==row['sha256'],'certificate input pin drift')
 need(Path(A06.__file__).resolve()==(BASE/'arithmetic/ledger/schedule_validator.py').resolve(),'foreign global schedule verifier')
 return pins

def actual_route_certificate():
 """A concrete blocked route: unknowns remain named obligations, never zero."""
 pins=authenticate_inputs()
 candidate=json.loads(Path(__file__).with_name('candidate-route.json').read_text())
 published=json.loads((BASE/'detector-selection/weighted-requests.json').read_text())
 need(candidate['weighted_request']==next(r for r in published['requests']if r['id']==30),'exact detector request drift')
 evidence=json.loads(Path(__file__).with_name('ledger-evidence.json').read_text())
 missing_global=['current authoritative ledger identity/revision and applicability to all workers',
  'current operation cap definitions and protected-vs-scratch byte metric',
  'measured spent counters including prerequisites and prior work',
  'all outstanding reservation IDs/owners/remaining counters/time intervals',
  'all live allocation IDs/aliases/bytes/layouts/owners/last uses',
  'current arithmetic hold and explicit physical release authority']
 missing_cost=['independent denotation/control-envelope acceptance for the pinned literal SR01 raw source program',
  'authoritative mapping of RF Fraction-operation and native-integer units to the actual shared cap metric',
  'review of the instantiated symbolic whole-root/weighted-degree exact-division height envelope under the named source/model premises',
  'machine representation linking those bit bounds to buffer/workspace bytes',
  'serial begin/end/output-before-free events joined with every other active worker and retained final outputs']
 return {'schema':'detector-route-prospective-status-v1','status':'BLOCKED_ROUTE','candidate':candidate,
  'input_pins':pins,'evidence_scope':evidence['searched_scope'],'authoritative_reconciled_ledger':None,
  'missing_global_evidence':missing_global,'missing_actual_algorithm_proofs':missing_cost,
  'whole_route_upper_envelope':__import__('whole_envelope').build(),
  'operation_upper_bound':{'expression_ref':'whole-route-envelope.json:RF_total','scope':'each RF Fraction-products/steps/storage_events counter; integer binomials separately bounded'},
  'coefficient_height_upper_bound':{'expression_ref':'whole-route-envelope.json:B,terminal_height_H'},
  'aggregate_peak_bytes':None,'layout_byte_factor':None,
  'unresolved_actual_root':{'name':'authoritative_metric_layout_beta_and_all_worker_ledger','known':'complete literal source/control graph has a finite symbolic prospective upper envelope; no large bound integers evaluated','dependency_proof':'RF counters are Fraction-level rather than historical polynomial-product units, storage_events are not occupancy bytes, and all-worker spent/live/commitments plus layout_beta are absent. Symbolic upper bounds cannot authenticate those external quantities.'},
  'historical_allowances_are_current_caps':False,'dense_upper_bound_is_lower_bound':False,
  'algorithm_independent_impossibility_claimed':False,'physical_release':False,
  'reduction':'Accepted BI raw replacement preserves all32 global cohomology outputs via independently admitted representatives; it needs no comparison primitive54-cutoff, removes inner N14 work and implies neither pointwise source equality nor physical admission.'}

def actual_admission(*args,**kwargs):raise RuntimeError('no authenticated reconciled physical ledger or complete actual resource certificate')
