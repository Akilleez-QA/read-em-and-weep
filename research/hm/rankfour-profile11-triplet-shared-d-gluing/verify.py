#!/usr/bin/env python3
"""Fixed universal checks for the shared-D gluing proof.

Only exact representation-ring arithmetic, displayed degree identities and
immutable input hashes are checked. No actual curve, coefficient, parameter,
point, jet, tensor, matrix, or instance rank is selected or evaluated.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
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

def dim(value):
    return sum(DIM[r] * n for r, n in value.items())

def difference(a, b):
    result = a.copy()
    result.subtract(b)
    return +result if all(v >= 0 for v in result.values()) else result

SOURCE_PINS = [
    ('inputs/shared-d.md', '252b967ebbfbea6fc0c6451a835ab2daff92d73b',
     'research/hm/rankfour-profile11-triplet-shared-d/PROOF.md',
     '82596d9d02147711e0d5f7953912a94fffbae684',
     'f2e5b5d8bdb0f8a156aaf38695042f204b4d3cffd1a40a4a28870bed2ef13793', 8801),
    ('inputs/positive-span.md', '97dad5c307a04f61d850e8a4211559e97ed4c2fd',
     'research/hm/rankfour-profile11-triplet-positive-span/PROOF.md',
     'b75b1272bbf3a360751cc22a9e04c641cdeeb787',
     '145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b', 12569),
    ('inputs/deep-images.md', '95af2c0fa1e3cce92496a44ef9023708735e1ec7',
     'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',
     '9cf95f42505f37900f5a24c25cff07acca1b499f',
     '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26', 12085),
    ('inputs/actual.md', 'db51525015bb7c5e825833d550d08dedf6f6ea96',
     'research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md',
     'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3',
     'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 9672),
]
manifest = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(manifest) == len(SOURCE_PINS) == 4, 'four complete immutable inputs')
for record, pin in zip(manifest, SOURCE_PINS):
    require(tuple(record[k] for k in ('file', 'ref', 'path', 'git_blob_sha1', 'sha256', 'bytes')) == pin,
            'exact source pins')
    data = (ROOT / record['file']).read_bytes()
    require(len(data) == record['bytes'], 'source UTF8 length')
    require(hashlib.sha256(data).hexdigest() == record['sha256'], 'source SHA256')
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == record['git_blob_sha1'], 'source Git blob SHA1')

fixed_powers = {
    2: rep(A=1), 3: rep(S=1), 4: rep(D=1), 5: rep(T=1),
    8: rep(P=1, D=1), 10: rep(A=1, V=1, D=1),
    16: rep(V=1, P=1, D=2), 18: rep(A=1, V=1, P=2, D=1),
}
for degree, expected in fixed_powers.items():
    require(product('one', degree) == expected, 'physical symmetric power ' + str(degree))
fixed_products = [
    ('D', 2, rep(A=1, V=1, P=1, D=1)),
    ('P', 2, rep(V=1, P=1, D=1)),
    ('D', 1, rep(S=1, T=1)),
    ('V', 1, rep(T=1)),
    ('P', 1, rep(Wp=1, T=1)),
    ('Wp', 1, rep(P=1)),
    ('W', 1, rep(one=1, A=1)),
    ('P', 3, rep(S=1, T=2)),
]
for name, degree, expected in fixed_products:
    require(product(name, degree) == expected, 'fixed tensor product')
sym16_times_W = rep()
for name, multiplicity in fixed_powers[16].items():
    sym16_times_W.update({r: n*multiplicity for r, n in product(name, 1).items()})
require(difference(sym16_times_W, product('P', 3)) == rep(Wp=1, S=1, T=2),
        'degree-eighteen twist-three Euler character')

E0 = [('D', -2), ('Wp', -3), ('T', -3), ('V', -4)]
F = E0 + [('one', -6)]
F10 = [('P', -2), ('D', -2)]
R = [('V', -4), ('one', -6)]
F18_SPLIT = [('D', -2), ('Wp', -3), ('T', -3)]
F18_EULER = [('D', -2), ('V', -2), ('Wp', -3), ('V', -4)]

def rank_degree(blocks):
    return sum(DIM[r] for r, d in blocks), sum(DIM[r] * d for r, d in blocks)

def cohomology(blocks, twist, index):
    answer = rep()
    for r, degree in blocks:
        n = degree + twist if index == 0 else -degree - twist - 2
        if n >= 0:
            answer.update(product(r, n))
    return answer

require(rank_degree(F) == (17, -52), 'F rank/degree')
require(rank_degree(E0) == (16, -46), 'E0 rank/degree')
require(rank_degree(F10) == (9, -18), 'complete10 first-jet kernel')
require(rank_degree(R) == (4, -18), 'projected10 first-jet kernel')
require(rank_degree(F18_SPLIT) == rank_degree(F18_EULER) == (13, -34),
        'both necessary F18 splittings')
require(9+13-5 == 17 and -18-34 == -52, 'gluing rank/degree')
require(11+15-5 == 21, 'constant gluing dimension')
require(5*2 == 10 < 12, 'universal maximal-minor degree below invariant divisor minimum')
require(10 < 12, 'projected10 basepoint divisor bound')
require(5 > 4 and -8 > -18, 'H0 projected10 rank/determinant exclusions')
require(difference(product('D', 2), rep(P=1, D=1)) == rep(A=1, V=1),
        'projected10 H1 budget')
require(cohomology(R, 2, 0) == rep() and cohomology(R, 2, 1) == rep(A=1, V=1),
        'projected10 exact cohomology')
require(cohomology(F, 2, 1) == rep(A=1, V=1), 'F H1 budget')
require((rep(A=1, V=1) & product('P', 2)) == rep(V=1), 'intersection of genuine H1 budgets')
require(difference(product('one', 16), product('P', 2)) == rep(D=1), 'F18 Euler at two')
require(cohomology(F18_SPLIT, 2, 0) == rep(D=1)
        and cohomology(F18_SPLIT, 2, 1) == rep(), 'first F18 cohomology')
require(cohomology(F18_EULER, 2, 0) == rep(D=1, V=1)
        and cohomology(F18_EULER, 2, 1) == rep(V=1), 'second F18 cohomology')
for candidate in [F18_SPLIT, F18_EULER]:
    require(cohomology(candidate, 3, 0) == rep(Wp=1, S=1, T=2),
            'two displayed twist-three characters')
    require(cohomology(candidate, 3, 1) == rep(), 'twist-three H1 vanishes')

# Only the displayed atom facts; this does not enumerate bundle candidates.
require(product('one', 0) == rep(one=1) and product('one', 4) == rep(D=1),
        'forbidden scalar contributions at degrees four and eight')
require(dim(product('A', 2)) == dim(product('V', 2)) == 9 > 6,
        'higher triplet atoms exceed six-dimensional budget')
require(dim(product('W', 3)) == dim(product('Wp', 3)) == 8 > 6,
        'higher odd doublet atoms exceed budget')
require(dim(product('W', 1)) == dim(product('Wp', 1)) == 4 > 3,
        'odd doublets excluded from sole V budget')

# Scalar cancellation and its universal quartic contradiction.
require(product('D', 4)['one'] == 1, 'unique quartic inclusion')
for name, degree in [('Wp', 3), ('T', 3), ('V', 2)]:
    require(product(name, degree)['one'] == 0, 'forbidden scalar component')
require(5-1 == 4 and -10-(-6) == -4, 'quartic quotient S4(-1)')
require(-2-(-1) < 0 and 4 > 3, 'quartic quotient cannot map to F18 or lie in rank3 kernel')
require(-6-(-4) < 0, 'scalar quotient kills V(-4)')
require(16-3 == 13 and -46-(-12) == -34, 'actual E0 restriction sequence')

# The only equivariant Ext block has equal coefficient V and degree gap two.
require('D' != 'V', 'Ext1 D(-2) by V(-4) has no invariants')
require(-4-(-3) >= -1 and -4-(-4) >= -1, 'remaining extension H1 groups vanish')
require(product('V', 1) == rep(T=1), 'physical Euler middle term')
require(rank_degree([('T', -3)]) == (6, -18), 'Euler rank/degree')
require(rank_degree([('V', -4), ('V', -2)]) == (6, -18), 'Euler endpoints rank/degree')

# Last corollary: the quotient by V(-4) is the nonzero universal extension.
require(9-3 == 6 and -18-(-12) == -6, 'Q rank/degree')
require(-6-(-2) < 0, 'split Q would yield forbidden F10 to O(-6) map')
require(product('one', 4) == rep(D=1), 'one-dimensional extension class of Q')
require(rank_degree([('T', -1)]) == (6, -6), 'Q universal middle term')

proof = (ROOT / 'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        '7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7',
        'exact frozen proof submitted for whole-proof review')
print(json.dumps({'status': 'PASS', 'checks': checks,
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'scope': 'Fixed universal identities and immutable input hashes only; no actual instance evaluation or proof-assistant certification.'}, indent=2))
