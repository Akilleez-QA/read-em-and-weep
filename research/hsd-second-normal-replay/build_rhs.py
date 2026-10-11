"""Rebuild the second-normal section right-hand side and freeze its hash.

Reads the source first jet and the fifteen W primitives. Does not read the
second-normal checker, its check receipt, or the exported section corrections.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    DIRECTIONS,
    MONOMIALS,
    ONE4,
    PAIRS,
    PLANES,
    V_E0,
    Z4,
    action,
    add,
    add_vec,
    apply_TB,
    g_times_c,
    monomial_key,
    omega_on_q,
    omega_pairs,
    pack_vec,
    relation,
    scale_vec,
    transport_identity_literal,
    vec_eq,
    vec_is_zero,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PIN = "22b800836385cf4c869c200bfc6715e07613aad6"
SOURCE = "6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb"
PINNED_FIRST_JET = "2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10"
PINNED_CERTIFICATE = "c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4"

SOURCE_JET = "research/carrier/formal-five-parameter-chart/data/first_jet.json"
SOURCE_CERTIFICATE = (
    "research/carrier/formal-five-parameter-chart/audit_original_cover/certificate.json"
)
FIRST_SECTIONS = (
    "research/carrier/plane-completion-lemma/first-normal-comparison/"
    "FIRST_NORMAL_SECTION_CORRECTIONS.json"
)
PARTS = ("kappa_on_v", "eta_on_xi", "half_square")


def git_bytes(rev, path):
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def load_jet_records(records):
    out = {}
    for record in records:
        poly = {}
        for slot, geom, value in record["terms"]:
            if isinstance(slot, int):
                slot = [slot]
            frame = [0, 0, 0, 0]
            for index in slot:
                frame[index] += 1
            exp = tuple(geom) + tuple(frame)
            coef = __import__("fractions").Fraction(str(value))
            if coef:
                poly[exp] = poly.get(exp, 0) + coef
                if not poly[exp]:
                    del poly[exp]
        if poly:
            key = tuple(record["open"])
            out[key] = add(out.get(key, {}), poly)
    return out


def load_directions(first_jet):
    loaded = {
        "1": {
            part: load_jet_records(first_jet["origin"][part])
            for part in ("finite", "infinity", "mixed")
        }
    }
    for direction in first_jet["directions"]:
        loaded[direction["name"]] = {
            part: load_jet_records(direction[part])
            for part in ("finite", "infinity", "mixed")
        }
    missing = [name for name in DIRECTIONS if name not in loaded]
    require(not missing, f"missing directions {missing}")
    return loaded


def load_primitives(certificate):
    """Keep only the fifteen W primitives. Drop every solver field."""
    coefficients = certificate["coefficients"]
    require(set(coefficients) == set(MONOMIALS), "unexpected certificate monomials")
    primitives = {}
    for name in MONOMIALS:
        raw = coefficients[name]["original_cover_primitive"]
        primitives[name] = {
            "finite": unpack_primitive(raw["finite_W_primitive"]),
            "infinity": unpack_primitive(raw["infinity_W_primitive"]),
            "mixed": unpack_primitive(raw["mixed_W_primitive"]),
        }
    return primitives


def unpack_primitive(records):
    out = {}
    for record in records:
        poly = {}
        for exp, value in record["terms"]:
            coef = __import__("fractions").Fraction(str(value))
            if coef:
                key = tuple(exp)
                poly[key] = poly.get(key, 0) + coef
                if not poly[key]:
                    del poly[key]
        if poly:
            key = tuple(record["open"])
            out[key] = add(out.get(key, {}), poly)
    return out


def load_sections(payload):
    from fractions import Fraction

    loaded = {}
    for name, block in payload.items():
        charts = {}
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
                            if not poly[exp]:
                                del poly[exp]
                    vec.append(poly)
                while len(vec) < 4:
                    vec.append({})
                opens[tuple(record["open"])] = vec[:4]
            charts[chart] = opens
        loaded[name] = charts
    require("origin" in loaded, "first-normal sections have no origin")
    return loaded


def section_vector(sections, direction, chart, open_index):
    key = "origin" if direction == "1" else direction
    return sections[key][chart].get((open_index,), [{}, {}, {}, {}])


def empty_store():
    return {
        name: {chart: {part: {} for part in PARTS} for chart in ("finite", "infinity", "mixed")}
        for name in MONOMIALS
    }


def accumulate(store, name, chart, part, open_pair, vec):
    bucket = store[name][chart][part].setdefault(open_pair, [{}, {}, {}, {}])
    store[name][chart][part][open_pair] = add_vec(bucket, vec)


def fill_overlap(store, store_chart, section_chart, etas, kappas, sections, open_pair, t0, q_chart):
    """Assemble κ(v), Aη(ξ_i) and ½ Aη²(v) on one double overlap or mixed open."""
    omega = omega_pairs(q_chart)
    q_index = open_pair[0]
    oq = omega_on_q(q_chart, q_index)
    eta = []
    xi = []
    q_coeff = []
    for direction in DIRECTIONS:
        eta.append(etas[direction].get(open_pair, {}))
        xi.append(section_vector(sections, direction, section_chart, q_index))
        q_coeff.append(t0 if direction == "1" else None)
    fields = [action(eta[p], V_E0, omega) for p in range(5)]
    for p in range(5):
        for q in range(5):
            key = monomial_key(p, q)
            if eta[p]:
                acted = action(eta[p], xi[q], omega, q_coeff[q], oq)
                if not vec_is_zero(acted):
                    accumulate(store, key, store_chart, "eta_on_xi", open_pair, acted)
            if eta[p] and not vec_is_zero(fields[q]):
                square = scale_vec(action(eta[p], fields[q], omega), "1/2")
                if not vec_is_zero(square):
                    accumulate(store, key, store_chart, "half_square", open_pair, square)
    for name in MONOMIALS:
        kappa = kappas[name].get(open_pair, {})
        if not kappa:
            continue
        acted = action(kappa, V_E0, omega)
        if not vec_is_zero(acted):
            accumulate(store, name, store_chart, "kappa_on_v", open_pair, acted)


def emit_chart(store, name, chart, opens):
    emitted = {}
    for part in PARTS:
        records = []
        for open_pair in opens:
            vec = store[name][chart][part].get(open_pair, [{}, {}, {}, {}])
            records.append({"open": list(open_pair), "components": pack_vec(vec)})
        emitted[part] = records
    return emitted


def build_payload(directions, primitives, sections):
    store = empty_store()
    for chart, t0, q_chart, opens in (
        ("finite", Z4, "finite", PAIRS),
        ("infinity", ONE4, "infinity", PAIRS),
    ):
        etas = {direction: directions[direction][chart] for direction in DIRECTIONS}
        kappas = {monomial: primitives[monomial][chart] for monomial in MONOMIALS}
        for open_pair in opens:
            print(f"  {chart} {open_pair}", flush=True)
            fill_overlap(store, chart, chart, etas, kappas, sections, open_pair, t0, q_chart)
    etas = {direction: directions[direction]["mixed"] for direction in DIRECTIONS}
    kappas = {monomial: primitives[monomial]["mixed"] for monomial in MONOMIALS}
    for index in PLANES:
        print(f"  mixed {(index,)}", flush=True)
        fill_overlap(store, "mixed", "finite", etas, kappas, sections, (index,), Z4, "finite")
    monomials = {}
    mixed_opens = tuple((index,) for index in PLANES)
    for name in MONOMIALS:
        monomials[name] = {
            "finite": emit_chart(store, name, "finite", PAIRS),
            "infinity": emit_chart(store, name, "infinity", PAIRS),
            "mixed": emit_chart(store, name, "mixed", mixed_opens),
        }
    return {"parts": list(PARTS), "sum": "kappa_on_v+eta_on_xi+half_square", "monomials": monomials}


def check_transport_pin():
    """Re-derived input: g C equals the hand binomial S^3 - z^3 W^6, and TB r_∞ = z^3 r_0."""
    require(g_times_c() == transport_identity_literal(), "g C disagrees with the hand expansion")
    from common import shift

    image = apply_TB(relation("infinity"))
    target = [shift(component, dz=3) for component in relation("finite")]
    require(vec_eq(image, target), "TB r_infinity is not z^3 r_finite")


def check_bracket_pin(directions):
    """Re-derived input: one pinned origin term's contraction, computed from Ω(E1,E0)=-XY."""
    from common import action_on_vector

    ham = directions["1"]["finite"].get((0, 1), {})
    exp = (1, -2, -1, 0, 0, 1, 1, 0)
    require(ham.get(exp) == __import__("fractions").Fraction(-2), "pinned E0 E1 term is not -2")
    alone = {exp: ham[exp]}
    vector = action_on_vector(alone, V_E0, omega_pairs("finite"))
    expected_e0 = {(1, -1, 0, 0): __import__("fractions").Fraction(2)}
    require(vector[0] == {} and vector[2] == {} and vector[3] == {}, "pinned term leaked slots")
    require(vector[1] == expected_e0, f"pinned contraction {vector[1]} != 2 z X^(-1)")


