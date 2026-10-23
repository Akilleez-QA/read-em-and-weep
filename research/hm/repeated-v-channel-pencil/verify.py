#!/usr/bin/env python3
"""Bounded universal representation checks. No actual HM/source data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
checks = []


def check(label, condition):
    if not condition:
        raise RuntimeError(label)
    checks.append(label)


# Exact sparse polynomial ring Q[u0,u1,s0,s1].
class P:
    def __init__(self, value=0):
        if isinstance(value, P):
            self.d = dict(value.d)
        elif isinstance(value, dict):
            self.d = {m: F(c) for m, c in value.items() if c}
        else:
            self.d = {} if not value else {(0, 0, 0, 0): F(value)}

    def __add__(self, other):
        d = dict(self.d)
        for m, c in P(other).d.items():
            d[m] = d.get(m, F(0)) + c
        return P(d)

    __radd__ = __add__

    def __neg__(self):
        return P({m: -c for m, c in self.d.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        d = {}
        for a, x in self.d.items():
            for b, y in P(other).d.items():
                m = tuple(v + w for v, w in zip(a, b))
                d[m] = d.get(m, F(0)) + x*y
        return P(d)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.d == P(other).d


def var(i):
    m = [0]*4
    m[i] = 1
    return P({tuple(m): 1})


def add(A, B):
    return [[x+y for x, y in zip(a, b)] for a, b in zip(A, B)]


def scale(c, A):
    return [[c*x for x in row] for row in A]


def mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return A[0][0]+A[1][1]


def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def rank2(A):
    if det(A):
        return 2
    return int(any(x for row in A for x in row))


I = [[P(1), P(0)], [P(0), P(1)]]
Z = [[P(0), P(0)], [P(0), P(0)]]
u0, u1, s0, s1 = [var(i) for i in range(4)]
K = [[u0*s0, u0*s1], [u1*s0, u1*s1]]
t = tr(K)
C0 = K
C1 = scale(F(1, 4), add(scale(3, K), scale(-1, I)))
C2 = scale(F(3, 20), add(K, I))
S = scale(F(1, 10), add(scale(9, K), scale(-1, I)))

for e in json.loads((ROOT/'INPUTS.json').read_text()):
    raw = (ROOT/e['local_path']).read_bytes()
    check(e['label']+' SHA256', hashlib.sha256(raw).hexdigest() == e['sha256'])
    blob = b'blob '+str(len(raw)).encode()+b'\0'+raw
    check(e['label']+' Git blob', hashlib.sha1(blob).hexdigest() == e['git_blob'])

check('K determinant', det(K) == 0)
check('rank-one polynomial identity', mul(K, K) == scale(t, K))
check('channel commutativity', C0 == add(C1, scale(F(5, 3), C2)))
check('invariant contraction Id', add(scale(-1, C1), scale(5, C2)) == I)
check('traceless coefficient', add(C1, C2) == S)
J = add(scale(10, S), I)
check('S determinant identity', det(J) == 0)
check('S polynomial identity', mul(J, J) == scale(10*tr(S)+2, J))
check('V determinant factor', det(add(scale(3, K), scale(-1, I))) == 1-3*t)
check('D determinant factor', det(add(K, I)) == 1+t)
check('distinct singularity roots', F(1, 3) != -1)
h = [[-s1], [s0]]
check('canonical scalar kernel', mul([[s0, s1]], h) == [[P(0)]])
check('K kills scalar kernel', mul(K, h) == [[P(0)], [P(0)]])
check('V coefficient on scalar kernel', mul(C1, h) == scale(F(-1, 4), h))
check('D coefficient on scalar kernel', mul(C2, h) == scale(F(3, 20), h))

# All basis triples of the universal orthogonal three-space, not HM points.
def Fs(i, j, k):
    f0 = [F(int(r == i and j == k)) for r in range(3)]
    f1 = [F(int(r == j and i == k)-int(r == k and i == j)) for r in range(3)]
    f2 = [F(int(r == j and i == k)+int(r == k and i == j))
          -F(2, 3)*int(r == i and j == k) for r in range(3)]
    return f0, f1, f2


def tensor(i, j, k):
    f = Fs(i, j, k)
    return [add(add(scale(f[0][r], C0), scale(f[1][r], C1)),
                scale(f[2][r], C2)) for r in range(3)]


for i in range(3):
    for j in range(3):
        for k in range(3):
            check('universal symmetry '+str((i, j, k)), tensor(i, j, k) == tensor(j, i, k))
for k in range(3):
    contraction = [Z for _ in range(3)]
    for i in range(3):
        value = tensor(i, i, k)
        contraction = [add(a, b) for a, b in zip(contraction, value)]
    check('universal contraction '+str(k), contraction == [I if r == k else Z for r in range(3)])

# Canonical dimensions imported from exact characters, not selected ranks.
dim = {'1': 1, 'A': 3, 'V': 3, 'P': 4, 'D': 5}
N2 = {'A': 1, 'V': 2, 'P': 3, 'D': 4}
P3 = {'1': 1, 'A': 4, 'V': 2, 'P': 3, 'D': 3}
N4 = {'V': 2, 'P': 4, 'D': 3}
reachable = {'1': 1, 'A': 3, 'V': 2, 'P': 3, 'D': 3}
for label, char, expected in [('N2', N2, 41), ('P3', P3, 46), ('N4', N4, 37), ('reachable', reachable, 43)]:
    check(label+' character dimension', sum(dim[j]*n for j, n in char.items()) == expected)
check('unique actual intermediate scalar', P3['1'] == reachable['1'] == 1)
check('full repeated V source and target', N2['V'] == N4['V'] == 2)
possibilities = [(r1, r2) for r1 in [1, 2] for r2 in [1, 2] if 2 in (r1, r2)]
check('all allowed support dimensions', {1+3*r1+5*r2 for r1, r2 in possibilities} == {12, 14, 17})
check('scalar-kernel restriction dimension', dim['V']+dim['D'] == 8)

# Four exact universal positive diagrams. These are not HM instances.
models = []
for value, expected in [(F(-1), 12), (F(1, 3), 14), (F(1), 17), (F(0), 17)]:
    km = [[value, F(0)], [F(0), F(0)]]
    im = [[F(1), F(0)], [F(0), F(1)]]
    c1 = scale(F(1, 4), add(scale(3, km), scale(-1, im)))
    c2 = scale(F(3, 20), add(km, im))
    rank = 1+3*rank2(c1)+5*rank2(c2)
    check('sharpness dimension t='+str(value), rank == expected)
    check('sharpness commutativity t='+str(value), km == add(c1, scale(F(5, 3), c2)))
    check('sharpness contraction t='+str(value), add(scale(-1, c1), scale(5, c2)) == im)
    models.append({'formal_trace': str(value), 'first_arrow_image_dimension': rank})

# Polynomial factorization of the two incidences with lambda=(1,0), h=e2.
check('incidence polynomial factor', K[0][1] == u0*s1)
check('trace-free channel ratio on h', C0[0][1]*F(3, 4) == C1[0][1]
      and C0[0][1]*F(3, 20) == C2[0][1])
for label, row, column, expected in [
    ('kernel incidence only', [1, 0], [1, 0], (False, True, True)),
    ('output incidence only', [0, 1], [0, 1], (True, False, True)),
    ('neither incidence', [1, 1], [1, 0], (False, False, False)),
    ('zero second arrow', [1, 1], [0, 0], (True, False, True)),
]:
    output_residual = column[0] == 0
    kernel_equal = row[1] == 0
    projected_zero = column[0]*row[1] == 0
    check(label, (output_residual, kernel_equal, projected_zero) == expected)
    check(label+' equivalence', projected_zero == (output_residual or kernel_equal))

result = {
    'status': 'PASS',
    'checks': len(checks),
    'scope': 'Bounded exact universal representation identities; no actual HM/source evaluation.',
    'allowed_first_arrow_dimensions': [12, 14, 17],
    'canonical_scalar_kernel_dimension': 8,
    'universal_sharpness': models,
}
print(json.dumps(result, indent=2, sort_keys=True))
