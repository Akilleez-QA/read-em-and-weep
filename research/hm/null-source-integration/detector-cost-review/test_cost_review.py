"""AC01 independent cost controls at d37436ee72fcb8bc93ce9b1ef7ff4febeed0c789.

Use: python -B test_cost_review.py --source-root PATH_TO_REPOSITORY
Only source text, integer/exponent metadata, and tiny invented polynomials run.
The imported SR implementation, physical catalog arithmetic, fibers, source jets,
and coefficient extraction are never executed. Mutation controls use copies.
Known-defect controls pass by demonstrating the documented mismatch.
"""
import argparse
import ast
import hashlib
import importlib.util
import itertools
import json
import math
from pathlib import Path
import random
import shutil
import sys
import tempfile
import unittest
from fractions import Fraction as Q

parser=argparse.ArgumentParser()
parser.add_argument('--source-root',type=Path,required=True)
args,rest=parser.parse_known_args()
ROOT=args.source_root.resolve()
BASE=ROOT/'research/codex-swarm'
HERE=BASE/'detector-admission'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

RF=load('ac01_cost_review_RF',BASE/'exact-curve-field/field.py')
RB=load('ac01_cost_review_RB',HERE/'rf_bounds.py')
WE=load('ac01_cost_review_WE',HERE/'whole_envelope.py')

def read(path):return json.loads(path.read_text())
def bit(q):return max(abs(q.numerator).bit_length(),q.denominator.bit_length())
def pb(p):
    return dict(terms=len(p.terms),degree=max([0]+[max(e)for e,c in p.terms]),
                bits=max([1]+[bit(c)for e,c in p.terms]))
def rb(r):return dict(numerator=pb(r.numerator),denominator=pb(r.denominator))

