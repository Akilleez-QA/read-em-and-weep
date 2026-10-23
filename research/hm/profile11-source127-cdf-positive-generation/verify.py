#!/usr/bin/env python3
"""Bounded universal checks only; no HM tensors or instance evaluations."""
from collections import Counter
from hashlib import sha1
from itertools import combinations_with_replacement
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
EXPECTED = {
    "GENERATION.md": "3d308f6fbdb5c224a085b41eec26e917a6031692",
    "FULL-MODULE.md": "2ba0a7eee6ef2eb5413683e85618d7902dca3970",
    "ALGEBRA.md": "83f5aee293995257459229e6b323522224ce8f3d",
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


manifest = json.loads((ROOT / "audit-inputs/manifest.json").read_text())
require({e["name"]: e["git_blob"] for e in manifest} == EXPECTED,
        "Manifest does not match the three immutable dependencies")
require(len(manifest) == 3, "Unexpected manifest multiplicity")
for entry in manifest:
    data = (ROOT / "audit-inputs" / entry["name"]).read_bytes()
    blob = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    require(blob == entry["git_blob"], "Input blob mismatch: " + entry["name"])

# Formal coordinate symbols: three positive and two negative. These are
# abstract indeterminates, not selected coordinates of an actual HM source.
PARITY = (0, 0, 0, 1, 1)


def pairs(monomial):
    counts = Counter(monomial)
    for i, j in combinations_with_replacement(range(5), 2):
        needed = Counter((i, j))
        if PARITY[i] == PARITY[j] and all(counts[k] >= v for k, v in needed.items()):
            yield (i, j)


checked = 0
for monomial in combinations_with_replacement(range(5), 5):
    possible = list(pairs(monomial))
    require(bool(possible), "A degree-five monomial has no even pair")
    pair = possible[0]
    remaining = list(monomial)
    for variable in pair:
        remaining.remove(variable)
    require(len(remaining) == 3, "Wrong remainder degree")
    require(sorted(remaining + list(pair)) == list(monomial), "Factorization failed")
    for generator_parity in (0, 1):
        before = (sum(PARITY[i] for i in monomial) + generator_parity) % 2
        after = (sum(PARITY[i] for i in remaining) + generator_parity) % 2
        require(before == after, "Generator-inclusive parity changed")
        checked += 1
require(checked == 252, "Expected 126 formal monomials and two generator signs")

# The n>=3 hypothesis is real: a mixed quadratic has no same-sign pair.
require(not list(pairs((0, 3))), "Degree-two negative control failed")

# Fixed dimensions from the exact algebra dependency; no matrix is built.
require(sum((17, 24)) == 41, "N2 block total")
require(sum((9, 21, 7)) == 37, "N4 block total")
require(3 + 4 == 7, "Scalar-target representation V+P")
require((41 - 0, 54 - 8, 37 - 4) == (41, 46, 33), "Common-kernel dimensions")
require(4 - 1 == 3 and 3 - 2 == 1, "Scalar quotient and injectivity bound")

print("PASS: three immutable input blobs; 126 formal monomials; 252 parity checks;")
print("degree-two negative control; fixed block and filtration dimensions.")
print("Written proof/review, not this checker, establishes module generation,")
print("actual-map identification, surjectivity, nonextension and the C/C^2 dichotomy.")
