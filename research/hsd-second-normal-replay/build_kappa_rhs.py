"""Scope B: freeze the fifteen raw quadratic BCH right-hand sides.

Reads the source first jet only. The hash is the hash of these right-hand
sides and of nothing else.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import MONOMIALS, pack_poly
from kappa import build_raw, load_eta, monomial_orders

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PIN = "22b800836385cf4c869c200bfc6715e07613aad6"
SOURCE = "6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb"
PINNED_FIRST_JET = "2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10"
SOURCE_JET = "research/carrier/formal-five-parameter-chart/data/first_jet.json"
BUNDLED_JET = "research/carrier/plane-completion-lemma/second-normal-comparison/first_jet.json"


def git_bytes(rev, path):
    return subprocess.check_output(["git", "show", f"{rev}:{path}"], cwd=ROOT)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def pack_tensor(tensor):
    return [
        {"slot": list(slot), "terms": pack_poly(poly)}
        for slot, poly in sorted(tensor.items())
    ]


def pack_raw(raw):
    packed = {}
    for label, _ordered in monomial_orders():
        block = raw[label]
        packed[label] = {
            "finite": pack_tensor(block["finite"]),
            "infinity": pack_tensor(block["infinity"]),
            "mixed": [
                {"open": list(pair), "tensor": pack_tensor(block["mixed"][pair])}
                for pair in ((0, 1), (0, 2), (1, 2))
            ],
        }
    return {"parts": ["finite", "infinity", "mixed"], "monomials": packed}


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def main():
    jet_bytes = git_bytes(SOURCE, SOURCE_JET)
    require(sha256(jet_bytes) == PINNED_FIRST_JET, "source first_jet hash mismatch")
    bundled = git_bytes(PIN, BUNDLED_JET)
    require(bundled == jet_bytes, "bundled first_jet is not the source blob")
    first_jet = json.loads(jet_bytes)
    print("building 15 quadratic BCH right-hand sides", flush=True)
    raw = build_raw(load_eta(first_jet))
    require(set(raw) == set(MONOMIALS), "right-hand side monomials are not the fifteen")
    payload = pack_raw(raw)
    digest = sha256(canonical(payload).encode("utf-8"))
    frozen = {
        "pin": PIN,
        "source": SOURCE,
        "first_jet_sha256": PINNED_FIRST_JET,
        "inputs": ["first_jet.json"],
        "rhs_sha256": digest,
        "rhs": payload,
    }
    (HERE / "frozen_kappa_rhs.json").write_text(
        json.dumps(frozen, sort_keys=True), encoding="utf-8"
    )
    (HERE / "frozen_kappa_rhs.sha256").write_text(digest + "\n", encoding="utf-8")
    print(digest)


if __name__ == "__main__":
    main()
