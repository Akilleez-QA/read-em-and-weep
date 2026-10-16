"""Static dual-weight/request controls; no source, rank, or model execution."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SRC = HERE / "sources" / "detector-selection"
PIN = "e93cf712f9da4926a8450cc870ed45a7bfc379ab"
HASHES = {
    "selection.json": "54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d",
    "weighted-requests.json": "f256746fbfd0897fd4a5241e13715198004d277fec700b7ba5c4b3ace9bfe5e0",
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def read(name):
    raw = (SRC / name).read_bytes()
    need(hashlib.sha256(raw).hexdigest() == HASHES[name], "Frozen input drift: " + name)
    return json.loads(raw)


def clean(p):
    return {m: c for m, c in p.items() if c}


def linear(*parts):
    out = defaultdict(Fraction)
    for coefficient, p in parts:
        for m, c in p.items():
            out[m] += coefficient * c
    return clean(out)


def multiply(p, q):
    out = defaultdict(Fraction)
    for m, c in p.items():
        for n, d in q.items():
            out[tuple(a + b for a, b in zip(m, n))] += c * d
    return clean(out)


def elementary(k):
    return {tuple(int(i in subset) for i in range(4)): Fraction(1)
            for subset in combinations(range(4), k)}


def action(p, g):
    # Defined on formal dual polynomial monomial labels, not model/source data.
    out = {}
    for m, c in p.items():
        n = [0] * 4
        for i in range(4):
            n[g[i]] = m[i]
        out[tuple(n)] = c
    return out


def symmetrize(p):
    return linear(*[(Fraction(1, 24), action(p, g)) for g in permutations(range(4))])


selection = read("selection.json")
weighted = read("weighted-requests.json")
requests = weighted["requests"]
need(len(requests) == 32 and [r["id"] for r in requests] == list(range(32)), "Request order")
need(selection["I20"] == [[i, 0] for i in range(5, 11)]
     + [[i, 1] for i in range(15) if i != 5], "Twenty-map order")
for j, (i, b) in enumerate(selection["I20"]):
    r = requests[j]
    need(r["scalar_map"] == {"i": i, "b": b} and r["block"] == "Q^2", "Q-squared label")

ten = [(5, 0), (5, 1), (5, 4), (6, 0), (6, 1),
       (6, 2), (7, 1), (7, 2), (8, 3), (9, 4)]
for r, (i, k) in zip(requests[20:30], ten):
    need(r["scalar_map"] == {"i": i, "b": 0}
         and r["base_monomial"] == [k] and r["block"] == "v_k Q", "Ten labels")
for r, monomial in zip(requests[30:], ([0, 0], [1, 4])):
    need(r["scalar_map"] == {"i": 5, "b": 0}
         and r["base_monomial"] == monomial and r["block"] == "v_k v_l", "Last two labels")
    p = {tuple(t["dual_monomial"]): Fraction(t["coefficient"]) for t in r["terms"]}
    need(all(action(p, g) == p for g in permutations(range(4))), "Last weight not symmetric")

v = [elementary(k) for k in range(5)]
q = {(1, 1, 0, 0): Fraction(1), (0, 0, 1, 1): Fraction(1)}
q2 = multiply(q, q)
need(symmetrize(q) == linear((Fraction(1, 3), v[2])), "Mean Q")
expected_q2_mean = linear((Fraction(1, 3), multiply(v[2], v[2])),
                          (Fraction(-2, 3), multiply(v[1], v[3])),
                          (Fraction(8, 3), multiply(v[0], v[4])))
need(symmetrize(q2) == expected_q2_mean, "Mean Q squared")
for k in range(5):
    need(symmetrize(multiply(v[k], q)) == linear((Fraction(1, 3), multiply(v[k], v[2]))),
         "Mean v_k Q")
need(symmetrize(linear((1, q2), (-1, expected_q2_mean))) == {}, "Centered square")

retained = requests[:30]
terms = sum(len(r["terms"]) for r in retained)
unique = {(r["scalar_map"]["i"], r["scalar_map"]["b"], tuple(t["laurent_exponents"]))
          for r in retained for t in r["terms"]}
need((terms, len(unique)) == (122, 116), "Retained request counts")
need(all(value is False for value in weighted["gates"].values()), "Frozen source gate drift")

derived = {
    "schema": "remaining-permutation-sector-weighted-requests-v1",
    "source_commit": PIN,
    "source_weighted_requests_sha256": HASHES["weighted-requests.json"],
    "source_selection_sha256": HASHES["selection.json"],
    "normalization": weighted["normalization"],
    "comparison": weighted["comparison"],
    "scalar_map_convention": weighted["scalar_map_convention"],
    "required_frame": weighted["required_frame"],
    "requests": retained,
    "omitted_request_ids": [30, 31],
    "omission_reason": "Both symmetric-weight tests factor through the full S4 sign projector, whose actual obstruction class is a proved global boundary.",
    "independence": "Inherited 32-test basis plus exact genuine scalar-target linearization; no rank recomputation.",
    "interpretation": "30 independent weighted functionals on the authenticated rank-30 projector kernel, not 30 individual Laurent positions.",
    "counts": {"requests": 30, "listed_weighted_terms": terms, "distinct_map_exponent_pairs": len(unique)},
    "gates": {"physical_source_evaluated": False, "rank_recomputed": False,
              "finite_cutoff_admitted_by_this_theorem": False, "execution_release": False},
    "obstruction": "remaining_30_dimensional_class_undecided",
}
output = HERE / "weighted-requests-30.json"
raw = (json.dumps(derived, sort_keys=True, indent=2) + "\n").encode()
if output.exists():
    need(output.read_bytes() == raw, "Derived output drift")
else:
    output.write_bytes(raw)
need(json.loads(output.read_bytes())["requests"] == requests[:30], "Exact subsequence readback")
receipt = {
    "status": "static_request_and_dual_weight_controls_pass",
    "source_commit": PIN,
    "input_sha256": HASHES,
    "retained_ids": [0, 29],
    "omitted_ids": [30, 31],
    "retained_counts": derived["counts"],
    "full_S4_symmetry_of_omitted_weights_checked": True,
    "centered_dual_weight_identities_checked": True,
    "output_sha256": hashlib.sha256(raw).hexdigest(),
    "physical_source_evaluated": False,
    "rank_recomputed": False,
    "model_reconstructed": False,
    "previous_source_experiment_repeated": False,
}
print(json.dumps(receipt, sort_keys=True, indent=2))
