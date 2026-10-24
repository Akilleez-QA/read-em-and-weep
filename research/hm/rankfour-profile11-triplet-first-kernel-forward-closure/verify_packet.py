#!/usr/bin/env python3
"""Fixed universal checks and complete-file authentication, not geometric certification."""
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

# Replaced with immutable complete-file constants when this proof is frozen.
PROOF_BYTES = 18052
PROOF_SHA256 = "90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137"
SOURCES = [{'git_blob_sha1': 'b846834f8451e7202721d9669b43df294f7a96d3',
  'id': 'first-kernel-span',
  'local_path': 'inputs/first-kernel-span.md',
  'path': 'research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md',
  'pr': 1235,
  'ref': '7152e94cedbab18036b5e032d4e97934c4c061b7',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'sha256': '66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/7152e94cedbab18036b5e032d4e97934c4c061b7/research/hm/rankfour-profile11-triplet-first-kernel-span/PROOF.md',
  'utf8_bytes': 11977},
 {'git_blob_sha1': 'c57074c1fbfaa61ef452a6d5e3a77dd0ff4ea70b',
  'id': 'kernel-three-exclusion',
  'local_path': 'inputs/kernel-three-exclusion.md',
  'path': 'research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md',
  'pr': 1234,
  'ref': '3d55622ece9a4bb9e20197dec560b298f1d03fb1',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'sha256': '9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/3d55622ece9a4bb9e20197dec560b298f1d03fb1/research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md',
  'utf8_bytes': 16183},
 {'git_blob_sha1': 'b75b1272bbf3a360751cc22a9e04c641cdeeb787',
  'id': 'positive-span',
  'local_path': 'inputs/positive-span.md',
  'path': 'research/hm/rankfour-profile11-triplet-positive-span/PROOF.md',
  'pr': 1205,
  'ref': '97dad5c307a04f61d850e8a4211559e97ed4c2fd',
  'repository': 'Akilleez-QA/read-em-and-weep',
  'sha256': '145a8b2607ac5d888de52aa75ce4271fb8426a63f5123841f356a4025354fc6b',
  'url': 'https://github.com/Akilleez-QA/read-em-and-weep/blob/97dad5c307a04f61d850e8a4211559e97ed4c2fd/research/hm/rankfour-profile11-triplet-positive-span/PROOF.md',
  'utf8_bytes': 12569}]

proof = (ROOT / "PROOF.md").read_bytes()
require(len(proof) == PROOF_BYTES, "entire frozen proof byte count")
require(sha256(proof) == PROOF_SHA256, "entire frozen proof SHA256")
manifest = json.loads((ROOT / "INPUTS.json").read_text())
require(manifest == {"schema": 1, "sources": SOURCES}, "exact immutable three-source metadata")
for entry in SOURCES:
    data = (ROOT / entry["local_path"]).read_bytes()
    require(len(data) == entry["utf8_bytes"], "entire source byte count: " + entry["id"])
    require(sha256(data) == entry["sha256"], "entire source SHA256: " + entry["id"])
    require(git_blob(data) == entry["git_blob_sha1"], "entire source Git blob: " + entry["id"])
authentication_checks = checks

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
    return {k: a.get(k, 0)-b.get(k, 0) for k in dim if a.get(k, 0)!=b.get(k, 0)}

for k, value in adj.items():
    require(dimension(value) == 2*dim[k], "fixed W adjacency dimension: "+k)
sym = [{"1": 1}, {"W": 1}]
for n in range(1, 12):
    value = subtract(times_w(sym[n]), sym[n-1])
    require(all(v>=0 for v in value.values()), "nonnegative fixed Sym character "+str(n+1))
    require(dimension(value)==n+2, "fixed Sym dimension "+str(n+1))
    sym.append(value)
require(adj["A"] == {"W": 1, "S4": 1}, "Euler Hom multiplicity one")
for n in range(4):
    require(sym[n].get("Wp", 0)==0, "no rank-one Q image through degree "+str(n))
require(sym[3] == {"S4": 1}, "zero W(5) to O(8) row")
require(sym[4] == {"D": 1}, "zero internal V row")
require(sym[8] == {"P": 1, "D": 1}, "zero equivariant extension of O(16) by O(6)")
require(sym[11] == {"W": 1, "S4": 1, "T6": 1}, "unique gradient row")
require(sym[12] == {"1": 1, "A": 1, "D": 1, "P": 1}, "unique degree-twelve invariant")
require(sym[12].get("1", 0)==1, "internal row has one invariant degree-twelve parameter")
character_checks = checks-authentication_checks

# These verify only the stated rank/degree arithmetic, never actual instance ranks.
chain = [(9,-54),(11,-52),(13,-46),(15,-36),(17,-10),(18,0)]
quotients = [(2,2),(2,6),(2,10),(2,26),(1,10)]
for i,(rank,degree) in enumerate(quotients):
    require(chain[i+1][0]-chain[i][0]==rank, "forward quotient rank "+str(i))
    require(chain[i+1][1]-chain[i][1]==degree, "forward quotient degree "+str(i))
require(16+3==19 and -46+3*6==-28, "E19 rank and degree")
require(21-19==2 and 8+16==24, "full E19 derivative target")
require(19-2==17, "E19 backward-kernel rank")
require(17-3==14 and 15>14, "projected third row cannot vanish")
require(2*(-3)==-6 and 0-(-6)==6, "Q and constant quotient degrees")
require(6-2==4 and 4-(-3)==7, "Q derivative row degree")
require(6<12 and 7<12 and 10<12, "three invariant-divisor bounds")
require(16-3==13 and -46-0==-46, "E0 constant-kernel rank and degree")
require(19-3==16 and -28-(-36)==8, "internal actual line O(8)")
require(2*5-16==-6, "kernel of onto gradient row")
require(6-(-6)==12, "internal row degree twelve")
require(-36+18==-18 and 15+1==16, "hypothetical rank-one forward span")
require(18-16==2 and 2*(-9)==-18, "projected first-jet determinant equality")
require((-8)*(-1)-2==6, "transpose target of actual first-jet factor")
require(8-18<0 and 6-18<0, "two ordinary Hom vanishings in rank-one exclusion")
require(6+16-2*5==12, "coherent/saturated determinant defect")
require(0+1==1 and 12*1==12, "unit plus simple invariant-factor arithmetic")
require(-36+6+16+2*2==-10, "rank-seventeen degree")
require(18-17==1 and 0-(-10)==10, "annihilator scalar degree")
require(8-18<0 and 8-8==0, "terminal derivative rows")
arithmetic_checks = checks-authentication_checks-character_checks
print("PASS: "+str(checks)+" bounded checks ("+str(authentication_checks)+" whole-file authentication; "+str(character_checks)+" universal character; "+str(arithmetic_checks)+" fixed rank/degree checks).")
print("Entire frozen proof SHA256: "+PROOF_SHA256)
print("Conditional K1 forward closure and rank-one exclusion only; no K1 exclusion or realization.")
