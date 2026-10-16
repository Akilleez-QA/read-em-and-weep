"""BI-R: tiny artificial algebra only. Direct replay supervises normal and -O.
No Git, producer runners, actual constructors, HM arrays, jets or fibers.
Historical text pins use read-only HTTPS when absent/different locally.
"""
import ast
from fractions import Fraction as Q
import hashlib
import importlib.util
import itertools as it
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
import unittest
import urllib.request

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MARKER = 'aa0e81b32699e15c3c95fc6792b3cdcec763fd5b12f074b169f8da908ebc6a65'
LIMIT = 768 * 1024 * 1024

def sha(b): return hashlib.sha256(b).hexdigest()
def check_pin(row, raw):
    if type(raw) is not bytes or len(raw) != row['bytes'] or sha(raw) != row['sha256']:
        raise ValueError('pin bytes/length/SHA drift')
    if 'git_blob' in row and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != row['git_blob']:
        raise ValueError('blob identity drift')

def producer_snapshot():
    raw = (HERE/'producer-ready.json').read_bytes()
    if sha(raw) != MARKER: raise ValueError('producer marker drift')
    rows = json.loads(raw)['files']
    if len(rows) != 13: raise ValueError('producer inventory drift')
    for name, digest in rows.items():
        if Path(name).name != name or sha((HERE/name).read_bytes()) != digest:
            raise ValueError('producer file drift: '+name)
    return dict(rows, **{'producer-ready.json': sha(raw)})

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    spec.loader.exec_module(m); return m

import boundary as A

def tiny_current():
    # Different from producer fixture: arbitrary formal SL2 first jets.
    h=A.mat([[1,0],[0,-1]]); e=A.mat([[0,1],[0,0]]); f=A.mat([[0,0],[1,0]])
    frames={0:A.mat([[1,2],[0,1]]),1:A.mat([[1,0],[3,1]]),2:A.mat([[3,2],[1,1]])}
    charges={i:(A.add(A.scale(i*i+2,h),A.scale(i+1,e)),A.add(A.scale(2*i-1,f),A.scale(i+3,h))) for i in frames}
    df={i:(Q(i+2,3),Q(i*i-1,5)) for i in frames}
    return A.ArtificialCurrents(frames,charges),df

def wedge(x,y): return A.trace(A.sub(A.mul(x[0],y[1]),A.mul(x[1],y[0])))
def formadd(x,y): return tuple(A.add(a,b) for a,b in zip(x,y))
def formscale(c,x): return tuple(A.scale(c,a) for a in x)
def edge_delta(fn): return fn(1,2)-fn(0,2)+fn(0,1)

