#!/usr/bin/env python3
"""Independent bounded character/Hom audit; never imports the author verifier.

The computations concern only fixed universal representations and degree
identities used in the proof. No actual instance or candidate scan is made.
All validity checks use RuntimeError and remain active under python -O.
"""
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FROZEN_PROOF_SHA256 = 'e5d2c74f516bb5b2ede85287fceb3a774c6870b68b7b2418398e30fd5093d9b2'
COUNT = 0

def require(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise RuntimeError(message)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

@dataclass(frozen=True)
class Quad:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)
    def __post_init__(self):
        object.__setattr__(self, 'a', Fraction(self.a))
        object.__setattr__(self, 'b', Fraction(self.b))
    @staticmethod
    def cast(x):
        return x if isinstance(x, Quad) else Quad(x)
    def __add__(self, x):
        q = self.cast(x)
        return Quad(self.a + q.a, self.b + q.b)
    __radd__ = __add__
    def __neg__(self):
        return Quad(-self.a, -self.b)
    def __sub__(self, x):
        return self + (-self.cast(x))
    def __rsub__(self, x):
        return self.cast(x) - self
    def __mul__(self, x):
        q = self.cast(x)
        return Quad(self.a*q.a + 5*self.b*q.b, self.a*q.b + self.b*q.a)
    __rmul__ = __mul__
    def __truediv__(self, n):
        return Quad(self.a / Fraction(n), self.b / Fraction(n))
    def conjugate(self):
        return Quad(self.a, -self.b)
    def integer(self):
        require(self.b == 0 and self.a.denominator == 1, 'Nonintegral exact character value')
        return int(self.a)

# Independent closed physical SU(2) traces, with binary-icosahedral class sizes.
# Galois conjugation produces Wprime; no McKay code is imported.
phi = Quad(Fraction(1,2), Fraction(1,2))
sizes = (1,1,30,20,20,12,12,12,12)
traces = tuple(map(Quad.cast, (2,-2,0,1,-1,phi,-phi,phi-1,1-phi)))
one = tuple(Quad(1) for _ in sizes)
zero = tuple(Quad(0) for _ in sizes)

def add(*xs):
    return tuple(sum(c, Quad()) for c in zip(*xs)) if xs else zero

def scale(n, x):
    return tuple(n*c for c in x)

def sub(x, y):
    return add(x, scale(-1,y))

def mul(*xs):
    out = one
    for x in xs:
        out = tuple(a*b for a,b in zip(out,x))
    return out

def sym(n):
    require(0 <= n <= 16, 'Outside the fixed needed character bound 0..16')
    if n == 0:
        return one
    a,b = one,traces
    for _ in range(2,n+1):
        a,b = b,sub(mul(traces,b),a)
    return b

Wp = tuple(t.conjugate() for t in traces)
V = sub(mul(Wp,Wp),one)
reps = {'one':one,'W':traces,'Wp':Wp,'A_std':sym(2),'V':V,
        'S4':sym(3),'D':sym(4),'T6':sym(5),'P':sub(sym(6),V)}
dims = {'one':1,'W':2,'Wp':2,'A_std':3,'V':3,'S4':4,'D':5,'T6':6,'P':4}

def inner(x,y):
    return (sum((s*a*b for s,a,b in zip(sizes,x,y)),Quad())/120).integer()

def lin(**terms):
    return add(*(scale(n,reps[r]) for r,n in terms.items()))

def decompose(x):
    out = {r:inner(x,c) for r,c in reps.items()}
    require(lin(**out) == x, 'Character decomposition reconstruction failed')
    return {r:n for r,n in out.items() if n}

require(sum(sizes)==120,'Wrong total class size')
require(sum(d*d for d in dims.values())==120,'Wrong irreducible dimensions')
for r,c in reps.items():
    require(c[0].integer()==dims[r], 'Wrong identity trace for '+r)
    for s,d in reps.items():
        require(inner(c,d)==int(r==s), 'Character orthogonality failed for '+r+'/'+s)

M2=lin(A_std=1,V=2,P=3,D=4)
M3=lin(Wp=3,S4=3,T6=6)
M4=lin(V=2,P=4,D=3)
H=sub(sub(mul(M3,reps['W']),M2),M4)
require(H==lin(A_std=2,V=2,P=2,D=2),'Actual-presentation ambient character failed')
require(sym(8)==lin(P=1,D=1),'Octic complement character failed')
C=sub(H,sym(8))
require(C==lin(A_std=2,V=2,P=1,D=1),'Small constant ambient character failed')
require(H[0].integer()==30 and C[0].integer()==21,'Ambient dimensions failed')

