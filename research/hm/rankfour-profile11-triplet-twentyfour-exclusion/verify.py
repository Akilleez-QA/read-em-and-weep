#!/usr/bin/env python3
"""Fixed near-top characters, coherent capacity and quotient-degree checks only."""
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
    ('inputs/defect-capacity.md', 'ca235151d5d93bbead2beffa7640fbd0741aec43',
     'research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md',
     '175af94697c44f3140bb2c1d04978931c255b3fe',
     '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f', 16069),
    ('inputs/five-kernels.md', '7d71f0e2a3963cff64a069198f4415c5cfd0fe9b',
     'research/hm/rankfour-profile11-triplet-kernels/PROOF.md',
     '163ba2126b6130befcc2351db7f6910d85fac2ec',
     '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a', 8501),
    ('inputs/eighteen-jets.md', '913892c66403ea57ed1681957ae1b9f8db9e5e15',
     'research/hm/rankfour-profile11-triplet-eighteen-jets/PROOF.md',
     '730021d4e97c4c1307a1d3c6c5303e4e9792202d',
     '33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf', 17528),
]
records = json.loads((ROOT/'INPUTS.json').read_text())
require(len(records)==len(PINS)==3, 'three complete immutable source files')
for record, pin in zip(records,PINS):
    require(tuple(record[k] for k in ('file','ref','path','git_blob_sha1','sha256','bytes'))==pin,
            'exact source pin')
    data = (ROOT/record['file']).read_bytes()
    require(len(data)==record['bytes'], 'source UTF8 length')
    require(hashlib.sha256(data).hexdigest()==record['sha256'], 'source SHA256')
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==record['git_blob_sha1'],
            'source Git blob SHA1')

# Near-top derivative factorization and physical irreducible supports.
require(-3-2==-5 < -4, 'near-top quotient derivative target is too negative')
require(-8+4<0, 'deep cubic-case tail contributes no twist-four sections')
require(product('S',1)==rep(A=1,D=1), 'S4 tensor W')
require(product('S',1)['V']==0 and product('S',1)['P']==0,
        'V and P cannot map into cubic S4 block')
cubic_h0=product('S',1)+rep(V=1,P=1)
require(cubic_h0==rep(A=1,D=1,V=1,P=1), 'fixed cubic-case twist-four character')
require(cubic_h0['one']==0, 'no trivial cubic-case section')
top_bound=rep(A=1,D=1)
h1_bound=top_bound+rep(P=1,D=2)
require(h1_bound['V']==0 and h1_bound['one']==0, 'H1 lacks both obstruction constituents')
require(h1_bound==rep(A=1,P=1,D=3), 'maximum H1 constituent support')

# The two actual scalar quotient targets in H1.
require(-22+4==-18 and 18-2==16, 'defect24 scalar H1 target exponent')
require(product('one',16)==rep(V=1,P=1,D=2), 'Sym16')
require(product('one',16)['V']==1>h1_bound['V'], 'defect24 missing-V obstruction')
require(-18+4==-14 and 14-2==12, 'forbidden defect20 scalar H1 target exponent')
require(product('one',12)==rep(one=1,A=1,P=1,D=1), 'Sym12')
require(product('one',12)['one']==1>h1_bound['one'], 'defect20 missing-trivial obstruction')

# One symbolic polynomial identity in k, not an actual flag or candidate scan.
def add(p,q):
    out=[0]*max(len(p),len(q))
    for i,x in enumerate(p): out[i]+=x
    for i,x in enumerate(q): out[i]+=x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def scale(c,p): return [c*x for x in p]

penalty=add(mul([10,-1],[9,-1]),mul([0,1],[-1,1]))
require(penalty==[90,-20,2], 'two-column penalty')
low_top=add([0,-8],scale(-1,penalty))
square=add([-72],scale(-2,mul([-3,1],[-3,1])))
require(low_top==[-90,12,-2]==square, 'defect20 low-top capacity square')
require(10-2*5==0 and -72 < -64, 'nonnegative coefficient and strict contradiction')
require(12-20==-8, 'defect20 coherent determinant degree')
require(10-1<12 and 2-1<12, 'positive top component degrees below invariant minimum')
require(-8-2==-10 and -8-10==-18, 'two forced coherent lower degrees')

# Actual full O2 inclusion and conditional cyclic orbit20 quotient.
require(10-2==8, 'cross-component polynomial degree')
require(product('one',8)==rep(P=1,D=1) and product('one',8)['one']==0,
        'cross-component and complement ambiguity vanish')
require(2-2==0, 'lower target line map is a constant isomorphism')
require(2+(-10)==12-20, 'retained coherent type degree')
require(10-(-10)==20, 'cyclic quotient divisor degree')
require(60//3==20 and 20//2==10 and 10*2==20, 'unique order-three fixed-point orbit')
require(12<20<24 and 30>20, 'only a single orbit20 can support degree20')
require(0+1==1 and 20*1==20, 'conditional local and global torsion lengths')

proof=(ROOT/'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest()==
        'b7f22a08e4c2e740bce1ab3340b88ef631b21f5045055c73f35fffad969c1aa5',
        'exact frozen whole-proof target')
print(json.dumps({'status':'PASS','checks':checks,
    'proof_sha256':hashlib.sha256(proof).hexdigest(),
    'scope':'Fixed physical characters, scalar quotient cohomology degrees, one symbolic two-column identity and orbit arithmetic only. No actual source-instance evaluation or candidate search.'},indent=2))
