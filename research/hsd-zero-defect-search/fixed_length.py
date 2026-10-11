"""Exact length of the pinned five-relation module, and the parameter obstruction.

The relations are those of coker(H_0^T) in PR #1 comment 6104798062,
reproduced by the grevlex encoding of comment 6104803214.  Generators are
e1, e2 over B = Q[x, y, w].  The formal-lift coordinates (a, b, c, d, lambda)
do not occur.

Run: python fixed_length.py
"""

from __future__ import annotations

import sympy as sp

# Chart coordinates.  They are not indeterminates of the pinned module.
CHART = sp.symbols("a b c d lam")
E1, E2, X, Y, W = sp.symbols("e1 e2 x y w")
GENS = (E1, E2, X, Y, W)
BASE = (X, Y, W)

# Comment 6104798062, in generator order (e1, e2).
FROZEN_RELATIONS = (
    (-X * Y / 2, 0),
    (-(W**2) * X / 2, 0),
    ((X + Y) / 2, -(W**2) / 2),
    (-(W**2) / 8, -X / 2),
    (-(W**2) / 8, Y / 2),
)

# Comment 6104798062 leading module monomials, written e1 / e2.
EXPECTED_LEADING = {
    E1 * Y**3,
    E1 * X**2,
    E1 * X * Y,
    E2 * Y**2,
    E2 * W**2,
    E1 * W**2,
    E2 * X,
}
EXPECTED_STANDARD = {
    E1,
    W * E1,
    X * E1,
    X * W * E1,
    Y * E1,
    Y * W * E1,
    Y**2 * E1,
    Y**2 * W * E1,
    E2,
    W * E2,
    Y * E2,
    Y * W * E2,
}


def module_generators(relations):
    """Encode a submodule of B^2 as an ideal, killing e1^2, e1*e2, e2^2."""
    polynomials = [e1_coeff * E1 + e2_coeff * E2 for e1_coeff, e2_coeff in relations]
    polynomials.extend((E1**2, E1 * E2, E2**2))
    return polynomials


def groebner(polynomials):
    return sp.groebner(polynomials, *GENS, order="grevlex", domain=sp.QQ)


def leading_module_monomials(basis):
    found = set()
    for poly in basis:
        lead = sp.LT(
            sp.Poly(poly, *GENS, domain=sp.QQ).as_expr(),
            *GENS,
            order=sp.grevlex,
        )
        if lead.free_symbols <= {E1, E2, X, Y, W} and (
            sp.total_degree(lead, E1, E2) == 1
        ):
            found.add(lead)
    return found


def exponent(monomial):
    polynomial = sp.Poly(monomial, *GENS, domain=sp.QQ)
    monoms = polynomial.monoms()
    if len(monoms) != 1 or polynomial.LC() != 1:
        raise RuntimeError(f"not a monic monomial: {monomial}")
    return monoms[0]


def divides(divisor, target):
    return all(left <= right for left, right in zip(divisor, target))


def pure_power_bounds(leads_for_generator):
    """Largest pure power of each base variable in the initial module."""
    bounds = []
    for axis in range(3):
        powers = [
            exp[2 + axis]
            for exp in leads_for_generator
            if exp[2 + axis] > 0
            and all(exp[2 + other] == 0 for other in range(3) if other != axis)
        ]
        if not powers:
            return None
        bounds.append(max(powers))
    return tuple(bounds)


def standard_monomials(leads):
    by_generator = {0: [], 1: []}
    for lead in leads:
        exp = exponent(lead)
        if exp[0] + exp[1] != 1:
            raise RuntimeError(f"leading term is not linear in the generators: {lead}")
        by_generator[0 if exp[0] == 1 else 1].append(exp)

    standard = []
    for index, generator in ((0, E1), (1, E2)):
        bounds = pure_power_bounds(by_generator[index])
        if bounds is None:
            raise RuntimeError(
                f"initial module on generator {index} has no pure-power bound; "
                "length is not certified finite by the leading terms"
            )
        for px in range(bounds[0]):
            for py in range(bounds[1]):
                for pw in range(bounds[2]):
                    exp = [0, 0, px, py, pw]
                    exp[index] = 1
                    if any(divides(lead, exp) for lead in by_generator[index]):
                        continue
                    standard.append(generator * X**px * Y**py * W**pw)
    return standard


def length_of(relations):
    basis = groebner(module_generators(relations))
    leads = leading_module_monomials(basis)
    standard = standard_monomials(leads)
    return leads, standard, len(standard)


def assert_no_chart_parameters(relations):
    for e1_coeff, e2_coeff in relations:
        used = (sp.sympify(e1_coeff).free_symbols | sp.sympify(e2_coeff).free_symbols)
        hit = used & set(CHART)
        if hit:
            raise RuntimeError(f"chart parameter leaked into a frozen relation: {hit}")
        extra = used - set(BASE)
        if extra:
            raise RuntimeError(f"relation uses symbols outside Q[x,y,w]: {extra}")


def main():
    assert_no_chart_parameters(FROZEN_RELATIONS)
    leads, standard, length = length_of(FROZEN_RELATIONS)
    if leads != EXPECTED_LEADING:
        raise SystemExit(f"leading monomials differ:\n got {leads}\n expected {EXPECTED_LEADING}")
    if set(standard) != EXPECTED_STANDARD:
        raise SystemExit(
            f"standard monomials differ:\n got {set(standard)}\n expected {EXPECTED_STANDARD}"
        )
    if length != 12:
        raise SystemExit(f"fixed carrier length is {length}, not 12")

    # Must-fail control: the same counter, on a different module, must not
    # still report 12.  Adding 1 to the first coefficient keeps a pure-power
    # initial bound, so the length is finite and is read from the relations.
    perturbed = list(FROZEN_RELATIONS)
    perturbed[0] = (perturbed[0][0] + 1, perturbed[0][1])
    _, _, perturbed_length = length_of(perturbed)
    if perturbed_length == 12:
        raise SystemExit("perturbing a relation still reported length 12")

    print("fixed_carrier_length", length)
    print("leading_module_monomials", len(leads))
    print("standard_monomials", length)
    print("chart_parameters_in_relations", 0)
    print("perturbed_relation_length", perturbed_length)
    print("slice_search", "inconclusive")
    print(
        "obstruction",
        "no presentation of coker(H_0^T) over Q[a,b,c,d,lam][x,y,w] is pinned",
    )


if __name__ == "__main__":
    main()
