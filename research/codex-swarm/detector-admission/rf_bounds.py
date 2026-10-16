"""RF01-specific prospective bounds and actual INPUT CONSTANT metadata only.
Never imports or invokes field.py or constructs any actual polynomial.
"""
import hashlib,json,math,subprocess
from pathlib import Path
PIN='10810ee877fdaf291399198ad60d7dd0c316a42d'
MODEL='research/hm/null-operator-compiler/hm-pinned-model.json'
MODEL_SHA='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'

def model_input_bounds(repo):
 raw=subprocess.check_output(['git','show',PIN+':'+MODEL],cwd=repo,timeout=10)
 if hashlib.sha256(raw).hexdigest()!=MODEL_SHA:raise ValueError('model constants pin drift')
 model=json.loads(raw);rows=[]
 def walk(value,path):
  if type(value)is list:
   # Sparse polynomial leaves, including exact empty zero arrays.
   if not value or all(type(t)is list and len(t)==2 and type(t[0])is str for t in value):
    degree=0;l1=0
    for key,c in value:
     a=tuple(map(int,key.split(',')))
     if len(a)!=4 or min(a)<0 or type(c)is not int:raise ValueError('stored polynomial metadata')
     degree=max(degree,sum(a));l1+=abs(c)*math.prod(math.comb(4,i+1)**n for i,n in enumerate(a))
    rows.append({'path':path,'stored_terms':len(value),'finite_coordinate_degree':degree,
     'pulled_back_coefficient_L1_upper':l1,'numerator_bit_upper':max(1,l1.bit_length()),
     'denominator_bit_upper':1,'support_box_cardinality_upper':(degree+1)**4 if l1 else 0})
   else:
    for i,x in enumerate(value):walk(x,path+'/'+str(i))
  elif type(value)is dict:
   for k,x in value.items():
    if k!='pivot':walk(x,path+'/'+k)
 walk(model,'model')
 return {'schema':'actual-constant-input-bound-v1','pin':PIN,'path':MODEL,'sha256':MODEL_SHA,
  'method':'elementary e_k has L1 norm binom(4,k); sum |stored c_a| product binom(4,k)^a_k; no substitution/coefficients evaluated',
  'catalog_polynomial_leaves':len(rows),'max_finite_coordinate_degree':max(r['finite_coordinate_degree']for r in rows),
  'max_numerator_bit_upper':max(r['numerator_bit_upper']for r in rows),'max_support_box_cardinality_upper':max(r['support_box_cardinality_upper']for r in rows),
  'rows':rows,'actual_coefficients_evaluated':False}


def rf_operation_recurrences():
 return {'schema':'RF01-literal-algorithm-prospective-recurrences-v1',
  'coefficient_metric':'RF products counts EACH Fraction multiply AND divide, including normalization; not interchangeable with historical nonconstant-polynomial products',
  'poly':{'multiply':{'pair_visits':'m*n','Fraction_multiply_upper':'m*n','coefficient_add_upper':'m*n','output_coordinate_degree':'D_left+D_right','output_terms':'min(m*n, product_i(D_left_i+D_right_i+1))','coefficient_rational_bits':'k*(h_left+h_right)+ceil(log2(max(1,k)))+1, k=min(m,n)'},
   'add':{'coefficient_add_upper':'m+n','output_terms':'min(m+n, product_i(max(D_left_i,D_right_i)+1))','coefficient_rational_bits':'h_left+h_right+1'},
   'partial':{'Fraction_multiply_upper':'m','output_degree':'D_i-1 in differentiated coordinate, nonnegative','coefficient_bits':'h+ceil(log2(max(1,D_i)))+1'}},
  'rational':{'multiply':'two Poly products, then Rational normalization',
   'add':'zero/equal-denominator comparisons must be charged; otherwise three Poly products and one Poly sum, then normalization',
   'partial':'two Poly partials, three Poly products and one subtraction, then normalization',
   'normalize':'at most one Fraction reciprocal plus term_count(N)+term_count(D) Fraction scales; height at most h_N+h_D and 2*h_D respectively; constant denominator case included'},
  'element16':{'multiply':'at most256 basis pairs; each one Rational product plus up to4 curve-factor Rational products; retain all mask xor accumulation/constructor costs',
   'inverse':'supported only one y-basis component: at most4 curve-factor Rational products then reciprocal; arbitrary multicomponent inverse is unresolved/unsupported',
   'V':'for each at most16 components: one Rational.partial, one y-basis product and optional c*(3*x_i^2-1)/2 term; aggregate all moving-y derivative contributions'},
  'exact_final_division':{'precondition':'complete rational is Laurent after whole source/weight assembly; no support shortcut before exact remainder check',
   'degree_control':'For denominator coordinate degree D, choose lex weights (D+1)^3,(D+1)^2,D+1,1. Every divisor tail is strictly lower weighted degree than its lex lead. Starting weighted numerator bound K controls every intermediate exponent.',
   'iteration_upper':'product_i(floor(K/w_i)+1), since each leading monomial strictly decreases lex in that finite box',
   'height_recurrence':'h_(t+1) <= 2*h_t+2*h_den+5; hence h_t <= 2^t*(h_0+2*h_den+5)-(2*h_den+5)',
   'per_iteration':'one leading Fraction division when divisible, at most denominator_terms coefficient multiplications, full negate/add constructors and quotient/remainder updates; all work/quotient/remainder/temporary buffers coexist before release',
   'must_bind_to_actual_source':'nonzero denominator and Laurent/divisibility theorem plus degree/height bounds for the final actual numerator and denominator are still required'},
  'storage':'RF uses Python Fraction/dict/list/tuple, not AC packed-integer layout; interpreter/object/alias lifetimes need a separate authenticated byte metric and schedule',
  'complete_actual_source_graph_bound':False,'physical_release':False}

