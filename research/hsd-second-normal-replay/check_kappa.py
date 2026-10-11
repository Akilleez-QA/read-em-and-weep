"""Scope B: check the fifteen κ cochains against the frozen BCH right-hand sides.

The frozen hash is checked before the certificate is opened. Two mutations of
the actual origin finite (0,1) cochain must then fail with the residuals
predicted from the Čech signs.
"""

import hashlib
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    MONOMIALS,
    V_E0,
    action_on_vector,
    omega_pairs,
    pack_poly,
    pack_vec,
    unpack_poly,
    vec_is_zero,
)
from kappa import (
    add_term,
    defect_chart,
    equation_defects,
    evaluate,
    ham_to_tensor,
    monomial_orders,
    mutation_term,
    predicted_mismatches,
    relation_mismatch,
    tensor_to_ham,
)

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[2]
PIN = "22b800836385cf4c869c200bfc6715e07613aad6"
SOURCE = "6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb"
PINNED_CERTIFICATE = "c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4"
SOURCE_CERTIFICATE = (
    "research/carrier/formal-five-parameter-chart/audit_original_cover/certificate.json"
)

# Both mutations hit the actual origin finite01 κ. The first is the kernel
# term of the action on E0. The second meets E1, so that action is nonzero.
MUTATIONS = (
    {
        "name": "kernel_E0_square",
        "monomial": "1",
        "chart": "finite",
        "open": (0, 1),
        "slot": (1, 1),
        "exp": (0, -1, -1, 2),
        "coef": 1,
        "kernel_of_action_on_E0": True,
    },
    {
        "name": "outside_E0_E1",
        "monomial": "1",
        "chart": "finite",
        "open": (0, 1),
        "slot": (1, 2),
        "exp": (0, -1, 0, 0),
        "coef": 1,
        "kernel_of_action_on_E0": False,
    },
)


def git_bytes(rev, path):
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def unpack_tensor(packed):
    tensor = {}
    for record in packed:
        poly = unpack_poly(record["terms"])
        if poly:
            tensor[tuple(record["slot"])] = poly
    return tensor


def unpack_raw(payload):
    raw = {}
    for label, block in payload["monomials"].items():
        mixed = {}
        for record in block["mixed"]:
            mixed[tuple(record["open"])] = unpack_tensor(record["tensor"])
        raw[label] = {
            "finite": unpack_tensor(block["finite"]),
            "infinity": unpack_tensor(block["infinity"]),
            "mixed": mixed,
        }
    return raw


def load_frozen():
    raw_text = (HERE / "frozen_kappa_rhs.json").read_text(encoding="utf-8")
    frozen = json.loads(raw_text)
    payload = frozen["rhs"]
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    require(digest == frozen["rhs_sha256"], "frozen payload hash does not match rhs_sha256")
    recorded = (HERE / "frozen_kappa_rhs.sha256").read_text(encoding="utf-8").strip()
    require(recorded == digest, "frozen_kappa_rhs.sha256 does not match the payload")
    require(frozen["inputs"] == ["first_jet.json"], "scope B right-hand side names an unexpected input")
    return frozen, digest


def pack_mismatch(mismatch):
    return [
        {"slot": list(slot), "terms": pack_poly(poly)}
        for slot, poly in sorted(mismatch.items())
    ]


def _primitive_to_tensors(records):
    opens = {}
    for record in records:
        ham = {}
        for exp, value in record["terms"]:
            coef = Fraction(str(value))
            if coef:
                key = tuple(exp)
                ham[key] = ham.get(key, 0) + coef
        opens[tuple(record["open"])] = ham_to_tensor(ham)
    return opens


def load_kappa(certificate):
    """Fifteen W primitives. Every other certificate field is ignored."""
    coefficients = certificate["coefficients"]
    loaded = {}
    for label, _ordered in monomial_orders():
        primitive = coefficients[label]["original_cover_primitive"]
        loaded[label] = {
            "finite": _primitive_to_tensors(primitive["finite_W_primitive"]),
            "infinity": _primitive_to_tensors(primitive["infinity_W_primitive"]),
            "mixed": _primitive_to_tensors(primitive["mixed_W_primitive"]),
        }
    return loaded


def action_of_term(slot, exp, coef):
    ham = tensor_to_ham(mutation_term(slot, exp, coef))
    return action_on_vector(ham, V_E0, omega_pairs("finite"))