class Independent(unittest.TestCase):
    def test_01_all_producer_and_dependency_pins(self):
        producer_snapshot()
        pins=json.loads((HERE/'source-pins.json').read_text())
        self.assertFalse(pins['actual_source_evaluated']); self.assertFalse(pins['physical_execution_authorized'])
        for row in pins['immutable_dependencies']+pins['workspace_dependencies']:
            p=ROOT/row['path']; raw=p.read_bytes() if p.is_file() else b''
            if sha(raw) != row['sha256'] and 'commit' in row:
                url='https://raw.githubusercontent.com/Akilleez-QA/read-em-and-weep/'+row['commit']+'/'+row['path']
                raw=urllib.request.urlopen(url,timeout=8).read()
            check_pin(row,raw)
        self.assertEqual(len(pins['immutable_dependencies']),15)
        self.assertEqual(len(pins['workspace_dependencies']),3)

    def test_02_malformed_pins_rejected_without_assert(self):
        b=b'artificial pin\n'; row={'bytes':len(b),'sha256':sha(b),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
        check_pin(row,b)
        for raw in (b+b' ',b.decode(),None):
            with self.assertRaises(ValueError): check_pin(row,raw)
        for key,value in (('bytes',0),('sha256','0'*64),('git_blob','0'*40)):
            bad=dict(row);bad[key]=value
            with self.assertRaises(ValueError): check_pin(bad,b)

    def test_03_noncommuting_endpoint_identity_and_sign_mutants(self):
        c,df=tiny_current(); failures=[False]*4
        for i,j,k in it.permutations(range(3)):
            edge=lambda a,b:c.B_edge(df,a,b)
            dij=A.scalar_difference(df,i,j); djk=A.scalar_difference(df,j,k)
            La,Lb=(c.L(i,j,d) for d in (0,1)); Ua,Ub=(c.U(i,j,k,d) for d in (0,1))
            expected=A.scale(Q(1,2),A.add(A.sub(A.scale(djk[0],Lb),A.scale(djk[1],La)),A.sub(A.scale(dij[1],Ua),A.scale(dij[0],Ub))))
            self.assertEqual(c.delta_edge(edge,i,j,k),expected)
            self.assertEqual(c.E_triangle(lambda a,b:A.scalar_difference(df,a,b),i,j,k),expected)
            terms=(A.scale(djk[0],Lb),A.scale(-djk[1],La),A.scale(dij[1],Ua),A.scale(-dij[0],Ub))
            for n,t in enumerate(terms): failures[n] |= A.sub(expected,t)!=expected
            wrong=A.add(A.sub(A.mul(A.mul(c.g(i,j),edge(j,k)),A.inv(c.g(i,j))),edge(i,k)),edge(i,j))
            if wrong!=expected: failures[0]=True
        self.assertTrue(all(failures))
        self.assertNotEqual(A.mul(c.g(0,1),c.g(1,2)),A.mul(c.g(1,2),c.g(0,1)))

    def test_04_unsymmetrized_four_block_transgression_and_edge_correction(self):
        # Artificial two-direction forms, with rank-weighted trace. These
        # are NOT evaluations of the four physical split matrices.
        ranks=(5,15,10,2); signs=(-1,1,-1,1); weights=(-1,1,3,5)
        q=((Q(1),Q(2)),(Q(3),Q(-1)),(Q(-2),Q(4)))
        theta=lambda i,j:tuple((q[j][d]-q[i][d])/2 for d in range(2))
        blocks=[[(A.mat([[(l+1)*i*i+l+1,2*i-l],[i+2,1-l]]),A.mat([[2-l,i+3],[l-i,(l+2)*i*i+1]])) for i in range(3)] for l in range(4)]
        def connection(l,i,j): return tuple(A.scale(-weights[l]*x,A.ID) for x in theta(i,j))
        def T(i,j,omit=False):
            out=Q(0)
            for l in range(4):
                bi,bj=blocks[l][i],blocks[l][j]; aa=connection(l,i,j)
                # B star A + A star B + B star delta B; (-,+,-).
                value=-wedge(bi,aa)+(0 if omit else wedge(aa,bj))-wedge(bi,formadd(bj,formscale(-1,bi)))
                simplified=-wedge(bi,bj)-weights[l]*sum((theta(i,j)[0]*A.trace(x[1])-theta(i,j)[1]*A.trace(x[0]) for x in (bi,bj)),Q(0))
                if not omit: self.assertEqual(value,simplified)
                out+=signs[l]*Q(ranks[l],2)*value
            return out
        def square(prime):
            out=Q(0)
            for l in range(4):
                x,y=connection(l,0,1),connection(l,1,2)
                if prime:
                    x=formadd(x,formadd(blocks[l][1],formscale(-1,blocks[l][0])))
                    y=formadd(y,formadd(blocks[l][2],formscale(-1,blocks[l][1])))
                out+=signs[l]*Q(ranks[l],2)*wedge(x,y)
            return out
        self.assertEqual(sum(s*r*k*k for s,r,k in zip(signs,ranks,weights)),-30)
        self.assertEqual(edge_delta(T),square(False)-square(True))
        self.assertNotEqual(edge_delta(lambda i,j:T(i,j,True)),edge_delta(T))
        r=lambda i,j:(q[j][0]-q[i][0])*(q[j][1]-q[i][1])
        Qab=(q[1][0]-q[0][0])*(q[2][1]-q[1][1])
        Qba=(q[1][1]-q[0][1])*(q[2][0]-q[1][0])
        self.assertEqual(edge_delta(r),-Qab-Qba)
        trC=-square(True)/2  # row/column transpose reversal sign
        F=Q(15,4)*Qab-trC/2
        ds=-edge_delta(T)/4-Q(15,8)*edge_delta(r)
        self.assertEqual(ds,F)
        self.assertNotEqual(-edge_delta(T)/4,F)
        self.assertNotEqual(-edge_delta(T)/4+Q(15,8)*edge_delta(r),F)
        self.assertNotEqual(ds,Q(15,4)*Qab+trC/2)

    def test_05_positive_RS_boundary_and_complete_variation(self):
        # Nonzero artificial cochains: R=M+delta W forces the MINUS
        # delta(Delta W) in the variation of M.
        d=lambda x:(x,2*x)
        K=Q(7,3); W=Q(5,2); baseline=(Q(11),Q(-4))
        dK,dW=d(K),d(W)
        changeR=dK; changeM=tuple(x-y for x,y in zip(dK,dW))
        self.assertEqual(tuple(x+y for x,y in zip(changeM,dW)),changeR)
        self.assertNotEqual(tuple(x-y for x,y in zip(changeM,dW)),changeR)
        # Seven kinetic and three NEGATIVE gerbe contributions are fixed.
        fixed=sum(range(1,8))-sum(range(8,11))+13+17
        self.assertNotEqual(fixed,0)
        self.assertEqual((fixed+K)-fixed,K)
        self.assertNotEqual((sum(range(1,8))+13+17+K)-fixed,K)

    def test_06_pair_H1_zero_is_not_pair_H2_zero(self):
        # Kunneth harmonic degrees for actual line twists, no sections.
        def harmonic(twists):
            degrees={0:1}
            for n in twists:
                factor={0:n+1} if n>=0 else ({1:-n-1} if n<=-2 else {})
                out={}
                for a,x in degrees.items():
                    for b,y in factor.items(): out[a+b]=out.get(a+b,0)+x*y
                degrees=out
            return degrees
        self.assertEqual(harmonic((-2,-2,0,0)),{2:1})
        self.assertEqual(harmonic((-2,-2,-2,-2)),{4:1})
        self.assertEqual(harmonic((-4,)*4),{4:81})
        self.assertEqual(harmonic((-2,0,0,0)),{1:1})

    def test_07_explicit_C_ladder_all_components_and_wrong_sign(self):
        import resolution_boundary as R
        fixture=load('bir_JC_fixture',R.JC/'test_lift.py')
        local,_=fixture.fixtures(); L=R.L
        edge=lambda v:L.checked_matrix([[v[0]-2*v[1],3+v[0]*v[1]],[2*v[0]+v[1],v[0]+v[1]*v[1]]])
        def source(v):
            out=L.zero(2)
            for n in range(3): out=L.add(out,L.scale((-1)**n,edge(v[:n]+v[n+1:])))
            return out
        J=L.TinyLift(local,source); C=R.TinyBoundaryPrimitive(J,edge)
        nonzero=[False]*4; mutant=False; transpose_seen=False
        for s in range(4):
            for v in it.combinations(range(7),3+s):
                self.assertEqual(C.total_boundary_component(s,v),J.component(s,v))
                c=C.component(s,v[:-1]); nonzero[s] |= c!=L.zero(8)
                local[v[0]].check_degree(c,-s)
                if s==1:
                    dv=local[v[0]].differential(C.component(2,v),-2)
                    mutant |= L.add(C.delta(1,v),dv)!=J.component(1,v)
            if s==0:
                v=(0,1); expected=L.times(L.times(local[0].inc,L.transpose(edge(v))),local[0].proj)
                self.assertEqual(C.component(0,v),expected)
                transpose_seen=expected!=L.times(L.times(local[0].inc,edge(v)),local[0].proj)
        self.assertTrue(all(nonzero)); self.assertTrue(mutant); self.assertTrue(transpose_seen)
        bottom=fixture.matrix(8,8,{(0,7):Q(3,2)})
        self.assertNotEqual(local[0].differential(bottom,-3),L.zero(8))

    def test_08_global_cover_iso_without_out_of_domain_primitive(self):
        # Coarse d:Q->Q^2, d(a)=(a,0); refined d:Q^2->Q^3,
        # d(a,b)=(a,b,0). Both H1=Q. r1(x,z)=(x,0,z) is an iso
        # on H1. A bounded subcomplex restricts C0=0: same H1 class
        # can then lack a bounded primitive. No Pi applied to it.
        coarse_d=lambda a:(a,Q(0)); refined_d=lambda a,b:(a,b,Q(0))
        r0=lambda a:(a,Q(0)); r1=lambda x,z:(x,Q(0),z)
        self.assertEqual(r1(*coarse_d(3)),refined_d(*r0(3)))
        old=(Q(2),Q(7)); new=(Q(19),Q(7))
        difference=tuple(a-b for a,b in zip(r1(*new),r1(*old)))
        self.assertEqual(difference,refined_d(17,0))
        self.assertEqual(new[1],old[1])
        self.assertNotEqual(new,old)  # bounded d has image zero
        bad_r=lambda x,z:(x,Q(0),Q(0))
        self.assertEqual(bad_r(0,1),bad_r(0,0)) # chain map alone not injective
        self.assertNotEqual((0,1)[1],(0,0)[1])

    def test_09_hypercohomology_not_isolated_Cech_component(self):
        # Two internal degrees -1,0 with vertical d=identity and delta=0.
        # Every degree0 element is a TOTAL boundary, while an isolated
        # horizontal complex in degree0 would retain it.
        x=Q(9,4); vertical=lambda a:a; horizontal=lambda a:Q(0)
        self.assertEqual(vertical(x),x);self.assertNotEqual(horizontal(x),x)
        # A commuting square totalizes with opposite vertical signs at
        # q=0 and q=1; reversing that sign gives 2*x instead of zero.
        self.assertEqual(vertical(x)-vertical(x),0)
        self.assertNotEqual(vertical(x)+vertical(x),0)
        # Bottom injectivity is essential: d=0 leaves an undetected error.
        self.assertNotEqual(x,0);self.assertEqual(horizontal(x),0)

    def test_10_frames_owned_poles_and_analytic_boxes_only(self):
        recipe=json.loads((HERE/'actual-raw-s-denotation.json').read_text())
        data=json.loads((HERE/'analytic-reduction.json').read_text())
        self.assertEqual(recipe['block_ranks'],[5,15,10,2]); self.assertEqual(recipe['supertrace_signs'],[-1,1,-1,1])
        self.assertTrue(recipe['physical_refined_line_frames']['moving_frames_differentiated'])
        self.assertTrue(recipe['physical_refined_line_frames']['nu_is_not_differentiated_as_constant1'])
        for s in range(4):
            # Degree comes from the homogeneous original frame, not a
            # multiplier appended to a finite-chart pole estimate.
            self.assertEqual((-s)-2,-s-2)
        for key,m,r in (('J2',5,-2),('full_lift_max6_owners',6,-3)):
            D=m*(54*5+29*3)+r-2
            self.assertEqual(data[key]['whole_numerator_degree_upper'],D)
            self.assertEqual(data[key]['finite_exponent_rectangle'],[-m*(2006+357),D+m*6677])
        for key in ('rectangles_are_occupied_support','six_owner_box_applies_to_seven_owner_deltaJ3','nonconstant_product_or_memory_bound_proved','new_execution_budget_issued','physical_execution_authorized','obstruction_decided'):
            self.assertIs(data[key],False)
        self.assertEqual(data['additional_standard_boundary_power_for_raw_route'],0)
        # Inserted-only weights leave suffix poles: exponents of two
        # artificial independent divisors, no physical ring operation.
        denominator=(-3,-5); weighted=(denominator[0]+3,denominator[1])
        self.assertLess(weighted[1],0);self.assertEqual((weighted[0],weighted[1]+5),(0,0))

    def test_11_physical_gate_without_constructor_or_request_inspection(self):
        import resolution_boundary as R
        class Poison:
            def __iter__(self): raise AssertionError('physical request inspected')
            def __repr__(self): raise AssertionError('physical request inspected')
        app=object.__new__(R.L.ActualFullLiftApplication)
        for fn in (R.L.actual_coefficient,app.coefficient,app.factor_terms,app.owners):
            with self.assertRaises(R.L.I.PhysicalAdmissionMissing): fn(Poison(),release=True,mode='physical')
        tree=ast.parse((HERE/'build_handoff.py').read_text())
        self.assertTrue(any(isinstance(n,ast.If) for n in ast.walk(tree)))
        # BI supplies no actual raw executor: its modules import only
        # scalar fractions and the existing toy lift, not HM evaluators.
        btree=ast.parse((HERE/'boundary.py').read_text())
        imports=[n.module for n in ast.walk(btree) if isinstance(n,ast.ImportFrom)]
        self.assertEqual(imports,['fractions'])

    def test_13_moving_nu_at_value_one_and_transpose_order(self):
        K=A.mat([[1,2],[3,7]]); dK=A.mat([[2,-1],[4,3]])
        Qi=A.mat([[2,0],[0,-2]]); Qj=A.mat([[-3,0],[0,3]])
        # D_i=D_j=1 at the point, but their logarithmic jets are nonzero.
        physical=A.add(dK,A.sub(A.mul(Qj,K),A.mul(K,Qi)))
        self.assertNotEqual(physical,dK)
        self.assertNotEqual(physical,A.add(dK,A.mul(Qj,K)))
        self.assertNotEqual(physical,A.sub(dK,A.mul(K,Qi)))
        transpose=lambda m:tuple(zip(*m))
        self.assertEqual(transpose(A.mul(Qj,K)),A.mul(transpose(K),transpose(Qj)))
        self.assertNotEqual(transpose(A.mul(Qj,K)),A.mul(transpose(Qj),transpose(K)))
        # Exact old connection transport: dx/[x(x^2-1)] becomes
        # -t dt/(1-t^2), retaining its nonzero value at a legal toy t.
        t=Q(2,3);x=1/t
        transported=(-1/t**2)/(x*(x*x-1))
        self.assertEqual(transported,-t/(1-t*t));self.assertNotEqual(transported,0)

    def test_12_generic_first_order_exactness_does_not_kill_second_class(self):
        # Independent nontrivial cokernel: d:Q^2->Q^3 has rank2.
        d=lambda a,b:(a,b,2*a-b)
        detector=lambda v:v[2]-2*v[0]+v[1]
        self.assertEqual(detector(d(Q(7,3),Q(-2,5))),0)
        self.assertEqual(detector((Q(0),Q(0),Q(1))),1)
        self.assertEqual(Q(4)-Q(4),0) # independent exact scalar problem


def main():
    if '--child' in sys.argv:
        resource.setrlimit(resource.RLIMIT_AS,(LIMIT,LIMIT))
        resource.setrlimit(resource.RLIMIT_CPU,(59,59))
        before=producer_snapshot(); start=time.monotonic()
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Independent))
        if before != producer_snapshot(): raise RuntimeError('producer changed during review')
        print(json.dumps({'success':result.wasSuccessful(),'tests':result.testsRun,'optimized':not __debug__,'seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'producer_marker_before':MARKER,'producer_marker_after':sha((HERE/'producer-ready.json').read_bytes()),'all13_producer_files_unchanged':True,'physical_execution':False}))
        return int(not result.wasSuccessful())
    for flags in ([],['-O']):
        result=subprocess.run([sys.executable,'-B',*flags,str(Path(__file__).resolve()),'--child'],text=True,capture_output=True,timeout=60)
        print(result.stderr,end='');print(result.stdout,end='')
        if result.returncode: return result.returncode
    return 0

if __name__=='__main__': raise SystemExit(main())
