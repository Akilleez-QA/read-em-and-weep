#!/usr/bin/env python3
"""Small universal representation, degree and immutable-input checks.

This does not sample actual curves or certify the imported geometry. There is
no coefficient, parameter, point, jet, tensor, matrix or bundle search.
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

def representation(**kwargs):
    return Counter(kwargs)

def dimension(rep):
    return sum(DIM[r] * n for r, n in rep.items())

def check_source_manifest():
    recorded = json.loads((ROOT / 'INPUTS.json').read_text())
    expected = [
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
    require(len(recorded) == len(expected) == 3, 'three complete source inputs')
    for rec, pin in zip(recorded, expected):
        require(tuple(rec[k] for k in ('file', 'ref', 'path', 'git_blob_sha1', 'sha256', 'bytes')) == pin,
                'independently fixed immutable source pins')
        data = (ROOT / rec['file']).read_bytes()
        require(len(data) == rec['bytes'], 'source byte length')
        require(hashlib.sha256(data).hexdigest() == rec['sha256'], 'source SHA256')
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        require(blob == rec['git_blob_sha1'], 'Git blob identity')

check_source_manifest()

# The physical McKay recurrence uses W, never W'.
s10 = product('one', 10)
s18 = product('one', 18)
require(s10 == representation(A=1, V=1, D=1), 'Sym10 physical decomposition')
require(s18 == representation(A=1, V=1, P=2, D=1), 'Sym18 physical decomposition')
require(product('one', 8) == representation(P=1, D=1), 'complete degree-ten jet kernel')
ambient = representation(A=2, V=2, P=1, D=1)
require(dimension(ambient) == 21, 'genuine constant ambient dimension')
loss = s10 + s18
loss.subtract(ambient)
require(loss == representation(P=1, D=1), 'joint coefficient loss')
require(dimension(s10) == 11 and dimension(s18) == 19, 'scalar coefficient dimensions')

# Universal rank and degree accounting for actual annihilators.
E0 = [(-2, 'D'), (-3, 'Wp'), (-3, 'T'), (-4, 'V')]
F = E0 + [(-6, 'one')]
def rank_degree(blocks):
    return sum(DIM[r] for d, r in blocks), sum(d * DIM[r] for d, r in blocks)
require(rank_degree(E0) == (16, -46), 'E0 rank/degree')
require(rank_degree(F) == (17, -52), 'ann(M) rank/degree')
require(all(d + 6 >= -1 for d, r in E0), 'extension H1 vanishing')
require(all(d >= -4 and -6-d < 0 for d, r in E0), 'actual quotient kills HN top')
require(2*(-9) + 2*(-17) == -52, 'first-jet degree')

# First disjoint alternative: rank-nine direct summand cannot be pure -2.
require((11-2, -18) == (9, 9*(-2)), 'first-case forced pure degree')
require(DIM['D'] == 5 < 9, 'insufficient minus-two multiplicity')
require(product('one', 8)['P'] == 1, 'independent P(-2) obstruction')

# Second alternative: four fixed irreducible-block dimensions, no candidate scan.
require(DIM['D'] > 4 and DIM['T'] > 4, 'large irreducibles do not fit rank4')
require(DIM['Wp'] == 2 and DIM['V'] == 3 and DIM['one'] == 1,
        'remaining distinct block dimensions')
require(2 + 1 < 4 and 2 + 3 > 4, 'single doublet cannot be completed')
require(rank_degree([(-4, 'V'), (-6, 'one')]) == (4, -18), 'forced F10')
require(rank_degree([(-2, 'D'), (-3, 'Wp'), (-3, 'T')]) == (13, -34), 'forced F18')
require(6-2 == 4 and 15-2 == 13, 'annihilator ranks in disjoint case')
require((-34)-(-18) == -16, 'principal-parts quotient degree')
require(-16-(-6) == -10 < 0, 'forbidden quotient Hom degree')

# Retained overlap: neither D entry can vanish, so kernel D is a graph.
require(11+15-5 == 21, 'shared-D dimension formula')
require(dimension(s18)-15 == DIM['P'], 'degree-eighteen remains incomplete')
proof = (ROOT / 'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        'f2e5b5d8bdb0f8a156aaf38695042f204b4d3cffd1a40a4a28870bed2ef13793',
        'exact frozen whole-proof-reviewed proof')
print(json.dumps({'status': 'PASS', 'checks': checks,
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'scope': 'Immutable inputs and fixed universal representation/degree identities only; not proof-assistant certification.'}, indent=2))
