#!/usr/bin/env python3
"""Complete immutable pins and fixed diagonal/rank/degree/Hom arithmetic only."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
CHECKS = 0


def require(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(label)


PROOF_BYTES = 6373
PROOF_SHA = '57a435c44d7de7f2ef0e97b168530acc32aa37dc25258adfff48ba06f848cc82'
PINS = [
    ('inputs/dual-extension.md',
     '430bdab090b2319313e5855c66fd7cc102c09e35',
     'research/hm/rankfour-profile11-triplet-dual-extension/PROOF.md',
     16075,
     'c0b961a3a851b21906218865208c304df8390dedb72b73fb9e2b912a33d68d0b',
     '54acabb5c6a641ca602f494956d209e1d268a955'),
    ('inputs/mixed-jet-pairing.md',
     '84b418e22f03b5718409bdeb23ae353ecc4eb681',
     'research/hm/rankfour-profile11-triplet-mixed-jet-pairing/PROOF.md',
     14593,
     '3e1ce0d1589d694d578796a90398cbdaf8fdf6fb340158b5098ad3f79cdfa95b',
     '91e0c23867113c0a7d5b032098c8e365b356859d'),
]

proof = (ROOT / 'PROOF.md').read_bytes()
require(len(proof) == PROOF_BYTES, 'complete frozen proof byte length')
require(hashlib.sha256(proof).hexdigest() == PROOF_SHA,
        'complete frozen proof SHA256')
manifest = json.loads((ROOT / 'INPUTS.json').read_text(encoding='utf-8'))
require(isinstance(manifest, list), 'input manifest is a list')
require(len(manifest) == len(PINS) == 2, 'two complete direct input pins')
for record, pin in zip(manifest, PINS):
    file, ref, path, length, sha, blob = pin
    data = (ROOT / file).read_bytes()
    require(set(record) == {'file', 'ref', 'path', 'url', 'bytes',
                            'sha256', 'git_blob_sha1'}, 'exact manifest fields')
    require(record['file'] == file and record['ref'] == ref
            and record['path'] == path, 'immutable source path and commit')
    url = 'https://github.com/Akilleez-QA/read-em-and-weep/blob/' + ref + '/' + path
    require(record['url'] == url, 'exact immutable source URL')
    require(record['bytes'] == len(data) == length, 'complete source byte length')
    require(record['sha256'] == hashlib.sha256(data).hexdigest() == sha,
            'complete source SHA256')
    git_blob = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii')
                           + b'\0' + data).hexdigest()
    require(record['git_blob_sha1'] == git_blob == blob, 'complete source Git blob')


def h0_line(degree):
    return max(degree + 1, 0)


def h1_line(degree):
    return max(-degree - 1, 0)


# Fixed universal diagonal and principal-parts data, not instance evaluations.
d, order = 18, 4
diagonal_power = order + 1
source_twist, base_twist = d - diagonal_power, -diagonal_power
require(diagonal_power == 5, 'fourth jets use the fifth diagonal-ideal power')
require((source_twist, base_twist) == (13, -5), 'fixed diagonal twists')
require(h1_line(source_twist) == 0, 'higher direct image vanishes')
require(h0_line(source_twist) == 14, 'universal kernel rank')
require(h0_line(d) == 19, 'complete section-space dimension')
jet_rank = order + 1
require(jet_rank == 5, 'fourth principal-parts rank')
require(h0_line(d) - h0_line(source_twist) == jet_rank,
        'universal exact-sequence ranks')
jet_degree = sum(d - 2 * j for j in range(order + 1))
require(jet_degree == 70, 'principal-parts degree from its fixed filtration')
require(jet_rank * (d - order) == jet_degree, 'known balanced jet degree')
kernel_degree = h0_line(source_twist) * base_twist
require(kernel_degree == -70 and kernel_degree + jet_degree == 0,
        'universal exact-sequence degrees')
require(15 < h0_line(d), 'auxiliary coefficient system is allowed incomplete')
require(15 - jet_rank == 10 and 5 <= 10, 'retained annihilator inclusion ranks')
require(base_twist - (-4) == -1 and h0_line(-1) == 0,
        'Hom from O(-4) to the universal kernel vanishes')

# Arithmetic of the two supplied extension types and retained actual incidence.
require(4 + 1 == 2 + 3 == 5, 'supplied dual-extension middle ranks')
require(4 * (-15) + (-4) == 2 * (-11) + 3 * (-14) == -64,
        'supplied dual-extension middle degrees')
require((-18) + (-4) == 2 * (-11), 'retained canonical-doublet exact degree')
require(1 + 5 == 2 + 4, 'retained pushout ranks')
require((-18) + (-64) == 2 * (-11) + 4 * (-15), 'retained pushout degrees')

print(json.dumps({
    'status': 'PASS',
    'checks': CHECKS,
    'proof_bytes': PROOF_BYTES,
    'proof_sha256': PROOF_SHA,
    'scope': 'two complete pins; fixed diagonal twists, ranks, degrees and Hom arithmetic',
    'not_claimed': [
        'actual coefficient, parameter, point, jet, tensor, matrix or instance-rank evaluation',
        'K1/K3 assumptions or new original higher jets',
        'residual branch exclusion, realization or algebraicity',
        'geometric proof by computation',
    ],
}, sort_keys=True, indent=2))
