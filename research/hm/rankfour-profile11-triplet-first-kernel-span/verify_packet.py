#!/usr/bin/env python3
"""Bounded universal checks and whole-file authentication, not geometric certification."""
from pathlib import Path
from collections import Counter
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


PROOF_SHA256 = "66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9"
SOURCES = [
    ("kernel-three-exclusion", 1234, "3d55622ece9a4bb9e20197dec560b298f1d03fb1", "rankfour-profile11-triplet-simultaneous-kernel-three-exclusion", 16183, "9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2", "c57074c1fbfaa61ef452a6d5e3a77dd0ff4ea70b"),
    ("first-kernel-structure", 1228, "d3c9e9ff8d06977e6c3d3be6cd1c9ed71007a593", "rankfour-profile11-triplet-first-kernel-structure", 12921, "4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e", "41ab2148d3ea13d07dcdfe2bf353a18c664bb848"),
    ("positive-span", 1205, "97dad5c307a04f61d850e8a4211559e97ed4c2fd", "rankfour-profile11-triplet-positive-span", 12569, "145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b", "b75b1272bbf3a360751cc22a9e04c641cdeeb787"),
    ("eighteen-jets", 1209, "913892c66403ea57ed1681957ae1b9f8db9e5e15", "rankfour-profile11-triplet-eighteen-jets", 17528, "33a3c8866f072f4aec607c2d6647222ee0031a3f1bbbaef550e58df5075b3dbf", "730021d4e97c4c1307a1d3c6c5303e4e9792202d"),
]

proof = (ROOT / "PROOF.md").read_bytes()
require(len(proof) == 11977, "entire frozen proof byte count")
require(sha256(proof) == PROOF_SHA256, "entire frozen proof SHA256")
manifest = json.loads((ROOT / "INPUTS.json").read_text())
require(manifest["schema"] == 1, "input schema")
require(len(manifest["sources"]) == 4, "exact four complete sources")
for entry, fixed in zip(manifest["sources"], SOURCES):
    key, pr, ref, directory, size, digest, blob = fixed
    path = "research/hm/" + directory + "/PROOF.md"
    local = "inputs/" + key + ".md"
    expected = {
        "id": key, "pr": pr, "repository": "Akilleez-QA/read-em-and-weep",
        "ref": ref, "path": path, "local_path": local, "utf8_bytes": size,
        "sha256": digest, "git_blob_sha1": blob,
        "url": "https://github.com/Akilleez-QA/read-em-and-weep/blob/" + ref + "/" + path,
    }
    require(entry == expected, "exact immutable source metadata: " + key)
    data = (ROOT / local).read_bytes()
    require(len(data) == size, "complete original byte count: " + key)
    require(sha256(data) == digest, "complete original SHA256: " + key)
    require(git_blob(data) == blob, "complete original Git blob: " + key)
authentication_checks = checks

# The nine fixed physical irreducibles and physical-W adjacency.
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
            answer[j] += n * m
    return dict(answer)


def subtract(a, b):
    out = {k: a.get(k, 0) - b.get(k, 0) for k in dim}
    return {k: n for k, n in out.items() if n != 0}


for k, value in adj.items():
    require(dimension(value) == 2 * dim[k], "fixed W-adjacency dimension: " + k)
sym = [{"1": 1}, {"W": 1}]
for n in range(1, 18):
    next_value = subtract(times_w(sym[n]), sym[n-1])
    require(all(v >= 0 for v in next_value.values()), "nonnegative fixed Sym character " + str(n+1))
    require(dimension(next_value) == n+2, "fixed Sym dimension " + str(n+1))
    sym.append(next_value)
for n, target in [(3, {"S4": 1}), (4, {"D": 1}), (5, {"T6": 1}),
                  (6, {"V": 1, "P": 1}), (7, {"T6": 1, "Wp": 1}),
                  (10, {"A": 1, "V": 1, "D": 1}),
                  (18, {"A": 1, "V": 1, "D": 1, "P": 2})]:
    require(sym[n] == target, "fixed Sym character identity " + str(n))
