"""SR-R: artificial controls only. Direct invocation supervises both modes.
No physical guard is removed; no actual payload is evaluated or imported.
"""
import sys, os, subprocess, resource, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
if __name__=='__main__' and '--child' not in sys.argv:
    for mode in ([],['-O']):
        start=time.monotonic()
        r=subprocess.run([sys.executable,'-B',*mode,str(Path(__file__).resolve()),'--child'],timeout=60)
        print('mode='+('optimized' if mode else 'normal')+' wall=%.3f exit=%s'%(time.monotonic()-start,r.returncode),flush=True)
        if r.returncode:raise SystemExit(r.returncode)
    raise SystemExit(0)
resource.setrlimit(resource.RLIMIT_AS,(768*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(59,59))
sys.dont_write_bytecode=True
import unittest, json, hashlib, itertools, math
from fractions import Fraction as Q
from types import SimpleNamespace
from unittest.mock import patch
import raw_engine as E
import program as P
import artificial as A
RF,SC,JC,I=E.RF,E.SC,E.JC,E.I

def digest(b):return hashlib.sha256(b).hexdigest()

def authenticate_local():
    raw=(HERE/'producer-ready.json').read_bytes()
    if digest(raw)!='f7f6d523c5f55af2b571cf8912e7473ac21f1a5949354d8bbb6d94eaddec794a':raise ValueError('marker drift')
    for f,h in json.loads(raw)['files'].items():
        if digest((HERE/f).read_bytes())!=h:raise ValueError(f)
    for r in json.loads((HERE/'source-pins.json').read_text())['local_dependencies']:
        if digest((HERE.parent/r['path']).read_bytes())!=r['sha256']:raise ValueError(r['path'])

class Number:
    def __init__(self,ex,v):self.ex,self.v=ex,Q(v)
    def inverse(self):return Number(self.ex,1/self.v)
    def __add__(self,b):return Number(self.ex,self.v+b.v)
    def __sub__(self,b):return Number(self.ex,self.v-b.v)
    def __mul__(self,b):return Number(self.ex,self.v*b.v)
    def __neg__(self):return Number(self.ex,-self.v)
class Numbers:
    def scalar(self,q):return Number(self,q)
    def x(self,i):return self.scalar((2,3,5,7)[i])

class NewFrames(A.ArtificialFrames):
    """New artificial SL2/gerbe fixture, never a PhysicalModel subclass."""
    def __init__(self,ex):
        super().__init__(ex)
        C=((ex.scalar(1),ex.scalar(2)),(ex.scalar(0),ex.scalar(1)))
        self.frames=tuple(self.M.mul(C,h,self.M.inverse(C))for h in self.frames)
    def charge(self,o,d):return (o.carrier**2+2*o.carrier)*(d+2)

def new_source(labels,omit=None):
    ex=RF.Execution();m=NewFrames(ex);oo=tuple(I.FullOwner(0,('new',j),c,0,0)for j,c in enumerate(labels))
    source=E.RawSource(m.M);r=source.residual(oo);parts=source.components[oo]
    if omit:r=m.M.add(*(v for k,v in parts.items()if k!=omit))
    r=m.M.mul(m.M.inverse(m.frame(oo[0])),r,m.frame(oo[0]))
    def coefficient(v):return dict(v.terms).get(15,ex.rational(0)).laurent_coefficient((0,0,0,0))
    return tuple(tuple(coefficient(v)for v in row)for row in r),parts

class FractionMatrices:
    """SC actual matrix methods on constant artificial contractions."""
    def __init__(self,local):self.local=local
    def add(self,*a):
        out=JC.zero(len(a[0]),len(a[0][0]))
        for b in a:out=JC.add(out,b)
        return out
    def scale(self,a,c):return JC.scale(c,a)
    def mul(self,*aa):
        out=aa[0]
        for a in aa[1:]:out=JC.times(out,a)
        return out
    def transpose(self,a):return JC.transpose(a)
    def leaf(self,name,shape,**kw):
        c=self.local[kw['owner'].standard_tag];ids=[[0],[1,2,3,4],[5,6],[7]]
        if name=='I_phys':return tuple(c.inc[j]for j in ids[1])
        if name=='P_phys':return tuple(tuple(row[j]for j in ids[1])for row in c.proj)
        k={'H0':1,'H1':2,'eta':3}[name]
        return tuple(tuple(c.h[i][j]for j in ids[k])for i in ids[k-1])

def tiny_end_to_end():
    source={t:new_source(t)[0]for t in itertools.combinations(range(5),3)}
    local=A.contractions();schema=E.load('sr01_lift_schema',HERE.parent/'transport-binding/lift_schema.py').closed_lift_schema()
    out=[]
    for stair in SC.staircase_records():
        owners=tuple(I.FullOwner(0,('new-outer',t),t.bit_count(),0,t)for t in stair['standard_tags'])
        canon,sgn=I.sorted_source(owners)
        def residual(oo):return source[tuple(o.carrier for o in oo)]
        lift=SC.Lift(FractionMatrices(local),residual,schema,dims=(1,4,2,1));blocks=lift.at(2,canon)
        # Independent full graded matrix engine cross-checks SC's block HPL.
        tags=tuple(o.standard_tag for o in canon)
        full=JC.TinyLift({t:local[t]for t in tags},lambda ts:source[tuple(t.bit_count()for t in ts)]).component(2,tags)
        for (u,v),b in blocks.items():
            ids=[[0],[1,2,3,4],[5,6],[7]]
            if b!=tuple(tuple(full[i][j]for j in ids[u])for i in ids[v]):raise ValueError('SC block/full mismatch')
        scalar=blocks[(3,1)][0][0]+blocks[(2,0)][0][0]-blocks[(2,0)][0][1]
        out.append(stair['orientation']*sgn*scalar)
    return out

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):authenticate_local();cls.rows=tiny_end_to_end()
    @classmethod
    def tearDownClass(cls):authenticate_local()
    def test_pins(self):authenticate_local()
    def test_pin_poison(self):
        with patch.object(Path,'read_bytes',return_value=b'bad'):
            with self.assertRaises(ValueError):authenticate_local()
    def test_new_e2e_partial_sign(self):
        self.assertEqual(len(self.rows),24);self.assertTrue(all(self.rows));self.assertEqual(sum(self.rows),0)
        self.assertNotEqual(self.rows[0],0)
        self.assertNotEqual(sum(self.rows)-2*self.rows[0],0)
    def test_source_correction_controls(self):
        r,parts=new_source((0,1,3));self.assertEqual(set(parts),{'baseline','Fk12','Fk34','E12','E34'})
        for k in ('baseline','Fk12','Fk34'):self.assertNotEqual(new_source((0,1,3),k)[0],r)
        self.assertNotEqual(r,JC.transpose(r))
    def test_order_before_faces(self):
        oo=tuple(I.FullOwner(0,('synthetic',j),c,m,t)for j,(c,m,t)in enumerate([(2,1,8),(5,3,1),(0,2,4),(2,0,2),(1,0,0)]))
        canon,sgn=I.sorted_source(oo);self.assertEqual([o.source_key for o in canon],sorted(o.source_key for o in oo))
        self.assertEqual(sgn,(-1)**sum(oo.index(canon[i])>oo.index(canon[j])for i in range(5)for j in range(i+1,5)))
        self.assertEqual(canon[0].carrier,5)
        for j in range(5):self.assertEqual(I.sorted_source(canon[:j]+canon[j+1:])[1],1)
        self.assertEqual({o.occurrence:o.standard_tag for o in oo},{o.occurrence:o.standard_tag for o in canon})
    def test_raw_four_blocks_endpoint_signs(self):
        ex=RF.Execution();M=E.Mat(ex)
        def m(x):return ((ex.scalar(x),),)
        ai,bi,aj,bj=map(lambda a:list(map(m,a)),([2,3,5,7],[11,13,17,19],[23,29,31,37],[41,43,47,53]))
        qa,qb=Q(3),Q(-2)
        pieces=[sign*(a*d-b*c+k*(qa*(b+d)-qb*(a+c))/2)for a,b,c,d,k,sign in zip([2,3,5,7],[11,13,17,19],[23,29,31,37],[41,43,47,53],[-1,1,3,5],[-1,1,-1,1])]
        got=E.raw_scalar_formula(M,(ai,bi),(aj,bj),ex.scalar(qa),ex.scalar(qb)).laurent_coefficient((0,0,0,0))
        self.assertEqual(got,sum(pieces)/4-Q(15,8)*qa*qb)
        for term in pieces:self.assertNotEqual(got,got-term/2)
    def test_original_inclusion_frame_and_carrier_H(self):
        local=A.contractions();base=FractionMatrices(local)
        o=I.FullOwner(0,('new-frame',0),1,0,8);D=((Q(2),Q(0)),(Q(0),Q(1,2)));Di=JC.inverse(D)
        class Framed(FractionMatrices):
            def leaf(self,name,shape,**kw):
                a=super().leaf(name,shape,**kw)
                return JC.times(a,D)if name=='I_phys'else JC.times(Di,a)if name=='P_phys'else a
        M=Framed(local);row=((Q(1),Q(3)),(Q(-2),Q(4)))
        oo=(o,I.FullOwner(0,('new-frame',1),2,0,12),I.FullOwner(0,('new-frame',2),3,0,14))
        schema=E.load('sr01_lift_schema',HERE.parent/'transport-binding/lift_schema.py').closed_lift_schema()
        lift=SC.Lift(M,lambda t:row,schema,dims=(1,4,2,1));got=lift.at(0,oo)[(1,1)]
        inc=base.leaf('I_phys',None,owner=o);proj=base.leaf('P_phys',None,owner=o)
        correct=base.mul(inc,D,JC.transpose(row),Di,proj)
        self.assertEqual(got,correct)
        self.assertNotEqual(got,base.mul(inc,D,row,Di,proj))
        self.assertEqual(base.mul(M.leaf('I_phys',None,owner=o),M.leaf('P_phys',None,owner=o)),base.mul(inc,proj))
        for name in ('H0','H1','eta'):self.assertEqual(M.leaf(name,None,owner=o),base.leaf(name,None,owner=o))
    def test_both_E_endpoints_sign_controls(self):
        ex=RF.Execution();model=NewFrames(ex);M=model.M
        z,o=ex.scalar(0),ex.scalar(1)
        model.frames=tuple(M.mul(((o,ex.x(0)*ex.scalar(c+1)+ex.x(2)*ex.scalar(c+2)),(z,o)),((o,z),(ex.x(1)*ex.scalar(c+3)+ex.x(3)*ex.scalar(c+4),o)))for c in range(6))
        oo=tuple(I.FullOwner(0,('new-E',i),c,0,0)for i,c in enumerate((0,1,3)))
        class ScalarFixture(E.RawSource):
            def T(self,p,a,b):
                v=ex.scalar((a.carrier+1)*(b.carrier+2))
                for d in range(4):v=v*ex.x(d)
                return ((v,),)
        S=ScalarFixture(M);i,j,k=oo
        for pair,other in (((0,1),(2,3)),((2,3),(0,1))):
            a,b=pair;g=S.g(i,j);gi=M.inverse(g);gjk=S.g(j,k);gjki=M.inverse(gjk)
            L=lambda d:M.mul(gi,M.D(g,d))
            U=lambda d:M.mul(gi,gjki,M.D(gjk,d),g)
            sij,sjk=S.T(other,i,j),S.T(other,j,k)
            terms=[M.smul(M.D(sjk,a),L(b)),M.scale(M.smul(M.D(sjk,b),L(a)),-1),M.smul(M.D(sij,b),U(a)),M.scale(M.smul(M.D(sij,a),U(b)),-1)]
            actual=S.E(pair,other,oo);expected=M.scale(M.add(*terms),Q(1,2))
            self.assertEqual(actual,expected)
            for term in terms:
                wrong=M.add(expected,M.scale(term,-1))
                self.assertNotEqual(actual,wrong)
    def test_partition_formula_small_artificial(self):
        ex=Numbers()
        # Independently expand multinomial first-hit, then endpoint binomial.
        for tag in (0,8,10,14,15):
            bits=[(tag>>(3-i))&1 for i in range(4)];s=sum(bits);z=[Q(1,(2,3,5,7)[i])if bits[i]else Q((2,3,5,7)[i])for i in range(4)]
            v=[sum(math.prod(z[i]for i in range(4)if (i in a)!=bool(bits[i]))for a in itertools.combinations(range(4),k))for k in range(5)]
            finite=[i for i in range(4)if not bits[i]]
            H=[sum(math.prod(z[i]**a for i,a in zip(finite,ns))for ns in itertools.product(range(k+1),repeat=len(finite))if sum(ns)==k)for k in range(s+1)]
            cs=[(-1)**(s-j)*H[s-j]for j in range(s+1)];T=5;L=(s+1)*4+1;B=[]
            for j in range(s+1):
                total=Q(0)
                for ns in P.compositions(L,s+1):
                    if ns[j]<T or any(ns[i]>=T for i in range(j)):continue
                    total+=Q(math.factorial(L),math.prod(math.factorial(n)for n in ns))*math.prod(cs[i]**n*v[i]**(n-(T if i==j else 0))for i,n in enumerate(ns))
                B.append(total)
            prod=math.prod(v);h=[a**5-prod for a in v];aux=v[0]*v[1]*v[3]*v[4]
            for b in range(6):
                carrier=B[b]*h[b]if b<=s else sum(B[j]*v[2]*aux**0 for j in range(s+1))*aux if b==5 else 0
                for mask in (0,15):
                    line=math.prod((1-z[i]**2)if(mask>>i)&1 else z[i]**2 for i in range(4)if bits[i])
                    if any(((mask>>i)&1)and not bits[i]for i in range(4)):line=0
                    got=P.outer_weight(ex,SimpleNamespace(standard_tag=tag,carrier=b,legal_mask=mask),N=1,n=1).v
                    self.assertEqual(got,carrier*line)
    def test_first_hit_not_last_hit(self):
        ex=Numbers();cs=[ex.scalar(2),ex.scalar(3)];vs=[ex.scalar(5),ex.scalar(7)]
        a=P.first_hit(ex,cs,vs,0,2,4).v;b=P.first_hit(ex,cs,vs,1,2,4).v
        # Overlap (2,2) belongs only to first0.
        overlap=6*2**2*3**2*7**2
        self.assertNotEqual(a,b);self.assertGreater(overlap,0)
        self.assertEqual(a,overlap+4*2**3*3*5*7+2**4*5**2)
    def test_reciprocal_types_and_moving_frame(self):
        ex=RF.Execution();x,y=ex.x(0),ex.y(0);one=ex.scalar(1)
        # Generic synthetic polynomial/monomial denominators, no model input.
        for d in (x, x*x-one, x*(x*x-one),x*x+ex.scalar(2),y/x,(y/x)*(ex.y(2)/ex.x(2))):self.assertEqual(d*d.inverse(),one)
        n=y/x;Qlog=n.V(0)/n
        self.assertEqual(Qlog,y*(x*x+one)/(ex.scalar(2)*x*(x*x-one)))
        self.assertNotEqual(Qlog,y/x);self.assertNotEqual(Qlog,y/(x*(x*x-one)))
    def test_frame_and_whole_laurent_division(self):
        ex=RF.Execution();x=ex.x(0);one=ex.scalar(1);deck=one
        for i in range(4):deck=deck*ex.y(i)
        a=deck/(x+one);b=deck*x/(x+one)
        with self.assertRaises(RF.NotLaurentPolynomial):dict(a.terms)[15].laurent_coefficient((9,0,0,0))
        self.assertEqual(dict((a+b).terms)[15].laurent_coefficient((0,0,0,0)),1)
        # Artificial chart tau: J2 has tau^-4, scalar rho no twist.
        t=Q(2,3);self.assertNotEqual(t**-4,t**-2);self.assertNotEqual(t**-4,t**-8)
    def test_hard_guards_constructor_poison(self):
        class Poison:
            def __getattribute__(self,k):raise AssertionError('inspected input '+k)
        bad=Poison()
        with patch.object(RF,'Execution',side_effect=AssertionError('Execution')),patch.object(I,'FullOwner',side_effect=AssertionError('owner')):
            for f in (lambda:P.actual_route30(bad),lambda:P._actual_body(bad),lambda:E.PhysicalModel(bad,bad),lambda:E.PhysicalModel._build_body(bad,bad,bad),lambda:P.weighted_assignment(bad,bad,bad),lambda:P.outer_weight(bad,bad),lambda:P.first_hit(bad,bad,bad,0,535,2671),lambda:next(P.potential_owners(bad,bad))):
                with self.assertRaises(I.PhysicalAdmissionMissing):f()
            import bindings
            with self.assertRaises(I.PhysicalAdmissionMissing):bindings.actual_model()
    def test_cardinality_only(self):
        with patch.object(I,'FullOwner',side_effect=AssertionError('owner')):
            self.assertEqual([P.alphabet_count(t)for t in (0,8,12,14,15)],[2,6,16,40,32])
        self.assertEqual(24*math.prod([2,6,16,40,32]),5898240)
    def test_logical_criterion_only(self):
        self.assertEqual(P.assumed_authenticated_detector_results({30:0}),'UNDECIDED')
        self.assertEqual(P.assumed_authenticated_detector_results({30:Q(2,7)}),'NONZERO')
        self.assertEqual(P.assumed_authenticated_detector_results(dict.fromkeys(range(32),0)),'ZERO')
        for v in ({True:0},{32:0},{0:0.0}):
            with self.assertRaises(ValueError):P.assumed_authenticated_detector_results(v)

if __name__=='__main__':
    # No child may create Git/network subprocesses. Producer suite is run separately.
    with patch.object(subprocess,'Popen',side_effect=AssertionError('no subprocess in controls')):
        unittest.main(argv=[sys.argv[0]],verbosity=2)
