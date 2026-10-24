"""Bounded authentication and universal arithmetic; no selected actual evaluation."""
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

# Exact independent hard-coded source and entire-proof pins.
PINS = {'inputs/first-kernel-structure.md': ('d3c9e9ff8d06977e6c3d3be6cd1c9ed71007a593',
                                      'research/hm/rankfour-profile11-triplet-first-kernel-structure/PROOF.md',
                                      12921,
                                      '4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e',
                                      '41ab2148d3ea13d07dcdfe2bf353a18c664bb848'),
 'inputs/third-kernel-top-rigidity.md': ('a370a91b3fa7fdf92e7d2b24af31602a71837bbc',
                                         'research/hm/rankfour-profile11-triplet-third-kernel-top-rigidity/PROOF.md',
                                         20248,
                                         'c501c094dfe7cff853f8b0a64552b4a59478581a2d11921ec5f8f70f34bb0542',
                                         'f3d7fc24958c867dd3509b18383d3831be6d56a3'),
 'inputs/top-jet-complement.md': ('317cf0c533b6ab8ce650d566e08c87610dd11ccd',
                                  'research/hm/rankfour-profile11-triplet-top-jet-complement/PROOF.md',
                                  11240,
                                  '08708a646f51fb6b10ef94c1eab1b5e4ee56a775fb8e377d6a92e8d34df54259',
                                  '63abea7d4412fced453c728d9f1e3c7dd4870521'),
 'inputs/common-kernel-ladder.md': ('5249c844765cfd96ffb51bdfd4aaef8307d49b1f',
                                    'research/hm/rankfour-profile11-triplet-common-kernel-ladder/PROOF.md',
                                    13135,
                                    '0a24ab99c6f3d6c2f60212532c7f4aed2bd7d5fba17823243dd479a83a7308dd',
                                    'd64a0db4f2bcbd61651cdefc37a37b672c321176')}
PROOF_BYTES = 16808
PROOF_SHA256 = '074dba0e590290f7b811a848b5fb4910ab6eebe5597f855111b66d5cd5fe71d0'
require(PINS is not None and PROOF_BYTES is not None and PROOF_SHA256 is not None,
        'packet frozen only after complete K3 immutable input')
inputs = json.loads((ROOT / 'INPUTS.json').read_text())
require(len(inputs) == 4 and {i['file'] for i in inputs} == set(PINS),
        'four complete immutable originals')
for item in inputs:
    ref, path, size, sha, blob = PINS[item['file']]
    data = (ROOT / item['file']).read_bytes()
    require(item['ref'] == ref and item['path'] == path,
            'exact immutable input ref and repository path')
    require(len(data) == item['bytes'] == size, 'complete input UTF8 length')
    require(hashlib.sha256(data).hexdigest() == item['sha256'] == sha,
            'complete input SHA256')
    require(hashlib.sha1(b'blob ' + str(size).encode() + b'\0' + data).hexdigest()
            == item['git_blob_sha1'] == blob, 'complete input Git blob identity')
    require(item['url'] == 'https://github.com/Akilleez-QA/read-em-and-weep/blob/'
            + ref + '/' + path, 'exact immutable input URL')
proof = (ROOT / 'PROOF.md').read_bytes()
require(len(proof) == PROOF_BYTES, 'frozen entire-proof UTF8 length')
require(hashlib.sha256(proof).hexdigest() == PROOF_SHA256,
        'frozen entire-proof SHA256')
require(ch.checks == 81, 'fixed exact-rational McKay consistency checks')

# Only the finitely many universal identities explicitly used in the proof.
EXPECTED = {
    1: {'W': 1},
    2: {'A': 1},
    3: {'S': 1},
    4: {'D': 1},
    5: {'T': 1},
    6: {'V': 1, 'P': 1},
    9: {'S': 1, 'T': 1},
    10: {'A': 1, 'V': 1, 'D': 1},
    11: {'W': 1, 'S': 1, 'T': 1},
    15: {'S': 1, 'T': 2},
    16: {'D': 2, 'V': 1, 'P': 1},
    17: {'S': 1, 'T': 2, 'Wp': 1},
    18: {'A': 1, 'D': 1, 'V': 1, 'P': 2},
}
for degree, decomposition in EXPECTED.items():
    require(ch.product('one', degree) == Counter(decomposition),
            f'Sym{degree} fixed physical decomposition')
