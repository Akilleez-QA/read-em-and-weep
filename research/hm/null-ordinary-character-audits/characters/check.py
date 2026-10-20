"""Bounded synthetic XOR/polynomial check; no actual source-model evaluation."""
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

P, Q, FULL = 0b0011, 0b1100, 0b1111
LOW = [0, 1, 2, 4, 8]
u_squared = sorted({a ^ b for a in LOW for b in LOW})
linear = sorted({a ^ b for a in (P, Q) for b in LOW})
hh2 = sorted({0} | {1 << i ^ 1 << j for i in range(4) for j in range(i + 1, 4)})
assert FULL not in u_squared and FULL not in linear and FULL not in hh2
assert {a ^ b for a in (P, Q) for b in (P, Q)} == {0, FULL}

def sign(mask, g):
    return (-1) ** ((mask & g).bit_count())

selection = []
for total in range(13):
    full_monomials = []
    for a in range(total + 1):
        b = total - a
        mask = (P if a % 2 else 0) ^ (Q if b % 2 else 0)
        for g in range(16):
            assert sign(mask, g) == sign(P, g) ** a * sign(Q, g) ** b
        assert (mask == FULL) == (a % 2 == b % 2 == 1)
        if mask == FULL:
            full_monomials.append([a, b])
    assert not (total % 2 and full_monomials)
    selection.append({'total_degree': total, 'full_sign_exponents': full_monomials})
assert selection[4]['full_sign_exponents'] == [[1, 3], [3, 1]]

def curvature(series, bracket):
    """All inputs degree one; d=0; degree-two outputs central."""
    result = defaultdict(Fraction)
    for (exp_a, gen_a), coefficient_a in series.items():
        for (exp_b, gen_b), coefficient_b in series.items():
            target = bracket.get((gen_a, gen_b))
            if target is not None:
                exp = tuple(a+b for a, b in zip(exp_a, exp_b))
                result[exp, target] += Fraction(coefficient_a * coefficient_b, 2)
    return {key: value for key, value in result.items() if value}

# Enumerate small integer choices only to test the formal bilinear identity.
choices_checked = 0
for alpha in range(-1, 2):
    for beta in range(-1, 2):
        series = {((1,), 'x'): 1, ((1,), 'y'): 1,
                  ((2,), 'z'): alpha, ((2,), 'v'): beta}
        result = curvature(series, {('z', 'v'): 'w', ('v', 'z'): 'w'})
        expected = {((4,), 'w'): Fraction(alpha * beta)} if alpha * beta else {}
        assert result == expected
        choices_checked += 1

chars = {'x': P, 'z': P, 'y': Q, 'w': FULL}
for alpha in range(-1, 2):
    series = {((1, 0), 'x'): 1, ((0, 1), 'y'): 1, ((3, 0), 'z'): alpha}
    for ((a, b), gen), coefficient in series.items():
        assert chars[gen] == ((P if a % 2 else 0) ^ (Q if b % 2 else 0))
    result = curvature(series, {('z', 'y'): 'w', ('y', 'z'): 'w'})
    expected = {((3, 1), 'w'): Fraction(alpha)} if alpha else {}
    assert result == expected
    choices_checked += 1

report = {
    'status': 'passed',
    'scope': 'Bounded synthetic XOR and sparse-polynomial identities only',
    'u_squared_character_masks': u_squared,
    'linear_variation_character_masks': linear,
    'HH2_character_masks': hh2,
    'selection_through_total_degree': 12,
    'selection': selection,
    'synthetic_integer_parameter_cases': choices_checked,
    'unrestricted_acceleration_curvature': 'alpha*beta*h^4*w',
    'strict_equivariant_curvature': 'alpha*s^3*t*w',
    'actual_obstruction_values_computed': False,
    'source_vanishings_recomputed': False,
    'all_order_ambient_existence_proved': False,
}
Path(__file__).with_name('check-result.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
