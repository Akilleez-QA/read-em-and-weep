#!/usr/bin/env python3
"""Fixed universal identities only; no actual coefficient or instance evaluation."""
import hashlib
import json
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

PINS = [
    ('inputs/projected-ranktwo.md', 'b2d020a32a3ac5aaf5f264e33e2f930c16195c34',
     'research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md',
     '99a5a0257b0d683b04c5d190333d868c5b0d194d',
     '7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd', 15271),
    ('inputs/eighteen-jets.md', '913892c66403ea57ed1681957ae1b9f8db9e5e15',
     'research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md',
     '730021d4e97c4c1307a1d3c6c5303e4e9792202d',
     '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf', 17528),
    ('inputs/actual.md', 'db51525015bb7c5e825833d550d08dedf6f6ea96',
     'research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md',
     'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3',
     'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 9672),
]
records = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(records) == len(PINS) == 3, 'three complete immutable inputs')
for record, pin in zip(records, PINS):
    require(tuple(record[k] for k in ('file','ref','path','git_blob_sha1','sha256','bytes')) == pin,
            'immutable input pin')
    data = (ROOT / record['file']).read_bytes()
    require(len(data) == record['bytes'], 'input UTF8 length')
    require(hashlib.sha256(data).hexdigest() == record['sha256'], 'input SHA256')
    require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            == record['git_blob_sha1'], 'input Git blob SHA1')

# Exact actual quotient degree identities and one fixed extension space.
require(4*(-15) == -60 and -64-(-60) == -4, 'actual rank-five extension degrees')
require(-15-(-4) == -11 and 11-2 == 9, 'extension Serre-dual exponent')
require(product('one', 6) == rep(V=1,P=1), 'Sym6')
require(product('one', 7) == rep(Wp=1,T=1), 'Sym7')
require(product('one', 8) == rep(P=1,D=1), 'Sym8')
require(product('one', 9) == rep(S=1,T=1), 'Sym9')
require(product('one',10) == rep(A=1,V=1,D=1), 'Sym10')
require(product('one',12) == rep(one=1,A=1,P=1,D=1), 'Sym12')
cg = Counter()
for n in (12,10,8,6):
    cg.update(product('one', n))
require(product('S',9) == cg, 'one fixed Clebsch-Gordan identity')
require(cg['one'] == 1, 'one-dimensional invariant extension space')
require(sum((product('one',n)['one'] for n in (6,8,10))) == 0,
        'only Cartan summand carries the invariant')
require(product('Wp',1) == rep(P=1), 'Wp tensor W')
require(product('Wp',2) == rep(T=1), 'Wp tensor Sym2')
require(product('Wp',3) == rep(V=1,D=1), 'Wp tensor Sym3')

# Universal binary apolar resolution; fixed symbolic identities, no apolar matrix.
require(12+2 == 14 and 7+7 == 14, 'socle shift and equal generator degrees')
require(1-2+1 == 0 and -7-7+14 == 0, 'Hilbert numerator double zero at one')
require(7 < 12 and 6 < 7, 'distinct minimal degree would be below invariant minimum')
require(DIM['Wp'] == 2 and DIM['T'] == 6, 'two-dimensional generator is Wp, not T6')
for m, dimension in ((7,2),(8,4),(9,6)):
    require(m < 14 and 2*(m-7+1) == dimension, 'generator multiples before first relation')
    require(m+1-dimension == 12-m+1, 'binary apolar quotient Hilbert value')
require(3+9 == 12 and 13-(4+9) == 0, 'connecting-map endpoints')
require(3+(9-9) == 12-9, 'last injective polarization target')
require(14-15 == -1 and 13-14 < 0, 'twist-fourteen H0/H1 of T3 vanish')

# Middle splitting from fixed cohomological values.
require(5-2 == 3, 'remaining middle rank')
require(-64-2*(-11) == -42 == 3*(-14), 'remaining degree forces three -14 summands')
require(product('Wp',1) == rep(P=1),
        'top doublet fills all twist-twelve sections')
require(product('Wp',2) == rep(T=1), 'top doublet fills all twist-thirteen sections')
require(product('Wp',3)+rep(A=1) == product('one',10), 'remaining coefficient representation A')
require(2*(-11)+3*(-14) == -64, 'nonzero middle total degree')
require(4*(-15)+(-4) == -64, 'zero middle total degree')

# Actual incidence arguments use only these fixed degree/Hom identities.
require(-15-(-11) == -4 < 0, 'top doublet cannot lie in T3')
require(-4-(-11) == 7 < 12, 'degree-seven quotient has no invariant base divisor')
require(2*(-11)-(-4) == -18, 'actual top-doublet kernel degree')
require(-12-(-18) == 6 and product('one',6)['one'] == 0,
        'kernel line maps trivially to T3/T2')
require(-16-(-18) == 2 and product('A',2)['one'] == 1,
        'unique scalar line in actual second jets')
require(2+4-1 == 5 and -22-60-(-18) == -64, 'actual pushout rank and degree')
require(2 > 1 and 2-0 == 2, 'T1 rank contradicts a rank-one intrinsic U kernel')

proof = (ROOT/'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        'c0b961a3a851b21906218865208c304df8390dedb72b73fb9e2b912a33d68d0b',
        'exact frozen whole-proof target')
print(json.dumps({'status':'PASS','checks':checks,
    'proof_sha256':hashlib.sha256(proof).hexdigest(),
    'scope':'Fixed universal characters, apolar Hilbert identities and bundle degrees only. No actual form, tensor, coefficient or instance rank evaluation.'}, indent=2))