if __name__=='__main__':
 root=Path(__file__).resolve().parents[3]
 print(json.dumps({'input_bounds':model_input_bounds(root),'recurrences':rf_operation_recurrences()},indent=2))


def ceil_log2(n):return max(0,(max(1,n)-1).bit_length())

def rf_poly_bound(kind,left,right=None):
 """Executable RF01 Poly bound/counter recurrence, metadata only.
 Bounds are terms, uniform per-coordinate degree and coefficient Fraction bit height.
 The aggregate observed height also includes input/output exponent integers.
 Counts include constructor coefficient adds and denominator normalizations
 when composed below. No cost is compared to an unrelated physical metric.
 """
 for b in(left,right)if right is not None else(left,):
  if set(b)!={'terms','degree','bits'}or any(type(n)is not int or n<0 for n in b.values()):raise ValueError('finite exact RF bound')
 m,d,h=(left[k]for k in('terms','degree','bits'));n,e,g=(right[k]for k in('terms','degree','bits'))if right is not None else(0,0,0)
 if kind=='mul':
  K=m*n;degree=d+e;t=min(K,(degree+1)**4);k=min(m,n);height=k*(h+g)+ceil_log2(k)+1
  products=K;steps=5*K;storage=K+t+1
 elif kind=='add':
  K=m+n;degree=max(d,e);t=min(K,(degree+1)**4);height=h+g+1
  products=0;steps=3*K;storage=K+t+1
 elif kind=='partial':
  degree=d;t=m;height=h+ceil_log2(d)+1;products=m;steps=6*m;storage=2*m+1
 elif kind=='neg':
  degree=d;t=m;height=h+1;products=m;steps=4*m+1;storage=2*m+1
 else:raise ValueError('RF polynomial operation')
 return {'bound':{'terms':t,'degree':degree,'bits':height},'counter_upper':{'products':products,'steps':steps,'storage_events':storage},'observed_bit_height_upper':max(1,height,h,g,d.bit_length(),e.bit_length(),degree.bit_length())}


def rf_rational_bound(kind,left,right=None):
 """Literal unreduced Rational worst branch, including leading normalization."""
 costs={'products':0,'steps':0,'storage_events':0};peak=0
 def op(k,a,b=None):
  nonlocal peak
  x=rf_poly_bound(k,a,b)
  for key,value in x['counter_upper'].items():costs[key]+=value
  peak=max(peak,x['observed_bit_height_upper']);return x['bound']
 N,D=left['numerator'],left['denominator']
 if kind=='mul':
  U=op('mul',N,right['numerator']);V=op('mul',D,right['denominator'])
 elif kind=='add':
  U=op('add',op('mul',N,right['denominator']),op('mul',right['numerator'],D));V=op('mul',D,right['denominator'])
 elif kind=='partial':
  U=op('add',op('mul',op('partial',N),D),op('neg',op('mul',N,op('partial',D))));V=op('mul',D,D)
 else:raise ValueError('RF rational operation')
 # Even if a zero/equal/constant branch is cheaper, charge generic normalization.
 hD=V['bits'];U=dict(U,bits=U['bits']+hD);V=dict(V,bits=2*hD)
 costs['products']+=1+U['terms']+V['terms']
 costs['steps']+=1+(4*U['terms']+1)+(4*V['terms']+1)+3
 costs['storage_events']+=2*U['terms']+1+2*V['terms']+1+4
 return {'bound':{'numerator':U,'denominator':V},'counter_upper':costs,'observed_bit_height_upper':max(peak,U['bits'],V['bits']),
  'live_byte_bound':None,'scope':'generic worst branch; nonzero denominator is a separate algebraic premise'}


def actual_PI_dot_envelope():
 """One canonical15-contraction dot product inside(P_a I_b)^t.
 Scalar basis0 only, before physical D-frame products; no physical values.
 """
 p={'terms':2401,'degree':6,'bits':32} # <=16 input bits plus leading normalization
 term={'numerator':p,'denominator':p};acc={'numerator':{'terms':0,'degree':0,'bits':1},'denominator':{'terms':1,'degree':0,'bits':1}}
 counters={'products':0,'steps':0,'storage_events':0};peak=0
 for _ in range(15):
  prod=rf_rational_bound('mul',term,term);summed=rf_rational_bound('add',acc,prod['bound'])
  for item in(prod,summed):
   for key,c in item['counter_upper'].items():counters[key]+=c
   peak=max(peak,item['observed_bit_height_upper'])
  acc=summed['bound']
 # Scalar Element wrapping/constructor and starting zero: conservative overhead.
 counters['steps']+=100*31;counters['storage_events']+=100*31
 return {'schema':'actual-source-primitive-dot-envelope-v1','denotation':'one15-term dot product inside(P_a I_b)^t for arbitrary pinned carriers a,b','input':'normalized scalar-basis0 rational I/P entries; source model leaf bits<=16 so normalization bits<=32','matrix_contraction_length':15,'counter_upper':counters,'output_bound':acc,'observed_bit_height_upper':peak,'complete_g_physical_frame_included':False,'moving_frame_products_and_full_source_root_bound':None,'physical_coefficients_evaluated':False,'not_a_lower_bound':True}
