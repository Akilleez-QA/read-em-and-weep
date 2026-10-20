"""Tiny invented tuple-chain controls; never reads or evaluates actual source data."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json


def clean(items):
    out = defaultdict(Fraction)
    for word, coefficient in items:
        out[tuple(word)] += coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def add(*chains):
    return clean((word, c) for chain in chains for word, c in chain.items())


def neg(chain):
    return {word: -c for word, c in chain.items()}


def linear(chain, operator):
    return clean((word, c*d) for source, c in chain.items()
                 for word, d in operator(source).items())


def boundary(word):
    if len(word) == 1:
        return {}
    return clean((word[:i]+word[i+1:], (-1)**i) for i in range(len(word)))


FIBERS = {0: ((0, Fraction(2)), (1, Fraction(-1))),
          1: ((2, Fraction(3)), (3, Fraction(-2)))}


def tag(a):
    return a // 2


def weighted_lists(tags, bad_sum=False):
    for choices in product(*(FIBERS[t] for t in tags)):
        coefficient = Fraction(1)
        for _, weight in choices:
            coefficient *= weight
        if bad_sum:
            coefficient *= 2 ** len(choices)
        yield tuple(owner for owner, _ in choices), coefficient


def average(word):
    return clean(weighted_lists(tuple(map(tag, word))))


def weighted_lift(tags):
    return clean(weighted_lists(tags))


def prism(word, wrong_sign=False, discard_repeats=False, bad_sum=False):
    terms = []
    for i in range(len(word)):
        for prefix, coefficient in weighted_lists(tuple(map(tag, word[:i+1])), bad_sum):
            target = prefix + word[i:]
            if discard_repeats and len(set(target)) < len(target):
                continue
            sign = 1 if wrong_sign else (-1)**i
            terms.append((target, sign * coefficient))
    return clean(terms)


def prism_error(word, **options):
    homotopy = lambda w: prism(w, **options)
    return add(linear(homotopy(word), boundary),
               linear(boundary(word), homotopy),
               neg({word: Fraction(1)}), average(word))


def plus(a, b):
    return tuple(x+y for x, y in zip(a, b))


def bound(*factors):
    result = (0, 0, 0)
    for factor in factors:
        result = plus(result, factor)
    return result


def edge(i, j, n):
    return tuple(n if k in (i, j) else 0 for k in range(3))


def full_ledger():
    result = []
    # Owner coordinates i,j,k are positions, not physical-label identities.
    for g, dg, ddg, u, du, b in ((2, 3, 4, 8, 9, (0, 0, 0)),
                                (1, 2, 3, 5, 6, (1, 2, 1))):
        outer = edge(0, 2, g)
        result.append([
            bound(outer, edge(1, 2, u), edge(0, 1, u)),
            bound(outer, edge(1, 2, du), edge(0, 1, dg)),
            bound(outer, edge(1, 2, dg), edge(0, 1, du)),
            bound(outer, edge(1, 2, ddg), edge(0, 1, ddg)),
            bound(outer, b, edge(0, 2, u)),
            bound(outer, b, b, edge(0, 2, g)),
        ])
    return result


def clearance_cases():
    # Occurrence identifiers distinguish inserted and suffix copies even if their
    # physical labels coincide. Exponents certify only formal divisor arithmetic.
    checked = 0
    for n in range(1, 7):
        for i in range(n):
            for d, weight in ((16, 54), (10, 29)):
                residual = {}
                for j in range(i+1):
                    residual[("b", j)] = weight-d
                for j in range(n):
                    residual[("a", j)] = d-(d if j >= i else 0)
                if min(residual.values()) < 0:
                    raise RuntimeError("formal source-domain clearance failed")
                # Before multiplying by output D's, the suffix is still indebted.
                if not (-d < 0):
                    raise RuntimeError("negative suffix control is broken")
                checked += 1
    return checked


def main():
    tuple_cases = 0
    repeated_cases = 0
    for degree in range(4):
        for word in product(range(4), repeat=degree+1):
            if prism_error(word):
                raise RuntimeError(("prism identity", word))
            if linear(boundary(word), boundary):
                raise RuntimeError(("boundary squared", word))
            tuple_cases += 1
            repeated_cases += len(set(word)) < len(word)
    lifting_cases = 0
    for degree in range(4):
        for tags in product(range(2), repeat=degree+1):
            lifted = weighted_lift(tags)
            if linear(lifted, boundary) != linear(boundary(tags), weighted_lift):
                raise RuntimeError(("weighted lift chain map", tags))
            retagged = clean((tuple(map(tag, word)), c) for word, c in lifted.items())
            if retagged != {tags: Fraction(1)}:
                raise RuntimeError(("Pi B identity", tags))
            lifting_cases += 1
    expected = [[(10,16,10), (5,12,11), (11,12,5), (6,8,6), (10,0,10), (4,0,4)],
                [(6,10,6), (3,8,7), (7,8,3), (4,6,4), (7,2,7), (4,4,4)]]
    ledger = full_ledger()
    if ledger != expected:
        raise RuntimeError(("full-M ledger", ledger))
    maximum = [tuple(max(row[j] for row in kind) for j in range(3)) for kind in ledger]
    if maximum != [(11,16,11), (7,10,7)]:
        raise RuntimeError(("full-M maximum", maximum))
    mutations = {}
    for name, options in (
        ("wrong_prism_sign", {"wrong_sign": True}),
        ("discard_repeated_tuples", {"discard_repeats": True}),
        ("nonunit_sum_weights", {"bad_sum": True}),
    ):
        witness = next((word for n in range(3)
                        for word in product(range(4), repeat=n+1)
                        if prism_error(word, **options)), None)
        if witness is None:
            raise RuntimeError(("mutation not rejected", name))
        mutations[name] = witness
    report = {
        "scope": "Invented rational weights, tuple chains and integer pole vectors only",
        "tuple_chain_cases": tuple_cases,
        "repeated_tuple_cases": repeated_cases,
        "weighted_lift_cases": lifting_cases,
        "clearance_cases": clearance_cases(),
        "full_M_maximum": maximum,
        "slot_multiplicities": [2, 2, 2, 1, 2, 1],
        "mutations_rejected": mutations,
        "actual_source_or_polynomial_evaluation": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