class CostReview(unittest.TestCase):
    def test_input_constant_metadata(self):
        raw=(ROOT/'research/hm/null-operator-compiler/hm-pinned-model.json').read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926')
        model=json.loads(raw);rows=[]
        def walk(v,path):
            if type(v)is list:
                if not v or all(type(t)is list and len(t)==2 and type(t[0])is str for t in v):
                    degree=0;mass=0
                    for key,c in v:
                        e=tuple(map(int,key.split(',')))
                        self.assertEqual(len(e),4);self.assertGreaterEqual(min(e),0)
                        degree=max(degree,sum(e));mass+=abs(c)*math.prod(w**a for w,a in zip((4,6,4,1),e))
                    rows.append(dict(path=path,stored_terms=len(v),finite_coordinate_degree=degree,
                        pulled_back_coefficient_L1_upper=mass,numerator_bit_upper=max(1,mass.bit_length()),
                        denominator_bit_upper=1,support_box_cardinality_upper=(degree+1)**4 if mass else 0))
                else:
                    for i,x in enumerate(v):walk(x,path+'/'+str(i))
            elif type(v)is dict:
                for k,x in v.items():
                    if k!='pivot':walk(x,path+'/'+k)
        walk(model,'model')
        self.assertEqual(rows,read(HERE/'actual-input-bounds.json')['rows'])
        self.assertEqual(len(rows),1973)
        self.assertEqual(tuple(max(r[k]for r in rows)for k in ('finite_coordinate_degree','numerator_bit_upper','support_box_cardinality_upper')),(6,16,2401))

    def test_relevant_pinned_source_bytes(self):
        pins=read(HERE/'source-pins.json')['workspace_inputs']
        audited=('exact-curve-field/field.py','detector-realization/producer-ready.json',
          'detector-realization/algorithm.json','detector-realization/raw_engine.py',
          'detector-realization/program.py','detector-realization/bindings.py',
          'scalar-compiler/compiler.py','transport-binding/lift_schema.py')
        for row in pins:
            if row['path']in audited:
                self.assertEqual(hashlib.sha256((BASE/row['path']).read_bytes()).hexdigest(),row['sha256'])
        sr=read(BASE/'detector-realization/source-pins.json')
        ip=next(r for r in sr['local_dependencies']if r['path']=='inserted-coefficients/interfaces.py')
        self.assertEqual(hashlib.sha256((BASE/ip['path']).read_bytes()).hexdigest(),ip['sha256'])

    def test_complete_symbolic_DAG_replay(self):
        result=WE.build()
        self.assertEqual(result,read(HERE/'whole-route-envelope.json'))
        self.assertEqual(sum(result['caller_AST_nodes'].values()),12804)
        defs=result['definitions']
        self.assertEqual(defs['B']['times'],'M')
        self.assertEqual(defs['B']['initial'],2**20)
        self.assertEqual(defs['RF_total'],WE.op('add','RF_before_terminal','RF_terminal'))
        for key in ('layout_beta','current_global_ledger','native_machine_bitcost_metric'):
            self.assertIsNone(result[key])
        self.assertFalse(result['physical_admission'])
        self.assertTrue(result['not_a_lower_bound'])

    def test_uniform_compound_majorant(self):
        for b in (2**20,2**21,2**22):
            p=dict(terms=b,degree=b,bits=b);r=dict(numerator=p,denominator=p)
            for kind in ('add','mul','partial'):
                q=RB.rf_rational_bound(kind,r,r if kind!='partial'else None)
                values=[q['observed_bit_height_upper'],*q['counter_upper'].values()]
                values.extend(v for side in q['bound'].values()for v in side.values())
                self.assertLessEqual(max(values),(b+2)**16)
        self.assertLess(5*2**20,8388608)
        self.assertEqual(3*2671+1,8014)
        self.assertLess(5**2671*2671,2**8014)

    def test_tiny_artificial_rational_bounds(self):
        rng=random.Random(573);checks=0
        for case in range(100):
            ex=RF.Execution()
            def p():
                return ex.poly((tuple(rng.randrange(3)for _ in range(4)),
                    Q(rng.choice((-5,-3,-1,1,2,3,5)),rng.choice((1,2,3,5,7))))
                    for _ in range(rng.randrange(1,5)))
            a=ex.rational(p(),p());b=ex.rational(p(),p())
            for kind in ('add','mul','partial'):
                pred=RB.rf_rational_bound(kind,rb(a),rb(b)if kind!='partial'else None)
                before=dict(ex.counts)
                out=a+b if kind=='add'else a*b if kind=='mul'else a.partial(0)
                for key,limit in pred['counter_upper'].items():
                    checks+=1;self.assertLessEqual(ex.counts[key]-before[key],limit)
                for side in ('numerator','denominator'):
                    for key,value in pb(getattr(out,side)).items():
                        checks+=1;self.assertLessEqual(value,pred['bound'][side][key])
        self.assertEqual(checks,2700)

    def test_known_exponent_observation_gap(self):
        for kind,expected in (('add',3),('mul',3),('neg',2)):
            ex=RF.Execution();p=ex.poly([((1024,0,0,0),1)]);q=ex.poly([((0,0,0,0),1)])
            pred=RB.rf_poly_bound(kind,pb(p),pb(q)if kind!='neg'else None)
            out=p+q if kind=='add'else p*q if kind=='mul'else -p
            self.assertEqual(pred['observed_bit_height_upper'],expected)
            self.assertEqual(ex.counts['bit_height'],11)
            self.assertGreater(ex.counts['bit_height'],pred['observed_bit_height_upper'])
            self.assertLessEqual(max(max(e)for e,c in out.terms),2**20)

    def test_weighted_lex_bound(self):
        for D in (0,1,2,3):
            w=((D+1)**3,(D+1)**2,D+1,1)
            box=list(itertools.product(range(D+1),repeat=4))
            self.assertEqual(sorted(box,key=lambda e:sum(a*b for a,b in zip(e,w))),box)
        ex=RF.Execution();n=ex.poly([((2,0,0,0),1),((0,4,0,0),-1)])
        d=ex.poly([((1,0,0,0),1),((0,2,0,0),-1)])
        q,r=n.divide(d)
        self.assertFalse(r.terms)
        self.assertEqual(dict(q.terms),{(1,0,0,0):Q(1),(0,2,0,0):Q(1)})

    def test_known_standalone_transitive_pin_gap(self):
        baseline=WE.build()
        mutations=(('inserted-coefficients/interfaces.py','sign=(-1)**sum','sign=(+1)**sum'),
          ('scalar-compiler/compiler.py','for perm in itertools.permutations(range(4)):',
           'for perm in itertools.permutations(range(1000000)):'))
        for i,(path,old,new)in enumerate(mutations):
            with tempfile.TemporaryDirectory()as temp:
                copy=Path(temp)/'swarm';shutil.copytree(BASE,copy)
                target=copy/path;raw=target.read_text();self.assertIn(old,raw)
                target.write_text(raw.replace(old,new))
                # Only whole_envelope is imported; mutated source is AST-parsed.
                module=load('ac01_cost_mutation_'+str(i),copy/'detector-admission/whole_envelope.py')
                self.assertEqual(module.build(),baseline)
        direct={r['path']for r in read(HERE/'source-pins.json')['workspace_inputs']}
        self.assertNotIn('inserted-coefficients/interfaces.py',direct)

    def test_blocked_unknowns_remain_explicit(self):
        b=read(HERE/'blocked-route.json')
        self.assertEqual(b['status'],'BLOCKED_ROUTE')
        self.assertIsNone(b['authoritative_reconciled_ledger'])
        self.assertIsNone(b['aggregate_peak_bytes'])
        self.assertIsNone(b['layout_byte_factor'])
        for key in ('historical_allowances_are_current_caps','dense_upper_bound_is_lower_bound',
                    'algorithm_independent_impossibility_claimed','physical_release'):
            self.assertFalse(b[key])
        source=ast.parse((HERE/'certifier.py').read_text())
        f=next(n for n in source.body if isinstance(n,ast.FunctionDef)and n.name=='actual_admission')
        self.assertIsInstance(f.body[0],ast.Raise)

if __name__=='__main__':unittest.main(argv=[sys.argv[0],*rest],verbosity=2)
