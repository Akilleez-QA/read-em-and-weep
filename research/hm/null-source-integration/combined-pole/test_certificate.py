import unittest
import sympy as s
from certificate import *

class UniversalAlgebra(unittest.TestCase):
    def test_combined_cancellation_then_derivative(self):
        # Three independent summands, each with a different inserted denominator.
        # Only the combined numerator is differentiated by the certificate.
        x=s.Symbol('x');d,e=s.Function('d')(x),s.Function('e')(x)
        ins=[s.Function('u'+str(j))(x) for j in range(3)]
        P=[s.Function('P'+str(j))(x) for j in range(3)]
        Q=[s.Function('Q'+str(j))(x) for j in range(3)]
        suffix=[d**2*e,d*e**2,d**2]
        signs=[1,-1,1]
        raw=sum(signs[j]*(ins[j]**14*Q[j])*P[j]/(ins[j]**14*suffix[j]) for j in range(3))
        D=d**2*e**2
        N=sum(signs[j]*Q[j]*P[j]*(D/suffix[j]) for j in range(3))
        delta=d*e
        corrected=(delta*s.diff(N,x)-N*(2*s.diff(d,x)*e+2*d*s.diff(e,x)))/(D*delta)
        self.assertEqual(s.simplify(raw-N/D),0)
        self.assertEqual(s.simplify(s.diff(raw,x)-corrected),0)
        self.assertFalse(any(corrected.has(u) for u in ins))
    def test_exact_two_prism_plus_standard_numerator(self):
        x=s.Symbol('x');Ca=s.Function('Ca')(x);Cb=s.Function('Cb')(x)
        Z=s.Function('Z')(x);B=s.Function('B')(x)
        u=[s.Function('u'+str(i))(x) for i in range(2)]
        v=[s.Function('v'+str(i))(x) for i in range(2)]
        Qu=[s.Function('Qu'+str(i))(x) for i in range(2)]
        Qv=[s.Function('Qv'+str(i))(x) for i in range(2)]
        P1=[s.Function('P1'+str(i))(x) for i in range(2)]
        P2=[[s.Function('P2'+str(i)+str(j))(x) for j in range(2)] for i in range(2)]
        raw=B+sum(u[i]*Qu[i]*P1[i]/(u[i]*Ca*Cb) for i in range(2))
        raw-=sum(u[i]*Qu[i]*v[j]*Qv[j]*P2[i][j]/(u[i]*v[j]*Cb) for i in range(2) for j in range(2))
        N=Ca*Cb*Z*B+Z*sum(Qu[i]*P1[i] for i in range(2))-Ca*Z*sum(Qu[i]*Qv[j]*P2[i][j] for i in range(2) for j in range(2))
        D=Ca*Cb*Z
        self.assertEqual(s.simplify(raw-N/D),0)
        self.assertEqual(s.simplify(s.diff(raw,x)-s.diff(N/D,x)),0)
        self.assertFalse(any(N.has(f) for f in u+v))
    def test_raw_leibniz_terms_need_cancellation(self):
        x=s.Symbol('x');u=s.Function('u')(x);P=s.Function('P')(x);Q=s.Function('Q')(x)
        left=s.diff(u**14*Q,x)*P/u**14
        right=u**14*Q*s.diff(P/u**14,x)
        self.assertEqual(s.simplify(left+right-s.diff(Q*P,x)),0)
        self.assertNotEqual(s.simplify(left-s.diff(Q,x)*P),0)
        self.assertTrue(s.cancel(left).has(1/u))
    def test_frame_identity(self):
        t=s.Symbol('t',nonzero=True)
        for n in (0,-2):
            for e in range(-8,9):
                fB=t**(n-e)
                op=-s.diff(fB,t)+n*fB/t
                # target twist n-2; derivative finite monomial e*x^(e-1).
                self.assertEqual(s.expand(op-e*t**(n-1-e)),0)
        # n=0 has no frame-connection term. n=-2 does.
        self.assertEqual(-s.diff(t**3,t),-3*t**2)
    def test_radical_denominator_general_orders(self):
        x=s.Symbol('x');d=s.Function('d')(x);e=s.Function('e')(x);N=s.Function('N')(x)
        for a in range(4):
            for b in range(4):
                D=d**a*e**b;delta=(d if a else 1)*(e if b else 1)
                correction=(a*s.diff(d,x)*(delta/d) if a else 0)+(b*s.diff(e,x)*(delta/e) if b else 0)
                self.assertEqual(s.simplify(s.diff(N/D,x)-(delta*s.diff(N,x)-N*correction)/(D*delta)),0)

