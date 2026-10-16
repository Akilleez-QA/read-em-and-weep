"""Bounded artificial cochains and polynomials; no physical source payload."""
from collections import defaultdict
from fractions import Fraction as Q
import itertools
import unittest
from unittest.mock import patch
import standard as S
I=S.I
E=(0,0,0,0)
H=(-1,-1,0,0)


def exact_fixture(exponent=E):
    t={(0,8):Q(1),(0,12):Q(2)};F={}
    for tri in itertools.combinations(range(16),3):
        z=sum((-1)**j*t.get(tri[:j]+tri[j+1:],0)for j in range(3))
        if z:F[tri]={exponent:z}
    return F


def harmonic_fixture():
    data={}
    for tri in itertools.combinations(range(16),3):
        z=sum(z for z,c in S.aw_cells(tri)if c[:2]==('C','C')and all(s in('A','B')for s in c[2:]))
        if z:data[tri]={H:Q(z)}
    return data


def output_edge(a,b):return(I.FullOwner(0,('output',0),0,0,a),I.FullOwner(0,('output',1),1,0,b))


class ToyCleared:
    mode='synthetic'
    def __init__(self,whole):self.whole=whole;self.calls=[]
    def degree_upper(self,owners,pair=(0,1)):
        if pair!=(0,1):raise ValueError('pair')
        return(3,3,0,0)
    def coefficient(self,owners,e,pair=(0,1)):
        if pair!=(0,1):raise ValueError('pair')
        sorted_owners,z=I.sorted_source(owners)
        if tuple(owners)!=sorted_owners:raise ValueError('source ordering')
        if min(e)<0:raise ValueError('polynomial exponent')
        self.calls.append((tuple(o.data()for o in owners),e))
        # Each owned artificial C=x0*x1; product of three shifts by(3,3,0,0).
        old=tuple(e[j]-(3 if j<2 else 0)for j in range(4))
        return self.whole.coefficient(tuple(o.standard_tag for o in owners),old)


class ToyQuotient:
    mode='synthetic'
    def factor_terms(self,owner,pair=(0,1)):
        if pair!=(0,1):raise ValueError('pair')
        return[((-1,-1,0,0),Q(1,2))] # C*Qhat=rho=1/2, exactly two fibers


class ToyFibers:
    mode='synthetic'
    def owners(self,tag,occurrence):
        return tuple(I.FullOwner(0,occurrence,c,tag,tag)for c in(0,1))


def extension(owners,tags):
    return I.RegularExtensionWitness('synthetic','complete-artificial-PiF',tuple(tags),tuple(owners),'explicit-tiny-standard-target')


