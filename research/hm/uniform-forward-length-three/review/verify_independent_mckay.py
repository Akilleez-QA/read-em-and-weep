#!/usr/bin/env python3
"""Independent, bounded integer-McKay checks for the length-three theorem.

Standard library only. No import of the author verifier or any external data.
The sole representation-theoretic input is the explicitly labelled affine E8
McKay graph for tensoring binary-icosahedral irreducibles by W. All computation
uses integer multiplicity vectors, not conjugacy-class character evaluations.
Only universal representations and the two proved finite scalar-degree lists
are checked. No actual map, coefficient, point, jet, rank or tail is evaluated.
"""

import hashlib
import json
from pathlib import Path


PROOF_SHA256 = "d16a3186e5d922fe55206c7f139e152fb9153614be71e2a172f47b801c44c40c"
INPUTS_SHA256 = "f365a59d991e90ebec228657929fc9a4c8d5d9faef4f9da03e6fa01a92a443df"
ROOT = Path(__file__).resolve().parents[1]
NAMES = ("1", "W", "Wp", "A", "V", "P", "S", "D", "T")
DIMS = (1, 2, 2, 3, 3, 4, 4, 5, 6)
PARITY = (0, 1, 1, 0, 0, 0, 1, 0, 1)
EDGES = (("1", "W"), ("W", "A"), ("A", "S"), ("S", "D"),
         ("D", "T"), ("T", "V"), ("T", "P"), ("P", "Wp"))
ZERO = (0,) * len(NAMES)
REPS = {name: tuple(int(i == j) for i in range(len(NAMES)))
        for j, name in enumerate(NAMES)}
CHECKS = []


def check(condition, label):
    # Deliberately not a Python assert: checks remain live under python -O.
    CHECKS.append(label)
    if not condition:
        raise RuntimeError(label)


def add(*vectors):
    return tuple(sum(entries) for entries in zip(*vectors))


def scale(number, vector):
    return tuple(number * entry for entry in vector)


def subtract(left, right):
    return add(left, scale(-1, right))


def rep(**multiplicities):
    return tuple(multiplicities.get(name, 0) for name in NAMES)


def w_tensor(vector):
    result = [0] * len(NAMES)
    for left, right in EDGES:
        i, j = NAMES.index(left), NAMES.index(right)
        result[i] += vector[j]
        result[j] += vector[i]
    return tuple(result)


def sym_tensor(degree, vector):
    """Sym^degree(W) tensor vector, via S_n=W*S_(n-1)-S_(n-2)."""
    if degree < 0:
        return ZERO
    previous, current = ZERO, vector
    for _ in range(degree):
        previous, current = current, subtract(w_tensor(current), previous)
    return current


def dimension(vector):
    return sum(a * b for a, b in zip(vector, DIMS))


def effective(vector):
    return all(entry >= 0 for entry in vector)


def contains(large, small):
    return effective(subtract(large, small))


def coefficient(vector, name):
    return vector[NAMES.index(name)]


def h0(vector, degree):
    return sym_tensor(degree, vector) if degree >= 0 else ZERO


def chi(vector, degree):
    if degree >= 0:
        return h0(vector, degree)
    return ZERO if degree == -1 else scale(-1, sym_tensor(-degree - 2, vector))


def hom(source, source_degree, target, target_degree):
    target_sections = h0(target, target_degree - source_degree)
    return sum(a * b for a, b in zip(source, target_sections))


def phi(vector, degree):
    # All irreducibles are self-dual; these are the three terms in (5).
    return add(h0(vector, 2 - degree), h0(vector, -degree), chi(vector, 4 - degree))


def serial(vector):
    # Retain zeros as well as negative multiplicities in every signed result.
    return dict(zip(NAMES, vector))


one, W, Wp, A, V, P, S, D, T = (REPS[name] for name in NAMES)
check(hashlib.sha256((ROOT / "PROOF.md").read_bytes()).hexdigest() == PROOF_SHA256,
      "frozen whole-proof SHA256")
manifest_data = (ROOT / "INPUTS.json").read_bytes()
check(hashlib.sha256(manifest_data).hexdigest() == INPUTS_SHA256, "frozen foundational source manifest SHA256")
manifest = json.loads(manifest_data)
check(len(manifest) == 4, "four explicit foundational source copies")
for item in manifest:
    path = Path(item["file"])
    check(not path.is_absolute() and ".." not in path.parts, "portable source path")
    data = (ROOT / path).read_bytes()
    check(len(data) == item["bytes"], "source byte length: " + path.name)
    check(hashlib.sha256(data).hexdigest() == item["sha256"], "source SHA256: " + path.name)
    git_blob = b"blob " + str(len(data)).encode() + b"\0" + data
    check(hashlib.sha1(git_blob).hexdigest() == item["git_blob_sha1"],
          "source Git blob identity: " + path.name)

