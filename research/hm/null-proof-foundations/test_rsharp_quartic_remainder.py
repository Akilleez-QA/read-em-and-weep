"""Formal sl2 multilinear identities only; never imports or evaluates HM data."""
import itertools
import unittest

ZERO=(0,0,0)
BASIS=((1,0,0),(0,1,0),(0,0,1))
def add(*vs): return tuple(sum(v[i] for v in vs) for i in range(3))
def sc(a,v): return tuple(a*x for x in v)
def br(v,w):
    z,x,y=v; Z,X,Y=w
    return (x*Y-y*X,2*(z*X-x*Z),2*(y*Z-z*Y))
def dot(v,w):
    z,x,y=v; Z,X,Y=w
    return 2*z*Z+x*Y+y*X

def pieces(L,U):
    pairs=((0,1),(2,3))
    BL=[br(L[a],L[b]) for a,b in pairs]
    BU=[br(U[a],U[b]) for a,b in pairs]
    Mix=[add(br(L[a],U[b]),br(U[a],L[b])) for a,b in pairs]
    Delta=[dot(U[a],L[b])-dot(U[b],L[a]) for a,b in pairs]
    quadratic=add(br(BU[0],BL[1]),br(BU[1],BL[0]))
    raw=quadratic
    r22=quadratic
    r31=ZERO
    for p,(a,b) in enumerate(pairs):
        r=1-p
        q=sc(2,add(sc(dot(U[a],BU[r]),L[b]),sc(-dot(U[b],BU[r]),L[a]),
                   sc(dot(L[b],BL[r]),U[a]),sc(-dot(L[a],BL[r]),U[b])))
        raw=add(raw,q,sc(-2*Delta[p],add(BL[r],BU[r],Mix[r])))
        r22=add(r22,sc(-2*Delta[p],Mix[r]))
        r31=add(r31,br(U[b],br(L[a],BU[r])),sc(-1,br(U[a],br(L[b],BU[r]))),
                   br(L[a],br(U[b],BL[r])),sc(-1,br(L[b],br(U[a],BL[r]))))
    return raw,r22,r31

class QuarticRemainder(unittest.TestCase):
    def test_all_1296_multilinear_basis_cases(self):
        count=0
        for assignment in itertools.product((0,1),repeat=4):
            for vectors in itertools.product(BASIS,repeat=4):
                L=[ZERO if assignment[i] else vectors[i] for i in range(4)]
                U=[vectors[i] if assignment[i] else ZERO for i in range(4)]
                raw,r22,r31=pieces(L,U)
                self.assertEqual(raw,add(r22,r31),(assignment,vectors))
                if sum(assignment)==2: self.assertEqual(r31,ZERO)
                else: self.assertEqual(r22,ZERO)
                count+=1
        self.assertEqual(count,1296)

    def test_exact_assignment_support(self):
        for assignment in itertools.product((0,1),repeat=4):
            nonzero=False
            for vectors in itertools.product(BASIS,repeat=4):
                L=[ZERO if assignment[i] else vectors[i] for i in range(4)]
                U=[vectors[i] if assignment[i] else ZERO for i in range(4)]
                nonzero |= pieces(L,U)[0] != ZERO
            self.assertEqual(nonzero,0 < sum(assignment) < 4,assignment)

    def test_pair_separated_survivor(self):
        h,e,f=BASIS
        L=[h,e,ZERO,ZERO]
        U=[ZERO,ZERO,h,f]
        raw,r22,r31=pieces(L,U)
        self.assertEqual(raw,(4,0,0)) # This is 32 times Q4, hence Q4=h/8.
        self.assertEqual(raw,r22)
        self.assertEqual(r31,ZERO)

if __name__=='__main__': unittest.main(verbosity=2)
