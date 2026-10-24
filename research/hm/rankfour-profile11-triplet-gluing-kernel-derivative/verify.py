#!/usr/bin/env python3
"""Exact bytes and fixed small universal characters/degrees, not geometry.

No network; no selected actual source-instance data, coefficient, point, jet,
scalar, tensor, matrix, normalization, instance rank, scan, or large computation.
All conditions are explicit runtime checks, effective also with python -O.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = (
    'PROOF.md', 'README.md', 'INPUTS.json', 'INPUTS.md', 'PROVENANCE.md',
    'verify.py', 'inputs/gluing-kernel-incidence.md',
    'inputs/f18-gluing-surjectivity.md', 'inputs/first-kernel-forward-closure.md',
)
PINS = (
    (1244, '6d2c3d06c11234f858f772edf212de5de850b5a2',
     'research/hm/rankfour-profile11-triplet-gluing-kernel-incidence/PROOF.md',
     'inputs/gluing-kernel-incidence.md', 21478,
     'b20161802eb43ae4a69de779146be620126fe2a0332afd0f19929517b7806807',
     '2a969e1c3e14edb4e593738623aaaa8f0b19a00b'),
    (1243, 'dde84900cd6f9ad117800c39042844bb897a2f79',
     'research/hm/rankfour-profile11-triplet-f18-gluing-surjectivity/PROOF.md',
     'inputs/f18-gluing-surjectivity.md', 12798,
     '3919909cd67055e266299a0841e4642c465185eba28500a3b00b4a284f93693a',
     '700257a6d8f41f9cfbae7fdf8d78d77795a07bb9'),
    (1236, '092fc5f31dfaa5553ee5ea687f175ecba1878a2a',
     'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md',
     'inputs/first-kernel-forward-closure.md', 18052,
     '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
     'f77cfb52743be86e46e0c40570ec036e69aebaf3'),
)
CHECKS = []


def check(name, condition):
    if not condition:
        raise SystemExit('FAIL: ' + name)
    CHECKS.append(name)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


# Read only the exact named core files and freeze, never author evidence.
frozen_bytes = (ROOT / 'FROZEN.json').read_bytes()
frozen = json.loads(frozen_bytes)
check('freeze schema', frozen['schema'] == 'triplet-gluing-kernel-derivative-freeze-v1')
check('exact nine-file core', tuple(x['path'] for x in frozen['files']) == CORE)
for entry in frozen['files']:
    data = (ROOT / entry['path']).read_bytes()
    check('frozen byte count ' + entry['path'], len(data) == entry['bytes'])
    check('frozen SHA256 ' + entry['path'], sha256(data) == entry['sha256'])

inputs = json.loads((ROOT / 'INPUTS.json').read_bytes())
check('input schema', inputs['schema'] == 'triplet-gluing-kernel-derivative-inputs-v1')
check('exactly three complete direct originals', len(inputs['sources']) == inputs['direct_original_count'] == 3)
for entry, pin in zip(inputs['sources'], PINS):
    pr, commit, repo_path, path, count, sha, blob = pin
    label = ' PR' + str(pr)
    data = (ROOT / path).read_bytes()
    check('complete UTF-8 round trip' + label, data.decode('utf-8').encode('utf-8') == data)
    check('input identity' + label,
          (entry['pr'], entry['commit'], entry['repository_path'], entry['local_path']) == pin[:4])
    check('input byte count' + label, len(data) == entry['bytes'] == count)
    check('input SHA256' + label, sha256(data) == entry['sha256'] == sha)
    check('input Git blob' + label,
          git_blob(data) == entry['git_blob_sha1'] == entry['returned_path_blob_sha1'] == blob)
    check('exact source URL' + label, entry['path_url'] ==
          'https://github.com/Akilleez-QA/read-em-and-weep/blob/' + commit + '/' + repo_path)
    check('exact blob URL' + label, entry['blob_api_url'] ==
          'https://api.github.com/repos/Akilleez-QA/read-em-and-weep/git/blobs/' + blob)
    expected_requests = (
        ('path', 'mcp__codex_apps__github_fetch_file', {
            'repository_full_name': 'Akilleez-QA/read-em-and-weep',
            'path': repo_path, 'ref': commit, 'encoding': 'utf-8'}),
        ('blob', 'mcp__codex_apps__github_fetch_blob', {
            'repository_full_name': 'Akilleez-QA/read-em-and-weep', 'blob_sha': blob}),
    )
    for kind, tool, arguments in expected_requests:
        request = entry[kind + '_request']
        check('exact ' + kind + ' request' + label,
              request['tool'] == tool and request['arguments'] == arguments)
        check('complete ' + kind + ' authentication metadata' + label,
              request['complete_no_line_limits'] is True and
              (request['decoded_bytes'], request['decoded_sha256'], request['recomputed_git_blob_sha1']) ==
              (count, sha, blob))
        check('ordered ' + kind + ' request timestamps' + label,
              request['started_at_utc'] <= request['completed_at_utc'])
    check('full source reading and equality recorded' + label,
          entry['full_original_read'] is True and entry['path_blob_retained_bytes_equal'] is True)
    check('assertion provenance recorded' + label, len(entry['assertion_provenance']) >= 2 and
          all(set(x) == {'source_sections', 'assertion', 'used_in'} for x in entry['assertion_provenance']))

# Formal fixed integer multiplicities, not selected character/matrix evaluations.
NAMES = ('1', 'W', 'A', 'S4', 'D', 'T6', 'V', 'P', 'Wp')
DIMS = (1, 2, 3, 4, 5, 6, 3, 4, 2)
W_PRODUCT = {
    '1': ('W',), 'W': ('1', 'A'), 'A': ('W', 'S4'),
    'S4': ('A', 'D'), 'D': ('S4', 'T6'), 'T6': ('D', 'V', 'P'),
    'V': ('T6',), 'P': ('T6', 'Wp'), 'Wp': ('P',),
}


def rep(**terms):
    return tuple(terms.get(name, 0) for name in NAMES)


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul_w(a):
    result = [0] * len(NAMES)
    for name, count in zip(NAMES, a):
        for target in W_PRODUCT[name]:
            result[NAMES.index(target)] += count
    return tuple(result)


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def dim(a):
    return sum(x * y for x, y in zip(a, DIMS))


for name, d in zip(NAMES, DIMS):
    check('fixed W product dimension ' + name, dim(mul_w(rep(**{name: 1}))) == 2 * d)
check('complete fixed irreducible dimension budget', sum(d * d for d in DIMS) == 120)
H = [rep(**{'1': 1}), rep(W=1)]
for n in range(2, 11):
    H.append(sub(mul_w(H[-1]), H[-2]))
    check('H_' + str(n) + ' dimension and multiplicities',
          dim(H[-1]) == n + 1 and all(m >= 0 for m in H[-1]))
expected = (
    rep(**{'1': 1}), rep(W=1), rep(A=1), rep(S4=1), rep(D=1), rep(T6=1),
    rep(V=1, P=1), rep(Wp=1, T6=1), rep(P=1, D=1), rep(S4=1, T6=1),
    rep(A=1, V=1, D=1),
)
check('exact H_0 through H_10', tuple(H) == expected)
check('quadratic evaluation Hom dimension', inner(rep(A=1), H[2]) == 1)
rank_one_degrees = (-4, -2, 0, 2)
check('rank-one degree bounds and parity', all(-4 <= a <= 3 and a % 2 == 0 for a in rank_one_degrees))
check('rank-one Hom multiplicities', tuple(inner(rep(W=1), H[3 - a]) for a in rank_one_degrees) == (0, 0, 0, 1))
check('rank-one surviving Euler-line degree', rank_one_degrees[-1] == 2)
m10 = rep(A=1, V=1, P=1)
common = tuple(min(x, y) for x, y in zip(H[10], m10))
check('hypothetical decic coefficient-span bound', common == rep(A=1, V=1) and dim(common) == 6)
check('rank-seven jets cannot fit coefficient-span bound', 7 > dim(common))
check('unbalanced defect-twelve top Hom vanishes', inner(rep(W=1), H[5]) == 0)
check('balanced physical W image Hom vanishes', inner(rep(**{'1': 1, 'A': 1}), H[6]) == 0)
check('Wp W product is P', mul_w(rep(Wp=1)) == rep(P=1))
check('actual V top is killed in Wp image type', inner(rep(V=1), mul_w(rep(Wp=1))) == 0)
check('V W product is T6', mul_w(rep(V=1)) == rep(T6=1))
check('M10 dimension', dim(m10) == 3 + 3 + 4 == 10)

# Only displayed small ranks and degrees. These do not certify actual-map rank.
check('E0 kernel rank and degree', (16 - 9, -46 - (-18)) == (7, -28))
check('D10 evaluation rank and degree', (11 - 1, -10) == (10, -10))
check('F10 first-jet evaluation rank and degree', (11 - 2, 9 * (-2)) == (9, -18))
check('D10 quotient and derivative degrees', -10 - (-18) == 8 and 8 - 2 == 6)
check('E19 quotient rank and degree', (19 - 16, -28 - (-46)) == (3, 18))
check('G9 kernel rank and degree', (19 - 10, -28 - (-10)) == (9, -18))
check('G9 G7 quotient rank and degree', (9 - 7, -18 - (-28)) == (2, 10))
check('Euler kernel rank and degree', (3 - 1, 3 * 6 - 8) == (2, 2 * 5))
check('derivative target degree', 2 * 5 - 2 * 2 == 2 * 3 == 6)
q = tuple(2 - 2 * i for i in range(7))
check('backward equality degree sum', q == (2, 0, -2, -4, -6, -8, -10) and sum(q) == -28)
check('positive defect weights', tuple(7 - i for i in range(1, 7)) == (6, 5, 4, 3, 2, 1))
for j in range(7):
    check('hypothetical intrinsic jet degree ' + str(j), sum(q[6 - j:]) == -(j + 1) * (10 - j))
check('rank-one terminal degree', q[-1] == -10)
check('rank-two H5 kernel rank', 7 - 2 == 5)
check('rank-two H5 degree formula constant', -28 - 6 == -34)
check('H5 subbundle degree bound', 5 * (-4) == -20 and -20 - (-34) == 14)
check('A5 possible cyclic stabilizer orbit sizes', tuple(60 // n for n in (1, 2, 3, 5)) == (60, 30, 20, 12))
check('only length twelve positive divisor at most fourteen', 12 <= 14 < 20 and 2 * 12 > 14)
check('defect-twelve image degree', 6 - 12 == -6)
check('two displayed defect-twelve degree lists', -2 - 4 == -3 - 3 == -6)
check('degree-list alternatives follow bounds', -4 <= -3 <= -2 and (-6) // 2 == -3)
check('forbidden horizontal block ordinary Hom degree', -6 - (-4) == -2 < 0)
check('forbidden horizontal block is negative', 3 * (-4) == -12 < 0)
check('G9 annihilator is negative line', (10 - 9, -(0 - (-18))) == (1, -18))

print(json.dumps({
    'status': 'PASS',
    'checker_is_not_proof': True,
    'checks_passed': len(CHECKS),
    'selected_core_files': len(CORE),
    'complete_direct_inputs': len(PINS),
    'maximum_symmetric_degree': 10,
    'frozen_sha256': sha256(frozen_bytes),
    'proof_sha256': sha256((ROOT / 'PROOF.md').read_bytes()),
    'checker_sha256': sha256((ROOT / 'verify.py').read_bytes()),
    'scope': 'Exact bytes and fixed small universal character/degree identities; no geometry or actual maps.',
    'checks': CHECKS,
}, indent=2, sort_keys=True))
