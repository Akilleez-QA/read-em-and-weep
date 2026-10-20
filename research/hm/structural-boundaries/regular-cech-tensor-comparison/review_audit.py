#!/usr/bin/env python3
"""Independent review harness; invented incidence and Laurent symbols only.
Imports the reviewed implementation as subject, with separately written incidence
operators as expectations. Does not read any source/model/physical input data.
"""
import importlib.util
import itertools as it
import json
from collections import defaultdict
from pathlib import Path

path = Path(__file__).with_name('check_controls.py')
spec = importlib.util.spec_from_file_location('reviewed_controls', path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
counts = defaultdict(int)

def require(ok, label):
    if not ok:
        raise RuntimeError(label)
    counts[label] += 1

def combine(*parts):
    out = defaultdict(int)
    for factor, chain in parts:
        for key, value in chain.items():
            out[key] += factor * value
    return {key: value for key, value in out.items() if value}

def apply(op, chain):
    return combine(*[(value, op(key)) for key, value in chain.items()])

def ds(s):
    if len(s) == 1:
        return {}
    return combine(*[((-1)**i, {s[:i]+s[i+1:]: 1}) for i in range(len(s))])

def dq(q):
    terms = []
    for i in range(len(q)):
        if q[i] == 2:
            sign = (-1)**q[:i].count(2)
            terms += [(sign, {q[:i]+(1,)+q[i+1:]: 1}),
                      (-sign, {q[:i]+(0,)+q[i+1:]: 1})]
    return combine(*terms)

def norm(s):
    if len(set(s)) != len(s):
        return {}
    sign = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:
                sign = -sign
    return {tuple(sorted(s)): sign}

def in_box(t, s):
    return all(all(w[i] in {v[i] for v in s} for i in range(4)) for w in t)

vertices = tuple(it.product((0, 1), repeat=4))
for size in range(1, 17):
    for s in it.combinations(vertices, size):
        a = m.aw(s)
        require(apply(dq, a) == apply(m.aw, ds(s)), 'all_65535_simplex_aw_chain')
        defect = combine((1, {s: 1}), (-1, apply(m.shuffle, a)))
        homotopy = combine((1, apply(ds, m.K(s))), (1, apply(m.K, ds(s))))
        require(homotopy == defect, 'all_65535_simplex_K_identity')
        require(all(in_box(t, s) for t in m.K(s)), 'all_65535_simplex_K_box')
        require(all(all((set((0, 1)) if x == 2 else {x}) <= {v[i] for v in s}
                        for i, x in enumerate(q)) for q in a), 'all_65535_simplex_aw_box')
for q in it.product((0, 1, 2), repeat=4):
    require(apply(ds, m.shuffle(q)) == apply(m.shuffle, dq(q)), 'all_81_cells_shuffle_chain')
    require(apply(m.aw, m.shuffle(q)) == {q: 1}, 'all_81_cells_retraction')

# Every ordered triple of all sixteen vertices, plus all length 1--6 tuples
# over three genuinely mixed vertices. Tuples with repeated entries remain.
tuple_set = set(it.product(vertices, repeat=3))
three = ((0,1,0,1), (1,0,1,0), (1,1,1,1))
for size in range(1, 7):
    tuple_set.update(it.product(three, repeat=size))
for s in tuple_set:
    require(apply(ds, norm(s)) == apply(norm, ds(s)), 'independent_normalization_chain')
    require(combine((1, apply(ds, m.L(s))), (1, apply(m.L, ds(s)))) ==
            combine((1, {s: 1}), (-1, norm(s))), 'expanded_all_tuple_L_identity')
    require(all(set(t) <= set(s) for t in m.L(s)), 'expanded_all_tuple_original_support')

# Treat a monomial exponent alpha as a coefficient system: allowed cells are
# precisely those on whose product domain that section is regular. This uses
# actual O(-2) chart exponent bounds in a common rational reference frame.
def regular(q, alpha):
    return all(x == 2 or (x == 0 and a >= 0) or (x == 1 and a <= -2)
               for x, a in zip(q, alpha))

def differential(f, degree):
    result = {}
    for q in it.product((0, 1, 2), repeat=4):
        if q.count(2) != degree:
            continue
        poly = combine(*[(coef, f.get(face, {})) for face, coef in dq(q).items()])
        if poly:
            result[q] = poly
    return result

def addf(*parts):
    result = {}
    keys = set().union(*(set(f) for _, f in parts))
    for key in keys:
        poly = combine(*[(coef, f.get(key, {})) for coef, f in parts])
        if poly:
            result[key] = poly
    return result

for q in it.product((0, 1, 2), repeat=4):
    n = q.count(2)
    for alpha in it.product((-3, -2, -1, 0, 1), repeat=4):
        if not regular(q, alpha):
            continue
        f = {q: {alpha: 1}}
        hf = m.H(f)
        require(all(regular(target, a) for target, p in hf.items() for a in p),
                'all_6561_regular_tensor_monomials_H_domain')
        lhs = addf((1, differential(hf, n) if n else {}),
                   (1, m.H(differential(f, n+1)) if n < 4 else {}))
        rhs = {} if q == (2,2,2,2) and alpha == (-1,-1,-1,-1) else f
        require(lhs == rhs, 'all_6561_regular_tensor_monomials_homotopy')

print(json.dumps({'status': 'PASS', 'checks': dict(sorted(counts.items())),
                  'total_checks': sum(counts.values()),
                  'scope': 'Only finite invented incidence/Laurent data; separately written boundary and regular-domain expectations.'},
                 indent=2, sort_keys=True))
