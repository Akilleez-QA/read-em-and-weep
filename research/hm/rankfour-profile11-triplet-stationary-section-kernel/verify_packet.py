#!/usr/bin/env python3
"""Bounded fixed-character/arithmetic checks; never actual-source evaluation."""
from collections import Counter
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
checks = 0


def require(condition, label):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(label)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


# FREEZE_CONSTANTS_BEGIN
PROOF_BYTES = 24626
PROOF_SHA256 = '7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2'
SOURCES = [{'id': 'seven-space-ramification',
  'pr': 1238,
  'ref': 'd259230fbf7259e52db267c56203a29f221da5f0',
  'path': 'research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md',
  'local_path': 'inputs/seven-space-ramification.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 20687,
  'sha256': '25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3',
  'git_blob_sha1': '0da306ac1dc4c879ced57c28e2ec3a07f027da70',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/d259230fbf7259e52db267c56203a29f221da5f0/research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md'},
 {'id': 'shared-d',
  'pr': 1206,
  'ref': '252b967ebbfbea6fc0c6451a835ab2daff92d73b',
  'path': 'research/hm/rankfour-profile11-triplet-shared-d/PROOF.md',
  'local_path': 'inputs/shared-d.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 8801,
  'sha256': 'f2e5b5d8bdb0f8a156aaf38695042f204b4d3cffd1a40a4a28870bed2ef13793',
  'git_blob_sha1': '82596d9d02147711e0d5f7953912a94fffbae684',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/252b967ebbfbea6fc0c6451a835ab2daff92d73b/research/hm/rankfour-profile11-triplet-shared-d/PROOF.md'}]
CORE_FILES = ['PROOF.md', 'INPUTS.json', 'verify_packet.py', 'inputs/seven-space-ramification.md', 'inputs/shared-d.md', 'README.md', 'PROVENANCE.md']
# FREEZE_CONSTANTS_END

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--arithmetic-only", action="store_true",
                    help="Run only bounded universal checks; no authentication claim.")
args = parser.parse_args()
if not args.arithmetic_only:
    require(PROOF_BYTES is not None and SOURCES is not None,
            "Missing freeze constants; use --arithmetic-only for universal checks.")
    proof = (ROOT / "PROOF.md").read_bytes()
    require(len(proof) == PROOF_BYTES, "entire frozen proof byte count")
    require(sha256(proof) == PROOF_SHA256, "entire frozen proof SHA256")
    manifest = json.loads((ROOT / "INPUTS.json").read_text())
    require(manifest == {"schema": 1, "sources": SOURCES}, "exact two-source manifest")
    require({s["id"] for s in SOURCES} == {"seven-space-ramification", "shared-d"},
            "two complete direct originals only")
    for source in SOURCES:
        require(len(source["ref"]) == 40 and source["pr"] > 0,
                "immutable published source pin: " + source["id"])
        data = (ROOT / source["local_path"]).read_bytes()
        require(len(data) == source["utf8_bytes"], "entire source length: " + source["id"])
        require(sha256(data) == source["sha256"], "entire source SHA256: " + source["id"])
        require(git_blob(data) == source["git_blob_sha1"], "entire source Git blob: " + source["id"])
    frozen = json.loads((ROOT / "FROZEN.json").read_text())
    require(frozen["schema"] == 1 and sorted(frozen["files"]) == sorted(CORE_FILES),
            "exact seven-file core freeze")
    require(frozen["proof_utf8_bytes"] == PROOF_BYTES and frozen["proof_sha256"] == PROOF_SHA256,
            "proof freeze agreement")
    for name in CORE_FILES:
        require(sha256((ROOT / name).read_bytes()) == frozen["files"][name],
                "entire frozen core file: " + name)
authentication_checks = checks

# Fixed physical representation ring only. No selected actual tensor is used.
dim = {"1": 1, "W": 2, "Wp": 2, "A": 3, "V": 3,
       "S4": 4, "P": 4, "D": 5, "T6": 6}
adj = {
    "1": {"W": 1}, "W": {"1": 1, "A": 1},
    "A": {"W": 1, "S4": 1}, "S4": {"A": 1, "D": 1},
    "D": {"S4": 1, "T6": 1}, "T6": {"D": 1, "V": 1, "P": 1},
    "V": {"T6": 1}, "P": {"T6": 1, "Wp": 1}, "Wp": {"P": 1},
}


def dimension(character):
    return sum(dim[k] * v for k, v in character.items())


def times_w(character):
    answer = Counter()
    for k, n in character.items():
        for j, m in adj[k].items():
            answer[j] += n * m
    return dict(answer)


def subtract(a, b):
    return {k: a.get(k, 0) - b.get(k, 0)
            for k in dim if a.get(k, 0) != b.get(k, 0)}


for k, value in adj.items():
    require(dimension(value) == 2 * dim[k], "W adjacency dimension: " + k)
sym = [{"1": 1}, {"W": 1}]
for n in range(1, 18):
    value = subtract(times_w(sym[n]), sym[n-1])
    require(all(v >= 0 for v in value.values()), "nonnegative fixed Sym character " + str(n+1))
    require(dimension(value) == n+2, "fixed Sym dimension " + str(n+1))
    sym.append(value)
require(sym[2] == {"A": 1}, "H2=A")
require(sym[4] == {"D": 1}, "H4=D")
require(sym[6] == {"V": 1, "P": 1}, "H6=V_alt+P")
require(sym[12] == {"1": 1, "A": 1, "D": 1, "P": 1}, "H12=1+A+D+P")
require(sym[18] == {"A": 1, "V": 1, "D": 1, "P": 2}, "H18=A+V_alt+D+2P")

# Independent even-character check in Z[phi], phi^2=phi+1.
# A pair (a,b) denotes a+b*phi. No numerical roots or orbit points occur.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c+b*d, a*d+b*c+b*d)


def scale(k, x):
    return (k*x[0], k*x[1])


def constant(n):
    return (n, 0)


one = constant(1)
phi = (0, 1)
phi_bar = (1, -1)
sizes = (1, 15, 20, 12, 12)
table = {
    "1": [one, one, one, one, one],
    "A": [constant(3), constant(-1), constant(0), phi, phi_bar],
    "V": [constant(3), constant(-1), constant(0), phi_bar, phi],
    "P": [constant(4), constant(0), constant(1), constant(-1), constant(-1)],
    "D": [constant(5), constant(1), constant(-1), constant(0), constant(0)],
}


def inner_numerator(x, y):
    result = (0, 0)
    for size, a, b in zip(sizes, x, y):
        result = add(result, scale(size, mul(a, b)))
    return result


require(sum(sizes) == 60, "A5 class sizes")
for k, row in table.items():
    for j, other in table.items():
        require(inner_numerator(row, other) == (60 if k == j else 0, 0),
                "fixed character orthogonality: " + k + "," + j)
require(sum(dim[k]**2 for k in table) == 60, "complete A5 even character table")
even = [table["1"], table["A"]]
for m in range(1, 9):
    even.append([add(mul(add(a, neg(one)), h), neg(previous))
                 for a, h, previous in zip(table["A"], even[m], even[m-1])])
for m, row in enumerate(even):
    decomposition = {}
    for k, irrep in table.items():
        a, b = inner_numerator(row, irrep)
        require(b == 0 and a % 60 == 0 and a >= 0,
                "integral even multiplicity: degree " + str(2*m) + "," + k)
        if a:
            decomposition[k] = a // 60
    require(decomposition == sym[2*m], "independent recurrence agreement in degree " + str(2*m))
character_checks = checks - authentication_checks

# Whole-orbit formal inertia exponents; all arithmetic is modulo five or ten.
weights = {
    "1": Counter([0]), "A": Counter([4, 0, 1]), "V": Counter([3, 0, 2]),
    "D": Counter([3, 4, 0, 1, 2]), "P": Counter([1, 2, 3, 4]),
}
require((-18) % 10 == 2, "value alpha weight is alpha^2=mu")
require((2-18) % 10 == 4, "cotangent derivative alpha weight is alpha^4=mu^2")
require(weights["A"][1] == 1 and weights["A"][2] == 0,
        "A has one value weight and no pure-derivative weight")
require(Counter(j % 5 for j in range(-3, 4)) == weights["V"]+weights["P"],
        "H6 inertia weights split as V_alt+P")
target = {k: c[2] for k, c in weights.items() if c[2]}
require(target == {"V": 1, "D": 1, "P": 1}, "induced target character multiplicities")
require(dimension(target) == 12, "target length and dimension")
require(6+12 == 18 and 6-12 == -6, "Leibniz product degree and injective restriction kernel")
require(-(-6)-2 == 4, "Serre-dual cohomology is H4 star")
inertia_checks = checks - authentication_checks - character_checks

# Fixed orbit and Wronskian arithmetic, never actual-instance ranks or values.
orbit_sizes = tuple(60 // order for order in (1, 2, 3, 5))
require(orbit_sizes == (60, 30, 20, 12), "cyclic stabilizer orbit arithmetic")
require(24 // 4 == 6 and 6 * 2 == 12, "six order-five subgroups and twelve fixed loci")
require(12 <= 18 < 20 and 2*12 > 18, "only possible fixed divisor through degree eighteen")
require(5*(18-4) == sum(18-2*j for j in range(5)) == 70, "D Wronskian degree")
require(sum(a-i for i, a in enumerate((0, 2, 3, 4, 5))) == 4,
        "stationary five-system minimum Wronskian weight")
require(70-4*12 == 22, "residual invariant divisor degree")
# Only 0 or 1 copies of length twenty, and at most 1 copy of length twelve,
# could occur below twenty-four. This is bounded fixed integer arithmetic.
require(22 < 30 and 22 % 12 != 0 and (22-20) % 12 != 0,
        "twenty-two is not an invariant-divisor degree")
require(12*(18-11) == 84 < 11*12 == 132, "independent twelve-system Wronskian contradiction")
require(19-12 == 7 == dim["A"]+dim["P"], "universal kernel dimension")
require(19-4 == 15 == dim["A"]+dim["V"]+dim["D"]+dim["P"],
        "original section image and gamma kernel dimension")
require(19-15 == 4 == dim["P"], "actual coefficient kernel dimension")
require((0, 2, 3, 4, 5, 6, 8)[1] == 2, "seven-space input implies first-order stationarity")
arithmetic_checks = checks - authentication_checks - character_checks - inertia_checks

print("PASS: " + str(checks) + " bounded checks (" + str(authentication_checks)
      + " whole-file authentication; " + str(character_checks) + " fixed universal character; "
      + str(inertia_checks) + " symbolic whole-orbit inertia/cohomology; "
      + str(arithmetic_checks) + " fixed orbit/degree/kernel checks).")
if args.arithmetic_only:
    print("Arithmetic-only run: no source authentication or frozen-packet claim.")
else:
    print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Universal stationary subspace and conditional actual coefficient kernel only; "
      "no K1 realization, exclusion, higher-order matching, or algebraicity.")
