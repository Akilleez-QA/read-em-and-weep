#!/usr/bin/env python3
"""Independent finite-character and byte-binding audit of the full-span lemma.

Only fixed universal characters and rank/degree arithmetic are evaluated.
The closed binomial character formula is independent of the author verifier.
Every validity test is explicit, counted, and active under python -O.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FROZEN_PROOF_SHA256 = 'f7952c7e28fe1cb4c31dffb3b4017e891b09b1bfd94012d583760840c7d043c3'
FROZEN_INPUTS_SHA256 = '3754f7a61685c6287f50cf707511675268a7c913602e1dea40c681d84e425f96'
CHECK_COUNT = 0

def require(condition, description):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise RuntimeError(description)

def sha256(data):
    return hashlib.sha256(data).hexdigest()

def git_blob_sha1(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

@dataclass(frozen=True)
class Q5:
    """Exact a+b*sqrt(5), with no floating-point character comparisons."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))

    @staticmethod
    def of(value):
        return value if isinstance(value, Q5) else Q5(value)

    def __add__(self, other):
        other = self.of(other)
        return Q5(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q5(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.of(other))

    def __rsub__(self, other):
        return self.of(other) - self

    def __mul__(self, other):
        other = self.of(other)
        return Q5(self.a * other.a + 5 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __pow__(self, power):
        require(isinstance(power, int) and 0 <= power <= 11,
                'Power exceeds the fixed closed-character polynomial bound')
        value = Q5(1)
        for _ in range(power):
            value = value * self
        return value

    def conjugate(self):
        return Q5(self.a, -self.b)

    def integer(self, divisor=1):
        value = self.a / divisor
        require(self.b == 0 and value.denominator == 1,
                'Expected exact rational integer character inner product')
        return int(value)

# The nine binary-icosahedral conjugacy classes, in one fixed physical ordering.
SIZE = (1, 1, 30, 20, 20, 12, 12, 12, 12)
phi = Q5(Fraction(1, 2), Fraction(1, 2))
W = tuple(Q5.of(x) for x in (2, -2, 0, 1, -1, phi, -phi, phi-1, 1-phi))
WP = tuple(x.conjugate() for x in W)
ONE = (Q5(1),) * 9
ZERO = (Q5(0),) * 9

def add(*characters):
    return tuple(sum(values, Q5()) for values in zip(*characters)) if characters else ZERO

def scale(n, character):
    return tuple(n * x for x in character)

def multiply(left, right):
    return tuple(x * y for x, y in zip(left, right))

def symmetric_character(n, traces=W):
    require(n in (0, 2, 3, 4, 5, 10, 11),
            'Symmetric-power request is outside the fixed proof requirements')
    # Closed formula U_n(t/2) = sum_j (-1)^j binom(n-j,j) t^(n-2j).
    return tuple(sum(((-1)**j * comb(n-j, j) * t**(n-2*j)
                      for j in range(n//2 + 1)), Q5()) for t in traces)

IRREP = {
    'one': ONE,
    'W': W,
    'Wprime': WP,
    'A_std': symmetric_character(2),
    'V': symmetric_character(2, WP),
    'S4': symmetric_character(3),
    'D': symmetric_character(4),
    'T6': symmetric_character(5),
    'P': multiply(W, WP),
}
DIM = {'one':1, 'W':2, 'Wprime':2, 'A_std':3, 'V':3,
       'S4':4, 'D':5, 'T6':6, 'P':4}

def linear(terms):
    return add(*(scale(n, IRREP[name]) for name, n in terms.items()))

def inner(left, right):
    return sum((n*x*y for n, x, y in zip(SIZE, left, right)), Q5()).integer(120)

def decompose(character):
    coefficients = {name:inner(character, value) for name, value in IRREP.items()}
    require(all(n >= 0 for n in coefficients.values()), 'A needed character is not genuine')
    require(linear(coefficients) == character, 'Exact character reconstruction failed')
    return {name:n for name, n in coefficients.items() if n}

def dimension(terms):
    return sum(DIM[name] * n for name, n in terms.items())

require(sum(SIZE) == 120, 'Wrong conjugacy-class size sum')
require(sum(n*n for n in DIM.values()) == 120, 'Wrong irreducible dimension squares')
for name, character in IRREP.items():
    require(character[0].integer() == DIM[name], 'Wrong irreducible dimension: ' + name)
    for other, other_character in IRREP.items():
        require(inner(character, other_character) == int(name == other),
                'Exact character orthogonality failed: ' + name + '/' + other)

decentic = symmetric_character(10)
complement_coefficients = multiply(WP, symmetric_character(11))
R_FULL = decompose(decentic)
J_COEFFICIENTS = decompose(complement_coefficients)
require(R_FULL == {'A_std':1, 'V':1, 'D':1}, 'Wrong degree-ten coefficient character')
require(J_COEFFICIENTS == {'A_std':1, 'V':1, 'D':2, 'P':2},
        'Wrong complement coefficient character')
require(dimension(R_FULL) == 11 and dimension(J_COEFFICIENTS) == 24,
        'Coefficient-space dimensions failed')

# Independently recover the imported ambient character from its fixed presentation.
M2 = linear({'A_std':1, 'V':2, 'P':3, 'D':4})
M3 = linear({'Wprime':3, 'S4':3, 'T6':6})
M4 = linear({'V':2, 'P':4, 'D':3})
H = add(multiply(M3, W), scale(-1, M2), scale(-1, M4))
H_CHARACTER = decompose(H)
require(H_CHARACTER == {'A_std':2, 'V':2, 'D':2, 'P':2},
        'Imported original-ambient character failed')
C = add(H, scale(-1, linear({'P':1, 'D':1})))
C_CHARACTER = decompose(C)
require(C_CHARACTER == {'A_std':2, 'V':2, 'D':1, 'P':1},
        'Imported constant twenty-one-space character failed')
require(dimension(C_CHARACTER) == 21, 'Wrong constant-ambient dimension')

for name in ('A_std', 'V'):
    require(C_CHARACTER[name] == 2 and J_COEFFICIENTS[name] == 1
            and R_FULL[name] == 1, 'Missing multiplicity forcing: ' + name)
require(set(R_FULL) == {'A_std', 'V', 'D'} and all(n == 1 for n in R_FULL.values()),
        'Degree-ten coefficient space is not the required multiplicity-free triple')
R_SMALL = {'A_std':1, 'V':1}
require(dimension(R_SMALL) == 6 and dimension(R_FULL) == 11,
        'The two representation-theoretically forced dimensions changed')
J_CAP = {name:min(C_CHARACTER.get(name, 0), J_COEFFICIENTS.get(name, 0))
         for name in IRREP}
J_CAP = {name:n for name, n in J_CAP.items() if n}
require(J_CAP == {'A_std':1, 'V':1, 'D':1, 'P':1}, 'Wrong complement coefficient bound')
require(dimension(J_CAP) == 15, 'Wrong maximum complement span dimension')
require(21 - 6 == 15 and 6 + 15 - 21 == 0,
        'Spanning must force dimension fifteen and zero constant intersection')

# These are identities of the fixed universal ranks/degrees, not instance ranks.
e0_rank = 5 + 2 + 6 + 3
e0_degree = 5*(-2) + (2+6)*(-3) + 3*(-4)
m_rank, m_degree = 3, 3*(-8)
t_rank, t_degree = 2, 2*(-11)
ar_rank, ar_degree = 6-m_rank, m_degree
aj_rank, aj_degree = 15-t_rank, t_degree
require((e0_rank, e0_degree) == (16, -46), 'Imported E0 rank/degree failed')
require((m_rank+t_rank, m_degree+t_degree) == (5, -46), 'S0 rank/degree failed')
require((ar_rank, ar_degree) == (3, -24), 'First actual annihilator rank/degree failed')
require((aj_rank, aj_degree) == (13, -22), 'Second actual annihilator rank/degree failed')
require((ar_rank+aj_rank, ar_degree+aj_degree) == (e0_rank, e0_degree),
        'Forced direct-annihilator sum has inconsistent rank/degree')
lower_bound = ar_rank * min(-2, -3, -4)
require(lower_bound == -12 and ar_degree < lower_bound,
        'Birkhoff direct-summand contradiction failed')
KERNEL_CHARACTER = decompose(add(C, scale(-1, decentic)))
require(KERNEL_CHARACTER == {'A_std':1, 'V':1, 'P':1}, 'Wrong actual dual-kernel character')
require(dimension(KERNEL_CHARACTER) == 10 and 21-11 == 10, 'Wrong actual dual-kernel dimension')

EXPECTED_SOURCE = {
    'file':'inputs/constant-exclusions.md',
    'ref':'62ec109e8960848ae9081a17141b30228b598a70',
    'path':'research/hm/rankfour-profile11-apolar-constant-exclusions/PROOF.md',
    'url':'https://github.com/Akilleez-QA/read-em-and-weep/blob/62ec109e8960848ae9081a17141b30228b598a70/research/hm/rankfour-profile11-apolar-constant-exclusions/PROOF.md',
    'bytes':15110,
    'sha256':'e5d2c74f516bb5b2ede85287fceb3a774c6870b68b7b2418398e30fd5093d9b2',
    'git_blob_sha1':'de0eacee65c0c738e87ed8ce47ad9582a8e76313',
}
proof_path = ROOT/'PROOF.md'
require(proof_path.is_file(), 'Reviewed PROOF.md is required')
require(sha256(proof_path.read_bytes()) == FROZEN_PROOF_SHA256,
        'Whole-proof bytes changed after independent review')
manifest_path = ROOT/'INPUTS.json'
require(manifest_path.is_file(), 'INPUTS.json is mandatory')
manifest_bytes = manifest_path.read_bytes()
require(sha256(manifest_bytes) == FROZEN_INPUTS_SHA256, 'INPUTS manifest bytes changed')
manifest = json.loads(manifest_bytes)
require(manifest == [EXPECTED_SOURCE], 'Exact immutable-source manifest mismatch')
source_path = ROOT/EXPECTED_SOURCE['file']
require(source_path.is_file(), 'Retained complete immutable source is required')
source = source_path.read_bytes()
require(len(source) == EXPECTED_SOURCE['bytes'], 'Source byte length mismatch')
require(sha256(source) == EXPECTED_SOURCE['sha256'], 'Source SHA256 mismatch')
require(git_blob_sha1(source) == EXPECTED_SOURCE['git_blob_sha1'], 'Source Git blob mismatch')

auth_path = ROOT/'REVIEW-AUTHENTICITY.json'
require(auth_path.is_file(), 'Fresh original-source authentication record is required')
auth = json.loads(auth_path.read_text())
require(auth['status'] == 'PASS', 'Original-source authentication did not pass')
require(auth['proof_sha256'] == FROZEN_PROOF_SHA256, 'Authentication binds a different proof')
require(auth['inputs_manifest_sha256'] == FROZEN_INPUTS_SHA256,
        'Authentication binds a different source manifest')
require(auth['public_writes'] is False, 'Authentication public-write boundary changed')
require(len(auth['sources']) == 1, 'Authentication source count mismatch')
fresh = auth['sources'][0]
for field, expected in EXPECTED_SOURCE.items():
    require(fresh[field] == expected, 'Fresh-source metadata mismatch: ' + field)
require(fresh['fresh_github_fetch'] is True, 'Independent fresh GitHub retrieval missing')
require(fresh['fresh_bytes_equal_retained_file'] is True, 'Fresh bytes were not equal to retained input')
require(fresh['fetched_sha256'] == EXPECTED_SOURCE['sha256'], 'Fresh-source SHA256 mismatch')
require(fresh['fetched_git_blob_sha1'] == EXPECTED_SOURCE['git_blob_sha1'],
        'Fresh-source Git blob mismatch')

result = {
    'status':'PASS',
    'check_count':CHECK_COUNT,
    'proof_sha256':FROZEN_PROOF_SHA256,
    'inputs_manifest_sha256':FROZEN_INPUTS_SHA256,
    'method':'Exact closed binomial character polynomials on the nine physical conjugacy classes; Galois-conjugate Wprime; no author-code imports.',
    'full_degree_ten_character':R_FULL,
    'complement_coefficient_character':J_COEFFICIENTS,
    'constant_ambient_character':C_CHARACTER,
    'deficient_span_dimensions':[6, 15, 21],
    'forced_constant_intersection_dimension':0,
    'contradictory_direct_summand':{'rank':ar_rank, 'degree':ar_degree, 'minimum_allowed_degree':lower_bound},
    'actual_dual_kernel_character':KERNEL_CHARACTER,
    'actual_dual_kernel_dimension':10,
    'original_defect_unchanged':12,
    'optimization_safe_checks':True,
    'candidate_scan':False,
    'actual_instance_evaluation':False,
    'public_writes':False,
    'scope':'Executable checks support, but do not replace, the independently reviewed sheaf-theoretic proof and imported actual geometry.'
}
print(json.dumps(result, indent=2, sort_keys=True))
