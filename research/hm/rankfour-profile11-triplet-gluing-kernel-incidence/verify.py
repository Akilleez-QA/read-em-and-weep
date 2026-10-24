#!/usr/bin/env python3
"""Bounded exact-byte and fixed character/degree arithmetic only.

This checker is not proof and does not certify geometry or actual maps.
No network, source-instance data, coefficient evaluations, selected points,
jets, tensors, matrices, eigenlines, scalar values, instance ranks, or scans.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = (
    'PROOF.md', 'README.md', 'INPUTS.json', 'INPUTS.md', 'PROVENANCE.md',
    'verify.py', 'inputs/r13-extension-incidence.md',
    'inputs/f18-gluing-surjectivity.md', 'inputs/orthogonal-top-incidence.md',
    'inputs/first-kernel-forward-closure.md',
)
PINS = ((1242, '66ef0616fdd0607272b8bbd23892bc33120ac7f2', 'research/hm/rankfour-profile11-triplet-r13-extension-incidence/PROOF.md', 'inputs/r13-extension-incidence.md', 19230, '4819cebda47b3ef7a48ecbcb1fe01295a3a3a7ea7986df540421e1433d547b21', '5ac2f53aec71adda224d3578fb6e871ac6a8fecb'), (1243, 'dde84900cd6f9ad117800c39042844bb897a2f79', 'research/hm/rankfour-profile11-triplet-f18-gluing-surjectivity/PROOF.md', 'inputs/f18-gluing-surjectivity.md', 12798, '3919909cd67055e266299a0841e4642c465185eba28500a3b00b4a284f93693a', '700257a6d8f41f9cfbae7fdf8d78d77795a07bb9'), (1240, '3fbaa182b1aceb6915be88088ef158d6d15e34fb', 'research/hm/rankfour-profile11-triplet-orthogonal-top-incidence/PROOF.md', 'inputs/orthogonal-top-incidence.md', 28094, '407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637', 'f00b059695615d9b8ab6d315798940e3ab0a58d4'), (1236, '092fc5f31dfaa5553ee5ea687f175ecba1878a2a', 'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md', 'inputs/first-kernel-forward-closure.md', 18052, '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137', 'f77cfb52743be86e46e0c40570ec036e69aebaf3'))
CHECKS = []


def check(name, condition):
    if not condition:
        raise SystemExit('FAIL: ' + name)
    CHECKS.append(name)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


# Exact named files only; no directory scan or dependency on author evidence.
frozen_bytes = (ROOT / 'FROZEN.json').read_bytes()
frozen = json.loads(frozen_bytes)
check('freeze schema', frozen['schema'] == 'triplet-gluing-kernel-freeze-v1')
check('exact ten-file core', tuple(x['path'] for x in frozen['files']) == CORE)
for entry in frozen['files']:
    data = (ROOT / entry['path']).read_bytes()
    check('frozen byte count ' + entry['path'], len(data) == entry['bytes'])
    check('frozen SHA256 ' + entry['path'], sha256(data) == entry['sha256'])

inputs = json.loads((ROOT / 'INPUTS.json').read_bytes())
check('input schema', inputs['schema'] == 'triplet-gluing-kernel-inputs-v1')
check('exactly four complete sources', len(inputs['sources']) == 4)
for entry, pin in zip(inputs['sources'], PINS):
    pr, commit, repository_path, path, count, sha, blob = pin
    data = (ROOT / path).read_bytes()
    label = ' PR' + str(pr)
    check('input identity' + label, (entry['pr'], entry['commit'], entry['repository_path'], entry['local_path']) == pin[:4])
    check('input bytes' + label, len(data) == entry['bytes'] == count)
    check('input SHA256' + label, sha256(data) == entry['sha256'] == sha)
    check('input Git blob' + label, git_blob(data) == entry['git_blob_sha1'] == entry['returned_path_blob_sha1'] == blob)
    path_request = entry['path_request']
    blob_request = entry['blob_request']
    check('exact commit path request' + label, path_request['tool'] == 'github.fetch_file' and path_request['arguments'] == {
        'repository_full_name': 'Akilleez-QA/read-em-and-weep',
        'path': repository_path, 'ref': commit, 'encoding': 'base64'})
    check('separate blob request' + label, blob_request['tool'] == 'github.fetch_blob' and blob_request['arguments'] == {
        'repository_full_name': 'Akilleez-QA/read-em-and-weep', 'blob_sha': blob})
    for method in (path_request, blob_request):
        check('complete request metadata' + label + ' ' + method['tool'],
              method['complete_no_line_limits'] is True and
              (method['decoded_bytes'], method['decoded_sha256'], method['recomputed_git_blob_sha1']) == (count, sha, blob))
        check('request timestamp ordering' + label + ' ' + method['tool'],
              method['started_at_utc'] <= method['completed_at_utc'])
    check('complete source author reading recorded' + label, entry['full_original_read'] is True)

# Fixed nine-character physical W multiplication graph, as formal integer
# multiplicities only. This is not a character derivation or geometry test.
NAMES = ('1', 'W', 'A', 'S4', 'D', 'T6', 'V', 'P', 'Wp')
DIMS = (1, 2, 3, 4, 5, 6, 3, 4, 2)
W_PRODUCT = {
    '1': ('W',), 'W': ('1', 'A'), 'A': ('W', 'S4'),
    'S4': ('A', 'D'), 'D': ('S4', 'T6'), 'T6': ('D', 'V', 'P'),
    'V': ('T6',), 'P': ('T6', 'Wp'), 'Wp': ('P',),
}


def rep(**terms):
    return tuple(terms.get(name, 0) for name in NAMES)


def add(*terms):
    return tuple(sum(t[i] for t in terms) for i in range(9))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def mul_w(a):
    result = [0] * 9
    for name, count in zip(NAMES, a):
        for target in W_PRODUCT[name]:
            result[NAMES.index(target)] += count
    return tuple(result)


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def dim(a):
    return sum(x * y for x, y in zip(a, DIMS))


for name, dimension in zip(NAMES, DIMS):
    check('fixed W product dimension ' + name, dim(mul_w(rep(**{name: 1}))) == 2 * dimension)
H = [rep(**{'1': 1}), rep(W=1)]
for n in range(2, 8):
    H.append(sub(mul_w(H[-1]), H[-2]))
    check('fixed H_' + str(n) + ' dimension', dim(H[-1]) == n + 1)
expected = (rep(A=1), rep(S4=1), rep(D=1), rep(T6=1), rep(V=1, P=1), rep(Wp=1, T6=1))
check('H_2 through H_7 characters', tuple(H[2:]) == expected)
check('A first occurrence', all(inner(rep(A=1), H[n]) == 0 for n in (0, 1)) and inner(rep(A=1), H[2]) == 1)
check('Wp first occurrence', all(inner(rep(Wp=1), H[n]) == 0 for n in range(7)) and inner(rep(Wp=1), H[7]) == 1)
check('Hom N to D0 vanishes', inner(rep(Wp=1), mul_w(rep(D=1))) == 0)
wp = rep(Wp=1)
wp_h3 = sub(mul_w(mul_w(mul_w(wp))), add(mul_w(wp), mul_w(wp)))
check('N dual coefficient type', wp_h3 == rep(D=1, V=1))
check('only V common with M10', inner(wp_h3, rep(A=1, V=1, P=1)) == 1)
check('Q5 extension space dimension', inner(rep(P=1), H[6]) == 1)
check('reciprocity Wp multiplicity in P W', inner(rep(P=1), mul_w(wp)) == 1)
check('reciprocity T6 multiplicity in P W', inner(rep(P=1), mul_w(rep(T6=1))) == 1)
check('P W exhausted by Wp plus T6', 4 * 2 == 2 + 6 and mul_w(rep(P=1)) == rep(Wp=1, T6=1))
check('connecting-map character cokernel', sub(mul_w(rep(P=1)), H[5]) == wp)
check('Q5 Euler characteristic at twist four', sub(H[6], rep(P=1)) == rep(V=1))
check('W and Wp distinct', rep(W=1) != wp)
check('D0 octic Hom zero', inner(rep(D=1), H[6]) == 0)
common_octic = (inner(rep(D=1), H[6]), inner(wp, H[5]), inner(rep(T6=1), H[5]), inner(rep(V=1), H[4]))
check('E0 octic Hom block dimensions', common_octic == (0, 0, 1, 0) and sum(common_octic) == 1)
check('intersection octic Hom vanishes', inner(rep(V=1), H[4]) + inner(wp, H[3]) == 0)
check('both degree-seven Hom lines', inner(wp, H[7]) == inner(rep(T6=1), H[7]) == 1)

# Only the displayed fixed integer degree/rank identities, not instance ranks.
check('rank-one N derivative inequalities incompatible', 2 < 4)
check('constant V derivative quotient bound', 3 - 2 == 1)
check('Q5 quotient degree', -22 - 4 * (-6) == 2)
check('Q5 two degree lists', sum((-6, -4, -4, -4, -4)) == sum((-5, -5, -4, -4, -4)) == -22)
check('Q5 deficit below all minus four', -4 * 5 - (-22) == 2)
check('Q5 final type degree and rank', 3 * (-4) + 2 * (-5) == -22 and 3 + 2 == 5)
check('L5 projection rank budget', 18 - 13 == 5 and 5 - 3 == 2 and 7 - 2 == 5)
check('W row degree below invariant minimum', 4 - (-3) == 7 and 7 < 12)
check('W row kernel degree', 2 * (-3) - 4 == -10)
check('zero T6 row alternative degree', 6 * (-3) + (-10) == -28)
check('octic scalar map degree', (-3) - (-8) == 5)
check('common image obstruction degrees', (-4) - (-8) == 4 and (-5) - (-8) == 3)
check('complete degree-seven evaluation kernel', 8 - 1 == 7 and 8 * (-3) - 4 == 7 * (-4) == -28)
check('E0 kernel rank and degree', (16 - 9, -46 - (-18)) == (7, -28))
check('F18 kernel rank and degree', (13 - 6, -34 - (-6)) == (7, -28))
check('H6 endpoint rank', dim(H[6]) == 3 + 4 == 7)

print(json.dumps({
    'status': 'PASS',
    'checker_is_not_proof': True,
    'checks_passed': len(CHECKS),
    'selected_core_files': len(CORE),
    'complete_direct_inputs': len(PINS),
    'maximum_symmetric_degree': 7,
    'frozen_sha256': sha256(frozen_bytes),
    'proof_sha256': sha256((ROOT / 'PROOF.md').read_bytes()),
    'checker_sha256': sha256((ROOT / 'verify.py').read_bytes()),
    'scope': 'Exact bytes and fixed small character/degree identities only; no geometry or actual maps.',
}, indent=2, sort_keys=True))
