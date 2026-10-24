#!/usr/bin/env python3
"""Fixed universal arithmetic for the constant-restriction jet argument.

No actual curve, coefficient, parameter, point, jet, tensor, matrix or instance
rank is selected or evaluated. The geometric derivative squares require the
separate complete proof and independent review.
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

SOURCE_PINS = [
    ('inputs/sixspace-derivative.md', '2a8105d5a3a263b7518eb98bdf81689c3d4b3dfa',
     'research/hm/rankfour-profile11-triplet-sixspace-derivative/PROOF.md',
     '0c4cfc3b36b29ee8ae5ed64bf6526c65471a62d7',
     '16823fcb3c9012c02a23406dcf4656e27441fcb05734551e7d2d4b1756085c67', 16248),
    ('inputs/shared-d-gluing.md', 'af136934955f1bcc700ee768e2debb983e75451d',
     'research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md',
     '3d051410e80a33f1c4d78d3403bb186595bb72c3',
     '7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7', 20361),
    ('inputs/deep-images.md', '95af2c0fa1e3cce92496a44ef9023708735e1ec7',
     'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',
     '9cf95f42505f37900f5a24c25cff07acca1b499f',
     '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26', 12085),
]
records = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(records) == len(SOURCE_PINS) == 3, 'three complete immutable sources')
for record, pin in zip(records, SOURCE_PINS):
    require(tuple(record[k] for k in ('file', 'ref', 'path', 'git_blob_sha1', 'sha256', 'bytes')) == pin,
            'fixed input pins')
    data = (ROOT / record['file']).read_bytes()
    require(len(data) == record['bytes'], 'source UTF8 length')
    require(hashlib.sha256(data).hexdigest() == record['sha256'], 'source SHA256')
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == record['git_blob_sha1'], 'source Git blob SHA1')

# First actual derivative square and its forced saturated Euler line.
require(17-2 == 15, 'first target P1(O18) twisted by minus two')
require(product('W', 1) == rep(one=1, A=1), 'unique linear equivariant Euler row')
require(product('W', 1)['one'] == 1, 'Euler row invariant multiplicity')
require(2*15-14 == 16, 'Euler line quotient degree')
require(3*4-(-2) == 14, 'A4 modulo W-prime minus one')
require(13-1 == 12 and -34-14 == -48, 'first actual kernel J')
require(13-1 == 12 and -58-(-10) == -48, 'same J from K/H')
require(-34 != 0, 'F18 cannot be constant horizontal')

# Second actual derivative square, induced by constant p on K.
require(4-2 == 2 and 14-2 == 12, 'twisted exact quotient A2 to O12')
require(-1-2 == -3, 'second-square kernel W-prime minus three')
require(12-1 == 11 and -48-12 == -60, 'second actual kernel J minus')
require(3*2-12 == -6, 'A2 kernel degree')
require(2*(-3) == -6, 'W-prime kernel degree')

# Universal principal parts of the partial degree-eighteen curve.
require(product('one', 1) == rep(W=1), 'physical first-jet coefficient')
require(product('one', 2) == rep(A=1), 'physical second-jet coefficient')
require(product('one', 3) == rep(S=1), 'physical third-jet coefficient')
require(2*(1-18) == -34, 'first-jet degree')
require(3*(2-18) == -48, 'second-jet degree')
require(4*(3-18) == -60, 'third-jet degree')
require(15-12 == 3 and 15-11 == 4, 'actual annihilator ranks')
require((-18)+(-16)+(-14) == -48, 'second-jet filtration degree')
require((-18)+(-16)+(-14)+(-12) == -60, 'third-jet filtration degree')
require((-48)-(-34) == -14, 'second forward step quotient degree')
require((-60)-(-48) == -12, 'third forward step quotient degree')

# The nonzero actual H row and the extra O4 quotient.
require(-3-(-10) == 7 < 12, 'H row common-zero degree below invariant divisor minimum')
require(product('one', 7) == rep(Wp=1, T=1), 'degree-seven physical coefficient identity')
require(product('Wp', 7)['one'] == 1, 'H row equivariant multiplicity')
require(2*(-3)-(-10) == 4, 'W-prime minus three modulo H row')
require(13-3 == 10 and -58-6 == -64, 'K minus rank/degree')
require(10+2 == 12 and -64-6 == -70, 'preimage of W-prime minus three')
require(12-1 == 11 and -70-(-10) == -60, 'preimage modulo H')
require(11-10 == 1 and -60-(-64) == 4, 'final O4 quotient rank/degree')

# The constant-span corollary uses positivity, not completeness.
require(-15 < 0, 'third-jet annihilator has no constant sections')
require(0-4 < 0, 'positive O4 quotient maps trivially to a constant bundle')
require(15-(18+1-4) == 0, 'ambient fifteen-space dimension only')

proof = (ROOT / 'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf',
        'exact frozen whole-proof review target')
print(json.dumps({'status': 'PASS', 'checks': checks,
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'scope': 'Immutable inputs and fixed universal character/degree identities only; no actual instance evaluation or algebraicity test.'}, indent=2))
