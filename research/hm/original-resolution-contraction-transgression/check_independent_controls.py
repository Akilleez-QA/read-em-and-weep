"""Tiny invented controls only. No repository source evaluator or model is imported."""
from fractions import Fraction as F
from itertools import permutations, combinations
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
def conj(A,x): return mul(mul(inv(A),x),A)
def tf(x): return sub(x,scale(tr(x)/2,I))
def wedge(x,Y,a,b): return sub(scale(x[a],Y[b]),scale(x[b],Y[a]))
def parity(p): return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))

def Q2(L,U,H,J,order=(0,1,2,3)):
    a,b,c,d=order
    S=((a,c,b,d,1),(a,d,b,c,-1),(b,c,a,d,-1),(b,d,a,c,1))
    out=Z
    for a,b,c,d,eps in S:
        Hab=tf(H.get((c,d),Z)); Jab=tf(J.get((a,b),Z))
        term=add(
            scale(tr(mul(U[a],U[b]))+tr(mul(U[a],L[b]))+tr(mul(U[b],L[a])),Hab),
            scale(-tr(mul(Hab,U[a])),L[b]),scale(-tr(mul(Hab,U[b])),L[a]),
            scale(tr(mul(L[c],L[d]))+tr(mul(U[c],L[d]))+tr(mul(U[d],L[c])),Jab),
            scale(-tr(mul(Jab,L[c])),U[d]),scale(-tr(mul(Jab,L[d])),U[c]))
        out=add(out,scale(F(eps,8),term))
    return out

class IndependentControls(unittest.TestCase):
    def test_rational_germ_q2_and_sign_projection(self):
        # A=diag(1+x2*x4,(1+x2*x4)^-1),
        # B=diag((1+x1)*(1+x3),((1+x1)*(1+x3))^-1).
        # Exact distinct-coordinate Taylor coefficients at the origin.
        L=[Z]*4; U=[h,Z,h,Z]
        H={(1,3):h,(3,1):h}
        J={(0,2):I,(2,0):I}
        self.assertEqual(Q2(L,U,H,J),scale(F(1,4),h))
        alt=Z
        for p in permutations(range(4)):
            alt=add(alt,scale(F(parity(p),24),Q2(L,U,H,J,p)))
        self.assertEqual(alt,Z)
        self.assertNotEqual(Q2(L,U,H,J),Z)

    def test_transgression_noncommuting_transport(self):
        A=((F(1),F(2)),(F(0),F(1)))
        B=((F(1),F(0)),(F(3),F(1)))
        G={(0,1):A,(1,2):B,(0,2):mul(B,A)}
        theta=[[add(scale(i+a+1,h),scale(2*i-a,e),scale(i*a-1,f)) for a in range(4)] for i in range(3)]
        W=[[add(scale(i-a,h),scale(i+2*a+1,e),scale(2*i-a+2,f)) for a in range(4)] for i in range(3)]
        x={(0,1):list(map(F,[1,3,2,7])),(1,2):list(map(F,[2,-1,5,4])),(0,2):list(map(F,[-3,4,1,6]))}
        L={ij:[sub(conj(g,W[ij[1]][a]),W[ij[0]][a]) for a in range(4)] for ij,g in G.items()}
        chi={ij:[sub(sub(conj(g,theta[ij[1]][a]),theta[ij[0]][a]),L[ij][a]) for a in range(4)] for ij,g in G.items()}
        U=[conj(A,z) for z in L[1,2]]
        chi12=[conj(A,z) for z in chi[1,2]]
        dF=[x[1,2][a]-x[0,2][a]+x[0,1][a] for a in range(4)]
        endpoint=[add(theta[0][a],conj(G[0,2],theta[2][a])) for a in range(4)]
        for a,b in combinations(range(4),2):
            C={ij:scale(F(1,2),wedge(x[ij],[add(theta[ij[0]][r],conj(g,theta[ij[1]][r])) for r in range(4)],a,b)) for ij,g in G.items()}
            deltaC=add(conj(A,C[1,2]),scale(-1,C[0,2]),C[0,1])
            E=scale(F(1,2),sub(wedge(x[1,2],L[0,1],a,b),wedge(x[0,1],U,a,b)))
            defect=scale(F(1,2),add(wedge(x[1,2],chi[0,1],a,b),scale(-1,wedge(x[0,1],chi12,a,b)),wedge(dF,endpoint,a,b)))
            self.assertEqual(sub(deltaC,defect),E)
        # The tested corrections genuinely survive, so zero-defect testing is not enough.
        self.assertNotEqual(defect,Z)

if __name__=='__main__': unittest.main(verbosity=2)
