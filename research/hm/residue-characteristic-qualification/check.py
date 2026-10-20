"""Universal synthetic arithmetic checks only. No production imports or data."""
from fractions import Fraction
from itertools import product
from math import gcd
from functools import reduce
import json

checks = 0

def require(condition, label):
    global checks
    if not condition:
        raise RuntimeError(label)
    checks += 1


def residue(a, prime):
    return all((v+1) % prime == 0 for v in a)


def certificate(a, c, prime):
    for i, v in enumerate(a):
        if (v+1) % prime:
            b = list(a)
            b[i] += 1
            return i, tuple(b), c * pow(v+1, -1, prime) % prime
    return None

for n in (1, 2, 3):
    for a in product(range(-4, 5), repeat=n):
        g = reduce(gcd, (abs(v+1) for v in a))
        for ell in (2, 3, 5, 7):
            require(residue(a, ell) == (g % ell == 0), 'gcd criterion')
            cert = certificate(a, 1, ell)
            require((cert is None) == residue(a, ell), 'certificate existence')
            if cert is not None:
                i, b, c = cert
                require(c*b[i] % ell == 1, 'monomial primitive derivative')
                require(tuple(v-(j==i) for j,v in enumerate(b)) == a,
                        'monomial primitive exponent')
            bound = max(abs(v+1) for v in a)
            if ell > bound:
                require(residue(a,ell) == all(v == -1 for v in a),
                        'safe support bound')

# Rational exact but not modular exact, ordinary residue zero.
for ell in (2,3,5,7):
    a = (ell-1,-1)
    require(a != (-1,-1) and residue(a,ell), 'extra resonance negative')
    require(Fraction(1,ell)*ell == 1, 'rational primitive')
    require((ell % ell) == 0 and ell != 0, 'modular success not rational zero')

# Bezout avoids both single-coordinate denominator primes.
require((-1)*2+1*3 == 1, 'Bezout 2,3 primitive')
require(all(not residue((1,2),p) for p in (2,3,5,7)), 'gcd one no bad primes')

# Sparse polynomial operations, used solely for tiny denominator identities.
def clean(f,p):
    return {a:c%p for a,c in f.items() if c%p}
def add(f,g,p):
    h=dict(f)
    for a,c in g.items(): h[a]=h.get(a,0)+c
    return clean(h,p)
def scale(f,c,p): return clean({a:c*v for a,v in f.items()},p)
def mul(f,g,p):
    h={}
    for a,c in f.items():
        for b,d in g.items():
            e=tuple(x+y for x,y in zip(a,b))
            h[e]=h.get(e,0)+c*d
    return clean(h,p)
def diff(f,i,p):
    h={}
    for a,c in f.items():
        b=list(a);b[i]-=1;b=tuple(b)
        h[b]=h.get(b,0)+c*a[i]
    return clean(h,p)

# Complete baseline with arbitrary small invented monomial denominator orders.
C={(0,0):1,(1,0):1,(0,1):1}
for ell in (2,3,5):
    for d in product(range(3),repeat=2):
        D=mul({d:1},C,ell)
        for b in product(range(4),repeat=2):
            a=tuple(bi-di for bi,di in zip(b,d))
            cert=certificate(a,1,ell)
            if cert is None: continue
            i,_,coefficient=cert
            shifted=list(b);shifted[i]+=1
            A=mul(C,{tuple(shifted):coefficient},ell)
            P=mul(C,{b:1},ell)
            lhs=mul(P,D,ell)
            rhs=add(mul(D,diff(A,i,ell),ell),
                    scale(mul(A,diff(D,i,ell),ell),-1,ell),ell)
            require(lhs==rhs,'denominator one identity')
            require(max(sum(a) for a in A)<=max(sum(a) for a in P)+1,
                    'total degree bound')
            for j in range(2):
                require(max(a[j] for a in A)<=max(a[j] for a in P)+(i==j),
                        'coordinate degree bound')

# Multiplicity failure: D=x^ell, vector A=1 is tangent to D, not to x.
for ell in (2,3,5,7):
    require(diff({(ell,):1},0,ell)=={}, 'inactive multiplicity derivative')
    require(diff({(1,):1},0,ell)=={(0,):1}, 'reduced factor not tangent')

print(json.dumps({'status':'pass','checks':checks,
                  'scope':'universal synthetic exponents and polynomial identities only'},sort_keys=True))
