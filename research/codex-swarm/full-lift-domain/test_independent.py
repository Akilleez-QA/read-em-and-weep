"""Independent bounded, coefficient-free JC01 controls. Run this file directly.

No git, network, actual constructors, coefficients, jets or fibers are executed.
"""
import resource
resource.setrlimit(resource.RLIMIT_AS, (768*1024*1024, 768*1024*1024))
resource.setrlimit(resource.RLIMIT_CPU, (59, 59))
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import sys
import time
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import lift as L

MARKER = '88cd12c2a2a90e5300966adc6b01999d6f65559e2b7a8c8d5c36b0946f323ae9'
PINS = '515c3d1a21645741aab58cf404228263ebc12128c9636c0df1fe0f9afd74d82a'

def digest(b): return hashlib.sha256(b).hexdigest()
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

# Separate elementary exact matrix arithmetic, including the graded operators.
def mat(n, m, entries):
    return tuple(tuple(F(entries.get((i,j), 0)) for j in range(m)) for i in range(n))
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))
def plus(*xs): return tuple(tuple(sum(row) for row in zip(*rs)) for rs in zip(*xs))
def neg(a): return tuple(tuple(-v for v in row) for row in a)
def tr(a): return tuple(zip(*a))
def eye(n): return mat(n,n,{(i,i):1 for i in range(n)})
def dz(d,f,r): return plus(mul(d,f), neg(mul(f,d)) if r%2==0 else mul(f,d))
def hz(h,e,f,r): return plus(mul(h,f), neg(mul(mul(e,f),h)) if r%2 else mul(mul(e,f),h))

G = (0,1,1,1,1,2,2,3)
Z = mat(8,8,{})

def artificial():
    d = mat(8,8,{(1,0):1,(5,4):1,(7,6):1})
    h = tr(d)
    inc = mat(8,2,{(2,0):1,(3,1):1})
    proj = tr(inc)
    local = {}
    for v in range(7):
        # A chain automorphism 1+[d,n], triangular on each two-grade block.
        n = mat(8,8,{(i,j):((v+2)*(i+3)+j*j+1)%5
                     for i in range(8) for j in range(8) if G[i]+1==G[j]})
        c = plus(eye(8),mul(d,n),mul(n,d))
        ci = L.inverse(c)  # fixture inversion only; reference identities below independent
        local[v] = L.TinyContraction(d,mul(c,inc),mul(proj,ci),mul(mul(c,h),ci),G)
    def edge(a,b):
        return mat(2,2,{(0,0):a*b+2*a,(0,1):a*a+b+1,(1,0):3*a-b*b,(1,1):a+2*b})
    def residual(v):
        a,b,c=v
        return plus(edge(b,c),neg(edge(a,c)),edge(a,b))
    return local,residual

def owners(n):
    labels=((5,0,15),(0,3,0),(1,5,8),(2,10,3),(3,12,12),(4,0,7),(4,1,14))
    return tuple(L.I.FullOwner(9,('independent',j),*v) for j,v in enumerate(labels[:n]))

class Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.local, r = artificial()
        cls.R = staticmethod(r)
        cls.p = L.TinyLift(cls.local,r)

    def test_01_snapshot_and_canonical_pins(self):
        raw=(HERE/'producer-ready.json').read_bytes()
        self.assertEqual(digest(raw),MARKER)
        m=json.loads(raw)
        self.assertEqual(len(m['files']),12)
        for f,h in m['files'].items(): self.assertEqual(digest((HERE/f).read_bytes()),h,f)
        raw=(HERE/'source-pins.json').read_bytes()
        self.assertEqual(digest(raw),PINS)
        p=json.loads(raw)
        self.assertEqual(len(p['immutable_dependencies']),13)
        self.assertEqual(len(p['canonical_workspace_dependencies']),9)
        for row in p['immutable_dependencies']+p['canonical_workspace_dependencies']:
            path=ROOT/row['path']
            if path.exists():
                b=path.read_bytes()
                self.assertEqual(len(b),row['bytes'])
                self.assertEqual(digest(b),row['sha256'],row['path'])
                if 'git_blob' in row:
                    self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),row['git_blob'])
        # Missing immutable proofs are reviewed via hash-checked HTTPS separately;
        # this offline file deliberately neither substitutes nor silently authenticates them.

    def test_02_all_End_matrix_units_and_both_H_terms(self):
        c=self.local[2]
        wrong_detected=False
        for i,j in it.product(range(8),repeat=2):
            f=mat(8,8,{(i,j):1});r=G[i]-G[j]
            ref=hz(c.h,c.E,f,r)
            self.assertEqual(c.homotopy(f,r),ref)
            self.assertEqual(c.differential(f,r),dz(c.d,f,r))
            lhs=plus(dz(c.d,ref,r-1),hz(c.h,c.E,dz(c.d,f,r),r+1))
            self.assertEqual(lhs,plus(f,neg(mul(mul(c.E,f),c.E))))
            bad=plus(dz(c.d,mul(c.h,f),r-1),mul(c.h,dz(c.d,f,r)))
            wrong_detected |= bad!=lhs
        self.assertTrue(wrong_detected)

    def test_03_all_signs_all_five_closures_seven_owners(self):
        nz=[False]*4
        for s in range(4):
            for v in it.combinations(range(7),s+3):
                f=self.p.component(s,v);nz[s]|=f!=Z
                c=self.local[v[0]]
                if s==0:
                    self.assertEqual(f,mul(mul(c.inc,tr(self.R(v))),c.proj))
                    self.assertNotEqual(self.R(v),tr(self.R(v)))
                    self.assertEqual(dz(c.d,f,0),Z)
                else:
                    delta=self.p.delta(s-1,v)
                    # From D=delta+(-1)^q d: dJs=(-1)^(s+1)delta J(s-1).
                    expected=delta if s%2 else neg(delta)
                    self.assertEqual(dz(c.d,f,-s),expected)
                    ref=hz(c.h,c.E,delta,1-s)
                    self.assertEqual(f,ref if s%2 else neg(ref))
        self.assertTrue(all(nz),nz)
        self.assertEqual(self.p.delta(3,tuple(range(7))),Z)
        # Every correction sign has a nonzero differential witness.
        for s in (1,2,3):
            self.assertTrue(any(dz(self.local[v[0]].d,self.p.component(s,v),-s)!=Z
                                for v in it.combinations(range(7),s+3)))
            for v in it.combinations(range(7),s+3):
                f=self.p.component(s,v);df=dz(self.local[v[0]].d,f,-s)
                if df!=Z:
                    self.assertNotEqual(dz(self.local[v[0]].d,neg(f),-s),df)
                    break

    def test_04_bottom_injectivity_not_six_owner_truncation(self):
        c=self.local[0]
        bottom=[mat(8,8,{(i,j):1}) for i,j in it.product(range(8),repeat=2) if G[i]-G[j]==-3]
        self.assertEqual(len(bottom),1)
        for w in bottom:
            self.assertNotEqual(dz(c.d,w,-3),Z)
            self.assertEqual(hz(c.h,c.E,dz(c.d,w,-3),-2),w)
        a=owners(7)
        b=L.outer_boundary_contract(a,3,[o.standard_tag for o in a])
        self.assertEqual((b['cech_degree'],b['internal_degree'],len(b['factors'])),(6,-3,7))
        self.assertEqual(b['source_bundle_degree'],[-5]*4)
        with self.assertRaises(ValueError): L.lift_terms(3,a)
        with self.assertRaises(ValueError): L.outer_boundary_contract(a[:6],3,[15])

    def test_05_every_face_sign_tail_and_original_prefix_owner(self):
        for s in range(4):
            a=owners(s+3);p=L.lift_terms(s,a)
            self.assertEqual(len(p['terms']),(1,4,20,120)[s])
            for term in p['terms']:
                current=list(a);prefix=[];sign=1;level=s
                word=term['operator_word']
                for pos in range(0,2*s,2):
                    hom,face=word[pos:pos+2]
                    self.assertEqual(hom['owner'],current[0].data())
                    self.assertEqual(hom['input_internal_degree'],1-level)
                    prefix.append(current[0]);j=face['face_index']
                    self.assertEqual(face['deleted_owner'],current[j].data())
                    sign*=(-1)**(level+1+j)
                    del current[j];level-=1
                self.assertEqual(term['coefficient'],sign)
                self.assertEqual(term['Rsharp_owners'],[o.data() for o in current])
                self.assertEqual(term['retained_prefix_owners'],[o.data() for o in prefix])
                self.assertEqual(term['all_factor_owners'],[o.data() for o in prefix+current])
                self.assertEqual(word[-1]['owner'],current[0].data())
                self.assertIs(word[-1]['transpose_row_input_once'],True)

    def test_06_canonical_factory_wiring_without_actual_construction(self):
        app=L.ActualFullLiftApplication()
        source_path=HERE.parent/'full-source-application/r_binding.py'
        self.assertIn("'full-source-application'/'r_binding.py'",(HERE/'lift.py').read_text())
        # Only artificial descriptors: tests wiring, not source semantics or admission.
        calls=[]
        class Source:
            def describe(self,a):
                calls.append(tuple(a))
                return {'schema':'actual-fresh-full-source-application-v1','source_homogeneity':{
                    'deck_character':[1]*4,'scalar_character_eigensheaf':'O(-2,-2,-2,-2)',
                    'matrix_frame':'actual physical row-End; conjugation/line frames retained'}}
            def source_pins(self): return {'artificial':True}
        class Transport:
            @staticmethod
            def build_template():return {'scalar_maps':[None]*20,'requests':[None]*32,'source_pins':{}}
        with patch.object(app,'_source',return_value=Source()), patch.object(L,'_load',return_value=Transport):
            for s in range(4):
                a=owners(s+3);d=app.describe(s,a)
                self.assertEqual(calls[-1],a[-3:])
                leaves={json.dumps(t['Rsharp_owners']) for t in d['lift_program']['terms']}
                self.assertEqual(leaves,{json.dumps(x) for x in d['source_leaf_bindings']})
                self.assertEqual(d['source_leaf_constructor'],'full-source-application/r_binding.py:ActualFullSourceApplication(repo).describe')
                self.assertFalse(d['physical_execution_authorized'])
                self.assertFalse(d['metadata_profile']['physical_arithmetic_cost_or_memory_admission'])
        rs=load('independent_rs',source_path)
        with self.assertRaises(ValueError):rs.authenticate(ROOT,reader=lambda *a:b'corrupt pinned proof')
        with patch.object(rs,'PINS_SHA','0'*64):
            with self.assertRaises(ValueError):rs.authenticate(ROOT,reader=lambda *a:b'')

    def test_07_actual_source_graph_metadata_not_source_values(self):
        rs=load('independent_rs_graph',HERE.parent/'full-source-application/r_binding.py')
        raw=(HERE.parent/'scalar-compiler/compiled-template.json').read_bytes()
        self.assertEqual(digest(raw),'30fa190054411ea8180015be2ad3dbba65bd209abef7ddd78973a6fae024c565')
        t=json.loads(raw);records=rs.compiler_source_contract(t)
        self.assertEqual(len(records),20)
        for rec in records:
            self.assertEqual(len(rec['kinetic_roots']),7)
            self.assertEqual(len(rec['gerbe_roots']),3)
            self.assertEqual(set(rec['component_roots']),{'baseline','Fk12','Fk34','E12','E34'})
        for change in ('branch','gerbe','jet'):
            bad=copy.deepcopy(t)
            if change=='branch':bad['Rsharp_components'].pop()
            elif change=='gerbe':bad['source_residual_components'][0]['baseline']['gerbe_terms'].pop()
            else:next(n for n in bad['nodes'] if n['op']=='physical_jet')['frames_differentiated']=False
            with self.assertRaises(ValueError):rs.compiler_source_contract(bad)

    def test_08_universal_noncommutative_U_identity(self):
        # Arbitrary invertible matrices and arbitrary derivative values: no physical jets.
        a=((F(1),F(2)),(F(0),F(1)));b=((F(2),F(1)),(F(1),F(1)))
        da=((F(3),F(-1)),(F(4),F(2)));db=((F(0),F(5)),(F(-2),F(1)))
        ai=L.inverse(a);bi=L.inverse(b);g=mul(b,a)
        dg=plus(mul(db,a),mul(b,da))
        u=mul(mul(mul(ai,bi),db),a)
        self.assertEqual(u,plus(mul(L.inverse(g),dg),neg(mul(ai,da))))
        self.assertNotEqual(u,mul(bi,db))
        self.assertNotEqual(u,plus(mul(L.inverse(g),dg),mul(ai,da)))

    def test_09_derived_bounds_exact_degree_original_tags(self):
        lo=-3*(481+2)-3*(14*5+3);hi=217+3*1677
        self.assertEqual((lo,hi),(-1668,5248))
        standard=max(-lo,hi+2,max(1677+70,481+70+2))+1
        g=(4,2);k=(2*(g[0]+1),2*(g[1]+1));u=tuple(x+y for x,y in zip(g,k))
        base=tuple(x+2*y for x,y in zip(g,u))
        inc=(4,2);hom=(6,3)
        derived=[tuple(base[i]+inc[i]+s*hom[i] for i in range(2)) for s in range(4)]
        self.assertEqual((base,standard),((32,18),5251))
        self.assertEqual(derived,[(36,20),(42,23),(48,26),(54,29)])
        self.assertEqual([(x['carrier'],x['legal']) for x in L.domain_ledger()['components']],derived)
        for s in range(4):
            for boundary in (False,True):
                a=owners(s+3+boundary);tags=[o.standard_tag for o in a]
                fn=L.outer_boundary_contract if boundary else L.outer_owner_contract
                out=fn(a,s,tags)
                degrees=tuple(sum(54*(4 if o.carrier==5 else 5)+29*(1+2*((o.legal_mask>>i)&1))+5251 for o in a)-s-2 for i in range(4))
                self.assertEqual(out['whole_numerator_homogeneous_degree'],degrees)
                self.assertEqual([x['owner'] for x in out['factors']],[o.data() for o in a])
                self.assertTrue(out['index_checks_are_not_source_clearing_proof'])
                with self.assertRaises(ValueError):fn(a,s,tags[1:])
            f=L.original_frame(s)
            self.assertEqual(f['tau_power'],-s-2)
            self.assertEqual(f['full_sign_deck_product_removed_count'],1)
            self.assertEqual(f['scalar_L_applied_after_this_conversion'],s==2)
        self.assertFalse(L.domain_ledger()['whole_standard_extension_from_ledger_alone'])

    def test_10_all_constant_rows_and_weighted_request_scope(self):
        sys.path.insert(0,str(HERE.parent/'transport-binding'))
        t=load('independent_transport',HERE.parent/'transport-binding/transport_binding.py')
        # Each W[a,b] v[k] occurs once in gamma W and once in W ev.
        for i,b in it.product(range(15),range(2)):
            coeff={}
            for a,k in it.product(range(5),range(5)):
                z=t.gamma(i,a,k)
                if z:coeff[a,b,k]=z
            for term in t.scalar_terms(i,b)[1:]:
                a,j=term['entry'];key=(a,j//5,j%5)
                coeff[key]=coeff.get(key,0)+term['coefficient']
            self.assertTrue(all(z==0 for z in coeff.values()))
        path=HERE.parent/'detector-selection/weighted-requests.json'
        raw=path.read_bytes()
        self.assertEqual(digest(raw),'f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0')
        requests=json.loads(raw)['requests']
        self.assertEqual(len(requests),32)
        self.assertEqual(sum(len(r['terms']) for r in requests),127)
        self.assertEqual(len({(r['scalar_map']['i'],r['scalar_map']['b'],tuple(term['laurent_exponents']))
                              for r in requests for term in r['terms']}),121)
        with self.assertRaises(ValueError):t.validate_frame(dict(t.FRAME,scalar_tau_exponent=-2))

    def test_11_nonclosed_artificial_source_is_not_promoted(self):
        def broken(v):
            return plus(self.R(v),mat(2,2,{(0,1):int(v==(0,1,2))}))
        p=L.TinyLift(self.local,broken)
        detected=False
        for v in it.combinations(range(7),4):
            c=self.local[v[0]]
            detected |= dz(c.d,p.component(1,v),-1)!=p.delta(0,v)
        self.assertTrue(detected)

    def test_12_RS_positive_boundary_and_ambient_syzygy(self):
        f=load('independent_RS_words',HERE.parent/'full-source-application/formal_identities.py')
        self.assertEqual(f.reduction_identity(),{})
        self.assertNotEqual(f.reduction_identity(-1),{})
        a,b=f.defect_syzygy()
        self.assertEqual(a,b)
        for j in range(4):
            signs=[1,1,-1,-1];signs[j]*=-1
            a,b=f.defect_syzygy(tuple(signs))
            self.assertNotEqual(a,b)

    def test_13_malformed_inputs_and_unconditional_physical_refusal(self):
        a=owners(4)
        for bad in (True,-1,4,1.0):
            with self.assertRaises(ValueError): L.lift_terms(bad,a)
        for bad in (a[::-1],(a[0],a[0],*a[2:]),(a[0],L.I.FullOwner(8,'bad',0,3,0),*a[2:])):
            with self.assertRaises(ValueError):L.lift_terms(1,bad)
        with self.assertRaises(ValueError):L.outer_owner_contract(a,1,[True,0,8,3])
        with self.assertRaises(ValueError):L.ActualFullLiftApplication('/tmp/replacement')
        with self.assertRaises(TypeError):L.ActualFullLiftApplication(closure=True)
        app=L.ActualFullLiftApplication()
        for f in (L.actual_coefficient,app.coefficient,app.factor_terms,app.owners):
            with self.assertRaises(L.I.PhysicalAdmissionMissing):f({'closure':True,'regularity':'accepted'},(0,0,0,0))

if __name__=='__main__':
    start=time.monotonic()
    # Fail if a future change tries to invoke git or any subprocess from controls.
    with patch('subprocess.Popen',side_effect=RuntimeError('no subprocess/git in independent controls')):
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Independent))
    print(json.dumps({'tests':result.testsRun,'success':result.wasSuccessful(),'optimized':not __debug__,
        'seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'actual_coefficients_jets_fibers':False,'resource_admission':False}))
    raise SystemExit(0 if result.wasSuccessful() else 1)
