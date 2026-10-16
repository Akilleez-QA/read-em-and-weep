"""Abstract controls only. No source imports, physical matrices, or evaluation."""
import itertools
import unittest
from fractions import Fraction

S = (2, 3, 0, 1)
def perm(v): return tuple(v[S[j]] for j in range(4))
def mask(m): return sum(((m >> i) & 1) << S[i] for i in range(4))
def tag(e): return sum(((e >> (3-i)) & 1) << (3-S[i]) for i in range(4))
def owner(o): return (*o[:3], mask(o[3]), tag(o[4]))
def sortkey(o): return (-1 if o[2] == 5 else o[2], o[3], o[4])
def atom(kind, *args): return (kind, *args)
def mul(*args): return ('mul', *args)
def sub(a,b): return ('sub',a,b)
def F(pair):
    i,j=pair
    return sub(mul(Fraction(15,4),atom('q',0,1,i),atom('q',1,2,j)),
               mul(Fraction(1,4),('trace',mul(atom('K',2,0),sub(
                   mul(atom('T',1,2,i),atom('T',0,1,j)),
                   mul(atom('T',1,2,j),atom('T',0,1,i)))))))
def rename(expr):
    if not isinstance(expr,tuple): return expr
    if expr[0] in ('q','T'): return (*expr[:-1],S[expr[-1]])
    return tuple(rename(x) for x in expr)
def target_degree(carriers,masks,pair):
    base=14*sum(4 if c==5 else 5 for c in carriers)
    return tuple(base+(sum(3 if (m>>i)&1 else 1 for m in masks)-2 if i in pair else 0) for i in range(4))
def matmul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(A): return A[0][0]+A[1][1]

