#!/usr/bin/env python3
"""Exact character count for the pinned HKR space HT^2(X), X = C^4.

Pins used as input, not recomputed here:
- research/hsd/gate-ladder.md at d915eeab, lines 25-35 and 57:
  V_i dual to dx_i/y_i, G = (Z/2)^4 by y_i |-> -y_i,
  pi = V_1 wedge V_2 + V_3 wedge V_4 has deck characters {1,2} and {3,4},
  H^1(T_X)^G is spanned by the four diagonal product-elliptic directions.
- research/hm/ext-model.md at add03476: Ext^2 is indexed by subsets
  S subset {1,2,3,4}, and the weight-4 row is the full-sign character.

Arithmetic is in Q via fractions.Fraction. Gaussian elimination decides ranks.
"""

from fractions import Fraction


FACTORS = (1, 2, 3, 4)


def bit(i):
    return 1 << (i - 1)


def popcount(mask):
    return bin(mask).count("1")


def subset(mask):
    return tuple(i for i in FACTORS if mask & bit(i))


def form_character():
    """Coefficient of dx_i/y_i under y_i |-> -y_i.

    dx_i/(-y_i) = - dx_i/y_i, so the coefficient is -1.
    A character of (Z/2) is recorded as the mask of factors that act by -1.
    """
    coefficient = Fraction(-1, 1)
    if coefficient not in (Fraction(1), Fraction(-1)):
        raise SystemExit("form coefficient is not a unit sign")
    return coefficient


def rank(matrix):
    """Exact rank over Q. matrix is a list of rows of Fraction."""
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    n = len(rows)
    m = len(rows[0])
    rank_found = 0
    col = 0
    while rank_found < n and col < m:
        pivot = None
        for i in range(rank_found, n):
            if rows[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rank_found], rows[pivot] = rows[pivot], rows[rank_found]
        pivot_value = rows[rank_found][col]
        for j in range(col, m):
            rows[rank_found][j] /= pivot_value
        for i in range(n):
            if i == rank_found or rows[i][col] == 0:
                continue
            factor = rows[i][col]
            for j in range(col, m):
                rows[i][j] -= factor * rows[rank_found][j]
        rank_found += 1
        col += 1
    return rank_found


def basis(tangent_masks, eta_masks, extra=()):
    """Eigenbasis of the three HKR summands.

    tangent_masks[i] is the character mask of V_{i+1}.
    eta_masks[i] is the character mask of the Kunneth class eta_{i+1}
    in H^1(O) pulled back from the i-th factor.
    extra is a tuple of (name, mask) vectors appended as a corruption.
    """
    items = []
    for i in FACTORS:
        for j in FACTORS:
            if i < j:
                mask = tangent_masks[i - 1] ^ tangent_masks[j - 1]
                items.append((f"V{i}^V{j}", mask, "H0"))
    for i in FACTORS:
        for a in FACTORS:
            mask = eta_masks[i - 1] ^ tangent_masks[a - 1]
            items.append((f"eta{i}*V{a}", mask, "H1"))
    for i in FACTORS:
        for j in FACTORS:
            if i < j:
                mask = eta_masks[i - 1] ^ eta_masks[j - 1]
                items.append((f"eta{i}*eta{j}", mask, "H2"))
    for name, mask in extra:
        items.append((name, mask, "extra"))
    return items


def projector(items, character):
    """Group-average projector onto one character, in the eigenbasis.

    P = (1/|G|) sum_g chi(g) rho(g), with chi = chi^{-1}.
    rho(g) is diagonal. Entries are computed in Q, then the rank is the
    rank of this matrix, not a count of labels.
    """
    n = len(items)
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    order = 16
    for g in range(order):
        chi_sign = Fraction(1 if popcount(character & g) % 2 == 0 else -1)
        for i, (_name, mask, _summand) in enumerate(items):
            eig = Fraction(1 if popcount(mask & g) % 2 == 0 else -1)
            matrix[i][i] += chi_sign * eig / order
    return matrix


def multiplicity_from_projector(items):
    """Multiplicity of each character is the exact rank of its projector."""
    counts = {}
    for mask in range(16):
        counts[mask] = rank(projector(items, mask))
    return counts


def kernel_dimension(columns):
    """Kernel dimension of a map Q^s -> Q^t given by columns.

    columns is a list of columns, each a tuple of Fraction.
    An empty list of columns is the unique map out of the zero space.
    """
    if not columns:
        return 0
    rows = list(zip(*columns))
    matrix = [list(row) for row in rows]
    image_rank = rank(matrix)
    return len(columns) - image_rank