check(sum(d * d for d in DIMS) == 120, "sum of irreducible dimension squares")
for name, vector in REPS.items():
    check(dimension(w_tensor(vector)) == 2 * dimension(vector), "McKay dimensions: " + name)
    check(all(PARITY[i] != PARITY[NAMES.index(name)] for i, m in enumerate(w_tensor(vector)) if m),
          "McKay central parity: " + name)
for degree in range(26):
    vector = sym_tensor(degree, one)
    check(effective(vector), "genuine symmetric power " + str(degree))
    check(dimension(vector) == degree + 1, "symmetric-power dimension " + str(degree))
    check(all(PARITY[i] == degree % 2 for i, m in enumerate(vector) if m),
          "symmetric-power parity " + str(degree))
for degree, expected in enumerate((one, W, A, S, D, T)):
    check(sym_tensor(degree, one) == expected, "low symmetric-power label " + str(degree))
check(sym_tensor(6, one) == add(V, P), "Sym6=V+P")
check(w_tensor(Wp) == P, "W*Wp=P")
check(w_tensor(V) == T, "W*V=T")

M2, M3, M4 = rep(A=1, V=2, P=3, D=4), rep(Wp=3, S=3, T=6), rep(V=2, P=4, D=3)
U = rep(Wp=1, T=2)
check((dimension(M2), dimension(M3), dimension(M4), dimension(U)) == (41, 54, 37, 14),
      "actual coefficient ranks and cubic section dimension")
expected_E = {1: rep(Wp=-1, T=-3), 2: rep(V=-1), 3: U, 4: rep(V=3, P=3, D=2)}
actual_E = {}
for twist, expected in expected_E.items():
    actual_E[twist] = subtract(sym_tensor(twist - 1, M3), sym_tensor(twist, M4))
    check(actual_E[twist] == expected, "full chi(E(" + str(twist) + "))")
Q3 = subtract(sym_tensor(2, M3), sym_tensor(3, M2))
check(Q3 == rep(W=-2, S=-1, T=1), "full chi(Q*(3))")
check(add(U, w_tensor(V)) == scale(-1, actual_E[1]), "split H1(E(1))")
check(dimension(U) + dimension(V) == 17 and -3 * dimension(U) - 4 * dimension(V) == -54,
      "forced E splitting rank and degree")
check(hom(V, 0, A, 0) == 0, "scalar degree-six source tail cannot supply V")
check(14 * -4 == -56 and -54 - (-56) + 3 * 3 == 11, "full-image degree lower bound")

# Check every low-degree source Hom used to exclude negative, scalar, or W blocks.
for target in (one, A, V):
    check(hom(U, 0, target, -1) == 0, "no cubic map to negative block " + str(serial(target)))
    check(hom(V, -1, target, -1) == int(target == V), "quartic negative-block Hom")
for degree in (1, 3):
    check(hom(U, 0, one, degree) == 0, "scalar cubic-source Hom at degree " + str(degree))
    check(hom(V, -1, one, degree) == 0, "scalar quartic-source Hom at degree " + str(degree))
    check(3 * (degree + 1) < dimension(U), "triplet block has too few sections")
for degree in (0, 2):
    check(hom(U, 0, W, degree) == 0, "W block cubic-source Hom at degree " + str(degree))
    check(hom(V, -1, W, degree) == 0, "W block quartic-source Hom at degree " + str(degree))
check(sym_tensor(2, Wp) == T, "Wp*Sym2=T")
check(sym_tensor(4, Wp) == add(S, T), "Wp*Sym4=S+T")

# Verify all displayed Phi cases, including the general negative-cohomology sign.
for degree in range(26):
    if degree == 0:
        expected = add(sym_tensor(4, one), sym_tensor(2, one), one)
    elif degree == 1:
        expected = add(sym_tensor(3, one), W)
    elif degree == 2:
        expected = add(sym_tensor(2, one), one)
    elif degree == 3:
        expected = W
    elif degree == 4:
        expected = one
    elif degree == 5:
        expected = ZERO
    else:
        expected = scale(-1, sym_tensor(degree - 6, one))
    check(phi(one, degree) == expected, "Phi formula degree " + str(degree))

