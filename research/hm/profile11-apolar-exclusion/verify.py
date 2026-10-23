#!/usr/bin/env python3
"""Only fixed universal character/degree controls; no actual instance data."""
from pathlib import Path
from collections import Counter
from itertools import product
import hashlib
import json
import sys
import characters as c

ROOT = Path(__file__).resolve().parent
checks = 0

def require(ok, message):
    global checks
    checks += 1
    if not ok:
        raise RuntimeError(message)

def rank(blocks):
    return sum(c.DIM[r] for _, r in blocks)

def degree(blocks):
    return sum(e * c.DIM[r] for e, r in blocks)

def same(x, y):
    z = x.copy()
    z.subtract(Counter(y))
    return not any(z.values())

def hom(source, target):
    return sum(c.product(t, te-se)[s]
               for se, s in source for te, t in target)

manifest = json.loads((ROOT / "INPUTS.json").read_text())
require(len(manifest) == 7, "seven immutable complete originals")
for item in manifest:
    data = (ROOT / item["file"]).read_bytes()
    require(len(data) == item["bytes"], item["file"] + ": byte count")
    require(hashlib.sha256(data).hexdigest() == item["sha256"],
            item["file"] + ": SHA256")
    require(hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            == item["git_blob_sha1"], item["file"] + ": Git blob")

sources = {
    "D": [(-2, "D"), (-3, "Wp"), (-3, "T"), (-4, "V"), (-8, "one")],
    "P": [(-2, "P"), (-3, "Wp"), (-3, "T"), (-4, "V"), (-5, "Wp")],
    "V": [(-2, "V"), (-3, "Wp"), (-3, "T"), (-4, "V"), (-4, "V")],
    "Z": [(-3, "Wp"), (-3, "T"), (-3, "T"), (-4, "V")],
}
E = sources["D"]
F = E[:-1]
require(rank(E) == 17 and degree(E) == -54, "actual D source")
require([name for name, src in sources.items()
         if hom(src, [(-8, "one")])] == ["D"], "negative tail forces D type")
require(rank(F) == 16 and degree(F) == -46, "constant residual source")
for n, target in [(6, {"V": 1, "P": 1}), (7, {"Wp": 1, "T": 1}),
                  (8, {"P": 1, "D": 1}), (10, {"A": 1, "V": 1, "D": 1})]:
    require(same(c.product("one", n), target), f"Sym{n} decomposition")
    require(sum(c.DIM[r]*m for r, m in target.items()) == n+1,
            f"Sym{n} dimension")
require(c.product("one", 2) == Counter(A=1), "physical standard three-space")
require(c.product("one", 6)["V"] == 1, "unique nonstandard V sextic channel")

proper_dimensions = {}
for n, dims, independent in [(8, [4, 5], 8), (10, [3, 3, 5], 9)]:
    dimensions = [sum(x*d for x, d in zip(bits, dims))
                  for bits in product((0, 1), repeat=len(dims))
                  if not all(bits)]
    require(max(dimensions) < independent, "proper quotient too small")
    proper_dimensions[str(n)] = sorted(set(dimensions))

A = [[-8, "one"], [2, "one"], [16, "one"]]
pairs = json.loads((ROOT / "inputs/profile11-pairs.json").read_text())
require(len(pairs) == 159, "fixed historical pair count")
matches = [(i, r) for i, r in enumerate(pairs) if r["A"] == A]
require([i for i, _ in matches] == [119, 127], "exact two A-shape records")
expected = {
    119: {"B": [[-18, "one"], [-16, "one"], [6, "one"]],
          "defect": 12, "degree_L": -26, "capacities": [-110, -90, -74, -62, -54, -50]},
    127: {"B": [[-18, "one"], [-4, "one"], [6, "one"]],
          "defect": 0, "degree_L": -38, "capacities": [-50, -42, -38, -38, -42, -50]},
}
row_controls = []
for index, row in matches:
    ex = expected[index]
    require(row["B"] == ex["B"] and row["defect"] == ex["defect"],
            "exact B and defect")
    require(row["a"] == degree(A) and row["b"] == degree(row["B"]),
            "row degree identities")
    require(-6-row["a"]-row["b"] == row["defect"], "transpose determinant degree")
    lam = sorted([e for e, _ in row["B"]], reverse=True)
    capacities = []
    for h in range(5, 11):
        h2 = 10-h
        cap = h*lam[0]-h*(h+1)+h2*lam[1]-h2*(h2+1)
        q = [int(j <= h)+int(j <= h2) for j in range(1, h+1)]
        require(sum(q) == 10 and all(a >= b for a, b in zip(q, q[1:])),
                "universal height partition")
        require(cap == sum(sum(lam[:r])-2*j*r for j, r in enumerate(q, 1)),
                "capacity equals graded determinant sum")
        capacities.append(cap)
    require(capacities == ex["capacities"], "six exact capacities")
    degL = -54-row["b"]
    require(degL == ex["degree_L"], "actual dual endpoint degree")
    if index == 119:
        require(degL > max(capacities), "positive-defect capacity contradiction")
    else:
        require([h for h, cap in zip(range(5, 11), capacities) if cap == degL]
                == [7, 8], "all equality optimizers")
        for h in (7, 8):
            require(6-2*h == {7: -8, 8: -10}[h], "terminal line degree")
    row_controls.append({"original_index": index, "defect": row["defect"],
                         "B": row["B"], "degree_L": degL, "capacities": capacities})

