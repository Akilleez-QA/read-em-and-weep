#!/usr/bin/env python3
"""Bounded universal identities and complete-file hashes, never actual-source evaluation."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
COUNTS = {"authentication": 0, "characters": 0, "degrees": 0}


def require(condition, label, group):
    COUNTS[group] += 1
    if not condition:
        raise RuntimeError(label)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


PROOF_BYTES = 15616
PROOF_SHA256 = "cd28b6dba69d23ef905f4816dcd1a7a3165bd8b337169ab0a6acb10a15ac06dc"
CORE_FILES = (
    "PROOF.md", "README.md", "INPUTS.md", "INPUTS.json", "PROVENANCE.md",
    "verify.py", "inputs/stationary-section-kernel.md", "inputs/shared-d-gluing.md",
)
SOURCE_PINS = (
    ("stationary-section-kernel", 1239,
     "360b7e8f55b05ca5740a10cb3ed844a594766f70",
     "research/hm/rankfour-profile11-triplet-stationary-section-kernel/PROOF.md",
     24626, "7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2",
     "2bc33710e6e3b5867955f6a3171786e10f1c08cb"),
    ("shared-d-gluing", 1207,
     "af136934955f1bcc700ee768e2debb983e75451d",
     "research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md",
     20361, "7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7",
     "3d051410e80a33f1c4d78d3403bb186595bb72c3"),
)
REPOSITORY = "Akilleez-QA/read-em-and-weep"

# Exact complete-file identity checks. These do not recertify source mathematics.
proof = (ROOT / "PROOF.md").read_bytes()
require(len(proof) == PROOF_BYTES, "complete proof byte length", "authentication")
require(sha256(proof) == PROOF_SHA256, "complete proof SHA256", "authentication")
inputs = json.loads((ROOT / "INPUTS.json").read_text(encoding="utf-8"))
require(inputs["schema"] == 1 and len(inputs["sources"]) == 2,
        "exactly two complete direct originals", "authentication")
for source, pin in zip(inputs["sources"], SOURCE_PINS):
    name, pr, ref, path, size, digest, blob = pin
    actual_pin = tuple(source[key] for key in
                       ("id", "pr", "ref", "path", "utf8_bytes", "sha256", "git_blob_sha1"))
    require(actual_pin == pin, "immutable source pin: " + name, "authentication")
    require(source["repository"] == REPOSITORY
            and source["local_path"] == "inputs/" + name + ".md"
            and source["url"] == "https://github.com/" + REPOSITORY + "/blob/" + ref + "/" + path,
            "source location: " + name, "authentication")
    data = (ROOT / source["local_path"]).read_bytes()
    require(len(data) == size, "entire source size: " + name, "authentication")
    require(sha256(data) == digest, "entire source SHA256: " + name, "authentication")
    require(git_blob(data) == blob, "entire source Git blob: " + name, "authentication")
    auth = source["authentication"]
    require(auth["path_blob_local_complete_bytes_equal"] is True
            and auth["computed_git_blob_equals_returned_sha"] is True,
            "recorded whole path/blob/local comparison: " + name, "authentication")
    require(auth["path_call"]["arguments"] == {
        "repository_full_name": REPOSITORY, "path": path, "ref": ref}
        and auth["blob_call"]["arguments"] == {
            "repository_full_name": REPOSITORY, "blob_sha": blob},
        "recorded complete path/blob requests: " + name, "authentication")
    for call in (auth["path_call"], auth["blob_call"]):
        require(call["started_at_utc"].startswith("2026-10-24T")
                and call["completed_at_utc"].startswith("2026-10-24T"),
                "recorded fresh retrieval date: " + name, "authentication")
frozen = json.loads((ROOT / "FROZEN.json").read_text(encoding="utf-8"))
require(frozen["schema"] == 1 and set(frozen["files"]) == set(CORE_FILES),
        "exact eight-file core freeze", "authentication")
require(frozen["proof_utf8_bytes"] == PROOF_BYTES
        and frozen["proof_sha256"] == PROOF_SHA256,
        "frozen proof agreement", "authentication")
for name in CORE_FILES:
    require(sha256((ROOT / name).read_bytes()) == frozen["files"][name],
            "whole frozen core file: " + name, "authentication")

# Five fixed A5 character rows, with exact integer arithmetic in Z[phi].
# A pair (a,b) is a+b*phi, phi^2=phi+1. No numerical root is used.
ZERO, ONE, PHI, PHI_BAR = (0, 0), (1, 0), (0, 1), (1, -1)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c+b*d, a*d+b*c+b*d


def scale(n, x):
    return n*x[0], n*x[1]


SIZES = (1, 15, 20, 12, 12)
CHARS = {
    "1": (ONE, ONE, ONE, ONE, ONE),
    "A": ((3, 0), (-1, 0), ZERO, PHI, PHI_BAR),
    "V": ((3, 0), (-1, 0), ZERO, PHI_BAR, PHI),
    "P": ((4, 0), ZERO, ONE, (-1, 0), (-1, 0)),
    "D": ((5, 0), ONE, (-1, 0), ZERO, ZERO),
}


def inner_numerator(left, right):
    result = ZERO
    for size, x, y in zip(SIZES, left, right):
        result = add(result, scale(size, mul(x, y)))
    return result


def char_sum(multiplicities):
    result = [ZERO] * 5
    for name, count in multiplicities.items():
        result = [add(x, scale(count, y)) for x, y in zip(result, CHARS[name])]
    return tuple(result)


require(sum(SIZES) == 60, "fixed class-size sum", "characters")
for name, row in CHARS.items():
    for other_name, other in CHARS.items():
        require(inner_numerator(row, other) == (60 if name == other_name else 0, 0),
                "fixed character orthogonality: " + name + "," + other_name, "characters")
require(sum(CHARS[name][0][0]**2 for name in CHARS) == 60,
        "fixed even irreducible dimension squares", "characters")
for target, expected in (("P", {"V": 1, "P": 1, "D": 1}),
                         ("V", {"P": 1, "D": 1})):
    product = tuple(mul(x, y) for x, y in zip(CHARS["A"], CHARS[target]))
    require(product == char_sum(expected), "fixed A tensor " + target, "characters")

# The even symmetric-power recurrence is capped at degree eighteen.
even = [CHARS["1"], CHARS["A"]]
for m in range(1, 9):
    even.append(tuple(add(mul(add(a, (-1, 0)), h), scale(-1, previous))
                      for a, h, previous in zip(CHARS["A"], even[m], even[m-1])))
EXPECTED_EVEN = {
    0: {"1": 1}, 2: {"A": 1}, 4: {"D": 1}, 6: {"V": 1, "P": 1},
    8: {"P": 1, "D": 1}, 16: {"V": 1, "P": 1, "D": 2},
    18: {"A": 1, "V": 1, "D": 1, "P": 2},
}
for degree, expected in EXPECTED_EVEN.items():
    require(even[degree//2] == char_sum(expected),
            "fixed H" + str(degree) + " character", "characters")
    require(even[degree//2][0] == (degree+1, 0),
            "fixed H" + str(degree) + " dimension", "characters")
require(tuple(add(x, scale(-1, y)) for x, y in
              zip(even[8], char_sum({"V": 1, "P": 1, "D": 1}))) == CHARS["D"],
        "twist-two equivariant Euler characteristic is D", "characters")

# A second fixed recurrence only through degree six records the physical
# odd low degrees used to exclude lower syzygy ranks. This is not enumeration.
ADJACENCY = {
    "1": {"W": 1}, "W": {"1": 1, "A": 1}, "A": {"W": 1, "S4": 1},
    "S4": {"A": 1, "D": 1}, "D": {"S4": 1, "T6": 1},
    "T6": {"D": 1, "V": 1, "P": 1},
}
low = [{"1": 1}, {"W": 1}]
for degree in range(1, 6):
    result = {}
    for name, count in low[degree].items():
        for neighbor, multiplicity in ADJACENCY[name].items():
            result[neighbor] = result.get(neighbor, 0) + count*multiplicity
    for name, count in low[degree-1].items():
        result[name] = result.get(name, 0) - count
    low.append({name: count for name, count in result.items() if count})
require(low == [{"1": 1}, {"W": 1}, {"A": 1}, {"S4": 1},
                {"D": 1}, {"T6": 1}, {"V": 1, "P": 1}],
        "fixed physical symmetric powers through degree six", "characters")
require(all("V" not in low[n] for n in range(6)) and low[6]["V"] == 1,
        "first V occurrence is degree six", "characters")

# Only prescribed small degree and sequence arithmetic follows. No point,
# matrix, jet, invariant polynomial, or actual section is evaluated.
require(4-1 == 3 and 0-6 == -6 == 3*(-2), "syzygy rank and degree", "degrees")
require(8-2 == 6 and 8-6 == 2 > 0, "rank-two syzygy contradiction degrees", "degrees")
require(4*(6-3) == 12, "degree-six P Wronskian degree", "degrees")
ordinary, ramified = (0, 1, 2, 3), (0, 1, 2, 4)
for sequence, expected in ((ordinary, 0), (ramified, 1)):
    require(all(sequence[i] < sequence[i+1] for i in range(3)),
            "prescribed vanishing sequence is increasing", "degrees")
    require(sum(a-i for i, a in enumerate(sequence)) == expected,
            "prescribed Wronskian weight", "degrees")
    require(sequence[:3] == (0, 1, 2), "prescribed second-jet orders", "degrees")
require(6+4+2 == 12 and 0-(6+4+2) == -12,
        "second-principal-parts and kernel degrees", "degrees")
require(18 == 16+2 and 6+18 == 24 and 4+18 == 22 and 2+18 == 20,
        "product and directed Hom-line degrees", "degrees")
require((-12)-(-18) == 6, "terminal factor Hom degree", "degrees")
require(20-12 == 8, "forbidden residual divisor degree", "degrees")
# Below 24, any nonzero orbit-divisor total from 12,20,30,60 is 12 or 20:
# two positive orbits already have total at least 24.
require(2*12 == 24 and 30 > 22 and 60 > 22,
        "fixed orbit-divisor lower bounds", "degrees")
for degree in (6, 8, 22):
    require(0 < degree < 24 and degree not in (12, 20),
            "forbidden invariant divisor degree " + str(degree), "degrees")


def cohomology_dimensions(blocks, twist):
    h0 = sum(rank*max(degree+twist+1, 0) for rank, degree in blocks)
    h1 = sum(rank*max(-degree-twist-1, 0) for rank, degree in blocks)
    return h0, h1


selected = ((5, -2), (2, -3), (6, -3))
other = ((8, -2), (2, -3), (3, -4))
for blocks in (selected, other):
    require(sum(rank for rank, _ in blocks) == 13,
            "prescribed F18 alternative rank", "degrees")
    require(sum(rank*degree for rank, degree in blocks) == -34,
            "prescribed F18 alternative degree", "degrees")
require(cohomology_dimensions(selected, 2) == (5, 0),
        "selected alternative twist-two cohomology dimensions", "degrees")
require(cohomology_dimensions(other, 2) == (8, 3),
        "other alternative twist-two cohomology dimensions", "degrees")
require(17-12 == 5 and 17-4 == 13 and 17*(-2) == -34,
        "complete-jet sequence dimensions and degree", "degrees")
require(13+3 == 16 and -34+3*(-4) == -46,
        "actual extension formal rank and degree", "degrees")
require(max(-(-1)-1, 0) == 0 and max(-(-2)-1, 0) == 1,
        "extension block H1 dimensions", "degrees")
require(inner_numerator(CHARS["D"], CHARS["V"]) == ZERO,
        "D to V equivariant extension block is zero", "degrees")

print("PASS: " + str(sum(COUNTS.values())) + " bounded checks " + json.dumps(COUNTS, sort_keys=True))
print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Entire frozen checker SHA256: " + sha256((ROOT / "verify.py").read_bytes()))
print("Exactly two complete direct originals authenticated; all eight frozen core files match.")
print("Checks are hashes and fixed universal arithmetic, not proof or actual-source evaluation.")
print("Conditional first F18 alternative and equivariantly split E0 extension only; "
      "no K1 exclusion or realization, horizontal splitting, higher-order matching, or algebraicity.")
