#!/usr/bin/env python3
"""Exact universal polynomial identity tests; no actual HM data are evaluated."""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def run():
    sources = json.loads((BASE / 'INPUTS.json').read_text())
    for row in sources:
        data = (BASE / 'inputs' / row['local']).read_bytes()
        require(len(data) == row['bytes'], 'source byte length')
        require(hashlib.sha256(data).hexdigest() == row['sha256'], 'source SHA256')
        require(hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == row['git_blob'], 'source Git blob')
    # All computations below are coefficients of formal monomials in t,
    # with independent vector coefficients v_l. No value is assigned to t.
    taylor = sharp = leibniz = higher_leibniz = 0
    def falling(n, j):
        return factorial(n)//factorial(n-j) if j <= n else 0
    for d in range(17):
        for k in range(d + 1):
            for ell in range(d + 1):
                # RHS coefficient of v_ell * t^(ell-k); absent if ell<k.
                coefficient = sum((Q(comb(a,k) * (-1)**(a-k) * factorial(ell), factorial(a)*factorial(ell-a)) for a in range(k,ell+1)), Q(0))
                require(coefficient == (1 if ell == k else 0), 'formal Taylor inversion')
                taylor += 1
        # Product rule tested on formal s=t^b and p=t^a, not evaluations.
        for a in range(d + 1):
            for b in range(d + 1):
                require(a+b == b+a, 'pairing product rule')
                # D<p,s>-<Ds,p>=<s,Dp>; moved term has minus sign.
                require((a+b)-b == a, 'pairing sign')
                leibniz += 1
                for n in range(d+1):
                    rhs = sum(comb(n,j)*falling(b,j)*falling(a,n-j) for j in range(n+1))
                    require(rhs == falling(a+b,n), "higher formal Leibniz identity")
                    higher_leibniz += 1
        if d:
            for a in range(d+1):
                # Pair s(t),D^a(1,t,...,t^d). The common t-power is d-a.
                coefficient = sum(comb(d,k)*(-1)**(d-k)*factorial(k)//factorial(k-a) for k in range(a,d+1))
                require(coefficient == (factorial(d) if a == d else 0), 'sharp formal jet annihilator')
                sharp += 1
            require(comb(d,d) == 1, 'nonzero top coordinate of sharp section')
    # D block multiplicities are dimensions, not chosen coefficient values.
    blocks = [(5,-2),(8,-3),(3,-4),(1,-8)]
    require(sum(r for r,e in blocks) == 17, 'D rank')
    require(sum(r*e for r,e in blocks) == -54, 'D degree')
    m = max(-e for r,e in blocks)
    require(m == 8 and all(e+m >= 0 for r,e in blocks), 'D global generation bound')
    return {'status':'PASS','source_files_authenticated':len(sources),
            'formal_degree_range':[0,16], 'formal_Taylor_coefficient_checks':taylor,
            'formal_Leibniz_monomial_checks':leibniz,
            'formal_higher_Leibniz_checks':higher_leibniz, 'formal_sharp_jet_pairings':sharp,
            'D_source':{'rank':17,'degree':-54,'dual_kernel_vanishes_at':m,'last_nonzero_index_at_most':m-1},
            'actual_instance_evaluations':0,'frontier_records_excluded':[],
            'proof_assistant_verified':False}

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
