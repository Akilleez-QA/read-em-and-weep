#!/usr/bin/env python3
"""Independent fixed-character and provenance checks, without author imports or search."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REVIEWED_PROOF_SHA256 = 'ff1ee385836e7af3f28c3d94892939f6b3b25af5daa6ddf2d6d2ee472c1999a3'
checks = 0

def check(actual, expected, label):
    global checks
    checks += 1
    if actual != expected:
        raise RuntimeError((label, actual, expected))

def q(a, b=0):
    return F(a), F(b)

def add(x, y):
    return x[0] + y[0], x[1] + y[1]

def mul(x, y):
    return x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0]

def scale(c, x):
    return c*x[0], c*x[1]

def power(x, n):
    out = q(1)
    for _ in range(n):
        out = mul(out, x)
    return out

def sym_value(n, x):
    # The closed character polynomial, rather than any imported tensor table.
    out = q(0)
    for k in range(n//2+1):
        out = add(out, scale((-1)**k*comb(n-k, k), power(x, n-2*k)))
    return out

TRACES = [q(2), q(-2), q(F(1,2), F(1,2)), q(F(-1,2), F(-1,2)),
          q(F(1,2), F(-1,2)), q(F(-1,2), F(1,2)), q(1), q(-1), q(0)]
SIZES = [1, 1, 12, 12, 12, 12, 20, 20, 30]

def sym(n):
    return [sym_value(n, x) for x in TRACES]

def linear(*terms):
    result = [q(0)]*9
    for coefficient, vector in terms:
        result = [add(x, scale(coefficient, y)) for x, y in zip(result, vector)]
    return result

def tensor(x, y):
    return [mul(a, b) for a, b in zip(x, y)]

def galois(vector):
    return [(a, -b) for a, b in vector]

def inner(x, y):
    total = q(0)
    for n, a, b in zip(SIZES, x, y):
        total = add(total, scale(n, mul(a, b)))
    value = scale(F(1,120), total)
    check(value[1], 0, 'rational inner product')
    check(value[0].denominator, 1, 'integral inner product')
    return int(value[0])

C = {'1':sym(0), 'W':sym(1), 'A_std':sym(2), 'S4':sym(3),
     'D':sym(4), 'T6':sym(5), 'Wp':galois(sym(1)), 'V':galois(sym(2))}
C['P'] = linear((1, sym(6)), (-1, C['V']))
check(C['P'], [q(x) for x in (4,4,-1,-1,-1,-1,1,1,0)], 'physical P marking')
check(sum(SIZES), 120, 'group order')
for name, value in C.items():
    for other, other_value in C.items():
        check(inner(value, other_value), int(name == other), 'irreducible orthogonality '+name+'/'+other)

def decompose(vector):
    out = {}
    for name, value in C.items():
        multiplicity = inner(vector, value)
        if multiplicity:
            out[name] = multiplicity
    return out

def h0(blocks):
    return linear(*[(1,tensor(C[r],sym(e))) for r,e in blocks if e >= 0])

def h1(blocks):
    return linear(*[(1,tensor(C[r],sym(-e-2))) for r,e in blocks if e <= -2])

Aq = [('W',3), ('1',2), ('1',-8)]
dual_twisted = [(r,-e-2) for r,e in Aq]
check(dual_twisted, [('W',-5), ('1',-4), ('1',6)], 'dual and cotangent twist')
check(sum(int(C[r][0][0]) for r,e in Aq), 4, 'quotient rank')
check(sum(e*int(C[r][0][0]) for r,e in Aq), 0, 'quotient degree')
for r,e in Aq:
    check(C[r][1], scale(-1 if e % 2 else 1,C[r][0]), 'center-even quotient block')
check(tensor(C['W'],sym(3)), linear((1,sym(2)),(1,sym(4))), 'Clebsch-Gordan identity')
demand = decompose(h0(Aq))
check(demand, {'A_std':2, 'D':1}, 'direct section demand')
check(decompose(h1(dual_twisted)), demand, 'dual cohomology demand')
M2 = linear((1,C['A_std']), (2,C['V']), (3,C['P']), (4,C['D']))
capacity = decompose(M2)
check(capacity, {'A_std':1, 'D':4, 'V':2, 'P':3}, 'actual source capacity')
check(int(M2[0][0]), 41, 'M2 dimension')
check(capacity['A_std'] < demand['A_std'], True, 'decisive multiplicity deficit')
check(h0([('1',-1)]), linear(), 'H0 O(-1) vanishes')
check(h1([('1',-1)]), linear(), 'H1 O(-1) vanishes')
check(decompose(h1([('1',-2)])), {'1':1}, 'H1 canonical line has trivial character')

expected_pins = {
 'inputs/actual.md': ('db51525015bb7c5e825833d550d08dedf6f6ea96', 'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3'),
 'inputs/top-three.md': ('518b3f2686269f83e4f788fe4ed30d0e36dac37b', 'f81bce6251bbaf5ab9cce0bda2fda33c166e5381'),
}
remote = {e['file']:e for e in json.loads((ROOT/'INDEPENDENT-REMOTE-EVIDENCE.json').read_text())}
manifest = json.loads((ROOT/'INPUTS.json').read_text())
check(set(e['file'] for e in manifest), set(expected_pins), 'exact input set')
authenticated = []
for entry in manifest:
    name = entry['file']
    data = (ROOT/name).read_bytes()
    check((entry['ref'],entry['git_blob_sha1']),expected_pins[name], 'immutable source pin')
    check(len(data),entry['bytes'],'input byte length')
    check(hashlib.sha256(data).hexdigest(),entry['sha256'],'input SHA256')
    check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),entry['git_blob_sha1'],'input Git blob')
    check(remote[name]['content'].encode(),data,'independently fetched complete source bytes')
    check(remote[name]['git_blob_sha1'],entry['git_blob_sha1'],'remote Git blob identity')
    check(remote[name]['url'],entry['url'],'remote immutable URL')
    authenticated.append({'file':name,'sha256':entry['sha256'],'url':entry['url']})
proof_sha = hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest()
check(proof_sha,REVIEWED_PROOF_SHA256,'exact reviewed proof')

result = {
 'status':'PASS',
 'scope':'Conditional actual top-degree-three boundary exclusion for every determinant defect.',
 'proof_sha256':proof_sha,
 'checks':checks,
 'source_capacity':capacity,
 'required_target':demand,
 'deficit':{'A_std':1},
 'independent_remote_fetch':True,
 'authenticated_inputs':authenticated,
 'computation':'Fixed exact universal characters only; no actual coefficient computation or bundle search.',
 'limitation':'The written sheaf and connection arguments were reviewed mathematically; this is not proof-assistant certification of the imported geometric premises.'
}
print(json.dumps(result,indent=2,sort_keys=True))
