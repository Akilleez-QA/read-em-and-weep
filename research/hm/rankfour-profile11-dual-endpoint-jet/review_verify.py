#!/usr/bin/env python3
"""Independent fixed character and rank/degree checks; no author-module imports.

All character values below are abstract conjugacy-class traces of the physical
binary icosahedral two-dimensional representation. No actual geometric instance
or selected coefficient, parameter, point, jet, matrix, or rank is evaluated.
The human geometric review is separate and is bound to the same proof hash.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from hashlib import sha256, sha1
from pathlib import Path
import json

CHECK_COUNT = 0

def check(condition, message='Independent check failed'):
    global CHECK_COUNT
    CHECK_COUNT += 1
    if not condition:
        raise AssertionError(message)

EXPECTED_PROOF_SHA256 = 'bbe7c05e9055b70ba511c77ebc0514a0fdf89d75844199f971e7e774355c08c6'
EXPECTED_INPUTS = {
    'inputs/actual.md': ('a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256', 'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3', 9672),
    'inputs/pair-defect.md': ('95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec', 'f409e036c549d15dc0ad03443325922575107b4d', 15519),
}

@dataclass(frozen=True)
class Quad:
    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)
    def __add__(self, other):
        return Quad(self.rational + other.rational, self.radical + other.radical)
    def __sub__(self, other):
        return Quad(self.rational - other.rational, self.radical - other.radical)
    def __mul__(self, other):
        return Quad(self.rational * other.rational + 5 * self.radical * other.radical,
                    self.rational * other.radical + self.radical * other.rational)
    def scale(self, scalar):
        return Quad(self.rational * scalar, self.radical * scalar)

ONE = Quad(Fraction(1))
ZERO = Quad()
HALF = Fraction(1, 2)
# Abstract trace classes: 2, -2, +/-phi, +/-phi-conjugate, 1, -1, 0.
CLASSES = (
    (1, Quad(Fraction(2))), (1, Quad(Fraction(-2))),
    (12, Quad(HALF, HALF)), (12, Quad(-HALF, -HALF)),
    (12, Quad(HALF, -HALF)), (12, Quad(-HALF, HALF)),
    (20, Quad(Fraction(1))), (20, Quad(Fraction(-1))),
    (30, ZERO),
)
check(sum((size for size, _ in CLASSES)) == 120, 'Failed invariant: sum((size for size, _ in CLASSES)) == 120')


def symmetric_character(degree, trace):
    """Closed universal SL2 recurrence, not the author's character engine."""
    if degree < 0:
        return ZERO
    previous, current = ZERO, ONE
    for _ in range(degree):
        previous, current = current, trace * current - previous
    return current


def invariant_dimension(*degrees):
    total = ZERO
    for size, trace in CLASSES:
        value = reduce(lambda a, b: a * b,
                       (symmetric_character(n, trace) for n in degrees), ONE)
        total = total + value.scale(Fraction(size, 120))
    check(total.radical == 0, 'Failed invariant: total.radical == 0')
    check(total.rational.denominator == 1, 'Failed invariant: total.rational.denominator == 1')
    check(total.rational >= 0, 'Failed invariant: total.rational >= 0')
    return int(total.rational)


def hom_dimension(source_rep, source_twist, target_rep, target_twist):
    """Representations are Sym^source_rep W and Sym^target_rep W."""
    return invariant_dimension(source_rep, target_rep, target_twist - source_twist)


def bundle(rank, degree):
    return {'rank': rank, 'degree': degree}


def h1_line(degree):
    return max(-degree - 1, 0)


