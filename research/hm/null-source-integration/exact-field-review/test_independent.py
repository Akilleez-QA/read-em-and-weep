"""Independent generic/artificial controls; no physical source data or execution."""
import itertools,unittest
from fractions import Fraction as F
from field import Execution,Limits,LimitExceeded,NotLaurentPolynomial,UnsupportedInverse
Z=(0,0,0,0)

def basis_expected(overlap,scale):
    axes=[i for i in range(4)if overlap&(1<<i)]
    out={}
    for choices in itertools.product([1,3],repeat=len(axes)):
        exps=[0]*4
        for i,power in zip(axes,choices):exps[i]=power
        out[tuple(exps)]=scale*(-1)**sum(p==1 for p in choices)
    return out

def polynomial_rational_terms(test,r):
    test.assertEqual(dict(r.denominator.terms),{Z:F(1)})
    return dict(r.numerator.terms)

class IndependentField(unittest.TestCase):
    def test_factory_mixed_scalar_and_poison_variants(self):
        requested,foreign=Execution(),Execution()
        own=requested.constant(2);other=foreign.constant(3)
        for numerator,denominator in [(other,own),(own,other),(other,3),(2,other),(other,None),(other,other)]:
            before=dict(requested.counts)
            with self.assertRaises(ValueError):requested.rational(numerator,denominator)
            self.assertEqual(dict(requested.counts),before)
        for numerator,denominator in [(own,own),(own,None),(own,3),(2,own),(2,3),(F(2,3),F(5,7))]:
            self.assertIs(requested.rational(numerator,denominator).ex,requested)
        with self.assertRaises(ZeroDivisionError):requested.rational(1,0)
        poisoned=Execution(Limits(products=0));old=poisoned.constant(1)
        with self.assertRaises(LimitExceeded):poisoned.mul(F(1),F(1))
        for numerator,denominator in [(other,old),(old,other),(other,3),(2,other),(other,None),(other,other),(old,old),(old,None),(2,3),(0.5,None)]:
            with self.assertRaises(LimitExceeded):poisoned.rational(numerator,denominator)
    def test_all_basis_products_against_literal_expansion(self):
        e=Execution()
        for a,b in itertools.product(range(16),repeat=2):
            left=e.element({a:e.rational(F(2,3))});right=e.element({b:e.rational(F(-3,5))})
            result=left*right
            self.assertEqual(len(result.terms),1)
            mask,r=result.terms[0]
            self.assertEqual(mask,a^b)
            self.assertEqual(polynomial_rational_terms(self,r),basis_expected(a&b,F(-2,5)))
    def test_second_invariant_derivative_closed_formula(self):
        # Independently expanded V_i^2(x_i^k*y^mask), including moving y_i.
        for mask,axis,k in itertools.product(range(16),range(4),range(4)):
            e=Execution();exp=tuple(k if j==axis else 0 for j in range(4))
            f=e.element({mask:e.rational(e.poly({exp:1}))})
            result=f.jet([axis,axis]);moving=bool(mask&(1<<axis))
            high=F(2*k*k+7*k+6,2)if moving else F(2*k*k+k,2)
            low=F(-2*k*k-k,2)if moving else F(-2*k*k+k,2)
            expected={}
            for power,c in [(k+1,high),(k-1,low)]:
                if c:expected[tuple(power if j==axis else 0 for j in range(4))]=c
            if not expected:self.assertTrue(result.is_zero())
            else:
                self.assertEqual(result.terms[0][0],mask)
                self.assertEqual(polynomial_rational_terms(self,result.terms[0][1]),expected)
    def test_reciprocals_cancellation_and_refusal(self):
        e=Execution();x=e.x(0);y=e.y(1);one=e.scalar(1)
        for value in [x,y,(x+one)*y/(x*x+one),e.scalar(F(-3,7))*y*e.y(3)]:
            self.assertEqual(value*value.inverse(),one)
            self.assertTrue((value.V(1)*value.inverse()+value*value.inverse().V(1)).is_zero())
        with self.assertRaises(UnsupportedInverse):(x+y).inverse()
        with self.assertRaises(ZeroDivisionError):(y-y).inverse()
        with self.assertRaises(ValueError):y.laurent_coefficient(Z)
    def test_multivariate_laurent_certificate(self):
        e=Execution();x=[e.xpoly(i)for i in range(4)]
        d=x[0]*x[2]+x[1]+e.constant(1)
        q=e.poly({(2,0,0,1):F(2,7),(0,3,1,0):F(-5,3),Z:F(4)})
        monomial=e.poly({(1,2,0,3):1})
        r=e.rational(d*q,d*monomial)
        expected={tuple(a-b for a,b in zip(exp,(1,2,0,3))):c for exp,c in q.terms}
        for exp,c in expected.items():self.assertEqual(r.laurent_coefficient(exp),c)
        self.assertEqual(r.laurent_coefficient((999,-999,1,2)),0)
        quotient,remainder=(d*q+x[2]).divide(d)
        self.assertEqual(quotient*d+remainder,d*q+x[2])
        self.assertFalse(remainder.is_zero())
        bad=e.rational(d*q+x[2],d*monomial)
        for exp in [Z,(999,-999,1,2)]:
            with self.assertRaises(NotLaurentPolynomial):bad.laurent_coefficient(exp)
    def test_cross_execution_arithmetic_rejected(self):
        a,b=Execution(),Execution()
        for left,right in [(a.constant(1),b.constant(1)),(a.rational(1),b.rational(1)),(a.scalar(1),b.scalar(1))]:
            with self.assertRaises(ValueError):left+right
            with self.assertRaises(ValueError):left*right
    def test_cap_poisoning_across_preexisting_objects(self):
        e=Execution(Limits(products=100));p=e.constant(1);r=e.rational(1);v=e.scalar(1)
        with self.assertRaises(LimitExceeded):e.tick('products',101)
        for fn in [lambda:p.is_zero(),lambda:r.is_zero(),lambda:v.is_zero(),lambda:p==p,lambda:r==r,lambda:v==v,lambda:e.poly(),lambda:e.element(),lambda:e.rational(p,p),lambda:v.jet([])]:
            with self.assertRaises(LimitExceeded):fn()
    def test_factory_rejects_foreign_polynomial_pair(self):
        # Required contract: this currently FAILS at 42559cd2.
        requested,foreign=Execution(),Execution()
        p,q=foreign.constant(2),foreign.constant(3)
        with self.assertRaises(ValueError):requested.rational(p,q)
    def test_poisoned_factory_cannot_switch_execution(self):
        # Required contract: this currently FAILS at 42559cd2.
        requested,foreign=Execution(Limits(products=0)),Execution()
        p,q=foreign.constant(2),foreign.constant(3)
        with self.assertRaises(LimitExceeded):requested.mul(F(1),F(1))
        with self.assertRaises(LimitExceeded):requested.rational(p,q)
if __name__=='__main__':unittest.main(verbosity=2)
