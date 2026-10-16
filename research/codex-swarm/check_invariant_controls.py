#!/usr/bin/env python3
"""Source-free exact controls for the proposed small HM detector route.

Only the abstract ring Z[X1,Y1,...,X4,Y4], a 30-coordinate relation
pattern, and integer character/Hilbert formulas are tested. No repository
inputs, source jets, finite HM matrices, or obstruction values are read.
Checks remain enabled under python -O. Passing does not evaluate Rsharp.
"""
import itertools
import json

ZERO = (0,) * 8
UPDATES = 0
CAP_UPDATES = 100_000
CAP_TERMS = 512


def require(condition, message):
    if not condition:
        raise ValueError(message)


def checked(p):
    require(len(p) <= CAP_TERMS, "abstract polynomial term cap")
    require(all(len(m) == 8 and all(type(e) is int and e >= 0 for e in m)
                and type(c) is int and c != 0 and abs(c).bit_length() <= 128
                for m, c in p.items()), "polynomial representation")
    return p


def add(*polynomials):
    out = {}
    for p in polynomials:
        for m, coefficient in p.items():
            out[m] = out.get(m, 0) + coefficient
            if out[m] == 0:
                del out[m]
    return checked(out)


def scale(p, coefficient):
    return checked({m: c * coefficient for m, c in p.items() if c * coefficient})


def mul(p, q):
    global UPDATES
    out = {}
    for a, coefficient_a in p.items():
        for b, coefficient_b in q.items():
            UPDATES += 1
            require(UPDATES <= CAP_UPDATES, "abstract product-update cap")
            m = tuple(x + y for x, y in zip(a, b))
            out[m] = out.get(m, 0) + coefficient_a * coefficient_b
    return checked({m: c for m, c in out.items() if c})


def product(polynomials):
    out = {ZERO: 1}
    for p in polynomials:
        out = mul(out, p)
    return out


def segre_term(x_coordinates):
    chosen = set(x_coordinates)
    # Exactly one of Xi,Yi occurs for each factor i.
    return {tuple(int(j == (0 if i in chosen else 1))
                  for i in range(4) for j in range(2)): 1}


def permute_factors(p, permutation):
    require(sorted(permutation) == list(range(4)), "factor permutation")
    return checked({tuple(m[2 * permutation[i] + j]
                          for i in range(4) for j in range(2)): c
                    for m, c in p.items()})


def resolvent(v, q, factor=4):
    q2 = mul(q, q)
    return add(mul(q2, q), scale(mul(v[2], q2), -1),
               mul(add(mul(v[1], v[3]), scale(mul(v[0], v[4]), -factor)), q),
               scale(mul(v[0], mul(v[3], v[3])), -1),
               scale(mul(mul(v[1], v[1]), v[4]), -1),
               scale(product([v[0], v[2], v[4]]), factor))


def main():
    v = [add(*(segre_term(s) for s in itertools.combinations(range(4), k)))
         for k in range(5)]
    q = add(segre_term((0, 1)), segre_term((2, 3)))
    generators = ((1, 0, 2, 3), (0, 1, 3, 2), (2, 3, 0, 1))
    require(not resolvent(v, q), "homogeneous cubic identity")
    require(all(permute_factors(q, g) == q for g in generators), "D8 invariance")
    conjugates = {tuple(sorted(permute_factors(q, g).items()))
                  for g in itertools.permutations(range(4))}
    require(len(conjugates) == 3, "three distinct formal S4 conjugates")
    require(sum(permute_factors(q, g) == q
                for g in itertools.permutations(range(4))) == 8, "stabilizer order")
    # Must-fail controls: changed resolvent coefficient and a permutation
    # outside the stabilizer. These are tested, not merely described.
    require(bool(resolvent(v, q, factor=3)), "wrong cubic coefficient survived")
    require(permute_factors(q, (2, 1, 0, 3)) != q, "outside-stabilizer control")

    def orbit_dimension(n):
        z = n + 1
        numerator = z**4 + 2*z**3 + 3*z**2 + 2*z
        require(numerator % 8 == 0, "Burnside integer division")
        return numerator // 8

    choose5 = (1, 5, 10, 10, 5, 1)
    numerator = [sum((-1)**j * choose5[j] * orbit_dimension(n-j)
                     for j in range(min(n, 5)+1)) for n in range(8)]
    require(numerator == [1, 1, 1, 0, 0, 0, 0, 0], "Hilbert formula control")
    # This finite control is not itself the all-degree Hilbert proof.
    indices = [(i, 0) for i in range(5, 11)] + [(i, 1) for i in range(15) if i != 5]
    kept = {15*b+i for i, b in indices}
    pairs = [(r, 25+r) for r in range(5)] + [(10+r, 20+r) for r in range(5)]
    paired = {j for pair in pairs for j in pair}
    require(len(kept) == 20 and (10, 0) in indices and (10, 1) in indices,
            "20-map selection and existing maps")
    require(all(len(kept.intersection(pair)) == 1 for pair in pairs)
            and (set(range(30)) - paired).issubset(kept), "unit relation complement")
    bound = lambda m: min(20, m) + min(10, 5*m) + min(2, 15*m)
    require(bound(1) == 8 and bound(2) == 14 and bound(19) == 31 and bound(20) == 32,
            "minimal map count")
    print(json.dumps({"status": "pass", "ring": "Z[X1,Y1,...,X4,Y4]",
                      "abstract_product_updates": UPDATES, "conjugates": 3,
                      "stabilizer_order": 8, "selected_map_indices": indices,
                      "remaining_polynomial_rows": [10, 2],
                      "remaining_rows_computed": False,
                      "physical_source_evaluated": False, "obstruction": "undecided"},
                     sort_keys=True))


if __name__ == "__main__":
    main()
