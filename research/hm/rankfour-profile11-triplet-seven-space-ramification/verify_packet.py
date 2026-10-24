#!/usr/bin/env python3
"""Whole-file authentication and fixed universal checks only; not geometric certification."""
from collections import Counter
from pathlib import Path
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
PROOF_BYTES = 20687
PROOF_SHA256 = '25388c411411f7304afc2dc7ad6695af5a931e852ba138c45cfb7a6f708d84e3'
SOURCES = [{'id': 'ten-pairing-splitting',
  'pr': 1237,
  'ref': '2dfb37187cf61c59b1277a4492881c0fd42de44f',
  'path': 'research/hm/rankfour-profile11-triplet-ten-pairing-splitting/PROOF.md',
  'local_path': 'inputs/ten-pairing-splitting.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 16304,
  'sha256': 'b233db763f8c7aa78174ae85629f28f00a373f6b78b3674602f96189f6cf3d2e',
  'git_blob_sha1': 'e41b654ff6edba56d5a071811f19d4db4346681c',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/2dfb37187cf61c59b1277a4492881c0fd42de44f/research/hm/rankfour-profile11-triplet-ten-pairing-splitting/PROOF.md'},
 {'id': 'first-kernel-forward-closure',
  'pr': 1236,
  'ref': '092fc5f31dfaa5553ee5ea687f175ecba1878a2a',
  'path': 'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md',
  'local_path': 'inputs/first-kernel-forward-closure.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 18052,
  'sha256': '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
  'git_blob_sha1': 'f77cfb52743be86e46e0c40570ec036e69aebaf3',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/092fc5f31dfaa5553ee5ea687f175ecba1878a2a/research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md'},
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
CORE_FILES = ["PROOF.md", "INPUTS.json", "verify_packet.py", "inputs/ten-pairing-splitting.md", "inputs/first-kernel-forward-closure.md", "inputs/shared-d.md", "README.md", "PROVENANCE.md"]
# FREEZE_CONSTANTS_END

proof = (ROOT / "PROOF.md").read_bytes()
require(len(proof) == PROOF_BYTES, "entire frozen proof byte count")
require(sha256(proof) == PROOF_SHA256, "entire frozen proof SHA256")
manifest = json.loads((ROOT / "INPUTS.json").read_text())
require(manifest == {"schema": 1, "sources": SOURCES}, "exact immutable three-source manifest")
require(len(SOURCES) == 3, "three complete direct originals")
for entry in SOURCES:
    require(len(entry["ref"]) == 40 and entry["pr"] > 0, "immutable published source pin: " + entry["id"])
    data = (ROOT / entry["local_path"]).read_bytes()
    require(len(data) == entry["utf8_bytes"], "entire source byte count: " + entry["id"])
    require(sha256(data) == entry["sha256"], "entire source SHA256: " + entry["id"])
    require(git_blob(data) == entry["git_blob_sha1"], "entire source Git blob: " + entry["id"])
frozen = json.loads((ROOT / "FROZEN.json").read_text())
require(frozen["schema"] == 1 and sorted(frozen["files"]) == sorted(CORE_FILES), "exact eight-file core freeze")
require(frozen["proof_utf8_bytes"] == PROOF_BYTES and frozen["proof_sha256"] == PROOF_SHA256, "proof freeze agreement")
for name in CORE_FILES:
    require(sha256((ROOT / name).read_bytes()) == frozen["files"][name], "entire frozen core file: " + name)
authentication_checks = checks

# Fixed physical representation ring, not an actual coefficient system.
dim = {"1": 1, "W": 2, "Wp": 2, "A": 3, "V": 3, "S4": 4, "P": 4, "D": 5, "T6": 6}
adj = {
    "1": {"W": 1}, "W": {"1": 1, "A": 1},
    "A": {"W": 1, "S4": 1}, "S4": {"A": 1, "D": 1},
    "D": {"S4": 1, "T6": 1}, "T6": {"D": 1, "V": 1, "P": 1},
    "V": {"T6": 1}, "P": {"T6": 1, "Wp": 1}, "Wp": {"P": 1},
}

def dimension(c):
    return sum(dim[k] * v for k, v in c.items())

def times_w(c):
    answer = Counter()
    for k, n in c.items():
        for j, m in adj[k].items():
            answer[j] += n*m
    return dict(answer)

def subtract(a, b):
    return {k: a.get(k, 0)-b.get(k, 0) for k in dim if a.get(k, 0) != b.get(k, 0)}

for k, value in adj.items():
    require(dimension(value) == 2*dim[k], "fixed W adjacency dimension: " + k)
sym = [{"1": 1}, {"W": 1}]
for n in range(1, 12):
    value = subtract(times_w(sym[n]), sym[n-1])
    require(all(v >= 0 for v in value.values()), "nonnegative universal Sym character " + str(n+1))
    require(dimension(value) == n+2, "universal Sym dimension " + str(n+1))
    sym.append(value)
require(sym[4] == {"D": 1}, "physical Sym4 is D")
require(sym[7] == {"Wp": 1, "T6": 1}, "degree-seven alternate-doublet model")
require(sym[9] == {"S4": 1, "T6": 1}, "degree-nine original first-jet Hom vanishing")
require(sym[12] == {"1": 1, "A": 1, "D": 1, "P": 1}, "degree-twelve invariant character")
require(sym[9].get("W", 0) == 0, "no map O(-18) to W(-9)")
require(sym[4].get("A", 0)+sym[4].get("P", 0) == 0, "no split O(-4) summand maps into C7 star")
require(sym[7].get("Wp", 0) == 1, "one-dimensional model inclusion Hom")
require(sym[12].get("1", 0) == 1, "one-dimensional invariant extension space and invariant section line")
require(dim["A"]+dim["P"] == 7, "constant seven-space dimension")
character_checks = checks-authentication_checks

# Fixed orbit and arithmetic checks only; no orbit points or actual ranks sampled.
stabilizer_orders = (1, 2, 3, 5)
orbit_sizes = tuple(60 // n for n in stabilizer_orders)
require(orbit_sizes == (60, 30, 20, 12), "cyclic A5 stabilizer orbit arithmetic")
require(min(orbit_sizes) == 12, "minimum nonempty invariant-divisor degree")
require(12 <= 18 < 20 and 2*12 > 18, "only possible degree-at-most-eighteen invariant base divisor")
require(21-11 == 10 and 15 > 10, "original Y0 cannot annihilate auxiliary eleven-space")
require(18-15 == 3 and 18-13 == 5, "annihilator ranks L3 and L5")
require(2*(-9)-18 == -36, "degree-zero determinant for L3 direct sum")
require(-9-(-18) == 9 and -6-(-18) == 12, "quotient and forbidden-lift degrees of y_Z")
require(10-7 == 3 and 2+7 == 9 < 10, "complete jet-annihilator rank and mixed diagonal order")
require(2*2-10 == -6, "complete x2 over x1 quotient degree")
require(3*(-8) == -24 and 2*(-17) == -34, "x2 and first-principal-parts degrees")
require(-46-(-24-34) == 12, "rank-five determinant divisor degree")
require(-46-(-24) == -22 and 5-3 == 2, "Q2 degree and rank")
require(-22-(-18) == -4, "Q2 over value-line quotient degree")
require(-22-(-34) == 12, "first-jet defect inside Q2")
require(sum(18-2*i for i in range(7)) == 84, "principal-parts full Wronskian determinant degree")
require(7*(18-6) == 84 and 84//6-12 == 2, "Wronskian budget for additional defect")
require(2 < 12, "invariance rules out every positive additional defect")
require(-18-(-4) == -14 and 14-2 == 12, "extension and Serre-duality degrees")
require(-11-(-18) == 7 and 7 < 12, "universal alternate-doublet model has no possible invariant zeros")
require(2*(-11)-(-18) == -4, "universal alternate-doublet model quotient degree")
require(2*(-11) == -22, "forced alternate-doublet bundle degree")
require(6*12 == 72 and 84-72 == 12 and 7*12 == 84, "full Wronskian divisor multiplicity")
minimal = (0, 2, 3, 4, 5, 6, 7)
forced = (0, 2, 3, 4, 5, 6, 8)
ordinary = tuple(range(7))
require(sum(a-i for i,a in enumerate(minimal)) == 6, "minimum weight with a0 zero and a1 two")
require(sum(a-i for i,a in enumerate(forced)) == 7, "forced exceptional vanishing-sequence weight")
require(tuple(a-b for a,b in zip(forced,minimal)) == (0,0,0,0,0,0,1), "single final excess in exceptional sequence")
require(all(forced[i] < forced[i+1] for i in range(6)), "strict increase of exceptional sequence")
require(sum(a-i for i,a in enumerate(ordinary)) == 0, "ordinary zero-weight sequence")
arithmetic_checks = checks-authentication_checks-character_checks

print("PASS: " + str(checks) + " bounded checks (" + str(authentication_checks) + " whole-file authentication; " + str(character_checks) + " universal character; " + str(arithmetic_checks) + " fixed orbit/degree/ramification checks).")
print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Conditional projected seven-space first-jet saturation and ramification only; no occurrence, K1 exclusion, further jet-defect classification, or algebraicity.")
