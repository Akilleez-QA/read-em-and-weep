#!/usr/bin/env python3
"""Independent exact check of one current-L quotient edge.

The ring is Q[v, w, z] / (v^6, w^37, z^22). Polynomials are stored as
numerator dictionaries over a positive common denominator, using Python
ints. Multiplication is ordinary sparse convolution with the truncation
above. Nothing in this file imports or calls the published evaluator,
its packed product, or its Fraction oracle.

Leaf assignment for an ordered role tuple (i, j, a, b), taken from the
published recurrence rather than from its code:

- j, the second eliminated axis, is the constant 1 and contributes degree
  (1, 1). Its powers are the reverse variable v, carried by term shifts.
- a is the constant 1 and contributes degree (0, 1).
- b is the monomial z and contributes degree (0, 1).

A sum node of declared degree (deg, total) and terms (c, du, factors)
contributes, for each term whose recomputed total-degree slack dt is
strictly below 37 and whose du is strictly below 6,

    c * v^du * w^dt * product over (symbol, exponent) of that symbol's
    polynomial raised to the exponent,

truncated in the quotient ring. dt is

    total - sum(child total degree * exponent).

du must equal deg - sum(child degree * exponent). The root is the same
kind of product, multiplied by the root coefficient and shifted by the
root reverse shift in v only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path


V, W, Z = 6, 37, 22
WV = W * V  # 222; key = r + V * w + WV * z


def encode(r: int, w: int, z: int) -> int:
    return r + V * w + WV * z


def decode(key: int) -> tuple[int, int, int]:
    r = key % V
    rest = key // V
    return r, rest % W, rest // W


def canon(terms: dict[int, int], den: int) -> tuple[dict[int, int], int]:
    if not terms:
        return {}, 1
    if den < 0:
        den = -den
        terms = {key: -coeff for key, coeff in terms.items()}
    gap = abs(den)
    for coeff in terms.values():
        gap = math.gcd(gap, coeff)
        if gap == 1:
            break
    if gap != 1:
        terms = {key: coeff // gap for key, coeff in terms.items()}
        den //= gap
    return terms, den


ZERO: tuple[dict[int, int], int] = ({}, 1)
ONE: tuple[dict[int, int], int] = ({0: 1}, 1)
Z_MONOMIAL: tuple[dict[int, int], int] = ({encode(0, 0, 1): 1}, 1)


def is_one(poly: tuple[dict[int, int], int]) -> bool:
    terms, den = poly
    return den == 1 and terms == {0: 1}


def scale_shift(poly, numer: int, denom: int, du: int, dt: int):
    """Multiply by numer/denom and by v^du * w^dt. Drop truncated terms."""
    if numer == 0 or du >= V or dt >= W or not poly[0]:
        return ZERO
    out: dict[int, int] = {}
    for key, coeff in poly[0].items():
        r, w, z = decode(key)
        r += du
        w += dt
        if r < V and w < W:
            out[encode(r, w, z)] = coeff * numer
    return canon(out, poly[1] * denom)


def mul(left, right):
    if not left[0] or not right[0]:
        return ZERO
    if is_one(left):
        return right
    if is_one(right):
        return left
    if len(left[0]) > len(right[0]):
        left, right = right, left
    out: dict[int, int] = {}
    for key_l, coeff_l in left[0].items():
        r_l, w_l, z_l = decode(key_l)
        for key_r, coeff_r in right[0].items():
            r = r_l + key_r % V
            if r >= V:
                continue
            rest = key_r // V
            w = w_l + rest % W
            if w >= W:
                continue
            z = z_l + rest // W
            if z >= Z:
                continue
            key = encode(r, w, z)
            total = out.get(key, 0) + coeff_l * coeff_r
            if total:
                out[key] = total
            else:
                out.pop(key, None)
    return canon(out, left[1] * right[1])


def power(poly, exponent: int):
    if exponent == 0:
        return ONE
    if exponent == 1:
        return poly
    terms, den = poly
    if len(terms) == 1:
        key, coeff = next(iter(terms.items()))
        r, w, z = decode(key)
        r *= exponent
        w *= exponent
        z *= exponent
        if r >= V or w >= W or z >= Z or coeff == 0:
            return ZERO
        return canon({encode(r, w, z): coeff ** exponent}, den ** exponent)
    result = ONE
    base = poly
    while exponent:
        if exponent & 1:
            result = mul(result, base)
        exponent >>= 1
        if exponent:
            base = mul(base, base)
    return result


def add(left, right):
    if not right[0]:
        return left
    if not left[0]:
        return right
    den = math.lcm(left[1], right[1])
    scale_l = den // left[1]
    scale_r = den // right[1]
    out = {key: coeff * scale_l for key, coeff in left[0].items()}
    for key, coeff in right[0].items():
        total = out.get(key, 0) + coeff * scale_r
        if total:
            out[key] = total
        else:
            out.pop(key, None)
    return canon(out, den)


def polynomial_to_fractions(poly) -> dict[tuple[int, int, int], tuple[int, int]]:
    den = poly[1]
    return {decode(key): (coeff, den) for key, coeff in poly[0].items()}


def self_test() -> None:
    assert mul(Z_MONOMIAL, power(Z_MONOMIAL, 21)) == ZERO
    assert power(Z_MONOMIAL, 7) == ({encode(0, 0, 7): 1}, 1)
    assert power(({encode(1, 0, 0): 1}, 1), 6) == ZERO
    assert power(({encode(0, 1, 0): 1}, 1), 37) == ZERO
    one_plus_z = ({0: 1, encode(0, 0, 1): 1}, 1)
    cube = power(one_plus_z, 3)
    assert cube == (
        {
            0: 1,
            encode(0, 0, 1): 3,
            encode(0, 0, 2): 3,
            encode(0, 0, 3): 1,
        },
        1,
    )
    # (1/2) * v^2 * w^4
    shifted = scale_shift(ONE, 1, 2, 2, 4)
    assert shifted == ({encode(2, 4, 0): 1}, 2)
    # Two canceling terms leave the zero polynomial.
    positive = scale_shift(ONE, 1, 3, 0, 0)
    negative = scale_shift(ONE, -1, 3, 0, 0)
    assert add(positive, negative) == ZERO
    # Node: degree 1, total 2, single term (1/2) * j * a with the shifts
    # required by those degrees. j and a are both the constant 1.
    degree, total = 1, 2
    factors = [(1, 1), (2, 1)]
    child = {1: (1, 1), 2: (0, 1)}
    du = degree - sum(child[j][0] * e for j, e in factors)
    dt = total - sum(child[j][1] * e for j, e in factors)
    assert (du, dt) == (0, 0)
    node = scale_shift(mul(ONE, ONE), 1, 2, du, dt)
    assert node == ({0: 1}, 2)
    # Root b^2, coefficient 5, reverse shift 0, is 5 z^2.
    root = scale_shift(power(Z_MONOMIAL, 2), 5, 1, 0, 0)
    assert root == ({encode(0, 0, 2): 5}, 1)


def factor(values, cache, symbol: int, exponent: int):
    if exponent == 1:
        return values[symbol]
    per = cache.setdefault(symbol, {})
    found = per.get(exponent)
    if found is None:
        found = power(values[symbol], exponent)
        per[exponent] = found
    return found


def evaluate_edge(compact: dict, roles: list[int]) -> dict:
    if sorted(roles) != [0, 1, 2, 3]:
        raise ValueError('roles must be a permutation of 0,1,2,3')
    first, second, axis_a, axis_b = roles
    if compact['firstEliminatedAxis'] != first or compact['secondEliminatedAxis'] != second:
        raise ValueError('compact pair does not match the requested roles')
    if compact['remainingAxes'] != sorted((axis_a, axis_b)):
        raise ValueError('remaining axes do not match the requested roles')
    nodes = compact['sumNodes']
    degree = {second: (1, 1), axis_a: (0, 1), axis_b: (0, 1)}
    for node in nodes:
        degree[node['sourceSymbol']] = (node['degree'], node['totalDegreeBound'])
    uses: dict[int, int] = {}
    for node in nodes:
        for _coeff, _du, factors_ in node['terms']:
            for symbol, _exponent in factors_:
                uses[symbol] = uses.get(symbol, 0) + 1
    for symbol, _exponent in compact['root']['factors']:
        uses[symbol] = uses.get(symbol, 0) + 1
    values = {second: ONE, axis_a: ONE, axis_b: Z_MONOMIAL}
    cache: dict[int, dict[int, tuple]] = {}
    started = time.monotonic()
    for index, node in enumerate(nodes):
        acc = ZERO
        declared = degree[node['sourceSymbol']]
        for coeff, du, factors_ in node['terms']:
            if du < 0:
                raise ValueError('negative reverse shift')
            slack = declared[1] - sum(degree[symbol][1] * exponent for symbol, exponent in factors_)
            expected_du = declared[0] - sum(degree[symbol][0] * exponent for symbol, exponent in factors_)
            if du != expected_du or expected_du < 0 or slack < 0:
                raise ValueError(f'degree shift mismatch at symbol {node["sourceSymbol"]}')
            if slack < W and du < V:
                product = ONE
                for symbol, exponent in factors_:
                    if exponent < 0:
                        raise ValueError('negative exponent')
                    product = mul(product, factor(values, cache, symbol, exponent))
                numer = int(coeff[0])
                denom = int(coeff[1])
                if denom <= 0:
                    raise ValueError('term denominator must be positive')
                acc = add(acc, scale_shift(product, numer, denom, du, slack))
            for symbol, _exponent in factors_:
                uses[symbol] -= 1
                if uses[symbol] == 0 and symbol >= 16:
                    values.pop(symbol, None)
                    cache.pop(symbol, None)
        values[node['sourceSymbol']] = acc
        if (index + 1) % 1000 == 0:
            live = sum(len(poly[0]) for poly in values.values())
            print(
                json.dumps({
                    'processed': index + 1,
                    'total': len(nodes),
                    'liveSymbols': len(values),
                    'liveTerms': live,
                    'elapsedSeconds': round(time.monotonic() - started, 3),
                }),
                flush=True,
            )
    product = ONE
    for symbol, exponent in compact['root']['factors']:
        product = mul(product, power(values[symbol], exponent))
    root_coeff = compact['root']['coefficient']
    quotient = scale_shift(
        product,
        int(root_coeff[0]),
        int(root_coeff[1]),
        int(compact['root']['reverseShift']),
        0,
    )
    rows = []
    den = quotient[1]
    for key, numer in quotient[0].items():
        r, w, z = decode(key)
        rows.append([r, w, z, numer, den])
    rows.sort()
    return {
        'rows': rows,
        'elapsedSeconds': round(time.monotonic() - started, 3),
        'sumNodes': len(nodes),
    }


def rows_over_common_denominator(rows, common: int) -> list[list]:
    encoded = []
    for r, w, z, numer, den in rows:
        if common % den != 0:
            raise ValueError(f'denominator {den} does not divide common denominator {common}')
        encoded.append([r, w, z, str(numer * (common // den))])
    encoded.sort()
    return encoded


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    self_test()
    parser = argparse.ArgumentParser()
    parser.add_argument('--compact', type=Path, required=True)
    parser.add_argument('--clearing', type=Path, required=True)
    parser.add_argument('--pins', type=Path, required=True)
    parser.add_argument('--roles', default='0123')
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    if len(args.roles) != 4 or not args.roles.isdigit():
        raise SystemExit('roles must be four digits')
    roles = [int(char) for char in args.roles]
    pair = args.roles[:2]
    pins = json.loads(args.pins.read_text())
    pair_pin = pins['pairs'][pair]
    expected = pins['expectedQuotients'][args.roles]
    compact_sha = sha256(args.compact)
    clearing_sha = sha256(args.clearing)
    if compact_sha != pair_pin['historicalCompactSHA256']:
        raise SystemExit('regenerated compact bytes do not match the published pin')
    if clearing_sha != pair_pin['historicalClearingSHA256']:
        raise SystemExit('regenerated clearing bytes do not match the published pin')
    compact = json.loads(args.compact.read_text())
    clearing = json.loads(args.clearing.read_text())
    common = int(expected['commonDenominator'])
    if int(clearing['root']['denominator']) != common:
        raise SystemExit('clearing root denominator disagrees with the published quotient denominator')
    evaluated = evaluate_edge(compact, roles)
    encoded = rows_over_common_denominator(evaluated['rows'], common)
    digest = hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest()
    receipt = {
        'schema': 'hsd-independent-quotient-edge-v1',
        'evidenceClass': 'source-regenerated input, independent rational arithmetic, compared with the published coefficient digest',
        'notSuppliedQuotientReplay': True,
        'authorsEvaluatorExecuted': False,
        'roles': roles,
        'pinnedCompactSHA256': compact_sha,
        'pinnedClearingSHA256': clearing_sha,
        'sumNodes': evaluated['sumNodes'],
        'commonDenominator': str(common),
        'retainedNonzeros': len(encoded),
        'integerCoefficientSHA256': digest,
        'publishedIntegerCoefficientSHA256': expected['integerCoefficientSHA256'],
        'publishedRetainedNonzeros': expected['retainedNonzeros'],
        'coefficientHashMatched': digest == expected['integerCoefficientSHA256'],
        'nonzeroCountMatched': len(encoded) == expected['retainedNonzeros'],
        'integerRows': encoded,
        'leastDenominatorRows': [
            [r, w, z, str(numer), str(den)] for r, w, z, numer, den in evaluated['rows']
        ],
        'elapsedSeconds': evaluated['elapsedSeconds'],
        'selfTest': 'PASS',
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({
        'coefficientHashMatched': receipt['coefficientHashMatched'],
        'nonzeroCountMatched': receipt['nonzeroCountMatched'],
        'integerCoefficientSHA256': digest,
        'retainedNonzeros': len(encoded),
        'elapsedSeconds': evaluated['elapsedSeconds'],
    }, indent=2))
    if not (receipt['coefficientHashMatched'] and receipt['nonzeroCountMatched']):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
