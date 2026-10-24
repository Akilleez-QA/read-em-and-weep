#!/usr/bin/env python3
"""Independent fixed-identity audit; no author's code or result data imported."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
checks=0

def require(condition, message):
    global checks
    checks+=1
    if not condition:
        raise RuntimeError(message)

def q(a=0,b=0): return F(a),F(b)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b): return a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(k,a): return k*a[0],k*a[1]
def powq(a,n):
    r=q(1)
    for _ in range(n): r=mul(r,a)
    return r

def symmetric_trace(n,x):
    r=q()
    for k in range(n//2+1):
        r=add(r,scale((-1)**k*comb(n-k,k),powq(x,n-2*k)))
    return r

traces=[q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0)]
class_sizes=[1,1,12,12,12,12,20,20,30]
sym={n:[symmetric_trace(n,x) for x in traces] for n in range(11)}
P=[q(x) for x in [4,4,-1,-1,-1,-1,1,1,0]]
V=[add(a,scale(-1,b)) for a,b in zip(sym[6],P)]
chars={'one':sym[0],'W':sym[1],'A_std':sym[2],'S4':sym[3],'D':sym[4],'T6':sym[5],'V':V,'P':P}
chars['Wp']=[add(mul(x,p),scale(-1,t)) for x,p,t in zip(traces,P,sym[5])]

def tensor(a,b): return [mul(x,y) for x,y in zip(a,b)]
def inner(a,b):
    r=q()
    for size,x,y in zip(class_sizes,a,b): r=add(r,scale(F(size,120),mul(x,y)))
    require(r[1]==0,'inner product has irrational part')
    return r[0]

for a,ca in chars.items():
    for b,cb in chars.items(): require(inner(ca,cb)==(a==b),'character orthogonality '+a+' '+b)
require(inner(chars['S4'],tensor(chars['D'],chars['W']))==1,'unique source evaluation kernel')
require(inner(chars['T6'],tensor(chars['D'],chars['W']))==1,'source Clebsch-Gordan complement')
require(inner(chars['one'],tensor(chars['W'],chars['W']))==1,'unique Euler injection')
require(inner(chars['S4'],tensor(chars['W'],sym[4]))==1,'unique derivative W component')
require(inner(chars['S4'],sym[3])==1,'unique cubic evaluation')
require(inner(chars['V'],sym[4])==0,'V cannot reach scalar O')
for n in range(6): require(inner(chars['V'],sym[n])==0,'V has no low symmetric covariant '+str(n))
require(inner(chars['V'],tensor(chars['W'],sym[5]))==1,'unique nonzero V row')

sources=[('D',5,-2),('Wp',2,-3),('T6',6,-3),('V',3,-4),('one',1,-8)]
require(sum(r for _,r,_ in sources)==17,'source rank')
require(sum(r*d for _,r,d in sources)==-54,'source degree')
quotient=[(2,3),(1,2),(1,-8)]
require(sum(r for r,d in quotient)==4 and sum(r*d for r,d in quotient)==0,'quotient rank/degree')
tails=[[(3,-4),(6,-5)],[(3,-4),(4,-4),(2,-7)],[(3,-4),(5,-4),(1,-10)]]
for tail in tails:
    require(sum(r for r,d in tail)==9 and sum(r*d for r,d in tail)==-42,'tail rank/degree')
    require(4+sum(r for r,d in tail)==13 and -12+sum(r*d for r,d in tail)==-54,'K rank/degree')
require(5-4==1 and 5*(-2)-4*(-3)==2,'quartic evaluation quotient')
require(4-3==1 and 4*(-3)-3*(-4)==0,'cubic evaluation quotient')
require(3*(-4)-2*1==-14,'surjective V-row kernel degree')
require(2*(1-(-4))==10,'maximal V-row minors degree')

height_rows=[]
for h1 in range(10):
    for h2 in range(h1+1):
        h3=9-h1-h2
        if not 0<=h3<=h2: continue
        hs=[h1,h2,h3]
        value=sum(h*l-h*(h+1) for h,l in zip(hs,[6,-4,-5]))
        y,z=F(h2),F(h3)
        u,v=y-F(3,2),z-1
        square=2*(u*u+v*v+u*v)
        require(square==u*u+v*v+(u+v)*(u+v),'positive quadratic identity')
        require(value==-F(53,2)-square,'completed square')
        height_rows.append({'heights':hs,'value':value})
maximum=max(r['value'] for r in height_rows)
optimizers=[r['heights'] for r in height_rows if r['value']==maximum]
require(maximum==-27,'integer capacity maximum')
require(optimizers==[[6,2,1],[7,1,1]],'all capacity optimizers')
require(8-4*F(3,2)-2==0 and 7-2*F(3,2)-4==0,'continuous stationary point')
require(-36+8*F(3,2)+7-2*F(3,2)**2-2-3==-F(53,2),'continuous maximum')
require(46+maximum==19,'defect upper bound')
possible=sorted({12*a+20*b+30*c for a in range(2) for b in range(1) for c in range(1) if 12*a+20*b+30*c<=19})
require(possible==[0,12],'invariant defect possibilities')
require([60//n for n in [1,2,3,5]]==[60,30,20,12],'orbit sizes')
require(15*2==30 and 20*2//2==20 and 24*2//4==12,'unique exceptional orbit counts')
require(10<12,'V minors cannot have invariant common divisor')

inputs=[]
for item in json.loads((ROOT/'INPUTS.json').read_text()):
    data=(ROOT/item['file']).read_bytes()
    require(len(data)==item['bytes'],'input byte length '+item['file'])
    require(hashlib.sha256(data).hexdigest()==item['sha256'],'input sha256 '+item['file'])
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob==item['git_blob_sha1'],'input Git identity '+item['file'])
    inputs.append({'file':item['file'],'sha256':item['sha256']})
result={
    'verdict':'PASS',
    'scope':'Independent exact arithmetic and retained-source authentication; actual geometry separately reviewed in REVIEW-INDEPENDENT.md.',
    'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),
    'checks':checks,
    'independence':'No imports from characters.py, verify.py, earlier verifiers, or result files. Characters use a closed symmetric-power trace formula and class inner products.',
    'continuous_capacity_maximum':'-53/2',
    'integer_capacity_maximum':maximum,
    'capacity_optimizers':optimizers,
    'height_rows':height_rows,
    'original_defects':possible,
    'inputs':inputs,
    'limits':['Not a construction of actual maps.','Not proof-assistant certification of source premises.','No full profile or top-three-boundary exclusion.','No actual coefficients, points, parameter values, jets, tensors, or instance matrices selected.'],
}
print(json.dumps(result,indent=2))
