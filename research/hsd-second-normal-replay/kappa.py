"""Scope B: the middle cocycle, rebuilt from the quadratic BCH formula.

The section formula in build_rhs.py sees κ only through its action on v = E0.
This module never calls that formula. It rebuilds the fifteen raw quadratic
right-hand sides from the first-jet cochains η and compares them with the
Čech coboundary of κ, modulo the relation, in the symmetric square.

The equations, one coefficient at a time, are

    δκ_F = ½ {η_F on (0,1), η_F on (1,2)},
    δκ_I = ½ {η_I on (0,1), η_I on (1,2)},
    T κ_I - κ_F - δκ_H = ½ ({h, T η_I} - {η_F, h}),

where { , } is the Poisson bracket of the displayed form Ω, h is the mixed
first-jet cochain, and T is z^{-4} Sym²(T_B). For a cross monomial u_i u_j
both orders of the pair are added; a square u_i² uses that direction once.

No second-normal checker is imported, and the order-three block is not read.
"""

from fractions import Fraction

from common import (
    C4,
    DIRECTIONS,
    F,
    ONE4,
    PAIRS,
    Z4,
    add,
    mul,
    omega_pairs,
    poisson,
    relation,
    scale,
    shift,
)

TOP = (0, 1, 2)
# (δc)_{012} = c_12 - c_02 + c_01. The sign of each face is the one in that formula.
FACE_SIGN = {(0, 1): 1, (0, 2): -1, (1, 2): 1}


def tensor_add(*tensors):
    out = {}
    for tensor in tensors:
        for slot, poly in tensor.items():
            total = add(out.get(slot, {}), poly)
            if total:
                out[slot] = total
            else:
                out.pop(slot, None)
    return out


def tensor_scale(tensor, coef):
    coef = F(coef)
    if coef == 0 or not tensor:
        return {}
    out = {}
    for slot, poly in tensor.items():
        scaled = scale(poly, coef)
        if scaled:
            out[slot] = scaled
    return out


def tensor_sub(left, right):
    return tensor_add(left, tensor_scale(right, -1))


def tensor_to_ham(tensor):
    """Stored symmetric monomials: c_{ij} is the coefficient of E_i E_j, and of E_i² on the diagonal."""
    ham = {}
    for (i, j), poly in tensor.items():
        frame = [0, 0, 0, 0]
        frame[i] += 1
        frame[j] += 1
        for base, coef in poly.items():
            exp = tuple(base) + tuple(frame)
            total = ham.get(exp, 0) + coef
            if total:
                ham[exp] = total
            else:
                ham.pop(exp, None)
    return ham


def ham_to_tensor(ham):
    out = {}
    for exp, coef in ham.items():
        frame = exp[4:]
        if sum(frame) != 2:
            raise ValueError(f"frame degree {sum(frame)} is not quadratic: {exp}")
        slot = tuple(i for i, power in enumerate(frame) for _ in range(power))
        poly = out.setdefault(slot, {})
        total = poly.get(exp[:4], 0) + coef
        if total:
            poly[exp[:4]] = total
        else:
            del poly[exp[:4]]
            if not poly:
                del out[slot]
    return out


def quadratic_bracket(left, right, chart):
    """Poisson bracket of two quadratic Hamiltonians, returned in the same monomial basis."""
    if not left or not right:
        return {}
    bracket = poisson(tensor_to_ham(left), tensor_to_ham(right), omega_pairs(chart))
    return ham_to_tensor(bracket)


def _tb_images():
    """Images of the infinity frame under T_B, as finite-slot polynomials.

    T_B(P, E0, E1, E2) = (z^3 P, E0 + z C E1, z^4 E1, z^3 E2).
    """
    return (
        ((0, shift(ONE4, dz=3)),),
        ((1, ONE4),),
        ((1, mul(Z4, C4)), (2, shift(ONE4, dz=4))),
        ((3, shift(ONE4, dz=3)),),
    )


def transport_sym2(tensor):
    """z^{-4} Sym²(T_B), the infinity-to-finite transport of a quadratic Hamiltonian.

    Substitute each infinity coordinate by its T_B image and multiply by z^{-4}.
    A diagonal monomial c E_i² expands as c (Σ x_k E_k)², so the cross term
    carries the factor two. An off-diagonal monomial is bilinear in the two images.
    """
    images = _tb_images()
    out = {}
    for (i, j), poly in tensor.items():
        for k, x in images[i]:
            for l, y in images[j]:
                contrib = shift(mul(poly, mul(x, y)), dz=-4)
                slot = tuple(sorted((k, l)))
                total = add(out.get(slot, {}), contrib)
                if total:
                    out[slot] = total
                else:
                    out.pop(slot, None)
    return out


