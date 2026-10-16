"""INS-R: artificial data only; reference arithmetic does not use producer lowering."""
import hashlib
import itertools
import json
from pathlib import Path
import sys
import unittest
from dataclasses import FrozenInstanceError, replace
from fractions import Fraction as Q

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'standard-coefficients'))
from interfaces import FullOwner, RegularExtensionWitness, PhysicalAdmissionMissing, sorted_source
from polynomial_coefficients import Budget, Ring, Catalog, ClearedSourceProgram
from source_program import ProgramOracle, actual_program_definition, pair_nodes
from inserted_program import (ZERO, SparseOracle, ProductOracle, SumOracle,
    DerivativeOracle, SourceSlice, SyntheticFibers, SyntheticQuotients,
    PrismProgram, WholeNumerator, DifferentiatedCombinedNumerator, RequestContext)
import standard as S


def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items(): out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}


def mul(*polys):
    out = {ZERO: Q(1)}
    for p in polys:
        terms = []
        for a, x in out.items():
            for b, y in p.items(): terms.append({tuple(i+j for i,j in zip(a,b)): x*y})
        out = add(*terms)
    return out


def scale(p, c): return {e: c*v for e,v in p.items() if c*v}
def deriv(p, axis):
    return {tuple(n-int(j==axis) for j,n in enumerate(e)): c*e[axis]
            for e,c in p.items() if e[axis]}
def mono(axis, power=1): return {tuple(power if j==axis else 0 for j in range(4)): Q(1)}
def owner(i, c, m=0, t=0): return FullOwner(701, ('outer',i), c,m,t)
def parity(owners):
    keys=[o.source_key for o in owners]
    return (-1)**sum(keys[i]>keys[j] for i in range(len(keys)) for j in range(i+1,len(keys)))


class ToySource:
    mode='synthetic'
    def __init__(self): self.calls=[]
    def polynomial(self, owners, pair):
        # Deliberately slot-sensitive. A second sorting/sign or owner loss changes it.
        c=1+sum((j+1)*(o.carrier+2*o.legal_mask+3*o.standard_tag) for j,o in enumerate(owners))
        return {ZERO: Q(c), tuple(int(j==pair[0]) for j in range(4)): Q(2)}
    def degree_upper(self, owners, pair=(0,1)): return tuple(int(j==pair[0]) for j in range(4))
    def coefficient(self, owners, e, pair=(0,1)):
        if tuple(owners)!=tuple(sorted(owners,key=lambda o:o.source_key)): raise ValueError('unsorted')
        self.calls.append((owners,e,pair))
        if len({o.physical_key for o in owners})<3: return Q(0)
        return self.polynomial(owners,pair).get(e,Q(0))


