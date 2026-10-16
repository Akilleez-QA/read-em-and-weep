"""SR01 tiny artificial and source-text controls; no physical execution."""
import ast
import inspect
import math
import unittest
from fractions import Fraction as Q
from unittest.mock import patch
import program as P
import raw_engine as R


class LiteralReview(unittest.TestCase):
    def test_four_block_raw_formula_against_independent_dense_constants(self):
        ex = R.RF.Execution(); mat = R.Mat(ex)
        def dense(seed):
            return ((Q(seed), Q(seed+1)), (Q(2-seed), Q(seed-2)))
        def field(a): return tuple(tuple(ex.scalar(x) for x in row) for row in a)
        def trace(a): return a[0][0]+a[1][1]
        def trace_product(a,b): return sum(a[i][j]*b[j][i] for i in range(2) for j in range(2))
        aa = [dense(j+1) for j in range(4)]
        ab = [dense(2*j+3) for j in range(4)]
        ba = [dense(3*j-1) for j in range(4)]
        bb = [dense(5*j+2) for j in range(4)]
        qa,qb=Q(3,2),Q(-2,3)
        expected=Q(0)
        for index in range(4):
            sign=(-1,1,-1,1)[index]; weight=(-1,1,3,5)[index]
            wedge=trace_product(aa[index],bb[index])-trace_product(ab[index],ba[index])
            endpoint=weight*(qa*(trace(ab[index])+trace(bb[index]))/2
                             -qb*(trace(aa[index])+trace(ba[index]))/2)
            expected+=sign*(wedge+endpoint)/4
        expected-=Q(15,8)*qa*qb
        actual=R.raw_scalar_formula(mat,([field(a)for a in aa],[field(a)for a in ab]),
            ([field(a)for a in ba],[field(a)for a in bb]),ex.scalar(qa),ex.scalar(qb))
        self.assertEqual(actual.rational_x().laurent_coefficient((0,0,0,0)),expected)

    def test_both_E_endpoint_derivatives_with_artificial_transitions(self):
        ex=R.RF.Execution(); m=R.Mat(ex); x,y=ex.x(0),ex.x(1); z,o=ex.scalar(0),ex.scalar(1)
        frames=[m.mul(((o,x*ex.scalar(a)),(z,o)),((o,z),(y*ex.scalar(b),o)))
                for a,b in ((0,0),(1,2),(3,5))]
        class Source(R.SC.Source):
            def g(self,a,b):return m.mul(frames[b],m.inverse(frames[a]))
            def T(self,p,a,b):return ((x*ex.scalar(2*a+3*b)+y*ex.scalar(5*a-b),),)
        source=Source(m);i,j,k=0,1,2
        gij=source.g(i,j);gjk=source.g(j,k);inv=m.inverse(gij)
        left=[m.mul(inv,m.D(gij,d))for d in (0,1)]
        right=[m.mul(inv,m.inverse(gjk),m.D(gjk,d),gij)for d in (0,1)]
        sij=source.T((2,3),i,j);sjk=source.T((2,3),j,k)
        terms=[m.smul(m.D(sjk,0),left[1]),m.scale(m.smul(m.D(sjk,1),left[0]),-1),
               m.smul(m.D(sij,1),right[0]),m.scale(m.smul(m.D(sij,0),right[1]),-1)]
        expected=m.scale(m.add(*terms),Q(1,2))
        actual=source.E((0,1),(2,3),(i,j,k))
        self.assertTrue(all(a==b for ra,rb in zip(actual,expected)for a,b in zip(ra,rb)))
        self.assertTrue(all(any(not v.is_zero()for row in term for v in row)for term in terms))

    def test_first_hit_integer_multiplicity_on_tiny_scalar_fixture(self):
        ex=R.RF.Execution();cs=[ex.scalar(1),ex.scalar(1)];vs=[ex.scalar(Q(1,3)),ex.scalar(Q(2,3))]
        total=ex.scalar(0)
        for j in (0,1):total=total+P.first_hit(ex,cs,vs,j,2,3)*R.power(vs[j],2)
        self.assertEqual(total.rational_x().laurent_coefficient((0,0,0,0)),1)
        for n in range(9):
            for k in range(n+1):self.assertEqual(P.binomial(n,k),math.comb(n,k))

    def test_full_character_extraction_requires_complete_sum_divisibility(self):
        ex=R.RF.Execution();x=ex.x(0);one=ex.scalar(1)
        y=ex.y(0)*ex.y(1)*ex.y(2)*ex.y(3)
        left=y/(one-x);right=-(y*x)/(one-x)
        with self.assertRaises(R.RF.NotLaurentPolynomial):dict(left.terms)[15].laurent_coefficient((0,0,0,0))
        whole=left+right
        self.assertEqual(dict(whole.terms)[15].laurent_coefficient((0,0,0,0)),1)

    def test_final_fiber_guard_before_first_yield_or_owner_construction(self):
        with patch.object(R.I,'FullOwner',side_effect=AssertionError('owner constructed')), \
             patch.object(R.RF,'Execution',side_effect=AssertionError('field execution')):
            iterator=P.potential_owners(0,('guard-test',0))
            with self.assertRaises(R.I.PhysicalAdmissionMissing):next(iterator)
            for callback in (lambda:P.actual_route30(),lambda:P._actual_body(None),
                    lambda:P.weighted_assignment(None,None,()),lambda:R.PhysicalModel(None,None),
                    lambda:R.PhysicalModel._build_body(None,None,None),lambda:P.outer_weight(None,None)):
                with self.assertRaises(R.I.PhysicalAdmissionMissing):callback()

    def test_outer_counts_and_structural_terminal_order_without_enumeration(self):
        with patch.object(R.I,'FullOwner',side_effect=AssertionError('owner constructed')):
            self.assertEqual([P.alphabet_count(t)for t in(0,8,12,14,15)],[2,6,16,40,32])
        self.assertEqual(24*2*6*16*40*32,5898240)
        stairs=R.SC.staircase_records()
        self.assertEqual(len(stairs),24)
        self.assertEqual(sum(s['orientation']for s in stairs),0)
        tree=ast.parse(inspect.getsource(P._actual_body))
        body=tree.body[0].body
        loop=next(i for i,n in enumerate(body)if isinstance(n,ast.For))
        stripped=next(i for i,n in enumerate(body)if isinstance(n,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='stripped'for t in n.targets))
        self.assertGreater(stripped,loop)
        self.assertEqual(P.EXPONENT,(-1,-1,-1,-1))
        text=inspect.getsource(P.weighted_assignment)
        self.assertIn('for owner in owners:',text)
        self.assertIn('I.sorted_source(owners)',text)
        self.assertIn('X13[5][0]+X02[1][3]+X02[4][2]',text)


if __name__=='__main__':unittest.main()
