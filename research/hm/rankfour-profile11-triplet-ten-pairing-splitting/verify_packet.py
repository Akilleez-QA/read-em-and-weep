#!/usr/bin/env python3
"""Whole-file authentication and fixed universal checks, not geometric certification."""
from collections import Counter
from pathlib import Path
from math import comb
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
PROOF_BYTES = 16304
PROOF_SHA256 = 'b233db763f8c7aa78174ae85629f28f00a373f6b78b3674602f96189f6cf3d2e'
SOURCES = [{'id': 'first-kernel-forward-closure',
  'pr': 1236,
  'ref': '092fc5f31dfaa5553ee5ea687f175ecba1878a2a',
  'path': 'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md',
  'local_path': 'inputs/first-kernel-forward-closure.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 18052,
  'sha256': '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
  'git_blob_sha1': 'f77cfb52743be86e46e0c40570ec036e69aebaf3',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/092fc5f31dfaa5553ee5ea687f175ecba1878a2a/research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md'},
 {'id': 'first-kernel-span',
  'pr': 1235,
  'ref': '7152e94cedbab18036b5e032d4e97934c4c061b7',
  'path': 'research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md',
  'local_path': 'inputs/first-kernel-span.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 11977,
  'sha256': '66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9',
  'git_blob_sha1': 'b846834f8451e7202721d9669b43df294f7a96d3',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/7152e94cedbab18036b5e032d4e97934c4c061b7/research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md'},
 {'id': 'kernel-two-exclusion',
  'pr': 1226,
  'ref': 'c565bd8b5b65829e99bdd96a7c5f076b01050465',
  'path': 'research/hm/rankfour-profile11-triplet-simultaneous-kernel-two-exclusion/PROOF.md',
  'local_path': 'inputs/kernel-two-exclusion.md',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'utf8_bytes': 13703,
  'sha256': '0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa',
  'git_blob_sha1': 'cb46875b07d8d79e82aebe980685c418d975d87b',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/c565bd8b5b65829e99bdd96a7c5f076b01050465/research/hm/rankfour-profile11-triplet-simultaneous-kernel-two-exclusion/PROOF.md'},
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
# FREEZE_CONSTANTS_END

require(PROOF_SHA256 is not None and SOURCES is not None, "immutable source authentication and proof freeze remain pending")
proof = (ROOT / "PROOF.md").read_bytes()
require(len(proof) == PROOF_BYTES, "entire frozen proof byte count")
require(sha256(proof) == PROOF_SHA256, "entire frozen proof SHA256")
manifest = json.loads((ROOT / "INPUTS.json").read_text())
require(manifest == {"schema": 1, "sources": SOURCES}, "exact immutable four-source metadata")
require(len(SOURCES) == 4, "four complete direct originals")
for entry in SOURCES:
    require(len(entry["ref"]) == 40 and entry["pr"] > 0, "immutable published source pin: " + entry["id"])
    data = (ROOT / entry["local_path"]).read_bytes()
    require(len(data) == entry["utf8_bytes"], "entire source byte count: " + entry["id"])
    require(sha256(data) == entry["sha256"], "entire source SHA256: " + entry["id"])
    require(git_blob(data) == entry["git_blob_sha1"], "entire source Git blob: " + entry["id"])
authentication_checks = checks

# Fixed physical representation ring: no actual coefficient system is sampled.
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
for n in range(1, 10):
    value = subtract(times_w(sym[n]), sym[n-1])
    require(all(v >= 0 for v in value.values()), "nonnegative fixed Sym character " + str(n+1))
    require(dimension(value) == n+2, "fixed Sym dimension " + str(n+1))
    sym.append(value)
require(sym[2] == {"A": 1}, "physical Sym2 is A")
require(sym[4] == {"D": 1}, "physical Sym4 is D")
require(sym[10] == {"A": 1, "V": 1, "D": 1}, "complete degree-ten coefficient character")
aa = subtract(times_w(times_w({"A": 1})), {"A": 1})
require(aa == {"1": 1, "A": 1, "D": 1}, "A tensor A from A=W tensor W-1")
require(aa.get("1", 0) == 1, "unique invariant of bidegree (2,2)")
C = {"A": 2, "V": 2, "D": 1, "P": 1}
S = subtract(C, {"V": 1})
Z = sym[10]
kappa = subtract(C, Z)
c7 = subtract(S, Z)
require(S == {"A": 2, "V": 1, "D": 1, "P": 1}, "constant eighteen-space character")
require(kappa == {"A": 1, "V": 1, "P": 1}, "constant original annihilator character")
require(c7 == {"A": 1, "P": 1}, "actual seven-space character after proved splitting")
character_checks = checks-authentication_checks

# Only universal order and dimension arithmetic, never actual instance ranks.
require(5+1 == 6 and 6+1 == 7, "two auxiliary forward-jet steps")
require(7+1 == 8, "seventh-jet annihilation imposes diagonal order eight")
require((10-8, 10-8) == (2, 2), "remaining bidegree after Delta eighth power")
require(8+2 == 10, "final determinant power ten")
require(10+1 == 11, "dimension of degree-ten scalar sections")
require(21-11 == 10 and 11 > 10, "zero pairing impossible in dimension twenty-one")
require(11+11 > 21, "two complete coefficient spans cannot annihilate each other")
require(dimension(C) == 21 and dimension(S) == 18, "retained ambient dimensions")
require(dimension(Z) == 11, "auxiliary coefficient dimension")
require(dimension(kappa) == 10, "canonical constant retraction kernel dimension")
require(dimension(c7) == 7, "canonical constant complement dimension")
require(11+10 == 21 and 11+7 == 18, "two actual direct-sum dimension balances")
require(10-7 == 3, "remaining constant quotient dimension")
for k in range(11):
    require(comb(10, k) > 0, "nonzero universal complementary-monomial coefficient " + str(k))
require(9+1 == 10 and (9+1)*(9-10) == -10, "complete ninth-jet rank and degree")
require(8+1 == 9 and (8+1)*(8-10) == -18, "complete eighth-jet rank and degree")
require(10+7 == 17 and 9+7 == 16, "two actual terminal direct-sum ranks")
require(2*9-10 == 8 and 2*10-10-2 == 8, "last complete-jet derivative scalar degrees")
require(10-9 == 1, "last auxiliary forward derivative rank")
arithmetic_checks = checks-authentication_checks-character_checks

print("PASS: " + str(checks) + " bounded checks (" + str(authentication_checks) + " whole-file authentication; " + str(character_checks) + " universal character; " + str(arithmetic_checks) + " fixed dimension/order checks).")
print("Entire frozen proof SHA256: " + PROOF_SHA256)
print("Conditional perfect pairing, projected completeness, and canonical constant splitting and terminal jet identifications only; original completeness is prior work; no K1 exclusion or realization.")
