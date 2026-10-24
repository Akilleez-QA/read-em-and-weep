#!/usr/bin/env python3
"""Bounded integrity/arithmetic checks only. This checker is not a proof.

No network, polynomial coefficients, source instances, points, jets, tensors,
matrices, eigenlines, scalar normalizations, instance ranks, scans, or search.
Only four pinned input hashes, ten frozen file hashes, and fixed integer
representation multiplicities/rank/degree arithmetic are checked.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = (
    'PROOF.md', 'README.md', 'INPUTS.json', 'INPUTS.md', 'PROVENANCE.md',
    'verify.py', 'inputs/shared-d-gluing.md', 'inputs/f18-row-resolution.md',
    'inputs/first-kernel-span.md', 'inputs/first-kernel-forward-closure.md',
)
PINS = (
    (1207, 'inputs/shared-d-gluing.md', 20361,
     '7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7',
     '3d051410e80a33f1c4d78d3403bb186595bb72c3'),
    (1241, 'inputs/f18-row-resolution.md', 15616,
     'cd28b6dba69d23ef905f4816dcd1a7a3165bd8b337169ab0a6acb10a15ac06dc',
     '429c462fe6ba5f2b99770b9cabb35440130c807b'),
    (1235, 'inputs/first-kernel-span.md', 11977,
     '66f8040b87f3d193fbd7e6eecb42a1457a59aa6f2cf3f10f29e7ac7b1aa1b6c9',
     'b846834f8451e7202721d9669b43df294f7a96d3'),
    (1236, 'inputs/first-kernel-forward-closure.md', 18052,
     '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
     'f77cfb52743be86e46e0c40570ec036e69aebaf3'),
)
CHECKS = []


def check(name, condition):
    if not condition:
        raise SystemExit('FAIL: ' + name)
    CHECKS.append(name)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def blob_digest(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


# Read only the exact ten selected files and freeze manifest, never a directory scan.
frozen_bytes = (ROOT / 'FROZEN.json').read_bytes()
frozen = json.loads(frozen_bytes)
check('freeze schema', frozen['schema'] == 'f18-gluing-surjectivity-freeze-v1')
check('exact selected core', tuple(x['path'] for x in frozen['files']) == CORE)
for item in frozen['files']:
    data = (ROOT / item['path']).read_bytes()
    check('frozen bytes: ' + item['path'], len(data) == item['bytes'])
    check('frozen SHA256: ' + item['path'], digest(data) == item['sha256'])

inputs = json.loads((ROOT / 'INPUTS.json').read_bytes())
check('exactly four inputs', len(inputs['sources']) == 4)
for entry, pin in zip(inputs['sources'], PINS):
    pr, path, length, sha, blob = pin
    data = (ROOT / path).read_bytes()
    check('input identity PR' + str(pr), (entry['pr'], entry['local_path']) == (pr, path))
    check('input bytes PR' + str(pr), len(data) == entry['bytes'] == length)
    check('input SHA256 PR' + str(pr), digest(data) == entry['sha256'] == sha)
    check('input Git blob PR' + str(pr), blob_digest(data) == entry['git_blob_sha1'] == blob)
    check('two read methods PR' + str(pr), [x['method'] for x in entry['retrievals']] == [
        'mcp__codex_apps__github_fetch_file', 'mcp__codex_apps__github_fetch_blob'])
    for retrieval in entry['retrievals']:
        check('retrieval hash metadata PR' + str(pr),
              (retrieval['bytes'], retrieval['sha256'], retrieval['recomputed_git_blob_sha1'])
              == (length, sha, blob))

# The fixed physical W multiplication graph on the nine irreducible characters.
# These are formal integer multiplicities, never actual coefficient data.
NAMES = ('1', 'W', 'A', 'S4', 'D', 'T6', 'V', 'P', 'Wp')
DIMS = dict(zip(NAMES, (1, 2, 3, 4, 5, 6, 3, 4, 2)))
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


def mul_a(a):
    return sub(mul_w(mul_w(a)), a)


def inner(a, b):
    return sum(x * y for x, y in zip(a, b))


def dim(a):
    return sum(count * DIMS[name] for name, count in zip(NAMES, a))


for name in NAMES:
    check('fixed W product dimension ' + name, dim(mul_w(rep(**{name: 1}))) == 2 * DIMS[name])
H = [rep(**{'1': 1}), rep(W=1)]
for n in range(2, 9):
    H.append(sub(mul_w(H[-1]), H[-2]))
    check('fixed H' + str(n) + ' dimension', dim(H[-1]) == n + 1)
expected = (rep(A=1), rep(S4=1), rep(D=1), rep(T6=1), rep(V=1, P=1), rep(Wp=1, T6=1), rep(P=1, D=1))
check('H2 through H8 characters', tuple(H[2:]) == expected)
check('quartic coefficient identity', mul_a(H[4]) == add(H[6], H[4], H[2]))
check('A tensor H5', mul_a(H[5]) == add(H[7], H[5], H[3]) == rep(Wp=1, T6=2, S4=1))
check('Hom W to A tensor H5 vanishes', inner(H[1], mul_a(H[5])) == 0)
check('scalar into K top vanishes', inner(rep(V=1, P=1), H[2]) == 0)
check('scalar into K bottom vanishes', inner(rep(T6=1), H[1]) == 0)
check('unique D row', mul_w(rep(T6=1)) == rep(D=1, V=1, P=1) and inner(rep(D=1), mul_w(rep(T6=1))) == 1)
check('Ext O(-4), W(-9) vanishes', inner(H[1], H[3]) == 0)
check('constant restriction kernel type', sub(rep(A=2, V=2, D=1, P=1), rep(A=1, V=1, D=1)) == rep(A=1, V=1, P=1))
check('constant restriction kernel dimension', dim(rep(A=1, V=1, P=1)) == 10)

# Fixed rank/degree arithmetic only, not instance-rank computation.
E0 = (5 + 2 + 6 + 3, -2 * 5 - 3 * (2 + 6) - 4 * 3)
F18 = (5 + 2 + 6, -2 * 5 - 3 * (2 + 6))
T = (3, -4 * 3)
F10 = (4 + 5, -2 * (4 + 5))
Q = (6, -6)
D_TOP = (5, -10)
R8 = (2 + 6, -3 * (2 + 6))
O4 = (1, 4)
minus = lambda a, b: tuple(x - y for x, y in zip(a, b))
check('E0 and F18 gluing arithmetic', E0 == (16, -46) and F18 == (13, -34) and minus(E0, T) == F18)
check('F10 and Q gluing arithmetic', F10 == (9, -18) and minus(F10, T) == Q)
check('saturated D quotient arithmetic', minus(Q, D_TOP) == O4)
check('canonical kernel arithmetic three ways', minus(E0, F10) == minus(F18, Q) == minus(R8, O4) == (7, -28))
check('annihilator extension arithmetic', (2 + 1, 2 * -9 - 4) == (3, -22))
check('ordinary degree obstruction D to T', -4 - (-2) < 0)
check('ordinary S0 Hom obstructions', all(d - (-4) < 0 for d in (-10, -18, -6)))
check('quotient-row degree below invariant minimum', 4 - (-3) == 7 and 7 < 12)

print(json.dumps({
    'status': 'PASS',
    'checker_is_not_proof': True,
    'checks_passed': len(CHECKS),
    'selected_core_files': len(CORE),
    'complete_direct_inputs': len(PINS),
    'maximum_symmetric_degree': 8,
    'frozen_sha256': digest(frozen_bytes),
    'proof_sha256': digest((ROOT / 'PROOF.md').read_bytes()),
    'checker_sha256': digest((ROOT / 'verify.py').read_bytes()),
    'scope': 'Exact hashes and fixed small character/rank/degree identities only.',
}, indent=2, sort_keys=True))
