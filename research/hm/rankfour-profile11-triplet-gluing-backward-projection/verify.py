#!/usr/bin/env python3
"""Bounded author checks only: frozen bytes and fixed universal identities.

Reads only the ten named core files and FROZEN.json; ignores other artifacts.
No network, writes, geometry representatives, instance evaluation, or scan.
Runtime checks deliberately do not use Python's optimizable assert statement.
"""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
CORE = (
    'README.md', 'INPUTS.json', 'INPUTS.md', 'PROVENANCE.md', 'PROOF.md',
    'verify.py', 'inputs/gluing-kernel-derivative.md',
    'inputs/original-second-kernel-derivative.md',
    'inputs/gluing-kernel-incidence.md', 'inputs/orthogonal-top-incidence.md',
)
SOURCES = (
    ('GD', 1246, '6f34ff7be5ce93a85da17d9c14a2f72bdd428a18',
     'rankfour-profile11-triplet-gluing-kernel-derivative',
     'inputs/gluing-kernel-derivative.md', 18760,
     '29e3de59ef651ebec60accba604970f0dfaacdcce0c45e35130fcbd6a816aa6a',
     'c4492f7b9d7b9b6f081b94b42434445369b6bb66'),
    ('OD', 1245, '4696eb607fd6446511dd9968a056778349bf17b3',
     'rankfour-profile11-triplet-original-second-kernel-derivative',
     'inputs/original-second-kernel-derivative.md', 11709,
     'a11b3386584390375a6a3249898170a2240d614d4f067e824ddf12aa0c3d6e6f',
     'e561adb180b5040a57464808dbbdfaef29f1c6a8'),
    ('GI', 1244, '6d2c3d06c11234f858f772edf212de5de850b5a2',
     'rankfour-profile11-triplet-gluing-kernel-incidence',
     'inputs/gluing-kernel-incidence.md', 21478,
     'b20161802eb43ae4a69de779146be620126fe2a0332afd0f19929517b7806807',
     '2a969e1c3e14edb4e593738623aaaa8f0b19a00b'),
    ('OT', 1240, '3fbaa182b1aceb6915be88088ef158d6d15e34fb',
     'rankfour-profile11-triplet-orthogonal-top-incidence',
     'inputs/orthogonal-top-incidence.md', 28094,
     '407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637',
     'f00b059695615d9b8ab6d315798940e3ab0a58d4'),
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def git_blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def check_bytes():
    freeze_raw = (BASE / 'FROZEN.json').read_bytes()
    frozen = json.loads(freeze_raw)
    require(frozen['schema'] == 'ten-core-author-freeze/v1', 'Freeze schema mismatch')
    require(frozen['core_file_count'] == 10, 'Freeze must bind exactly ten core files')
    entries = frozen['files']
    require(len(entries) == 10, 'Wrong core entry count')
    require(tuple(e['path'] for e in entries) == CORE, 'Frozen core membership/order mismatch')
    raw = {}
    for entry in entries:
        name = entry['path']
        payload = (BASE / name).read_bytes()
        payload.decode('utf-8', errors='strict')
        require(len(payload) == entry['bytes'], 'Core byte length mismatch: ' + name)
        require(sha256(payload) == entry['sha256'], 'Core SHA256 mismatch: ' + name)
        raw[name] = payload
    ledger = json.loads(raw['INPUTS.json'])
    require(ledger['direct_input_count'] == 4, 'Wrong direct source count')
    require(len(ledger['sources']) == 4, 'Wrong ledger source count')
    require(tuple(s['alias'] for s in ledger['sources']) == ('GD', 'OD', 'GI', 'OT'), 'Source order mismatch')
    for source, expected in zip(ledger['sources'], SOURCES):
        alias, pr, commit, slug, name, length, digest, blob = expected
        repository_path = 'research/hm/' + slug + '/PROOF.md'
        require(source['alias'] == alias and source['pr'] == pr, 'Source label mismatch')
        require(source['repository'] == 'Akilleez-QA/read-em-and-weep', 'Source repository mismatch')
        require(source['commit'] == commit and source['repository_path'] == repository_path, 'Source pin mismatch')
        require(source['retained_path'] == name, 'Retained source path mismatch')
        payload = raw[name]
        require(len(payload) == source['bytes'] == length, 'Source length mismatch: ' + alias)
        require(sha256(payload) == source['sha256'] == digest, 'Source SHA256 mismatch: ' + alias)
        require(git_blob(payload) == source['git_blob_sha1'] == blob, 'Source blob mismatch: ' + alias)
        expected_path_args = {'repository_full_name': 'Akilleez-QA/read-em-and-weep',
                              'ref': commit, 'path': repository_path, 'encoding': 'utf-8'}
        expected_blob_args = {'repository_full_name': 'Akilleez-QA/read-em-and-weep', 'blob_sha': blob}
        require(source['fetch_file_arguments'] == expected_path_args, 'Complete exact path request mismatch')
        require(source['fetch_blob_arguments'] == expected_blob_args, 'Separate blob request mismatch')
        require(source['full_byte_comparison'] == 'PASS', 'Missing source comparison record')
    print('PASS: exactly ten frozen core identities and four immutable full original identities')
    print('FROZEN.json SHA256: ' + sha256(freeze_raw))


# Fixed physical W-adjacency from OD Section 6. These are character labels,
# not selected coefficients, points, jets, matrices, or instance ranks.
NAMES = ('1', 'W', 'A', 'S4', 'D', 'T6', 'V', 'P', 'Wp')
DIMS = {'1': 1, 'W': 2, 'A': 3, 'S4': 4, 'D': 5, 'T6': 6,
        'V': 3, 'P': 4, 'Wp': 2}
W_PRODUCT = {
    '1': {'W': 1}, 'W': {'1': 1, 'A': 1},
    'A': {'W': 1, 'S4': 1}, 'S4': {'A': 1, 'D': 1},
    'D': {'S4': 1, 'T6': 1}, 'T6': {'D': 1, 'V': 1, 'P': 1},
    'V': {'T6': 1}, 'P': {'T6': 1, 'Wp': 1}, 'Wp': {'P': 1},
}


def times_w(character):
    result = {name: 0 for name in NAMES}
    for name, multiplicity in character.items():
        for target, count in W_PRODUCT[name].items():
            result[target] += multiplicity * count
    return result


def reduced(character):
    return {name: coefficient for name, coefficient in character.items() if coefficient}


def check_characters():
    require(sum(d * d for d in DIMS.values()) == 120, 'Irreducible dimension sum')
    for name in NAMES:
        require(sum(DIMS[t] * c for t, c in W_PRODUCT[name].items()) == 2 * DIMS[name], 'Adjacency dimension: ' + name)
    h = [{'1': 1}, {'W': 1}]
    for degree in range(2, 13):
        next_h = times_w(h[-1])
        for name, count in h[-2].items():
            next_h[name] -= count
        require(all(c >= 0 for c in next_h.values()), 'Negative universal character multiplicity')
        h.append(reduced(next_h))
        require(sum(DIMS[name] * count for name, count in h[-1].items()) == degree + 1, 'Symmetric degree dimension')
    expected = (
        {'1': 1}, {'W': 1}, {'A': 1}, {'S4': 1}, {'D': 1}, {'T6': 1},
        {'V': 1, 'P': 1}, {'Wp': 1, 'T6': 1}, {'P': 1, 'D': 1},
        {'S4': 1, 'T6': 1}, {'A': 1, 'V': 1, 'D': 1},
        {'W': 1, 'S4': 1, 'T6': 1}, {'1': 1, 'A': 1, 'D': 1, 'P': 1},
    )
    require(tuple(h) == expected, 'Fixed characters H0 through H12')
    require(h[6].get('P', 0) == 1 and h[6].get('V', 0) == 1, 'Q3 cohomology constituents')
    require(h[4].get('P', 0) == 0, 'Unique equivariant H5 complement Hom vanishing')
    require(h[2].get('P', 0) == 0, 'Actual L10 horizontal contradiction Hom vanishing')
    require(h[10].get('1', 0) == 0, 'Nonzero decic cannot factor through trivial Euler line')
    require(h[12].get('1', 0) == 1, 'Unique invariant degree-twelve line')
    require(h[1].get('W', 0) == 1 and h[2].get('A', 0) == 1, 'Euler Hom uniqueness')
    require(h[5].get('T6', 0) == 1, 'Noncanonical E7 complement difference space')
    print('PASS: fixed physical characters H0 through H12 and all displayed Hom multiplicities')


def h0(degree):
    return max(degree + 1, 0)


def h1(degree):
    return max(-degree - 1, 0)


def check_degrees():
    # Only the three degree lists explicitly appearing in PROOF Section 3.
    candidates = ((-7, -7, -10), (-7, -8, -9), (-8, -8, -8))
    for row in candidates:
        require(sum(row) == -24 and max(row) <= -7, 'Q3 fixed degree-list arithmetic')
        require(sum(h0(d + 6) for d in row) == 0, 'Q3 H0 vanishing')
        require(sum(h1(d + 6) for d in row) == 3, 'Q3 H1 dimension')
    require(h1(-1) == 0 and h1(-4) == 3, 'First candidate bottom cohomology dimension')
    require(candidates[1][0] % 2 == 1 and candidates[1][2] % 2 == 1, 'Middle candidate odd singleton degrees')
    require(h1(-2) == 1, 'Balanced candidate Serre dimension')
    require(h1(4) == 0 and h1(5) == 0, 'H5 and E7 ordinary Ext vanishings')
    require(tuple(60 // stabilizer for stabilizer in (5, 3, 2, 1)) == (12, 20, 30, 60), 'Fixed projective orbit sizes')
    require(12 < 20 and 2 * 12 > 12, 'Degree-twelve orbit and reducedness arithmetic')

    # Universal complete degree-ten target flag, only k=1,...,6.
    flag = {k: (11 - k, -k * (11 - k)) for k in range(1, 7)}
    require(tuple(flag[k] for k in range(1, 7)) ==
            ((10, -10), (9, -18), (8, -24), (7, -28), (6, -30), (5, -30)), 'Complete target rank/degree table')
    for k in range(1, 6):
        require(flag[k][0] - flag[k + 1][0] == 1, 'Complete evaluation quotient rank')
        require(flag[k][1] - flag[k + 1][1] == 10 - 2 * k, 'Complete evaluation quotient degree')
    for k in range(2, 6):
        require(flag[k - 1][1] - flag[k][1] - 2 == 10 - 2 * k, 'Complete normal target degree')
        require(k != 0, 'Characteristic-zero tautological symbol factor')

    # Displayed ranks/degrees; these numbers do not verify any actual map.
    bundles = {
        'E0': (16, -46), 'K': (13, -58), 'G7': (7, -28),
        'H5': (5, 4 * -6 - 10), 'H3': (3, 3 * -8),
        'Fhat': (10, 9 * -6 - 10), 'Bhat': (9, 9 * -6),
        'Chat': (7, 4 * -7 + 3 * -8), 'Q2': (2, 2 * -11),
        'F10': flag[2], 'J8': flag[3], 'J7': flag[4],
        'J6': flag[5], 'J5': flag[6], 'E7': (7, 6 * -5 - 10),
        'W3': (2, 6), 'W1': (2, 2), 'A4': (3, 12),
        'A2': (3, 6), 'image_beta_H5': (2, -10),
    }
    rows = (
        ('E0', 'G7', 'F10'), ('E0', 'K', 'A4'),
        ('G7', 'H5', 'W3'), ('H5', 'H3', 'image_beta_H5'),
        ('K', 'H5', 'J8'), ('K', 'Fhat', 'A2'),
        ('Fhat', 'H3', 'E7'), ('Bhat', 'H3', 'J6'),
        ('Chat', 'Q2', 'J5'),
    )
    for total, kernel, quotient in rows:
        require(tuple(bundles[total][i] - bundles[kernel][i] for i in (0, 1)) == bundles[quotient],
                'Displayed exact-row arithmetic: ' + total + '/' + kernel)
    require(bundles['W1'][1] - bundles['image_beta_H5'][1] == 12, 'H5 coherent defect length')
    require(bundles['J7'][0] == bundles['E7'][0] and bundles['J7'][1] - bundles['E7'][1] == 12, 'Evaluation modification length')
    require(bundles['E7'] == (bundles['J6'][0] + 1, bundles['J6'][1] - 10), 'Actual preimage extension arithmetic')
    require((2 + 1, 2 + 4) == bundles['A2'], 'First normal exact-row arithmetic')
    require(2 - (-10) == 12, 'Nonzero line quotient divisor degree')
    print('PASS: three displayed Q3 degree lists, P1 cohomology, fixed orbit sizes, and complete target flag')
    print('PASS: displayed kernel/projection/normal rows and reduced-defect degree arithmetic')


def main():
    check_bytes()
    check_characters()
    check_degrees()
    print('AUTHOR CHECKS PASS. Actual-map proof and all four complete sources still require NEW independent review.')


if __name__ == '__main__':
    main()
