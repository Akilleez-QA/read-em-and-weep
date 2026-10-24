#!/usr/bin/env python3
"""Fixed universal bounds and character checks, with no actual instances."""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from collections import Counter
from characters import product, DIM

ROOT = Path(__file__).resolve().parent
checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)

def rep(**values):
    return Counter(values)

SOURCE_PINS = [
    ('inputs/eighteen-jets.md', '913892c66403ea57ed1681957ae1b9f8db9e5e15',
     'research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md',
     '730021d4e97c4c1307a1d3c6c5303e4e9792202d',
     '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf', 17528),
    ('inputs/deep-images.md', '95af2c0fa1e3cce92496a44ef9023708735e1ec7',
     'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',
     '9cf95f42505f37900f5a24c25cff07acca1b499f',
     '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26', 12085),
    ('inputs/actual.md', 'db51525015bb7c5e825833d550d08dedf6f6ea96',
     'research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md',
     'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3',
     'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 9672),
]
records = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(records) == len(SOURCE_PINS) == 3, 'three complete immutable sources')
for record, pin in zip(records, SOURCE_PINS):
    require(tuple(record[k] for k in ('file', 'ref', 'path', 'git_blob_sha1', 'sha256', 'bytes')) == pin,
            'exact source pins')
    data = (ROOT / record['file']).read_bytes()
    require(len(data) == record['bytes'], 'source UTF8 length')
    require(hashlib.sha256(data).hexdigest() == record['sha256'], 'source SHA256')
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == record['git_blob_sha1'], 'source Git blob SHA1')

# Two exact quotient rows; representation splitting is not horizontal splitting.
require(15-10 == 5 and -64 < 0, 'dual rank and degree')
require(12-10 == 2 and -48-(-64) == 16, 'J/F rank and degree')
require(4+12 == 16, 'two scalar quotient degrees')
require(4-12 == -8 and -(-8)-2 == 6, 'equivariant extension degree')
require(product('one', 6) == rep(V=1, P=1), 'physical symmetric sixth power')
require(product('one', 6)['one'] == 0, 'equivariant J/F extension splits')
require(4-2 == 2 and 12-2 == 10, 'saturation candidate target degrees')

# Rank-one coherent-kernel capacity, evaluated only as universal scalar sums.
require(2*sum(range(1, 10)) == 9*10 == 90, 'nine-step line capacity sum')
require(2*sum(range(1, 5)) == 4*5 == 20, 'four-step dual line capacity sum')
require(Fraction(90-64, 10) == Fraction(13, 5), 'primal a lower bound')
require(Fraction(-64+20, 5) == Fraction(-44, 5), 'dual b lower bound')
require(2 < Fraction(13, 5) <= 4, 'even primal a starts at four')
require(-10 < Fraction(-44, 5) <= -8, 'even dual b starts at minus eight')
require(-2-(-8) == 6, 'transpose upper bound a<=6')
require(-12 < Fraction(-44, 5), 'dual capacity independently excludes the O10 escape')
require(product('one', 4) == rep(D=1), 'physical symmetric fourth power')
for a, polynomial_degree in [(4, 6), (6, 4)]:
    require(2-a < 0 and 10-a == polynomial_degree, 'two remaining scalar Hom degrees')
    require(product('one', polynomial_degree)['one'] == 0, 'remaining scalar Hom vanishes')

# Actual local dual endpoint and its equivariant quotient.
require(5-2 == 3, 'dual actual kernel rank')
require(3*(-16) == -48, 'actual second-jet kernel degree')
require(4*(-15) == -60, 'actual third-jet degree')
require(-60-(-48) == -12, 'third over second jet quotient')
require(-64-(-60) == -4, 'dual scalar quotient')
require(-64-(-48) == -16 == -12-4, 'local dual quotient degree')
require(-12-(-4) == -8 and product('one', 6)['one'] == 0,
        'local dual quotient extension splits')
require(-(-12)-2 == 10 and -(-4)-2 == 2, 'dual derivative saturation target')

# New defect is not original t: only its degree identities and upper bound.
require(2+10 == 12, 'saturated rank-two target determinant degree')
require(10-2 == 8, 'new actual kernel rank')
require(-64-12 == -76, 'kernel degree constant term before new defect')
require(18-3-1 == 14 and -(3+1) == -4, 'universal complete third-jet kernel source')
require(product('one', 14) == rep(A=1, V=1, P=1, D=1), 'universal kernel coefficient type')
require(-4-2 < -4, 'strict-top negative-horizontal contradiction')
require(8*(-5) == -40, 'ordinary top-degree kernel bound')
require(-40-(-76) == 36, 'new defect upper bound')
require(12 <= 36, 'nonzero invariant divisor lower bound is compatible with upper bound')

proof = (ROOT / 'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        '7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd',
        'exact frozen whole-proof review target')
print(json.dumps({'status': 'PASS', 'checks': checks,
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'scope': 'Fixed universal representation and symbolic capacity/degree identities; no actual instance evaluations or defect-fullness assumption.'}, indent=2))
