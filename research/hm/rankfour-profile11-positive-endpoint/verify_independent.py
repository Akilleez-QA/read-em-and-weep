#!/usr/bin/env python3
"""Independent bounded audit of the positive-endpoint argument.
No author verifier, character implementation, result file, or previous verifier is imported.
No source instance, point, coefficient, jet, matrix, or broad candidate search is used.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
checks = 0

def require(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

def q(a=0, b=0):
    return F(a), F(b)

def add(x, y):
    return x[0]+y[0], x[1]+y[1]

def mul(x, y):
    return x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0]

def scale(a, x):
    return a*x[0], a*x[1]

def power(x, n):
    result = q(1)
    for _ in range(n):
        result = mul(result, x)
    return result

def sym_trace(x, n):
    result = q()
    for k in range(n//2+1):
        result = add(result, scale((-1)**k*comb(n-k, k), power(x, n-2*k)))
    return result

# Physical W trace classes. Symmetric powers use the closed binomial formula,
# independently of the author's McKay recurrence or character helper.
traces = [q(2), q(-2), q(F(1,2), F(1,2)), q(F(-1,2), F(-1,2)),
          q(F(1,2), F(-1,2)), q(F(-1,2), F(1,2)), q(1), q(-1), q()]
class_sizes = [1,1,12,12,12,12,20,20,30]
require(sum(class_sizes) == 120, 'binary icosahedral class sizes')
sym = {n: [sym_trace(t, n) for t in traces] for n in range(11)}
chars = {r: sym[n] for r,n in [('one',0), ('W',1), ('A_std',2), ('S4',3), ('D',4), ('T6',5)]}
chars['P'] = [q(v) for v in [4,4,-1,-1,-1,-1,1,1,0]]
chars['V'] = [add(x, scale(-1, y)) for x,y in zip(sym[6], chars['P'])]
chars['Wp'] = [add(mul(x,y), scale(-1,z)) for x,y,z in zip(traces, chars['P'], sym[5])]
dims = {'one':1,'W':2,'A_std':3,'S4':4,'D':5,'T6':6,'P':4,'V':3,'Wp':2}

def inner(x,y):
    result=q()
    for size,a,b in zip(class_sizes,x,y):
        result=add(result,scale(F(size,120),mul(a,b)))
    require(result[1] == 0, 'character inner product rationality')
    require(result[0].denominator == 1, 'character inner product integrality')
    return int(result[0])

for r, row in chars.items():
    require(row[0] == q(dims[r]), 'dimension '+r)
    for s, other in chars.items():
        require(inner(row,other) == int(r==s), 'character orthogonality '+r+','+s)
for n in range(6):
    require(inner(chars['V'], sym[n]) == 0, 'no rank-one V quotient at degree '+str(n))
require(inner(chars['V'], [mul(x,y) for x,y in zip(chars['W'],sym[5])]) == 1,
        'V positive row Hom dimension')
require(inner(chars['one'], sym[10]) == 0, 'no scalar row from O(-10)')
for r in chars:
    require(inner(chars[r], sym[10]) == int(r in ['A_std','D','V']),
            'complete Sym10 decomposition '+r)

shapes = {
    'K_T': [('S4',-3),('V',-4),('T6',-5)],
    'K_W': [('S4',-3),('V',-4),('P',-4),('Wp',-7)],
    'K_1': [('S4',-3),('V',-4),('D',-4),('one',-10)],
}
scalar_rows={}
negative_rows={}
expected_scalar={'K_T':[('S4',3),('T6',5)],
                 'K_W':[('S4',3),('Wp',7)],
                 'K_1':[('S4',3),('D',4)]}
for name,blocks in shapes.items():
    require(sum(dims[r] for r,e in blocks)==13, name+' rank')
    require(sum(dims[r]*e for r,e in blocks)==-54, name+' degree')
    scalar_rows[name]=[]
    negative_rows[name]=[]
    for r,e in blocks:
        multiplicity=inner(chars[r],sym[-e])
        require(multiplicity in [0,1], name+' scalar Hom multiplicity')
        if multiplicity:
            scalar_rows[name].append((r,-e))
            require(-e<12, name+' scalar base divisor bound')
        if -10-e>=0:
            m=inner(chars[r],sym[-10-e])
            if m:
                negative_rows[name].append((r,e,m))
    require(scalar_rows[name]==expected_scalar[name], name+' complete scalar source list')
    require(negative_rows[name]==([('one',-10,1)] if name=='K_1' else []),
            name+' complete negative source list')

require(2*(1-(-4))==10, 'degree of V maximal minors')
require(10<12 and max(n for rows in scalar_rows.values() for r,n in rows)<12,
        'all base divisors below least invariant orbit')
require([60//s for s in [1,2,3,5]]==[60,30,20,12], 'projective orbit sizes')

# Capacities of actual negative-kernel chains only. These are all ordered
# heights of two prescribed tiny universal domains, not bundle candidates.
def heights(n,r,prefix=()):
    if r==1:
        if not prefix or n<=prefix[-1]:
            yield prefix+(n,)
        return
    upper=min(n,prefix[-1]) if prefix else n
    for h in range((n+r-1)//r,upper+1):
        yield from heights(n-h,r-1,prefix+(h,))

def capacity_rows(n,lambdas):
    return [{'heights':list(h), 'value':sum(a*l-a*(a+1) for a,l in zip(h,lambdas))}
            for h in heights(n,len(lambdas))]

rank_two=capacity_rows(11,[1,1])
for row in rank_two:
    h,k=row['heights']
    require(row['value']==-h*h-k*k, 'rank-two simplified capacity')
    require(row['value']==-F(121,2)-2*(F(h)-F(11,2))**2,
            'rank-two completed square')
max_two=max(row['value'] for row in rank_two)
opt_two=[row['heights'] for row in rank_two if row['value']==max_two]
require(len(rank_two)==6 and max_two==-61 and opt_two==[[6,5]], 'rank-two exact optimum')
require(13-2==11 and -54-2==-56 and -56>max_two, 'rank-two contradiction')

negative_only=capacity_rows(10,[1,1,-10])
for row in negative_only:
    h,k,z=row['heights']
    value=row['value']
    bound=-50-F(z)-F(3,2)*z*z
    require(value==-h*h-k*k-z*z-11*z, 'negative-only simplified capacity')
    require(value==bound-F(h-k)**2/2, 'negative-only completed square')
    require(value<=bound<=-50, 'negative-only uniform capacity bound')
max_negative=max(row['value'] for row in negative_only)
opt_negative=[row['heights'] for row in negative_only if row['value']==max_negative]
require(max_negative==-50 and opt_negative==[[5,5,0]], 'negative-only exact optimum')
require(13-3==10 and 2-10==-8 and -54-(-8)==-46 and -46>max_negative,
        'negative-only contradiction')
require(2+1+1==4 and 4>3, 'simultaneous scalar and negative rank contradiction')

E0=[('D',-2),('Wp',-3),('T6',-3),('V',-4)]
require(sum(dims[r] for r,e in E0)==16, 'E0 rank')
require(sum(dims[r]*e for r,e in E0)==-46, 'E0 degree')
require(2*1+0==2 and 13-3==10 and -54-2==-56, 'actual positive derivative image and kernel')
require(2*3+2==8 and 16-13==3 and -46-(-54)==8, 'E0/K positive quotient')
require(8-2*3==2, 'unramified adjacent twist degree')
require(17-16==1 and -54-(-46)==-8, 'actual negative quotient cancellation')

inputs=[]
for item in json.loads((ROOT/'INPUTS.json').read_text()):
    data=(ROOT/item['file']).read_bytes()
    require(len(data)==item['bytes'], 'source byte count '+item['file'])
    digest=hashlib.sha256(data).hexdigest()
    require(digest==item['sha256'], 'source SHA256 '+item['file'])
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob==item['git_blob_sha1'], 'source Git blob '+item['file'])
    inputs.append({'file':item['file'],'sha256':digest})
result={
    'verdict':'PASS',
    'checks':checks,
    'scope':'Independent exact fixed-character, complete source-row, bounded capacity, degree, and retained-source authentication checks. Actual geometry reviewed separately.',
    'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),
    'scalar_source_rows':scalar_rows,
    'negative_source_rows':negative_rows,
    'rank_two_capacity':{'maximum':max_two,'optimizers':opt_two,'rows':rank_two},
    'negative_only_capacity':{'maximum':max_negative,'optimizers':opt_negative,'rows':negative_only},
    'inputs':inputs,
    'limits':['No actual-map construction or occurrence claim.',
              'No certification of inherited source geometry by arithmetic.',
              'No assumption of a descended flat connection on K/S4(-3).',
              'No claim that beta_E0 is everywhere full rank.',
              'No selection of one of the three K forms or original determinant defect.',
              'No top-three-boundary or full-profile closure.'],
}
print(json.dumps(result,indent=2))
