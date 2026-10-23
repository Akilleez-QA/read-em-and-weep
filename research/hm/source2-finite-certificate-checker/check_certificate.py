#!/usr/bin/env python3
"""Bounded exact checks over Q[a0,a1,a2]; never authenticates geometry."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

SCHEMA = "source2-finite-correction-v1"
COMMIT = "5b52eedce3420ccc3e407e97201bcdd056501bbf"
THEOREM_SHA256 = "d1f96ad68df6781474e0aa247625b08de8cfc06e2af854418cbd32ce52469140"
THEOREM_GIT_BLOB = "a8f57401d93c296d23a5ed55cd09d8893222e7c1"
ZERO = (0, 0, 0)
MAX_BYTES = 8_000_000
MAX_DIM = 64
MAX_TERMS = 100_000
MAX_OPERATIONS = 5_000_000
MAX_BITS = 4096


class InvalidCertificate(ValueError):
    pass


class ResourceLimit(InvalidCertificate):
    """An inconclusive bounded-resource stop, not a mathematical refutation."""


def require(condition, message):
    if not condition:
        raise InvalidCertificate(message)


def integer(value):
    return type(value) is int


def fields(value, expected, where):
    require(type(value) is dict and set(value) == set(expected),
            where + ": wrong object fields")


def bounded(q):
    if max(q.numerator.bit_length(), q.denominator.bit_length()) > MAX_BITS:
        raise ResourceLimit("intermediate rational coefficient exceeds bit bound")
    return q


class Budget:
    def __init__(self):
        self.operations = 0
        self.input_terms = 0

    def tick(self, n=1):
        self.operations += n
        if self.operations > MAX_OPERATIONS:
            raise ResourceLimit("exact arithmetic operation budget exceeded")


def accumulate(out, key, value):
    value = bounded(out.get(key, Fraction(0)) + value)
    if value:
        out[key] = value
    else:
        out.pop(key, None)
    if len(out) > MAX_TERMS:
        raise ResourceLimit("intermediate sparse support exceeds term bound")


def matrix(obj, rows, cols, degree, budget, label):
    fields(obj, ("rows", "cols", "terms"), label)
    require(integer(obj["rows"]) and integer(obj["cols"])
            and (obj["rows"], obj["cols"]) == (rows, cols),
            label + ": matrix shape mismatch")
    terms = obj["terms"]
    require(type(terms) is list, label + ": terms must be a list")
    budget.input_terms += len(terms)
    if budget.input_terms > MAX_TERMS:
        raise ResourceLimit("total input term bound exceeded")
    out = {}
    for term in terms:
        require(type(term) is list and len(term) == 4, label + ": malformed term")
        r, c, powers, coeff = term
        require(integer(r) and integer(c) and 0 <= r < rows and 0 <= c < cols,
                label + ": row/column index out of range")
        require(type(powers) is list and len(powers) == 3
                and all(integer(k) and 0 <= k <= 23 for k in powers),
                label + ": invalid exponent vector")
        require(sum(powers) == degree, label + ": not homogeneous of degree " + str(degree))
        require(type(coeff) is list and len(coeff) == 2
                and all(integer(k) for k in coeff), label + ": rational pair required")
        num, den = coeff
        require(num != 0 and den > 0 and math.gcd(num, den) == 1,
                label + ": coefficient must be nonzero, reduced, positive denominator")
        if max(abs(num).bit_length(), den.bit_length()) > 512:
            raise ResourceLimit(label + ": input coefficient exceeds bit bound")
        key = (r, c, tuple(powers))
        require(key not in out, label + ": duplicate entry/monomial")
        out[key] = Fraction(num, den)
    return out


def product(a, b, budget):
    byrow = {}
    for (r, c, e), v in b.items():
        byrow.setdefault(r, []).append((c, e, v))
    out = {}
    for (r, k, e), v in a.items():
        for c, f, w in byrow.get(k, []):
            budget.tick()
            accumulate(out, (r, c, tuple(x + y for x, y in zip(e, f))), v * w)
    return out


def negate(a):
    return {k: -v for k, v in a.items()}


def polynomial_product(a, b, budget):
    out = {}
    for e, v in a.items():
        for f, w in b.items():
            budget.tick()
            accumulate(out, tuple(x + y for x, y in zip(e, f)), v * w)
    return out


def substitute(a, action, budget):
    """Return a(A*a), with column coordinates and A represented by action."""
    linear = [{} for _ in range(3)]
    for (r, c, e), v in action.items():
        unit = tuple(int(j == c) for j in range(3))
        linear[r][unit] = v
    powers = {(j, 0): {ZERO: Fraction(1)} for j in range(3)}
    for j in range(3):
        highest = max((e[j] for r, c, e in a), default=0)
        for n in range(1, highest + 1):
            powers[j, n] = polynomial_product(powers[j, n - 1], linear[j], budget)
    out = {}
    for (r, c, e), v in a.items():
        poly = {ZERO: v}
        for j in range(3):
            poly = polynomial_product(poly, powers[j, e[j]], budget)
        for f, w in poly.items():
            budget.tick()
            accumulate(out, (r, c, f), w)
    return out


def nonsingular(a, n, budget, label):
    """Check supplied constant action matrices, not the pencil or its rank."""
    rows = [[a.get((r, c, ZERO), Fraction(0)) for c in range(n)] for r in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if rows[r][col]), None)
        require(pivot is not None, label + ": singular generator action")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        for r in range(col + 1, n):
            if not rows[r][col]:
                continue
            factor = bounded(rows[r][col] / rows[col][col])
            for c in range(col, n):
                budget.tick()
                rows[r][c] = bounded(rows[r][c] - factor * rows[col][c])


def canonical_digest(data):
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def theorem_pin():
    raw = (Path(__file__).resolve().parent / "inputs" / "PR1107-PROOF.md").read_bytes()
    require(hashlib.sha256(raw).hexdigest() == THEOREM_SHA256, "bundled theorem SHA256 mismatch")
    git = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(git == THEOREM_GIT_BLOB, "bundled theorem Git blob mismatch")


def duplicate_safe_object(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "duplicate JSON key: " + k)
        out[k] = v
    return out


def forbidden_number(value):
    raise InvalidCertificate("only integer JSON numbers are allowed")


def load_bytes(raw):
    if len(raw) > MAX_BYTES:
        raise ResourceLimit("input byte bound exceeded")
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=duplicate_safe_object,
                          parse_float=forbidden_number, parse_constant=forbidden_number)
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise InvalidCertificate("invalid bounded UTF-8 JSON") from exc


def check(certificate, expected_data_sha256=None):
    theorem_pin()
    fields(certificate, ("schema", "binding", "data"), "certificate")
    require(certificate["schema"] == SCHEMA, "unsupported schema")
    binding = certificate["binding"]
    fields(binding, ("theorem_commit", "theorem_sha256", "data_sha256"), "binding")
    require(binding["theorem_commit"] == COMMIT and binding["theorem_sha256"] == THEOREM_SHA256,
            "wrong finite-theorem pin")
    digest = canonical_digest(certificate["data"])
    require(binding["data_sha256"] == digest, "data digest mismatch")
    if expected_data_sha256 is not None:
        require(type(expected_data_sha256) is str and expected_data_sha256 == digest,
                "caller-supplied expected data digest mismatch")
    data = certificate["data"]
    fields(data, ("variables", "dimensions", "maps", "corrections", "generators"), "data")
    require(data["variables"] == ["a0", "a1", "a2"], "three named polynomial coordinates required")
    dims = data["dimensions"]
    fields(dims, ("N", "M", "P"), "dimensions")
    require(all(integer(x) and x >= 1 for x in dims.values()), "invalid dimension")
    if any(x > MAX_DIM for x in dims.values()):
        raise ResourceLimit("dimension bound exceeded")
    N, M, P = (dims[k] for k in ("N", "M", "P"))
    budget = Budget()
    maps = data["maps"]
    fields(maps, ("Q", "T", "s", "i_P"), "maps")
    q = matrix(maps["Q"], M, N, 0, budget, "Q")
    t = matrix(maps["T"], M, N, 1, budget, "T")
    s = matrix(maps["s"], N, P, 0, budget, "s")
    inc = matrix(maps["i_P"], M, P, 0, budget, "i_P")
    require(type(data["corrections"]) is list and len(data["corrections"]) == 24,
            "exactly x0 through x23 required")
    xs = [matrix(x, N, P, i, budget, "x" + str(i))
          for i, x in enumerate(data["corrections"])]
    require(xs[0] == s, "x0 does not equal supplied s")
    require(product(q, xs[0], budget) == inc, "Q*x0 != i_P")
    for i in range(1, 24):
        require(product(q, xs[i], budget) == negate(product(t, xs[i - 1], budget)),
                "correction identity fails at x" + str(i))
    generators = data["generators"]
    require(type(generators) is list, "generators must be a list")
    if len(generators) > 8:
        raise ResourceLimit("generator count bound exceeded")
    names = set()
    for g in generators:
        fields(g, ("name", "A", "N", "M", "P"), "generator")
        name = g["name"]
        require(type(name) is str and 1 <= len(name) <= 80 and name not in names,
                "generator names must be short, nonempty and unique")
        names.add(name)
        acts = {k: matrix(g[k], n, n, 0, budget, name + "/" + k)
                for k, n in (("A", 3), ("N", N), ("M", M), ("P", P))}
        for k, n in (("A", 3), ("N", N), ("M", M), ("P", P)):
            nonsingular(acts[k], n, budget, name + "/" + k)
        tests = [("Q", q, "N", "M"), ("T", t, "N", "M"),
                 ("s", s, "P", "N"), ("i_P", inc, "P", "M")]
        tests += [("x" + str(i), x, "P", "N") for i, x in enumerate(xs)]
        for label, f, source, target in tests:
            lhs = product(substitute(f, acts["A"], budget), acts[source], budget)
            rhs = product(acts[target], f, budget)
            require(lhs == rhs, name + ": equivariance fails for " + label)
    return {
        "status": "ALGEBRAIC_IDENTITIES_VERIFIED",
        "correction_equations": 24,
        "x0_equals_supplied_s": True,
        "homogeneity_checked_through": 23,
        "supplied_generator_equivariance": "CHECKED" if generators else "NOT_CHECKED",
        "generator_count": len(generators),
        "original_positive_shape": (N, M, P) == (41, 37, 4),
        "data_sha256": digest,
        "caller_expected_digest_checked": expected_data_sha256 is not None,
        "theorem_content_pin_checked": True,
        "actual_map_authentication": "NOT_ESTABLISHED",
        "group_generation_and_relations": "NOT_ESTABLISHED",
        "retained_geometric_hypotheses": "NOT_ESTABLISHED",
        "actual_original_positive_rank": "NOT_DETERMINED",
        "operations": budget.operations,
        "input_terms": budget.input_terms,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--expected-data-sha256")
    args = parser.parse_args()
    try:
        with args.certificate.open("rb") as stream:
            raw = stream.read(MAX_BYTES + 1)
        result = check(load_bytes(raw), args.expected_data_sha256)
    except ResourceLimit as exc:
        result = {"status": "RESOURCE_LIMIT_INCONCLUSIVE", "reason": str(exc)}
        code = 2
    except (InvalidCertificate, OSError, ValueError, TypeError, RecursionError) as exc:
        result = {"status": "CERTIFICATE_REJECTED", "reason": str(exc)}
        code = 1
    else:
        code = 0
    print(json.dumps(result, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
