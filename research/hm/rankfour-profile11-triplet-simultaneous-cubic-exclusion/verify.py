"""Small universal representation/degree checks only; no actual-instance data."""
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

pins = {'inputs/lifted-jets-and-kernel-two.md': ('c565bd8b5b65829e99bdd96a7c5f076b01050465', 'research/hm/rankfour-profile11-triplet-simultaneous-kernel-two-exclusion/PROOF.md', 13703, '0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa', 'cb46875b07d8d79e82aebe980685c418d975d87b'), 'inputs/five-kernels.md': ('7d71f0e2a3963cff64a069198f4415c5cfd0fe9b', 'research/hm/rankfour-profile11-triplet-kernels/PROOF.md', 8501, '4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a', '163ba2126b6130befcc2351db7f6910d85fac2ec')}
inputs = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(inputs) == 2 and {i['file'] for i in inputs} == set(pins), 'two complete immutable originals')
for item in inputs:
    ref, path, n, sha, blob = pins[item['file']]
    data = (ROOT / item['file']).read_bytes()
    require(item['ref'] == ref and item['path'] == path, 'exact immutable ref and path')
    require(len(data) == item['bytes'] == n, 'complete input length')
    require(hashlib.sha256(data).hexdigest() == item['sha256'] == sha, 'complete input SHA256')
    require(hashlib.sha1(b'blob ' + str(n).encode() + b'\0' + data).hexdigest() == item['git_blob_sha1'] == blob, 'complete Git blob identity')
    require(item['url'] == 'https://github.com/Akilleez-QA/read-em-and-weep/blob/' + ref + '/' + path, 'exact immutable URL')
proof = (ROOT / 'PROOF.md').read_bytes()
require(len(proof) == 13289, 'frozen entire-proof bytes')
require(hashlib.sha256(proof).hexdigest() == '9da994c73b8c5365de31fc8b5552ba364bfc6af624108acdb8567feba9365103', 'frozen entire-proof hash')
require(ch.checks == 81, 'fixed character module checks')

expected = {
    1: {'W': 1}, 3: {'S': 1}, 4: {'D': 1}, 5: {'T': 1},
    6: {'V': 1, 'P': 1}, 7: {'T': 1, 'Wp': 1},
    8: {'D': 1, 'P': 1},
    12: {'one': 1, 'A': 1, 'D': 1, 'P': 1},
    13: {'W': 1, 'S': 1, 'T': 1, 'Wp': 1},
    14: {'A': 1, 'D': 1, 'V': 1, 'P': 1},
}
for n, value in expected.items():
    require(ch.product('one', n) == Counter(value), f'Sym{n} fixed identity')

require(ch.product('W', 5) == Counter({'D': 1, 'V': 1, 'P': 1}), 'W tensor T6 has no scalar')
require(ch.product('S', 2) == Counter({'T': 1, 'S': 1, 'W': 1}), 'unique cubic projection')
require(ch.product('P', 5)['W'] == 1, 'W(-9) to P(-4) universal Hom dimension one')
require(ch.product('one', 8)['P'] == 1, 'P(-4) to O4 universal Hom dimension one')
require(ch.product('one', 13)['W'] == 1, 'degree thirteen W multiplicity one')
require(ch.product('one', 12)['one'] == 1, 'degree twelve invariant dimension one')
require(ch.product('one', 14)['one'] == 0, 'degree fourteen invariant vanishing')
require(ch.product('one', 7)['S'] == 0, 'cubic row has zero O4 projection')
require(ch.product('one', 6)['D'] == 0, 'R misses D extension obstruction')

# Exhausts only the three degree-allowed rank-one image degrees, not kernel tuples.
degrees = [-4, -6, -8]
possible = [e for e in degrees if ch.product('one', e + 9)['W']]
require(possible == [-8], 'rank-one saturation would have degree minus eight')
require(ch.product('one', 4)['P'] == 0, 'P(-4) has no O(-8) subline')
require(2 * ((-4) - (-9)) == 10 < 12, 'j minors below orbit minimum')
require(4 - (-4) == 8 < 12, 'q entries below orbit minimum')
require(4 * (-4) - 4 == -20, 'kernel q degree')
require((-20) - 2 * (-9) == -2, 'kernel quotient degree')
require((-9) - (-2) == -7, 'extension cohomology twist')
require(-(-7) - 2 == 5, 'Serre dual degree')
require((-4) - (-2) < 0, 'split O(-2) line cannot map into P(-4)')
require(6 * (-5) - 4 * (-3) == 2 * (-9), 'universal cubic kernel degree')
require(3 * (-4) - 2 == -14, 'actual V row kernel degree')
require((-14) - (-9) < 0, 'first jets cannot map to V row kernel')
require(4 - (-9) == 13 and 13 - 12 == 1, 'K4 low row invariant factor degree')
require(4 - (-8) == 12 and 4 - (-10) == 14, 'K5 low row degrees')

print(json.dumps({'status': 'PASS', 'checks': len(checks),
                  'proof_sha256': hashlib.sha256(proof).hexdigest(),
                  'universal_character_consistency_checks': ch.checks,
                  'scope': 'Immutable local input authentication and fixed universal representation/degree identities only. The structural geometric proof is not certified by this arithmetic checker.',
                  'details': checks}, indent=2))