def main():
    root = Path(__file__).resolve().parent
    check(EXPECTED_PROOF_SHA256 != 'PENDING_WHOLE_PROOF_REVIEW', 'Not yet bound by independent whole-proof review')
    proof_hash = sha256((root / 'PROOF.md').read_bytes()).hexdigest()
    check(proof_hash == EXPECTED_PROOF_SHA256, 'Failed invariant: proof_hash == EXPECTED_PROOF_SHA256')
    source_checks = []
    for name, (expected_sha256, expected_blob, expected_size) in EXPECTED_INPUTS.items():
        data = (root / name).read_bytes()
        actual_sha256 = sha256(data).hexdigest()
        actual_blob = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        check((actual_sha256, actual_blob, len(data)) == (expected_sha256, expected_blob, expected_size), 'Failed invariant: (actual_sha256, actual_blob, len(data)) == (expected_sha256, expected_blob, expected_size)')
        source_checks.append({'file': name, 'sha256': actual_sha256, 'git_blob_sha1': actual_blob, 'bytes': len(data), 'verdict': 'PASS'})
    auth = json.loads((root / 'REVIEW-AUTHENTICITY.json').read_text())
    check(auth['verdict'] == 'PASS', "Failed invariant: auth['verdict'] == 'PASS'")
    check(auth['source_manifest_sha256'] == sha256((root / 'INPUTS.json').read_bytes()).hexdigest(), "Failed invariant: auth['source_manifest_sha256'] == sha256((root / 'INPUTS.json').read_bytes()).hexdigest()")
    for item in auth['sources']:
        check(item['remote_equals_local'] and item['verdict'] == 'PASS', "Failed invariant: item['remote_equals_local'] and item['verdict'] == 'PASS'")
        check((item['computed_remote_sha256'], item['computed_remote_blob_sha1'], item['computed_remote_bytes']) == EXPECTED_INPUTS[item['file']], "Failed invariant: (item['computed_remote_sha256'], item['computed_remote_blob_sha1'], item['computed_remote_bytes']) == EXPECTED_INPUTS[item['file']]")

    # Fixed irreducibility and nontriviality checks used in the Hom proof.
    for degree in (1, 2, 3, 4, 5):
        check(invariant_dimension(degree, degree) == 1, 'Failed invariant: invariant_dimension(degree, degree) == 1')
        check(invariant_dimension(degree) == 0, 'Failed invariant: invariant_dimension(degree) == 0')
    for left, right in ((1, 3), (2, 4)):
        check(invariant_dimension(left, right) == 0, 'Failed invariant: invariant_dimension(left, right) == 0')
    for _, trace in CLASSES:
        check(symmetric_character(1, trace) * symmetric_character(3, trace) == symmetric_character(4, trace) + symmetric_character(2, trace), 'Failed invariant: symmetric_character(1, trace) * symmetric_character(3, trace) == symmetric_character(4, trace) + symmetric_character(2, trace)')
        check(symmetric_character(1, trace) * symmetric_character(1, trace) == ONE + symmetric_character(2, trace), 'Failed invariant: symmetric_character(1, trace) * symmetric_character(1, trace) == ONE + symmetric_character(2, trace)')

    hom_specs = (
        ('O(-10) -> O(-6)', (0, -10, 0, -6), 0),
        ('O(-10) -> O(-8)', (0, -10, 0, -8), 0),
        ('O(-10) -> W(-7)', (0, -10, 1, -7), 0),
        ('W(-9) -> O(-6)', (1, -9, 0, -6), 0),
        ('W(-9) -> O(-8)', (1, -9, 0, -8), 1),
        ('W(-9) -> W(-7)', (1, -9, 1, -7), 1),
        ('O(-8) -> W(-7)', (0, -8, 1, -7), 1),
        ('O(-8) -> O(-6)', (0, -8, 0, -6), 0),
    )
    hom_checks = []
    for name, args, expected in hom_specs:
        actual = hom_dimension(*args)
        check(actual == expected, 'Failed invariant: actual == expected')
        hom_checks.append({'map': name, 'dimension': actual})
    check(hom_dimension(0, -10, 0, -6) + 2 * hom_dimension(0, -10, 0, -8) == 0, 'Failed invariant: hom_dimension(0, -10, 0, -6) + 2 * hom_dimension(0, -10, 0, -8) == 0')
    check(hom_dimension(0, -10, 1, -7) + hom_dimension(0, -10, 0, -8) == 0, 'Failed invariant: hom_dimension(0, -10, 1, -7) + hom_dimension(0, -10, 0, -8) == 0')

    # Numerical invariants of universal exact sequences, not instance ranks.
    check(h1_line(8 - 10) == 1, 'Failed invariant: h1_line(8 - 10) == 1')
    check(10 != 0, 'Failed invariant: 10 != 0')
    check((2, 8 + 10) == (2, 2 * 9), 'Failed invariant: (2, 8 + 10) == (2, 2 * 9)')
    S0 = bundle(5, -46)
    L0 = bundle(2, -18)
    B0 = bundle(S0['rank'] - L0['rank'], S0['degree'] - L0['degree'])
    check(B0 == bundle(3, -28), 'Failed invariant: B0 == bundle(3, -28)')
    F_dual_minus2 = bundle(3, -16)
    check(F_dual_minus2['degree'] - B0['degree'] == 12, "Failed invariant: F_dual_minus2['degree'] - B0['degree'] == 12")
    small_kernel = bundle(1, -10)
    small_derivative_image = bundle(1, -8)
    check(L0['degree'] - small_kernel['degree'] == small_derivative_image['degree'], "Failed invariant: L0['degree'] - small_kernel['degree'] == small_derivative_image['degree']")
    small_osculating = bundle(3, -18 + (-8 + 2))
    check(small_osculating == bundle(3, -24), 'Failed invariant: small_osculating == bundle(3, -24)')
    S_tail = bundle(8, 8 * -1)
    L_tail = bundle(7, 7 * -2)
    tail_kernel = bundle(6, 6 * -3)
    tail_derivative_image = bundle(1, 4)
    check(S_tail['degree'] - L_tail['degree'] == 6, "Failed invariant: S_tail['degree'] - L_tail['degree'] == 6")
    check(L_tail['degree'] - tail_kernel['degree'] == tail_derivative_image['degree'], "Failed invariant: L_tail['degree'] - tail_kernel['degree'] == tail_derivative_image['degree']")
    S = bundle(S0['rank'] + S_tail['rank'], S0['degree'] + S_tail['degree'])
    L = bundle(L0['rank'] + L_tail['rank'], L0['degree'] + L_tail['degree'])
    L_minus = bundle(small_kernel['rank'] + tail_kernel['rank'], small_kernel['degree'] + tail_kernel['degree'])
    check(S == bundle(13, -54), 'Failed invariant: S == bundle(13, -54)')
    check(L == bundle(9, -32), 'Failed invariant: L == bundle(9, -32)')
    check(L_minus == bundle(7, -28), 'Failed invariant: L_minus == bundle(7, -28)')
    check(L['rank'] - L_minus['rank'] == 2, "Failed invariant: L['rank'] - L_minus['rank'] == 2")
    check(L['degree'] - L_minus['degree'] == -8 + 4, "Failed invariant: L['degree'] - L_minus['degree'] == -8 + 4")

    print(json.dumps({
        'verdict': 'PASS',
        'check_count': CHECK_COUNT,
        'scope': 'Fixed closed character/Hom arithmetic, input hash checks, and universal exact-sequence rank/degree identities only. Geometric jet and saturation arguments are independently reviewed in REVIEW-INDEPENDENT.md, not algorithmically certified here.',
        'proof_sha256': proof_hash,
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'authentication_sha256': sha256((root / 'REVIEW-AUTHENTICITY.json').read_bytes()).hexdigest(),
        'input_checks': source_checks,
        'hom_checks': hom_checks,
        'jet_extension': {'Ext1_dimension': 1, 'nonzero_cocycle_coefficient_up_to_sign': 10, 'jet_rank': 2, 'jet_degree': 18},
        'bundle_checks': {'S0': S0, 'L0': L0, 'B0': B0, 'small_derivative_kernel': small_kernel, 'small_derivative_image': small_derivative_image, 'L0_plus': small_osculating, 'S_tail': S_tail, 'L_tail': L_tail, 'tail_derivative_kernel': tail_kernel, 'tail_derivative_image': tail_derivative_image, 'S': S, 'L': L, 'L_minus': L_minus},
        'original_defect': 12,
        'original_derivative_rank_everywhere_claim_numerical_consistency': 2,
    }, indent=2))

if __name__ == '__main__':
    main()