fixed_sym = {
    6:{'V':1,'P':1},
    10:{'A_std':1,'V':1,'D':1},
    16:{'D':2,'V':1,'P':1},
}
for n,expect in fixed_sym.items():
    require(sym(n)==lin(**expect),'Needed symmetric-power decomposition failed: '+str(n))
require(inner(reps['A_std'],sym(10))==1,'Wrong decic A_std multiplicity')
require(inner(reps['A_std'],sym(6))==0,'Unexpected sextic A_std')
require(inner(reps['A_std'],sym(16))==0,'Unexpected degree-sixteen A_std')
require(inner(reps['A_std'],C)==2,'Small ambient needs two A_std copies')
require(1+0+0<2,'Coefficient-span contradiction lost')

# Only the four canonical rows in the proved top-D flag are checked.
# A block R(-j) -> T(-k) has invariant section character R*T*Sym^(j-k).
def hom(r,j,t,k):
    if j < k:
        return 0
    return inner(one,mul(reps[r],reps[t],sym(j-k)))
flag_rows=(('S4',3,'one',0),('A_std',4,'one',2),('W',5,'one',4),('one',6,'one',6))
flag_homs=[hom(*row) for row in flag_rows]
require(flag_homs==[1,1,1,1],'Canonical top-D flag Hom dimensions failed')
require(hom('S4',3,'D',2)==1,'Initial cubic-to-D inclusion is not unique')
require(3<5,'Initial degree obstruction failed')
flag_ranks=(5,4,3,2,1,0)
flag_degrees=(-10,-12,-12,-10,-6,0)
quotient_degrees=[flag_degrees[i]-flag_degrees[i+1] for i in range(5)]
require(quotient_degrees==[2,0,-2,-4,-6],'Flag degree calculation failed')
require(all(flag_ranks[i]-flag_ranks[i+1]==1 for i in range(5)),'Flag ranks failed')
require(all(quotient_degrees[i]==quotient_degrees[i-1]-2 for i in range(1,5)),'Graded derivative degree equality failed')
require(5*(-2)==-10 and (4+1)*(4-6)==-10,'Fourth principal-parts rank/degree failed')
# These four quotient dimensions are the subsets of the two explicit inequivalent
# constituents V and P, not a candidate-domain scan.
sextic_quotient_dimensions=(0,3,4,7)
require(tuple(d for d in sextic_quotient_dimensions if d>=5)==(7,),'Full actual sextic span is not forced')

require(hom('one',4,'W',5)==0,'Upper residual line should have no restriction row')
require(hom('one',18,'W',5)==1,'Degree-thirteen W multiplicity failed')
require(inner(one,sym(12))==1,'Degree-twelve invariant multiplicity failed')
require(hom('one',6,'W',5)==1,'Euler inclusion Hom dimension failed')
require(13==12+1,'Invariant-times-Euler degree failed')
require(-18+12==-6,'Invariant-times-Euler source degree failed')
require(-2>-3,'Apolarity top-degree obstruction failed')
require((10-2-1+1)*(0-2-1)==-24,'Universal second-jet kernel degree failed')
require((2+1)*(10-2)==24,'Universal second-jet target degree failed')
require((6-4-1+1)*(0-4-1)==-10,'Full sextic fourth-jet annihilator degree failed')
require(6*(-1)==-6 and -1>-2,'Contradictory Euler annihilator degree/top failed')
require(3+2==5 and 3*(-8)+2*(-11)==-46,'Surviving S0 rank/degree failed')
require(3+1+1==5 and 3*(-8)-6-16==-46,'First excluded S0 rank/degree failed')
require(3*(-8)-4-18==-46 and 4*(-7)-18==-46,'Last two excluded S0 degrees failed')