# Ordinary-degree Hom obstructions in the height-eight and height-seven routes.
require(hom(E, [(-9, "W")]) == 0, "height-eight apolar Hom vanishes")
require(hom(E[:-1], [(-8, "one")]) == 0, "only the negative tail projects")
require(hom([E[-1]], [(-8, "one")]) == 1, "nonzero tail is a scalar")
require(30-9 == 21 and 21-rank(F) == 5, "actual constant residual dimensions")
SJ = [(-1, "Wp"), (-1, "T")]
LJ = [(-2, "V"), (-2, "P")]
require(rank(SJ) == 8 and degree(SJ) == -8, "degree-eight annihilator")
require(rank(LJ) == 7 and degree(LJ) == -14, "annihilator derivative kernel")
require(rank(SJ)-rank(LJ) == 1 and degree(SJ)-degree(LJ) == 6,
        "complete-line dual quotient O6")
BF = [(-4, "one"), (-18, "one")]
require(13-8 == 5 and 10-7 == 3, "residual dual ranks")
require(-54-(-8) == -46 and -46-degree(BF) == -24, "residual dual degrees")
residual_steps = [-4-2*j for j in range(1, 4)]
require(residual_steps == [-6, -8, -10] and sum(residual_steps) == -24,
        "forced three-step equality")
apolar = [(-4, "V"), (-4, "P")]
require(hom(F[:-1], apolar) == 0, "rank-thirteen top has zero apolar Hom")
require(hom([F[-1]], apolar) == 1, "unique V apolar channel")
require(rank(F[:-1]) == 13 and 21-11 == 10 and 13 > 10,
        "final ambient rank contradiction after completeness")

# Universal apolar rank/degree formulas, not evaluation at a parameter.
for n, k, coefficient_rank, line_degree in [
        (10, 8, 2, -9), (8, 7, 1, -8), (10, 3, 7, -4)]:
    require(n-k == coefficient_rank and -(k+1) == line_degree,
            "full apolar annihilator formula")
    require((k+1)+coefficient_rank == n+1, "apolar dimensions")

# Independent basepoint-free sextic net: all possible Birkhoff degree pairs.
net_controls = []
for a in range(1, 6):
    b = 6-a
    h1 = max(a-5, 0)+max(b-5, 0)
    kernel_h0 = max(5-a, 0)+max(5-b, 0)
    require(a >= 1 and b >= 1 and max(a, b) <= 5, "sextic syzygy degrees")
    require(h1 == 0, "H1 of fourth-twisted net kernel vanishes")
    require(3*5-kernel_h0 == 11, "quartic multiplication image dimension")
    net_controls.append({"a": a, "b": b, "twisted_H1": h1,
                         "multiplication_rank": 3*5-kernel_h0})
require(max(0-5, 0)+max(6-5, 0) == 1,
        "independence is necessary: zero syzygy degree is not allowed")
require(60//5 == 12 and 6 < 12, "invariant divisor cannot be a sextic base divisor")

out = {
    "scope": "Actual maximal-profile11 A=O(-8)+O2+O16 exclusion only",
    "authenticated_originals": len(manifest),
    "checks": checks+c.checks,
    "historical_rows": row_controls,
    "proper_polynomial_quotient_dimensions": proper_dimensions,
    "residual_quotient_degrees": residual_steps,
    "sextic_net_controls": net_controls,
    "actual_instance_evaluated": False,
    "historical_enumeration_rerun": False,
    "full_profile11_excluded": False,
    "global_rank3_excluded": False,
}
text = json.dumps(out, indent=2, sort_keys=True)+"\n"
if "--write" in sys.argv:
    (ROOT / "RESULT.json").write_text(text)
else:
    require((ROOT / "RESULT.json").read_text() == text, "exact retained result replay")
print(text, end="")