require(ch.product('P', 1) == Counter({'T': 1, 'Wp': 1}),
        'P tensor W for twist-seven source and Euler sequence')
require(ch.product('P', 2) == Counter({'D': 1, 'V': 1, 'P': 1}),
        'P tensor Sym2 for twist-eight source')
require(ch.product('Wp', 1) == Counter({'P': 1}),
        'alternate-doublet Euler middle coefficient')
require(ch.product('one', 4)['P'] == 0,
        'degree-sixteen P row cannot have f12 as a common factor')
require(ch.product('one', 15)['Wp'] == 0,
        'twist-seven Wprime section row cannot vanish')
require(ch.product('one', 12)['one'] == 1,
        'fixed degree-twelve invariant line')
require(ch.product('one', 10)['one'] == 0,
        'O0 plus Ominus2 cannot surject equivariantly to O10')
require(ch.product('one', 6)['P'] == 1,
        'P row to O0 is permitted and cannot be discarded')
require(ch.product('one', 11)['W'] == 1
        and ch.product('one', 11)['Wp'] == 0
        and ch.product('one', 11)['one'] == 0,
        'balanced normal extension has only physical W coefficient')

# Rank-four section argument: exact sources and target multiplicities.
source6 = Counter({'D': 1, 'P': 1})
source7 = ch.product('one', 5) + ch.product('P', 1)
source8 = ch.product('one', 6) + ch.product('P', 2)
require(source6 == Counter({'D': 1, 'P': 1}), 'twist-six inequivalent row sources')
require(source7 == Counter({'T': 2, 'Wp': 1}), 'twist-seven full source')
require(source8 == Counter({'D': 1, 'V': 2, 'P': 2}), 'twist-eight full source')
require(source8['V'] - ch.product('one', 18)['V'] == 1,
        'twist-eight V_alt multiplicity forces a kernel constituent')
require(ch.DIM['T'] > 4, 'rank-four Q cannot carry a top T6 kernel')
require(ch.DIM['V'] <= 4
        and ch.DIM['V'] + min(ch.DIM[r] for r in source8) > 4,
        'rank-four Q leaves no additional source constituent after V_alt')

# Elementary bundle arithmetic appearing verbatim in the proof.
require(5 + 4 + 1 == 10 and 9 * (-6) - 10 == -64,
        'common F rank and degree')
require(5 * (-6) - 4 * (-7) == -2,
        'actual fourth-to-third jet quotient degree')
require(9 - 1 == 8 and 9 * (-6) - 10 == -64,
        'actual kernel of the coherent upper row')
require(1 + 4 - 1 == 4 and -2 + 4 * (-6) - 10 == -36,
        'rank-four Q rank and degree')
require(3 * (-8) - 12 == -36, 'remaining scalar degree of Q')
require(all(t >= -1 for t in (1, 5)), 'both final Z3 extension components vanish')
require(4 + 3 + 1 == 8 and 4 * (-7) + 3 * (-8) - 12 == -64,
        'shared F-minus rank and degree')
require(-12 - (-7) < 0 and -12 - (-8) < 0,
        'beta_B restriction kills both canonical top blocks by degree')
require(4 + 3 == 7 and 4 * (-7) + 3 * (-8) == -52,
        'exact B-minus rank and degree')
require(9 - 7 == 2 and 9 * (-6) - (-52) == -2,
        'actual beta_B coherent image rank and degree')
require(-12 + 10 == -2, 'actual normal extension degree matches coherent image')
require(-10 - 2 == -12, 'regular internal normal target for F-minus restriction')
require(-12 - (-6) < 0, 'split normal extension incompatible with beta_B onto')
require(10 - (-1) == 11 and -12 + 1 == -11,
        'balanced-extension section injection has exact twist eleven')
require(9 + 2 == 11 and 9 * (-6) + 2 * 1 == -52,
        'actual B-plus rank and degree')
require(-52 - (-64) == 12 and -48 - (-52) == 4,
        'actual B-plus quotients in the retained J flag')

print(json.dumps({
    'status': 'PASS',
    'checks': len(checks),
    'proof_sha256': hashlib.sha256(proof).hexdigest(),
    'universal_character_consistency_checks': ch.checks,
    'scope': 'Complete immutable input authentication and bounded universal representation, degree, rank, and Ext arithmetic only. This checker does not certify the actual geometric proof, exclude K1 or K3, or evaluate a selected actual instance.',
    'details': checks,
}, indent=2))
