"""Independent selector for the supplied L_minus all-81 scalar image.

The contraction is derived from the stated selector, not from another
implementation. Inputs are the 24 supplied quotient arrays. Arithmetic is
exact over Q.

Stated rules used here:

- Targets m run through {2,1,0}^4 in lexicographic order. The coordinate
  index is sum_i (2-m_i) 3^(3-i). The Laurent label is (-m_i-1).
- An orientation (i,j,k,l), a permutation of the four axes, is requested
  exactly when m_i = 2. The orientation sign is the sign of that permutation.
  The source-root scalar is already in the quotient and is not applied again.
- S = sum(m), d = 6+m_j, L = 22-m_l, w = 35+S.
- For 0 <= r <= d and 0 <= ell <= L, read quotient slot (r, w, ell),
  divide by the common denominator, and multiply by the coefficient of
  T^(d-r) z^(L-ell) in G(T,z)^(-70), where
  G = 1 + z + T + 3Tz + Tz^2 + T^2 z + T^2 z^2.
- A missing slot inside a supplied full quotient is zero. A missing quotient
  or a missing required orientation is an error.
- Role-ordered physical exponents are
  (272, 215-r, 157-S+r-ell, 47+ell), placed on axes (i,j,k,l).
- A coordinate whose requested-orientation set is empty has an empty
  selector boundary. Its value is the empty sum, 0. That conclusion is the
  empty sum itself; it is not inferred from a global source symmetry.
- Equal role-relative arrays related by the physical involution
  sigma = (0 2)(1 3) stay distinct bindings. Selector rows correspond after
  sigma acts on the target and on the physical exponent vector.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


PIN = "4fcc2e09aa80b77da5bc872acc1985e86bba417c"
T_MAX = 8
Z_MAX = 22
AXIS_COUNT = 4
SIGMA = (2, 3, 0, 1)
BINDING_FIELDS = (
    "configuration_sha256",
    "normalized_source_sha256",
    "compact_source_sha256",
    "checkpoint_sha256",
    "original_quotient_sha256",
    "completion_receipt_sha256",
)


def permutation_sign(roles):
    """Sign of a permutation given in one-line notation."""
    inversions = 0
    for left in range(len(roles)):
        for right in range(left + 1, len(roles)):
            if roles[left] > roles[right]:
                inversions += 1
    return 1 if inversions % 2 == 0 else -1


def monomials():
    """All 81 targets in the stated lexicographic order, with indices."""
    targets = []
    for digits in itertools.product((2, 1, 0), repeat=AXIS_COUNT):
        index = sum((2 - digits[i]) * 3 ** (3 - i) for i in range(AXIS_COUNT))
        targets.append((index, digits))
    if [index for index, _ in targets] != list(range(81)):
        raise RuntimeError("lexicographic index formula is not 0..80")
    return targets


def apply_sigma_tuple(values):
    """Push a 4-tuple forward along sigma: out[sigma(t)] = values[t]."""
    image = [None] * AXIS_COUNT
    for source, value in enumerate(values):
        image[SIGMA[source]] = value
    return tuple(image)


def permute_roles(roles):
    """Relabel axes by sigma. This is not the pushforward of the role tuple."""
    return tuple(SIGMA[axis] for axis in roles)


def binomial(n, k):
    if k < 0 or n < 0 or k > n:
        raise ValueError((n, k))
    k = min(k, n - k)
    value = 1
    for i in range(k):
        value = value * (n - i) // (i + 1)
    return value


def _trim(series):
    return {key: coeff for key, coeff in series.items() if coeff}


def _mul(left, right):
    product = {}
    for (a, b), ca in left.items():
        for (c, d), cb in right.items():
            na, nb = a + c, b + d
            if na <= T_MAX and nb <= Z_MAX:
                product[(na, nb)] = product.get((na, nb), 0) + ca * cb
    return _trim(product)


def _scale_add(base, extra, factor):
    total = dict(base)
    for key, coeff in extra.items():
        total[key] = total.get(key, 0) + factor * coeff
    return _trim(total)


def _pow(series, exponent):
    result = {(0, 0): 1}
    base = dict(series)
    power = exponent
    while power:
        if power & 1:
            result = _mul(result, base)
        power >>= 1
        if power:
            base = _mul(base, base)
    return result


def kernel_polynomial():
    """Integer coefficients of G, indexed by (T power, z power)."""
    return {
        (0, 0): 1,
        (0, 1): 1,
        (1, 0): 1,
        (1, 1): 3,
        (1, 2): 1,
        (2, 1): 1,
        (2, 2): 1,
    }


def kernel_weights_binomial():
    """Coefficients of G^(-70) modulo (T^9, z^23), via (1-U)^(-70)."""
    generator = kernel_polynomial()
    tail = {key: -coeff for key, coeff in generator.items() if key != (0, 0)}
    weights = {}
    power = {(0, 0): 1}
    for n in range(31):
        weights = _scale_add(weights, power, binomial(n + 69, n))
        power = _mul(power, tail)
    return weights


def kernel_weights_inverse_power():
    """Same window by truncating G^(-1) and raising it to the 70th power."""
    generator = kernel_polynomial()
    inverse = {}
    for t_power in range(T_MAX + 1):
        for z_power in range(Z_MAX + 1):
            carried = 0
            for (i, j), coeff in generator.items():
                if (i, j) == (0, 0):
                    continue
                if t_power >= i and z_power >= j:
                    carried += coeff * inverse.get((t_power - i, z_power - j), 0)
            target = 1 if (t_power, z_power) == (0, 0) else 0
            inverse[(t_power, z_power)] = target - carried
    inverse = _trim(inverse)
    return _pow(inverse, 70)


def certified_kernel_weights():
    """Return G^(-70) after the two expansions agree and G^70 H = 1."""
    binomial_weights = kernel_weights_binomial()
    inverse_power_weights = kernel_weights_inverse_power()
    if binomial_weights != inverse_power_weights:
        raise RuntimeError("kernel expansions disagree")
    product = _mul(_pow(kernel_polynomial(), 70), binomial_weights)
    if product != {(0, 0): 1}:
        raise RuntimeError("G^70 H is not 1 in the selector window")
    missing = [
        (t_power, z_power)
        for t_power in range(T_MAX + 1)
        for z_power in range(Z_MAX + 1)
        if (t_power, z_power) not in binomial_weights
    ]
    if missing:
        raise RuntimeError("kernel window has zero coefficients: %s" % (missing[:8],))
    return binomial_weights


def all_orientations():
    return tuple(itertools.permutations(range(AXIS_COUNT)))


def _parse_numerator(text, where):
    if isinstance(text, bool) or not isinstance(text, str) or not text.lstrip("-").isdigit():
        raise ValueError("non-integral numerator at %s" % (where,))
    return int(text)


@dataclass(frozen=True)
class Quotient:
    roles: tuple
    sign: int
    denominator: int
    coefficients: dict
    bindings: dict
    array_sha256: str
    homogeneous_degrees_separated: bool
    pairing_aggregated: bool

    def numerator(self, r, w, ell):
        return self.coefficients.get((r, w, ell), 0)

    def coefficient(self, r, w, ell):
        return Fraction(self.numerator(r, w, ell), self.denominator)


def load_quotients(package_dir):
    path = Path(package_dir) / "quotients.json"
    payload = json.loads(path.read_text())
    if payload.get("schema") != "Lminus-all81-quotients-v1":
        raise ValueError("unexpected quotient schema")
    if payload.get("field") != "Q":
        raise ValueError("unexpected scalar field")
    if payload.get("scalar_map") != "X02[0,5]-X13[10,1]":
        raise ValueError("unexpected scalar map")
    raw_rows = payload.get("quotients")
    if not isinstance(raw_rows, list) or len(raw_rows) != 24:
        raise ValueError("expected 24 quotient arrays")
    by_roles = {}
    for row in raw_rows:
        roles = tuple(row["roles"])
        if roles in by_roles or sorted(roles) != [0, 1, 2, 3] or len(roles) != 4:
            raise ValueError("bad or duplicate orientation %s" % (roles,))
        shape = tuple(row["shape"])
        if shape != (9, 44, 23):
            raise ValueError("unexpected shape for %s" % (roles,))
        if str(row["denominator"]) != "64":
            raise ValueError("unexpected denominator for %s" % (roles,))
        if row.get("homogeneous_degrees_separated") is not True:
            raise ValueError("homogeneous degrees are not separated for %s" % (roles,))
        if row.get("pairing_aggregated") is not False:
            raise ValueError("pairing aggregation is not false for %s" % (roles,))
        coefficients = {}
        for entry in row["coefficients"]:
            if len(entry) != 4:
                raise ValueError("bad coefficient row in %s" % (roles,))
            r, w, ell, numerator = entry
            key = (int(r), int(w), int(ell))
            if key in coefficients:
                raise ValueError("duplicate slot %s in %s" % (key, roles))
            if not (0 <= key[0] < 9 and 0 <= key[1] < 44 and 0 <= key[2] < 23):
                raise ValueError("slot %s outside shape in %s" % (key, roles))
            coefficients[key] = _parse_numerator(numerator, (roles, key))
        bindings = {field: row[field] for field in BINDING_FIELDS}
        by_roles[roles] = Quotient(
            roles=roles,
            sign=permutation_sign(roles),
            denominator=64,
            coefficients=coefficients,
            bindings=bindings,
            array_sha256=row["array_sha256"],
            homogeneous_degrees_separated=True,
            pairing_aggregated=False,
        )
    expected = set(all_orientations())
    if set(by_roles) != expected:
        raise ValueError("orientation set is not all 24 permutations")
    return by_roles


@dataclass(frozen=True)
class SelectorRow:
    target_index: int
    target: tuple
    roles: tuple
    sign: int
    r: int
    ell: int
    w: int
    numerator: int
    coefficient: Fraction
    weight: int
    weighted: Fraction
    signed: Fraction
    physical: tuple


@dataclass(frozen=True)
class OrientedRequest:
    target_index: int
    target: tuple
    roles: tuple
    sign: int
    d: int
    upper_l: int
    w: int
    degree_sum: int
    row_count: int
    signed_sum: Fraction


def iter_boundary(target, quotient, weights):
    """Yield the selector rows of one requested orientation, or nothing."""
    roles = quotient.roles
    leading = roles[0]
    if target[leading] != 2:
        return
    degree_sum = sum(target)
    reversed_axis = roles[1]
    reference_axis = roles[2]
    low_axis = roles[3]
    d = 6 + target[reversed_axis]
    upper_l = 22 - target[low_axis]
    w = 35 + degree_sum
    for r in range(d + 1):
        for ell in range(upper_l + 1):
            weight = weights[(d - r, upper_l - ell)]
            numerator = quotient.numerator(r, w, ell)
            coefficient = Fraction(numerator, quotient.denominator)
            weighted = coefficient * weight
            signed = quotient.sign * weighted
            role_exponents = (
                272,
                215 - r,
                157 - degree_sum + r - ell,
                47 + ell,
            )
            if sum(role_exponents) != 691 - degree_sum:
                raise RuntimeError("physical exponents do not sum to 691-S")
            physical = [None] * AXIS_COUNT
            physical[leading] = role_exponents[0]
            physical[reversed_axis] = role_exponents[1]
            physical[reference_axis] = role_exponents[2]
            physical[low_axis] = role_exponents[3]
            yield (
                degree_sum,
                d,
                upper_l,
                w,
                SelectorRow(
                    target_index=-1,
                    target=target,
                    roles=roles,
                    sign=quotient.sign,
                    r=r,
                    ell=ell,
                    w=w,
                    numerator=numerator,
                    coefficient=coefficient,
                    weight=weight,
                    weighted=weighted,
                    signed=signed,
                    physical=tuple(physical),
                ),
            )


def coordinate_value(target, quotients, weights):
    """Exact rational value of one coordinate. Empty boundary returns 0."""
    total = Fraction(0)
    requests = 0
    for roles in all_orientations():
        rows = list(iter_boundary(target, quotients[roles], weights))
        if not rows:
            continue
        requests += 1
        total += sum((row.signed for *_, row in rows), Fraction(0))
    return total, requests


def evaluate(quotients, weights=None):
    """Contract every coordinate and collect selector statistics."""
    if weights is None:
        weights = certified_kernel_weights()
    coordinates = []
    requests = []
    rows = []
    physical_coefficients = {}
    physical_conflicts = []
    physical_conflict_count = 0
    nonzero_physical = set()
    for index, target in monomials():
        total = Fraction(0)
        active = 0
        for roles in all_orientations():
            produced = list(iter_boundary(target, quotients[roles], weights))
            if not produced:
                continue
            active += 1
            signed_sum = Fraction(0)
            degree_sum = produced[0][0]
            d = produced[0][1]
            upper_l = produced[0][2]
            w = produced[0][3]
            for _, _, _, _, row in produced:
                row = SelectorRow(
                    target_index=index,
                    target=row.target,
                    roles=row.roles,
                    sign=row.sign,
                    r=row.r,
                    ell=row.ell,
                    w=row.w,
                    numerator=row.numerator,
                    coefficient=row.coefficient,
                    weight=row.weight,
                    weighted=row.weighted,
                    signed=row.signed,
                    physical=row.physical,
                )
                rows.append(row)
                signed_sum += row.signed
                previous = physical_coefficients.get(row.physical)
                if previous is None:
                    physical_coefficients[row.physical] = row.coefficient
                elif previous != row.coefficient:
                    physical_conflict_count += 1
                    if len(physical_conflicts) < 8:
                        physical_conflicts.append((row.physical, previous, row.coefficient))
                if row.numerator:
                    nonzero_physical.add(row.physical)
            total += signed_sum
            requests.append(
                OrientedRequest(
                    target_index=index,
                    target=target,
                    roles=roles,
                    sign=quotients[roles].sign,
                    d=d,
                    upper_l=upper_l,
                    w=w,
                    degree_sum=degree_sum,
                    row_count=len(produced),
                    signed_sum=signed_sum,
                )
            )
        empty_boundary = active == 0
        coordinates.append(
            {
                "index": index,
                "target": target,
                "laurent": tuple(-entry - 1 for entry in target),
                "value": total,
                "empty_boundary": empty_boundary,
                "request_count": active,
            }
        )
    return {
        "coordinates": coordinates,
        "requests": requests,
        "rows": rows,
        "physical_vectors": set(physical_coefficients),
        "physical_conflicts": physical_conflicts,
        "physical_conflict_count": physical_conflict_count,
        "nonzero_physical": nonzero_physical,
        "weights": weights,
    }


def boundary_partition(quotients, weights):
    """Classify coordinates by whether the selector boundary is empty.

    Emptiness is the absence of requested orientations under m_i = 2. It is
    counted from that boundary, not from a preassigned symmetry mask.
    """
    nonempty = []
    empty = []
    for index, target in monomials():
        requested = [
            roles
            for roles in all_orientations()
            if target[roles[0]] == 2
        ]
        rectangles = []
        for roles in requested:
            degree_sum = sum(target)
            d = 6 + target[roles[1]]
            upper_l = 22 - target[roles[3]]
            rectangles.append((d + 1) * (upper_l + 1))
            # Touch the weight table so a zero window cannot hide here.
            _ = weights[(d, upper_l)]
        if requested and sum(rectangles) > 0:
            nonempty.append(index)
        elif not requested and not rectangles:
            empty.append(index)
        else:
            raise RuntimeError("boundary classification is inconsistent at %s" % (index,))
    return nonempty, empty


def array_content_key(quotient):
    payload = tuple(sorted(
        (r, w, ell, numerator)
        for (r, w, ell), numerator in quotient.coefficients.items()
    ))
    return hashlib.sha256(repr(payload).encode("ascii")).hexdigest(), payload


def equal_array_pairs(quotients):
    """Pairs of orientations with identical role-relative coefficient arrays."""
    groups = defaultdict(list)
    for roles, quotient in quotients.items():
        digest, _ = array_content_key(quotient)
        groups[digest].append(roles)
    pairs = []
    for members in groups.values():
        members = sorted(members)
        if len(members) != 2:
            raise ValueError("expected equal arrays to occur in pairs, got %s" % (members,))
        left, right = members
        if permute_roles(left) == right:
            pairs.append((left, right))
        elif permute_roles(right) == left:
            pairs.append((right, left))
        else:
            raise ValueError("equal arrays are not a sigma pair: %s" % (members,))
    pairs.sort()
    return pairs


def documented_duplicate_pairs():
    """The six pairs named for the m=(2,2,2,0) eighteen."""
    named = (
        ((0, 1, 2, 3), (2, 3, 0, 1)),
        ((0, 1, 3, 2), (2, 3, 1, 0)),
        ((0, 2, 1, 3), (2, 0, 3, 1)),
        ((0, 2, 3, 1), (2, 0, 1, 3)),
        ((0, 3, 1, 2), (2, 1, 3, 0)),
        ((0, 3, 2, 1), (2, 1, 0, 3)),
    )
    return named


def bindings_distinct(left, right):
    return all(left.bindings[field] != right.bindings[field] for field in BINDING_FIELDS)


def covariance_failures(quotients, weights, pairs, targets=None):
    """Rows of A at m must match rows of sigma(A) at sigma(m).

    Compared data are the role-relative coefficient, the kernel weight, the
    weighted contribution, and the sigma-image of the physical exponent.
    Orientation signs are compared separately; sigma is even, so they agree.
    """
    if targets is None:
        targets = [target for _, target in monomials()]
    failures = []
    compared = 0
    for left_roles, right_roles in pairs:
        if permute_roles(left_roles) != right_roles:
            failures.append(("sigma-roles", left_roles, right_roles))
            continue
        if permutation_sign(left_roles) != permutation_sign(right_roles):
            failures.append(("sign", left_roles, right_roles))
        left = quotients[left_roles]
        right = quotients[right_roles]
        if not bindings_distinct(left, right):
            failures.append(("bindings", left_roles, right_roles))
        for target in targets:
            image = apply_sigma_tuple(target)
            left_rows = {
                (row.r, row.ell): row
                for *_, row in iter_boundary(target, left, weights)
            }
            right_rows = {
                (row.r, row.ell): row
                for *_, row in iter_boundary(image, right, weights)
            }
            if set(left_rows) != set(right_rows):
                failures.append(("window", target, left_roles, set(left_rows), set(right_rows)))
                continue
            for key, row in left_rows.items():
                other = right_rows[key]
                compared += 1
                if row.coefficient != other.coefficient:
                    failures.append(("coefficient", target, left_roles, key))
                if row.weight != other.weight or row.weighted != other.weighted:
                    failures.append(("weight", target, left_roles, key))
                if apply_sigma_tuple(row.physical) != other.physical:
                    failures.append(("physical", target, left_roles, key))
                if row.sign != other.sign or row.signed != other.signed:
                    failures.append(("signed", target, left_roles, key))
                if len(failures) > 12:
                    return failures, compared
    return failures, compared


def request_orientation_failures(requests):
    """Each request is an orientation with leading axis 2 and its permutation sign."""
    failures = []
    seen = set()
    for request in requests:
        key = (request.target, request.roles)
        if key in seen:
            failures.append(("duplicate", key))
        seen.add(key)
        if sorted(request.roles) != [0, 1, 2, 3]:
            failures.append(("not-permutation", request.roles))
        if request.target[request.roles[0]] != 2:
            failures.append(("inactive", key))
        if request.sign != permutation_sign(request.roles):
            failures.append(("sign", request.roles, request.sign))
        if request.row_count != (request.d + 1) * (request.upper_l + 1):
            failures.append(("rows", key))
        if request.w != 35 + request.degree_sum:
            failures.append(("weight-index", key))
    for _, target in monomials():
        for roles in all_orientations():
            active = target[roles[0]] == 2
            present = (target, roles) in seen
            if active != present:
                failures.append(("coverage", target, roles, active, present))
                if len(failures) > 12:
                    return failures
    return failures


def sensitivity(sign, weight, numerator_delta, denominator=64):
    """Exact change in a coordinate from one selected slot.

    The kernel weight is computed from G^(-70) alone. A zero weight would
    put the edit in the detector kernel; callers must pass a nonzero weight.
    """
    if weight == 0:
        raise ValueError("zero kernel weight is not a sensitivity control")
    return Fraction(sign * weight * numerator_delta, denominator)


def perturb_numerator(quotients, roles, slot, delta):
    """Return a new quotient map with one numerator changed by delta."""
    original = quotients[roles]
    updated = dict(original.coefficients)
    r, w, ell = slot
    updated[slot] = updated.get(slot, 0) + delta
    replacement = Quotient(
        roles=original.roles,
        sign=original.sign,
        denominator=original.denominator,
        coefficients=updated,
        bindings=original.bindings,
        array_sha256=original.array_sha256,
        homogeneous_degrees_separated=original.homogeneous_degrees_separated,
        pairing_aggregated=original.pairing_aggregated,
    )
    return {key: (replacement if key == roles else value) for key, value in quotients.items()}


def fraction_pair(value):
    return [str(value.numerator), str(value.denominator)]


def summary(audit):
    coordinates = audit["coordinates"]
    requests = audit["requests"]
    rows = audit["rows"]
    empty = [item["index"] for item in coordinates if item["empty_boundary"]]
    nonempty = [item["index"] for item in coordinates if not item["empty_boundary"]]
    nonzero_rows = [row for row in rows if row.numerator]
    nonzero_requests = [request for request in requests if request.signed_sum != 0]
    return {
        "coordinates": 81,
        "empty_boundary": len(empty),
        "nonempty_boundary": len(nonempty),
        "empty_indices": empty,
        "values": [fraction_pair(item["value"]) for item in coordinates],
        "oriented_requests": len(requests),
        "selected_rows": len(rows),
        "distinct_physical": len(audit["physical_vectors"]),
        "nonzero_rows": len(nonzero_rows),
        "distinct_nonzero_physical": len(audit["nonzero_physical"]),
        "nonzero_signed_requests": len(nonzero_requests),
        "physical_coefficient_conflicts": audit["physical_conflict_count"],
        "all_coordinates_zero": all(item["value"] == 0 for item in coordinates),
    }