def pinned_signs():
    """V_i has character {i}, because dx_i/y_i scales by -1 under y_i |-> -y_i.

    The four diagonal classes eta_i * V_i are the product-elliptic directions.
    The pin says they span H^1(T)^G, so each is invariant. Therefore eta_i
    has the same character as V_i.
    """
    if form_character() != Fraction(-1):
        raise SystemExit("pinned form character is not -1")
    tangent = [bit(i) for i in FACTORS]
    eta = list(tangent)
    return tangent, eta


def failures(items, tangent_masks):
    """Return human-readable failures of the pinned assertions. Empty means holds."""
    bad = []
    counts = multiplicity_from_projector(items)
    if sum(counts.values()) != len(items):
        bad.append("projector ranks do not partition the basis")
    by_name = {name: mask for name, mask, _summand in items}
    if by_name.get("V1^V2") != bit(1) | bit(2):
        bad.append("V1^V2 is not the character {1,2}")
    if by_name.get("V3^V4") != bit(3) | bit(4):
        bad.append("V3^V4 is not the character {3,4}")
    for i in FACTORS:
        if by_name.get(f"eta{i}*V{i}") != 0:
            bad.append(f"diagonal eta{i}*V{i} is not invariant")
    trivial = counts[0]
    if trivial != 4:
        bad.append(f"trivial multiplicity is {trivial}, not 4")
    weight2 = [mask for mask in range(16) if popcount(mask) == 2]
    if len(weight2) != 6:
        bad.append("weight-2 character count is not 6")
    for mask in weight2:
        if counts[mask] != 4:
            bad.append(f"character {subset(mask)} has multiplicity {counts[mask]}, not 4")
    for mask in range(16):
        weight = popcount(mask)
        if weight not in (0, 2) and counts[mask] != 0:
            bad.append(f"character {subset(mask)} has multiplicity {counts[mask]}")
    full = bit(1) | bit(2) | bit(3) | bit(4)
    if counts[full] != 0:
        bad.append(f"full-sign projector rank is {counts[full]}, not 0")
    # The full-sign component of any equivariant map is the unique map
    # out of a source of this dimension. Dimension 0 is injective.
    source_dim = counts[full]
    columns = [tuple() for _ in range(source_dim)]
    # A zero map on a positive-dimensional source is the must-fail shape.
    if source_dim > 0:
        columns = [tuple(Fraction(0) for _ in range(1)) for _ in range(source_dim)]
    nullity = kernel_dimension(columns)
    if nullity != 0:
        bad.append(f"full-sign component has kernel dimension {nullity}")
    if tangent_masks[0] != bit(1):
        bad.append("tangent character of V1 is not {1}")
    return bad


def report(label, items, tangent_masks):
    bad = failures(items, tangent_masks)
    counts = multiplicity_from_projector(items)
    full = bit(1) | bit(2) | bit(3) | bit(4)
    print(f"{label}: basis={len(items)} full_sign_rank={counts[full]} failures={len(bad)}")
    for item in bad:
        print(f"  - {item}")
    return bad


def main():
    tangent, eta = pinned_signs()
    pinned = basis(tangent, eta)
    pinned_bad = report("pinned", pinned, tangent)
    if pinned_bad:
        raise SystemExit("pinned model failed its own assertions")

    # Control 1. Flip the tangent sign, the error dx/(-y) read as +dx/y.
    # The same checker must fail, because V1^V2 leaves {1,2}.
    flipped_tangent = [0 for _ in FACTORS]
    flipped = basis(flipped_tangent, eta)
    flip_bad = report("control_tangent_sign", flipped, flipped_tangent)
    if not flip_bad:
        raise SystemExit("tangent-sign control did not fail")

    # Control 2. One corrupt full-sign vector. The projector rank leaves 0,
    # and the zero map on that line is not injective.
    corrupt = basis(tangent, eta, extra=(("corrupt_full_sign", 15),))
    corrupt_bad = report("control_extra_full_sign", corrupt, tangent)
    if not any("full-sign projector rank" in item or "kernel dimension" in item for item in corrupt_bad):
        raise SystemExit("full-sign control did not fail")

    counts = multiplicity_from_projector(pinned)
    print("multiplicities:")
    for mask in range(16):
        if counts[mask]:
            print(f"  {subset(mask) or (0,)} weight={popcount(mask)} multiplicity={counts[mask]}")
    print("pinned_holds=1")
    print("controls_fired=2")


if __name__ == "__main__":
    main()