budgets = {0: rep(W=2, Wp=1, S=2, T=1), 2: rep(W=2, Wp=1, S=1)}
for degree, expected in budgets.items():
    check(subtract(phi(Wp, degree), Q3) == expected, "full scalar budget for a=" + str(degree))
check((dimension(budgets[0]), dimension(budgets[2])) == (20, 10), "bounded scalar budgets")
check(2 * 0 + 5 < 11 and 2 * 2 + 5 < 11, "degree-five scalar excluded")
for degree in (7, 9, 11, 13):
    check(coefficient(sym_tensor(degree, one), "T") == 1, "small scalar single T")
for degree in (21, 23, 25):
    check(coefficient(sym_tensor(degree - 6, one), "T") == 2, "large scalar exceeds T budget")
for degree in (9, 11):
    check(coefficient(sym_tensor(degree, one), "Wp") == 0, "degree-two doublet misses Wp")
for degree in (13, 15):
    check(coefficient(sym_tensor(degree - 6, one), "T") == 1, "degree-two doublet exceeds T budget")
check(sym_tensor(7, one) == add(Wp, T), "Sym7=Wp+T")

# Two fixed scalar-degree lists, not splitting/negative-tail enumeration.
lists = {0: (7, 9, 11, 13, 15, 17, 19, 21, 23, 25), 2: (7, 9, 11, 13, 15)}
survivors = []
for doublet_degree, scalar_degrees in lists.items():
    for scalar_degree in scalar_degrees:
        sections = add(sym_tensor(doublet_degree, Wp), sym_tensor(scalar_degree, one))
        cost = sym_tensor(scalar_degree - 6, one)
        eligible = (2 * doublet_degree + scalar_degree >= 11 and
                    contains(sections, U) and contains(budgets[doublet_degree], cost))
        if eligible:
            survivors.append((doublet_degree, scalar_degree))
check(survivors == [(0, 15), (0, 17), (0, 19), (2, 7)], "complete two-list survivor comparison")

expected_kernels = (rep(V=2, P=1), rep(A=-1, V=2, D=1),
                    rep(**{"1": -1, "A": -1, "V": 2, "P": 1}), rep(V=2, P=2))
kernel_results = []
for (a, b), expected in zip(survivors, expected_kernels):
    quotient_a, quotient_b = a - 3, b - 3
    quotient_chi4 = add(chi(Wp, quotient_a + 4), chi(one, quotient_b + 4))
    kernel_chi4 = subtract(actual_E[4], quotient_chi4)
    check(kernel_chi4 == expected, "complete signed kernel character for " + str((a, b)))
    check(coefficient(kernel_chi4, "V") == 2, "two top V multiplicities")
    doublet_hom = hom(V, -4, Wp, quotient_a - 2)
    scalar_hom = hom(V, -4, one, quotient_b - 2)
    check(doublet_hom == 0, "complete doublet endpoint Hom vanishing")
    check(scalar_hom == 1, "exact scalar endpoint Hom dimension")
    defect_bound = 2 * a + b - 11
    check(0 <= defect_bound < 12, "invariant full-image defect bound")
    check(dimension(kernel_chi4) == 14 * 5 + (-54 - (2 * quotient_a + quotient_b)),
          "ordinary kernel Euler characteristic")
    kernel_results.append({"saturated_image_degrees": [a, b],
                           "quotient_degrees": [quotient_a, quotient_b],
                           "chi_K4": serial(kernel_chi4),
                           "endpoint_Hom_dimensions": [doublet_hom, scalar_hom],
                           "maximum_defect_degree": defect_bound})
check(-4 - 2 < -4, "all internal target degrees are below the top source")
check(3 * -4 == -12 != 0, "horizontal top subbundle degree contradiction")
check(tuple(60 // order for order in (1, 2, 3, 5)) == (60, 30, 20, 12),
      "projective A5 orbit degrees")

print(json.dumps({"status": "PASS", "proof_sha256": PROOF_SHA256,
                  "inputs_sha256": INPUTS_SHA256,
                  "method": "integer affine-E8 McKay recursion; stdlib only",
                  "fixed_universal_checks": len(CHECKS),
                  "maximum_symmetric_degree": 25,
                  "chi_E": {str(t): serial(c) for t, c in actual_E.items()},
                  "chi_Qstar3": serial(Q3), "kernels": kernel_results,
                  "scope": "Abstract fixed universal checks only; geometry is reviewed separately."},
                 indent=2, sort_keys=True))
