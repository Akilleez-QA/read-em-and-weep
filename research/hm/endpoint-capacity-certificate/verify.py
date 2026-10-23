"""Synthetic bounded tests and constant-size huge-integer certificates."""
import copy
import hashlib
import json
from pathlib import Path
from capacity import solve, verify, value, equality_filter, classify_degree

counts = {}
def check(condition, group):
    if not condition:
        raise RuntimeError('failed: ' + group)
    counts[group] = counts.get(group, 0) + 1

def rejects(call, group):
    try:
        call()
    except ValueError:
        check(True, group)
    else:
        check(False, group)

for n in range(1, 25):
    for l2 in range(-12, 13):
        for l1 in range(l2, 13):
            cert = solve(n, l1, l2)
            check(verify(cert), 'certificate')
            brute = [(h*l1+(n-h)*l2-h*(h+1)-(n-h)*(n-h+1), h)
                     for h in range((n+1)//2, n+1)]
            best = max(v for v, h in brute)
            check(cert['maximum'] == best and cert['heights'] ==
                  [h for v, h in brute if v == best], 'synthetic_exhaustive')
            shifted = solve(n, l1+17, l2+17)
            check(shifted['heights'] == cert['heights'] and
                  shifted['maximum'] == best+17*n, 'translation')
            for t0 in (-20, -1, 0, 7, 20):
                filtered = equality_filter(cert, best, t0, actual_top_flags_proved=True)
                check(filtered['surviving_heights'] ==
                      [h for v, h in brute if v == best and l1-2*h <= t0-h],
                      'conditional_equality_filter')

# Synthetic parity, exact tie, clipped boundary, singleton domain.
for args, heights in [((6, 0, 0), [3]), ((5, 0, 0), [3]),
                      ((6, 2, 0), [3, 4]), ((6, 100, 0), [6]),
                      ((1, 0, 0), [1]), ((6, 10, 0), [5, 6])]:
    check(solve(*args)['heights'] == heights, 'parity_tie_boundary')

huge = []
for n, l1, l2 in [(10**100, 2, 0), (10**100+1, 10**150, -10**150),
                   (10**100, -10**120, -10**120), (10**100+1, 1, -1)]:
    cert = solve(n, l1, l2)
    check(verify(cert), 'huge_no_enumeration')
    huge.append(cert)

for args in [(0, 1, 0), (-1, 1, 0), (3, 0, 1), (True, 2, 1),
             (3, 1.0, 0), (3, 2, False), ('3', 2, 1)]:
    rejects(lambda args=args: solve(*args), 'malformed')
base = solve(6, 2, 0)
for key, bad in [('maximum', base['maximum']+1), ('square_distance', 0),
                 ('heights', [3]), ('heights', [4]), ('heights', [4, 3]),
                 ('heights', [3, 3]), ('heights', [True]), ('rank', True)]:
    c = copy.deepcopy(base); c[key] = bad
    rejects(lambda c=c: verify(c), 'tampering')
rejects(lambda: verify({}), 'tampering')
for degree in (base['maximum']-1, base['maximum']+1):
    rejects(lambda degree=degree: equality_filter(base, degree, 0,
            actual_top_flags_proved=True), 'equality_misuse')
for flag in (False, None, 1, 'proved'):
    rejects(lambda flag=flag: equality_filter(base, base['maximum'], 0,
            actual_top_flags_proved=flag), 'equality_misuse')
check(equality_filter(base, base['maximum'], -100,
      actual_top_flags_proved=True)['excluded_equality'], 'all_equality_heights_excluded')
for delta, expected in [(-1, 'below_capacity_no_exclusion'), (0, 'attains_capacity'),
                        (1, 'excluded_above_capacity')]:
    check(classify_degree(base, base['maximum']+delta) == expected, 'degree_trichotomy')

# Already-known PR1138 regressions ONLY, not new deductions or new row searches.
known = []
for label, triple, degree, maximum in [(5, (6,-6,-18), -36, -42),
        (9, (6,-8,-18), -34, -46), (10, (6,-11,-11), -38, -49),
        (2, (6,-4,-18), -38, -38)]:
    cert = solve(10, *triple[:2])
    check(verify(cert) and cert['maximum'] == maximum, 'already_known_regressions')
    known.append(dict(original_index=label, degree_triple=triple, degree=degree,
                      certificate=cert, status='already_known_PR1138'))
check(known[-1]['certificate']['heights'] == [7,8], 'already_known_regressions')
check(equality_filter(known[-1]['certificate'], -38, -2,
      actual_top_flags_proved=True)['surviving_heights'] == [8], 'already_known_regressions')
print(json.dumps(dict(status='PASS', checks=counts, total=sum(counts.values()),
    huge_integer_certificates=huge, already_known_regressions=known), indent=2, sort_keys=True))