def check_mutation(raw, kappa, spec):
    term_action = action_of_term(spec["slot"], spec["exp"], spec["coef"])
    in_kernel = vec_is_zero(term_action)
    require(
        in_kernel == spec["kernel_of_action_on_E0"],
        f"{spec['name']}: action on E0 is kernel={in_kernel}, prediction was {spec['kernel_of_action_on_E0']}",
    )
    predicted = predicted_mismatches(
        spec["chart"], spec["open"], spec["slot"], spec["exp"], spec["coef"]
    )
    mutant = add_term(
        kappa[spec["monomial"]],
        spec["chart"],
        spec["open"],
        spec["slot"],
        spec["exp"],
        spec["coef"],
    )
    defects = equation_defects(raw[spec["monomial"]], mutant)
    seen = {
        key: relation_mismatch(defect, defect_chart(key[0]))
        for key, defect in defects.items()
    }
    expected = {key: {} for key in defects}
    expected.update(predicted)
    require(seen == expected, f"{spec['name']}: residual was not the predicted one")
    require(all(predicted.values()), f"{spec['name']}: a predicted residual vanished")
    return {
        "name": spec["name"],
        "monomial": spec["monomial"],
        "open": list(spec["open"]),
        "slot": list(spec["slot"]),
        "term": pack_poly(mutation_term(spec["slot"], spec["exp"], spec["coef"])[spec["slot"]]),
        "action_on_E0_is_zero": in_kernel,
        "action_on_E0": pack_vec(term_action),
        "rejected": True,
        "residuals": [
            {
                "kind": kind,
                "open": list(opened),
                "mismatch": pack_mismatch(seen[(kind, opened)]),
            }
            for kind, opened in sorted(predicted, key=lambda item: (item[0], item[1]))
        ],
    }


def main():
    frozen, digest = load_frozen()
    print(f"frozen bch rhs {digest}", flush=True)
    cert_bytes = git_bytes(SOURCE, SOURCE_CERTIFICATE)
    require(hashlib.sha256(cert_bytes).hexdigest() == PINNED_CERTIFICATE, "certificate hash mismatch")
    kappa = load_kappa(json.loads(cert_bytes))
    require(set(kappa) == set(MONOMIALS), "kappa monomials are not the fifteen")
    raw = unpack_raw(frozen["rhs"])
    good = evaluate(raw, kappa)
    print(
        json.dumps(
            {
                "monomials": len(monomial_orders()),
                "equations": good["checked_equations"],
                "failures": len(good["failures"]),
            }
        ),
        flush=True,
    )
    if good["failures"]:
        sample = []
        for item in good["failures"][:5]:
            sample.append(
                {
                    "monomial": item["monomial"],
                    "kind": item["kind"],
                    "open": item["open"],
                    "slots": [list(slot) for slot in item["mismatch"]],
                }
            )
        print(json.dumps(sample, indent=2))
        raise SystemExit("kappa equations left a nonzero residual")
    mutations = [check_mutation(raw, kappa, spec) for spec in MUTATIONS]
    report = {
        "rhs_sha256": digest,
        "certificate_sha256": PINNED_CERTIFICATE,
        "monomials": len(MONOMIALS),
        "equations": good["checked_equations"],
        "failures": 0,
        "mutations": mutations,
    }
    (HERE / "kappa_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    (HERE / "independence.json").write_text(
        json.dumps(independence_record(digest), indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"mutations": [item["name"] for item in mutations], "rejected": True}))


def independence_record(rhs_sha256):
    return {
        "pin": PIN,
        "source": SOURCE,
        "shared_source_inputs": [
            {
                "name": "first_jet.json",
                "rev": SOURCE,
                "sha256": "2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10",
                "scope_A": "the cochain η inside Aη(ξ) and ½ Aη²(v)",
                "scope_B": "the cochain η inside the Poisson bracket that builds the BCH right-hand side",
            },
            {
                "name": "certificate.json",
                "rev": SOURCE,
                "sha256": PINNED_CERTIFICATE,
                "scope_A": "the fifteen W primitives, used only through their action on v=E0",
                "scope_B": "the same fifteen W primitives, as the cochain κ under test; not an input of the right-hand side",
            },
        ],
        "shared_derived_geometry": "Ω, the relation r, and T_B, recomputed in common.py from the displayed chart formulas",
        "scope_A_only": [
            "FIRST_NORMAL_SECTION_CORRECTIONS.json at the pin, the first-order section ξ",
            "SECOND_NORMAL_SECTION_CORRECTIONS.json at the pin, the 405 second-section terms under test",
        ],
        "scope_B_only": [
            "the Poisson bracket of η on two different opens",
            "z^{-4} Sym^2(T_B) applied to quadratic Hamiltonians",
            "the Čech coboundary of κ",
        ],
        "scope_B_rhs_sha256": rhs_sha256,
        "scope_B_rhs_inputs": ["first_jet.json"],
    }


if __name__ == "__main__":
    main()
