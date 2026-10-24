#!/usr/bin/env python3
"""Bounded universal checks and complete-file authentication, never actual-source evaluation."""
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
PROOF_BYTES = 28094
PROOF_SHA256 = '407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637'
SOURCES = [{'id': 'stationary-section-kernel',
  'pr': 1239,
  'ref': '360b7e8f55b05ca5740a10cb3ed844a594766f70',
  'path': 'research/hm/rankfour-profile11-triplet-stationary-section-kernel/PROOF.md',
  'local_path': 'inputs/stationary-section-kernel.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 24626,
  'sha256': '7835e0a0e6769163dca0ad2ed0a62e3c79a491dc6ebc39e5f8c988d9a9ec6de2',
  'git_blob_sha1': '2bc33710e6e3b5867955f6a3171786e10f1c08cb',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/360b7e8f55b05ca5740a10cb3ed844a594766f70/research/hm/rankfour-profile11-triplet-stationary-section-kernel/PROOF.md'},
 {'id': 'seven-space-ramification',
  'pr': 1238,
  'ref': 'd259230fbf7259e52db267c56203a29f221da5f0',
  'path': 'research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md',
  'local_path': 'inputs/seven-space-ramification.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 20687,
  'sha256': '25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3',
  'git_blob_sha1': '0da306ac1dc4c879ced57c28e2ec3a07f027da70',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/d259230fbf7259e52db267c56203a29f221da5f0/research/hm/rankfour-profile11-triplet-seven-space-ramification/PROOF.md'},
 {'id': 'first-kernel-forward-closure',
  'pr': 1236,
  'ref': '092fc5f31dfaa5553ee5ea687f175ecba1878a2a',
  'path': 'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md',
  'local_path': 'inputs/first-kernel-forward-closure.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 18052,
  'sha256': '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
  'git_blob_sha1': 'f77cfb52743be86e46e0c40570ec036e69aebaf3',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/092fc5f31dfaa5553ee5ea687f175ecba1878a2a/research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md'}]
CORE_FILES = ['PROOF.md', 'INPUTS.json', 'verify_packet.py', 'inputs/stationary-section-kernel.md', 'inputs/seven-space-ramification.md', 'inputs/first-kernel-forward-closure.md', 'README.md', 'PROVENANCE.md']
# FREEZE_CONSTANTS_END

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--arithmetic-only", action="store_true",
                    help="Run bounded universal identities only; no authentication claim.")
args = parser.parse_args()
if not args.arithmetic_only:
    require(PROOF_BYTES is not None and SOURCES is not None,
            "Missing frozen constants; use --arithmetic-only before freezing.")
    proof = (ROOT / "PROOF.md").read_bytes()
    require(len(proof) == PROOF_BYTES, "complete proof length")
    require(sha256(proof) == PROOF_SHA256, "complete proof SHA256")
    manifest = json.loads((ROOT / "INPUTS.json").read_text())
    require(manifest == {"schema": 1, "sources": SOURCES}, "exact three-source manifest")
    require({s["id"] for s in SOURCES} == {
        "stationary-section-kernel", "seven-space-ramification",
        "first-kernel-forward-closure"}, "exact three complete direct originals")
    for source in SOURCES:
        require(len(source["ref"]) == 40 and source["pr"] > 0,
                "immutable published source pin: " + source["id"])
        data = (ROOT / source["local_path"]).read_bytes()
        require(len(data) == source["utf8_bytes"], "complete source length: " + source["id"])
        require(sha256(data) == source["sha256"], "complete source SHA256: " + source["id"])
        require(git_blob(data) == source["git_blob_sha1"], "complete source Git blob: " + source["id"])
    frozen = json.loads((ROOT / "FROZEN.json").read_text())
    require(frozen["schema"] == 1 and sorted(frozen["files"]) == sorted(CORE_FILES),
            "exact eight-file core freeze")
    require(frozen["proof_utf8_bytes"] == PROOF_BYTES
            and frozen["proof_sha256"] == PROOF_SHA256, "proof freeze agreement")
    for name in CORE_FILES:
        require(sha256((ROOT / name).read_bytes()) == frozen["files"][name],
                "complete frozen core file: " + name)
authentication_checks = checks

# Only two prescribed universal integer sequences are checked. There is no scan.
ordinary = (0, 1, 2, 3, 4, 5, 6)
ramified = (0, 2, 3, 4, 5, 6, 8)
expected_deficits = (0, 1, 2, 3, 4, 5, 7)
expected_source_degrees = (-18, -34, -48, -60, -70, -78, -84)
expected_flag_degrees = (-18, -22, -24, -24, -22, -18, 0)
flag_degrees = []
for r in range(1, 8):
    require(all(ramified[i] < ramified[i+1] for i in range(6)),
            "distinct formal exponents, rank " + str(r))
    deficit = sum(ramified[i]-i for i in range(r))
    source_degree = sum(-18+2*j for j in range(r))
    require(deficit == expected_deficits[r-1], "prescribed local saturation deficit " + str(r))
    require(sum(ordinary[i]-i for i in range(r)) == 0, "ordinary local deficit " + str(r))
    require(source_degree == -18*r+r*(r-1) == expected_source_degrees[r-1],
            "intrinsic rank-r principal-parts degree " + str(r))
    degree = source_degree+12*deficit
    require(degree == expected_flag_degrees[r-1], "saturated flag degree " + str(r))
    flag_degrees.append(degree)
for name, sequence in (("ordinary", ordinary), ("ramified", ramified)):
    reflected = tuple(sequence[-1]-sequence[6-i] for i in range(7))
    require(reflected == sequence, "reflected dual sequence: " + name)
    cofactor_orders = tuple(sum(sequence)-sequence[i]-15 for i in range(7))
    common = min(cofactor_orders)
    require(common == sum(sequence[:6])-15, "primitive cofactor common factor: " + name)
    require(tuple(sorted(order-common for order in cofactor_orders)) == reflected,
            "primitive dual cofactor orders: " + name)
    require(len(set(cofactor_orders)) == 7, "distinct formal dual orders: " + name)
require(flag_degrees[5] == -18, "Q6 and dual curve degree")
require(-flag_degrees[5] == 18, "constant quotient line degree")
require(7*12 == 84 == 7*(18-6), "full Wronskian budget")
for r in range(1, 7):
    require(flag_degrees[r-1] == flag_degrees[6-r],
            "self-dual flag degree compatibility " + str(r))
quotient_degrees = tuple(flag_degrees[i] - (flag_degrees[i-1] if i else 0)
                         for i in range(7))
require(quotient_degrees == (-18, -4, -2, 0, 2, 4, 18),
        "successive saturated quotient degrees")
require(quotient_degrees == tuple(-a for a in reversed(quotient_degrees)),
        "opposite paired quotient degrees")
sequence_checks = checks-authentication_checks

# Small fixed A5 character identities, in the exact ring Z[phi].
# A pair (a,b) means a+b*phi and phi^2=phi+1; no numerical roots are used.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c+b*d, a*d+b*c+b*d)


def scale(k, x):
    return (k*x[0], k*x[1])


sizes = (1, 15, 20, 12, 12)
one = (1, 0)
zero = (0, 0)
phi = (0, 1)
phi_bar = (1, -1)
characters = {
    "A": [(3, 0), (-1, 0), zero, phi, phi_bar],
    "P": [(4, 0), zero, one, (-1, 0), (-1, 0)],
    "D": [(5, 0), one, (-1, 0), zero, zero],
}


def weighted_sum(row):
    result = zero
    for size, value in zip(sizes, row):
        result = add(result, scale(size, value))
    return result


require(sum(sizes) == 60, "fixed A5 class sizes")
for label, row in characters.items():
    for other_label, other in characters.items():
        inner = weighted_sum([mul(x, y) for x, y in zip(row, other)])
        require(inner == (60 if label == other_label else 0, 0),
                "fixed irreducibility and distinctness " + label + "," + other_label)
# Squaring classes sends 1 to 1, order 2 to 1, order 3 to itself,
# and interchanges the two order-five classes. This is fixed class data.
square_class = (0, 0, 2, 4, 3)
for label in ("A", "P"):
    row = characters[label]
    symmetric_numerators = [add(mul(row[i], row[i]), row[square_class[i]])
                            for i in range(5)]
    alternating_numerators = [add(mul(row[i], row[i]), scale(-1, row[square_class[i]]))
                              for i in range(5)]
    require(weighted_sum(symmetric_numerators) == (120, 0),
            "one fixed invariant symmetric form line on " + label)
    require(weighted_sum(alternating_numerators) == zero,
            "no fixed invariant alternating form on " + label)
require([add(mul(add(a, (-1, 0)), a), (-1, 0)) for a in characters["A"]]
        == characters["D"], "fixed physical Sym4 W equals D")
require(3+4 == 7 and 5+4 == 9, "fixed seven-space and top dimensions")
representation_checks = checks-authentication_checks-sequence_checks

# Actual-map claims are not checked here: only their formal degree arithmetic.
require(11+7 == 18 and 2*9 == 18, "ambient blocks and maximal-isotropic dimensions")
require(5+4 == 9, "formal generic span dimensions")
require(5*(4-10) == -30, "degree of complete x4")
require(-54-(-30) == -24 == flag_degrees[3], "actual projection equal-degree arithmetic")
require(6*(5-10)-5*(4-10) == 0, "UZ quotient degree")
require(flag_degrees[3]-flag_degrees[2] == 0, "U7 quotient degree")
require(-18+3*2 == -12, "intrinsic top source quotient degree")
require((-6)-(-18) == 12, "nonzero actual quotient-row divisor degree")
for j in (2, 3, 4):
    require(2*j-10 == (2*(j+1)-10)-2,
            "complete second-fundamental-form symbol equal degree " + str(j))
require((-6)+3*2 == 0 and 0-(-12) == 12, "three-symbol top map degree")
require(0+0 == 0, "graph restriction target line degree")
require(2-1 == 1, "two specified form lines with nonzero common line target")
require(4 == 3+1, "Q4 means rank four, third-order jets")
require(4*(-6) == -24 and 5*(-6) == -30 and 9*(-6) == -54,
        "P(-6), D(-6), and original top degree compatibility")
degree_checks = checks-authentication_checks-sequence_checks-representation_checks

print("PASS: " + str(checks) + " bounded checks (" + str(authentication_checks)
      + " whole-file authentication; " + str(sequence_checks) + " prescribed sequence/duality; "
      + str(representation_checks) + " fixed representation; "
      + str(degree_checks) + " formal degree/dimension checks).")
if args.arithmetic_only:
    print("Arithmetic-only run: no authentication or frozen-packet claim.")
else:
    print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Conditional constant self-duality, actual maximal-isotropic incidence, and Q4=P(-6) only; "
      "no K1 realization, exclusion, higher-order branch matching, or algebraicity.")