def coboundary_1(cochain):
    """Alternating coboundary of a 1-cochain on the single triple (0,1,2)."""
    return tensor_add(
        tensor_scale(cochain.get((1, 2), {}), 1),
        tensor_scale(cochain.get((0, 2), {}), -1),
        cochain.get((0, 1), {}),
    )


def coboundary_0(cochain):
    """(δc)_{ij} = c_j - c_i."""
    out = {}
    for i, j in PAIRS:
        diff = tensor_sub(cochain.get((j,), {}), cochain.get((i,), {}))
        if diff:
            out[(i, j)] = diff
    return out


def sym_product(radial, partner):
    """r ⊙ x in the stored basis: c_{ii} = r_i x_i and c_{ij} = r_i x_j + r_j x_i."""
    out = {}
    for i in range(4):
        for j in range(i, 4):
            if i == j:
                poly = mul(radial[i], partner[i])
            else:
                poly = add(mul(radial[i], partner[j]), mul(radial[j], partner[i]))
            if poly:
                out[(i, j)] = poly
    return out


def _divide_by_F(poly):
    """Divide by F = XY. Exact on the Laurent ring; a non-multiple stays non-matching later."""
    return shift(poly, dX=-1, dY=-1)


def relation_mismatch(tensor, chart):
    """Return the slots where `tensor` differs from r ⊙ x, with x read off the E2 row.

    x_E2 = c_{E2²} / F and x_i = (c_{i,E2} - r_i x_E2) / F. The zero tensor matches.
    """
    radial = relation(chart)
    x2 = _divide_by_F(tensor.get((3, 3), {}))
    partner = [None, None, None, x2]
    for i in range(3):
        raw = add(tensor.get((i, 3), {}), scale(mul(radial[i], x2), -1))
        partner[i] = _divide_by_F(raw)
    expected = sym_product(radial, partner)
    mismatch = {}
    for i in range(4):
        for j in range(i, 4):
            diff = add(tensor.get((i, j), {}), scale(expected.get((i, j), {}), -1))
            if diff:
                mismatch[(i, j)] = diff
    return mismatch


def monomial_orders():
    """Fifteen quadratic monomials and the ordered direction pairs that polarize them."""
    items = []
    for left in range(5):
        for right in range(left, 5):
            if left == right == 0:
                label = "1"
            elif left == 0:
                label = DIRECTIONS[right]
            else:
                label = f"{DIRECTIONS[left]}*{DIRECTIONS[right]}"
            ordered = [(left, right)] if left == right else [(left, right), (right, left)]
            items.append((label, ordered))
    return items


def _records_to_tensors(records):
    opens = {}
    for record in records:
        tensor = {}
        for slot, geom, value in record["terms"]:
            coef = F(value)
            if not coef:
                continue
            key = tuple(slot)
            poly = tensor.setdefault(key, {})
            exp = tuple(geom)
            poly[exp] = poly.get(exp, 0) + coef
            if not poly[exp]:
                del poly[exp]
            if not poly:
                del tensor[key]
        opens[tuple(record["open"])] = tensor_add(opens.get(tuple(record["open"]), {}), tensor)
    return opens


def load_eta(first_jet):
    """Five direction cochains, each with finite, infinity and mixed symmetric tensors."""
    blocks = {"1": first_jet["origin"]}
    for direction in first_jet["directions"]:
        blocks[direction["name"]] = direction
    missing = [name for name in DIRECTIONS if name not in blocks]
    if missing:
        raise ValueError(f"missing directions {missing}")
    eta = []
    for name in DIRECTIONS:
        block = blocks[name]
        eta.append(
            {
                chart: _records_to_tensors(block[chart])
                for chart in ("finite", "infinity", "mixed")
            }
        )
    return eta


