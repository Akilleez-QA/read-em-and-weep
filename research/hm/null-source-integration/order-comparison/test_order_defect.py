"""Independent exact abstract tests. No HM source models are imported or evaluated."""
import itertools
import unittest
from fractions import Fraction as Q


def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def edge(r, i, j):
    return r[i,j] if i<j else -r[j,i]

def e(h,r,v):
    i,j,k=v
    return Q((h[j]-h[i])*edge(r,j,k)-edge(r,i,j)*(h[k]-h[j]),2)

def f(r,v):
    i,j,k=v
    return edge(r,j,k)-edge(r,i,k)+edge(r,i,j)

def delta(c,v):
    return sum((-1)**i*c(v[:i]+v[i+1:]) for i in range(len(v)))

class OrderDefect(unittest.TestCase):
    def test_all_six_permutations_universal_bilinear_basis(self):
        # Basis testing is exhaustive for the bilinear formal identity, not sampling.
        pairs=list(itertools.combinations(range(3),2))
        for hpos in range(3):
            h=[int(i==hpos) for i in range(3)]
            for rpos in pairs:
                r={ij:int(ij==rpos) for ij in pairs}
                F=f(r,(0,1,2))
                table={(0,1,2):0,(1,0,2):-Q((h[1]-h[0])*F,2),
                       (0,2,1):Q((h[2]-h[1])*F,2),
                       (1,2,0):Q((h[2]-h[1])*F,2),
                       (2,0,1):-Q((h[1]-h[0])*F,2),(2,1,0):0}
                for p in itertools.permutations(range(3)):
                    self.assertEqual(parity(p)*e(h,r,p)-e(h,r,(0,1,2)),table[p])
    def test_nonzero_defect_and_wrong_sign_control(self):
        h=[0,1,1]; r={(0,1):0,(1,2):0,(0,2):1}
        self.assertEqual(e(h,r,(0,1,2)),0)
        self.assertEqual(-e(h,r,(1,0,2)),Q(1,2))
        self.assertNotEqual(-e(h,r,(1,0,2)), -Q(1,2))
    def test_closed_scalar_edges_remove_all_local_order_defects(self):
        h=[2,-3,7]; potentials=[-4,6,1]
        r={(i,j):potentials[j]-potentials[i] for i,j in itertools.combinations(range(3),2)}
        self.assertEqual(f(r,(0,1,2)),0)
        for p in itertools.permutations(range(3)):
            self.assertEqual(parity(p)*e(h,r,p),e(h,r,(0,1,2)))
    def test_closedness_defect_on_tetrahedron(self):
        # delta E(r) = -1/2 (ell cup delta r + delta r cup ell).
        pairs=list(itertools.combinations(range(4),2))
        for hpos in range(4):
            h=[int(i==hpos) for i in range(4)]
            for rpos in pairs:
                r={ij:int(ij==rpos) for ij in pairs}
                lhs=delta(lambda v:e(h,r,v),(0,1,2,3))
                rhs=-Q((h[1]-h[0])*f(r,(1,2,3))+f(r,(0,1,2))*(h[3]-h[2]),2)
                self.assertEqual(lhs,rhs)
    def test_nonclosed_example(self):
        h=[0,1,1,1]
        r={ij:0 for ij in itertools.combinations(range(4),2)};r[1,3]=1
        self.assertEqual(delta(lambda v:e(h,r,v),(0,1,2,3)),Q(1,2))
    def test_reindex_chain_map_on_edge_basis(self):
        # Values are alternatingly extended ONCE, not recomputed by e on each tuple.
        pairs=list(itertools.combinations(range(4),2))
        for rpos in pairs:
            r={ij:int(ij==rpos) for ij in pairs}
            for p in itertools.permutations(range(4),3):
                asc=tuple(sorted(p)); ranks=tuple(asc.index(i) for i in p)
                self.assertEqual(f(r,p),parity(ranks)*f(r,asc))
    def test_same_carrier_q2_inclusion_naturality(self):
        # Artificial split inclusion, three independent moving diagonal frames.
        def mm(a,b):
            return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
        def tr(a):return list(map(list,zip(*a)))
        I=[[1,0],[0,1],[1,1]];P=[[1,0,0],[0,1,0]]
        R=[[1,2],[3,-1]]; bare=mm(mm(I,tr(R)),P)
        nu=[Q(2),Q(3),Q(5)]
        for perm in itertools.permutations(range(3)):
            a=perm[0];D=[[nu[a],0],[0,1/nu[a]]];Di=[[1/nu[a],0],[0,nu[a]]]
            signed=[[parity(perm)*x for x in row] for row in R]
            physical=mm(mm(D,signed),Di)
            included=mm(mm(mm(I,D),tr(physical)),mm(Di,P))
            # Pull the new tuple orientation back; the same q=2 row is retained.
            self.assertEqual([[parity(perm)*x for x in row] for row in included],bare)

    def test_single_component_does_not_kill_boundaries(self):
        r={(0,1):0,(0,2):1,(1,2):0}
        self.assertEqual(f(r,(0,1,2)),-1)
        # A triangle-evaluation row is not a dual cocycle, despite being linear.
        self.assertNotEqual(f(r,(0,1,2)),0)

if __name__=='__main__':unittest.main(verbosity=2)