class Predicates(unittest.TestCase):
    def setUp(self):
        self.a=Owner(1,0,1,0,3);self.b=Owner(1,1,2,0,11)
    def test_wrong_owner_rejected(self):
        alias=Owner(1,9,1,0,3)
        with self.assertRaises(ValueError): cancel_owned({(self.a,'H',None):14},{(alias,'H',None):14})
        self.assertEqual(cancel_owned({(self.a,'H',None):14},{(self.a,'H',None):14}),{})
    def test_no_absent_derivative_pole(self):
        self.assertEqual(derivative_orders({'H':14,'unused':0}),{'H':15})
    def test_full_geometric_duplicate_vanishes(self):
        alias=Owner(2,9,self.a.carrier,self.a.legal_mask,self.a.standard_tag)
        self.assertEqual(alternating_sort((self.a,alias,self.b))[0],0)
    def test_source_pullback_zero_across_standard_tags(self):
        alias=Owner(1,9,self.a.carrier,self.a.legal_mask,11)
        vertices=(self.a,alias,self.b)
        self.assertNotEqual(alternating_sort(vertices)[0],0)
        self.assertEqual(source_F_sort(vertices)[0],0)
        self.assertEqual(set(source_F_sort(vertices)[1]),set(vertices))
        # Equal source factors still cannot borrow another occurrence's weight.
        with self.assertRaises(ValueError):
            cancel_owned({(alias,'H',None):14},{(self.a,'H',None):14})
    def test_prism_repeated_source_is_zero(self):
        u=Owner(1,4,self.b.carrier,self.b.legal_mask,self.a.standard_tag)
        branch=prism_branch((self.a,self.b),(u,))
        self.assertTrue(active_weight(u))
        self.assertEqual(branch['sign'],0)
        self.assertIn(u,branch['source'])
    def test_standard_repetition_does_not_kill_common_edge(self):
        c=Owner(1,3,0,0,self.a.standard_tag)
        self.assertNotEqual(alternating_sort((self.a,c,self.b))[0],0)
    def test_prism_tag_and_sign(self):
        u=Owner(1,4,0,0,3);v=Owner(1,5,1,0,11)
        self.assertEqual(prism_branch((self.a,self.b),(u,))['sign'],1)
        self.assertEqual(prism_branch((self.a,self.b),(u,v))['sign'],-1)
        with self.assertRaises(ValueError): prism_branch((self.a,self.b),(v,))
    def test_raw_reversed_output_edge_rejected(self):
        u=Owner(1,4,0,0,self.b.standard_tag)
        with self.assertRaises(ValueError):prism_branch((self.b,self.a),(u,))
    def test_structural_filters_not_nonzero_claim(self):
        self.assertFalse(active_weight(Owner(0,0,0,1,0)))
        self.assertFalse(active_weight(Owner(0,0,3,0,3)))
        self.assertFalse(active_weight(Owner(0,0,1,0,15)))
        self.assertTrue(active_weight(Owner(0,0,4,0,15)))
    def test_h_boundary_and_shift(self):
        cell=('B','C','A','A');n=(0,-2,0,-2)
        self.assertIsNone(h_adjoint(cell,(0,-1,0,0),n,0))
        self.assertEqual(h_adjoint(cell,(-1,-1,0,0),n,0)[0],1)
        self.assertIsNone(differentiated_h_adjoint(cell,(-1,-1,0,0),n,0,0))
        r=differentiated_h_adjoint(cell,(-2,-1,0,0),n,0,0)
        self.assertEqual(r,(-1,('C','C','A','A'),(-1,-1,0,0)))
    def test_coupled_reversal_bounds(self):
        self.assertEqual([inserted_reversal_bound(True,m) for m in (0,1)],[553,554])
        self.assertEqual([inserted_reversal_bound(False,m) for m in (0,1)],[553,553])
        for pair in (True,False):
            for mask in (0,1):
                for degree in (4,5):self.assertGreaterEqual(5250-inserted_reversal_bound(pair,mask,degree),0)
    def test_no_absent_standard_denominator(self):
        self.assertFalse(standard_exponent_admissible((0,0),(-1,0,0,0),(-2,-2,0,0)))
        self.assertTrue(standard_exponent_admissible((0,8),(-1668,0,0,0),(-2,-2,0,0)))
        self.assertFalse(standard_exponent_admissible((15,15),(0,0,0,0),(-2,-2,0,0)))
    def test_recipe_keeps_full_sum_and_suffix_padding(self):
        r=full_sum_recipe()
        self.assertEqual(r['branches'][2]['numerator_padding'],'C_a Z_ab')
        self.assertEqual(r['inserted_negative_bounds'],{'pair':554,'complement':553})
        self.assertFalse(r['source_clearing_verified_by_this_artifact'])
    def test_support_numbers(self):
        m=support_metadata()
        self.assertEqual(m['standard_branch_finite_box'],[-1668,5248])
        self.assertEqual(m['standard_pole'],5250)
        self.assertEqual(m['raw_weight_degree'],1747)
        self.assertFalse(m['execution_admitted'])
    def test_reject_bool_labels(self):
        with self.assertRaises(ValueError):Owner(1,False,1,0,0)

if __name__=='__main__':unittest.main()