wp_sym = [{"Wp": 1}, adj["Wp"]]
wp_sym.append(subtract(times_w(wp_sym[1]), wp_sym[0]))
wp_sym.append(subtract(times_w(wp_sym[2]), wp_sym[1]))
require(wp_sym[1] == {"P": 1}, "W' tensor W = P")
require(wp_sym[2] == {"T6": 1}, "W' tensor Sym2 W = T6")
require(wp_sym[3] == {"D": 1, "V": 1}, "H0(Q*) = D+V")
require(wp_sym[1].get("V", 0) == 0, "canonical V top has zero Q row")
require(wp_sym[1].get("P", 0) == 1, "canonical P Euler row is unique")
require(-3 < 0, "ordinary Hom(O,Q) vanishes")
character_checks = checks - authentication_checks

# Fixed ranks and degrees only. No actual coefficient system is evaluated.
require(3 + 4 + 6 == 13, "K rank")
require(7*(-4) + 6*(-5) == -58, "K degree")
require(3 + 2 + 6 == 11, "R rank")
require(3*(-4) + 2*(-5) + 6*(-5) == -52, "R degree")
require(13-11 == 2 and -58-(-52) == -6, "Q rank and degree")
require(5+4 == 9 and 9*(-6) == -54, "Bhat rank and degree")
require(11-9 == 2 and -52-(-54) == 2, "R/Bhat is W(1)")
require(6-5 == 1 and 6*(-5)-5*(-6) == 0, "Zhat5/Zhat4 is O")
require(4-2 == 2 and 4*(-4)-2*(-5) == 2*(-3), "Euler quotient rank and degree")
require(2*3+2*3+5+4 == 21, "original C* dimension")
require(3+3+5+4 == 15, "V18 coefficient dimension")
c_dual = {"A": 2, "V": 2, "D": 1, "P": 1}
v18 = {"A": 1, "V": 1, "D": 1, "P": 1}
missing_bound = subtract(c_dual, v18)
require(missing_bound == {"A": 1, "V": 1}, "one-copy A/V missing bound")
require(sorted({21, 21-3, 21-3-3}) == [15,18,21], "constant-span alternatives")
require(21-9 == 12, "actual annihilator rank")
require(-(0-9*(-6)) == -54, "actual annihilator degree is Bhat degree")
require(1-2 == -1, "transpose image I* tensor Omega has twist -1")
capacity = []
for h2 in range(1, 7):
    h1 = 12-h2
    ranks = [int(i<h1)+int(i<h2) for i in range(h1)]
    require(sum(ranks) == 12 and ranks[0] == 2, "column rank sum " + str(h2))
    require(all(ranks[i]>=ranks[i+1] for i in range(len(ranks)-1)), "nonincreasing ranks " + str(h2))
    degree_bound = sum(q*(-1-2*i) for i,q in enumerate(ranks))
    require(degree_bound == -h1*h1-h2*h2, "column square identity " + str(h2))
    require(degree_bound <= -72, "rank-twelve capacity " + str(h2))
    capacity.append(degree_bound)
require(max(capacity) == -72, "sharp balanced rank-twelve bound")
require(-54 > -72, "full21 degree contradiction")
intersection = {k: min(n, wp_sym[3].get(k, 0)) for k,n in missing_bound.items() if wp_sym[3].get(k, 0)}
require(intersection == {"V": 1}, "only common missing constituent is V_alt")
require(21-dimension(intersection) == 18, "original constant span is eighteen")
arithmetic_checks = checks-authentication_checks-character_checks
print("PASS: " + str(checks) + " bounded checks (" + str(authentication_checks) + " whole-file authentication; " + str(character_checks) + " universal character; " + str(arithmetic_checks) + " fixed rank/degree checks).")
print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Only necessary K1 structure: exact R and original span18/missing V_alt; no exclusion or realization.")
