"""Abstract sl2 tests only; deliberately imports no HM source module or data."""
from fractions import Fraction as F
import unittest
Z=(0,0,0); h=(1,0,0); e=(0,1,0); f=(0,0,1)
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(a,x):return tuple(a*b for b in x)
def bracket(x,y):
    a,b,c=x; d,u,v=y
    return (b*v-c*u,2*(a*u-b*d),2*(c*d-a*v))
def numerator(J,H):
    out=Z
    for i,k,s in ((0,3,1),(1,2,-1),(2,1,-1),(3,0,1)):
        out=add(out,scale(s,bracket(J[i],H[k])))
    return out
def gram(J,H):return [[sum(s*J[i][a]*H[k][b] for i,k,s in ((0,3,1),(1,2,-1),(2,1,-1),(3,0,1))) for b in range(3)] for a in range(3)]
def one(i,x):
    a=[Z]*4;a[i]=x;return a
class TestAbstractRelations(unittest.TestCase):
    def test_cross_gram_all_bilinear_basis_pairs(self):
        for i in range(4):
            for k in range(4):
                for x in (h,e,f):
                    for y in (h,e,f):
                        J,H=one(i,x),one(k,y);M=gram(J,H)
                        self.assertEqual(numerator(J,H),(M[1][2]-M[2][1],2*(M[0][1]-M[1][0]),2*(M[2][0]-M[0][2])))
    def test_internal_commutativity_is_insufficient(self):
        J,H=one(0,e),one(3,f)
        for A in (J,H):
            self.assertTrue(all(bracket(x,y)==Z for x in A for y in A))
        self.assertEqual(numerator(J,H),h)
    def test_same_line_and_same_array(self):
        H=[h,e,f,add(h,f)]
        self.assertEqual(numerator(H,H),Z)
        self.assertEqual(numerator([scale(a,e) for a in (1,2,3,4)],[scale(a,e) for a in (2,5,7,11)]),Z)
        # Same array cancellation does not require pairwise commutativity.
        self.assertNotEqual(bracket(H[0],H[1]),Z)
    def test_rank_one_coordinate_arrays(self):
        def arr(u,v,X):return [scale(a*b,X) for a in u for b in v]
        u,v,s,t=(2,3),(5,7),(11,13),(17,19)
        J,H=arr(u,v,e),arr(s,t,f)
        det=lambda a,b:a[0]*b[1]-a[1]*b[0]
        self.assertEqual(numerator(J,H),scale(det(u,s)*det(v,t),h))
        self.assertNotEqual(numerator(J,H),Z)
        self.assertEqual(numerator(arr(u,v,e),arr(u,t,f)),Z)
    def test_pairwise_cancellation_not_necessary(self):
        # J=H: complementary nonzero brackets cancel in pairs.
        A=[e,Z,Z,f]
        self.assertNotEqual(bracket(A[0],A[3]),Z)
        self.assertEqual(numerator(A,A),Z)
    def test_two_jet_symmetry_and_antisymmetry(self):
        J,H=[h,e,f,add(e,f)],[f,h,e,add(h,e)]
        self.assertEqual(numerator(J,H),scale(-1,numerator(H,J)))
    def test_single_entry_projection_is_inadequate(self):
        out=scale(F(1,8),numerator(one(0,e),one(3,f)))
        self.assertEqual(out,(F(1,8),0,0))
        self.assertEqual(out[2],0) # lower-left entry misses nonzero h
        # A diagonal-only projection misses e instead.
        out=numerator(one(0,h),one(3,e))
        self.assertEqual(out,(0,2,0))
    def test_physical_second_jet_binding(self):
        # Artificial two-coordinate matrices only, not HM source polynomials.
        import sympy as s
        x,y=s.symbols('x y', nonzero=True)
        def frame(z):return s.diag(z,1/z)
        Da,Db,Dc=frame(x*y**2),frame(y/x),frame(x**2/y)
        A=s.Matrix([[1,x+y],[x*y,1+x*y*(x+y)]])
        B=s.Matrix([[1,x*y],[x-y,1+x*y*(x-y)]])
        ga,gb=Db*A*Da.inv(),Dc*B*Db.inv()
        Q=lambda D,z:D.inv()*D.diff(z)
        def V(K,Dleft,Dright,i,j):
            T=K.diff(i)+Q(Dright,i)*K-K*Q(Dleft,i)
            return T.diff(j)+Q(Dright,j)*T-T*Q(Dleft,j)
        zero=lambda M:all(s.cancel(z)==0 for z in M)
        for i,j in ((x,x),(x,y),(y,x),(y,y)):
            Va,Vb=V(A,Da,Db,i,j),V(B,Db,Dc,i,j)
            self.assertTrue(zero(Da*A.inv()*Va*Da.inv()-ga.inv()*ga.diff(i,j)))
            self.assertTrue(zero(Da*A.inv()*B.inv()*Vb*A*Da.inv()-ga.inv()*gb.inv()*gb.diff(i,j)*ga))
            self.assertTrue(zero(Va-V(A,Da,Db,j,i)))
        # Differentiating T only would lose both endpoint frame terms.
        T=A.diff(x)+Q(Db,x)*A-A*Q(Da,x)
        self.assertFalse(zero(V(A,Da,Db,x,y)-T.diff(y)))
    def test_scalar_trace_pairing_commutator_adjoint(self):
        dot=lambda x,y:2*x[0]*y[0]+x[1]*y[2]+x[2]*y[1]
        for W in (h,e,f):
            for J in (h,e,f):
                for H in (h,e,f):self.assertEqual(dot(W,bracket(J,H)),dot(bracket(W,J),H))
if __name__=='__main__':unittest.main()
