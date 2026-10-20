"""Small invented controls. No physical source modules, data or evaluations."""
from fractions import Fraction as F
from itertools import combinations
import unittest

Z=((F(0),F(0)),(F(0),F(0)))
I=((F(1),F(0)),(F(0),F(1)))
h=((F(1),F(0)),(F(0),F(-1)))
e=((F(0),F(1)),(F(0),F(0)))
f=((F(0),F(0)),(F(1),F(0)))
def add(*xs): return tuple(tuple(sum(x[i][j] for x in xs) for j in range(2)) for i in range(2))
def scale(c,x): return tuple(tuple(c*v for v in row) for row in x)
def sub(x,y): return add(x,scale(-1,y))
def mul(x,y): return tuple(tuple(sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(x): return x[0][0]+x[1][1]
def inv(x):
    a,b=x[0]; c,d=x[1]; det=a*d-b*c
    return ((d/det,-b/det),(-c/det,a/det))
def comm(x,y): return sub(mul(x,y),mul(y,x))
def conj(A,x): return mul(mul(inv(A),x),A)
def tf(x): return sub(x,scale(tr(x)/2,I))
def wedge(x,Y,a,b): return sub(scale(x[a],Y[b]),scale(x[b],Y[a]))
def invent(n): return add(scale(n+1,h),scale(n*n-3,e),scale(2-n,f))

class AdditionalControls(unittest.TestCase):
    def test_physical_c_derivative_retains_transport_commutator(self):
        wrong_sign_detected=False
        for n in range(5):
            L=[invent(n+a) for a in range(4)]
            U=[invent(2*n-a) for a in range(4)]
            H={}; J={}
            for a in range(4):
                for b in range(a,4):
                    H[a,b]=H[b,a]=add(invent(n+2*a+b),scale(tr(mul(L[a],L[b]))/2,I))
                    J[a,b]=J[b,a]=add(invent(n-a+3*b),scale(tr(mul(U[a],U[b]))/2,I))
            for a,c,d in [(0,2,3),(1,2,3),(2,0,1),(3,0,1)]:
                DL=lambda b:sub(H[a,b],mul(L[a],L[b]))
                DU=lambda b:add(J[a,b],scale(-1,mul(U[a],U[b])),comm(U[b],L[a]))
                direct_terms=add(
                    mul(DU(c),L[d]),mul(U[c],DL(d)),
                    scale(-1,mul(DU(d),L[c])),scale(-1,mul(U[d],DL(c))))
                direct=tr(direct_terms)/4
                compact_terms=add(
                    mul(tf(J[a,c]),L[d]),scale(-1,mul(tf(J[a,d]),L[c])),
                    mul(U[c],tf(H[a,d])),scale(-1,mul(U[d],tf(H[a,c]))),
                    scale(-1,mul(add(L[a],U[a]),sub(mul(U[c],L[d]),mul(U[d],L[c])))))
                compact=tr(compact_terms)/4
                self.assertEqual(direct,compact)
                DUwrong=lambda b:add(J[a,b],scale(-1,mul(U[a],U[b])))
                wrong_terms=add(
                    mul(DUwrong(c),L[d]),mul(U[c],DL(d)),
                    scale(-1,mul(DUwrong(d),L[c])),scale(-1,mul(U[d],DL(c))))
                wrong=tr(wrong_terms)/4
                wrong_sign_detected |= wrong != compact
        self.assertTrue(wrong_sign_detected)

    def test_delta_E_on_four_vertices(self):
        frames=[I,add(I,scale(2,e)),add(I,scale(3,f)),((F(2),F(1)),(F(1),F(1)))]
        G={(i,j):mul(frames[j],inv(frames[i])) for i in range(4) for j in range(i+1,4)}
        W=[[invent(2*i+a) for a in range(4)] for i in range(4)]
        L={ij:[sub(conj(g,W[ij[1]][a]),W[ij[0]][a]) for a in range(4)] for ij,g in G.items()}
        x={(i,j):[F((i+1)*(j+2)+(i-j)*a+a*a) for a in range(4)] for i,j in G}
        triples=list(combinations(range(4),3))
        Fd={(i,j,k):[x[j,k][a]-x[i,k][a]+x[i,j][a] for a in range(4)] for i,j,k in triples}
        any_nonzero=False
        for a,b in combinations(range(4),2):
            E={}
            for i,j,k in triples:
                U=[conj(G[i,j],z) for z in L[j,k]]
                E[i,j,k]=scale(F(1,2),sub(wedge(x[j,k],L[i,j],a,b),wedge(x[i,j],U,a,b)))
            lhs=add(conj(G[0,1],E[1,2,3]),scale(-1,E[0,2,3]),E[0,1,3],scale(-1,E[0,1,2]))
            last=[conj(G[0,2],z) for z in L[2,3]]
            rhs=scale(F(-1,2),add(wedge(Fd[1,2,3],L[0,1],a,b),wedge(Fd[0,1,2],last,a,b)))
            self.assertEqual(lhs,rhs)
            any_nonzero |= lhs != Z
        self.assertTrue(any_nonzero)

    def test_every_five_factor_derivative_by_dual_multiplication(self):
        # Abstract product-rule check for the second trace in dK, including dI/dP/dh.
        # The factors are independent invented matrices; this is not a contraction model.
        def dualmul(x,y): return mul(x[0],y[0]),add(mul(x[1],y[0]),mul(x[0],y[1]))
        detects=[False]*5
        for n in range(3):
            factors=[(add(I,invent(n+j)),add(scale(j+1,I),invent(n-j))) for j in range(5)]
            product=(I,Z)
            for pair in factors: product=dualmul(product,pair)
            terms=[]
            for a in range(5):
                term=I
                for j,pair in enumerate(factors): term=mul(term,pair[int(a==j)])
                terms.append(term)
            self.assertEqual(product[1],add(*terms))
            for a,term in enumerate(terms): detects[a] |= tr(term) != 0
        self.assertTrue(all(detects))

if __name__=='__main__': unittest.main(verbosity=2)