class Controls(unittest.TestCase):
    def test_AW_staircase_left_inverse_all81_cells(self):
        for cell in itertools.product('ABC',repeat=4):
            result=defaultdict(int)
            for z,s in S.stairs(cell):
                for a,c in S.aw_cells(s):result[c]+=z*a
            self.assertEqual({c:z for c,z in result.items()if z},{cell:1})
    def test_rectangle_cone_sign_and_chain_identity(self):
        self.assertEqual(S.k_chain((0,12)),{(0,4,12):-1})
        self.assertEqual(S.k_chain((4,8)),{(0,4,8):1})
        for s in itertools.combinations(range(16),3):
            left=defaultdict(int,S.boundary(S.k_chain(s)))
            for face,z in S.boundary({s:1}).items():
                for t,a in S.k_chain(face).items():left[t]+=z*a
            right=defaultdict(int,{s:1})
            for t,a in S.G_chain(s).items():right[t]-=a
            self.assertEqual({t:a for t,a in left.items()if a},{t:a for t,a in right.items()if a})
    def test_actual_both_branches_and_exact_input(self):
        F=S.SyntheticStandardCochain(exact_fixture());P=S.StandardProgram(F)
        values={edge:P.branches(edge,E)for edge in itertools.combinations(range(16),2)}
        self.assertEqual(values[(0,12)]['K'],2);self.assertEqual(values[(0,1)]['AhS'],-1)
        badK=badA=False
        for tri in itertools.combinations(range(16),3):
            components={k:sum((-1)**j*values[tri[:j]+tri[j+1:]][k]for j in range(3))for k in('K','AhS')}
            f=F.coefficient(tri,E)
            self.assertEqual(components['K']+components['AhS'],f)
            badK|=components['K']!=f;badA|=components['AhS']!=f
        self.assertTrue(badK and badA) # neither branch alone is a valid substitute
        self.assertEqual(P.harmonic_projection(),0)
    def test_nonzero_harmonic_remainder_prevents_false_exactness(self):
        F=S.SyntheticStandardCochain(harmonic_fixture());P=S.StandardProgram(F)
        self.assertEqual(P.harmonic_projection(),1)
        self.assertEqual(F.coefficient((0,8,12),H),1)
        values={edge:sum(P.branches(edge,H).values())for edge in itertools.combinations(range(16),2)}
        for tri in itertools.combinations(range(16),3):
            delta=sum((-1)**j*values[tri[:j]+tri[j+1:]]for j in range(3))
            self.assertEqual(delta,F.coefficient(tri,H)-P.harmonic_image(tri,H))
            self.assertEqual(delta,0)
        self.assertFalse(P.contract()['source_harmonic_vanishing_witness'])
    def test_h_exact_zero_boundary_and_prefix_rules(self):
        self.assertEqual(S.h_requests(('A','C','A','A'),E,twist=(0,0,0,0)),[(-1,('C','C','A','A'),E)])
        self.assertEqual(S.h_requests(('B','C','A','A'),E,twist=(0,0,0,0)),[])
        self.assertEqual(S.h_requests(('A','B','A','A'),H),[])
        # A -2 harmonic prefix MUST be C at exponent -1, never an A/B constant.
        requests=S.h_requests(('C','B','A','A'),(-1,-2,0,0))
        self.assertEqual(requests,[(-1,('C','C','A','A'),(-1,-2,0,0))])
    def test_derivative_shift_before_h_and_zero_factor(self):
        F=S.SyntheticStandardCochain(exact_fixture());P=S.StandardProgram(F)
        seen=[];original=S.h_requests
        def tracked(cell,e,*args,**kwargs):seen.append(e);return original(cell,e,*args,**kwargs)
        with patch.object(S,'h_requests',tracked):P.coefficient(output_edge(0,12),(0,0,-2,0),derivative_direction=2)
        self.assertTrue(seen);self.assertTrue(all(e==(0,0,-1,0)for e in seen))
        calls=len(P.calls);self.assertEqual(P.coefficient(output_edge(0,12),(0,0,-1,0),derivative_direction=2),0);self.assertEqual(len(P.calls),calls)
        with self.assertRaises(ValueError):P.coefficient(output_edge(0,12),E,derivative_direction=0)
    def test_factored_Pi_convolution_cleared_numerator_owners_parity(self):
        whole=S.SyntheticStandardCochain(exact_fixture());cleared=ToyCleared(whole)
        pi=S.PiCoefficientProgram(cleared,ToyQuotient(),ToyFibers(),extension)
        for tri in itertools.combinations(range(16),3):self.assertEqual(pi.coefficient(tri,E),whole.coefficient(tri,E))
        self.assertTrue(any(r['source_sign']==-1 for r in pi.trace))
        self.assertTrue(all(len({tuple(v[:2])for v in r['owners']})==3 for r in pi.trace))
        p=S.StandardProgram(pi);direct=S.StandardProgram(whole)
        for edge in((0,1),(0,12),(4,8),(3,11)):self.assertEqual(p.coefficient(output_edge(*edge),E),direct.coefficient(output_edge(*edge),E))
        calls=len(cleared.calls)
        self.assertEqual(S.StandardEdgeOracle(p).bind(output_edge(0,1)).support_box(),((-3,-3,0,0),E))
        self.assertEqual(len(cleared.calls),calls) # metadata-only, no numerator values
    def test_F34_harmonic_structure_without_source_order_claim(self):
        H34=(0,0,-1,-1);data={}
        for tri in itertools.combinations(range(16),3):
            z=sum(z for z,c in S.aw_cells(tri)if c[2:]==('C','C')and all(t in('A','B')for t in c[:2]))
            if z:data[tri]={H34:Q(z)}
        F=S.SyntheticStandardCochain(data,twist=S.F34_TWIST);P=S.StandardProgram(F)
        self.assertEqual(P.pair,(2,3));self.assertEqual(P.harmonic_projection(),1)
        values={edge:sum(P.branches(edge,H34).values())for edge in itertools.combinations(range(16),2)}
        for tri in itertools.combinations(range(16),3):
            delta=sum((-1)**j*values[tri[:j]+tri[j+1:]]for j in range(3))
            self.assertEqual(delta,F.coefficient(tri,H34)-P.harmonic_image(tri,H34))
        with self.assertRaises(ValueError):P.coefficient(output_edge(0,1),E,derivative_direction=2)
        self.assertEqual(P.coefficient(output_edge(0,1),E,derivative_direction=0),0)
    def test_standard_extension_not_common_local_claim(self):
        with self.assertRaises(ValueError):S.SyntheticStandardCochain({(0,1,2):{(-1,0,0,0):1}})
        weak=lambda owners,tags:I.RegularExtensionWitness('synthetic','x',tuple(tags),tuple(owners),'d',scope='common_local_only')
        pi=S.PiCoefficientProgram(ToyCleared(S.SyntheticStandardCochain({})),ToyQuotient(),ToyFibers(),weak)
        with self.assertRaises(ValueError):pi.coefficient((0,1,2),E)
    def test_source_repeat_zero_not_generic_common_cochain_rule(self):
        class Repeated(ToyFibers):
            def owners(self,tag,occurrence):return(I.FullOwner(0,occurrence,0,0,tag),)
        oracle=ToyCleared(S.SyntheticStandardCochain(exact_fixture()));pi=S.PiCoefficientProgram(oracle,ToyQuotient(),Repeated(),extension)
        self.assertEqual(pi.coefficient((0,8,12),E),0);self.assertFalse(oracle.calls)
        # Different standard tags with equal physical labels are still a real
        # common cochain edge. Only the SOURCE F pullback received that zero rule.
        p=S.StandardProgram(S.SyntheticStandardCochain(exact_fixture()))
        self.assertNotEqual(p.coefficient((I.FullOwner(0,'a',0,0,0),I.FullOwner(0,'b',0,0,1)),E),0)
    def test_output_restriction_reversed_equal_tags_and_support_adapter(self):
        P=S.StandardProgram(S.SyntheticStandardCochain(exact_fixture()));O=S.StandardEdgeOracle(P)
        self.assertEqual(P.coefficient(output_edge(1,0),E),-P.coefficient(output_edge(0,1),E))
        calls=len(P.calls);self.assertEqual(P.coefficient(output_edge(0,0),E),0);self.assertEqual(len(P.calls),calls)
        self.assertEqual(O.support_box(output_edge(0,1)),(E,E))
        with self.assertRaises(ValueError):O.coefficient(output_edge(0,1),E,pair=(2,3))
    def test_physical_mode_and_boolean_inputs_rejected(self):
        bad=ToyQuotient();bad.mode='physical'
        with self.assertRaises(I.PhysicalAdmissionMissing):S.PiCoefficientProgram(ToyCleared(S.SyntheticStandardCochain({})),bad,ToyFibers(),extension)
        for value in(False,1.0):
            with self.assertRaises(ValueError):S.aw_cells((value,8))
            with self.assertRaises(ValueError):S.h_requests(('A','C','A','A'),(value,0,0,0))
        with self.assertRaises(ValueError):S.h_requests(('A','C','A','A'),E,twist=(-2,-2,False,0))
        with self.assertRaises(ValueError):S.SyntheticStandardCochain({(0,8,12):{E:True}})

if __name__=='__main__':unittest.main()