def main():
    check_transport_pin()
    jet_bytes = git_bytes(SOURCE, SOURCE_JET)
    cert_bytes = git_bytes(SOURCE, SOURCE_CERTIFICATE)
    require(sha256(jet_bytes) == PINNED_FIRST_JET, "source first_jet hash mismatch")
    require(sha256(cert_bytes) == PINNED_CERTIFICATE, "source certificate hash mismatch")
    bundled_jet = git_bytes(
        PIN,
        "research/carrier/plane-completion-lemma/second-normal-comparison/first_jet.json",
    )
    require(bundled_jet == jet_bytes, "bundled first_jet is not the source blob")
    section_bytes = git_bytes(PIN, FIRST_SECTIONS)
    first_jet = json.loads(jet_bytes)
    certificate = json.loads(cert_bytes)
    primitives = load_primitives(certificate)
    del certificate
    directions = load_directions(first_jet)
    check_bracket_pin(directions)
    sections = load_sections(json.loads(section_bytes))
    print("building right-hand side", flush=True)
    monomials = build_payload(directions, primitives, sections)
    digest = sha256(canonical(monomials).encode("utf-8"))
    frozen = {
        "pin": PIN,
        "source": SOURCE,
        "first_jet_sha256": PINNED_FIRST_JET,
        "certificate_sha256": PINNED_CERTIFICATE,
        "rhs_sha256": digest,
        "rhs": monomials,
    }
    out = HERE / "frozen_rhs.json"
    out.write_text(json.dumps(frozen, sort_keys=True), encoding="utf-8")
    (HERE / "frozen_rhs.sha256").write_text(digest + "\n", encoding="utf-8")
    print(digest)


if __name__ == "__main__":
    main()