class Independent(unittest.TestCase):
    def check_poly(self, oracle, expected, ranges):
        for e in itertools.product(*ranges):
            self.assertEqual(oracle.coefficient(e),expected.get(e,Q(0)),e)

    def test_handoff_hashes(self):
        manifest=json.loads((HERE/'producer-ready.json').read_text())
        self.assertFalse(manifest['physical_admission'])
        self.assertFalse(manifest['execution_release'])
        for name,digest in manifest['files'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest,name)

    def test_independent_sparse_lowering(self):
        r=Ring('synthetic',Budget())
        elementary=[]
        for k in range(5):
            elementary.append({tuple(int(i in subset) for i in range(4)):Q(1)
                               for subset in itertools.combinations(range(4),k)})
        # Mixed powers and derivative after elementary substitution, including rational cancellation.
        p=mul(elementary[1],elementary[2],elementary[2])
        expected=add(scale(deriv(p,2),Q(-3,7)), elementary[4])
        node=r.plus(r.times(r.const(Q(-3,7)),r.partial(r.times(r.elementary(1),r.power(r.elementary(2),2)),2)),r.elementary(4))
        for e in itertools.product(range(4),repeat=4):
            self.assertEqual(r.coefficient(node,e),expected.get(e,Q(0)),e)
        self.assertEqual(r.coefficient(node,(-1,0,0,0)),0)
        self.assertEqual(r.coefficient(r.power(r.const(0),0),ZERO),1)
        self.assertIsNone(r.bound(r.partial(r.x(0),1)))
        with self.assertRaises(ValueError): r.power(r.x(0),-1)

    def test_source_sorting_and_raw_F34_with_order_reversal(self):
        # Same carrier masks 1<2<4 map to 4,8,1; target inverse-image is unsorted.
        definition={'dag':[['owned_polynomial_factor',[0,'ell',0]],
            ['owned_polynomial_factor',[1,'ell',1]],['scale',3,1,1],
            ['sum',0,2],['polynomial_partial_after_elementary_substitution',3,0]],'cleared_P':4}
        cat=Catalog('synthetic',[],{})
        source=ProgramOracle(definition,cat)
        target=(owner(0,1,1,8),owner(1,1,2,12),owner(2,1,4,15))
        # Fresh target F34: slot0 bit2=0 => derivative is zero. Inverse sorting
        # moves mask4 into slot0 and gives 3*x2^2-1, an invalid cochain transfer.
        self.assertEqual(source.coefficient(target,ZERO,(2,3)),0)
        inverse=tuple(FullOwner(o.seed,o.occurrence,o.carrier,((o.legal_mask&3)<<2)|(o.legal_mask>>2),o.standard_tag) for o in target)
        self.assertNotEqual(inverse,sorted_source(inverse)[0])
        self.assertNotEqual(source.alternating_coefficient(inverse,ZERO),0)
        self.assertEqual(pair_nodes(pair_nodes(definition['dag'],(2,3)),(2,3)),definition['dag'])
        # Auxiliary first; full identities survive all six permutations and exactly one sign.
        owners=(owner(0,5,7,15),owner(1,1,1,8),owner(2,1,4,12))
        toy=ToySource()
        for p in itertools.permutations(owners):
            sl=SourceSlice(toy,p,(2,3))
            self.assertEqual(sl.coefficient(ZERO),parity(p)*toy.polynomial(owners,(2,3))[ZERO])
            self.assertEqual(toy.calls[-1][0],owners)
        # Actual pinned topology/proof authenticated, no physical program evaluation.
        authentic,physical_catalog=actual_program_definition(HERE.parents[2])
        self.assertEqual(len(authentic['dag']),153)
        self.assertEqual(authentic['cleared_P'],152)
        physical=ProgramOracle(authentic,physical_catalog)
        for pair,bound in [((0,1),(217,217,210,210)),((2,3),(210,210,217,217))]:
            maximizers=tuple(owner(i,i+1,15,i) for i in range(3))
            self.assertEqual(physical.degree_upper(maximizers,pair),bound)
            for e in [ZERO,(-1,0,0,0),(1000,0,0,0)]:
                with self.assertRaises(PhysicalAdmissionMissing): physical.coefficient(owners,e,pair)

    def test_authentic_topology_with_zero_artificial_matrices(self):
        definition,_=actual_program_definition(HERE.parents[2])
        charts=[{'I':[[[],[]],[[],[]]],'P':[[[],[]],[[],[]]]} for _ in range(6)]
        catalog=Catalog('synthetic',charts,{i:{ZERO:Q(1)} for i in range(6)})
        oracle=ProgramOracle(definition,catalog)
        for pair,masks in [((0,1),(0,1,2)),((2,3),(0,4,8))]:
            owners=tuple(owner(i,i,m) for i,m in enumerate(masks))
            # Zero trace; only 15/4*q01,i*q12,j remains. H=1, exactly
            # one active legal factor at each pair axis cancels the x denominator.
            expected=scale(mul(add(mono(pair[0],2),{ZERO:Q(-1)}),
                               add(mono(pair[1],2),{ZERO:Q(-1)})),Q(15,4))
            for e in itertools.product(range(3),repeat=4):
                self.assertEqual(oracle.coefficient(owners,e,pair),expected.get(e,0),e)
        # Physical-source repetition is zero despite distinct occurrence and tag.
        repeated=(owner(0,1,0,0),owner(1,1,0,8),owner(2,2,0,12))
        self.assertEqual(oracle.coefficient(repeated,ZERO),0)

    def test_artificial_catalog_elementary_substitution_and_auxiliary_multiplier(self):
        elementary=[]
        for k in range(5):
            elementary.append({tuple(int(i in subset) for i in range(4)):Q(1)
                               for subset in itertools.combinations(range(4),k)})
        stored=[['2,0,0,0',Q(2,3)],['0,1,0,0',-2]]
        charts=[{'P':[[stored]],'I':[[stored]]} for _ in range(6)]
        h=add({ZERO:Q(1)},mono(0))
        catalog=Catalog('synthetic',charts,{i:h for i in range(6)})
        numerator=add(scale(mul(elementary[1],elementary[1]),Q(2,3)),scale(elementary[2],-2))
        for carrier in [1,5]:
            r=Ring('synthetic',Budget())
            root=catalog.cleared(owner(0,carrier),'P',r)[0][0].node
            multiplier=scale(h,-1) if carrier==1 else scale(mul(elementary[3],elementary[4]),-1)
            expected=mul(multiplier,numerator)
            for e in itertools.product(range(4),repeat=4):
                self.assertEqual(r.coefficient(root,e),expected.get(e,0),(carrier,e))

    def test_ordered_matrix_catalog_lowering(self):
        r=Ring('synthetic',Budget())
        # Arbitrary artificial matrices; expected order computed independently.
        A=[[{ZERO:1},mono(0)],[{}, {ZERO:2}]]
        B=[[{}, {ZERO:3}],[{ZERO:1}, {}]]
        C=[[{ZERO:2},{}],[mono(1),{ZERO:1}]]
        def mm(a,b):
            return [[add(*(mul(a[i][k],b[k][j]) for k in range(2)))
                     for j in range(2)] for i in range(2)]
        AB=mm(A,B); BA=mm(B,A)
        from polynomial_coefficients import Scalar, times
        def lower(a):return [[Scalar(r.polynomial(p)) for p in row] for row in a]
        product=times(times(lower(A),lower(B),r),lower(C),r)
        expected=mm(AB,C)
        self.assertNotEqual(expected,mm(BA,C))
        for i,j in itertools.product(range(2),repeat=2):
            for e in itertools.product(range(2),repeat=4):
                self.assertEqual(r.coefficient(product[i][j].node,e),expected[i][j].get(e,0))

    def fixture(self,pair=(0,1),box=None):
        budget=Budget(max_queries=1000000,max_splits=1000000,max_owner_terms=200000)
        a,b=owner(1,2,1,8),owner(2,4,2,12)
        fibers=SyntheticFibers(701,{8:[(5,3),(1,4)],12:[(0,5),(3,6)]})
        qdata={(5,3,8):{ZERO:Q(2),(-1,0,0,0):Q(1,2)},
               (1,4,8):{(0,1,0,0):Q(-1)},
               (0,5,12):{ZERO:Q(3)},(3,6,12):{(1,0,0,0):Q(2)}}
        q=SyntheticQuotients(qdata); src=ToySource()
        ca={ZERO:Q(1),(1,0,0,0):Q(2)}; cb={ZERO:Q(3),(0,1,0,0):Q(-1)}
        B={ZERO:Q(5),(0,0,1,0):Q(7)}; Z=(1,0,0,0)
        w=RegularExtensionWitness('synthetic','whole-artificial',(8,12),(a,b),'artificial-domain')
        prefix,last=owner(0,5,0,0),owner(3,0,0,15)
        outer=(prefix,a,b,last)
        context=RequestContext(outer,(prefix,),outer)
        prism=PrismProgram((a,b),src,q,fibers,SparseOracle(ca,budget),Z,w,budget,context,pair)
        # Independent expanded reference on four artificial owner combinations only.
        p1={}; p2={}
        us=fibers.owners(8,('inserted',a.occurrence,b.occurrence,'u'))
        vs=fibers.owners(12,('inserted',a.occurrence,b.occurrence,'v'))
        def source_poly(os):
            ordered=tuple(sorted(os,key=lambda o:o.source_key))
            return scale(src.polynomial(ordered,pair),parity(os))
        for u in us:
            U=qdata[u.common_key]
            p1=add(p1,mul({Z:Q(1)},U,source_poly((u,a,b))))
            for v in vs:
                p2=add(p2,scale(mul(ca,{Z:Q(1)},U,qdata[v.common_key],source_poly((u,v,b))),-1))
        standard=mul(ca,cb,{Z:Q(1)},B)
        N=WholeNumerator(SparseOracle(B,budget),prism,SparseOracle(cb,budget),box or ((0,0,0,0),(4,2,1,1)))
        return budget,a,b,prism,N,p1,p2,add(standard,p1,p2),ca,cb

    def test_both_prisms_whole_derivative_and_owned_multiplicities(self):
        for pair in [(0,1),(2,3)]:
            budget,a,b,p,N,p1,p2,expected,ca,cb=self.fixture(pair)
            grid=[range(-1,5),range(4),range(3),range(2)]
            for e in itertools.product(*grid):
                self.assertEqual(p.coefficient('prism1',e),p1.get(e,0),('first',pair,e))
                self.assertEqual(p.coefficient('prism2',e),p2.get(e,0),('second',pair,e))
            self.check_poly(N,expected,grid)
            # Same polynomial, separate owner and multiplicity: Delta=f*f*g.
            f=SparseOracle(ca,budget); g=SparseOracle(cb,budget)
            factors=[(a,'f',2,f),(b,'f',3,f),(a,'g',1,g)]
            delta=mul(ca,ca,cb)
            dlog=add(scale(mul(deriv(ca,0),ca,cb),5),mul(ca,ca,deriv(cb,0)))
            want=add(mul(delta,deriv(expected,0)),scale(mul(expected,dlog),-1))
            D=DifferentiatedCombinedNumerator(N,factors,0,budget)
            self.check_poly(D,want,[range(-2,7),range(4),range(2),range(2)])
            self.assertEqual(len(D.denominator_description['Delta']),3)
            with self.assertRaises(ValueError): DifferentiatedCombinedNumerator(p,factors,0,budget)
            with self.assertRaises(ValueError): DifferentiatedCombinedNumerator(N,factors+[factors[0]],0,budget)
            for os,e,seen_pair in p.source.calls:
                self.assertEqual(seen_pair,pair)
                self.assertEqual(tuple(sorted(os,key=lambda o:o.source_key)),os)
                for o in os:
                    self.assertEqual(o.seed,701)
                    if o not in (a,b):
                        self.assertEqual(o.occurrence,('inserted',a.occurrence,b.occurrence,'u' if o.standard_tag==8 else 'v'))

    def test_standard_endpoint_both_branches_and_padding(self):
        self.assertIs(S.I.FullOwner,FullOwner)
        # delta t, t_(0,8)=1, t_(0,12)=2, so extension holds on all triples.
        data={}
        for s in itertools.combinations(range(16),3):
            t={(0,8):1,(0,12):2}
            c=t.get(s[1:],0)-t.get((s[0],s[2]),0)+t.get(s[:2],0)
            if c:data[s]={ZERO:Q(c)}
        endpoint=S.StandardProgram(S.SyntheticStandardCochain(data))
        a,b=owner(1,2,0,0),owner(2,4,0,12)
        self.assertEqual(endpoint.branches((0,12),ZERO)['K'],2)
        self.assertEqual(endpoint.branches((0,1),ZERO)['AhS'],-1)
        budget,_,_,p,_,p1,p2,_,ca,cb=self.fixture()
        # Use exact edge owners for both programs; B is the full K+AhS endpoint.
        a,b=p.edge
        bound=S.StandardEdgeOracle(endpoint).bind((a,b))
        B=endpoint.branches((8,12),ZERO)
        self.assertEqual(bound.coefficient(ZERO),sum(B.values()))
        N=WholeNumerator(bound,p,SparseOracle(cb,budget),((-1,0,0,0),(5,5,1,1)))
        expected=add(mul(ca,cb,{p.Z:sum(B.values())}),p1,p2)
        self.check_poly(N,expected,[range(-1,5),range(4),range(2),range(2)])

    def test_enclosure_is_trusted_obligation_not_certificate(self):
        budget,a,b,p,N,p1,p2,expected,ca,cb=self.fixture()
        lo,hi=N.support_box()
        for e in expected:self.assertTrue(all(l<=x<=h for l,x,h in zip(lo,e,hi)))
        # Understated boxes silently lose convolution terms. This negative control
        # is intentional evidence for the documented caller enclosure obligation.
        class Understated:
            mode='synthetic'
            def coefficient(self,e):return Q(1) if e in (ZERO,(2,0,0,0)) else Q(0)
            def support_box(self):return ZERO,ZERO
        identity=SparseOracle({ZERO:1},budget)
        self.assertEqual(Understated().coefficient((2,0,0,0)),1)
        self.assertEqual(ProductOracle([Understated(),identity],budget).coefficient((2,0,0,0)),0)
        # A whole N with omitted prism support similarly hides genuine terms.
        bad=WholeNumerator(SparseOracle({},budget),p,SparseOracle(cb,budget),None)
        self.assertIsNone(bad.support_box())
        e=next(e for e,c in add(p1,p2).items() if c)
        self.assertNotEqual(bad.coefficient(e),0)
        self.assertEqual(ProductOracle([bad,identity],budget).coefficient(e),0)

    def test_witness_context_and_physical_refusal_all_layers(self):
        budget,a,b,p,N,*_=self.fixture()
        for scope in ['common_local_only','']:
            p.witness=RegularExtensionWitness('synthetic','toy',(8,12),(a,b),'toy',scope)
            with self.assertRaises(ValueError):p.coefficient('prism1',ZERO)
        for owners,tags in [((b,a),(8,12)),((a,b),(12,8))]:
            w=RegularExtensionWitness('synthetic','toy',(8,12),(a,b),'toy')
            with self.assertRaises(ValueError):w.require(owners,tags)
        for context in [RequestContext(p.context.outer,p.context.prefix,()),
                        RequestContext(p.context.outer,(b,),p.context.outer)]:
            with self.assertRaises(ValueError):context.validate((a,b))
        # Test each public execution wrapper before any negative-exponent shortcut.
        f=SparseOracle({ZERO:1},budget); f.mode='physical'
        objects=[f,ProductOracle([f],budget),SumOracle([(1,f)],budget),DerivativeOracle(f,0)]
        physical_source=ToySource();physical_source.mode='physical'
        objects.append(SourceSlice(physical_source,(owner(0,0),a,b)))
        for obj in objects:
            for e in [ZERO,(-1,0,0,0)]:
                with self.assertRaises(PhysicalAdmissionMissing):obj.coefficient(e)
        p.mode='physical';N.mode='physical'
        objects.append(DifferentiatedCombinedNumerator(N,[(a,'toy',1,f)],0,budget))
        for e in [ZERO,(-1,0,0,0)]:
            with self.assertRaises(PhysicalAdmissionMissing):objects[-1].coefficient(e)
        for e in [ZERO,(-1,0,0,0)]:
            with self.assertRaises(PhysicalAdmissionMissing):p.coefficient('prism1',e)
            with self.assertRaises(PhysicalAdmissionMissing):N.coefficient(e)
        r=Ring('physical',Budget());node=r.const(1)
        with self.assertRaises(PhysicalAdmissionMissing):r.coefficient(node,(-1,0,0,0))

    def test_caps_and_non_enclosure_inputs(self):
        b=Budget(max_queries=1)
        f=SparseOracle({ZERO:1},b)
        self.assertEqual(f.coefficient(ZERO),1)
        with self.assertRaises(ValueError):f.coefficient(ZERO)
        b=Budget(max_splits=0)
        f=SparseOracle({ZERO:1},b)
        with self.assertRaises(ValueError):ProductOracle([f,f],b).coefficient(ZERO)
        for args in [(1,'x',True,0,0),(1,'x',1,True,0),(1,'x',1,0,True)]:
            with self.assertRaises(ValueError):FullOwner(*args)
        budget,a,b,p,*_=self.fixture()
        with self.assertRaises(ValueError):WholeNumerator(SparseOracle({},budget),p,SparseOracle({},budget),((1,0,0,0),ZERO))

    def test_external_fiber_occurrence_premise_is_not_validated(self):
        # Historical test name retained; INS-R follow-up now requires rejection.
        budget,a,b,p,*_=self.fixture()
        class WrongOccurrence:
            mode='synthetic'
            def owners(self,tag,occurrence):
                return (FullOwner(999,'wrong-occurrence',5 if tag==8 else 0,3 if tag==8 else 5,tag),)
        p.fibers=WrongOccurrence()
        with self.assertRaisesRegex(ValueError,'inserted fiber full owner binding'):
            p.coefficient('prism2',ZERO)
        self.assertEqual(p.source.calls,[])

    def test_external_fiber_binding_controls_both_slots(self):
        for slot,kind in [('u','prism1'),('u','prism2'),('v','prism2')]:
            for defect in ['seed','occurrence','swapped-slot','tag','type','duplicate']:
                with self.subTest(slot=slot,kind=kind,defect=defect):
                    _,a,b,p,*_=self.fixture()
                    bundled=p.fibers
                    requests=[]
                    quotient_calls=[]
                    original_terms=p.quotient.factor_terms
                    def terms(o,pair):
                        quotient_calls.append(o)
                        return original_terms(o,pair)
                    p.quotient.factor_terms=terms
                    class Provider:
                        mode='synthetic'
                        def owners(self,tag,occurrence):
                            requests.append((tag,occurrence))
                            values=bundled.owners(tag,occurrence)
                            if occurrence[-1]!=slot:return iter(values)
                            good=values[0]
                            bad={'seed':lambda:replace(good,seed=999),
                                 'occurrence':lambda:replace(good,occurrence='wrong'),
                                 'swapped-slot':lambda:replace(good,occurrence=occurrence[:-1]+('v' if slot=='u' else 'u',)),
                                 'tag':lambda:replace(good,standard_tag=12 if tag==8 else 8),
                                 'type':lambda:good.data(),
                                 'duplicate':lambda:replace(good)}[defect]()
                            # Even a valid prefix must not reach arithmetic before
                            # the entire returned fiber passes validation.
                            return (x for x in (good,bad))
                    p.fibers=Provider()
                    message='duplicate inserted fiber label' if defect=='duplicate' else 'inserted fiber full owner binding'
                    with self.assertRaisesRegex(ValueError,message):p.coefficient(kind,ZERO)
                    self.assertEqual(p.source.calls,[])
                    self.assertFalse(any(o.standard_tag==(8 if slot=='u' else 12) for o in quotient_calls))
                    self.assertIn((8 if slot=='u' else 12,
                        ('inserted',a.occurrence,b.occurrence,slot)),requests)

    def test_same_seed_edge_required_at_construction(self):
        _,a,b,p,*_=self.fixture()
        for edge in [(replace(a,seed=999),b),(a,replace(b,seed=999))]:
            with self.assertRaisesRegex(ValueError,'edge request seed mismatch'):
                PrismProgram(edge,p.source,p.quotient,p.fibers,p.C_a,p.Z,
                             p.witness,p.budget)

    def test_conforming_generator_preserves_full_unsorted_owners(self):
        _,a,b,p,_,p1,p2,*_=self.fixture()
        bundled=p.fibers
        delivered=[]
        quotient_owners=[]
        original_terms=p.quotient.factor_terms
        class Provider:
            mode='synthetic'
            def owners(self,tag,occurrence):
                values=bundled.owners(tag,occurrence)
                delivered.extend(values)
                return (o for o in values)
        def terms(o,pair):
            self.assertTrue(any(o is supplied for supplied in delivered))
            quotient_owners.append(o)
            return original_terms(o,pair)
        p.fibers=Provider();p.quotient.factor_terms=terms
        for e in itertools.product(range(-1,5),range(4),range(2),range(2)):
            self.assertEqual(p.coefficient('prism1',e),p1.get(e,0))
            self.assertEqual(p.coefficient('prism2',e),p2.get(e,0))
        self.assertEqual([o.common_key for o in quotient_owners[:2]],[(5,3,8),(1,4,8)])
        for os,_,_ in p.source.calls:
            for o in os:
                self.assertTrue(o is a or o is b or any(o is supplied for supplied in delivered))

    def test_fiber_cap_bounds_generator_consumption(self):
        for slot,kind in [('u','prism1'),('u','prism2'),('v','prism2')]:
            for count in [4096,4097,None]:
                with self.subTest(slot=slot,kind=kind,count=count):
                    _,_,_,p,*_=self.fixture()
                    bundled=p.fibers
                    consumed=[]
                    class Provider:
                        mode='synthetic'
                        def owners(self,tag,occurrence):
                            values=bundled.owners(tag,occurrence)
                            if occurrence[-1]!=slot:return iter(values)
                            def stream():
                                for i in itertools.count():
                                    if count is not None and i==count:return
                                    consumed.append(i)
                                    yield values[0]
                            return stream()
                    p.fibers=Provider()
                    # Only 6*16 distinct labels exist per fixed tag, so a
                    # 4096-element valid unique FullOwner fiber is impossible.
                    message='duplicate inserted fiber label' if count==4096 else 'finite fiber provider cap'
                    with self.assertRaisesRegex(ValueError,message):p.coefficient(kind,ZERO)
                    self.assertEqual(len(consumed),4096 if count==4096 else 4097)
                    self.assertEqual(p.source.calls,[])

    def test_full_owner_normalizes_and_freezes_occurrence(self):
        supplied=['inserted',['outer',1],['outer',2],'u']
        o=FullOwner(701,supplied,5,3,8)
        supplied[1][1]=999
        self.assertEqual(o.occurrence,('inserted',('outer',1),('outer',2),'u'))
        self.assertEqual(hash(o),hash(FullOwner(*o.data())))
        for field,value in [('seed',999),('occurrence','changed'),('carrier',0),
                            ('legal_mask',4),('standard_tag',12)]:
            with self.assertRaises(FrozenInstanceError):setattr(o,field,value)
        for occurrence in [{'mutable':1},object(),('nested',{})]:
            with self.assertRaises(ValueError):FullOwner(701,occurrence,5,3,8)

    def test_fiber_completeness_remains_a_premise(self):
        _,_,_,p,*_=self.fixture()
        class EmptyProvider:
            mode='synthetic'
            def owners(self,tag,occurrence):return iter(())
        p.fibers=EmptyProvider()
        for kind in ['prism1','prism2']:self.assertEqual(p.coefficient(kind,ZERO),0)
        self.assertEqual(p.source.calls,[])

if __name__=='__main__':unittest.main()
