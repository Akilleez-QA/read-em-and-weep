#!/usr/bin/env python3
"""Independent bases of H^2(U_k) and transport-compatible H^2(W_k) for k=2,3.

Inputs are the fixed bidegrees, the finite/infinity frame weights, the original
plane cover, and the triangular infinity-to-finite transport. Shipped label
lists, stored maps, pivot sets, and expected dimensions are not read.

Arithmetic is exact over Q (fractions.Fraction). Run from any directory:

    python generate_bases.py --output frozen/basis_certificate.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path

# Fixed frame. Order is P, E0, E1, E2.
BASE_B = (3, 0, 4, 3)
PLANE_B = (-3, 0, -4, -4)
D_FINITE = (3, 0, 2, 2)
D_INFINITY = (3, 6, 0, 2)
SLOT_NAME = ("P", "E0", "E1", "E2")

# A L^{-1} I^k contributes base -1 and plane -4-k.
# L^{-1} I^k contributes base -4 and plane 2-k.


def Q(value=0):
    return Fraction(value)


def mono(z=0, x=0, y=0, w=0, coeff=1):
    coefficient = Q(coeff)
    if not coefficient:
        return {}
    return {(z, x, y, w): coefficient}


def add(*polys):
    out = {}
    for poly in polys:
        for exp, coeff in poly.items():
            total = out.get(exp, Q(0)) + coeff
            if total:
                out[exp] = total
            elif exp in out:
                del out[exp]
    return out


def scale(poly, factor):
    factor = Q(factor)
    return {exp: coeff * factor for exp, coeff in poly.items() if coeff * factor}


def shift(poly, z=0, x=0, y=0, w=0):
    return {(e[0] + z, e[1] + x, e[2] + y, e[3] + w): c for e, c in poly.items()}


def mul(left, right):
    out = {}
    for e, a in left.items():
        for f, b in right.items():
            g = (e[0] + f[0], e[1] + f[1], e[2] + f[2], e[3] + f[3])
            total = out.get(g, Q(0)) + a * b
            if total:
                out[g] = total
            elif g in out:
                del out[g]
    return out


def project_negative(poly):
    """Keep plane Laurent monomials with each of X, Y, W strictly negative."""
    return {e: c for e, c in poly.items() if e[1] < 0 and e[2] < 0 and e[3] < 0}


Z = mono(z=1)
X = mono(x=1)
Y = mono(y=1)
W = mono(w=1)
ONE = mono()
S = add(mul(X, X), mul(Y, Y))
# C = S^2 + z S W^2 + z^2 W^4, the off-diagonal polynomial in TB[E0, E1] = z C.
C = add(
    mul(S, S),
    mul(mul(Z, S), mul(W, W)),
    mul(mul(Z, Z), mul(mul(mul(W, W), W), W)),
)


def u_base(channel):
    return BASE_B[channel] - 1


def u_plane(channel, k):
    return PLANE_B[channel] - 4 - k


def w_base(i, j):
    return BASE_B[i] + BASE_B[j] - 4


def w_plane(i, j, k):
    return PLANE_B[i] + PLANE_B[j] + 2 - k


def monomial_count(total):
    """Number of u,v,w >= 0 with u+v+w = total. Equals dim H^0(P^2, O(total))."""
    if total < 0:
        return 0
    return (total + 1) * (total + 2) // 2


def enumerate_dual(total):
    for u in range(total + 1):
        for v in range(total - u + 1):
            yield (u, v, total - u - v)


def plane_monomial(dual):
    u, v, w = dual
    return mono(x=-u - 1, y=-v - 1, w=-w - 1)


def character_from_actual(e, x, y, frame_weight):
    return 2 * e + x + y - frame_weight


def h1_projective_line(degree):
    """dim H^1(P^1, O(degree)). Zero for degree >= -1."""
    if degree >= -1:
        return 0
    return -degree - 1


# Linear substitution realizing TB, before the universal z-power of TU or TW.
# Infinity frame generator i pulls back to a sum of (geometry, finite generator).
def _frame_columns():
    z3 = mul(mul(Z, Z), Z)
    z4 = mul(z3, Z)
    return (
        ((z3, 0),),
        ((ONE, 1),),
        ((mul(Z, C), 1), (z4, 2)),
        ((z3, 3),),
    )


FRAME_COLUMNS = _frame_columns()


def transport_U(infinity):
    """Infinity-to-finite map TU = z^{-1} TB on linear frame coefficients."""
    finite = {i: {} for i in range(4)}
    for channel, poly in infinity.items():
        if not poly:
            continue
        for geom, target in FRAME_COLUMNS[channel]:
            finite[target] = add(finite[target], mul(shift(geom, z=-1), poly))
    return finite


def transport_W(infinity):
    """Infinity-to-finite map TW = z^{-4} Sym^2(TB) on symmetric frame slots."""
    finite = {pair: {} for pair in combinations_with_replacement(range(4), 2)}
    for (i, j), poly in infinity.items():
        if not poly:
            continue
        for geom_i, target_i in FRAME_COLUMNS[i]:
            for geom_j, target_j in FRAME_COLUMNS[j]:
                slot = tuple(sorted((target_i, target_j)))
                geom = mul(mul(geom_i, geom_j), shift(poly, z=-4))
                finite[slot] = add(finite[slot], geom)
    return finite


def base_degree(kind, slot):
    if kind == "U":
        return u_base(slot)
    return w_base(*slot)


def plane_degree(kind, slot, k):
    if kind == "U":
        return u_plane(slot, k)
    return w_plane(*slot, k)


def frame_weight(kind, slot, chart):
    weights = D_INFINITY if chart == "infinity" else D_FINITE
    if kind == "U":
        return weights[slot]
    return weights[slot[0]] + weights[slot[1]]


def empty_components(kind):
    if kind == "U":
        return {i: {} for i in range(4)}
    return {pair: {} for pair in combinations_with_replacement(range(4), 2)}


def project_components(components):
    return {slot: project_negative(poly) for slot, poly in components.items()}


def support_negative(components):
    return {slot: poly for slot, poly in project_components(components).items() if poly}


def cancel_to_infinity(kind, slot, cancel):
    """Diagonal preimage of -cancel. Exponents stay <= 0 when cancel has z <= beta."""
    beta = base_degree(kind, slot)
    return shift(scale(cancel, -1), z=-beta)


def representative(kind, slot, e, dual, k):
    """Glued finite/infinity representative of one graded monomial.

    The finite all-negative part is the leading monomial plus the forced lower
    terms whose z exponent is at least beta(lower)+1. Terms below that cutoff
    are carried by the infinity chart. For a lower line of nonnegative base
    degree the cutoff omits its global H^2 summand, which is a separate basis
    vector. That is the connecting normalization.
    """
    beta = base_degree(kind, slot)
    if not 0 <= e <= beta:
        raise ValueError(f"z exponent {e} is outside the global range 0..{beta}")
    leading_plane = plane_monomial(dual)
    infinity = empty_components(kind)
    infinity[slot] = shift(leading_plane, z=e - beta)
    full = transport_U(infinity) if kind == "U" else transport_W(infinity)
    finite = empty_components(kind)
    expected_leading = shift(leading_plane, z=e)
    if project_negative(full[slot]) != expected_leading:
        raise ValueError(f"transport failed to reproduce the leading monomial on {slot}")
    finite[slot] = expected_leading
    for lower, poly in full.items():
        if lower == slot:
            continue
        negative = project_negative(poly)
        if not negative:
            continue
        lower_beta = base_degree(kind, lower)
        threshold = lower_beta + 1
        keep = {}
        cancel = {}
        for exp, coeff in negative.items():
            if exp[0] >= threshold:
                keep[exp] = coeff
            else:
                cancel[exp] = coeff
        if keep:
            finite[lower] = add(finite[lower], keep)
        if cancel:
            infinity[lower] = add(infinity[lower], cancel_to_infinity(kind, lower, cancel))
    glued = transport_U(infinity) if kind == "U" else transport_W(infinity)
    if support_negative(glued) != support_negative(finite):
        raise ValueError(f"finite/infinity gluing failed for {kind} {slot} e={e} dual={dual}")
    for poly in infinity.values():
        for exp in poly:
            if exp[0] > 0:
                raise ValueError("infinity representative has a positive z exponent")
    for poly in finite.values():
        for exp in poly:
            if exp[0] < 0:
                raise ValueError("finite representative has a negative z exponent")
    return finite, infinity


def forced_terms(finite, leading_slot):
    records = []
    for slot, poly in finite.items():
        if slot == leading_slot:
            continue
        for exp in sorted(poly):
            records.append(
                {
                    "slot": slot if isinstance(slot, int) else list(slot),
                    "e": exp[0],
                    "actual": [exp[1], exp[2], exp[3]],
                    "coefficient": str(poly[exp]),
                }
            )
    return records


def iter_lines(kind, k):
    if kind == "U":
        candidates = [(channel,) for channel in range(4)]
    else:
        candidates = list(combinations_with_replacement(range(4), 2))
    for raw in candidates:
        slot = raw[0] if kind == "U" else raw
        beta = base_degree(kind, slot)
        plane = plane_degree(kind, slot, k)
        if beta < 0 or plane > -3:
            continue
        total = -plane - 3
        yield slot, beta, plane, total


def build_basis(kind, k):
    vectors = []
    for slot, beta, plane, total in iter_lines(kind, k):
        weight = frame_weight(kind, slot, "finite")
        for e in range(beta + 1):
            for dual in enumerate_dual(total):
                finite, infinity = representative(kind, slot, e, dual, k)
                actual = [-dual[0] - 1, -dual[1] - 1, -dual[2] - 1]
                character = character_from_actual(e, actual[0], actual[1], weight)
                _assert_representative(kind, slot, e, dual, character, finite, infinity, k)
                vectors.append(
                    {
                        "slot": slot if isinstance(slot, int) else list(slot),
                        "e": e,
                        "dual": list(dual),
                        "actual": actual,
                        "character": character,
                        "forced": forced_terms(finite, slot),
                        "_finite": finite,
                        "_infinity": infinity,
                    }
                )
    return vectors


def _assert_representative(kind, slot, e, dual, character, finite, infinity, k):
    leading = finite[slot]
    actual = (-dual[0] - 1, -dual[1] - 1, -dual[2] - 1)
    if leading != {(e, actual[0], actual[1], actual[2]): Q(1)}:
        raise ValueError("leading symbol is not the chosen monomial")
    for lower, poly in finite.items():
        expected_plane = plane_degree(kind, lower, k)
        lower_weight = frame_weight(kind, lower, "finite")
        for exp, coeff in poly.items():
            if exp[1] + exp[2] + exp[3] != expected_plane:
                raise ValueError("forced term has the wrong plane degree")
            if character_from_actual(exp[0], exp[1], exp[2], lower_weight) != character:
                raise ValueError("forced term changes the finite character")
            if exp[0] < 0:
                raise ValueError("finite pole")
    shift_character = character - 4
    for lower, poly in infinity.items():
        lower_weight = frame_weight(kind, lower, "infinity")
        expected_plane = plane_degree(kind, lower, k)
        for exp, _coeff in poly.items():
            if exp[0] > 0:
                raise ValueError("infinity pole")
            if exp[1] + exp[2] + exp[3] != expected_plane:
                raise ValueError("infinity plane degree")
            got = character_from_actual(exp[0], exp[1], exp[2], lower_weight)
            if got != shift_character:
                raise ValueError(
                    f"infinity character {got} != finite character - 4 ({shift_character})"
                )


def coordinate_key(kind, slot, exp):
    if kind == "U":
        return (slot, exp[0], -exp[1] - 1, -exp[2] - 1, -exp[3] - 1)
    return (slot[0], slot[1], exp[0], -exp[1] - 1, -exp[2] - 1, -exp[3] - 1)


def reduced_coordinates(kind, k, finite):
    """Independent coordinates of a finite cocycle.

    Higher-slot transport forces every lower term with z >= beta(lower)+1.
    Those terms are removed. What remains must be global monomials of the
    nonnegative-base, plane-negative lines.
    """
    residual = {slot: dict(poly) for slot, poly in finite.items()}
    # Apply the forcing rules from the actual higher components still present.
    rules = _forcing_rules(kind)
    for higher, lower, _multiplicity in rules:
        higher_poly = residual.get(higher, {})
        if not higher_poly:
            continue
        forced = _forced_polynomial(kind, higher, lower, higher_poly)
        threshold = base_degree(kind, lower) + 1
        current = residual.get(lower, {})
        for exp, coeff in forced.items():
            if exp[0] < threshold:
                continue
            updated = current.get(exp, Q(0)) - coeff
            if updated:
                current[exp] = updated
            elif exp in current:
                del current[exp]
        residual[lower] = current
    coords = {}
    allowed = {}
    for slot, beta, plane, total in iter_lines(kind, k):
        allowed[slot] = (beta, plane)
    for slot, poly in residual.items():
        negative = project_negative(poly)
        if not negative:
            continue
        if slot not in allowed:
            raise ValueError(f"cocycle has a component outside the basis lines: {slot}")
        beta, plane = allowed[slot]
        for exp, coeff in negative.items():
            if not 0 <= exp[0] <= beta:
                raise ValueError(f"residual z exponent {exp[0]} outside 0..{beta} on {slot}")
            if exp[1] + exp[2] + exp[3] != plane:
                raise ValueError("residual plane degree")
            if exp[1] >= 0 or exp[2] >= 0 or exp[3] >= 0:
                continue
            coords[coordinate_key(kind, slot, exp)] = coeff
    return coords


def _forcing_rules(kind):
    """(higher slot, lower slot, multiplicity) read off Sym^2(TB) or TB.

    Multiplicity is not applied separately: _forced_polynomial recomputes the
    image from the same transport, so the multiplicity is whatever transport
    produces (1, or 2 on the square).
    """
    if kind == "U":
        return ((2, 1, 1),)
    return (
        ((0, 2), (0, 1), 1),
        ((2, 2), (1, 2), 2),
        ((2, 3), (1, 3), 1),
    )


def _forced_polynomial(kind, higher, lower, higher_poly):
    """All-negative lower component produced by the off-diagonal of TB.

    The multiplicity is 2 on a square, where both frame factors contribute,
    and 1 otherwise. Gluing against the expanded transport checks the factor.
    """
    multiplicity = {rule[:2]: rule[2] for rule in _forcing_rules(kind)}[(higher, lower)]
    return project_negative(scale(mul(shift(C, z=-3), higher_poly), multiplicity))


def assert_coordinate_identity(kind, k, vectors):
    for index, vector in enumerate(vectors):
        coords = reduced_coordinates(kind, k, vector["_finite"])
        slot = vector["slot"]
        if kind == "W":
            slot = tuple(slot)
        key = coordinate_key(
            kind,
            slot,
            (vector["e"], vector["actual"][0], vector["actual"][1], vector["actual"][2]),
        )
        if coords != {key: Q(1)}:
            raise ValueError(f"coordinate projection is not the unit vector at index {index}: {coords}")


def relation_polynomials():
    """Finite relation r0 = (-a0, W^6, -g, F), with a0=X^3+Y^3 and g=S-z W^2."""
    a0 = add(mul(mul(X, X), X), mul(mul(Y, Y), Y))
    g = add(S, scale(mul(Z, mul(W, W)), -1))
    xy = mul(X, Y)
    w6 = W
    for _ in range(5):
        w6 = mul(w6, W)
    return (scale(a0, -1), w6, scale(g, -1), xy)


def alpha_image(k, finite_u):
    """Multiply a finite U representative by the finite relation and reduce."""
    relation = relation_polynomials()
    image = empty_components("W")
    for channel, poly in finite_u.items():
        if not poly:
            continue
        for j, factor in enumerate(relation):
            slot = tuple(sorted((channel, j)))
            image[slot] = add(image[slot], mul(poly, factor))
    image = {slot: project_negative(poly) for slot, poly in image.items()}
    return reduced_coordinates("W", k, image)


def assert_alpha_lands(k, u_vectors, w_index):
    for vector in u_vectors:
        coords = alpha_image(k, vector["_finite"])
        for key in coords:
            if key not in w_index:
                raise ValueError(f"alpha image leaves the W basis at {key}")


def public_vector(vector):
    return {key: value for key, value in vector.items() if not key.startswith("_")}


def character_histogram(vectors):
    hist = defaultdict(int)
    for vector in vectors:
        hist[vector["character"]] += 1
    return {str(key): hist[key] for key in sorted(hist)}


def line_dimensions(kind, k):
    rows = []
    for slot, beta, plane, total in iter_lines(kind, k):
        count = (beta + 1) * monomial_count(total)
        rows.append(
            {
                "slot": slot if isinstance(slot, int) else list(slot),
                "base_degree": beta,
                "plane_degree": plane,
                "plane_H2_degree": total,
                "dimension": count,
            }
        )
    return rows


def connecting_vanishing(k):
    """H^3 of each extension subbundle vanishes for this normal order.

    H^3(O(b,p)) = H^1(P^1, O(b)) * H^2(P^2, O(p)). The second factor is zero
    when p > -3. The first is zero when b >= -1.
    """
    subs = []
    # U: subbundle AE0 inside AE0+AE1.
    subs.append(("U", "AE0", u_base(1), u_plane(1, k)))
    # W chains: PE0; E0E2; E0^2 and E0E1 inside the E1^2 extension.
    for slot, name in (
        ((0, 1), "PE0"),
        ((1, 3), "E0E2"),
        ((1, 1), "E0^2"),
        ((1, 2), "E0E1"),
    ):
        subs.append(("W", name, w_base(*slot), w_plane(*slot, k)))
    report = []
    for kind, name, beta, plane in subs:
        h1 = h1_projective_line(beta)
        h2_plane = 0 if plane > -3 else monomial_count(-plane - 3)
        if h1 * h2_plane != 0:
            raise ValueError(f"connecting map may be nonzero on {name} at order {k}")
        report.append(
            {
                "kind": kind,
                "subbundle": name,
                "base_degree": beta,
                "plane_degree": plane,
                "H3_dimension": 0,
            }
        )
    return report


def build_order(k):
    connecting_vanishing(k)
    u_vectors = build_basis("U", k)
    w_vectors = build_basis("W", k)
    assert_coordinate_identity("U", k, u_vectors)
    assert_coordinate_identity("W", k, w_vectors)
    w_index = {}
    for vector in w_vectors:
        key = (
            vector["slot"][0],
            vector["slot"][1],
            vector["e"],
            vector["dual"][0],
            vector["dual"][1],
            vector["dual"][2],
        )
        w_index[key] = vector
    assert_alpha_lands(k, u_vectors, w_index)
    u_lines = line_dimensions("U", k)
    w_lines = line_dimensions("W", k)
    if sum(row["dimension"] for row in u_lines) != len(u_vectors):
        raise ValueError("U enumeration disagrees with the line-dimension formula")
    if sum(row["dimension"] for row in w_lines) != len(w_vectors):
        raise ValueError("W enumeration disagrees with the line-dimension formula")
    return {
        "k": k,
        "dimension_U": len(u_vectors),
        "dimension_W": len(w_vectors),
        "characters_U": character_histogram(u_vectors),
        "characters_W": character_histogram(w_vectors),
        "lines_U": u_lines,
        "lines_W": w_lines,
        "glue_and_coordinate_checks": len(u_vectors) + len(w_vectors),
        "alpha_image_lands_in_W_basis": len(u_vectors),
        "U": [public_vector(vector) for vector in u_vectors],
        "W": [public_vector(vector) for vector in w_vectors],
    }


def assert_relation_transition():
    """TB ri = z^3 r0, including the off-diagonal E0 entry."""
    a0 = add(mul(mul(X, X), X), mul(mul(Y, Y), Y))
    g = add(S, scale(mul(Z, mul(W, W)), -1))
    xy = mul(X, Y)
    w6 = mono(w=6)
    s3 = mul(S, mul(S, S))
    r0 = (scale(a0, -1), w6, scale(g, -1), xy)
    ri = (scale(a0, -1), s3, scale(shift(g, z=-1), -1), xy)
    z3 = mul(mul(Z, Z), Z)
    image = (
        shift(ri[0], z=3),
        add(ri[1], mul(mul(Z, C), ri[2])),
        shift(ri[2], z=4),
        shift(ri[3], z=3),
    )
    expected = tuple(mul(z3, component) for component in r0)
    if image != expected:
        raise ValueError("TB ri differs from z^3 r0")


def assert_plane_homotopy():
    """delta K + K delta = 1 - Pi on plane cochains.

    Pi keeps a cochain only when every inverted coordinate is a negative
    exponent. The ordered homotopy contracts the first nonnegative coordinate.
    """

    def delta(cochain, degree):
        out = {}
        for opened in combinations(range(3), degree + 2):
            total = 0
            for index in range(len(opened)):
                face = opened[:index] + opened[index + 1 :]
                total += ((-1) ** index) * cochain.get(face, 0)
            if total:
                out[opened] = total
        return out

    def homotopy(cochain, pivot):
        out = {}
        for opened, value in cochain.items():
            if pivot not in opened:
                continue
            target = tuple(index for index in opened if index != pivot)
            sign = (-1) ** opened.index(pivot)
            out[target] = out.get(target, 0) + sign * value
        return out

    count = 0
    for mask in product((False, True), repeat=3):
        negative = {index for index, flag in enumerate(mask) if flag}
        pivot = next((index for index in range(3) if index not in negative), None)
        for degree in (1, 2):
            for opened in combinations(range(3), degree + 1):
                if not negative.issubset(opened):
                    continue
                cochain = {opened: 1}
                if pivot is None:
                    left, right = {}, {}
                else:
                    left = delta(homotopy(cochain, pivot), degree - 1)
                    right = homotopy(delta(cochain, degree), pivot)
                for target in combinations(range(3), degree + 1):
                    if not negative.issubset(target):
                        continue
                    expected = 0 if pivot is None else cochain.get(target, 0)
                    if left.get(target, 0) + right.get(target, 0) != expected:
                        raise ValueError("plane homotopy identity failed")
                count += 1
    if count == 0:
        raise ValueError("plane homotopy checked nothing")
    return count


def certificate_payload():
    assert_relation_transition()
    homotopy_checks = assert_plane_homotopy()
    orders = {str(k): build_order(k) for k in (2, 3)}
    return {
        "relation_transition_identity": True,
        "plane_homotopy_support_checks": homotopy_checks,
        "scope": "k=2,3 only",
        "arithmetic": "exact rational",
        "inputs": {
            "base_bidegrees_B": list(BASE_B),
            "plane_bidegrees_B": list(PLANE_B),
            "finite_frame_weights": list(D_FINITE),
            "infinity_frame_weights": list(D_INFINITY),
            "weights_z_X_Y_W": [2, 1, 1, 0],
            "U_scalar_base_and_plane": [-1, "-4-k"],
            "W_scalar_base_and_plane": [-4, "2-k"],
            "transport": "TU=z^{-1} TB, TW=z^{-4} Sym^2(TB), TB=diag(z^3,1,z^4,z^3) with TB[E0,E1]=z C",
            "C": "S^2 + z S W^2 + z^2 W^4",
            "negative_laurent": "X^{-u-1} Y^{-v-1} W^{-w-1}, u,v,w>=0",
            "excluded": "shipped order label lists, stored maps, pivot sets, expected dimensions",
        },
        "normalization": (
            "A graded monomial lifts by the triangular transport. "
            "On each lower line of base degree beta the finite representative keeps "
            "only z >= beta+1. Global sections 0 <= z <= beta of that line, when any "
            "exist, stay in their own basis summand."
        ),
        "orders": orders,
    }


def canonical_bytes(payload):
    return json.dumps(payload, indent=2, sort_keys=True).encode("utf-8") + b"\n"


def body_of(document):
    return {key: value for key, value in document.items() if key != "content_sha256"}


def digest_of(document):
    return hashlib.sha256(canonical_bytes(body_of(document))).hexdigest()


def attach_hash(payload):
    return {"content_sha256": digest_of(payload), **payload}


def verify_certificate(path):
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    digest = digest_of(document)
    if digest != document.get("content_sha256"):
        raise ValueError("certificate hash mismatch")
    return digest


def write_certificate(path):
    payload = attach_hash(certificate_payload())
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # The file bytes are exactly canonical_bytes of the unhashed payload, plus
    # the hash field. Recompute from the body so the recorded hash matches a
    # second run.
    return payload["content_sha256"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    digest = write_certificate(args.output)
    stored = json.loads(args.output.read_text(encoding="utf-8"))
    for k in ("2", "3"):
        order = stored["orders"][k]
        print(
            f"k={k} dim H2(U)={order['dimension_U']} dim H2(W)={order['dimension_W']} "
            f"characters U {order['characters_U']} W {order['characters_W']}"
        )
    print(f"content_sha256 {digest}")


if __name__ == "__main__":
    main()
