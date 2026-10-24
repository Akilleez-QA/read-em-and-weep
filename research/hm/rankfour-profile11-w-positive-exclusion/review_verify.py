#!/usr/bin/env python3
"""Independent fixed-character/degree audit of the W-positive exclusion.

No author module is imported, and no actual coefficient, parameter, point,
jet, tensor, matrix, or instance rank is selected or evaluated. Every test
raises RuntimeError explicitly and remains active under python -O.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
PROOF_SHA256 = 'eacf658ecef85350c36591f25f80cae14408869d56f077d371982a5311e0232f'
INPUTS_SHA256 = 'be7b276db775e62a3e6559ca1d5bc106eb05aaedc89b67b6e9805131645a4a9b'
AUTH_SHA256 = 'aecf7d7ad3848965fe1f627f17040db5373267047be22bcba47afbcc5447ae69'
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def blob_digest(data):
    header = b'blob ' + str(len(data)).encode('ascii') + b'\0'
    return hashlib.sha1(header + data).hexdigest()


def required_bytes(relative):
    path = ROOT / relative
    require(path.is_file(), 'Missing required file: ' + relative)
    return path.read_bytes()


proof_bytes = required_bytes('PROOF.md')
require(digest(proof_bytes) == PROOF_SHA256, 'Frozen whole-proof bytes changed')
input_bytes = required_bytes('INPUTS.json')
require(digest(input_bytes) == INPUTS_SHA256, 'Mandatory input-manifest bytes changed')
auth_bytes = required_bytes('REVIEW-AUTHENTICITY.json')
require(digest(auth_bytes) == AUTH_SHA256, 'Fresh source-authentication record changed')
inputs = json.loads(input_bytes)
authentication = json.loads(auth_bytes)
require(isinstance(inputs, list) and len(inputs) == 3, 'Expected three complete direct sources')
require(isinstance(authentication.get('sources'), list), 'Missing fresh-authentication source records')

EXPECTED_SOURCES = {
    'research/hm/rankfour-profile11-full-decentic-span/PROOF.md': {
        'ref': 'd269346fefc80e5beb3115ad010bd4d1837a9a5c',
        'sha256': 'f7952c7e28fe1cb4c31dffb3b4017e891b09b1bfd94012d583760840c7d043c3',
        'git_blob_sha1': '80d7ccb946eb9e511abe7734a082fa1d047a82e2',
        'bytes': 7025,
    },
    'research/hm/rankfour-profile11-apolar-constant-exclusions/PROOF.md': {
        'ref': '62ec109e8960848ae9081a17141b30228b598a70',
        'sha256': 'e5d2c74f516bb5b2ede85287fceb3a774c6870b68b7b2418398e30fd5093d9b2',
        'git_blob_sha1': 'de0eacee65c0c738e87ed8ce47ad9582a8e76313',
        'bytes': 15110,
    },
    'research/hm/rankfour-profile11-top-four-pair-image/PROOF.md': {
        'ref': '972993db6a0ab4f2a65f4f8da39cd3862923238d',
        'sha256': 'db1e23909dbabd423cbeb855f0f376e7e0fac53d557fdd8aef7685b5449edfdb',
        'git_blob_sha1': '12cbf71fd50a623cc5e7daa4fcc3835bd016d460',
        'bytes': 13500,
    },
}
require({entry.get('path') for entry in inputs} == set(EXPECTED_SOURCES),
        'Direct-source set differs from the independently reviewed set')
require({entry.get('path') for entry in authentication['sources']} == set(EXPECTED_SOURCES),
        'Fresh-authentication source set is incomplete')
for source in inputs:
    path = source['path']
    expected = EXPECTED_SOURCES[path]
    for key in ('ref', 'sha256', 'git_blob_sha1', 'bytes'):
        require(source.get(key) == expected[key], 'Wrong immutable source field: ' + path + '/' + key)
    url = 'https://github.com/Akilleez-QA/read-em-and-weep/blob/' + expected['ref'] + '/' + path
    require(source.get('url') == url, 'Wrong exact original-source URL')
    retained = required_bytes(source['file'])
    require(len(retained) == expected['bytes'], 'Wrong retained-source byte length')
    require(digest(retained) == expected['sha256'], 'Changed retained-source SHA256')
    require(blob_digest(retained) == expected['git_blob_sha1'], 'Changed retained-source Git blob identity')
    matches = [entry for entry in authentication['sources'] if entry.get('path') == path]
    require(len(matches) == 1, 'Fresh original authentication is not unique')
    fresh_record = matches[0]
    for key in ('ref', 'sha256', 'git_blob_sha1', 'bytes'):
        require(fresh_record.get(key) == expected[key], 'Wrong fresh-source field: ' + path + '/' + key)
    require(fresh_record.get('url') == url and fresh_record.get('matches_retained') is True,
            'Fresh original read did not authenticate the exact retained source')


@dataclass(frozen=True)
class Quadratic:
    """An exact element a+b*sqrt(5)."""
    a: F = F(0)
    b: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', F(self.a))
        object.__setattr__(self, 'b', F(self.b))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Quadratic) else Quadratic(value)

    def __add__(self, other):
        other = self.coerce(other)
        return Quadratic(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Quadratic(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Quadratic(self.a * other.a + 5*self.b*other.b,
                         self.a*other.b + self.b*other.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        require(isinstance(n, int) and 0 <= n <= 10, 'Power outside fixed character requirements')
        product = Quadratic(1)
        for _ in range(n):
            product = product * self
        return product

    def conjugate(self):
        return Quadratic(self.a, -self.b)

    def integer(self, denominator=1):
        result = self.a / denominator
        require(self.b == 0 and result.denominator == 1, 'Nonintegral exact character multiplicity')
        return int(result)


# One fixed nine-class binary-icosahedral character table. The physical W is
# fixed; the other doublet is its Galois conjugate, not a relabelled W.
CLASS_SIZES = (1, 1, 30, 20, 20, 12, 12, 12, 12)
phi = Quadratic(F(1, 2), F(1, 2))
W = tuple(Quadratic.coerce(x) for x in (2, -2, 0, 1, -1, phi, -phi, phi-1, 1-phi))
WP = tuple(x.conjugate() for x in W)
ONE = (Quadratic(1),) * 9
ZERO = (Quadratic(0),) * 9


def add(*characters):
    return tuple(sum(values, Quadratic()) for values in zip(*characters)) if characters else ZERO


def scale(n, character):
    return tuple(n*x for x in character)


def tensor(left, right):
    return tuple(x*y for x, y in zip(left, right))


def sym(n, trace=W):
    require(n in (2, 3, 4, 5, 6, 7, 10), 'Symmetric power outside fixed proof requirements')
    # Closed Chebyshev polynomial, not the author's McKay recursion.
    return tuple(sum(((-1)**j * comb(n-j, j) * x**(n-2*j)
                      for j in range(n//2+1)), Quadratic()) for x in trace)


CHAR = {'one':ONE, 'W':W, 'Wp':WP, 'A':sym(2), 'V':sym(2, WP),
        'S':sym(3), 'D':sym(4), 'T':sym(5), 'P':tensor(W, WP)}
DIM = {'one':1, 'W':2, 'Wp':2, 'A':3, 'V':3, 'S':4, 'D':5, 'T':6, 'P':4}


def linear(coefficients):
    return add(*(scale(n, CHAR[name]) for name, n in coefficients.items()))


def inner(left, right):
    return sum((s*x*y for s, x, y in zip(CLASS_SIZES, left, right)), Quadratic()).integer(120)


def decompose(character):
    coefficients = {name:inner(character, irrep) for name, irrep in CHAR.items()}
    require(all(n >= 0 for n in coefficients.values()), 'Needed character is not genuine')
    require(linear(coefficients) == character, 'Full exact character reconstruction failed')
    return {name:n for name, n in coefficients.items() if n}


def dim(coefficients):
    return sum(DIM[name]*n for name, n in coefficients.items())


require(sum(CLASS_SIZES) == 120, 'Wrong class-size sum')
require(sum(n*n for n in DIM.values()) == 120, 'Wrong irreducible dimension-square sum')
for name, character in CHAR.items():
    require(character[0].integer() == DIM[name], 'Wrong dimension for ' + name)
    for other, other_character in CHAR.items():
        require(inner(character, other_character) == int(name == other),
                'Irreducible orthogonality failed: ' + name + '/' + other)

SYM6 = decompose(sym(6))
SYM7 = decompose(sym(7))
SYM10 = decompose(sym(10))
require(SYM6 == {'V':1, 'P':1}, 'Wrong universal first predecessor character')
require(SYM7 == {'Wp':1, 'T':1}, 'Wrong universal complete second-jet kernel character')
require(SYM10 == {'A':1, 'V':1, 'D':1}, 'Wrong full degree-ten coefficient character')
require(decompose(tensor(W, WP)) == {'P':1}, 'Wrong marked physical W tensor Wprime')
require(inner(CHAR['V'], tensor(WP, W)) == 0, 'Quartic V has a forbidden Wprime-target component')
require(inner(WP, sym(7)) == 1, 'The degree-seven line Hom is not one-dimensional')
require(inner(CHAR['Wp'], CHAR['T']) == 0, 'Cubic source blocks are not inequivalent')
require(inner(CHAR['V'], linear(SYM6)) == 1, 'The two quartic V rows have more than one V target')
require(inner(CHAR['V'], CHAR['P']) == 0, 'A constant quartic V-to-P map is possible')

C = {'A':2, 'V':2, 'P':1, 'D':1}
N = decompose(add(linear(C), scale(-1, linear(SYM10))))
require(dim(C) == 21 and dim(SYM10) == 11, 'Wrong actual full-span dimensions')
require(N == {'A':1, 'V':1, 'P':1} and dim(N) == 10, 'Wrong genuine constant kernel character')
require(dim({'V':1, 'P':1}) == 7 and 8 > 7,
        'Rank-eight constant span is not forced to add the A constituent')

# E0 and the universal second-jet kernel J, with only fixed rank/degree data.
e0_rank = 5 + 8 + 3
e0_degree = 5*(-2) + 8*(-3) + 3*(-4)
j_rank = 10 + 1 - 3
j_degree = j_rank * (-3)
require((e0_rank, e0_degree) == (16, -46), 'Wrong E0 rank or degree')
require((j_rank, j_degree) == (8, -24), 'Wrong complete second-jet kernel rank or degree')
minimum_image_rank = e0_rank - dim(N)
require(minimum_image_rank == 6, 'Wrong minimum actual q(E0) rank')
require(2 + 3 < minimum_image_rank, 'Vanishing T scalar was not excluded')
require(11 - 6 == 5 and 21 > 11,
        'Vanishing Wprime scalar does not give the stated full-span contradiction')
require(2 + 6 == j_rank, 'Both nonzero cubic scalars do not fill J')

f0_rank = e0_rank - j_rank
f0_degree = e0_degree - j_degree
sn_rank = dim(N) - f0_rank
sn_degree = f0_degree
require((f0_rank, f0_degree) == (8, -22), 'Wrong actual constant-kernel intersection')
require(5 + 3 == f0_rank and 5*(-2) + 3*(-4) == f0_degree,
        'Graph cancellation has the wrong source rank or degree')
require((sn_rank, sn_degree) == (2, -22), 'Wrong actual annihilator quotient rank or degree')
require(5 - 3 == sn_rank and -46 - (-24) == sn_degree,
        'Residual restriction does not have equal rank and degree')
require(2*(-11) == sn_degree, 'Projected Wprime(-11) degree does not match')

# The actual K is imported, and q(K) is used only by its structural rank bound.
k_rank = 4 + 2*3 + 2 + 1
k_degree = 4*(-3) + 2*3*(-4) + 2*(-5) - 10
jminus_rank = 10 + 1 - 4
jminus_degree = jminus_rank * (-4)
require((k_rank, k_degree) == (13, -56), 'Wrong actual K rank or degree')
require((jminus_rank, jminus_degree) == (7, -28), 'Wrong universal J-minus rank or degree')
require(-4 - (-3) < 0, 'The cubic K block can map to the pure quartic target')
qk_rank_bound = 0 + 3 + 2 + 1
require(qk_rank_bound == 6, 'Wrong K-image rank capacity')
require(k_rank - qk_rank_bound == 7, 'Wrong derivative-kernel lower rank bound')
require(f0_rank - (k_rank - qk_rank_bound) == 1, 'Wrong actual F0 derivative-rank bound')

# The actual top-D row, the saturated degree-seven line, and exact image degree.
d_rank, d_degree = 5, -10
s_rank, s_degree = 4, -12
line_degree = d_degree - s_degree
require(d_rank - s_rank == 1 and line_degree == 2, 'Wrong top-D quotient line')
sn_dual_twist_degree = 11 - 2
entry_degree = sn_dual_twist_degree - line_degree
require(entry_degree == 7, 'Wrong homogeneous degree of the line entries')
projective_orbit_sizes = tuple(60 // stabilizer for stabilizer in (1, 2, 3, 5))
require(projective_orbit_sizes == (60, 30, 20, 12), 'Wrong possible A5 point orbit sizes')
require(entry_degree < min(projective_orbit_sizes), 'A nonempty invariant common-zero divisor is possible')
f1_rank = f0_rank - 1
f1_degree = f0_degree - line_degree
require((f1_rank, f1_degree) == (7, -24), 'Wrong exact first derivative kernel')

# Seven actual successive rank-one quotients. No bundle-domain search occurs.
line_capacity = tuple(line_degree - 2*j for j in range(1, f1_rank+1))
require(line_capacity == (0, -2, -4, -6, -8, -10, -12), 'Wrong seven successive quotient-degree bounds')
for j in range(1, len(line_capacity)):
    require(line_capacity[j] == line_capacity[j-1] - 2, 'Wrong one-form twist in capacity recursion')
capacity_total = sum(line_capacity)
require(capacity_total == -42, 'Wrong total rank-one kernel capacity')
require(f1_degree > capacity_total, 'The final rank-one capacity contradiction is absent')
require(f1_degree - capacity_total == 18, 'Wrong degree contradiction gap')

print(json.dumps({
    'status':'PASS',
    'checks':CHECKS,
    'proof_sha256':PROOF_SHA256,
    'inputs_sha256':INPUTS_SHA256,
    'authentication_sha256':AUTH_SHA256,
    'complete_jet_kernel':{'rank':j_rank, 'degree':j_degree, 'character':SYM7},
    'constant_kernel':{'rank':dim(N), 'character':N},
    'actual_intersection':{'rank':f0_rank, 'degree':f0_degree},
    'actual_first_kernel':{'rank':f1_rank, 'degree':f1_degree},
    'successive_line_degree_upper_bounds':list(line_capacity),
    'degree_capacity':capacity_total,
    'contradiction_gap':f1_degree-capacity_total,
    'scope':'Fixed universal characters, source-byte authentication and structural rank-degree arithmetic only. The sheaf-theoretic argument is independently reviewed, not machine-certified.',
}, sort_keys=True, indent=2))
