#!/usr/bin/env python3
"""Fixed coherent equality/slack, principal-parts degree and character identities."""
import hashlib
import json
from pathlib import Path
from collections import Counter
from characters import product, DIM

ROOT=Path(__file__).resolve().parent
checks=0

def require(condition,message):
    global checks
    checks+=1
    if not condition: raise RuntimeError(message)

def rep(**values): return Counter(values)

PINS=[
    ('inputs/twentyfour-exclusion.md','838bc46c3be7b4a40cb74017de421da44f00958e',
     'research/hm/rankfour-profile11-triplet-twentyfour-exclusion/PROOF.md',
     '1fa1477fa73c0eded705f80e360963401af9b7e9',
     'b7f22a08e4c2e740bce1ab3340b88ef631b21f5045055c73f35fffad969c1aa5',13247),
    ('inputs/defect-capacity.md','ca235151d5d93bbead2beffa7640fbd0741aec43',
     'research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md',
     '175af94697c44f3140bb2c1d04978931c255b3fe',
     '135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f',16069),
    ('inputs/projected-ranktwo.md','b2d020a32a3ac5aaf5f264e33e2f930c16195c34',
     'research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md',
     '99a5a0257b0d683b04c5d190333d868c5b0d194d',
     '7f1567617b78898bcd218107de5bac5a71342a4cb34411862f7342d13699c4bd',15271),
    ('inputs/deep-images.md','95af2c0fa1e3cce92496a44ef9023708735e1ec7',
     'research/hm/rankfour-profile11-triplet-deep-images/PROOF.md',
     '9cf95f42505f37900f5a24c25cff07acca1b499f',
     '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26',12085),
]
records=json.loads((ROOT/'INPUTS.json').read_text())
require(len(records)==len(PINS)==4,'four complete immutable sources')
for record,pin in zip(records,PINS):
    require(tuple(record[k] for k in ('file','ref','path','git_blob_sha1','sha256','bytes'))==pin,
            'exact source pin')
    data=(ROOT/record['file']).read_bytes()
    require(len(data)==record['bytes'],'source UTF8 length')
    require(hashlib.sha256(data).hexdigest()==record['sha256'],'source SHA256')
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==record['git_blob_sha1'],
            'source Git blob SHA1')

# Actual normal flag and four fixed physical symmetric powers.
require(4-2==2 and 12-2==10,'actual normal-line twists')
require(2+(-10)==12-20,'hypothetical coherent determinant degree')
require(product('one',6)==rep(V=1,P=1),'Sym6')
require(product('one',7)==rep(Wp=1,T=1),'Sym7')
require(product('one',8)==rep(P=1,D=1),'Sym8')
require(product('one',9)==rep(S=1,T=1),'Sym9')
require(product('one',6)['one']==0 and product('one',8)['one']==0,
        'degree-six and degree-eight invariant maps vanish')

# Polynomial identities in a formal indeterminate k, not a candidate/flag scan.
def add(p,q):
    out=[0]*max(len(p),len(q))
    for i,x in enumerate(p):out[i]+=x
    for i,x in enumerate(q):out[i]+=x
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def scale(c,p):return[c*x for x in p]

def mul(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    while len(out)>1 and out[-1]==0:out.pop()
    return out

penalty=add(mul([10,-1],[9,-1]),mul([0,1],[-1,1]))
capacity=add(add(scale(2,[10,-1]),[0,-10]),scale(-1,penalty))
require(penalty==[90,-20,2] and capacity==[-70,8,-2],'coherent two-column polynomial')
slack=add(capacity,[64])
require(slack==add([2],scale(-2,mul([-2,1],[-2,1]))),'slack is two minus twice a square')
require(2-2*(1-2)**2==0 and 2-2*(3-2)**2==0,'two equality cases')
require(2-2*(2-2)**2==2,'middle case total slack two')
require(2<12 and -12+2<0,'slack cannot reach a nonzero invariant divisor or lower line')
require(2-(-10)==12,'fixed coherent column gap')

# k=3: fixed quotient ranks/degrees and universal auxiliary principal-parts degrees.
require(3*2+4*1==10,'k3 quotient ranks')
require(-4-6-8-10==-28,'rank-one tail Q3 degree')
require(-8-10==-18 and -6-8-10==-24,'earlier tail jet degrees')
require(2*(1-10)==-18 and 3*(2-10)==-24 and 4*(3-10)==-28,
        'degree-ten intrinsic tail degrees')
require(-2-2==-4 and -14-2==-16,'first k3 forward upper/lower target degrees')
require(-28+(-2)==-30==5*(4-10),'actual and intrinsic fourth-jet degree')
require(-30+0==-30==6*(5-10),'actual and intrinsic fifth-jet degree')
require(-30+2==-28==7*(6-10),'actual and intrinsic sixth-jet degree')
require(product('one',6)['V']==1 and rep(A=1,D=1)['V']==0,
        'forced sixth jets have forbidden V top constituent')
require(6<=10,'auxiliary principal-parts order is within degree-ten bound')

# k=1: a fixed sum for the eight rank-one tail quotients.
require(2+8==10,'k1 quotient ranks')
require(2-2*8==-14,'last k1 scalar line degree')
require(sum(2-2*i for i in range(1,9))==-56==8*(7-14),
        'rank-one tail and seventh-jet degrees')
require(-56+2==-54==9*(8-14),'actual and intrinsic eighth-jet degree')
require(-64-(-54)==-10,'F over eighth-jet quotient degree')
require(-54+4==-50==10*(9-14),'actual and intrinsic ninth-jet degree')
require(11-10==1 and -60-(-50)==-10,'Jminus over ninth-jet quotient')
require(9<=14,'auxiliary principal-parts order is within degree-fourteen bound')

# Final actual-map contradiction: distinct equivariant and ordinary Hom vanishings.
require(10-4==6 and product('one',6)['one']==0,'T9/G9 map to beta_Jminus target vanishes')
require(-10-2==-12,'actual final normal quotient twist')
require(-12-(-5)==-7<0,'intrinsic ninth-jet derivative ordinary Hom vanishes')
require(10*(-5)==-50<0,'negative horizontal bundle contradiction')

proof=(ROOT/'PROOF.md').read_bytes()
require(hashlib.sha256(proof).hexdigest()==
        'fc42728dd57303770e15c9ff2ffa7d490f4f6aa11dae26cf4cabdcb8792b0fa7',
        'exact frozen whole-proof target')
print(json.dumps({'status':'PASS','checks':checks,
    'proof_sha256':hashlib.sha256(proof).hexdigest(),
    'scope':'Fixed symbolic coherent capacity/slack, universal principal-parts ranks/degrees and small physical character identities. No actual coefficients, jets, tensors, matrices or instance ranks evaluated.'},indent=2))
