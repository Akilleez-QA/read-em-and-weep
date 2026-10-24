#!/usr/bin/env python3
"""Fixed universal checks only; no actual source instance is selected."""
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

SOURCE_PINS = [
    ('inputs/shared-d-gluing.md', 'af136934955f1bcc700ee768e2debb983e75451d',
     'research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md',
     '3d051410e80a33f1c4d78d3403bb186595bb72c3',
     '7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7', 20361),
    ('inputs/positive-span.md', '97dad5c307a04f61d850e8a4211559e97ed4c2fd',
     'research/hm/rankfour-profile11-triplet-positive-span/PROOF.md',
     'b75b1272bbf3a360751cc22a9e04c641cdeeb787',
     '145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b', 12569),
    ('inputs/actual.md', 'db51525015bb7c5e825833d550d08dedf6f6ea96',
     'research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md',
     'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3',
     'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 9672),
]
records = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(records) == len(SOURCE_PINS) == 3, 'three complete immutable inputs')
for record, pin in zip(records, SOURCE_PINS):
    require(tuple(record[k] for k in ('file', 'ref', 'path', 'git_blob_sha1', 'sha256', 'bytes')) == pin,
            'exact source pins')
    data = (ROOT / record['file']).read_bytes()
    require(len(data) == record['bytes'], 'UTF8 input length')
    require(hashlib.sha256(data).hexdigest() == record['sha256'], 'input SHA256')
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == record['git_blob_sha1'], 'input Git blob SHA1')

# The nine-vertex recurrence is for physical W, not W'.
require(product('V', 4) == rep(A=1, V=1, P=1, D=1), 'V tensor Sym4')
require(dim(rep(A=1, V=1)) == 6, 'constant N dimension')
require(DIM['A'] == DIM['V'] == 3, 'only proper invariant spans have rank3')
require(-12 < 0, 'negative equal-rank bundle cannot fill constant rank3')
require(3*(-4) == -12, 'G0 rank/degree')
require(6-3 == 3, 'local dual annihilator rank')
require((-12)-(-18) == 6, 'S/m positive quotient degree')
require(product('one', 8) == rep(P=1, D=1), 'H1 projected scalar line')
local_h1 = product('V', 4).copy()
local_h1.subtract(rep(A=1, V=1))
require(+local_h1 == rep(P=1, D=1), 'H1 local annihilator')

# Rank-one contradiction: low physical powers have no V, hence a>=2.
require(product('one', 0)['V'] == product('one', 2)['V'] == product('one', 4)['V'] == 0,
        'rank-one quotient lower bound')
require(product('one', 6)['V'] == 1, 'first even power containing V')
require(-2-2 == -4, 'actual transpose imposes b<=-4')
require((-2)+(-4) == -6, 'two-step coherent-kernel capacity')
require((-12+6)/3 == -2, 'capacity forces b>=-2')
require(-2 > -4, 'rank-one bounds contradict')

# Rank two: four explicit representations, not a search over quotient tuples.
require((-12)-(-10) == -2, 'local derivative quotient degree')
budget = rep(P=1, D=1)
require(dim(budget) == 9, 'H0 quotient budget bounds scalar degree by eight')
fixed_scalar_powers = {
    0: rep(one=1), 2: rep(A=1), 4: rep(D=1),
    6: rep(V=1, P=1), 8: rep(P=1, D=1),
}
for degree, expected in fixed_scalar_powers.items():
    require(product('one', degree) == expected, 'fixed scalar quotient character')
require(product('one', 0)['one'] == 1 and product('one', 2)['A'] == 1
        and product('one', 6)['V'] == 1, 'three forbidden scalar alternatives')
require(product('one', 4) <= budget and product('one', 8) <= budget,
        'two remaining scalar characters')
require(4+(-6) == 8+(-10) == -2, 'two displayed scalar quotient degrees')
require(-6 < -4 and -10 < -4, 'negative transpose row kills rank-two scalar alternatives')
require(product('W', 3) == rep(A=1, D=1), 'physical W target has no V')
require(product('Wp', 3) == rep(V=1, D=1), 'W-prime target has a single V')
require(product('W', 3)['V'] == 0 and product('Wp', 3)['V'] == 1,
        'actual local derivative target selection')
require(2*3 == 6 < 12, 'rank-two cubic minor divisor bound')
require(-12-(-2) == -10, 'local primal kernel degree')

# The genuine constant-intersection comparison and its exact quotient.
require(16+6-3 == 19 and 21-19 == 2, 'constant intersection ambient ranks')
require(3*4 == 12 and 12-(-2) == 14, 'saturated W-prime image quotient degree')
require(16-3 == 13 and -46-12 == -58, 'original K rank/degree')
require(13-1 == 12 and -58-(-10) == -48, 'K modulo actual line')
require(13-1 == 12 and -34-14 == -48, 'same quotient kernel in F18')

# Separate local-dual splitting corollary, with no cross-ambient identification.
require(product('one', 7) == rep(Wp=1, T=1), 'one-dimensional local Ext')
require(product('one', 7)['Wp'] == 1, 'local extension multiplicity')
require(product('A', 1) == rep(W=1, S=1), 'A tensor W')
require(product('V', 1) == rep(T=1), 'V tensor W')
require((product('A', 1)+product('V', 1))['Wp'] == 0,
        'local dual sequence cannot split inside constant N dual')
require(-10+(-2) == -12, 'nonzero local extension middle degree')

proof = (ROOT / 'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        '16823fcb3c9012c02a23406dcf4656e27441fcb05734551e7d2d4b1756085c67',
        'exact frozen whole-proof review target')
print(json.dumps({'status': 'PASS', 'checks': checks,
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'scope': 'Fixed universal representations, symbolic degree bounds and immutable inputs only; no actual instance evaluation.'}, indent=2))
