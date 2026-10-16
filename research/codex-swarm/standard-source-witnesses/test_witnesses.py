"""Tiny artificial degree/owner/schema controls only."""
from copy import deepcopy
from fractions import Fraction
import json
import unittest
import witnesses as W
I=W.I

def owners(tags=(0,8,12)):
    return tuple(I.FullOwner(12,('artificial-slot',j),c,m,t)for j,(c,m,t)in enumerate(zip((5,0,4),(0,3,15),tags)))

class Controls(unittest.TestCase):
    def test_exact_owned_degrees_both_pairs(self):
        a=owners();self.assertEqual(W.divisor_degree(a[0],(0,1)),(57,57,56,56))
        self.assertEqual(W.divisor_degree(a[1],(0,1)),(73,73,70,70))
        self.assertEqual(W.numerator_degree(a,(0,1)),(201,201,196,196))
        self.assertEqual(W.numerator_degree(a,(2,3)),(196,196,199,199))
    def test_all16_representation_vertices_and_both_pairs(self):
        # Every three-owner common target where all tags coincide is checked.
        for tag in range(16):
            for p in W.PAIR_ORDER:
                a=owners((tag,tag,tag));D=W.numerator_degree(a,p)
                qs=[{tuple(-c[i]if W.bits(tag)[i]else 0 for i in range(4)):1}for c in[W.divisor_degree(o,p)for o in a]]
                for e in((0,0,0,0),D):
                    out=W.synthetic_extension_control(a,p,{e:Fraction(3,7)},qs)
                    self.assertTrue(out);self.assertTrue(all(W.regular((tag,tag,tag),f,p)for f in out))
    def test_mixed_intersection_and_actual_finite_convolution(self):
        a=owners((0,8,12));p=(0,1);qs=[]
        for o in a:
            c=W.divisor_degree(o,p);base=tuple(-c[i]if W.bits(o.standard_tag)[i]else 0 for i in range(4))
            other=tuple(base[i]+(-1 if W.bits(o.standard_tag)[i]else 1)for i in range(4))
            qs.append({base:1,other:Fraction(1,2)})
        out=W.synthetic_extension_control(a,p,{(0,0,0,0):1,(1,0,0,0):-1},qs)
        self.assertTrue(out);self.assertTrue(all(W.regular((0,8,12),e,p)for e in out))
    def test_uniform_degree_does_not_replace_exact_owned_degree(self):
        a=owners((15,15,15));p=(0,1);D=W.numerator_degree(a,p)
        qs=[{tuple(-x for x in W.divisor_degree(o,p)):1}for o in a]
        wrong=(D[0]+1,D[1],D[2],D[3]) # below217 uniformly but invalid locally
        self.assertLess(wrong[0],217)
        with self.assertRaises(ValueError):W.synthetic_extension_control(a,p,{wrong:1},qs)
    def test_common_local_division_without_extension_rejected(self):
        a=owners((15,15,15));p=(0,1)
        qs=[{tuple(-x for x in W.divisor_degree(o,p)):1}for o in a]
        e=next(iter(qs[0]));qs[0]={tuple(x+(i==0)for i,x in enumerate(e)):1}
        with self.assertRaises(ValueError):W.synthetic_extension_control(a,p,{(0,0,0,0):1},qs)
    def test_proposal_indices_and_candidate_are_never_admission(self):
        x=W.proposal(owners(),(0,1));self.assertFalse(W.validate_proposal(x)['admitted'])
        self.assertTrue(W.validate_proposal(json.loads(json.dumps(x)))['shape_valid'])
        x['obligations']['actual_homogeneous_P_identity']={'status':'candidate','candidate_proof_sha256':'a'*64}
        self.assertFalse(W.validate_proposal(x)['actual_source_identity_accepted'])
        x['obligations']['actual_homogeneous_P_identity']['status']='verified'
        with self.assertRaises(ValueError):W.validate_proposal(x)
    def test_mutations_rejected(self):
        base=W.proposal(owners(),(0,1))
        for mutate in(lambda x:x.update(admitted=True),lambda x:x.update(admitted=0),
            lambda x:x.update(extension_scope='common_local_only'),
            lambda x:x['numerator_degree'].__setitem__(0,217),
            lambda x:x['owners'][0].__setitem__(4,False),
            lambda x:x['target_standard_tags'].__setitem__(0,False),
            lambda x:x['source_sorted_owners'][0].__setitem__(0,False),
            lambda x:x['owners'][1].__setitem__(1,x['owners'][0][1]),
            lambda x:x.update(source_sorting_sign=-x['source_sorting_sign'])):
            x=deepcopy(base);mutate(x)
            with self.assertRaises(ValueError):W.validate_proposal(x)
    def test_physical_gate_and_inexact_coefficients(self):
        with self.assertRaises(I.PhysicalAdmissionMissing):W.require_actual_admission(W.proposal(owners(),(0,1)))
        with self.assertRaises(I.PhysicalAdmissionMissing):W.synthetic_extension_control(owners(),(0,1),{},[{}, {}, {}],mode='physical')
        with self.assertRaises(ValueError):W.synthetic_extension_control(owners(),(0,1),{(0,0,0,0):True},[{}, {}, {}])

if __name__=='__main__':unittest.main()
