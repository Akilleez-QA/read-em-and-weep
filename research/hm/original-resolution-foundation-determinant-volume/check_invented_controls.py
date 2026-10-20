"""Tiny invented rational complexes only. This file never opens source inputs.

Ranks are (1,4,2,1), cohomology rank two. All matrices are at most 4 by 4.
The checks test the determinant-line proof, not any pinned physical matrix.
"""
from fractions import Fraction as F
from itertools import permutations

COUNT = 0

def require(ok, label):
    global COUNT
    if not ok:
        raise RuntimeError(label)
    COUNT += 1

def matrix(rows):
    return [[F(x) for x in row] for row in rows]

def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])

def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def cat(*arrays):
    return [sum((a[i] for a in arrays), []) for i in range(len(arrays[0]))]

def add(*arrays):
    return [[sum(a[i][j] for a in arrays) for j in range(len(arrays[0][0]))]
            for i in range(len(arrays[0]))]

def inv(a):
    n = len(a)
    u = [list(a[i]) + eye(n)[i] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if u[i][k])
        u[k], u[pivot] = u[pivot], u[k]
        factor = u[k][k]
        u[k] = [x / factor for x in u[k]]
        for i in range(n):
            if i != k:
                factor = u[i][k]
                u[i] = [x - factor * y for x, y in zip(u[i], u[k])]
    return [row[n:] for row in u]

def det(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        sign = -1 if sum(p[i] > p[j] for i in range(n) for j in range(i+1,n)) % 2 else 1
        term = F(sign)
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total

GAMMA = matrix([[1], [0], [0], [0]])
DELTA = matrix([[0, 0, 0, 1], [0, 0, 0, 0]])
EV = matrix([[0, 1]])
ES = matrix([[0], [0], [0], [1]])

def frame(f, w, r, shifts, lift):
    f = matrix(f)
    inclusion = [list(map(F, shifts)), f[0], f[1], [F(0), F(0)]]
    w, r = F(w), F(r)
    W = matrix([[w], [0]])
    eta = matrix([[r], [1]])
    L = matrix([[1/w, -r/w]])
    lift = matrix([[lift[0]], [lift[1]], [lift[2]], [w]])
    U = cat(GAMMA, inclusion, lift)
    Q = inv(U)
    H0, P = Q[:1], Q[1:3]
    H1 = mul(lift, L)
    V = cat(W, eta)
    require(Q[3:] == mul(L, DELTA), "last split row")
    require(add(mul(GAMMA,H0), mul(inclusion,P), mul(H1,DELTA)) == eye(4), "A identity")
    require(mul(H1,eta) == matrix([[0],[0],[0],[0]]), "B identity")
    require(mul(EV,DELTA) == matrix([[0,0,0,0]]), "C identity")
    require(mul(P,inclusion) == eye(2), "quotient left inverse")
    require(mul(DELTA,inclusion) == matrix([[0,0],[0,0]]), "closed inclusion")
    require(mul(EV,W) == matrix([[0]]), "kernel basis")
    lam = det(U)/det(V)
    N = cat(GAMMA,inclusion,ES)
    Y = cat(mul(DELTA,ES),eta)
    require(lam == det(N)/det(Y), "homotopy-free volume")
    require(lam == det(f), "normalized cohomology volume")
    return inclusion, P, lam

frames = [
    frame([[1,0],[0,1]], 1, 0, [0,0], [0,0,0]),
    frame([[2,1],[1,1]], -3, 5, [2,-7], [4,8,-2]),
    frame([[2,0],[0,1]], 7, -2, [-1,3], [9,-5,2]),
    frame([[0,1],[1,0]], -2, 6, [4,1], [3,7,11]),
]
for i, (Ii,Pi,li) in enumerate(frames):
    for j, (Ij,Pj,lj) in enumerate(frames):
        T = mul(Pi,Ij)
        require(det(T) == lj/li, "ordered transition determinant ratio")
        require(mul(T,mul(Pj,Ii)) == eye(2), "ordered transition inverse")
        Ci = matrix([[i+2,0],[0,F(1,i+2)]])
        Cj = matrix([[j+2,0],[0,F(1,j+2)]])
        require(det(mul(mul(inv(Ci),T),Cj)) == det(T), "reciprocal-frame invariance")

require(frames[0][2] == frames[1][2] == 1, "changed contractible lifts cancel")
require(frames[2][2] == 2, "unnormalized cohomology remains detectable")
require(frames[3][2] == -1, "cohomology orientation remains detectable")
print(f"PASS: {COUNT} exact invented rational controls; no source inputs were read.")
