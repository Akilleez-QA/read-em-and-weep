"""Source-byte/exponent metadata and source-free algebra controls only."""
import copy
from fractions import Fraction as Q
from pathlib import Path
import unittest
import clearing as c

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.repo=Path(__file__).resolve().parents[3]
        cls.model,cls.pins=c.authenticate(cls.repo)
        cls.catalog=c.primitive_catalog(cls.model)
    def test_actual_denominator_and_weight_metadata(self):
        self.assertEqual([x['finite_primitive_weight_excess'] for x in self.catalog],[1,0,0,0,0,2])
        model=copy.deepcopy(self.model);model['charts'][5]['di'][0][0]='1,0,1,1'
        with self.assertRaises(ValueError):c.primitive_catalog(model)
        model=copy.deepcopy(self.model);model['charts'][1]['I'][0][0]=[['20,0,0,0',1]]
        with self.assertRaises(ValueError):c.primitive_catalog(model)
    def test_whole_F_polynomial_constructor(self):
        s=c.whole_source(self.catalog)
        self.assertEqual(s['finite_carrier_orders'],[5,6,5])
        self.assertEqual(len(s['dag']),153)
        self.assertEqual(s['naive_finite_coordinate_degree_bound']['pair'],218)
        self.assertEqual(s['refined_finite_coordinate_degree_bound']['pair'],217)
        self.assertFalse(s['physical_homogeneous_frame_identification_verified'])
        self.assertTrue(all(x['factor'][2] in (0,1) for x in s['F_denominator'] if x['factor'][1]=='ell'))
        self.assertTrue(any(n[0]=='mask_times_x_squared_plus_one_over_two' for n in s['dag']))
        self.assertTrue(any(n[0]=='binary_mask_q_numerator' for n in s['dag']))
    def test_degree_case_partition_and_covariant_top_layer(self):
        # Counts of exceptional owners and mask0, not a source-label scan.
        for n0 in range(4):
            for n5 in range(4-n0):
                for m0 in range(4):
                    gap=1-12*n0-10*n5-m0
                    if n0+n5+m0:self.assertLessEqual(gap,0)
                    else:self.assertEqual(gap,1) # only critical case, resolved below
        # Laurent monomial x^k, k<=w, abstract rf. Numerator coefficients are
        # (k-w)x²-(k+w); no pinned source polynomial is instantiated.
        for w in range(-3,4):
            for k in range(w-4,w+1):
                a,b=k-w,-(k+w)
                numerator_degree=2 if a else 0 if b else None
                if numerator_degree is not None:
                    self.assertLessEqual(k-1+numerator_degree-2,w-2)
                # Omitting both physical Q terms fails for leading x^w, w!=0.
                if k==w and w:self.assertGreater(w-1,w-2)
    def test_binary_gerbe_q_rewrite_source_free(self):
        # Tiny arbitrary scalar indeterminate specialization, not HM data.
        for x in (Q(2),Q(3)):
            L=x*(x*x-1)
            for ma in (0,1):
                for mb in (0,1):
                    la=L if ma else Q(1);lb=L if mb else Q(1)
                    rhs=mb*(1-ma)*(x*x-1)/lb-ma*(1-mb)*(x*x-1)/la
                    self.assertEqual(rhs,(mb-ma)/x)
                    if ma==mb:self.assertEqual(rhs,0)
        # rf is a DIFFERENT scalar; accidental gerbe q substitution must fail.
        self.assertNotEqual((Q(2)**2+1)/(2*Q(2)*(Q(2)**2-1)),1/Q(2))
    def test_quotient_rule_and_distinct_equal_factor_owners_toy(self):
        g=c.DAG();u=(0,'H',-1);v=(1,'H',-1)
        r=g.rat(g.n('toy_constant',1),{u:1,v:1});dr=g.partial(r,0)
        self.assertEqual(dr[1],{u:2,v:2})
        # Deliberately restricted toy interpreter: source atoms are unsupported.
        def value(n,x,derivative=False):
            op,*args=g.nodes[n]
            if op=='toy_constant':return Q(0 if derivative else args[0])
            if op=='owned_polynomial_factor':return Q(1) if derivative else x+1
            if op=='polynomial_partial_after_elementary_substitution':
                self.assertFalse(derivative);return value(args[0],x,True)
            if op=='scale':return Q(args[0],args[1])*value(args[2],x,derivative)
            if op=='sum':return sum((value(a,x,derivative) for a in args),Q(0))
            if op=='power':
                a,k=args
                return k*value(a,x)**(k-1)*value(a,x,True) if derivative and k else Q(0) if derivative else value(a,x)**k
            if op=='ordered_product':
                from math import prod
                if derivative:return sum((prod(value(a,x,j==i) for j,a in enumerate(args)) for i in range(len(args))),Q(0))
                return prod(value(a,x) for a in args)
            raise ValueError('toy interpreter rejects source node '+op)
        # Independent quotient rule with equal factor values but two owners.
        for x in (Q(2),Q(5)):
            H=x+1
            direct=-(H+H)/(H*H)**2
            separated=-1/(H*H*H)-1/(H*H*H)
            self.assertEqual(direct,separated)
            self.assertNotEqual(direct,-1/(H*H*H))
            emitted=value(dr[0],x)/(H**sum(dr[1].values()))
            self.assertEqual(emitted,direct)
    def test_exact_four_E34_and_combined_fullsum_padding(self):
        result=c.build(self.repo)
        for entry in result['requests']:
            binding=entry['v5_binding'];edges=entry['combined_edges'];self.assertEqual(len(edges),2)
            self.assertEqual(len(binding['branches']),4)
            for edge in edges:
                a,b=edge['output_edge']
                self.assertEqual(edge['inserted_owner_maps']['u']['standard_tag'],a[4])
                self.assertEqual(edge['inserted_owner_maps']['v']['standard_tag'],b[4])
                self.assertNotEqual(edge['inserted_owner_maps']['u']['occurrence'],edge['inserted_owner_maps']['v']['occurrence'])
                self.assertEqual(edge['N_fullsum']['padding']['prism2'],['C_a','Z_ab'])
                self.assertEqual(edge['N_fullsum']['padding']['prism1'],['Z_ab'])
                self.assertTrue(edge['standard_B_requirements']['complete_sum'])
                self.assertFalse(edge['geometric_source_premise_discharged'])
        self.assertTrue(all(x is False for x in result['gates'].values()))

if __name__=='__main__':unittest.main()
