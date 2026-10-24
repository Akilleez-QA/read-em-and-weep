"""Fixed universal character, degree and formal-identity checks; no actual data."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import characters as ch

ROOT = Path(__file__).resolve().parent
checks = []

def require(condition, name):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

pins = {
    'inputs/lifted-jets-and-kernel-two.md': (
        'c565bd8b5b65829e99bdd96a7c5f076b01050465',
        'research/hm/rankfour-profile11-triplet-simultaneous-kernel-two-exclusion/PROOF.md',
        13703, '0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa',
        'cb46875b07d8d79e82aebe980685c418d975d87b'),
    'inputs/five-kernels.md': (
        '7d71f0e2a3963cff64a069198f4415c5cfd0fe9b',
        'research/hm/rankfour-profile11-triplet-kernels/PROOF.md',
        8501, '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a',
        '163ba2126b6130befcc2351db7f6910d85fac2ec'),
    'inputs/quartic-normal-map.md': (
        '06385eec63b85efac6cc25441d4b58d4fa5a8adb',
        'research/hm/rankfour-profile11-triplet-quartic-normal-map/PROOF.md',
        15127, '205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba',
        '243adcdfe618e0792f330534c5c74931ad2741ac'),
}
inputs = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(inputs) == 3 and {i['file'] for i in inputs} == set(pins),
        'three complete immutable originals')
for item in inputs:
    ref, path, n, sha, blob = pins[item['file']]
    data = (ROOT / item['file']).read_bytes()
    require(item['ref'] == ref and item['path'] == path, 'exact immutable ref and path')
    require(len(data) == item['bytes'] == n, 'complete input length')
    require(hashlib.sha256(data).hexdigest() == item['sha256'] == sha, 'complete input SHA256')
    require(hashlib.sha1(b'blob ' + str(n).encode() + bytes([0]) + data).hexdigest()
            == item['git_blob_sha1'] == blob, 'complete Git blob identity')
    require(item['url'] == 'https://github.com/Akilleez-QA/read-em-and-weep/blob/'
            + ref + '/' + path, 'exact immutable URL')
proof = (ROOT / 'PROOF.md').read_bytes()
require(len(proof) == 20248, 'frozen entire-proof bytes')
require(hashlib.sha256(proof).hexdigest()
        == 'c501c094dfe7cff853f8b0a64552b4a59478581a2d11921ec5f8f70f34bb0542',
        'frozen entire-proof hash')
require(ch.checks == 81, 'fixed exact-rational character consistency checks')

expected = {
    ('one', 0): {'one': 1}, ('one', 1): {'W': 1},
    ('one', 2): {'A': 1}, ('one', 3): {'S': 1},
    ('one', 4): {'D': 1}, ('one', 5): {'T': 1},
    ('one', 15): {'S': 1, 'T': 2},
    ('V', 1): {'T': 1}, ('P', 1): {'T': 1, 'Wp': 1},
    ('D', 1): {'S': 1, 'T': 1},
    ('T', 1): {'D': 1, 'V': 1, 'P': 1},
    ('S', 1): {'A': 1, 'D': 1},
    ('W', 1): {'one': 1, 'A': 1}, ('Wp', 1): {'P': 1},
    ('A', 7): {'S': 1, 'T': 3, 'Wp': 1},
    ('A', 6): {'V': 1, 'P': 2, 'D': 2},
}
for (r, n), value in expected.items():
    require(ch.product(r, n) == Counter(value), f'fixed identity {r} tensor Sym{n}')

h0_k5 = ch.product('V', 1) + ch.product('P', 1) + ch.product('D', 1)
require(h0_k5 == Counter({'S': 1, 'T': 3, 'Wp': 1}), 'only S,T,Wp at degree minus five')
require(ch.product('one', 15)['Wp'] == 0, 'Wp upper coherent derivative vanishes')
require(-10 - (-5) < 0, 'Wp lower coherent derivative vanishes by degree')
require(-5 - 2 < -5, 'Wp internal derivative vanishes by strict degree')
require(-4 - 2 < -4, 'top minus four line internal derivative vanishes')
require(ch.product('V', 1)['S'] == ch.product('P', 1)['S'] == 0,
        'S4 map has no V or P component')
require(ch.product('D', 1)['S'] == 1, 'unique S4 to D evaluation-kernel inclusion')
require(-4 - 2 < -5, 'octic initial derivative has zero projection modulo D')

# Four universal evaluation sequences in the octic ladder, plus the bottom row.
for j, rep in [(1, 'W'), (2, 'A'), (3, 'S'), (4, 'D')]:
    source_degree = j - 8
    quotient_degree = 2 * j - 8
    kernel_degree = j - 9
    require(ch.product('one', quotient_degree - source_degree)[rep] == 1,
            f'octic row {j} universal evaluation Hom has dimension one')
    require((j + 1) * source_degree - quotient_degree == j * kernel_degree,
            f'octic row {j} exact kernel degree')
    require((j + 1) * source_degree < 0, f'octic rank {j + 1} is negative')
require((-6) - 2 == -8, 'octic bottom forward map is O(-8) to itself')
require((-14) - (-8) < 0 and (-9) - (-8) < 0,
        'octic line cannot map to either actual F6 block')

# Formal differentiated pairings only: no functions, points or jets are evaluated.
zero_pairings = {(a, b) for a in range(4) for b in range(4)}
steps = []
for b, max_a in [(4, 2), (5, 1), (6, 0)]:
    for a in range(max_a + 1):
        require((a, b - 1) in zero_pairings and (a + 1, b - 1) in zero_pairings,
                f'formal derivative identity forces pairing ({a},{b}) to vanish')
        zero_pairings.add((a, b))
        steps.append([a, b])
require(all((0, b) in zero_pairings for b in range(7)),
        'formal order-three rectangle implies annihilation through original order six')

require(6 <= 10 < 12, 'at most one T6 highest block in rank ten')
require(10 - 6 == 4 < 5, 'rank-four tail cannot contain a D coefficient block')
require(ch.product('T', 1)['D'] == 1, 'unique actual fourth-jet inclusion in T6')
require(6 * (-5) - 5 * (-6) == 0, 'actual fifth over fourth jet quotient has degree zero')
require(max(-4, -10) < 0, 'O cannot map to original K in extension comparison')

# Exact virtual Euler arithmetic; retain negative coefficients, not Counter subtraction.
def difference(*terms):
    out = Counter()
    for sign, value in terms:
        for r, n in value.items():
            out[r] += sign * n
    return {r: n for r, n in out.items() if n}

chi5 = difference((1, h0_k5), (-1, ch.product('one', 3)), (-1, ch.product('A', 7)))
require(chi5 == {'S': -1}, 'chi F(5) equals minus S4')
chi4 = difference((1, Counter({'V': 1, 'P': 1, 'D': 1})),
                  (-1, ch.product('one', 4)), (-1, ch.product('A', 6)))
require(chi4 == {'P': -1, 'D': -2}, 'chi F(4) equals minus P minus two D')

# The three factorizations of the single dimension-four irreducible budget.
require([(7 - 6) * 4, (8 - 6) * 2, (10 - 6) * 1] == [4, 4, 4],
        'fixed dimension-four budget factorizations')
require(ch.product('W', 1) != Counter({'S': 1})
        and ch.product('Wp', 1) != Counter({'S': 1}), 'j8 doublets cannot contribute S4')
require(ch.product('S', 0) == ch.product('one', 3) == Counter({'S': 1}),
        'the two possible deep atoms contribute exactly S4')
bad_top = difference((1, Counter({'P': 1, 'D': 2})), (-1, ch.product('S', 1)))
require(bad_top == {'P': 1, 'D': 1, 'A': -1}, 'S4(-7) would force nongenuine top')
good_top = difference((1, Counter({'P': 1, 'D': 2})), (-1, ch.product('one', 4)))
require(good_top == {'P': 1, 'D': 1}, 'O(-10) forces P plus D at degree minus six')
require(4 + 5 + 1 == 10 and 9 * (-6) - 10 == -64, 'final F rank and degree')

print(json.dumps({
    'status': 'PASS', 'checks': len(checks),
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'proof_bytes': len(proof),
    'universal_character_consistency_checks': ch.checks,
    'formal_rectangle_steps': steps,
    'scope': 'Complete immutable input authentication and fixed universal character, degree and formal differentiation identities only. Arithmetic does not certify the structural geometric proof.',
    'details': checks,
}, indent=2))
