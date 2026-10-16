import unittest,json
from unittest.mock import patch
import lower_selected_kernel_denominators as m
import owned_scalar_denominator_binding as o
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.art=m.build()
    def lower(self,end=4):return m.Lower(tuple(o.VertexLabel(4,i,b,mask,t) for i,(b,mask,t) in enumerate(((1,12,3),(2,13,11),(end,15,15)))))
    def test_all_four_signs_and_owners(self):
        a=self.art
        self.assertEqual([t['E_sign'] for t in a['terms']],[1,-1,1,-1])
        self.assertEqual([x[2] for x in a['owners']],[1,2,4])
        for t in a['terms']:
            for k in ('A','B'):self.assertEqual([list(x['owner']) for x in t[k]['derived_denominators']],[list(x) for x in a['owners']])
    def test_derived_orders(self):
        ledgers=[x for t in self.art['terms'] for k in ('A','B') for x in t[k]['derived_denominators']]
        self.assertEqual(max(x['carrier'] for x in ledgers),20)
        self.assertEqual(max(max(x['legal']) for x in ledgers),3)
        self.assertEqual(max(max(x['standard']) for x in ledgers),5251)
    def test_only_coordinate_inverses(self):
        nodes=self.art['dag']
        for op,*args in nodes:
            self.assertIn(op,('rational','coordinate','add','multiply','power','bounded_composition_sum'))
            if op=='power' and args[1]<0:self.assertEqual(nodes[args[0]][0],'coordinate')
    def test_endpoint_123_zero_124_not_structurally_zero(self):
        lo=self.lower(3);self.assertEqual(lo.quotient(lo.vs[-1]),lo.g.c(0))
        lo=self.lower(4);self.assertNotEqual(lo.quotient(lo.vs[-1]),lo.g.c(0))
    def test_active_mask_filter(self):
        lo=self.lower();v=o.VertexLabel(4,0,1,1,3)
        self.assertEqual(lo.quotient(v),lo.g.c(0))
    def test_actual_metadata_mutation_rejected(self):
        model=m.source.authenticate();model['charts'][1]['di']=[['0,0,0,0',1]]
        with patch.object(m.source,'authenticate',return_value=model):
            with self.assertRaisesRegex(ValueError,'pinned denominator'):self.lower()
    def test_unmatched_and_excess_factors_rejected(self):
        lo=self.lower()
        with self.assertRaisesRegex(ValueError,'unmatched'):lo.cancel(lo.rat(lo.g.c(1),{'alien':1}))
        with self.assertRaisesRegex(ValueError,'clearance'):lo.cancel(lo.rat(lo.g.c(1),{lo.key(lo.vs[0],'H'):55}))
    def test_finite_sum_domains(self):
        for op,*a in self.art['dag']:
            if op!='bounded_composition_sum':continue
            d=a[0];self.assertEqual(d['total'],d['dimension']*534+1)
            self.assertEqual(d['threshold'],535)
            self.assertEqual(d['earlier_upper'],534)
            self.assertIn(d['chosen'],range(d['dimension']))
    def test_abstract_derivative_quotient(self):
        # Formal single indeterminate control; no physical source evaluation.
        g=m.DAG();x=g.node('coordinate',0)
        n=g.add(g.pow(x,3),g.c(1));dn=g.diff(n,0)
        def ev(i,z):
            op,*a=g.nodes[i]
            if op=='rational':return a[0]/a[1]
            if op=='coordinate':return z
            if op=='add':return sum(ev(j,z) for j in a)
            if op=='multiply':
                r=1
                for j in a:r*=ev(j,z)
                return r
            if op=='power':return ev(a[0],z)**a[1]
        self.assertEqual(ev(dn,2),12)
    def test_nonzero_trace_is_projected(self):
        from fractions import Fraction
        lo=self.lower();g=lo.g
        R=[[lo.rat(g.c(n)) for n in row] for row in ((3,7),(11,5))]
        tf=lo.tracefree(R)
        def ev(i):
            op,*a=g.nodes[i]
            if op=='rational':return Fraction(*a)
            if op=='add':return sum(map(ev,a))
            if op=='multiply':
                p=1
                for j in a:p*=ev(j)
                return p
            raise ValueError(op)
        self.assertEqual([[ev(x[0]) for x in row] for row in tf],[[-1,7],[11,1]])
        scalar=[[lo.rat(g.c(9 if i==j else 0)) for j in range(2)] for i in range(2)]
        self.assertEqual([[ev(x[0]) for x in row] for row in lo.tracefree(scalar)],[[0,0],[0,0]])
    def test_saved_artifact_and_cross_hash_seed_bytes(self):
        import os,sys,subprocess
        from pathlib import Path
        script=Path(m.__file__)
        outputs=[]
        for seed in ('1','51'):
            env=dict(os.environ,PYTHONHASHSEED=seed)
            outputs.append(subprocess.check_output([sys.executable,'-B',str(script)],env=env))
        self.assertEqual(outputs[0],outputs[1])
        self.assertEqual(outputs[0],script.with_name('selected-full-owner-kernel-lowering.json').read_bytes())
    def test_pinned_identity_provenance(self):
        cert=self.art['transition_inverse_rewrite']['source_certificate']
        self.assertFalse(cert['historical_checker_executed_now'])
        self.assertEqual(set(cert['identities']),{'E_identity','P_I','delta_I','P_gamma'})
    def test_abstract_bounded_sum_body_semantics(self):
        from math import comb
        from itertools import product
        for dim in (1,2,3):
            for threshold in (1,2,3):
                g=m.DAG();cs=list(range(2,2+dim));vs=list(range(5,5+dim));total=dim*(threshold-1)+1
                weighted=0
                for j in range(dim):
                    node=m.composition_sum(g,dim,j,threshold,[g.c(x) for x in cs],[g.c(x) for x in vs])
                    _,domain,body=g.nodes[node];value=0
                    for n in product(range(total+1),repeat=dim):
                        if sum(n)!=total or n[j]<threshold or any(n[i]>=threshold for i in range(j)):continue
                        affine=lambda a:a['constant']+sum(x*y for x,y in zip(a['coefficients'],n))
                        term=1
                        for b in body['coefficient']['factors']:term*=comb(affine(b['top']),affine(b['bottom']))
                        for p in body['powers']:
                            exponent=affine(p['exponent']);self.assertGreaterEqual(exponent,0)
                            term*=g.nodes[p['base']][1]**exponent
                        value+=term
                    weighted+=vs[j]**threshold*value
                self.assertEqual(weighted,sum(x*y for x,y in zip(cs,vs))**total)
    def test_abstract_normal_order_quotient_semantics(self):
        from fractions import Fraction
        lo=m.Lower.__new__(m.Lower);lo.g=g=m.DAG();x=g.node('coordinate',0)
        denominator=g.add(x,g.c(2));lo.factors={'abstract':denominator}
        numerator=g.add(g.pow(x,3),g.c(1));r=lo.rat(numerator,{'abstract':2});dr=lo.diff(r,0)
        def ev(i,z):
            op,*a=g.nodes[i]
            if op=='rational':return Fraction(*a)
            if op=='coordinate':return Fraction(z)
            if op=='add':return sum(ev(j,z) for j in a)
            if op=='multiply':
                value=1
                for j in a:value*=ev(j,z)
                return value
            if op=='power':return ev(a[0],z)**a[1]
            raise ValueError(op)
        for z in (1,3,7):
            got=ev(dr[0],z)/(z+2)**dr[1]['abstract']
            expected=Fraction(3*z*z,(z+2)**2)-Fraction(2*(z**3+1),(z+2)**3)
            self.assertEqual(got,expected)
    def test_gate_and_limits(self):
        self.assertFalse(self.art['actual_factorization_accepted'])
        self.assertFalse(self.art['physical_polynomial_evaluation'])
        self.assertEqual(self.art['held_limits'],{'private_resource_configuration_omitted':True})
if __name__=='__main__':unittest.main()
