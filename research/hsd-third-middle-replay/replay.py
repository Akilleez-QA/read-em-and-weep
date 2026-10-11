#!/usr/bin/env python3
"""Independent exact replay of the 40 third-middle raw equations.

The cubic BCH right-hand sides are rebuilt from the literal first jet eta and
the literal second-middle primitives kappa, including the mixed lambda term
z^{-1} E0^2, before the proposed third cochain is read. Finite, infinity and
mixed raw equations are then checked modulo the line relation, together with
grading and regularity, over the rationals.

This file does not import the third-middle generator, the pinned contraction,
or the published checkers. The shared inputs are eta, kappa and the geometry
recorded below. Polynomial arithmetic, the BCH assembly, the relation
quotient, grading and the controls are local to this file.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import subprocess
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

Q = Fraction

SOURCE_COMMIT = "fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b"
CARRYING_COMMIT = "22b800836385cf4c869c200bfc6715e07613aad6"

ETA_SHA256 = "2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10"
KAPPA_SHA256 = "c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4"
COCHAIN_SHA256 = "011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd"
GZIP_SHA256 = "5033872e143d1e93d650698659a13853af0d7332c405b5454aacab96cfa7196c"

ETA_BYTES = 12297
KAPPA_BYTES = 152410
COCHAIN_BYTES = 23833465
GZIP_BYTES = 875342

REL_ETA = "research/carrier/plane-completion-lemma/third-middle-construction/first_jet.json"
REL_KAPPA = "research/carrier/plane-completion-lemma/third-middle-construction/certificate.json"
REL_GZIP = "research/carrier/plane-completion-lemma/third-order-distribution/THIRD_MIDDLE_COCHAINS.json.gz"
CARRY_ETA = "research/carrier/plane-completion-lemma/second-normal-comparison/first_jet.json"
CARRY_KAPPA = "research/carrier/plane-completion-lemma/second-normal-comparison/certificate.json"

NAMES = ("a", "b", "c", "d", "lambda")
W_KEYS = ("finite_W_primitive", "infinity_W_primitive", "mixed_W_primitive")
TOP = (0, 1, 2)
PAIRS = ((0, 1), (0, 2), (1, 2))
# Symmetric quadratic slots. Frame index 1 is the coordinate called E0:
# the input legend stores c as z^{-2} X E0^2 on slot (1, 1).
SLOTS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 0), (1, 1), (2, 2), (3, 3))
E0_SLOT = (1, 1)
PLANTED = (0, -1, -1, 1)  # X^{-1} Y^{-1} W

STATED_NONZERO = (
    "1", "a", "b", "c", "d",
    "a*a", "a*b", "a*c", "a*d", "b*b", "b*c", "b*d", "c*c", "c*d", "d*d",
    "a*a*a", "a*a*b", "a*a*c", "a*a*d", "a*b*b", "a*b*c", "a*b*d",
    "b*b*b", "b*b*c", "b*b*d",
    "lambda", "a*lambda", "b*lambda",
)
STATED_ZERO = (
    "a*c*c", "a*c*d", "a*d*d", "b*c*c", "b*c*d", "b*d*d",
    "c*c*c", "c*c*d", "c*d*d", "d*d*d", "c*lambda", "d*lambda",
)


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / REL_ETA).is_file():
            return candidate
    raise FileNotFoundError("repository root containing the pinned first jet was not found")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rat(value) -> Q:
    if isinstance(value, float) or isinstance(value, bool):
        raise ValueError("non-rational coefficient")
    if isinstance(value, str) and any(mark in value for mark in ".eE"):
        raise ValueError("non-rational coefficient literal")
    return Q(value)


def label_of(exponent) -> str:
    parts = [name for name, power in zip(NAMES, exponent) for _ in range(power)]
    return "*".join(parts) if parts else "1"


def exponent_of_label(label: str):
    exponent = [0, 0, 0, 0, 0]
    if label != "1":
        for factor in label.split("*"):
            exponent[NAMES.index(factor)] += 1
    return tuple(exponent)


def all_exponents():
    found = []
    for total in range(4):
        for seq in combinations_with_replacement(range(4), total):
            exponent = [0, 0, 0, 0, 0]
            for index in seq:
                exponent[index] += 1
            found.append(tuple(exponent))
    found.append((0, 0, 0, 0, 1))
    for index in range(4):
        exponent = [0, 0, 0, 0, 1]
        exponent[index] = 1
        found.append(tuple(exponent))
    if len(found) != 40 or len(set(found)) != 40:
        raise RuntimeError("the cubic parameter list is not the 40 monomials")
    return tuple(found)


ALL_EXPONENTS = all_exponents()
ALL_LABELS = tuple(label_of(exponent) for exponent in ALL_EXPONENTS)


def _check_stated_support_partition():
    nonzero = set(STATED_NONZERO)
    zero = set(STATED_ZERO)
    if len(nonzero) != 28 or len(zero) != 12 or nonzero & zero:
        raise RuntimeError("stated support lists do not form a 28/12 partition")
    if nonzero | zero != set(ALL_LABELS):
        raise RuntimeError("stated support lists do not cover the 40 monomials")


_check_stated_support_partition()


# --- Laurent polynomials in (z, X, Y, W) with rational coefficients ---

def mono(z=0, X=0, Y=0, W=0, c=1):
    if c == 0:
        return {}
    return {(z, X, Y, W): Q(c)}


def add_poly(*polys):
    out = {}
    for poly in polys:
        for exponent, coeff in poly.items():
            total = out.get(exponent, Q(0)) + coeff
            if total:
                out[exponent] = total
            else:
                out.pop(exponent, None)
    return out


def scale_poly(poly, coeff):
    if not poly or coeff == 0:
        return {}
    if coeff == 1:
        return dict(poly)
    return {exponent: value * coeff for exponent, value in poly.items()}


def neg_poly(poly):
    return scale_poly(poly, -1)


def mul_poly(left, right):
    if not left or not right:
        return {}
    out = {}
    for e_left, a_left in left.items():
        for e_right, a_right in right.items():
            key = (
                e_left[0] + e_right[0],
                e_left[1] + e_right[1],
                e_left[2] + e_right[2],
                e_left[3] + e_right[3],
            )
            total = out.get(key, Q(0)) + a_left * a_right
            if total:
                out[key] = total
            else:
                out.pop(key, None)
    return out


def shift_poly(poly, z=0, X=0, Y=0, W=0):
    if not poly or (z, X, Y, W) == (0, 0, 0, 0):
        return dict(poly)
    return {
        (exponent[0] + z, exponent[1] + X, exponent[2] + Y, exponent[3] + W): coeff
        for exponent, coeff in poly.items()
    }


def power_poly(poly, power):
    out = mono()
    for _ in range(power):
        out = mul_poly(out, poly)
    return out


# Geometry of the fixed completed plane. These formulas are the shared
# geometric input. They are written here and are not imported.
Z = mono(z=1)
X = mono(X=1)
Y = mono(Y=1)
W = mono(W=1)
S = add_poly(power_poly(X, 2), power_poly(Y, 2))
F = mul_poly(X, Y)
A = add_poly(power_poly(X, 3), power_poly(Y, 3))
G = add_poly(S, neg_poly(mul_poly(Z, power_poly(W, 2))))
C = add_poly(
    power_poly(S, 2),
    mul_poly(Z, mul_poly(S, power_poly(W, 2))),
    mul_poly(power_poly(Z, 2), power_poly(W, 4)),
)
W6 = power_poly(W, 6)
S3 = power_poly(S, 3)
# alpha = -A f0 + W^6 f1 - g f2 + XY f3 on the finite chart.
# On the infinity chart the f1 coefficient is S^3 and the f2 coefficient is -g/z.
RF = (neg_poly(A), W6, neg_poly(G), F)
RI = (neg_poly(A), S3, shift_poly(neg_poly(G), z=-1), F)

# B = (z^3 f0, f1, z C f1 + z^4 f2, z^3 f3). W-transport substitutes B and
# multiplies by z^{-4}. The f2 column carries both an f1 and an f2 term.
B_COLUMNS = (
    {0: mono(z=3)},
    {1: mono()},
    {1: shift_poly(C, z=1), 2: mono(z=4)},
    {3: mono(z=3)},
)


def _omega_table(pairs):
    table = [[None] * 4 for _ in range(4)]
    for (i, j), poly in pairs.items():
        table[i][j] = poly
        table[j][i] = neg_poly(poly)
    return tuple(tuple(row) for row in table)


# Tensor Poisson bivector on frame indices 1, 2, 3. Index 0 is absent.
OMEGA = (
    _omega_table({(1, 2): F, (1, 3): G, (2, 3): W6}),
    _omega_table({(1, 2): F, (1, 3): shift_poly(G, z=-1), (2, 3): S3}),
)


def add_quad(left, right):
    if not left:
        return {slot: dict(poly) for slot, poly in right.items()}
    if not right:
        return {slot: dict(poly) for slot, poly in left.items()}
    out = {slot: dict(poly) for slot, poly in left.items()}
    for slot, poly in right.items():
        total = add_poly(out.get(slot, {}), poly)
        if total:
            out[slot] = total
        else:
            out.pop(slot, None)
    return out


def scale_quad(quad, coeff):
    if not quad or coeff == 0:
        return {}
    out = {}
    for slot, poly in quad.items():
        scaled = scale_poly(poly, coeff)
        if scaled:
            out[slot] = scaled
    return out


def bracket_quad(left, right, chart):
    """Poisson bracket of two symmetric quadratic Hamiltonians.

    A slot (i, j), i < j, stores the coefficient of f_i f_j. A diagonal slot
    (i, i) stores the coefficient of f_i^2. Differentiating and contracting
    with the bivector produces four contributions. The two identical summands
    on a diagonal reproduce the factor 2 from d(f_i^2)/df_i.
    """
    if not left or not right:
        return {}
    table = OMEGA[chart]
    out = {}
    for (i, j), a_poly in left.items():
        for (k, l), b_poly in right.items():
            product = mul_poly(a_poly, b_poly)
            if not product:
                continue
            for u, v, x, y in ((i, k, j, l), (i, l, j, k), (j, k, i, l), (j, l, i, k)):
                weight = table[x][y]
                if not weight:
                    continue
                term = mul_poly(product, weight)
                if not term:
                    continue
                slot = (u, v) if u <= v else (v, u)
                out[slot] = add_poly(out.get(slot, {}), term)
    return {slot: poly for slot, poly in out.items() if poly}


def transport_quad(quad):
    """Substitute the gluing frame B and multiply by z^{-4}."""
    if not quad:
        return {}
    out = {}
    for (i, j), poly in quad.items():
        for k, left_factor in B_COLUMNS[i].items():
            for l, right_factor in B_COLUMNS[j].items():
                term = shift_poly(mul_poly(poly, mul_poly(left_factor, right_factor)), z=-4)
                if not term:
                    continue
                slot = (k, l) if k <= l else (l, k)
                out[slot] = add_poly(out.get(slot, {}), term)
    return {slot: poly for slot, poly in out.items() if poly}


def quotient_remainder(quad, relation):
    """Remainder of a quadratic tensor modulo the line relation.

    The linear cofactor is fixed by the frame-3 row, whose relation
    coefficient is XY. Slots that meet frame 3 determine that cofactor.
    Every slot, including those, is then compared with relation times the
    cofactor. The returned slot polynomials are the unexplained part.
    An empty result means the tensor lies in the relation module.
    """
    if relation[3] != F:
        raise RuntimeError("relation pivot is not XY")
    cofactor = [None] * 4
    cofactor[3] = shift_poly(quad.get((3, 3), {}), X=-1, Y=-1)
    for index in range(3):
        cross = quad.get((index, 3), {})
        residual = add_poly(cross, neg_poly(mul_poly(relation[index], cofactor[3])))
        cofactor[index] = shift_poly(residual, X=-1, Y=-1)
    remainder = {}
    for i, j in SLOTS:
        if i == j:
            expected = mul_poly(relation[i], cofactor[i])
        else:
            expected = add_poly(mul_poly(relation[i], cofactor[j]), mul_poly(relation[j], cofactor[i]))
        diff = add_poly(quad.get((i, j), {}), neg_poly(expected))
        if diff:
            remainder[(i, j)] = diff
    return remainder


def scale_remainder(remainder, coeff):
    out = {}
    for slot, poly in remainder.items():
        scaled = scale_poly(poly, coeff)
        if scaled:
            out[slot] = scaled
    return out


def delta_triple(cochain):
    """Čech coboundary on the triple overlap (0, 1, 2): c12 - c02 + c01."""
    return add_quad(
        cochain.get((1, 2), {}),
        add_quad(scale_quad(cochain.get((0, 2), {}), -1), cochain.get((0, 1), {})),
    )


def delta_edge(cochain, i, j):
    """Čech coboundary of a vertex cochain on the edge (i, j): c_j - c_i."""
    return add_quad(cochain.get((j,), {}), scale_quad(cochain.get((i,), {}), -1))


def add_family(*families):
    out = {}
    for family in families:
        for exponent, quad in family.items():
            total = add_quad(out.get(exponent, {}), quad)
            if total:
                out[exponent] = total
            else:
                out.pop(exponent, None)
    return out


def scale_family(family, coeff):
    if coeff == 0:
        return {}
    out = {}
    for exponent, quad in family.items():
        scaled = scale_quad(quad, coeff)
        if scaled:
            out[exponent] = scaled
    return out


def bracket_families(left, right, chart):
    out = {}
    for e_left, quad_left in left.items():
        for e_right, quad_right in right.items():
            bracket = bracket_quad(quad_left, quad_right, chart)
            if not bracket:
                continue
            key = tuple(a + b for a, b in zip(e_left, e_right))
            out[key] = add_quad(out.get(key, {}), bracket)
    return {exponent: quad for exponent, quad in out.items() if quad}


def nested_family(left, right, chart):
    """N(left, right) = [left, [left, right]] + [right, [right, left]]."""
    left_right = bracket_families(left, right, chart)
    right_left = bracket_families(right, left, chart)
    return add_family(
        bracket_families(left, left_right, chart),
        bracket_families(right, right_left, chart),
    )


def extract(family, chart, opened, transport=False):
    out = {}
    for exponent, charts in family.items():
        quad = charts[chart].get(opened, {})
        if transport and quad:
            quad = transport_quad(quad)
        if quad:
            out[exponent] = quad
    return out


def plane_rhs(half, nested):
    """(1/2) bracket sum minus (1/12) N, on one plane chart."""
    return add_family(half, scale_family(nested, Q(-1, 12)))


def mixed_rhs(half, nested):
    """(1/2) mixed bracket sum plus (1/12)(N(hj, F) - N(I, hi))."""
    return add_family(half, scale_family(nested, Q(1, 12)))


class CubicPieces:
    def __init__(self, finite_half, finite_nested, infinity_half, infinity_nested, mixed_half, mixed_nested):
        self.finite_half = finite_half
        self.finite_nested = finite_nested
        self.infinity_half = infinity_half
        self.infinity_nested = infinity_nested
        self.mixed_half = mixed_half
        self.mixed_nested = mixed_nested

    def finite(self):
        return plane_rhs(self.finite_half, self.finite_nested)

    def infinity(self):
        return plane_rhs(self.infinity_half, self.infinity_nested)

    def mixed(self, pair):
        return mixed_rhs(self.mixed_half[pair], self.mixed_nested[pair])


def build_cubic_rhs(eta, kappa) -> CubicPieces:
    """Rebuild every cubic right-hand side. Does not read the third cochain."""
    finite_half = []
    finite_nested = []
    infinity_half = []
    infinity_nested = []
    for chart, half_bucket, nested_bucket in (
        (0, finite_half, finite_nested),
        (1, infinity_half, infinity_nested),
    ):
        x = extract(eta, chart, (0, 1))
        y = extract(eta, chart, (1, 2))
        u = extract(kappa, chart, (0, 1))
        v = extract(kappa, chart, (1, 2))
        half_bucket.append(
            scale_family(
                add_family(bracket_families(x, v, chart), bracket_families(u, y, chart)),
                Q(1, 2),
            )
        )
        nested_bucket.append(nested_family(x, y, chart))
    mixed_half = {}
    mixed_nested = {}
    for i, j in PAIRS:
        hi = extract(eta, 2, (i,))
        hj = extract(eta, 2, (j,))
        finite_edge = extract(eta, 0, (i, j))
        infinity_edge = extract(eta, 1, (i, j), transport=True)
        ki = extract(kappa, 2, (i,))
        kj = extract(kappa, 2, (j,))
        kappa_finite = extract(kappa, 0, (i, j))
        kappa_infinity = extract(kappa, 1, (i, j), transport=True)
        mixed_half[(i, j)] = scale_family(
            add_family(
                bracket_families(hi, kappa_infinity, 0),
                bracket_families(ki, infinity_edge, 0),
                scale_family(bracket_families(finite_edge, kj, 0), -1),
                scale_family(bracket_families(kappa_finite, hj, 0), -1),
            ),
            Q(1, 2),
        )
        mixed_nested[(i, j)] = add_family(
            nested_family(hj, finite_edge, 0),
            scale_family(nested_family(infinity_edge, hi, 0), -1),
        )
    return CubicPieces(
        finite_half[0],
        finite_nested[0],
        infinity_half[0],
        infinity_nested[0],
        mixed_half,
        mixed_nested,
    )


def monomial_count(family) -> int:
    return sum(len(poly) for quad in family.values() for poly in quad.values())


def load_jet_chart(records):
    out = {}
    for record in records:
        quad = {}
        for ij, exponent, coeff in record["terms"]:
            slot = tuple(ij)
            if len(slot) != 2 or tuple(sorted(slot)) != slot:
                raise ValueError("first-jet slot is not a sorted quadratic pair")
            if len(exponent) != 4:
                raise ValueError("first-jet exponent is not a geometric 4-tuple")
            value = rat(coeff)
            if not value:
                continue
            poly = quad.setdefault(slot, {})
            key = tuple(exponent)
            total = poly.get(key, Q(0)) + value
            if total:
                poly[key] = total
            else:
                poly.pop(key, None)
        quad = {slot: poly for slot, poly in quad.items() if poly}
        if quad:
            out[tuple(record["open"])] = quad
    return out


def slot_of_tail(tail):
    slot = tuple(index for index, power in enumerate(tail) for _ in range(power))
    if len(slot) != 2 or tuple(sorted(slot)) != slot:
        raise ValueError("cover term is not a sorted quadratic frame monomial")
    return slot


def load_cover(records):
    out = {}
    for record in records:
        quad = {}
        for exponent, coeff in record["terms"]:
            if len(exponent) != 8:
                raise ValueError("cover exponent is not an 8-tuple")
            value = rat(coeff)
            if not value:
                continue
            slot = slot_of_tail(exponent[4:])
            poly = quad.setdefault(slot, {})
            key = tuple(exponent[:4])
            total = poly.get(key, Q(0)) + value
            if total:
                poly[key] = total
            else:
                poly.pop(key, None)
        quad = {slot: poly for slot, poly in quad.items() if poly}
        if quad:
            out[tuple(record["open"])] = quad
    return out


def load_eta(document):
    legend = ["a=nu_X", "b=nu_Y", "c=z^-2 X E0^2", "d=z^-2 Y E0^2"]
    if document.get("coordinate_order") != legend:
        raise ValueError("first-jet coordinate legend does not match the pinned E0 naming")
    directions = document["directions"]
    if [item["name"] for item in directions] != ["a", "b", "c", "d"]:
        raise ValueError("first-jet direction order changed")
    family = {}
    objects = [document["origin"], *directions]
    for name, obj in zip(("1", "a", "b", "c", "d"), objects):
        family[exponent_of_label(name)] = tuple(load_jet_chart(obj[key]) for key in ("finite", "infinity", "mixed"))
    c_mixed = family[(0, 0, 1, 0, 0)][2]
    d_mixed = family[(0, 0, 0, 1, 0)][2]
    c_expected = {E0_SLOT: mono(z=-2, X=1)}
    d_expected = {E0_SLOT: mono(z=-2, Y=1)}
    for vertex in range(3):
        if c_mixed.get((vertex,)) != c_expected:
            raise ValueError("direction c is not z^{-2} X E0^2 on slot (1, 1)")
        if d_mixed.get((vertex,)) != d_expected:
            raise ValueError("direction d is not z^{-2} Y E0^2 on slot (1, 1)")
    return family


def lambda_kappa_tensor():
    """Mixed closed tensor z^{-1} E0^2, with empty finite and infinity parts."""
    vertex = {E0_SLOT: mono(z=-1)}
    return {}, {}, { (i,): {E0_SLOT: dict(vertex[E0_SLOT])} for i in range(3) }


def load_kappa(document):
    family = {}
    for name, record in document["coefficients"].items():
        exponent = exponent_of_label(name)
        if exponent[4] != 0 or sum(exponent) > 2:
            raise ValueError("kappa coefficient is outside the quadratic parameter span")
        primitive = record["original_cover_primitive"]
        family[exponent] = tuple(load_cover(primitive[key]) for key in W_KEYS)
    if len(family) != 15:
        raise ValueError("kappa does not have the 15 quadratic coefficients")
    if (0, 0, 0, 0, 1) in family:
        raise ValueError("lambda is already inside the quadratic kappa blocks")
    family[(0, 0, 0, 0, 1)] = lambda_kappa_tensor()
    return family


def git_bytes(root: Path, commit: str, relative: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{relative}"], cwd=root)


def verify_eta_kappa(root: Path):
    eta_bytes = (root / REL_ETA).read_bytes()
    kappa_bytes = (root / REL_KAPPA).read_bytes()
    eta_hash = sha256(eta_bytes)
    kappa_hash = sha256(kappa_bytes)
    if eta_hash != ETA_SHA256 or len(eta_bytes) != ETA_BYTES:
        raise ValueError("first jet hash or size mismatch")
    if kappa_hash != KAPPA_SHA256 or len(kappa_bytes) != KAPPA_BYTES:
        raise ValueError("kappa certificate hash or size mismatch")
    if sha256(git_bytes(root, SOURCE_COMMIT, REL_ETA)) != ETA_SHA256:
        raise ValueError("working first jet differs from the source commit")
    if sha256(git_bytes(root, SOURCE_COMMIT, REL_KAPPA)) != KAPPA_SHA256:
        raise ValueError("working kappa certificate differs from the source commit")
    carry_eta = sha256(git_bytes(root, CARRYING_COMMIT, CARRY_ETA)) == ETA_SHA256
    carry_kappa = sha256(git_bytes(root, CARRYING_COMMIT, CARRY_KAPPA)) == KAPPA_SHA256
    if not carry_eta or not carry_kappa:
        raise ValueError("carrying commit does not contain these eta and kappa bytes")
    return {
        "eta": {"path": REL_ETA, "sha256": eta_hash, "bytes": len(eta_bytes)},
        "kappa": {
            "path": REL_KAPPA,
            "sha256": kappa_hash,
            "bytes": len(kappa_bytes),
            "carried_at": CARRYING_COMMIT,
            "carried_path": CARRY_KAPPA,
            "carried_bytes_match": True,
        },
        "eta_carried_at_same_commit": True,
    }


def read_cochain_bytes(root: Path) -> bytes:
    """Read and pin the third cochain. Call only after the right-hand sides exist."""
    compressed = (root / REL_GZIP).read_bytes()
    if sha256(compressed) != GZIP_SHA256 or len(compressed) != GZIP_BYTES:
        raise ValueError("compressed third-cochain hash or size mismatch")
    raw = gzip.decompress(compressed)
    if sha256(raw) != COCHAIN_SHA256 or len(raw) != COCHAIN_BYTES:
        raise ValueError("third-cochain hash or size mismatch")
    if sha256(git_bytes(root, SOURCE_COMMIT, REL_GZIP)) != GZIP_SHA256:
        raise ValueError("working compressed cochain differs from the source commit")
    return raw


def remainder_records(remainder):
    rows = []
    for slot in sorted(remainder):
        for exponent in sorted(remainder[slot]):
            rows.append({
                "slot": list(slot),
                "frame": "E0^2" if slot == E0_SLOT else f"f{slot[0]}*f{slot[1]}",
                "exponent_zXYW": list(exponent),
                "coefficient": str(remainder[slot][exponent]),
            })
    return rows


def identify_visible_bch_sign(pieces: CubicPieces):
    """Find a BCH summand with nonzero relation remainder, conventions fixed.

    The summand is taken from the rebuilt right-hand side. Eta and kappa are
    not flipped. The third cochain is not an argument of this function.
    """
    trials = (
        {
            "name": "finite nested contribution with published coefficient -1/12",
            "chart": "finite",
            "piece": "nested",
            "published_coefficient": "-1/12",
            "family": scale_family(pieces.finite_nested, Q(-1, 12)),
            "relation": RF,
            "replacement": "replace the finite coefficient -1/12 of N by +1/12",
        },
        {
            "name": "infinity nested contribution with published coefficient -1/12",
            "chart": "infinity",
            "piece": "nested",
            "published_coefficient": "-1/12",
            "family": scale_family(pieces.infinity_nested, Q(-1, 12)),
            "relation": RI,
            "replacement": "replace the infinity coefficient -1/12 of N by +1/12",
        },
        {
            "name": "finite bracket contribution with published coefficient +1/2",
            "chart": "finite",
            "piece": "half",
            "published_coefficient": "1/2",
            "family": pieces.finite_half,
            "relation": RF,
            "replacement": "replace the finite bracket sum by its negative",
        },
    )
    for trial in trials:
        hits = []
        for exponent in ALL_EXPONENTS:
            remainder = quotient_remainder(trial["family"].get(exponent, {}), trial["relation"])
            if remainder:
                hits.append((exponent, remainder))
        if not hits:
            continue
        exponent, remainder = min(hits, key=lambda item: label_of(item[0]))
        return {
            "name": trial["name"],
            "chart": trial["chart"],
            "piece": trial["piece"],
            "published_coefficient": trial["published_coefficient"],
            "replacement": trial["replacement"],
            "parameter": label_of(exponent),
            "exponent": exponent,
            "remainder": remainder,
            "relation": trial["relation"],
            "nonzero_parameters_for_this_summand": len(hits),
        }
    raise RuntimeError("no BCH summand has a nonzero relation remainder; the sign control would be blind")


def component_passes(remainder) -> str:
    return "pass" if not remainder else "fail"


def grade_cochain(cochain, chart):
    """Plane degree, secondary character, plane poles and base regularity."""
    weights = (3, 6, 0, 2) if chart == 1 else (3, 0, 2, 2)
    offset = -5 if chart == 1 else -1
    plane_weights = (-3, 0, -4, -4)
    errors = []
    terms = 0
    for opened, quad in cochain.items():
        for (i, j), poly in quad.items():
            for exponent in poly:
                terms += 1
                z_power, x_power, y_power, w_power = exponent
                if x_power + y_power + w_power != plane_weights[i] + plane_weights[j] - 1:
                    errors.append(("plane degree", list(opened), [i, j], list(exponent)))
                if 2 * z_power + x_power + y_power != weights[i] + weights[j] + offset:
                    errors.append(("character", list(opened), [i, j], list(exponent)))
                for plane in range(3):
                    if plane not in opened and exponent[plane + 1] < 0:
                        errors.append(("plane pole", list(opened), [i, j], list(exponent)))
                        break
                if chart == 0 and z_power < 0:
                    errors.append(("base pole", list(opened), [i, j], list(exponent)))
                elif chart == 1 and z_power > 0:
                    errors.append(("base pole", list(opened), [i, j], list(exponent)))
    return terms, errors


def canon_terms(terms):
    rows = []
    for exponent, coeff in terms:
        value = rat(coeff)
        if value:
            rows.append((tuple(exponent), value))
    rows.sort()
    return tuple(rows)


def canon_primitive(primitive):
    canon = {}
    for key, value in primitive.items():
        if value and isinstance(value[0], dict):
            blocks = []
            for block in value:
                blocks.append((tuple(block["open"]), canon_terms(block["terms"])))
            blocks.sort()
            canon[key] = tuple(blocks)
        else:
            canon[key] = canon_terms(value)
    return canon


def w_is_nonzero(record) -> bool:
    primitive = record["original_cover_primitive"]
    for key in W_KEYS:
        for block in primitive[key]:
            for _exponent, coeff in block["terms"]:
                if rat(coeff):
                    return True
    return False


def check_equations(pieces: CubicPieces, cochain):
    if set(cochain) != set(ALL_LABELS):
        raise ValueError("third cochain label set is not the 40 monomials")
    finite_rhs = pieces.finite()
    infinity_rhs = pieces.infinity()
    mixed_rhs_families = {pair: pieces.mixed(pair) for pair in PAIRS}
    rows = []
    graded_terms = 0
    for exponent in ALL_EXPONENTS:
        label = label_of(exponent)
        record = cochain[label]
        if tuple(record["parameter_exponents"]) != exponent:
            raise ValueError("parameter exponent does not match its label")
        finite, infinity, mixed = (load_cover(record["original_cover_primitive"][key]) for key in W_KEYS)
        finite_remainder = quotient_remainder(
            add_quad(delta_triple(finite), scale_quad(finite_rhs.get(exponent, {}), -1)),
            RF,
        )
        infinity_remainder = quotient_remainder(
            add_quad(delta_triple(infinity), scale_quad(infinity_rhs.get(exponent, {}), -1)),
            RI,
        )
        mixed_results = {}
        mixed_remainders = {}
        for pair in PAIRS:
            defect = add_quad(
                transport_quad(infinity.get(pair, {})),
                scale_quad(finite.get(pair, {}), -1),
            )
            defect = add_quad(defect, scale_quad(delta_edge(mixed, pair[0], pair[1]), -1))
            defect = add_quad(defect, scale_quad(mixed_rhs_families[pair].get(exponent, {}), -1))
            mixed_remainders[pair] = quotient_remainder(defect, RF)
            mixed_results[f"{pair[0]}{pair[1]}"] = component_passes(mixed_remainders[pair])
        grade_errors = []
        for chart, chain in enumerate((finite, infinity, mixed)):
            count, errors = grade_cochain(chain, chart)
            graded_terms += count
            grade_errors.extend(errors)
        components = {
            "finite": component_passes(finite_remainder),
            "infinity": component_passes(infinity_remainder),
            "mixed_01": mixed_results["01"],
            "mixed_02": mixed_results["02"],
            "mixed_12": mixed_results["12"],
            "grading_regularity": "pass" if not grade_errors else "fail",
        }
        result = "pass" if all(value == "pass" for value in components.values()) else "fail"
        row = {"parameter": label, "exponents": list(exponent), **components, "result": result}
        if result != "pass":
            row["finite_remainder_terms"] = len(remainder_records(finite_remainder))
            row["infinity_remainder_terms"] = len(remainder_records(infinity_remainder))
            row["grading_error_count"] = len(grade_errors)
        rows.append(row)
    return rows, graded_terms


def lambda_slice(certificate, cochain):
    rows = []
    for label, key in (("lambda", "1"), ("a*lambda", "a"), ("b*lambda", "b"), ("c*lambda", "c"), ("d*lambda", "d")):
        supplied = certificate["lambda_order_three"]["coefficients"][key]["original_cover_primitive"]
        exported = cochain[label]["original_cover_primitive"]
        rows.append({
            "parameter": label,
            "supplied_key": key,
            "result": "pass" if canon_primitive(supplied) == canon_primitive(exported) else "fail",
        })
    return rows


def support_check(cochain):
    nonzero = sorted(label for label, record in cochain.items() if w_is_nonzero(record))
    zero = sorted(label for label, record in cochain.items() if label not in set(nonzero))
    return {
        "nonzero_count": len(nonzero),
        "zero_count": len(zero),
        "nonzero": nonzero,
        "zero": zero,
        "matches_stated_nonzero": nonzero == sorted(STATED_NONZERO),
        "matches_stated_zero": zero == sorted(STATED_ZERO),
        "result": "pass" if nonzero == sorted(STATED_NONZERO) and zero == sorted(STATED_ZERO) else "fail",
    }


def known_sensitive_control(pieces: CubicPieces, cochain):
    """Add X^{-1} Y^{-1} W E0^2 to the origin finite01 primitive."""
    finite = load_cover(cochain["1"]["original_cover_primitive"]["finite_W_primitive"])
    origin = (0, 0, 0, 0, 0)
    unmutated = quotient_remainder(
        add_quad(delta_triple(finite), scale_quad(pieces.finite().get(origin, {}), -1)),
        RF,
    )
    mutated = {opened: {slot: dict(poly) for slot, poly in quad.items()} for opened, quad in finite.items()}
    edge = {slot: dict(poly) for slot, poly in mutated.get((0, 1), {}).items()}
    edge[E0_SLOT] = add_poly(edge.get(E0_SLOT, {}), mono(X=-1, Y=-1, W=1))
    mutated[(0, 1)] = edge
    remainder = quotient_remainder(
        add_quad(delta_triple(mutated), scale_quad(pieces.finite().get(origin, {}), -1)),
        RF,
    )
    expected = {E0_SLOT: mono(X=-1, Y=-1, W=1)}
    exact = remainder == expected and unmutated == {}
    return {
        "parameter": "1",
        "chart": "finite",
        "overlap": [0, 1, 2],
        "planted_edge": [0, 1],
        "planted_slot": list(E0_SLOT),
        "planted_monomial": "X^-1 Y^-1 W E0^2",
        "unmutated_equation": "pass" if unmutated == {} else "fail",
        "quotient_remainder": remainder_records(remainder),
        "remainder_equals_planted_monomial": exact,
        "result": "pass" if exact else "fail",
    }


def wrong_sign_control(pieces: CubicPieces, identified, cochain, equation_rows):
    exponent = identified["exponent"]
    label = identified["parameter"]
    published_row = next(row for row in equation_rows if row["parameter"] == label)
    chart_name = identified["chart"]
    chart = 0 if chart_name == "finite" else 1
    relation = RF if chart == 0 else RI
    key = "finite_W_primitive" if chart == 0 else "infinity_W_primitive"
    nu = load_cover(cochain[label]["original_cover_primitive"][key])
    if chart == 0:
        half = pieces.finite_half
        nested = pieces.finite_nested
    else:
        half = pieces.infinity_half
        nested = pieces.infinity_nested
    if identified["piece"] == "nested":
        wrong = add_quad(half.get(exponent, {}), scale_quad(nested.get(exponent, {}), Q(1, 12)))
    elif identified["piece"] == "half":
        wrong = add_quad(scale_quad(half.get(exponent, {}), -1), scale_quad(nested.get(exponent, {}), Q(-1, 12)))
    else:
        raise RuntimeError("unknown BCH piece")
    failure = quotient_remainder(add_quad(delta_triple(nu), scale_quad(wrong, -1)), relation)
    predicted = scale_remainder(identified["remainder"], 2)
    failed = failure == predicted and predicted != {} and published_row[chart_name] == "pass"
    return {
        "identified_before_cochain_was_read": True,
        "summand": identified["name"],
        "parameter": label,
        "chart": chart_name,
        "overlap": [0, 1, 2],
        "replacement": identified["replacement"],
        "published_equation": published_row[chart_name],
        "identified_remainder_term_count": len(remainder_records(identified["remainder"])),
        "identified_remainder_nonzero": identified["remainder"] != {},
        "nonzero_parameters_for_this_summand": identified["nonzero_parameters_for_this_summand"],
        "identified_remainder": remainder_records(identified["remainder"]),
        "wrong_sign_remainder_equals_twice_identified": failure == predicted,
        "wrong_sign_equation": "fail" if failure else "pass",
        "blanket_input_flip_used": False,
        "result": "pass" if failed else "fail",
    }


def run(write_path: Path | None = None):
    root = repo_root()
    pins = verify_eta_kappa(root)
    eta = load_eta(json.loads((root / REL_ETA).read_text()))
    certificate = json.loads((root / REL_KAPPA).read_text())
    kappa = load_kappa(certificate)
    pieces = build_cubic_rhs(eta, kappa)
    identified = identify_visible_bch_sign(pieces)
    rhs_counts = {
        "finite_monomials": monomial_count(pieces.finite()),
        "infinity_monomials": monomial_count(pieces.infinity()),
        "mixed_monomials": sum(monomial_count(pieces.mixed(pair)) for pair in PAIRS),
    }
    # The third cochain is opened only after every cubic right-hand side and
    # the wrong-sign residual have been computed from eta and kappa.
    raw = read_cochain_bytes(root)
    cochain = json.loads(raw)
    equations, graded_terms = check_equations(pieces, cochain)
    lambdas = lambda_slice(certificate, cochain)
    support = support_check(cochain)
    sensitive = known_sensitive_control(pieces, cochain)
    signed = wrong_sign_control(pieces, identified, cochain, equations)
    equation_pass = sum(row["result"] == "pass" for row in equations)
    receipt = {
        "scope": "Forty third-middle raw equations at order h^3, exact over Q. No new gauge, no order-four equation, no carrier or formal-existence claim.",
        "source_commit": SOURCE_COMMIT,
        "arithmetic": "fractions.Fraction; floating-point coefficients are rejected",
        "primitive_gauge_regenerated": False,
        "primitive_equality_required": False,
        "hashes": {
            **pins,
            "third_cochain": {
                "path": REL_GZIP,
                "uncompressed_sha256": COCHAIN_SHA256,
                "uncompressed_bytes": COCHAIN_BYTES,
                "gzip_sha256": GZIP_SHA256,
                "gzip_bytes": GZIP_BYTES,
            },
        },
        "rhs_built_before_cochain": True,
        "rhs_monomials": rhs_counts,
        "equations": equations,
        "equation_count": 40,
        "equations_passed": equation_pass,
        "equations_failed": 40 - equation_pass,
        "component_checks_per_equation": ["finite", "infinity", "mixed_01", "mixed_02", "mixed_12", "grading_regularity"],
        "graded_w_terms": graded_terms,
        "lambda_slice": lambdas,
        "lambda_slice_passed": sum(row["result"] == "pass" for row in lambdas),
        "w_support": support,
        "controls": {
            "known_sensitive_origin_finite01": sensitive,
            "wrong_sign_bch": signed,
        },
        "dependencies": {
            "shared_with_published_verifiers": [
                "literal first jet eta",
                "literal second-middle primitives kappa, including mixed lambda z^{-1} E0^2",
                "plane geometry: coordinates, frame, bivector, line relation, transport and Cech cover",
            ],
            "independent_in_this_replay": [
                "polynomial and symmetric-tensor arithmetic",
                "cubic BCH assembly",
                "relation quotient",
                "grading and regularity",
                "the two controls",
            ],
            "not_imported": [
                "construct_third_middle.py",
                "pinned_contraction.py",
                "verify_third_middle.py",
                "tensor_slot_support.py",
            ],
            "lambda_slice_comparison": "The five supplied lambda-order-three primitives inside the kappa certificate are compared with the exported primitives. They are not recomputed.",
        },
        "all_passed": (
            equation_pass == 40
            and all(row["result"] == "pass" for row in lambdas)
            and support["result"] == "pass"
            and sensitive["result"] == "pass"
            and signed["result"] == "pass"
            and graded_terms == 13547
        ),
    }
    if write_path is not None:
        write_path.write_text(json.dumps(receipt, indent=2) + "\n")
    return receipt


def main():
    destination = Path(__file__).resolve().parent / "RECEIPT.json"
    receipt = run(destination)
    print(
        "equations",
        f"{receipt['equations_passed']}/{receipt['equation_count']}",
        "lambda",
        f"{receipt['lambda_slice_passed']}/5",
        "support",
        receipt["w_support"]["result"],
        "sensitive",
        receipt["controls"]["known_sensitive_origin_finite01"]["result"],
        "wrong_sign",
        receipt["controls"]["wrong_sign_bch"]["result"],
        "all_passed",
        receipt["all_passed"],
    )
    if not receipt["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
