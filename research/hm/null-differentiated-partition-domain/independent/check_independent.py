#!/usr/bin/env python3
"""Invented-symbol/combinatorial controls only; no source or model imports."""
import itertools
import json

checks = {}
def require(condition, message):
    if not condition:
        raise RuntimeError(message)

# Per-occurrence additive certificates, with no disjoint-owner optimization.
scalar, current, inclusion, homotopy = (10, 2), (9, 5), (4, 2), (6, 3)
def add(a, b):
    return tuple(x+y for x,y in zip(a,b))
z = add(scalar, current)
c = add(add(add(z, inclusion), homotopy), homotopy)
require(z == (19,7) and c == (35,15), 'endpoint ledger')
require(tuple(x-y for x,y in zip((53,28),c)) == (18,13), 'derivative slack')
checks['ledger_and_slack'] = True

# Differentiate one factor of H^54 times four legal factors^29 times Q.
# Simultaneous reduced formal product divides each Leibniz summand.
original = (54,29,29,29,29)
reduced = (53,28,28,28,28)
terms = [original] + [tuple(e-(j==i) for j,e in enumerate(original)) for i in range(5)]
require(all(all(a>=b for a,b in zip(term,reduced)) for term in terms), 'formal divisibility')
# Arbitrary factor multiplicities at a prime, including shared/repeated factors.
for multiplicities in itertools.product(range(4), repeat=5):
    required = sum(a*b for a,b in zip(reduced,multiplicities))
    require(all(sum(a*b for a,b in zip(term,multiplicities)) >= required for term in terms), 'coincident divisor')
checks['product_rule_and_coincident_divisors'] = True

# All infinity-chart subsets and all derivative axes. These are transition
# exponents, not claims that chart-transition units are new allowable poles.
for chart in itertools.product((0,1), repeat=4):
    for d in range(4):
        missing = tuple((-2-2*(i!=d))*chart[i] for i in range(4))
        odd = tuple(-2*(i==d)*chart[i] for i in range(4))
        require(add(missing,odd) == tuple(-4*x for x in chart), 'missing-axis frame')
# rho=x^n: -d/dt rho(1/t) = n*t^(-n-1), and
# t^-2 * (d/dx rho)(1/t) has precisely the same coefficient/exponent.
for n in range(-8,9):
    require((n,-n-1) == (n,-(n-1)-2), 'normalized chart derivative')
checks['all_chart_frames_and_derivative_sign'] = True

# Multiplication of squarefree character masks. Only missing-axis mask can
# reach full mask under multiplication by y_d, and it has no repeated bit.
for d in range(4):
    hits = [m for m in range(16) if (m ^ (1<<d)) == 15]
    require(hits == [15 ^ (1<<d)], 'character projection')
    require(not (hits[0] & (1<<d)), 'unwanted curve factor')
checks['arbitrary_character_projection'] = True

# Synthetic owner labels distinguish common-source vertices from target tags.
# Every sampled occurrence has a weight and every tag is a target unit.
for q in (4,5):
    for k in range(q):
        a = [('a',j,j) for j in range(q)]
        b = ('b',k,k)
        occurrences = a[:k+1] + [b] + a[k+1:]
        weights = {v:'derivative' if v==b else 'ordinary' for v in occurrences}
        require(len(occurrences)==q+1 and len(weights)==q+1, 'occurrence coverage')
        require(all(v[2] in range(q) for v in occurrences), 'target units')
        require(occurrences[k][2] == occurrences[k+1][2], 'repeated pivot tag')
        require(occurrences[k] != occurrences[k+1], 'distinct source vertices')
        # A face can lose an owner, but harmless padding supplies its factor.
        for deleted in range(q+1):
            face = occurrences[:deleted] + occurrences[deleted+1:]
            require(set(face).issubset(weights), 'face clearing')
checks['full_weights_standard_units_and_faces'] = True

# Two nested HPL selections occur BEFORE deletion. Retain their owners even
# if those owners are subsequently absent from the three-input source tail.
seen_deleted_owner = False
for first in range(5):
    original_tuple = tuple(range(5))
    h1 = original_tuple[0]
    face1 = original_tuple[:first]+original_tuple[first+1:]
    h2 = face1[0]
    for second in range(4):
        tail = face1[:second]+face1[second+1:]
        all_owners = set(tail) | {h1,h2}
        require(all_owners.issubset(original_tuple), 'HPL owner outside tuple')
        require({h1,h2}.issubset(all_owners), 'lost HPL prefix owner')
        seen_deleted_owner |= h1 not in tail or h2 not in tail
require(seen_deleted_owner, 'deleted-owner control missing')
checks['retained_hpl_prefix_owners'] = True

# Source-summand alternating extension is by full source identity, not by
# the target tags attached to sampled source occurrences. This control makes
# no nonvanishing claim for repeated indices of the output target cochain.
def orientation(vertices):
    if len(set(vertices)) != len(vertices):
        return 0
    return (-1)**sum(vertices[i]>vertices[j] for i in range(len(vertices)) for j in range(i+1,len(vertices)))
require(orientation(((0,0),(0,1))) == 1, 'repeated target zero shortcut')
require(orientation(((0,1),(0,0))) == -1, 'sorting sign')
require(orientation(((0,0),(0,0))) == 0, 'source degeneracy')
checks['source_alternation'] = True

require(tuple(-4+2 for _ in range(4)) == (-2,)*4, 'Serre dual twist')
# ID0 test: (x0*x1+x2*x3)^2 has exponent vectors below.
require(all(all(e<=2 for e in term) for term in ((2,2,0,0),(1,1,1,1),(0,0,2,2))), 'test multidegree')
checks['dual_test_degree'] = True
print(json.dumps({'status':'pass','checks':checks,'scope':'Synthetic structural controls only; geometric premises and actual source denotations are not certified.'}, indent=2, sort_keys=True))
