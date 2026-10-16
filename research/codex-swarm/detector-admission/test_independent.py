"""AC-R independent prospective controls. Direct entry supervises four children.
Only fictional RF arithmetic and static catalog metadata; no Git commands.
"""
import ast
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
import unittest
import urllib.request

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = BASE.parents[1]
MARKER = '1e3bbefde892b3131986dc579ac592dfcbd6c2dab2253668e69396d199bc76be'
LIMIT = 768 * 1024 * 1024
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))

def sha(raw): return hashlib.sha256(raw).hexdigest()
def require(ok, message):
    if not ok: raise ValueError(message)
def read_json(p): return json.loads(p.read_bytes())
def snapshot():
    raw = (HERE/'producer-ready.json').read_bytes()
    require(sha(raw) == MARKER, 'AC marker changed')
    files = json.loads(raw)['files']
    require(len(files) == 15, 'AC inventory changed')
    for name, digest in files.items():
        require(Path(name).name == name and sha((HERE/name).read_bytes()) == digest, 'AC drift: '+name)
    return dict(files, **{'producer-ready.json':sha(raw)})
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

snapshot()
import certifier as AC
import rf_bounds as RB
import whole_envelope as WE
RF = load('acr_fictional_rf', BASE/'exact-curve-field/field.py')

# Immutable sources are read as bytes, never through Git or executable builders.
def pinned_bytes(row):
    p = ROOT/row['path']
    raw = p.read_bytes() if p.is_file() else b''
    if sha(raw) != row['sha256']:
        require('commit' in row, 'local pin drift '+str(p))
        url = 'https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'+row['commit']+'/'+row['path']
        raw = urllib.request.urlopen(url, timeout=8).read()
    require(sha(raw) == row['sha256'], 'content pin drift')
    if 'bytes' in row: require(len(raw) == row['bytes'], 'length pin drift')
    if 'git_blob' in row:
        require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == row['git_blob'], 'blob pin drift')
    return raw

def counts(**kw): return dict(dict.fromkeys(AC.A06.COUNTERS, 0), **kw)
def fiction():
    a={'terms':1,'height':5,'exponent_abs':3}; b={'terms':3,'height':7,'exponent_abs':2}
    mul=AC.operation(a,b,'mul'); add=AC.operation(mul['bound'],a,'add')
    algorithm={'evidence':'explicit-artificial-integer-polynomials','inputs':{'a':a,'b':b},
      'steps':[{'id':'p','kind':'mul','left':'a','right':'b','output':'c'},
               {'id':'s','kind':'add','left':'c','right':'a','output':'d'}], 'outputs':['d']}
    allocations=[]
    for aid,n,initial,last,r in [('a',82,True,3,None),('b',182,True,1,None),('c',182,False,3,'ours'),('d',232,False,3,'ours'),('foreign',37,True,-1,'theirs')]:
        allocations.append(dict(id=aid,owner='B' if aid=='foreign' else 'A',bytes=n,initial=initial,last_use=last,reservation=r,binding='synthetic'))
    ledger=dict(schema='a06-global-schedule-v1',evidence='synthetic-only',ledger_id='ACR-fiction-two-stage',revision=17,global_complete=True,source_pin='synthetic:no-physical-source',
      caps=dict(counts=counts(products=9,coefficient_multiplications=20,additions=30),bytes=1060,metric='synthetic-live-plus-workspace-bytes'),
      spent=counts(products=4,coefficient_multiplications=2,additions=3),
      reservations=[dict(id='ours',owner='A',remaining=counts(products=2,coefficient_multiplications=3,additions=7),bytes=0,first_event=0,last_event=3,authorization='synthetic'),
                    dict(id='theirs',owner='B',remaining=counts(products=3),bytes=100,first_event=0,last_event=3,authorization='synthetic')],
      allocations=allocations,
      operations=[dict(id=oid,owner='A',inputs=ins,outputs=[out],counts=cost['counts'],workspace=cost['workspace'],reservation='ours',source_binding='synthetic') for oid,ins,out,cost in [('p',['a','b'],'c',mul),('s',['c','a'],'d',add)]],
      events=[dict(begin=['p'],end=[],free=[]),dict(begin=[],end=['p'],free=['b']),dict(begin=['s'],end=[],free=[]),dict(begin=[],end=['s'],free=['a','c'])])
    return algorithm,ledger