class Controls(unittest.TestCase):
    def test_mask_tag_bijections_exhaustive(self):
        self.assertEqual([mask(m) for m in range(16)], [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15])
        for m in range(16):
            self.assertEqual(mask(mask(m)),m)
            self.assertEqual(tag(tag(m)),m)
            for i in range(4):
                self.assertEqual((mask(m)>>S[i])&1,(m>>i)&1)
                self.assertEqual((tag(m)>>(3-S[i]))&1,(m>>(3-i))&1)
    def test_full_owner_occurrence_retention(self):
        a=(12,7,5,1,3);b=(12,8,5,1,3)
        self.assertNotEqual(owner(a),owner(b))
        self.assertEqual(owner(owner(a)),a)
        self.assertEqual(owner(a)[:3],a[:3])
    def test_elementary_symmetric_subset_invariance(self):
        for k in range(5):
            terms={tuple(t) for t in itertools.combinations(range(4),k)}
            renamed={tuple(sorted(S[i] for i in t)) for t in terms}
            self.assertEqual(renamed,terms)
        # Thus polynomials in fixed v symbols, including each H, remain fixed.
        for c in range(5):
            self.assertEqual(rename(('sub',('power',('v',c),5),('product_v',0,1,2,3,4))),
                             ('sub',('power',('v',c),5),('product_v',0,1,2,3,4)))
        self.assertEqual(rename(mul(('v',1),('v',3),('v',4))),mul(('v',1),('v',3),('v',4)))
        self.assertEqual(rename(mul(('v',0),('v',1),('v',3),('v',4))),mul(('v',0),('v',1),('v',3),('v',4)))
    def test_ordered_mu_gerbe_exact_tree(self):
        self.assertEqual(rename(F((0,1))),F((2,3)))
        self.assertEqual(rename(rename(F((0,1)))),F((0,1)))
        self.assertNotEqual(rename(F((0,1))),F((3,2)))
        self.assertEqual(rename(atom('q',0,1,0)),atom('q',0,1,2))
    def test_noncommutative_product_negative_control(self):
        # Artificial constant matrices, unrelated to physical source data.
        A=((0,1),(0,0)); B=((0,0),(1,0)); K=((2,0),(0,3))
        self.assertEqual(tr(matmul(K,matmul(B,A))),3)
        self.assertEqual(tr(matmul(K,matmul(A,B))),2)
    def test_arbitrary_ordered_triple_map(self):
        triples=[((0,8,4,1,3),(0,2,5,4,12),(0,9,1,2,8)),
                 ((0,0,1,1,0),(0,1,1,2,0),(0,2,1,4,0))]
        for t in triples:
            for p in itertools.permutations(t):
                self.assertEqual(tuple(owner(owner(o)) for o in p),p)
                self.assertEqual(tuple(o[1] for o in p),tuple(owner(o)[1] for o in p))
    def test_degrees_all_carriers_and_mask_patterns(self):
        # All carrier triples; all 4096 mask triples tested separately below.
        for cs in itertools.product(range(6),repeat=3):
            for ms in [(0,0,0),(15,15,15),(1,6,12)]:
                self.assertEqual(perm(target_degree(cs,ms,(0,1))),target_degree(cs,tuple(map(mask,ms)),(2,3)))
        for ms in itertools.product(range(16),repeat=3):
            self.assertEqual(perm(target_degree((1,2,3),ms,(0,1))),target_degree((1,2,3),tuple(map(mask,ms)),(2,3)))
        self.assertEqual(target_degree((1,2,3),(15,15,15),(0,1)),(217,217,210,210))
        self.assertEqual(target_degree((1,2,3),(15,15,15),(2,3)),(210,210,217,217))
    def test_ledger_and_padding(self):
        ledger=tuple(sum(x) for x in zip((2,0,2),(0,3,3),(3,3,0)))
        self.assertEqual(ledger,(5,6,5))
        self.assertEqual(tuple(14-v for v in ledger),(9,8,9))
        legal=[(slot,i) for slot in range(3) for i in (0,1)]
        self.assertEqual([(slot,S[i]) for slot,i in legal],[(slot,i) for slot in range(3) for i in (2,3)])
    def test_critical_cancellation_metadata(self):
        for ms in itertools.product(range(16),repeat=3):
            mapped=tuple(map(mask,ms))
            for i in range(4):
                z=sum(1-((m>>i)&1) for m in ms)
                zp=sum(1-((m>>S[i])&1) for m in mapped)
                self.assertEqual(z,zp)
        # Laurent weight cancellation is symbolic, including negative weights.
        for w in range(-5,6):
            self.assertEqual(Fraction(w)-2*w*Fraction(1,2),0)
    def test_finite_legal_equation_and_frame_transport(self):
        # Monomial labels only; a homogeneous legal factor is Y or X(X²-Y²).
        for m in range(16):
            for i in range(4):
                bit=(m>>i)&1
                targetbit=(mask(m)>>S[i])&1
                source=('Y',i) if not bit else ('cubic_legal',i)
                target=('Y',S[i]) if not targetbit else ('cubic_legal',S[i])
                self.assertEqual((source[0],S[source[1]]),target)
        for e in range(16):
            n=(-2,-2,0,0)
            exps=tuple(n[i] if (e>>(3-i))&1 else 0 for i in range(4))
            mapped=tuple(perm(n)[i] if (tag(e)>>(3-i))&1 else 0 for i in range(4))
            self.assertEqual(perm(exps),mapped)
    def test_derivative_naturality_on_abstract_laurent_monomials(self):
        for exps in itertools.product(range(-1,2),repeat=4):
            for i in range(4):
                derived=list(exps); derived[i]-=1
                mapped=list(perm(exps)); mapped[S[i]]-=1
                self.assertEqual(perm(derived),tuple(mapped))
                self.assertEqual(exps[i],perm(exps)[S[i]])
    def test_gerbe_q_and_endpoint_Q_are_distinct(self):
        # Artificial scalar checks only, never evaluate actual transitions.
        for a,b in itertools.product((0,1),repeat=2):
            x=Fraction(3)
            ell=lambda m: x*(x*x-1) if m else Fraction(1)
            cleared=b*(1-a)*(x*x-1)/ell(b)-a*(1-b)*(x*x-1)/ell(a)
            self.assertEqual(cleared,Fraction(b-a)/x)
        # Equal nonzero masks give q=0 but nonzero endpoint logarithmic Q.
        self.assertEqual(Fraction(1-1,3),0)
        self.assertNotEqual(Fraction(3*3+1,2*3*(3*3-1)),0)
    def test_source_order_not_preserved(self):
        t=((0,0,1,1,0),(0,1,1,2,0),(0,2,1,4,0))
        self.assertEqual(tuple(sorted(t,key=sortkey)),t)
        mapped=tuple(map(owner,t))
        self.assertEqual(tuple(o[3] for o in mapped),(4,8,1))
        self.assertNotEqual(tuple(sorted(mapped,key=sortkey)),mapped)
        # Abstract nonlinear ordered cup example: no automatic alternating law.
        # c(a,b,c)=q01,0*q12,1 for artificial vertex coordinate potentials.
        potentials=((0,0),(1,2),(3,1))
        def cup(a,b,c): return (potentials[b][0]-potentials[a][0])*(potentials[c][1]-potentials[b][1])
        self.assertNotEqual(cup(0,1,2),-cup(1,0,2))

if __name__=='__main__': unittest.main()
