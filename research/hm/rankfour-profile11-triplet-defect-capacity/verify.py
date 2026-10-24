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

# Small polynomial arithmetic for the universal two-column identity.
# Coefficients are in ascending powers of an indeterminate k, not actual data.
def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, x in enumerate(p): out[i] += x
    for i, x in enumerate(q): out[i] += x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(c, p):
    return [c*x for x in p]

def mul(p, q):
    out = [0] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): out[i+j] += x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

k = [0,1]
ten_minus_k = [10,-1]
penalty = add(mul(ten_minus_k,[9,-1]), mul(k,[-1,1]))
require(penalty == [90,-20,2], 'two column height penalties')
sum_penalty = add(scale(2,mul(k,[-1,1])), scale(9,[10,-2]))
require(sum_penalty == penalty, 'coherent quotient sum equals column penalty')
require(add(scale(2,k),[10,-2]) == [10], 'rank-two plus rank-one quotient rank sum')
require(2*1<=10 and 2*5==10, 'k ranges from one to five')
require(10-2*5==0 and 10-2*1>0, 'coefficient of a is nonnegative throughout')
low_bound = add(add(scale(2,[10,-2]),scale(-12,k)),scale(-1,penalty))
square_bound = add([-68],scale(-2,mul([-1,1],[-1,1])))
require(low_bound == [-70,4,-2] == square_bound,
        'high-defect low-top bound is minus68 minus twice a square')
require(-68 < -64, 'capacity contradiction')

# Actual quotient degrees, top line and slope endpoint.
require(2+10==12 and 12-24==-12, 'coherent image degree threshold')
require(10-3==7<12, 'positive top-to-O10 polynomial degrees stay below orbit minimum')
require(12-10==2, 'high-defect lower coherent summand degree')
require(-64-9*(-4)==-28, 'smallest ordinary F degree bound')
require(2-(-28)==30, 'upper defect bound from actual quotient')
require(2-30==-28, 'forced endpoint quotient degree')
require(-64-(-28)==-36==9*(-4), 'forced endpoint nine top summands')
require(9+1==10, 'forced endpoint rank')

# Exactly the fixed universal characters used at delta=30.
require(product('one',8)==rep(P=1,D=1), 'Sym8')
require(product('one',14)==rep(A=1,V=1,P=1,D=1), 'Sym14')
require(product('P',4)==rep(A=1,V=1,P=1,D=2), 'P tensor Sym4')
require(product('one',22)==rep(A=2,V=1,P=1,D=2), 'Sym22')
require(18-3-1==14 and -3-1==-4, 'complete thirdjet kernel degrees')
require(19-15==DIM['P']==4, 'actual versus complete coefficient quotient rank')
require(15-4==11, 'actual thirdjet kernel rank')
require(15*(-4)-4*0==-60, 'partial-system Jminus degree')
require(-60-4==-64, 'actual F degree after O4 quotient')
chi = product('one',14).copy()
chi.subtract(product('P',4))
chi.subtract(product('one',8))
require(+(-chi)==rep(P=1,D=2) and +chi==Counter(), 'fixed Euler-characteristic identity')
require(-28+4==-24 and 24-2==22, 'endpoint H1 exponent')
r9 = product('one',22).copy()
r9.update(chi)
require(+r9==rep(A=2,V=1), 'forced endpoint top representation')
require(2*DIM['A']+DIM['V']==9, 'endpoint top representation rank')
require(r9['A']==2>product('one',14)['A']==1, 'actual top injection multiplicity contradiction')

# Fixed group-orbit arithmetic, no polynomial range or bundle candidate scan.
require(tuple(60//n for n in (1,2,3,5))==(60,30,20,12), 'projective orbit sizes')
require(20+12>29 and 3*12>29 and 2*12==24, 'only 0 12 20 24 remain below30')
require(24//4==6 and 6*2==12, 'unique order-five fixed-point orbit size')
require(2*12==24, 'degree24 determinant is twice the length12 orbit')

# Conditional cyclic endpoint description.
require(2-24==-22, 'conditional lower coherent line degree')
require(10+(-22)==12-24, 'conditional rank-two coherent degree')
require(2-(-22)==24, 'conditional lower-line divisor degree')
require(0+2==2 and 12*2==24, 'local elementary divisor lengths sum globally')
require(10-10==0, 'top-line map is a nonzero constant isomorphism')

proof = (ROOT/'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest() ==
        '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f',
        'exact frozen whole-proof target')
print(json.dumps({'status':'PASS','checks':checks,
    'proof_sha256':hashlib.sha256(proof).hexdigest(),
    'scope':'Fixed symbolic two-column capacity, physical characters, bundle degrees and group-orbit arithmetic only. No actual coefficient, point, tensor, matrix or instance-rank evaluation.'}, indent=2))

