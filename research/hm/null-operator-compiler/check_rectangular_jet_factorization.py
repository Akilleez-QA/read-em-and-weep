"""Exact origin-jet factorization checker for complete first-order Laurent operators.

No source coefficients are evaluated. Coefficients live in a formal polynomial
ring over Q. An Operator is INPUT mathematics, never supplied by a certificate.
This checker does not authenticate an operator as the physical E*Phi; the actual
metadata entry point refuses unsupported/uncompiled detector semantics.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


class Refused(ValueError):
    pass


def polynomial(items):
    """Canonical exact polynomial: (formal-parameter exponent tuple, Q scalar)."""
    out = {}
    for powers, value in items:
        if any(type(x) is not int or x < 0 for x in powers):
            raise Refused('invalid formal parameter exponent')
        if isinstance(value, bool) or not isinstance(value, (int, str, Fraction)):
            raise Refused('coefficient must be exact rational, never float')
        powers = tuple(powers)
        while powers and powers[-1] == 0:
            powers = powers[:-1]
        try:
            value = Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise Refused('invalid rational') from exc
        out[powers] = out.get(powers, Fraction()) + value
    return tuple(sorted((p, c) for p, c in out.items() if c))


def add(a, b):
    return polynomial(a + b)


def scale(a, k):
    return polynomial((p, c * k) for p, c in a)


@dataclass(frozen=True)
class Term:
    edge: tuple
    kappa: tuple
    nu: tuple
    derivative: object  # None or a coordinate index
    coefficient: tuple
    # Semantics: coefficient * [z^kappa] z^nu partial_i(P_edge).
    # Coefficients may be formal polynomials, including sums with cancellation.


@dataclass(frozen=True)
class Operator:
    vertex_degrees: tuple
    character: tuple
    terms: tuple
    frame: str = 'standard-product-affine-origin'


def derive_row(op):
    """Derive the ENTIRE full-domain row without enumerating numerator boxes.

    Finite sum semantics makes all absent coefficients identically zero. Each
    monomial multiplier contributes to exactly one numerator exponent.
    """
    d = len(op.character)
    if any(type(x) is not int for x in op.character):
        raise Refused('invalid character')
    if not d or op.frame != 'standard-product-affine-origin':
        raise Refused('unsupported frame')
    if len(op.vertex_degrees) < 2:
        raise Refused('too few vertices')
    if any(len(v) != d or any(type(x) is not int or x < 0 for x in v)
           for v in op.vertex_degrees):
        raise Refused('invalid complete vertex degree table')
    row = {}
    for t in op.terms:
        if (len(t.edge) != 2 or any(type(v) is not int for v in t.edge)
                or not 0 <= t.edge[0] < t.edge[1] < len(op.vertex_degrees)):
            raise Refused('invalid exact owner edge')
        if len(t.kappa) != d or len(t.nu) != d:
            raise Refused('wrong coordinate dimension')
        if any(type(x) is not int for x in t.kappa + t.nu):
            raise Refused('nonintegral exponent')
        i = t.derivative
        if i is not None and (type(i) is not int or not 0 <= i < d):
            raise Refused('invalid derivative')
        a = tuple(t.kappa[j] - t.nu[j] + (j == i) for j in range(d))
        m = tuple(op.character[j] + sum(op.vertex_degrees[v][j] for v in t.edge)
                  for j in range(d))
        if not all(0 <= a[j] <= m[j] for j in range(d)):
            continue
        c = scale(polynomial(t.coefficient), 1 if i is None else a[i])
        key = (t.edge, a)
        row[key] = add(row.get(key, ()), c)
    return {k: v for k, v in row.items() if v}


def check(op, certificate):
    """Verify Q0 surjectivity and exact e=Q1^t ebar at the affine origin.

    Certificate cannot substitute a different operator, domain, or row support.
    No samples, asserted proof flags, or external zero-testing oracle are used.
    """
    if set(certificate) != {'kind', 'orders', 'quotient_row'}:
        raise Refused('unknown or missing certificate field')
    if certificate['kind'] != 'complete-origin-rectangular-v1':
        raise Refused('unsupported proof language')
    r = certificate['orders']
    d = len(op.character)
    if len(r) != d or any(type(x) is not int or x < 1 for x in r):
        raise Refused('invalid orders')
    row = derive_row(op)
    ceilings = tuple(1 + op.character[j] + min(v[j] for v in op.vertex_degrees)
                     for j in range(d))
    if any(r[j] > ceilings[j] for j in range(d)):
        raise Refused('Q0 not surjective')
    for (edge, a), coefficient in sorted(row.items()):
        if any(a[j] >= r[j] for j in range(d)):
            raise Refused(f'kernel witness: edge={edge}, exponent={a}, coefficient={coefficient}')
    proposed = {}
    for edge, a, c in certificate['quotient_row']:
        key = (tuple(edge), tuple(a))
        if key in proposed:
            raise Refused('duplicate quotient entry')
        if (len(a) != d or any(type(x) is not int or not 0 <= x < r[j]
                              for j, x in enumerate(a))):
            raise Refused('quotient entry outside stencil')
        if tuple(edge) not in combinations(range(len(op.vertex_degrees)), 2):
            raise Refused('quotient owner mismatch')
        proposed[key] = polynomial(c)
    proposed = {k: v for k, v in proposed.items() if v}
    if proposed != row:
        raise Refused('complete row identity failed')
    return {'factorization': True, 'Q0_surjective': True,
            'nonzero_row_entries': len(row), 'orders': list(r),
            'actual_detector_authenticated': False, 'execution_release': False}


def admit_current_actual_metadata(metadata, certificate):
    """Public actual-detector gate. Metadata is NOT a complete Laurent operator.

    Authentication of a future compiler must be implemented here, rather than
    trusting caller-supplied 'complete', hashes, samples, or proof-success flags.
    Fail closed even if these flags are forged or unresolved_leaves is erased.
    """
    if metadata.get('schema') != 'hm-refined-detector-metadata-v1':
        raise Refused('unsupported authenticated detector schema')
    raise Refused('actual E*Phi has no supported complete regularized numerator-operator compiler; '
                  'terminal seeds, envelopes and assertions cannot authenticate factorization')
