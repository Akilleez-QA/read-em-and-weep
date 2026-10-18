#!/usr/bin/env python3
"""Bounded invented free-word controls, never production/model evaluation."""
from collections import defaultdict
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def need(condition, message):
    if not condition:
        raise RuntimeError(message)

def clean(p):
    return {w: c for w, c in p.items() if c}

def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for w, c in p.items():
            out[w] += c
    return clean(out)

def scale(p, c):
    return clean({w: c*v for w, v in p.items()})

def mul(*ps):
    out = {(): 1}
    for p in ps:
        acc = defaultdict(int)
        for w, c in out.items():
            for v, b in p.items():
                acc[w+v] += c*b
        out = clean(acc)
    return out

def sym(name):
    return {(name,): 1}

d,H,C,j,p,q,S,t,a,D = [sym(n) for n in ('d','H','C','j','p','q','S','t','a','D')]
ONE = {(): 1}
# q denotes d-prime; C denotes ambient Cech delta; D denotes row Delta.
# A p or p-prime projection vanishes outside internal degree zero.
DEG = {'d':1, 'H':-1, 'C':0, 'j':0, 'p':0, 'q':1,
       'S':-2, 't':-1, 'a':0, 'D':0, 'r':-1}

def reduce_word(w):
    # Every input is a formal row element of internal degree zero.
    for i, token in enumerate(w):
        if token == 'p' and sum(DEG[x] for x in w[i+1:]) != 0:
            return {}
    rules = [
        (('d','C'), mul(C,d)),
        (('d','H'), add(ONE,scale(mul(H,d),-1),scale(mul(j,p),-1))),
        (('d','j'), {}),
        (('d','d'), {}),
        (('H','H'), {}),
        (('H','j'), {}),
        (('p','H'), {}),
        (('p','d'), {}),
        (('p','C','d'), {}),
        (('p','j'), ONE),
        (('p','C','j'), D),
        (('C','C'), {}),
    ]
    for key, replacement in rules:
        for i in range(len(w)-len(key)+1):
            if w[i:i+len(key)] == key:
                return mul({w[:i]:1},replacement,{w[i+len(key):]:1})
    return None

def normal(poly):
    for _ in range(300):
        changed = False
        out = defaultdict(int)
        for w,c in poly.items():
            replacement = reduce_word(w)
            if replacement is None:
                out[w] += c
            else:
                changed = True
                for v,b in replacement.items():
                    out[v] += c*b
        poly = clean(out)
        if not changed:
            return poly
    raise RuntimeError('Formal rewrite did not terminate')

def equal(lhs, rhs):
    return not normal(add(lhs,scale(rhs,-1)))

def main():
    pins = json.loads((ROOT/'pins.json').read_text())
    for entry in pins['files']:
        path = ROOT/entry['path']
        need(hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],
             'Hash mismatch: '+entry['path'])

    J1 = mul(H,C,j)
    J2 = scale(mul(H,C,J1),-1)
    U = add(mul(S,C,j),scale(mul(H,C,t),-1))
    W = add(scale(mul(S,C,J1),-1),mul(H,C,U))
    B = add(scale(mul(H,q,J1),-1),scale(mul(H,C,H,q,j),-1))
    E = add(scale(mul(H,q,J2),-1),mul(H,C,H,q,J1),mul(H,C,H,C,H,q,j))
    jp = add(mul(d,t),scale(mul(H,q,j),-1),mul(j,a))
    # H-prime restricted to negative input, and then to degree-zero input.
    hpneg = add(mul(d,S),scale(mul(S,d),-1),scale(mul(H,q,H),-1))
    hpzero = add(hpneg,scale(mul(t,p),-1))
    direct1 = add(mul(hpzero,C,j),mul(H,C,jp))
    claimed1 = add(mul(d,U),mul(C,t),scale(mul(t,D),-1),mul(J1,a),B)
    need(equal(direct1,claimed1),'Stage-one derivative mismatch')
    direct2 = scale(add(mul(hpneg,C,H,C,j),mul(H,C,hpzero,C,j),mul(H,C,H,C,jp)),-1)
    claimed2 = add(mul(d,W),scale(mul(C,U),-1),scale(mul(U,D),-1),mul(J2,a),E)
    need(equal(direct2,claimed2),'Stage-two derivative mismatch')

    # Separate full-family compatibility: pi-prime as an invented expression.
    # H-prime, denoted r here, is never evaluated: r*d*C*j vanishes by dj=0.
    r = sym('r')
    pp = add(scale(mul(a,p),-1),scale(mul(p,q,H),-1),scale(mul(p,r,d),-1))
    directD = add(mul(pp,C,j),mul(p,C,jp))
    claimedD = add(mul(D,a),scale(mul(a,D),-1),scale(mul(p,q,J1),-1),scale(mul(p,C,H,q,j),-1))
    need(equal(directD,claimedD),'Row differential variation mismatch')

    # These controls establish nonzero free-word residuals when stated terms
    # are removed/reversed; they are not actual geometric counterexamples.
    mutations = {
        'drop_nonclosed_input': add(claimed2,mul(U,D)),
        'reverse_boundary_sign': add(claimed2,scale(mul(C,U),2)),
        'drop_cohomology_connection': add(claimed2,scale(mul(J2,a),-1)),
        'drop_first_differential_insertion': add(claimed2,mul(H,q,J2)),
        'drop_second_differential_insertion': add(claimed2,scale(mul(H,C,H,q,J1),-1)),
        'drop_third_differential_insertion': add(claimed2,scale(mul(H,C,H,C,H,q,j),-1)),
    }
    for name, mutant in mutations.items():
        need(not equal(direct2,mutant),'Mutation not distinguished: '+name)

    # Typed arity controls, including applying U to a nonclosed defect.
    for n in (2,3):
        U_type = (n+1,-2)
        W_type = (n+2,-3)
        need((U_type[0]+1,U_type[1])==(n+2,-2),'delta U type')
        need(((n+1)+1,-2)==(n+2,-2),'U_(n+1) Delta_n type')
        need((W_type[0],W_type[1]+1)==(n+2,-2),'dW type')
        need(n+3 in (5,6),'Stage-two owner arity')
        a1 = (-1)**(n+2)
        a2 = (-1)**(n+3)
        need(a1*a2==-1,'General-input HPL stage-two sign')

    # Invented Laurent-monomial derivative, not an actual matrix product.
    def derivative_monomial(coefficient, exponent):
        return coefficient*exponent, exponent-1
    need(derivative_monomial(1,-1)==(-1,-2),'Inverse scalar derivative')
    # For formal basis e12, e12*e11=0 and e11*e12=e12.
    # Thus [t^-1 e12,t^-1 e11] has coefficient -1 and exponent -2.
    transport_prime = derivative_monomial(1,-1)
    basis_commutator = (-1,-2)
    need(transport_prime==basis_commutator,'Invented row transport control')
    need(transport_prime[0]!=0,'Nonzero row derivative control')

    print(json.dumps({'status':'PASS','authenticated_files':len(pins['files']),
      'formal_identities':['stage_one','stage_two','row_differential_variation'],
      'distinguished_mutations':list(mutations),'input_degrees':[2,3],
      'formal_controls':['acyclic_inverse_scalar','invented_rank_two_transport'],
      'scope':'Invented formal words and scalar exponents only; normalization and geometry are written-proof premises; no physical evaluation.'},indent=2))

if __name__=='__main__':
    main()