def poly(ex, rows): return ex.poly((tuple(e), Q(c)) for e,c in rows)
def bit(q): return max(abs(q.numerator).bit_length(), q.denominator.bit_length())
def reference_divide(n, d):
    """Independent tiny dictionary division with per-step support/height log."""
    work=dict(n); quotient={}; remainder={}; log=[]; de=max(d); dc=d[de]
    while work:
        before=max([1]+[bit(q) for q in work.values()]+[bit(q) for q in quotient.values()]+[bit(q) for q in remainder.values()])
        e=max(work); c=work[e]
        if all(a>=b for a,b in zip(e,de)):
            f=tuple(a-b for a,b in zip(e,de)); q=c/dc
            quotient[f]=quotient.get(f,Q(0))+q
            for g,z in d.items():
                v=tuple(a+b for a,b in zip(f,g)); work[v]=work.get(v,Q(0))-q*z
                if not work[v]:del work[v]
        else: remainder[e]=work.pop(e)
        support=set(work)|set(quotient)|set(remainder)
        after=max([1]+[bit(q) for p in (work,quotient,remainder) for q in p.values()])
        log.append((e,before,after,support))
    return quotient,remainder,log

class Independent(unittest.TestCase):
    def test_01_frozen_inventory_and_all_dependency_bytes(self):
        snapshot(); ac=read_json(HERE/'source-pins.json'); sr=read_json(BASE/'detector-realization/source-pins.json'); bi=read_json(BASE/'source-boundary-analysis/source-pins.json')
        for directory in ('detector-realization','exact-curve-field'):
            marker=read_json(BASE/directory/'producer-ready.json')
            for name,digest in marker.get('files',marker.get('files_sha256',{})).items():
                self.assertEqual(sha((BASE/directory/name).read_bytes()),digest)
        for row in ac['workspace_inputs']+sr['local_dependencies']:
            self.assertEqual(sha((BASE/row['path']).read_bytes()),row['sha256'])
        for row in bi['workspace_dependencies']: pinned_bytes(row)
        immutable=sr['git_objects']+[ac['immutable_outer_formula_source']]+bi['immutable_dependencies']
        # Deduplicate byte identities, preserving every record's identity check.
        cache={}
        for row in immutable:
            key=(row['path'],row['sha256'])
            if key not in cache:cache[key]=pinned_bytes(row)
            raw=cache[key];self.assertEqual(sha(raw),row['sha256'])
            if 'git_blob' in row:self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),row['git_blob'])
        private=ac['A06_review_read'];p=Path(private['read_path'])
        if p.is_file(): self.assertEqual(sha(p.read_bytes()),private['sha256'])
        self.assertFalse(private['private_artifact_required_for_replay'])

    def test_02_exact_historical_payload_scope(self):
        evidence=read_json(HERE/'ledger-evidence.json');scope=evidence['searched_scope']
        p=Path('/tmp/ac01-pr1-ledger-read.json')
        # The historical receipt is optional for portable replay, never replaced
        # by today's mutable PR contents or silently treated as authenticated.
        if p.is_file():
            raw=p.read_bytes();self.assertEqual(sha(raw),scope['readback_payload_sha256']);data=json.loads(raw)
            self.assertEqual(sha(data['body'].encode()),scope['issue_body_sha256'])
            self.assertEqual(len(data['comments']),326)
            byurl={c['url']:c for c in data['comments']}
            self.assertEqual(data['comments'][0]['url'],scope['first_returned_comment'])
            self.assertEqual(data['comments'][-1]['url'],scope['last_returned_comment'])
            for row in evidence['published_evidence']:
                body=byurl[row['url']]['body'];self.assertEqual(sha(body.encode()),row['body_sha256'])
                for line in row['lines']:self.assertIn(line,body)
        self.assertTrue(scope['last_returned_comment'].endswith('6213072026'))
        self.assertIsNone(evidence['current_reconciled_state']);self.assertFalse(evidence['release'])
        h=evidence['historical_held_allowances'];self.assertEqual((h['nonconstant_products'],h['unallocated_bytes'],h['protected_reserve_bytes']),(149,294117,2097152))
        self.assertFalse(h['current_authority']);self.assertFalse(h['reserve_addable_to_scratch'])

    def test_03_independent_catalog_metadata_only(self):
        sr=read_json(BASE/'detector-realization/source-pins.json');row=next(r for r in sr['git_objects'] if r['path'].endswith('hm-pinned-model.json'))
        model=json.loads(pinned_bytes(row));rows=[]
        def walk(v,path):
            if isinstance(v,list):
                if not v or all(isinstance(t,list) and len(t)==2 and isinstance(t[0],str) for t in v):
                    degree=0;mass=0
                    for key,c in v:
                        e=tuple(map(int,key.split(',')));require(len(e)==4 and min(e)>=0 and type(c)is int,'catalog metadata')
                        degree=max(degree,sum(e));factor=1
                        for a,w in zip(e,(4,6,4,1)):factor*=w**a
                        mass+=abs(c)*factor
                    rows.append(dict(path=path,stored_terms=len(v),finite_coordinate_degree=degree,pulled_back_coefficient_L1_upper=mass,numerator_bit_upper=max(1,mass.bit_length()),denominator_bit_upper=1,support_box_cardinality_upper=(degree+1)**4 if mass else 0))
                else:
                    for i,x in enumerate(v):walk(x,path+'/'+str(i))
            elif isinstance(v,dict):
                for k,x in v.items():
                    if k!='pivot':walk(x,path+'/'+k)
        walk(model,'model');published=read_json(HERE/'actual-input-bounds.json')
        self.assertEqual(rows,published['rows']);self.assertEqual(len(rows),1973)
        self.assertEqual((max(r['finite_coordinate_degree'] for r in rows),max(r['numerator_bit_upper'] for r in rows),max(r['support_box_cardinality_upper'] for r in rows)),(6,16,2401))
        seed=read_json(HERE/'actual-seed-envelope.json');self.assertEqual(seed['common_seed_envelope'],dict(terms=2401,degree=6,bits=8014))
        self.assertEqual(3*2671+1,8014)
        # 8014 also covers chained intermediate integers: multinomial prefixes
        # <=5^2671; a pending binomial recurrence product adds <=12 bits.
        self.assertLess(5**2671*2671,2**8014)

    def test_04_symbolic_DAG_and_activation_majorant(self):
        envelope=WE.build();self.assertEqual(envelope,read_json(HERE/'whole-route-envelope.json'))
        self.assertEqual(sum(envelope['caller_AST_nodes'].values()),12804)
        d=envelope['definitions'];self.assertEqual(d['M'],WE.op('pow','local_activation_bound',130))
        self.assertEqual(d['B']['initial'],2**20);self.assertEqual(d['B']['times'],'M')
        self.assertEqual(d['per_RF_exponent'],WE.op('pow',2,8388608))
        self.assertLess(5*2**20,8388608) # 32^(2^20) fits F's exponent.
        for b in (2**20,2**21):
            bound=dict(terms=b,degree=b,bits=b);rat=dict(numerator=bound,denominator=bound)
            for kind in ('mul','add','partial'):
                r=RB.rf_rational_bound(kind,rat,rat if kind!='partial' else None)
                self.assertLessEqual(max([r['observed_bit_height_upper']]+list(r['counter_upper'].values())+[x for p in r['bound'].values() for x in p.values()]),(b+2)**16)
        for s in range(1,6):
            for depth in range(5): self.assertLessEqual(s*sum(s**i for i in range(depth+1)),(s+1)**(depth+2))
        self.assertEqual(d['RF_total'],WE.op('add','RF_before_terminal','RF_terminal'))
        self.assertEqual(d['retain_all_abstract_cells'],WE.op('mul',WE.op('add','M','RF_terminal',1),WE.op('pow',WE.op('add','division_iterations_T','terminal_height_H','weighted_degree_K','B',2),16)))
        for key in ('layout_beta','current_global_ledger','native_machine_bitcost_metric'):self.assertIsNone(envelope[key])

    def test_05_guard_and_canonical_control_AST(self):
        raw=ast.parse((BASE/'detector-realization/raw_engine.py').read_text());program=ast.parse((BASE/'detector-realization/program.py').read_text())
        def functions(tree):return {n.name:n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
        rr,pp=functions(raw),functions(program)
        for table,names in ((rr,('require_aggregate_admission','_build_body','__init__')),(pp,('potential_owners','weighted_assignment','_actual_body','actual_route30'))):
            for name in names:
                n=table[name];body=n.body[1:] if isinstance(n.body[0],ast.Expr) and isinstance(n.body[0].value,ast.Constant) else n.body
                if name=='require_aggregate_admission':self.assertIsInstance(body[0],ast.Raise)
                elif name!='__init__': self.assertEqual(ast.unparse(body[0]),'require_aggregate_admission()')
        physical=next(n for n in raw.body if isinstance(n,ast.ClassDef) and n.name=='PhysicalModel')
        init=next(n for n in physical.body if isinstance(n,ast.FunctionDef) and n.name=='__init__')
        self.assertEqual(ast.unparse(init.body[0]),'require_aggregate_admission()')
        source=ast.unparse(rr['source_and_lift']);self.assertIn('source = RawSource(M)',source);self.assertIn('source.residual',source)
        body=ast.unparse(pp['_actual_body']);self.assertIn('total = total +',body);self.assertIn('stripped.laurent_coefficient(EXPONENT)',body)
        self.assertNotIn('laurent_coefficient',ast.unparse(pp['weighted_assignment']))
        for n in (pp['first_hit'],pp['outer_weight']):self.assertIn('require_aggregate_admission()',ast.unparse(n))
        self.assertNotIn('math.comb',ast.unparse(program))
        self.assertIn('out * (n - j + 1) // j',ast.unparse(pp['binomial']))
        # Do not import SR, enumerate its fibers, or invoke any guarded body.

    def test_06_two_stage_global_storage_certificate(self):
        a,l=fiction();saved=copy.deepcopy(l);r=AC.certify_synthetic(a,l)
        self.assertEqual(l,saved);self.assertEqual(r['output_bounds']['d'],dict(terms=4,height=40,exponent_abs=5))
        s=r['schedule'];self.assertEqual(s['peak_charged_bytes'],1060)
        self.assertEqual(s['spent_after']['products'],5);self.assertEqual(s['remaining_reservations']['ours']['products'],1)
        self.assertEqual(s['remaining_reservations']['theirs']['products'],3);self.assertEqual(s['live_after'],['d','foreign'])
        self.assertTrue(any(t['unbacked_commitments']==63 for t in s['trace']))
        self.assertFalse(r['physical_release'])

    def test_07_negative_global_lifetimes_counts_unknowns(self):
        def cap(l):l['caps']['bytes']=1059
        def countcap(l):l['caps']['counts']['products']=8
        def free(l):l['events'][2]['free']=['c']
        def early(l):l['events'][1]['begin']=['s'];l['events'][2]['begin']=[]
        def drop(l):l['operations'][1]['workspace']=0
        def retained(l):l['events'][3]['free'].append('d')
        def unknown(l):l['spent']['products']=None
        def dup(l):l['allocations'].append(copy.deepcopy(l['allocations'][0]))
        def incomplete(l):l['global_complete']=False
        def physical(l):l['evidence']='physical'
        for mutate in (cap,countcap,free,early,drop,retained,unknown,dup,incomplete,physical):
            a,l=fiction();mutate(l)
            with self.subTest(mutate=mutate.__name__),self.assertRaises(ValueError):AC.certify_synthetic(a,l)
        a,l=fiction();a['inputs']['a']['height']=None
        with self.assertRaises(ValueError):AC.certify_synthetic(a,l)
        with self.assertRaises(ValueError):AC.packed_bytes(1,1,2**63)
        with self.assertRaises(RuntimeError):AC.actual_admission()

    def test_08_fraction_normalization_and_rational_bounds(self):
        ex=RF.Execution();z=(0,0,0,0);x=(1,0,0,0);y=(0,1,0,0)
        a=ex.rational(poly(ex,[(x,Q(5,7)),(z,Q(-2,3))]),poly(ex,[(y,Q(3,11)),(z,Q(7,13))]))
        b=ex.rational(poly(ex,[(y,Q(-4,5)),(z,Q(3,17))]),poly(ex,[(x,Q(9,7)),(z,Q(2,19))]))
        def bounds(r):return {k:dict(terms=len(p.terms),degree=max([0]+[max(e) for e,c in p.terms]),bits=max([1]+[bit(c) for e,c in p.terms])) for k,p in [('numerator',r.numerator),('denominator',r.denominator)]}
        for kind in ('mul','add','partial'):
            prediction=RB.rf_rational_bound(kind,bounds(a),bounds(b) if kind!='partial' else None);start=dict(ex.counts)
            value=a*b if kind=='mul' else a+b if kind=='add' else a.partial(0)
            for key,limit in prediction['counter_upper'].items():self.assertLessEqual(ex.counts[key]-start[key],limit)
            for side,p in [('numerator',value.numerator),('denominator',value.denominator)]:
                for e,c in p.terms:self.assertLessEqual(bit(c),prediction['bound'][side]['bits'])
            self.assertLessEqual(ex.counts['bit_height'],prediction['observed_bit_height_upper'])
        self.assertEqual(a.denominator.terms[-1][1],1)

    def test_09_observed_exponent_height_counterexample(self):
        # Known producer auxiliary defect, positively demonstrated in both modes.
        ex=RF.Execution();p=poly(ex,[((1024,0,0,0),1)])
        predicted=RB.rf_poly_bound('add',dict(terms=1,degree=1024,bits=1),dict(terms=0,degree=0,bits=1))
        result=p+ex.poly()
        self.assertEqual(result.terms,p.terms)
        self.assertEqual(predicted['observed_bit_height_upper'],3)
        self.assertEqual(ex.counts['bit_height'],11)
        self.assertGreater(ex.counts['bit_height'],predicted['observed_bit_height_upper'])
        # This does not refute the common B envelope, which bounds degree too.
        self.assertLess(11,2**20)

    def test_10_all_sixteen_basis_pairs_and_moving_terms(self):
        ex=RF.Execution();a=ex.element((m,ex.rational(Q(m+1,17))) for m in range(16));b=ex.element((m,ex.rational(Q(2*m+1,19))) for m in range(16))
        before=dict(ex.counts);c=a*b;self.assertEqual(ex.counts['basis_products']-before['basis_products'],256)
        self.assertLessEqual(len(c.terms),16)
        self.assertNotEqual(ex.y(0).V(0),ex.scalar(0))
        with self.assertRaises(RF.UnsupportedInverse):a.inverse()
        self.assertLess(ex.counts['products'],2**20)

    def test_11_weighted_lex_division_height_and_degree_growth(self):
        ex=RF.Execution();n={(2,0,0,0):Q(3,7),(0,4,0,0):Q(-3,7)};d={(1,0,0,0):Q(5,11),(0,2,0,0):Q(-5,11)}
        q,r,trace=reference_divide(n,d);got,rem=poly(ex,n.items()).divide(poly(ex,d.items()))
        self.assertEqual(dict(got.terms),q);self.assertEqual(dict(rem.terms),r);self.assertFalse(r)
        D=2;w=((D+1)**3,(D+1)**2,D+1,1);K=54;T=(K+1)**4;hd=max(map(bit,d.values()))
        self.assertLessEqual(len(trace),T)
        for i,(lead,h0,h1,support) in enumerate(trace):
            self.assertLessEqual(h1,2*h0+2*hd+5)
            for e in support:self.assertLessEqual(sum(a*b for a,b in zip(e,w)),K)
            if i:self.assertGreater(trace[i-1][0],lead)
        self.assertTrue(any(e[1]>2 for _,_,_,support in trace for e in support))
        # Every lex tail in a divisor box has smaller weighted degree.
        for D in (1,2,3):
            w=((D+1)**3,(D+1)**2,D+1,1);box=list(itertools.product(range(D+1),repeat=4))
            ordered=sorted(box,key=lambda e:sum(a*b for a,b in zip(e,w)))
            self.assertEqual(ordered,box)

    def test_12_whole_sum_before_division_and_negative_remainder(self):
        ex=RF.Execution();one=ex.constant(1);x=ex.xpoly(0);den=one+x
        a=ex.rational(one,den);b=ex.rational(x,den)
        with self.assertRaises(RF.NotLaurentPolynomial):a.laurent_coefficient((777,0,0,0))
        self.assertEqual((a+b).laurent_coefficient((0,0,0,0)),1)
        self.assertEqual((a+b).laurent_coefficient((777,0,0,0)),0)
        # A monomial factor is extracted without turning non-Laurent into zero.
        r=ex.rational(one,x*x);self.assertEqual(r.laurent_coefficient((-2,0,0,0)),1)

    def test_13_scoped_structural_alphabets_and_blocked_status(self):
        candidate=read_json(HERE/'candidate-route.json');r=candidate['structural_weight_zero_reductions']
        self.assertEqual(24*6**5*2**10,191102976);self.assertEqual(24*2*3*4*5*2*2**10,5898240)
        self.assertEqual(r['carrier_alphabet_sizes_by_popcount'],[2,3,4,5,2])
        blocked=AC.actual_route_certificate();self.assertEqual(blocked,read_json(HERE/'blocked-route.json'))
        self.assertEqual(blocked['status'],'BLOCKED_ROUTE');self.assertIsNone(blocked['aggregate_peak_bytes'])
        for key in ('historical_allowances_are_current_caps','dense_upper_bound_is_lower_bound','algorithm_independent_impossibility_claimed','physical_release'):self.assertFalse(blocked[key])


def limits():
    resource.setrlimit(resource.RLIMIT_AS,(LIMIT,LIMIT));resource.setrlimit(resource.RLIMIT_CPU,(59,59))

def main():
    if '--child' in sys.argv:
        limits();before=snapshot();suite=unittest.defaultTestLoader.loadTestsFromTestCase(Independent)
        result=unittest.TextTestRunner(verbosity=2).run(suite)
        require(snapshot()==before,'producer changed during child')
        raise SystemExit(0 if result.wasSuccessful() else 1)
    before=snapshot()
    for label,optimized,producer in [('independent-normal',False,False),('independent-O',True,False),('producer-normal',False,True),('producer-O',True,True)]:
        command=[sys.executable,'-B']+(['-O'] if optimized else [])
        command+=['-m','unittest','discover','-s',str(HERE),'-p','test_certifier.py','-v'] if producer else [str(Path(__file__).resolve()),'--child']
        start=time.monotonic();done=subprocess.run(command,timeout=60,preexec_fn=limits,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
        require(snapshot()==before,'producer changed during '+label)
        print(json.dumps(dict(suite=label,returncode=done.returncode,wall_seconds=round(time.monotonic()-start,3),address_space_bytes=LIMIT,cpu_seconds=59,wall_limit_seconds=60,marker=MARKER)),flush=True)
        require(done.returncode==0,'failed '+label)
    print('AC-R: independent 13 + separate producer 10 cases per mode; frozen producer unchanged.',flush=True)

if __name__=='__main__':main()