def build_raw(eta):
    """Fifteen raw quadratic right-hand sides. κ is not an input."""
    raw = {}
    for label, ordered in monomial_orders():
        finite = {}
        infinity = {}
        mixed = {pair: {} for pair in PAIRS}
        for left, right in ordered:
            finite = tensor_add(
                finite,
                tensor_scale(
                    quadratic_bracket(
                        eta[left]["finite"].get((0, 1), {}),
                        eta[right]["finite"].get((1, 2), {}),
                        "finite",
                    ),
                    Fraction(1, 2),
                ),
            )
            infinity = tensor_add(
                infinity,
                tensor_scale(
                    quadratic_bracket(
                        eta[left]["infinity"].get((0, 1), {}),
                        eta[right]["infinity"].get((1, 2), {}),
                        "infinity",
                    ),
                    Fraction(1, 2),
                ),
            )
            for pair in PAIRS:
                head, tail = pair
                transported = transport_sym2(eta[right]["infinity"].get(pair, {}))
                cross = tensor_sub(
                    quadratic_bracket(
                        eta[left]["mixed"].get((head,), {}),
                        transported,
                        "finite",
                    ),
                    quadratic_bracket(
                        eta[left]["finite"].get(pair, {}),
                        eta[right]["mixed"].get((tail,), {}),
                        "finite",
                    ),
                )
                mixed[pair] = tensor_add(mixed[pair], tensor_scale(cross, Fraction(1, 2)))
        raw[label] = {"finite": finite, "infinity": infinity, "mixed": mixed}
    return raw


def equation_defects(raw_one, kappa_one):
    """The five tensors that must be relation multiples: finite, infinity, three mixed."""
    defects = {
        ("finite", TOP): tensor_sub(coboundary_1(kappa_one["finite"]), raw_one["finite"]),
        ("infinity", TOP): tensor_sub(coboundary_1(kappa_one["infinity"]), raw_one["infinity"]),
    }
    mixed_delta = coboundary_0(kappa_one["mixed"])
    for pair in PAIRS:
        left = tensor_sub(
            transport_sym2(kappa_one["infinity"].get(pair, {})),
            kappa_one["finite"].get(pair, {}),
        )
        left = tensor_sub(left, mixed_delta.get(pair, {}))
        defects[("mixed", pair)] = tensor_sub(left, raw_one["mixed"][pair])
    return defects


def defect_chart(kind):
    # The mixed equation is written in the finite frame, after T has been applied.
    return "infinity" if kind == "infinity" else "finite"


def evaluate(raw, kappa):
    failures = []
    checked = 0
    for label, _ordered in monomial_orders():
        for (kind, opened), defect in equation_defects(raw[label], kappa[label]).items():
            checked += 1
            mismatch = relation_mismatch(defect, defect_chart(kind))
            if mismatch:
                failures.append(
                    {
                        "monomial": label,
                        "kind": kind,
                        "open": list(opened),
                        "mismatch": mismatch,
                    }
                )
    return {"checked_equations": checked, "failures": failures}


def copy_kappa(kappa_one):
    return {
        chart: {opened: {slot: dict(poly) for slot, poly in tensor.items()} for opened, tensor in opens.items()}
        for chart, opens in kappa_one.items()
    }


def add_term(kappa_one, chart, opened, slot, exp, coef):
    """Return a copy of one κ cochain with a single stored monomial added."""
    out = copy_kappa(kappa_one)
    tensor = {key: dict(poly) for key, poly in out[chart].get(opened, {}).items()}
    poly = dict(tensor.get(slot, {}))
    poly[exp] = poly.get(exp, 0) + F(coef)
    if poly[exp] == 0:
        del poly[exp]
    if poly:
        tensor[slot] = poly
    else:
        tensor.pop(slot, None)
    out[chart][opened] = tensor
    return out


def mutation_term(slot, exp, coef):
    return {slot: {exp: F(coef)}}


def predicted_mismatches(chart, opened, slot, exp, coef):
    """Residuals of adding one E2-free monomial, from the Čech signs alone.

    Finite (0,1) enters δκ_F with sign +1 and enters the mixed equation on that
    same pair with sign -1, because that equation subtracts κ_F. An E2-free
    tensor reconstructs the zero partner, so the relation gate reports the
    signed monomial itself. Infinity and the other mixed pairs are untouched.
    """
    if 3 in slot:
        raise ValueError("this prediction is only for a term that misses E2")
    if chart != "finite" or opened != (0, 1):
        raise ValueError("prediction is stated for the finite (0,1) cochain")
    term = mutation_term(slot, exp, coef)
    return {
        ("finite", TOP): tensor_scale(term, FACE_SIGN[opened]),
        ("mixed", opened): tensor_scale(term, -1),
    }
