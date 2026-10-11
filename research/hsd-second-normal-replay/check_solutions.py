"""Compare the frozen right-hand side with the 405 exported corrections.

The frozen hash is checked before the correction file is opened.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    MONOMIALS,
    PAIRS,
    PLANES,
    add_vec,
    apply_TB,
    relation_holds,
    scale_vec,
    scalar_regular_on,
    unpack_vec,
)

HERE = Path(__file__).resolve().parent
PIN = "22b800836385cf4c869c200bfc6715e07613aad6"
CORRECTIONS = (
    "research/carrier/plane-completion-lemma/second-normal-comparison/"
    "SECOND_NORMAL_SECTION_CORRECTIONS.json"
)
ROOT = Path(__file__).resolve().parents[2]


def git_bytes(rev, path):
    import subprocess

    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)


def load_frozen():
    import hashlib

    raw = (HERE / "frozen_rhs.json").read_text(encoding="utf-8")
    frozen = json.loads(raw)
    payload = frozen["rhs"]
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    if digest != frozen["rhs_sha256"]:
        raise SystemExit("frozen payload hash does not match rhs_sha256")
    recorded = (HERE / "frozen_rhs.sha256").read_text(encoding="utf-8").strip()
    if recorded != digest:
        raise SystemExit("frozen_rhs.sha256 does not match the payload")
    return frozen, digest


def load_corrections():
    from fractions import Fraction

    payload = json.loads(git_bytes(PIN, CORRECTIONS))
    loaded = {}
    total = 0
    for name, block in payload.items():
        loaded[name] = {}
        for chart, records in block.items():
            opens = {}
            for record in records:
                vec = []
                for component in record["components"]:
                    poly = {}
                    for geom, value in component:
                        coef = Fraction(str(value))
                        if coef:
                            exp = tuple(geom)
                            poly[exp] = poly.get(exp, 0) + coef
                            total += 1
                    vec.append(poly)
                while len(vec) < 4:
                    vec.append({})
                opens[tuple(record["open"])] = vec[:4]
            loaded[name][chart] = opens
    return loaded, total


def records_by_open(records):
    return {tuple(record["open"]): unpack_vec(record["components"]) for record in records}


def y_of(monomial_payload, chart, open_pair, half_sign):
    total = [{}, {}, {}, {}]
    for part, sign in (
        ("kappa_on_v", 1),
        ("eta_on_xi", 1),
        ("half_square", half_sign),
    ):
        vec = records_by_open(monomial_payload[chart][part]).get(open_pair, [{}, {}, {}, {}])
        total = add_vec(total, scale_vec(vec, sign))
    return total


def sigma_at(corrections, name, chart, index):
    return corrections[name][chart].get((index,), [{}, {}, {}, {}])


def sub_vec(a, b):
    return add_vec(a, scale_vec(b, -1))


def z_mode_for(chart):
    # Finite charts are regular in z, infinity charts in z^{-1}.
    # The mixed base overlap inverts z, so both signs are allowed there.
    if chart == "infinity":
        return "nonpositive"
    if chart == "mixed":
        return "free"
    return "nonnegative"


def check_residual(residual, relation_chart, open_pair, mode):
    ok, scalar = relation_holds(residual, relation_chart)
    if not ok:
        return False, "not a relation multiple"
    if not scalar_regular_on(scalar, open_pair, mode):
        return False, f"quotient not regular ({mode}) on {list(open_pair)}"
    return True, ""


def first_mismatch(residual, chart):
    from common import mul_vec, quotient_by_F, relation

    produced = mul_vec(relation(chart), quotient_by_F(residual))
    for slot in range(4):
        keys = set(produced[slot]) | set(residual[slot])
        for exp in sorted(keys):
            left = produced[slot].get(exp, 0)
            right = residual[slot].get(exp, 0)
            if left != right:
                return {"slot": slot, "exp": list(exp), "produced": str(left), "residual": str(right)}
    return None


def evaluate(frozen, corrections, half_sign):
    failures = []
    checked = 0
    monomials = frozen["rhs"]["monomials"]
    for name in MONOMIALS:
        block = monomials[name]
        for chart, opens, rel_chart in (
            ("finite", PAIRS, "finite"),
            ("infinity", PAIRS, "infinity"),
        ):
            for i, j in opens:
                y = y_of(block, chart, (i, j), half_sign)
                residual = sub_vec(
                    sub_vec(sigma_at(corrections, name, chart, j), sigma_at(corrections, name, chart, i)),
                    y,
                )
                checked += 1
                ok, reason = check_residual(residual, rel_chart, (i, j), z_mode_for(chart))
                if not ok:
                    failures.append(
                        {
                            "monomial": name,
                            "chart": chart,
                            "open": [i, j],
                            "reason": reason,
                            "mismatch": first_mismatch(residual, rel_chart),
                        }
                    )
        for index in PLANES:
            y = y_of(block, "mixed", (index,), half_sign)
            residual = sub_vec(
                sub_vec(
                    apply_TB(sigma_at(corrections, name, "infinity", index)),
                    sigma_at(corrections, name, "finite", index),
                ),
                y,
            )
            checked += 1
            ok, reason = check_residual(residual, "finite", (index,), z_mode_for("mixed"))
            if not ok:
                failures.append(
                    {
                        "monomial": name,
                        "chart": "mixed",
                        "open": [index],
                        "reason": reason,
                        "mismatch": first_mismatch(residual, "finite"),
                    }
                )
    return {"checked_equations": checked, "failures": failures}


def main():
    frozen, digest = load_frozen()
    print(f"frozen rhs {digest}", flush=True)
    corrections, term_count = load_corrections()
    print(f"exported terms {term_count}", flush=True)
    good = evaluate(frozen, corrections, half_sign=1)
    bad = evaluate(frozen, corrections, half_sign=-1)
    bad_algebra = [item for item in bad["failures"] if item["reason"] == "not a relation multiple"]
    report = {
        "rhs_sha256": digest,
        "exported_terms": term_count,
        "good_failures": len(good["failures"]),
        "good_equations": good["checked_equations"],
        "bad_failures": len(bad["failures"]),
        "bad_algebra_failures": len(bad_algebra),
        "bad_equations": bad["checked_equations"],
        "good_sample": good["failures"][:3],
        "bad_sample": bad_algebra[:3],
        "opposite_sign_nontrivial": len(bad_algebra) > 0,
    }
    (HERE / "check_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in report if k not in ("good_sample", "bad_sample")}))
    if good["failures"]:
        print(json.dumps(good["failures"][:5], indent=2))
        raise SystemExit("positive convention left a nonzero residual")
    if not bad_algebra:
        raise SystemExit("opposite sign convention was annihilated")
    if term_count != 405:
        raise SystemExit(f"expected 405 terms, found {term_count}")


if __name__ == "__main__":
    main()
