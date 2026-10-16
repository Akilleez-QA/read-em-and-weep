"""Finite symbolic envelope of the PINNED literal SR/RF route; no big evaluation."""
from pathlib import Path
import ast,json,hashlib
BASE=Path(__file__).resolve().parents[1]
SR_MARKER='f7f6d523c5f55af2b571cf8912e7473ac21f1a5949354d8bbb6d94eaddec794a'
def need(p,m):
 if not p:raise ValueError(m)
def op(name,*args):return {'op':name,'args':list(args)}
def build():
 path=BASE/'detector-realization';raw=(path/'producer-ready.json').read_bytes()
 need(hashlib.sha256(raw).hexdigest()==SR_MARKER,'frozen SR marker drift')
 marker=json.loads(raw);files=marker.get('files',marker.get('files_sha256',{}));need(bool(files),'missing SR producer hashes')
 for name,h in files.items():need(hashlib.sha256((path/name).read_bytes()).hexdigest()==h,'SR producer input drift')
 algorithm=json.loads((path/'algorithm.json').read_text());s=algorithm['static_execution_envelope']
 need(algorithm['request']['id']==30 and algorithm['literal_recurrence']['inner_N14_calls']==0,'raw route identity')
 need((s['non_RF_call_depth_upper'],s['simultaneously_active_non_RF_loop_depth_upper'])==(128,32),'source control envelope changed')
 # Count the actual caller ASTs, including the imported source/HPL code.
 names=['detector-realization/raw_engine.py','detector-realization/program.py','detector-realization/bindings.py','scalar-compiler/compiler.py','transport-binding/lift_schema.py','inserted-coefficients/interfaces.py']
 counts={n:sum(1 for _ in ast.walk(ast.parse((BASE/n).read_text())))for n in names}
 need(sum(counts.values())<=65536,'caller AST exceeds envelope')
 for n,count in s['caller_AST_nodes'].items():
  need(sum(1 for _ in ast.walk(ast.parse((path/n).read_text())))==count,'SR caller AST count drift')
 N=65536;d=128;l=32
 definitions={
  'C':op('pow',2672,5),
  'local_activation_bound':op('add',1,op('mul',N,op('pow',op('add','C',1),l))),
  'M':op('pow','local_activation_bound',d+2),
  'per_RF_exponent':op('pow',2,8388608),
  'B':{'op':'iterate','variable':'b','initial':1048576,'times':'M','body':op('pow',op('add','b',2),'per_RF_exponent')},
  'weighted_degree_K':op('mul',4,'B',op('pow',op('add','B',1),3)),
  'division_iterations_T':op('pow',op('add','weighted_degree_K',1),4),
  'terminal_height_H':op('mul',op('pow',2,'division_iterations_T'),op('add',op('mul',3,'B'),5)),
  'RF_before_terminal':op('mul',op('add','M',1),op('pow',op('add','B',2),16)),
  'RF_terminal':op('mul',100,op('pow',op('add','division_iterations_T',1),2)),
  'RF_total':op('add','RF_before_terminal','RF_terminal'),
  'integer_binomial_products':op('mul',2671,'M'),
  'integer_binomial_exact_divisions':op('mul',2671,'M'),
  'integer_binomial_height_bits':8014,
  'retain_all_abstract_cells':op('mul',op('add','M','RF_terminal',1),op('pow',op('add','division_iterations_T','terminal_height_H','weighted_degree_K','B',2),16)),
  'conditional_route_bytes':op('mul',op('add','layout_beta',1),'retain_all_abstract_cells')}
 return {'schema':'SR01-RF01-complete-symbolic-upper-envelope-v1','route_id':algorithm['route_id'],'request_id':30,
  'SR_marker_sha256':SR_MARKER,'caller_AST_nodes':counts,'caller_AST_node_upper':N,
  'source_control_premises':s,'source_control_proof_scope':'literal raw call graph/loop audit; producer claims are not execution capabilities; independent SR denotation review remains external',
  'definitions':definitions,'bound_units':{'RF_total':'upper for EACH RF Fraction-products/steps/storage_events counter; not old nonconstant polynomial products','B':'preterminal polynomial coordinate degrees, term counts and Fraction numerator/denominator bit heights','terminal_height_H':'terminal intermediate Fraction bit height upper','retain_all_abstract_cells':'conservative logical payload/reference cells with all objects retained','conditional_route_bytes':'requires authoritative layout_beta header/allocator/representation byte envelope'},
  'event_schedule':'Allocate outputs and every workspace before any release; conservatively retain all route objects until terminal extraction/output exists. No route frees are needed for this upper bound.',
  'actual_integer_values_materialized':False,'source_coefficients_evaluated':False,'layout_beta':None,
  'current_global_ledger':None,'native_machine_bitcost_metric':None,'physical_admission':False,'not_a_lower_bound':True,
  'remaining_dependencies':['independent source denotation/control-envelope acceptance','authoritative RF/native-integer versus cap metric reconciliation','layout_beta and current all-worker spent/reservation/live-allocation ledger','physical execution release']}
if __name__=='__main__':print(json.dumps(build(),indent=2))
