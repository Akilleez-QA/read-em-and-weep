"""Independent small Laurent-duality controls, not physical source tests."""
import itertools
import json
from pathlib import Path
from weighted_requests import build, index, need

result = build()
# Exhaust all 81 possible dual monomials and recover the pinned base-three order.
for k, e in enumerate(itertools.product((-3, -2, -1), repeat=4)):
    need(index(tuple(-x - 1 for x in e)) == k, 'Laurent basis order')
need(index((2, 2, 2, 0)) == 2, 'published m2220 calibration')
# Reconstruct values at several integer points directly from elementary sections,
# independently of the dictionary multiplication used by the request generator.
for point in ((1, 2, 3, 4), (-2, 3, 0, 1), (0, 0, 0, 0)):
    v = [sum(__import__('math').prod(point[i] for i in subset)
             for subset in itertools.combinations(range(4), k)) for k in range(5)]
    q = point[0] * point[1] + point[2] * point[3]
    for request in result['requests']:
        actual = sum(t['coefficient'] * __import__('math').prod(x ** m for x, m in zip(point, t['dual_monomial']))
                     for t in request['terms'])
        monomial = request['base_monomial']
        expected = q * q if request['block'] == 'Q^2' else (
            v[monomial[0]] * q if len(monomial) == 1 else v[monomial[0]] * v[monomial[1]])
        need(actual == expected, 'wrong polynomial weighting')
# Deliberate out-of-range and altered selection inputs must fail closed under -O.
for bad in ((3, 0, 0, 0), (True, 0, 0, 0), (0, 0, 0)):
    try:
        index(bad)
    except ValueError:
        pass
    else:
        raise ValueError('accepted invalid dual monomial')
try:
    build(b'{}')
except ValueError:
    pass
else:
    raise ValueError('accepted changed selection')
need(all(gate is False for gate in result['gates'].values()), 'released source gate')
saved = Path(__file__).with_name('weighted-requests.json')
need(json.loads(saved.read_text()) == result, 'saved request drift')
print('PASS: 81 dual indices, 96 direct polynomial checks, invalid-input controls; no source values')
