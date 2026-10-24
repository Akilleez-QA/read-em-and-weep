"""Bounded universal checks only; no selected actual-instance data."""
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

PINS = {
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
}
inputs = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(inputs) == 2 and {i['file'] for i in inputs} == set(PINS),
        'two complete immutable originals')
for item in inputs:
    ref, path, size, sha, blob = PINS[item['file']]
    data = (ROOT / item['file']).read_bytes()
    require(item['ref'] == ref and item['path'] == path, 'exact immutable ref and path')
    require(len(data) == item['bytes'] == size, 'complete input UTF8 length')
    require(hashlib.sha256(data).hexdigest() == item['sha256'] == sha,
            'complete input SHA256')
    require(hashlib.sha1(b'blob ' + str(size).encode() + b'\0' + data).hexdigest()
            == item['git_blob_sha1'] == blob, 'complete Git blob identity')
    require(item['url'] == 'https://github.com/Akilleez-QA/read-em-and-weep/blob/'
            + ref + '/' + path, 'exact immutable URL')
proof = (ROOT / 'PROOF.md').read_bytes()
require(len(proof) == 12921, 'frozen entire-proof UTF8 length')
require(hashlib.sha256(proof).hexdigest()
        == '4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e',
        'frozen entire-proof SHA256')
require(ch.checks == 81, 'fixed exact-rational McKay consistency checks')

# Only these fixed universal symmetric powers are requested.
EXPECTED = {
    1: {'W': 1}, 2: {'A': 1}, 3: {'S': 1}, 4: {'D': 1}, 5: {'T': 1},
    6: {'V': 1, 'P': 1}, 7: {'T': 1, 'Wp': 1},
    9: {'S': 1, 'T': 1},
    14: {'A': 1, 'D': 1, 'V': 1, 'P': 1},
    15: {'S': 1, 'T': 2}, 16: {'D': 2, 'V': 1, 'P': 1},
    17: {'S': 1, 'T': 2, 'Wp': 1},
    18: {'A': 1, 'D': 1, 'V': 1, 'P': 2},
}
for degree, decomposition in EXPECTED.items():
    require(ch.product('one', degree) == Counter(decomposition),
            f'Sym{degree} universal decomposition')
require(ch.product('V', 3) == Counter({'S': 1, 'T': 1, 'Wp': 1}),
        'V_alt tensor Sym3 fixed identity')
require(ch.product('P', 1) == Counter({'T': 1, 'Wp': 1}),
        'P tensor W fixed identity')
require(ch.product('P', 2) == Counter({'D': 1, 'V': 1, 'P': 1}),
        'P tensor Sym2 fixed identity')
require(ch.product('Wp', 1) == Counter({'P': 1}), 'alternate-doublet Euler coefficient')
require(ch.product('A', 2)['one'] == 1, 'unique canonical quadratic invariant line')
require(ch.product('one', 4)['one'] == 0, 'quadratic line has zero O4 projection')
require(ch.product('one', 6)['D'] == 0, 'missing-D extension obstruction vanishes')
require(ch.product('one', 9)['Wp'] == 0, 'both universal kernel composites vanish')
require(ch.product('one', 15)['Wp'] == 0, 'highest-doublet derivative vanishes')
require(ch.product('one', 16)['P'] == 1, 'degree-sixteen P row multiplicity one')
require(ch.product('one', 4)['P'] == 0, 'degree-sixteen P row cannot contain f12 factor')
require(ch.product('one', 12)['one'] == 1, 'degree-twelve invariant line')
require(ch.product('one', 20)['one'] == 1, 'normal extension warning retains degree-twenty invariant')

# These are exactly the two degree-allowed scalar images in Section 2.
require(all(ch.product('one', e + 7)['Wp'] == 0 for e in (-4, -6)),
        'rank-one Wprime image excluded at both allowed degrees')
require(2 * (7 - 4) == 6 < 12, 'rank-two minors below invariant divisor minimum')
require(3 * (-4) - 2 == 2 * (-7), 'V row kernel degree')
require(4 * (-4) - 4 == 2 * (-5) + (-10), 'P row kernel degree')
require(7 * (-4) - 2 * 3 == -34, 'N degree and rank-five quotient')
require(7 - 2 == 5, 'N rank')
require(2 * (-7) + 2 * (-5) == 4 * (-6), 'nonzero Euler extension degree')
require((-7) - (-5) == -2, 'one-dimensional H1 twist for middle Euler extension')
require((-7) - (-10) >= -1, 'O(-10) extension component vanishes ordinarily')
require(all(t >= -1 for t in (0, 4, -1, 1, 4)),
        'all D(-6) extension components vanish ordinarily')
require(5 + 4 + 1 == 10 and 9 * (-6) - 10 == -64, 'forced F rank and degree')
require(2 + 5 + 2 + 1 == 10 and 2*(-5) + 5*(-6) + 2*(-7) - 10 == -64,
        'discarded F alternative rank and degree')
require(-6 - 2 < -5, 'killed highest doublet has no internal derivative target')
require(9 - 1 == 8 and 9 * (-6) - 10 == -64, 'actual backward kernel rank and degree')
require(4 * (-7) + (-2) == 5 * (-6), 'actual third-to-fourth jet quotient degree')
require(1 + 4 - 1 == 4 and -2 + 4 * (-6) - 10 == -36, 'Q rank and degree')
require(6 > 4, 'rank-four Q cannot carry a top T6 coefficient block')
require(3 <= 4 and 3 + min(3, 4, 5) > 4,
        'forced top V_alt leaves no additional source irreducible')
require(3 * (-8) - 12 == -36, 'Q forced line degree')
require(all(t >= -1 for t in (1, 5)), 'final Z3 extension components vanish ordinarily')
require(4 + 3 + 1 == 8 and 4 * (-7) + 3 * (-8) - 12 == -64,
        'forced F-minus rank and degree')
require(-(-12 - 10) - 2 == 20, 'unresolved normal extension Serre degree')

print(json.dumps({
    'status': 'PASS',
    'checks': len(checks),
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'universal_character_consistency_checks': ch.checks,
    'scope': 'Complete immutable input authentication and bounded universal character, degree, rank, and Ext arithmetic only. This checker does not certify the actual geometric proof or exclude K1.',
    'details': checks,
}, indent=2))
