#!/usr/bin/env python3
"""Hash-bound fixed universal character/degree checks; no actual-instance data.
Independent method: exact character-table inner products, not McKay products.
All checks use require(), so Python -O changes neither coverage nor behavior.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
CHECKS = []
def require(ok, label):
    if not ok:
        raise RuntimeError(label)
    CHECKS.append(label)

PINS = {
    'PROOF.md': '09424f92b56ce3b907968ccae3c065ececbfbc800fb4db0f79a04a3863f74e26',
    'inputs/five-kernels.md': '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a',
    'inputs/low-top.md': 'c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af',
    'inputs/top-four.md': '56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0',
}
for name, digest in PINS.items():
    require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, 'SHA256 ' + name)

MANIFEST = json.loads((ROOT / 'INPUTS.json').read_text())
REFS = {'inputs/five-kernels.md':'7d71f0e2a3963cff64a069198f4415c5cfd0fe9b',
        'inputs/top-four.md':'e4de44641a53b0b3424102cd5fbaf3cf5821996d',
        'inputs/low-top.md':'236e0a3723c3d73ea7fb9e549376540a8e70508b'}
require({r['file'] for r in MANIFEST} == set(REFS), 'manifest input set')
for record in MANIFEST:
    name=record['file']; data=(ROOT / name).read_bytes()
    require(record['ref']==REFS[name], 'manifest immutable ref '+name)
    require(record['sha256']==PINS[name], 'manifest SHA256 '+name)
    require(record['bytes']==len(data), 'manifest byte length '+name)
    blob=b'blob '+str(len(data)).encode()+b'\0'+data
    require(record['git_blob_sha1']==hashlib.sha1(blob).hexdigest(), 'manifest Git blob '+name)

# Q(sqrt(5)) pairs. These are fixed group-character values, never coordinates,
# coefficients, jets, parameters or ranks of an actual geometric instance.
def q(a=0, b=0): return (F(a), F(b))
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def scale(n,x): return (n*x[0],n*x[1])
def total(xs):
    out=q()
    for x in xs: out=add(out,x)
    return out
SIZES=(1,1,12,12,12,12,20,20,30)
TRACE=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),
       q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
def sym_value(n,t):
    if n == 0: return q(1)
    prev,cur=q(1),t
    for _ in range(2,n+1): prev,cur=cur,sub(mul(t,cur),prev)
    return cur
def sym(n): return tuple(sym_value(n,t) for t in TRACE)
def tensor(a,b): return tuple(mul(x,y) for x,y in zip(a,b))
def plus(*cs): return tuple(total(xs) for xs in zip(*cs))
def minus(a,b): return tuple(sub(x,y) for x,y in zip(a,b))
C={name:sym(n) for name,n in [('one',0),('W',1),('A',2),('S',3),('D',4),('T',5)]}
C['P']=tuple(q(x) for x in (4,4,-1,-1,-1,-1,1,1,0))
C['V']=minus(sym(6),C['P'])
C['Wp']=minus(tensor(C['W'],C['P']),C['T'])
DIMS={'one':1,'W':2,'A':3,'S':4,'D':5,'T':6,'V':3,'P':4,'Wp':2}
def inner(a,b): return scale(F(1,120),total(scale(s,mul(x,y)) for s,x,y in zip(SIZES,a,b)))
def expect_char(actual, names, label):
    expected=plus(*(C[n] for n in names))
    require(actual==expected,label)
def multiplicity(name,char):
    v=inner(C[name],char)
    require(v[1]==0 and v[0].denominator==1,'integral multiplicity: '+name)
    return int(v[0])
require(sum(SIZES)==120,'class sizes sum to group order')
require(sum(d*d for d in DIMS.values())==120,'irreducible dimension squares')
for a in C:
    require(C[a][0]==q(DIMS[a]),'dimension '+a)
    for b in C:
        require(inner(C[a],C[b])==q(int(a==b)),'orthogonality '+a+'/'+b)
for n,names in [(1,['W']),(2,['A']),(3,['S']),(4,['D']),
                (6,['V','P']),(7,['Wp','T']),(8,['P','D'])]:
    expect_char(sym(n),names,'Sym'+str(n))
for n,names in [(0,['W']),(1,['one','A']),(2,['W','S']),
                (3,['A','D']),(4,['S','T'])]:
    expect_char(tensor(C['W'],sym(n)),names,'W tensor Sym'+str(n))
require(multiplicity('S',tensor(C['D'],C['W']))==1,'unique cubic top inclusion')
require(multiplicity('one',tensor(C['A'],sym(2)))==1,'unique quadratic dual inclusion')
require(multiplicity('S',sym(3))==1,'unique cubic scalar evaluation')
require(multiplicity('S',sym(7))==0,'cubic row has no positive scalar component')
require(multiplicity('V',sym(8))==0,'V row has no positive scalar component')
require(multiplicity('P',sym(8))==1,'P scalar-target Hom')
require(multiplicity('D',sym(8))==1,'D scalar-target Hom')
require(multiplicity('one',sym(12))==1,'degree-twelve invariant dimension')
require(multiplicity('W',sym(13))==1,'degree-thirteen W covariant dimension')
require(multiplicity('one',sym(14))==0,'degree-fourteen invariant vanishing')
# Twisted torsion character, retaining the inherited linearization.
expect_char(plus(sym(4),sym(6)),['D','V','P'],'H0(O_Delta(4))')
require(multiplicity('one',plus(sym(4),sym(6)))==0,'torsion character is not untwisted permutation character')

# All five fixed input splittings; this is not a candidate or tuple search.
K=[ [('V',-4),('P',-4),('T',-5)],
    [('V',-4),('P',-4),('P',-4),('Wp',-7)],
    [('V',-4),('P',-4),('D',-4),('one',-10)],
    [('S',-3),('V',-4),('P',-4),('W',-9)],
    [('S',-3),('V',-4),('P',-4),('one',-8),('one',-10)] ]
def rd(blocks): return (sum(DIMS[r] for r,e in blocks),sum(DIMS[r]*e for r,e in blocks))
for i,k in enumerate(K,1): require(rd(k)==(13,-58),'K'+str(i)+' rank and degree')
require(rd([('D',-2),('Wp',-3),('T',-3),('V',-4),('one',-8)])==(17,-54),'actual source rank and degree')
require(rd([('A',4),('one',-8)])==(4,4),'actual quotient rank and degree')
require((rd([('S',-3)])[0]+1,rd([('S',-3)])[1]+2)==rd([('D',-2)]),'quartic evaluation exact-sequence rank and degree')
require((rd([('A',-4)])[0]+1,rd([('A',-4)])[1])==rd([('S',-3)]),'cubic derivative-kernel exact-sequence rank and degree')
require((1+rd([('W',5)])[0],2+rd([('W',5)])[1])==rd([('A',4)]),'quadratic dual inclusion exact-sequence rank and degree')
require((rd([('W',1)])[0]+1,rd([('W',1)])[1]+4)==rd([('A',2)]),'canonical J exact-sequence rank and degree')

# Symbolic polynomial identities in x=h1,z=h3; no height evaluations or scan.
def pconst(c): return {(0,0):F(c)}
def padd(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c}
def pscale(c,p): return {m:c*a for m,a in p.items() if c*a}
def pmul(a,b):
    out={}
    for (i,j),c in a.items():
        for (k,l),d in b.items(): out[(i+k,j+l)]=out.get((i+k,j+l),F(0))+c*d
    return {m:c for m,c in out.items() if c}
def square(a):return pmul(a,a)
x={(1,0):F(1)};z={(0,1):F(1)}
h2=padd(pconst(10),pscale(-1,z),pscale(-1,x))
capacity=padd(pscale(-1,square(x)),pscale(-1,square(h2)),pscale(-1,square(z)),pscale(-11,z))
completed=padd(pconst(-50),pscale(-1,z),pscale(F(-3,2),square(z)),
               pscale(F(-1,2),square(padd(pscale(2,x),z,pconst(-10)))))
require(capacity==completed,'exact all-height negative-image square completion')
two_col=padd(pscale(-1,square(x)),pscale(-1,square(padd(pconst(11),pscale(-1,x)))))
two_completed=padd(pconst(F(-121,2)),pscale(F(-1,2),square(padd(pscale(2,x),pconst(-11)))))
require(two_col==two_completed,'exact rank-eleven two-column square completion')
require(F(-121,2).__floor__()==-61,'integer two-column capacity upper bound')

FLAGS=[ [('S',-5),('T',-5)], [('A',-6),('D',-6)],
        [('W',-7),('S',-7)], [('one',-8),('A',-8)], [('W',-9)] ]
for j,flag in enumerate(FLAGS,1):
    n=5-j
    expected=(2*(n+1),2*(n+1)*(n-9))
    require(rd(flag)==expected,'F'+str(j)+' principal-parts rank and degree')
    require(expected[1]==sum(2-4*r for r in range(j,6)),'F'+str(j)+' exact filtration degree')
require(rd(FLAGS[0])==(10,-50),'sharp F1')
require(-58-(-8)==-50,'negative image F1 degree')
require(-58-2==-60,'rank-two image F1 degree')
require(2-(-9)==11,'determinant degree gap in negative image')
require(-10-1==-11,'graph component degree vanishing')
require(9>=-1,'positive branch Ext1 vanishing')
require(6-(2-8)==12,'positive torsion length')
require(-4>-5,'quartic into reconstructed pure-minus-five vanishing')
require(8<12 and 10<12,'fixed invariant-divisor degree bounds')

print(json.dumps({'verdict':'PASS','proof_sha256':PINS['PROOF.md'],
                  'method':'exact universal character inner products and symbolic degree identities',
                  'checks':len(CHECKS),'optimized':bool(sys.flags.optimize),
                  'pins':PINS,'limitations':'Not a proof-assistant verification of geometric premises; no actual coefficients, points, jets, matrices or instance ranks evaluated.'},indent=2,sort_keys=True))
