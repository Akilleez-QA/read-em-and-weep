"""Artificial exact matrices/cochains only; no actual HM coefficients."""
from fractions import Fraction as Q
import itertools
import importlib.util
from pathlib import Path
import sys
import unittest
import boundary as A

def fixture():
    h=A.mat([[1,0],[0,-1]]);e=A.mat([[0,1],[0,0]]);f=A.mat([[0,0],[1,0]])
    frames={0:A.ID,1:A.mat([[1,1],[0,1]]),2:A.mat([[1,0],[1,1]]),3:A.mat([[2,1],[1,1]])}
    charges={i:(A.add(A.scale(i+1,h),A.scale(i-1,e)),A.add(A.scale(i+2,e),A.scale(2-i,f)))for i in frames}
    derivs={0:(Q(0),Q(2)),1:(Q(1),Q(-1)),2:(Q(-2),Q(4)),3:(Q(3,2),Q(5,3))}
    return A.ArtificialCurrents(frames,charges),derivs

class Controls(unittest.TestCase):
    def test_actual_current_cocycle_and_noncommuting_transport_on_toy_data(self):
        C,df=fixture();found=False
        for i,j,k in itertools.permutations(range(4),3):
            self.assertEqual(A.mul(C.g(j,k),C.g(i,j)),C.g(i,k))
            for d in(0,1):
                self.assertEqual(C.L(i,k,d),A.add(C.L(i,j,d),C.U(i,j,k,d)))
                self.assertEqual(A.trace(C.L(i,j,d)),0)
                found|=C.U(i,j,k,d)!=C.L(j,k,d)
        self.assertTrue(found)
    def test_E_delta_f_equals_delta_explicit_B_all24_ordered_triples(self):
        C,df=fixture();edge=lambda i,j:C.B_edge(df,i,j);dt=lambda i,j:A.scalar_difference(df,i,j)
        nonzero=False
        for i,j,k in itertools.permutations(range(4),3):
            left=C.E_triangle(dt,i,j,k);right=C.delta_edge(edge,i,j,k)
            self.assertEqual(left,right);self.assertEqual(A.trace(left),0);nonzero|=left!=A.ZERO
        self.assertTrue(nonzero)
    def test_B_is_an_alternating_row_End_edge_cochain(self):
        C,df=fixture()
        for i,j in itertools.permutations(range(4),2):
            self.assertEqual(C.B_edge(df,j,i),A.scale(-1,A.conjugate_inverse(C.g(j,i),C.B_edge(df,i,j))))
            self.assertEqual(A.trace(C.B_edge(df,i,j)),0)
    def test_missing_endpoint_or_wrong_transport_fails(self):
        C,df=fixture();dt=lambda i,j:A.scalar_difference(df,i,j);bad_endpoint=bad_transport=False
        for i,j,k in itertools.permutations(range(4),3):
            correct=C.E_triangle(dt,i,j,k)
            wrong=lambda a,b:A.scale(Q(1,2),A.sub(A.scale(df[b][1],C.L(a,b,0)),A.scale(df[b][0],C.L(a,b,1))))
            bad_endpoint|=C.delta_edge(wrong,i,j,k)!=correct
            edge=lambda a,b:C.B_edge(df,a,b)
            wrong_delta=A.add(A.sub(A.mul(A.mul(C.g(i,j),edge(j,k)),A.inv(C.g(i,j))),edge(i,k)),edge(i,j))
            bad_transport|=wrong_delta!=correct
        self.assertTrue(bad_endpoint and bad_transport)
    def test_full_five_term_variation_retains_ten_baseline_and_Fk_terms(self):
        C,df=fixture();dt=lambda i,j:A.scalar_difference(df,i,j)
        # Two independent artificial scalar directions and an arbitrary fixed
        # complete baseline:7 kinetic plus3 NEGATIVE gerbe contributions.
        dg={i:(2*x,-3*y)for i,(x,y)in df.items()};ds=lambda i,j:A.scalar_difference(dg,i,j)
        base_terms=[A.mat([[i+1,i],[2-i,3*i]])for i in range(10)]
        baseline=A.ZERO
        for j,m in enumerate(base_terms):baseline=A.add(baseline,A.scale(1 if j<7 else-1,m))
        baseline=A.tf(baseline);Fkq=A.mat([[1,2],[3,-1]]);Fkp=A.mat([[2,-1],[4,-2]])
        fixed=A.add(A.add(baseline,Fkq),Fkp)
        self.assertNotEqual(fixed,A.ZERO)
        for i,j,k in itertools.combinations(range(4),3):
            Ep=C.E_triangle(dt,i,j,k);Eq=C.E_triangle(ds,i,j,k)
            Rold=fixed;Rnew=A.add(fixed,A.add(Ep,Eq))
            K=lambda a,b:A.add(C.B_edge(df,a,b),C.B_edge(dg,a,b))
            self.assertEqual(A.sub(Rnew,Rold),C.delta_edge(K,i,j,k))
    def test_first_order_exactness_does_not_force_global_second_class_zero(self):
        # Countercontrol to the inference alone, not an HM specialization.
        # C1=Q -> C2=Q^2 has delta(u)=(u,0); d2=0. R=(0,1)
        # is closed, detected by its second coordinate and is not a boundary,
        # even while both independent first-order scalar problems have F=0.
        delta=lambda u:(u,Q(0));Lambda=lambda r:r[1]
        self.assertEqual(Lambda(delta(Q(7,3))),0)
        self.assertEqual(Lambda((Q(0),Q(1))),1)
        scalar_delta=lambda s:s[1]-s[0]
        self.assertEqual(scalar_delta((Q(3),Q(3))),0)
        self.assertEqual(scalar_delta((Q(-2),Q(-2))),0)
    def test_row_boundary_has_explicit_total_lift_primitive(self):
        import resolution_boundary as RB
        # Reuse only the existing SOURCE-FREE seven-contraction fixture,
        # not its tests or any actual source descriptor.
        path=RB.JC/'test_lift.py';name='bi_artificial_JC_fixture'
        spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec)
        sys.modules[name]=m;spec.loader.exec_module(m)
        local,_=m.fixtures();L=RB.L
        edge=lambda v:L.checked_matrix([[v[0]+v[1],v[0]*v[1]+1],[v[0]-v[1],v[0]+2*v[1]]])
        def source(v):
            out=L.zero(2)
            for j in range(3):out=L.add(out,L.scale((-1)**j,edge(v[:j]+v[j+1:])))
            return out
        J=L.TinyLift(local,source);C=RB.TinyBoundaryPrimitive(J,edge)
        nonzero_top=False
        for s in range(4):
            for v in itertools.combinations(range(7),3+s):
                self.assertEqual(C.total_boundary_component(s,v),J.component(s,v))
            if s==3:
                nonzero_top=any(C.component(3,v)!=L.zero(8)for v in itertools.combinations(range(7),5))
        self.assertTrue(nonzero_top)
    def test_inexact_or_non_SL2_artificial_input_rejected(self):
        with self.assertRaises(ValueError):A.mat([[True,0],[0,1]])
        with self.assertRaises(ValueError):A.mat([[1.0,0],[0,1]])
        with self.assertRaises(ValueError):A.ArtificialCurrents({0:[[2,0],[0,1]]},{0:(A.ZERO,A.ZERO)})

if __name__=='__main__':unittest.main()
