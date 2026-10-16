"""Independent exterior/tensor controls. Invented inputs only; no source imports.

All forms use ordinary exterior products, never Cech-totalized products.
"""
from fractions import Fraction as F
from itertools import product, permutations
import random
import unittest

ZERO=(0,0,0,0)
ID=(1,0,0,1)
H=(1,0,0,-1)
E=(0,1,0,0)
F0=(0,0,1,0)
PERMS=list(permutations(range(4)))
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def add(*xs): return tuple(sum(x[i] for x in xs) for i in range(4))
def scale(q,x): return tuple(q*a for a in x)
def mul(a,b): return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
def trace(x): return x[0]+x[3]
def trans(x): return (x[0],x[2],x[1],x[3])
def comm(a,b): return add(mul(a,b),scale(-1,mul(b,a)))
def K(x,a,b): return scale(F(1,4),comm(x[a],x[b]))
def T4(l,u,a,b,c,d):
    return scale(F(1,4),add(scale(trace(mul(u[a],K(u,c,d))),l[b]),
      scale(-trace(mul(u[b],K(u,c,d))),l[a]),
      scale(trace(mul(l[b],K(l,c,d))),u[a]),
      scale(-trace(mul(l[a],K(l,c,d))),u[b])))
def curvature(l,u,a,b): return F(trace(mul(u[a],l[b]))-trace(mul(u[b],l[a])),4)
def Q4(l,u,a,b,c,d):
    v=[add(x,y) for x,y in zip(l,u)]
    return add(scale(F(1,2),add(comm(K(u,a,b),K(l,c,d)),comm(K(u,c,d),K(l,a,b)))),
      T4(l,u,a,b,c,d),T4(l,u,c,d,a,b),scale(-curvature(l,u,c,d),K(v,a,b)),
      scale(-curvature(l,u,a,b),K(v,c,d)))
def alt(fn): return scale(F(1,24),add(*(scale(sign(p),fn(*p)) for p in PERMS)))
def cube(x,abc):
    return sum(sign(p)*trace(mul(mul(x[abc[p[0]]],x[abc[p[1]]]),x[abc[p[2]]])) for p in permutations(range(3)))
def cube_wedge(x,y):
    # The 3-form tr(x^3) is followed by matrix-valued 1-form y.
    return add(*(scale((-1)**(3-b)*cube(x,tuple(a for a in range(4) if a!=b)),y[b]) for b in range(4)))
def scalar3_wedge(z,y):
    return add(*(scale((-1)**(3-b)*z[tuple(a for a in range(4) if a!=b)],y[b]) for b in range(4)))
def zform(x): return {abc:cube(x,abc) for abc in __import__('itertools').combinations(range(4),3)}
def zadd(x,y,q=1): return {abc:x[abc]+q*y[abc] for abc in x}
def scalar_derivatives(bi,bj):
    # Flat exponential germs: partial_a B_c = -[B_a,B_c]/2 at zero.
    dbi=lambda a,c:scale(F(-1,2),comm(bi[a],bi[c]))
    dbj=lambda a,c:scale(F(-1,2),comm(bj[a],bj[c]))
    return {(a,c,d):F(1,4)*trace(add(mul(dbi(a,c),bj[d]),mul(bi[c],dbj(a,d)),
         scale(-1,mul(dbi(a,d),bj[c])),scale(-1,mul(bi[d],dbj(a,c)))))
       for a,c,d in product(range(4),repeat=3)}
def ER(l,u,sij,sjk,a,b,c,d):
    return scale(F(1,2),add(scale(sjk[a,c,d],l[b]),scale(-sjk[b,c,d],l[a]),
                            scale(sij[b,c,d],u[a]),scale(-sij[a,c,d],u[b])))
def random_form(rng):
    return [(a,b,c,-a) for a,b,c in ([rng.randrange(-3,4) for _ in range(3)] for _ in range(4))]

class IndependentChecks(unittest.TestCase):
    def test_quartic_identity_all_1296_basis_tensors(self):
        # Each coordinate slot lies in sl2_L direct-sum sl2_U (dimension six).
        basis=[(x,ZERO) for x in (H,E,F0)]+[(ZERO,x) for x in (H,E,F0)]
        for slots in product(basis,repeat=4):
            l=[s[0] for s in slots];u=[s[1] for s in slots]
            actual=alt(lambda a,b,c,d:Q4(l,u,a,b,c,d))
            expected=scale(F(1,72),add(cube_wedge(u,l),scale(-1,cube_wedge(l,u))))
            self.assertEqual(actual,expected)

    def test_column_cubic_and_scalar_shift(self):
        x=[H,E,F0,add(H,E)]
        xt=[scale(-1,trans(a)) for a in x]
        self.assertEqual(zform(xt),zform(x))
        self.assertNotEqual(zform(x),{abc:0 for abc in zform(x)})
        # Ordinary transpose alone has the opposite sign.
        self.assertEqual(zform([trans(a) for a in x]),{abc:-q for abc,q in zform(x).items()})
        shifted=[add(a,scale(k,ID)) for a,k in zip(x,(2,-1,3,4))]
        self.assertEqual(zform(shifted),zform(x))

    def test_full_remainder_on_invented_flat_germs(self):
        rng=random.Random(16102026)
        nonzero=0
        for _ in range(16):
            bi,bj,bk=(random_form(rng) for _ in range(3))
            l=[scale(-1,trans(add(y,scale(-1,x)))) for x,y in zip(bi,bj)]
            u=[scale(-1,trans(add(y,scale(-1,x)))) for x,y in zip(bj,bk)]
            sij=scalar_derivatives(bi,bj);sjk=scalar_derivatives(bj,bk)
            actual=alt(lambda a,b,c,d:add(Q4(l,u,a,b,c,d),ER(l,u,sij,sjk,a,b,c,d),ER(l,u,sij,sjk,c,d,a,b)))
            zi,zj,zk=map(zform,(bi,bj,bk))
            expected=scale(F(1,72),add(scalar3_wedge(zadd(zk,zj,-1),l),scale(-1,scalar3_wedge(zadd(zj,zi,-1),u))))
            self.assertEqual(actual,expected)
            # Direct row-Cech differential of the proposed edge primitive.
            pjk=scale(F(-1,72),scalar3_wedge(zadd(zj,zk),u))
            pik=scale(F(-1,72),scalar3_wedge(zadd(zi,zk),[add(x,y) for x,y in zip(l,u)]))
            pij=scale(F(-1,72),scalar3_wedge(zadd(zi,zj),l))
            self.assertEqual(actual,add(pjk,scale(-1,pik),pij))
            nonzero+=actual!=ZERO
        self.assertGreater(nonzero,0)

    def test_raw_symmetric_edge_correction_cancels(self):
        rng=random.Random(2416)
        l,u=random_form(rng),random_form(rng)
        # Arbitrary derivatives of a symmetric pair correction; stronger than separation.
        sij={};sjk={}
        for a in range(4):
            for c in range(4):
                for d in range(c,4):
                    sij[a,c,d]=sij[a,d,c]=rng.randrange(-4,5)
                    sjk[a,c,d]=sjk[a,d,c]=rng.randrange(-4,5)
        self.assertEqual(alt(lambda a,b,c,d:add(ER(l,u,sij,sjk,a,b,c,d),ER(l,u,sij,sjk,c,d,a,b))),ZERO)

if __name__=='__main__': unittest.main(verbosity=2)
