"""Abstract small-power polynomial controls only; never evaluate physical N54."""
import copy
import unittest
from math import comb, factorial, prod
import sympy as S
import outer_partition_source_binding as p
from owned_scalar_denominator_binding import VertexLabel, label


def compositions(total,d):
    if d==1:
        yield (total,)
    else:
        for n in range(total+1):
            for tail in compositions(total-n,d-1):yield (n,)+tail

class Tests(unittest.TestCase):
    def test_metadata_all_charts(self):
        for e in range(16):
            chart=p.PartitionChart(e)
            self.assertEqual(chart.M,107)
            self.assertEqual(chart.threshold,535)
            self.assertEqual(chart.L,(chart.s+1)*534+1)
            self.assertEqual(chart.data()['line_M'],57)
        self.assertEqual(p.PartitionChart(0).L,535)
        self.assertEqual(p.PartitionChart(15).L,2671)
    def test_small_abstract_multinomial_partition(self):
        # Threshold 1..3, NOT the physical 535; generic independent symbols.
        for d in (1,2,3):
            v=S.symbols('v:'+str(d)); c=S.symbols('c:'+str(d))
            for threshold in (1,2,3):
                L=d*(threshold-1)+1
                quotients=[S.Integer(0)]*d
                for n in compositions(L,d):
                    j=next(i for i in range(d) if n[i]>=threshold)
                    self.assertTrue(all(n[i]<threshold for i in range(j)))
                    coefficient=factorial(L)//prod(factorial(ni) for ni in n)
                    chained=prod(comb(L-sum(n[:i]),n[i]) for i in range(d))
                    self.assertEqual(coefficient,chained)
                    quotients[j]+=coefficient*S.prod(c[i]**n[i]*v[i]**(n[i]-threshold*(i==j)) for i in range(d))
                self.assertEqual(S.expand(sum(v[j]**threshold*quotients[j] for j in range(d))-sum(c[i]*v[i] for i in range(d))**L),0)
    def test_small_abstract_carrier_quotients(self):
        h,v,a=S.symbols('h v a')
        for n in (1,2,3):
            M=2*n-1
            cq=sum(comb(M,k)*h**(k-n)*(v*a)**(M-k) for k in range(n,M+1))
            dq=sum(comb(M,k)*h**k*v**(M-k)*a**(M-k-n) for k in range(n))
            self.assertEqual(S.expand(h**n*cq+a**n*dq-(h+v*a)**M),0)
            self.assertTrue(S.Poly(cq,h,v,a).is_multivariate)
    def test_small_abstract_line_quotients(self):
        t=S.Symbol('t')
        for n in (1,2,3):
            M=2*n-1
            q0=sum(comb(M,k)*t**(2*k-n)*(1-t*t)**(M-k) for k in range(n,M+1))
            q1=sum(comb(M,k)*t**(2*k)*(1-t*t)**(M-k-n) for k in range(n))
            self.assertEqual(S.expand(t**n*q0+(1-t*t)**n*q1-1),0)
            self.assertLessEqual(S.degree(q0,t),2*M-n)
            self.assertLessEqual(S.degree(q1,t),2*M-2*n)
    def test_homogeneous_single_coordinate_conversion(self):
        t=S.Symbol('t',nonzero=True)
        # Generic legal equations; no source or partition evaluation.
        self.assertEqual(S.simplify(t*1-t),0)
        self.assertEqual(S.simplify(t**3*(1/t)*((1/t)**2-1)-(1-t*t)),0)
    def test_full_owners_not_merged(self):
        a=VertexLabel(7,0,2,1,9); b=VertexLabel(7,1,2,1,9)
        self.assertNotEqual(p.build_outer_partition_binding(a),p.build_outer_partition_binding(b))
        for v in (a,b,label(7,2)):
            binding=p.build_outer_partition_binding(v)
            self.assertTrue(p.validate_outer_partition_binding(binding))
            bad=copy.deepcopy(binding);bad['carrier_power']=53
            with self.assertRaises(ValueError):p.validate_outer_partition_binding(bad)
    def test_domain_fail_closed(self):
        v=VertexLabel(0,0,5,3,9)
        good=p.check_cancellation_domain(v,(9,3),54,(29,)*4,(5251,)*4)
        self.assertFalse(good['actual_source_admitted'])
        with self.assertRaises(ValueError):p.check_cancellation_domain(v,(3,),54,(29,)*4,(5251,)*4)
        with self.assertRaises(ValueError):p.check_cancellation_domain(v,(9,),55,(29,)*4,(5251,)*4)
        with self.assertRaises(ValueError):p.check_cancellation_domain(v,(9,),54,(30,)*4,(5251,)*4)
        with self.assertRaises(ValueError):p.check_cancellation_domain(v,(9,),54,(29,)*4,(5252,)*4)
        with self.assertRaises(ValueError):p.build_outer_partition_binding((0,0,5,3,9))
    def test_shared_reference_preserves_owner_without_chart_duplication(self):
        v=label(8,2); ref=p.bind_reference(v)
        self.assertEqual(ref['owner'],v.data())
        self.assertNotIn('chart_cases',ref)
        self.assertFalse(ref['executable_AST_lowered'])
        self.assertEqual(len(p.shared_definition()['chart_cases']),16)
    def test_boolean_standard_tag_rejected(self):
        v=VertexLabel(0,0,5,3,9)
        object.__setattr__(v,'standard_tag',True)
        with self.assertRaises(ValueError):p.check_cancellation_domain(v,(1,),54,(29,)*4,(5251,)*4)
    def test_authenticated_public_sources(self):
        self.assertEqual(len(p.authenticate_public_sources()),2)
    def test_release_stays_held(self):
        gate=p.release_gate()
        self.assertEqual(set(gate), {'actual_source_admitted','Laurent_admitted','physical_polynomial_expansion','physical_polynomial_evaluation','arithmetic_cost_certificate','resource_gate_passed'})
        self.assertFalse(any(v for v in gate.values() if isinstance(v,bool)))

if __name__=='__main__':unittest.main()