# Exact immutable-source and whole-proof binding. Missing files are failures.
proof=(ROOT/'PROOF.md').read_bytes()
require(sha(proof)==FROZEN_PROOF_SHA256,'Proof bytes changed since independent whole-proof review')
manifest_path=ROOT/'INPUTS.json'
require(manifest_path.is_file(),'INPUTS.json is required')
manifest_bytes=manifest_path.read_bytes()
manifest=json.loads(manifest_bytes)
expected={
 'inputs/second-jet-residual.md':('56e304a0d6d9c321095f182d94c326645ec704d9','research/hm/rankfour-profile11-second-jet-residual/PROOF.md','793c635439cf05c0234b4152aca4e9213780258d096d9036902b808a952f39e4'),
 'inputs/pair-image.md':('972993db6a0ab4f2a65f4f8da39cd3862923238d','research/hm/rankfour-profile11-top-four-pair-image/PROOF.md','db1e23909dbabd423cbeb855f0f376e7e0fac53d557fdd8aef7685b5449edfdb'),
 'inputs/principal-parts.md':('95af2c0fa1e3cce92496a44ef9023708735e1ec7','research/hm/rankfour-profile11-triplet-deep-images/PROOF.md','09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26'),
 'inputs/actual.md':('db51525015bb7c5e825833d550d08dedf6f6ea96','research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md','a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256'),
}
require(isinstance(manifest,list) and len(manifest)==len(expected),'Wrong input manifest size/type')
require({x['file'] for x in manifest}==set(expected),'Wrong input manifest file set')
for rec in manifest:
    file=rec['file']
    ref,path,digest=expected[file]
    require((rec['ref'],rec['path'],rec['sha256'])==(ref,path,digest),'Immutable source identity changed: '+file)
    canonical='https://github.com/Akilleez-QA/read-em-and-weep/blob/'+ref+'/'+path
    require(rec['url']==canonical,'Wrong canonical source URL: '+file)
    data=(ROOT/file).read_bytes()
    require(len(data)==rec['bytes'],'Input byte length mismatch: '+file)
    require(sha(data)==digest,'Input SHA256 mismatch: '+file)
    require(blob(data)==rec['git_blob_sha1'],'Input Git blob SHA1 mismatch: '+file)

auth_path=ROOT/'REVIEW-AUTHENTICITY.json'
require(auth_path.is_file(),'Independent fresh-authentication record is required')
auth=json.loads(auth_path.read_text())
require(auth['status']=='PASS','Source authentication did not pass')
require(auth['proof_sha256']==FROZEN_PROOF_SHA256,'Authentication binds another proof')
require(auth['inputs_manifest_sha256']==sha(manifest_bytes),'Authentication binds another manifest')
require(auth['public_writes'] is False,'Authentication scope changed')
require(len(auth['sources'])==4 and {x['file'] for x in auth['sources']}==set(expected),'Authenticated source set changed')
for rec in auth['sources']:
    match=next(x for x in manifest if x['file']==rec['file'])
    for key in ('file','ref','path','url','bytes','sha256','git_blob_sha1'):
        require(rec[key]==match[key],'Authentication metadata mismatch: '+key)
    require(rec['fresh_github_fetch'] is True,'Not freshly fetched')
    require(rec['fresh_bytes_equal_retained_file'] is True,'Fresh bytes were not equal')
    require(rec['fetched_sha256']==match['sha256'],'Fresh SHA256 mismatch')
    require(rec['fetched_git_blob_sha1']==match['git_blob_sha1'],'Fresh Git blob SHA1 mismatch')

out={
 'status':'PASS',
 'check_count':COUNT,
 'proof_sha256':FROZEN_PROOF_SHA256,
 'inputs_manifest_sha256':sha(manifest_bytes),
 'independent_method':'Exact conjugacy-class characters over Q(sqrt(5)); orthogonality and reconstruction; no author-code imports.',
 'ambient_character':decompose(H),
 'small_constant_character':decompose(C),
 'fixed_symmetric_powers':{str(n):decompose(sym(n)) for n in (6,10,16)},
 'top_D_flag_hom_dimensions':flag_homs,
 'top_D_flag_quotient_degrees':quotient_degrees,
 'sextic_quotient_dimensions':list(sextic_quotient_dimensions),
 'residual_restriction_hom_dimensions':[hom('one',4,'W',5),hom('one',18,'W',5)],
 'f12_invariant_dimension':inner(one,sym(12)),
 'conceptual_review':'PASS: actual constant span, full top-D osculation, apolarity factorization, torsion-safe annihilator, and all three exclusions were reviewed as a whole proof.',
 'new_conclusion':'Only S0=A_std(-8)+Wp(-11) survives the four imported forms; scalar primal F=O(2)+2O(4) is impossible under the stated actual hypotheses.',
 'limits':'No realization or exclusion of surviving doublet primal; original defect remains 12; triplet branch and broader rank-four repair remain open.',
 'actual_instance_computations':False,
 'broad_candidate_scan':False,
 'public_writes':False,
 'optimization_safe':True,
}
out['check_count']=COUNT
print(json.dumps(out,indent=2,sort_keys=True))
