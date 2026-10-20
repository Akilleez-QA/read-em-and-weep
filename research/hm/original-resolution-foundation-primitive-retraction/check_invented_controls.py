"""Tiny invented rational controls; no file/source/model reads or physical data.

All square matrices are at most 4x4. This checks the abstract residual theorem,
not the pinned inverse or any physical polynomial identity.
"""
from fractions import Fraction as F

COUNT = 0

def require(ok, label):
    global COUNT
    if not ok:
        raise RuntimeError(label)
    COUNT += 1

def mat(rows):
    return [[F(x) for x in row] for row in rows]

def zeros(r, c):
    return mat([[0] * c for _ in range(r)])

def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])

def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]

def sub(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def inv(a):
    n = len(a)
    z = [row[:] + unit for row, unit in zip(a, eye(n))]
    for c in range(n):
        pivot = next(r for r in range(c, n) if z[r][c])
        z[c], z[pivot] = z[pivot], z[c]
        divisor = z[c][c]
        z[c] = [x / divisor for x in z[c]]
        for r in range(n):
            if r != c:
                coefficient = z[r][c]
                z[r] = [x - coefficient * y for x, y in zip(z[r], z[c])]
    return [row[n:] for row in z]

def column(a, c):
    return [[row[c]] for row in a]

def zero(a):
    return all(x == 0 for row in a for x in row)

# Invented ranks (1,4,3,1), with one cohomology coordinate and two lifts.
N = mat([[2, 0, 0, 0], [3, 3, 0, 0],
         [5, 11, 1, 0], [7, 13, 0, 1]])
Ni = inv(N)
gamma, inclusion = column(N, 0), column(N, 1)
S = mat([[0, 0], [0, 0], [1, 0], [0, 1]])
H0 = mat([[F(1, 2), 0, 0, 0]])
W = mat([[1, 0], [0, 1], [0, 0]])
L = mat([[1, 0, 0], [0, 1, 0]])
ev, eta = mat([[0, 0, 1]]), mat([[0], [0], [1]])
M = mat([[2, 1], [1, 1]])
T0 = inv(M)
require(mul(Ni, N) == eye(4), 'invented basis inverse')

for defect in ('none', 'quotient', 'complex', 'inclusion', 'complement'):
    P = [Ni[1][:]]
    LD_N = mat([[0, 0, 2, 1], [0, 0, 1, 1]])
    T = [row[:] for row in T0]
    if defect == 'quotient':
        P[0][0] += 1
    elif defect == 'complex':
        LD_N[0][0] += 1
    elif defect == 'inclusion':
        LD_N[0][1] += 1
    elif defect == 'complement':
        T[0][0] += 1
    delta = mul(W, mul(LD_N, Ni))
    H1 = mul(S, mul(T, L))
    require(mul(H0, gamma) == eye(1), 'retraction')
    require(zero(mul(H0, inclusion)), 'H0I')
    require(zero(mul(H0, H1)), 'H0H1')
    require(mul(P, inclusion) == eye(1), 'PI')
    require(zero(mul(P, H1)), 'PH1')
    require(zero(mul(H1, eta)), 'B')
    require(zero(mul(ev, delta)), 'C')
    R = sub(add(add(mul(gamma, H0), mul(inclusion, P)), mul(H1, delta)), eye(4))
    pg, dg, di = mul(P, gamma), mul(L, mul(delta, gamma)), mul(L, mul(delta, inclusion))
    mm = mul(L, mul(delta, S))
    tc = sub(mul(T, mm), eye(2))
    tdg, tdi = mul(T, dg), mul(T, di)
    expected = [mat([[0, 0, 0, 0]])[0], [pg[0][0], F(0), F(0), F(0)],
                [tdg[0][0], tdi[0][0]] + tc[0],
                [tdg[1][0], tdi[1][0]] + tc[1]]
    require(mul(Ni, mul(R, N)) == expected, 'exact defect normal form')
    require(zero(R) == (zero(pg) and zero(dg) and zero(di) and zero(tc)), 'four-family equivalence')
    require(zero(R) == (defect == 'none'), 'separate defect detected')
    if defect == 'quotient':
        require(P != [Ni[1]], 'P must not be assumed to be middle inverse row')

print(f'PASS: {COUNT} tiny invented rational controls; each remaining defect is retained.')
print('No source/model files, physical matrices, source values, or jets were read or evaluated.')
